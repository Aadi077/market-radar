"""Daily insider-trading and market snapshot.

- Insider trades: open-market purchases (P) and sales (S) parsed from SEC EDGAR Form 4 filings.
- Market: index, sector ETF, and large-cap closes from Yahoo Finance's chart endpoint.
- Sundays: a weekly recap built from the week's saved data.

Stdlib only. Pass --commit to create one git commit per update.
"""

import argparse
import json
import os
import re
import subprocess
import sys
import threading
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from datetime import date, datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
CHARTS = ROOT / "charts"
NY = ZoneInfo("America/New_York")

SEC_USER_AGENT = os.environ.get("SEC_USER_AGENT", "")
LOOKBACK_DAYS = int(os.environ.get("LOOKBACK_DAYS", "7"))
MAX_FILINGS = int(os.environ.get("MAX_FILINGS", "0"))  # 0 = no limit; handy for local testing

INDICES = {"SPY": "S&P 500", "QQQ": "Nasdaq 100", "DIA": "Dow 30", "IWM": "Russell 2000"}
SECTORS = {
    "XLK": "Technology", "XLC": "Communication Services", "XLY": "Consumer Discretionary",
    "XLF": "Financials", "XLV": "Health Care", "XLI": "Industrials", "XLE": "Energy",
    "XLP": "Consumer Staples", "XLB": "Materials", "XLU": "Utilities", "XLRE": "Real Estate",
}
LARGE_CAPS = [
    "AAPL", "MSFT", "NVDA", "GOOGL", "AMZN", "META", "AVGO", "TSLA", "BRK-B", "JPM",
    "LLY", "V", "UNH", "XOM", "MA", "COST", "HD", "PG", "JNJ", "WMT",
    "NFLX", "ORCL", "BAC", "ABBV", "CRM", "AMD", "KO", "CVX", "MRK", "PEP",
    "ADBE", "TMO", "CSCO", "MCD", "WFC", "PLTR", "IBM", "GE", "INTC", "DIS",
]

DISCLAIMER = "_Informational only, not investment advice. Data: SEC EDGAR (Form 4) and Yahoo Finance; may contain errors or delays._"


# ---------------------------------------------------------------- HTTP

class RateLimiter:
    def __init__(self, per_second):
        self.interval = 1 / per_second
        self.lock = threading.Lock()
        self.next_slot = 0.0

    def wait(self):
        with self.lock:
            now = time.monotonic()
            delay = self.next_slot - now
            self.next_slot = max(now, self.next_slot) + self.interval
        if delay > 0:
            time.sleep(delay)


sec_limiter = RateLimiter(8)  # SEC fair-access limit is 10 requests/second


def http_get(url, headers, retries=3):
    """Return the response body, or None on 404."""
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=30) as resp:
                return resp.read()
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            if attempt == retries - 1 or e.code not in (429, 500, 502, 503, 504):
                raise
        except (urllib.error.URLError, TimeoutError):
            if attempt == retries - 1:
                raise
        time.sleep(2 ** (attempt + 1))


def sec_get(url):
    sec_limiter.wait()
    return http_get(url, {"User-Agent": SEC_USER_AGENT})


# ---------------------------------------------------------------- Insider trades

def text(node, path):
    el = node.find(path)
    return el.text.strip() if el is not None and el.text else None


def is_true(value):
    return (value or "").lower() in ("1", "true")


def form4_filings(day):
    """Map accession number -> archive path for every Form 4 filed on `day`, or None if no index exists."""
    qtr = (day.month - 1) // 3 + 1
    raw = sec_get(f"https://www.sec.gov/Archives/edgar/daily-index/{day.year}/QTR{qtr}/form.{day:%Y%m%d}.idx")
    if raw is None:
        return None
    filings = {}
    for line in raw.decode("latin-1").splitlines():
        if not line.startswith("4 "):
            continue
        m = re.search(r"(edgar/data/\d+/(\d{10}-\d{2}-\d{6})\.txt)\s*$", line)
        if m:
            filings.setdefault(m.group(2), m.group(1))
    return filings


def parse_form4(accession, path):
    raw = sec_get("https://www.sec.gov/Archives/" + path)
    m = raw and re.search(rb"<XML>\s*(.*?)\s*</XML>", raw, re.S)
    if not m:
        return []
    doc = ET.fromstring(m.group(1))

    owners, roles = [], []
    for owner in doc.findall("reportingOwner"):
        if name := text(owner, "reportingOwnerId/rptOwnerName"):
            owners.append(name)
        rel = owner.find("reportingOwnerRelationship")
        if rel is None:
            continue
        if is_true(text(rel, "isOfficer")):
            roles.append(text(rel, "officerTitle") or "Officer")
        if is_true(text(rel, "isDirector")):
            roles.append("Director")
        if is_true(text(rel, "isTenPercentOwner")):
            roles.append("10% Owner")

    totals = {}
    for t in doc.findall("nonDerivativeTable/nonDerivativeTransaction"):
        code = text(t, "transactionCoding/transactionCode")
        if code not in ("P", "S"):
            continue
        try:
            shares = float(text(t, "transactionAmounts/transactionShares/value"))
            price = float(text(t, "transactionAmounts/transactionPricePerShare/value"))
        except (TypeError, ValueError):
            continue
        if shares <= 0 or price <= 0:
            continue
        agg = totals.setdefault(code, {"shares": 0.0, "value": 0.0, "dates": set()})
        agg["shares"] += shares
        agg["value"] += shares * price
        if d := text(t, "transactionDate/value"):
            agg["dates"].add(d[:10])

    ticker = (text(doc, "issuer/issuerTradingSymbol") or "").upper()
    cik = path.split("/")[2]
    url = f"https://www.sec.gov/Archives/edgar/data/{cik}/{accession.replace('-', '')}/{accession}-index.htm"
    return [
        {
            "type": "buy" if code == "P" else "sell",
            "issuer": text(doc, "issuer/issuerName") or "",
            "ticker": "" if ticker in ("NONE", "N/A", "NA") else ticker,
            "insiders": owners,
            "roles": list(dict.fromkeys(roles)),
            "shares": round(agg["shares"]),
            "avg_price": round(agg["value"] / agg["shares"], 2),
            "value": round(agg["value"]),
            "transaction_dates": sorted(agg["dates"]),
            "accession": accession,
            "url": url,
        }
        for code, agg in totals.items()
    ]


def insider_path(day, ext="json"):
    return DATA / "insider" / f"{day:%Y}" / f"{day:%m}" / f"{day}.{ext}"


def update_insider(day):
    filings = form4_filings(day)
    if filings is None:
        print(f"insider: no EDGAR index for {day} (holiday or not published yet)")
        return None
    items = list(filings.items())[: MAX_FILINGS or None]

    failures = 0

    def safe_parse(item):
        nonlocal failures
        try:
            return parse_form4(*item)
        except Exception as e:  # one bad filing shouldn't sink the day
            failures += 1
            print(f"  warning: {item[0]}: {e}", file=sys.stderr)
            return []

    with ThreadPoolExecutor(max_workers=10) as pool:
        trades = [t for result in pool.map(safe_parse, items) for t in result]
    if items and failures / len(items) > 0.2:
        raise RuntimeError(f"{failures}/{len(items)} Form 4 filings failed for {day}; not saving partial data")

    # The same trade is sometimes filed twice under different accession numbers.
    unique = {}
    for t in trades:
        key = (t["type"], t["ticker"] or t["issuer"], tuple(t["insiders"]), t["shares"], t["avg_price"], tuple(t["transaction_dates"]))
        unique.setdefault(key, t)
    trades = sorted(unique.values(), key=lambda t: t["value"], reverse=True)
    buys = [t for t in trades if t["type"] == "buy"]
    sells = [t for t in trades if t["type"] == "sell"]
    json_path = insider_path(day)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps({"filing_date": str(day), "form4_count": len(filings), "trades": trades}, indent=1) + "\n")
    insider_path(day, "md").write_text(
        f"# Insider trades filed {day}\n\n"
        f"{len(filings):,} Form 4 filings · {len(buys):,} open-market buys · {len(sells):,} open-market sales\n\n"
        f"## Biggest buys\n\n{trades_table(buys[:25])}\n\n## Biggest sales\n\n{trades_table(sells[:25])}\n\n{DISCLAIMER}\n"
    )
    print(f"insider: {day}: {len(filings)} filings, {len(buys)} buys, {len(sells)} sells")
    return [json_path, insider_path(day, "md")], f"insider: Form 4 trades filed {day}"


def fmt_money(v):
    for unit, size in (("B", 1e9), ("M", 1e6), ("K", 1e3)):
        if abs(v) >= size:
            return f"${v / size:.1f}{unit}"
    return f"${v:,.0f}"


def cell(s):
    return s.replace("|", "\\|")


def trades_table(trades):
    if not trades:
        return "_None._"
    rows = ["| Company | Insider | Role | Value | Shares | Avg price | Filing |", "|---|---|---|---:|---:|---:|---|"]
    for t in trades:
        company = f"**{t['ticker']}** {t['issuer']}" if t["ticker"] else t["issuer"]
        rows.append(
            f"| {cell(company)} | {cell(', '.join(t['insiders']))} | {cell(', '.join(t['roles']))} | "
            f"{fmt_money(t['value'])} | {t['shares']:,} | ${t['avg_price']:,.2f} | [Form 4]({t['url']}) |"
        )
    return "\n".join(rows)


# ---------------------------------------------------------------- Market

def yahoo_daily(symbol):
    """List of (date, close) daily bars for the last ~2 weeks."""
    raw = http_get(
        f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}?range=15d&interval=1d",
        {"User-Agent": "Mozilla/5.0"},
    )
    if raw is None:
        return []
    result = json.loads(raw)["chart"]["result"][0]
    closes = result["indicators"]["quote"][0]["close"]
    bars = {}
    for ts, close in zip(result.get("timestamp", []), closes):
        if close is not None:
            bars[datetime.fromtimestamp(ts, NY).date()] = close
    return sorted(bars.items())


def market_path(day):
    return DATA / "market" / f"{day:%Y}" / f"{day:%m}" / f"{day}.json"


def update_market(now):
    bars = {}
    for symbol in [*INDICES, *SECTORS, *LARGE_CAPS]:
        try:
            if len(b := yahoo_daily(symbol)) >= 2:
                bars[symbol] = b
        except Exception as e:
            print(f"  warning: {symbol}: {e}", file=sys.stderr)
        time.sleep(0.3)
    if "SPY" not in bars:
        raise RuntimeError("market: no SPY data from Yahoo Finance")

    session = bars["SPY"][-1][0]
    if session == now.date() and (now.hour, now.minute) < (16, 30):
        print("market: today's session hasn't closed yet; skipping")
        return None
    if market_path(session).exists():
        print(f"market: {session} already recorded")
        return None

    quotes = {}
    for symbol, b in bars.items():
        closes = dict(b)
        prior = [d for d, _ in b if d < session]
        if session in closes and prior:
            prev = closes[prior[-1]]
            quotes[symbol] = {"close": round(closes[session], 2), "prev_close": round(prev, 2),
                              "change_pct": round((closes[session] / prev - 1) * 100, 2)}

    path = market_path(session)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps({"session": str(session), "quotes": quotes}, indent=1) + "\n")
    CHARTS.mkdir(exist_ok=True)
    sectors = {SECTORS[s]: q["change_pct"] for s, q in quotes.items() if s in SECTORS}
    (CHARTS / "sectors-daily.svg").write_text(bar_chart(f"Sector performance · {session}", sectors))
    print(f"market: recorded {session} ({len(quotes)} symbols)")
    return [path, CHARTS / "sectors-daily.svg"], f"market: closing snapshot for {session}"


def bar_chart(title, values):
    """Horizontal diverging bar chart as a standalone SVG."""
    items = sorted(values.items(), key=lambda kv: kv[1], reverse=True)
    width, label_w, row_h, top = 640, 190, 26, 44
    height = top + row_h * len(items) + 16
    max_abs = max((abs(v) for _, v in items), default=1) or 1
    plot_w = width - label_w - 70
    zero_x = label_w + plot_w / 2
    scale = (plot_w / 2) / max_abs
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" '
        'font-family="-apple-system,Segoe UI,Helvetica,Arial,sans-serif" font-size="13">',
        f'<text x="16" y="26" font-size="15" font-weight="600" fill="#8b949e">{title}</text>',
        f'<line x1="{zero_x}" y1="{top - 6}" x2="{zero_x}" y2="{height - 12}" stroke="#8b949e" stroke-opacity="0.5"/>',
    ]
    for i, (label, v) in enumerate(items):
        y = top + i * row_h
        w = max(abs(v) * scale, 1)
        x = zero_x if v >= 0 else zero_x - w
        color = "#2da44e" if v >= 0 else "#cf222e"
        value_x = zero_x + w + 6 if v >= 0 else zero_x - w - 6
        anchor = "start" if v >= 0 else "end"
        parts += [
            f'<text x="{label_w - 10}" y="{y + 16}" text-anchor="end" fill="#8b949e">{label}</text>',
            f'<rect x="{x:.1f}" y="{y + 4}" width="{w:.1f}" height="{row_h - 8}" rx="3" fill="{color}"/>',
            f'<text x="{value_x:.1f}" y="{y + 16}" text-anchor="{anchor}" fill="#8b949e">{v:+.2f}%</text>',
        ]
    parts.append("</svg>\n")
    return "\n".join(parts)


# ---------------------------------------------------------------- Weekly recap

def load_json(path):
    return json.loads(path.read_text()) if path.exists() else None


def update_weekly(today):
    if today.weekday() != 6:
        return None
    week_days = [today - timedelta(days=6 - i) for i in range(5)]  # Mon..Fri
    year, week, _ = week_days[-1].isocalendar()
    path = DATA / "weekly" / f"{year}-W{week:02d}.md"
    if path.exists():
        return None

    trades = [t for d in week_days if (j := load_json(insider_path(d))) for t in j["trades"]]
    sessions = [j for d in week_days if (j := load_json(market_path(d)))]
    if not trades and not sessions:
        print("weekly: no data for this week")
        return None

    buys = sorted((t for t in trades if t["type"] == "buy"), key=lambda t: t["value"], reverse=True)
    clusters = defaultdict(lambda: {"insiders": set(), "value": 0, "issuer": ""})
    for t in buys:
        c = clusters[t["ticker"] or t["issuer"]]
        c["insiders"].update(t["insiders"])
        c["value"] += t["value"]
        c["issuer"] = t["issuer"]
    cluster_rows = sorted(((k, c) for k, c in clusters.items() if len(c["insiders"]) >= 2),
                          key=lambda kc: (len(kc[1]["insiders"]), kc[1]["value"]), reverse=True)[:15]

    sections = [f"# Weekly recap · {week_days[0]} to {week_days[-1]}"]
    files = [path]
    if sessions:
        first, last = sessions[0]["quotes"], sessions[-1]["quotes"]
        weekly = {s: round((last[s]["close"] / first[s]["prev_close"] - 1) * 100, 2)
                  for s in last if s in first}
        rows = ["| Index | Week change |", "|---|---:|"]
        rows += [f"| {INDICES[s]} ({s}) | {weekly[s]:+.2f}% |" for s in INDICES if s in weekly]
        chart = CHARTS / f"sectors-{year}-W{week:02d}.svg"
        CHARTS.mkdir(exist_ok=True)
        chart.write_text(bar_chart(f"Sector performance · week of {week_days[0]}",
                                   {SECTORS[s]: v for s, v in weekly.items() if s in SECTORS}))
        files.append(chart)
        sections.append(f"## Market\n\n" + "\n".join(rows) + f"\n\n![Sectors](../../charts/{chart.name})")
    sections.append(f"## Biggest insider buys this week\n\n{trades_table(buys[:15])}")
    if cluster_rows:
        rows = ["| Company | Insiders buying | Total value |", "|---|---:|---:|"]
        rows += [f"| {cell(k if k == c['issuer'] else f'**{k}** ' + c['issuer'])} | {len(c['insiders'])} | {fmt_money(c['value'])} |"
                 for k, c in cluster_rows]
        sections.append("## Cluster buys\n\nCompanies where two or more insiders bought shares this week.\n\n" + "\n".join(rows))
    sections.append(DISCLAIMER)

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n\n".join(sections) + "\n")
    print(f"weekly: wrote {path.name}")
    return files, f"weekly: recap for {year}-W{week:02d}"


# ---------------------------------------------------------------- README

def latest(pattern):
    files = sorted(DATA.glob(pattern))
    return files[-1] if files else None


def write_readme(today):
    parts = [
        "# 📊 Market Radar\n",
        "A daily, automatically updated record of **insider trading** (SEC Form 4 open-market buys and sales) "
        "and **US market performance**, with a weekly recap every Sunday. Collected by GitHub Actions.\n",
        f"**Last updated:** {today}\n",
    ]

    if m := latest("market/*/*/*.json"):
        snap = json.loads(m.read_text())
        q = snap["quotes"]
        rows = ["| Index | Close | Change |", "|---|---:|---:|"]
        rows += [f"| {name} ({s}) | {q[s]['close']:,.2f} | {q[s]['change_pct']:+.2f}% |" for s, name in INDICES.items() if s in q]
        movers = sorted((s for s in LARGE_CAPS if s in q), key=lambda s: q[s]["change_pct"])
        mover_line = lambda syms: " · ".join(f"**{s}** {q[s]['change_pct']:+.2f}%" for s in syms)
        parts.append(
            f"## Market close · {snap['session']}\n\n" + "\n".join(rows) + "\n\n"
            "![Sector performance](charts/sectors-daily.svg)\n\n"
            f"**Top large-cap gainers:** {mover_line(movers[::-1][:5])}  \n"
            f"**Top large-cap decliners:** {mover_line(movers[:5])}\n"
        )

    if i := latest("insider/*/*/*.json"):
        snap = json.loads(i.read_text())
        buys = [t for t in snap["trades"] if t["type"] == "buy"]
        sells = [t for t in snap["trades"] if t["type"] == "sell"]
        parts.append(
            f"## Biggest insider buys · filed {snap['filing_date']}\n\n{trades_table(buys[:10])}\n\n"
            f"## Biggest insider sales · filed {snap['filing_date']}\n\n{trades_table(sells[:5])}\n\n"
            f"Full list: [`{i.with_suffix('.md').relative_to(ROOT)}`]({i.with_suffix('.md').relative_to(ROOT)})\n"
        )

    if w := latest("weekly/*.md"):
        parts.append(f"## Latest weekly recap\n\n[{w.stem}]({w.relative_to(ROOT)})\n")

    parts.append(
        "## How it works\n\n"
        "- [`scripts/update.py`](scripts/update.py) (Python stdlib only) runs daily via "
        "[`.github/workflows/daily.yml`](.github/workflows/daily.yml).\n"
        "- **Insider trades:** reads SEC EDGAR's daily index, parses every Form 4, and keeps open-market "
        "purchases (code `P`) and sales (code `S`).\n"
        "- **Market:** closing prices for major index ETFs, the 11 S&P sector ETFs, and 40 large-cap stocks.\n"
        "- **Weekly recap:** every Sunday, including cluster buys (multiple insiders buying the same company).\n"
        "- Raw JSON lives in [`data/`](data) for anyone who wants to analyze it.\n\n"
        f"{DISCLAIMER}\n"
    )
    (ROOT / "README.md").write_text("\n".join(parts))


# ---------------------------------------------------------------- Main

def git_commit(paths, message):
    subprocess.run(["git", "add", "--", *map(str, paths)], cwd=ROOT, check=True)
    if subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=ROOT).returncode:
        subprocess.run(["git", "commit", "-q", "-m", message], cwd=ROOT, check=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--commit", action="store_true", help="commit each update to git")
    args = parser.parse_args()

    now = datetime.now(NY)
    today = now.date()
    updates, errors = [], []

    def attempt(fn, *fn_args):
        try:
            if result := fn(*fn_args):
                updates.append(result)
        except Exception as e:
            errors.append(f"{fn.__name__}: {e}")
            print(f"error: {fn.__name__}: {e}", file=sys.stderr)

    if SEC_USER_AGENT:
        for offset in range(LOOKBACK_DAYS, 0, -1):
            day = today - timedelta(days=offset)
            if day.weekday() < 5 and not insider_path(day).exists():
                attempt(update_insider, day)
    else:
        errors.append("SEC_USER_AGENT is not set; skipping insider trades")
    attempt(update_market, now)
    attempt(update_weekly, today)
    write_readme(today)

    if args.commit:
        for paths, message in updates:
            git_commit(paths, message)
        git_commit([ROOT / "README.md"], f"docs: refresh README for {today}")

    for e in errors:
        print(f"::warning::{e}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
