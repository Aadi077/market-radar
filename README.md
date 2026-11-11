# 📊 Market Radar

An automatically updated record of **insider trading** (SEC Form 4 open-market buys and sales) and **US market performance**, updated every weekday with a recap each Monday. Collected by GitHub Actions.

**Last updated:** 2026-11-10

## Market close · 2026-11-10

| Index | Close | Change |
|---|---:|---:|
| S&P 500 (SPY) | 749.92 | -0.37% |
| Nasdaq 100 (QQQ) | 674.76 | -0.68% |
| Dow 30 (DIA) | 521.73 | -0.31% |
| Russell 2000 (IWM) | 280.58 | -0.68% |

![Sector performance](charts/sectors-daily.svg)

**Top large-cap gainers:** **AVGO** +3.91% · **UNH** +1.89% · **AMZN** +1.48% · **LLY** +1.44% · **BRK-B** +1.41%  
**Top large-cap decliners:** **NVDA** -5.47% · **MSFT** -2.20% · **INTC** -2.09% · **ORCL** -1.51% · **NFLX** -1.08%

## Biggest insider buys · filed 2026-11-09

| Company | Insider | Role | Value | Shares | Avg price | Filing |
|---|---|---|---:|---:|---:|---|
| **NFRX** 2023 ETF Series Trust | Harrison Street Real Assets Fund LLC | 10% Owner | $45.2M | 1,712,121 | $26.40 | [Form 4](https://www.sec.gov/Archives/edgar/data/1969674/000168789826000010/0001687898-26-000010-index.htm) |
| Keenova Therapeutics plc | GOLDENTREE ASSET MANAGEMENT LP, GoldenTree Asset Management LLC, Tananbaum Steven A. | 10% Owner | $26.4M | 295,716 | $89.25 | [Form 4](https://www.sec.gov/Archives/edgar/data/1278951/000149315226050818/0001493152-26-050818-index.htm) |
| **LRN** Stride, Inc. | Haggart Dylan G., Fivespan Partners, LP, Fivespan Partners GP, LLC | Director | $8.1M | 108,273 | $74.83 | [Form 4](https://www.sec.gov/Archives/edgar/data/2162829/000121390026117633/0001213900-26-117633-index.htm) |
| **NATR** NATURES SUNSHINE PRODUCTS INC | PRESCOTT GROUP CAPITAL MANAGEMENT, L.L.C., PRESCOTT GROUP AGGRESSIVE SMALL CAP LP, PRESCOTT GROUP AGGRESSIVE SMALL CAP II LP, PRESCOTT GROUP AGGRESSIVE SMALL CAP MASTER FUND GP, FROHLICH PHIL | 10% Owner | $2.8M | 291,666 | $9.77 | [Form 4](https://www.sec.gov/Archives/edgar/data/1127429/000116615226000014/0001166152-26-000014-index.htm) |
| **ROK** ROCKWELL AUTOMATION, INC | Moret Blake D. | President and CEO, Director | $1.5M | 4,000 | $386.36 | [Form 4](https://www.sec.gov/Archives/edgar/data/1515154/000151515426000003/0001515154-26-000003-index.htm) |
| **PAM** Pampa Energy Inc. | Mindlin Damian Miguel | Vicepresident | $1.3M | 20,000 | $64.37 | [Form 4](https://www.sec.gov/Archives/edgar/data/2028916/000202891626000013/0002028916-26-000013-index.htm) |
| **VDTA** Vertical Data Inc. | Hamble International Inc., Koverko Trevor | 10% Owner | $999.9K | 333,294 | $3.00 | [Form 4](https://www.sec.gov/Archives/edgar/data/2145730/000214573026000006/0002145730-26-000006-index.htm) |
| **NLY** ANNALY CAPITAL MANAGEMENT INC | Wede Scott | Director | $940.0K | 50,000 | $18.80 | [Form 4](https://www.sec.gov/Archives/edgar/data/1043219/000199443626000004/0001994436-26-000004-index.htm) |
| **FLOC** Flowco Holdings Inc. | EDWARDS JOSEPH R | President and CEO, Director | $798.2K | 41,000 | $19.47 | [Form 4](https://www.sec.gov/Archives/edgar/data/1202019/000119312526453692/0001193125-26-453692-index.htm) |
| **DGICA** DONEGAL GROUP INC | DONEGAL MUTUAL INSURANCE CO | 10% Owner | $621.5K | 33,000 | $18.83 | [Form 4](https://www.sec.gov/Archives/edgar/data/800457/000093559626000028/0000935596-26-000028-index.htm) |

## Biggest insider sales · filed 2026-11-09

| Company | Insider | Role | Value | Shares | Avg price | Filing |
|---|---|---|---:|---:|---:|---|
| **SYK** STRYKER CORP | STRYKER RONDA E | Director | $178.9M | 550,000 | $325.32 | [Form 4](https://www.sec.gov/Archives/edgar/data/310764/000124291426000012/0001242914-26-000012-index.htm) |
| **FIGS** FIGS, Inc. | Spear Catherine Eva | Chief Executive Officer, Director, 10% Owner | $79.7M | 4,044,284 | $19.70 | [Form 4](https://www.sec.gov/Archives/edgar/data/1846576/000162828026072460/0001628280-26-072460-index.htm) |
| **ANET** Arista Networks, Inc. | BECHTOLSHEIM ANDREAS | 10% Owner | $43.0M | 260,000 | $165.45 | [Form 4](https://www.sec.gov/Archives/edgar/data/1596532/000159653226000260/0001596532-26-000260-index.htm) |
| **WEX** WEX Inc. | Wolfe Lauren Taylor, Impactive Capital LP, Impactive Capital LLC, Asmar Christian | Director | $42.6M | 234,577 | $181.47 | [Form 4](https://www.sec.gov/Archives/edgar/data/1787532/000092189526002975/0000921895-26-002975-index.htm) |
| **CHYM** Chime Financial, Inc. | DST Global Advisors Ltd, Cardew Services Ltd, Galileo (PTC) Ltd, Zinonos Despoina | 10% Owner | $41.4M | 1,329,767 | $31.14 | [Form 4](https://www.sec.gov/Archives/edgar/data/1550169/000119312526454169/0001193125-26-454169-index.htm) |

Full list: [`data/insider/2026/11/2026-11-09.md`](data/insider/2026/11/2026-11-09.md)

## Latest weekly recap

[2026-W45](data/weekly/2026-W45.md)

## How it works

- [`scripts/update.py`](scripts/update.py) (Python stdlib only) runs every weekday via [`.github/workflows/daily.yml`](.github/workflows/daily.yml).
- **Insider trades:** reads SEC EDGAR's daily index, parses every Form 4, and keeps open-market purchases (code `P`) and sales (code `S`).
- **Market:** closing prices for major index ETFs, the 11 S&P sector ETFs, and 40 large-cap stocks.
- **Weekly recap:** every Monday, covering the week just ended, including cluster buys (multiple insiders buying the same company).
- Raw JSON lives in [`data/`](data) for anyone who wants to analyze it.

_Informational only, not investment advice. Data: SEC EDGAR (Form 4) and Yahoo Finance; may contain errors or delays._
