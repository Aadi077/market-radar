# 📊 Market Radar

An automatically updated record of **insider trading** (SEC Form 4 open-market buys and sales) and **US market performance**, updated every weekday with a recap each Monday. Collected by GitHub Actions.

**Last updated:** 2026-11-04

## Market close · 2026-11-04

| Index | Close | Change |
|---|---:|---:|
| S&P 500 (SPY) | 766.81 | +1.65% |
| Nasdaq 100 (QQQ) | 691.95 | +0.97% |
| Dow 30 (DIA) | 533.11 | +3.10% |
| Russell 2000 (IWM) | 284.02 | +1.51% |

![Sector performance](charts/sectors-daily.svg)

**Top large-cap gainers:** **MSFT** +6.68% · **MCD** +6.53% · **HD** +6.53% · **AMZN** +6.12% · **AAPL** +5.31%  
**Top large-cap decliners:** **XOM** -4.62% · **INTC** -3.77% · **CVX** -3.69% · **TSLA** -3.34% · **NVDA** -3.17%

## Biggest insider buys · filed 2026-11-03

| Company | Insider | Role | Value | Shares | Avg price | Filing |
|---|---|---|---:|---:|---:|---|
| **MGM** MGM Resorts International | Meister Keith A. | Director | $51.7M | 1,745,592 | $29.64 | [Form 4](https://www.sec.gov/Archives/edgar/data/789570/000101143826000643/0001011438-26-000643-index.htm) |
| **BBTX** Bambusa Therapeutics, Inc. | RA CAPITAL MANAGEMENT, L.P., RA Capital Healthcare Fund LP, RA Capital Nexus Fund III, L.P., Kolchinsky Peter, Shah Rajeev M. | Director, 10% Owner | $46.6M | 2,953,820 | $15.79 | [Form 4](https://www.sec.gov/Archives/edgar/data/2044950/000123191926001533/0001231919-26-001533-index.htm) |
| John Hancock GA Senior Loan Trust | Manufacturers Life Reinsurance Ltd | 10% Owner | $31.0M | 1,922,581 | $16.12 | [Form 4](https://www.sec.gov/Archives/edgar/data/1742951/000176549626000020/0001765496-26-000020-index.htm) |
| **SIRI** SIRIUS XM HOLDINGS INC. | BERKSHIRE HATHAWAY INC, BUFFETT WARREN E | 10% Owner | $26.9M | 924,281 | $29.10 | [Form 4](https://www.sec.gov/Archives/edgar/data/1067983/000119312526445930/0001193125-26-445930-index.htm) |
| **LRN** Stride, Inc. | Haggart Dylan G., Fivespan Partners, LP, Fivespan Partners GP, LLC | Director | $17.6M | 228,057 | $77.06 | [Form 4](https://www.sec.gov/Archives/edgar/data/2162829/000121390026115698/0001213900-26-115698-index.htm) |
| John Hancock GA Senior Loan Trust | Manufacturers Life Insurance Co (Bermuda Branch) | 10% Owner | $12.2M | 756,629 | $16.12 | [Form 4](https://www.sec.gov/Archives/edgar/data/1742951/000183368326000020/0001833683-26-000020-index.htm) |
| **CRBG** Corebridge Financial, Inc. | NIPPON LIFE INSURANCE CO | 10% Owner | $7.9M | 227,773 | $34.62 | [Form 4](https://www.sec.gov/Archives/edgar/data/1889539/000119312526445611/0001193125-26-445611-index.htm) |
| **PLBY** Playboy, Inc. | Docler Holding S.a r.l., Byborg Enterprises S.A., Million S.a r.l., Gattyan Gyorgy | Director, 10% Owner | $5.0M | 4,761,905 | $1.05 | [Form 4](https://www.sec.gov/Archives/edgar/data/2044291/000101297526001005/0001012975-26-001005-index.htm) |
| **SITE** SiteOne Landscape Supply, Inc. | BLACK DOUG | CEO, Director | $1.0M | 9,100 | $110.30 | [Form 4](https://www.sec.gov/Archives/edgar/data/1672083/000110465926122247/0001104659-26-122247-index.htm) |
| **BA** BOEING CO | Buckley Mortimer J | Director | $998.4K | 5,820 | $171.55 | [Form 4](https://www.sec.gov/Archives/edgar/data/12927/000122520826008642/0001225208-26-008642-index.htm) |

## Biggest insider sales · filed 2026-11-03

| Company | Insider | Role | Value | Shares | Avg price | Filing |
|---|---|---|---:|---:|---:|---|
| **APH** AMPHENOL CORP /DE/ | NORWITT RICHARD ADAM | President & CEO, Director | $65.9M | 799,576 | $82.48 | [Form 4](https://www.sec.gov/Archives/edgar/data/820313/000110465926121973/0001104659-26-121973-index.htm) |
| **ANET** Arista Networks, Inc. | BECHTOLSHEIM ANDREAS | 10% Owner | $45.9M | 267,892 | $171.19 | [Form 4](https://www.sec.gov/Archives/edgar/data/1596532/000159653226000256/0001596532-26-000256-index.htm) |
| **KNSA** Kiniksa Pharmaceuticals International, plc | Patel Sanj K | CHAIRMAN & CEO, Director | $37.4M | 402,494 | $92.92 | [Form 4](https://www.sec.gov/Archives/edgar/data/1730430/000153221826000018/0001532218-26-000018-index.htm) |
| **AXP** AMERICAN EXPRESS CO | Seeger Laureen | Chief Legal Officer | $22.9M | 69,860 | $328.17 | [Form 4](https://www.sec.gov/Archives/edgar/data/4962/000000496226000424/0000004962-26-000424-index.htm) |
| **FTNT** Fortinet, Inc. | Xie Ken | President & CEO, Director | $20.9M | 161,483 | $129.31 | [Form 4](https://www.sec.gov/Archives/edgar/data/1262039/000147558726000016/0001475587-26-000016-index.htm) |

Full list: [`data/insider/2026/11/2026-11-03.md`](data/insider/2026/11/2026-11-03.md)

## Latest weekly recap

[2026-W44](data/weekly/2026-W44.md)

## How it works

- [`scripts/update.py`](scripts/update.py) (Python stdlib only) runs every weekday via [`.github/workflows/daily.yml`](.github/workflows/daily.yml).
- **Insider trades:** reads SEC EDGAR's daily index, parses every Form 4, and keeps open-market purchases (code `P`) and sales (code `S`).
- **Market:** closing prices for major index ETFs, the 11 S&P sector ETFs, and 40 large-cap stocks.
- **Weekly recap:** every Monday, covering the week just ended, including cluster buys (multiple insiders buying the same company).
- Raw JSON lives in [`data/`](data) for anyone who wants to analyze it.

_Informational only, not investment advice. Data: SEC EDGAR (Form 4) and Yahoo Finance; may contain errors or delays._
