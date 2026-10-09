# 📊 Market Radar

An automatically updated record of **insider trading** (SEC Form 4 open-market buys and sales) and **US market performance**, updated every weekday with a recap each Monday. Collected by GitHub Actions.

**Last updated:** 2026-10-08

## Market close · 2026-10-08

| Index | Close | Change |
|---|---:|---:|
| S&P 500 (SPY) | 773.93 | -0.42% |
| Nasdaq 100 (QQQ) | 747.58 | -1.34% |
| Dow 30 (DIA) | 511.65 | +0.12% |
| Russell 2000 (IWM) | 277.57 | -0.05% |

![Sector performance](charts/sectors-daily.svg)

**Top large-cap gainers:** **PEP** +3.73% · **ADBE** +3.56% · **HD** +3.39% · **CVX** +3.12% · **IBM** +2.77%  
**Top large-cap decliners:** **ORCL** -5.48% · **INTC** -5.34% · **AVGO** -4.35% · **AMD** -3.90% · **NVDA** -2.94%

## Biggest insider buys · filed 2026-10-07

| Company | Insider | Role | Value | Shares | Avg price | Filing |
|---|---|---|---:|---:|---:|---|
| **BORR** Borr Drilling Ltd | Troim Tor Olav | Director | $6.4M | 1,500,000 | $4.24 | [Form 4](https://www.sec.gov/Archives/edgar/data/1715497/000162828026065290/0001628280-26-065290-index.htm) |
| **CRBG** Corebridge Financial, Inc. | NIPPON LIFE INSURANCE CO | 10% Owner | $2.3M | 65,711 | $34.75 | [Form 4](https://www.sec.gov/Archives/edgar/data/1889539/000119312526417005/0001193125-26-417005-index.htm) |
| **IRIX** IRIDEX CORP | Lin Shih-Yao David | 10% Owner | $597.9K | 570,184 | $1.05 | [Form 4](https://www.sec.gov/Archives/edgar/data/1006045/000106299326005210/0001062993-26-005210-index.htm) |
| **MXF** MEXICO FUND INC | Saba Capital Management, L.P. | 10% Owner | $520.3K | 25,900 | $20.09 | [Form 4](https://www.sec.gov/Archives/edgar/data/65433/000151028126000325/0001510281-26-000325-index.htm) |
| **IRIX** IRIDEX CORP | Lin Shih-Yao David | 10% Owner | $438.8K | 350,557 | $1.25 | [Form 4](https://www.sec.gov/Archives/edgar/data/1006045/000106299326005214/0001062993-26-005214-index.htm) |
| **IRIX** IRIDEX CORP | Lin Shih-Yao David | 10% Owner | $273.6K | 266,068 | $1.03 | [Form 4](https://www.sec.gov/Archives/edgar/data/1006045/000106299326005212/0001062993-26-005212-index.htm) |
| **GF** NEW GERMANY FUND INC | Saba Capital Management, L.P. | 10% Owner | $264.3K | 25,144 | $10.51 | [Form 4](https://www.sec.gov/Archives/edgar/data/858706/000151028126000326/0001510281-26-000326-index.htm) |
| **STWI** StageWise Strategies Corp. | Tourism & Entertainment Group, LLC | 10% Owner | $138.0K | 1,000,000 | $0.14 | [Form 4](https://www.sec.gov/Archives/edgar/data/1999261/000121390026107676/0001213900-26-107676-index.htm) |
| **AGMB** AgomAb Therapeutics NV | Knotnerus Tim Jasper | Chief Executive Officer, Director | $94.4K | 11,000 | $8.58 | [Form 4](https://www.sec.gov/Archives/edgar/data/2020932/000212088626000001/0002120886-26-000001-index.htm) |
| **AGMB** AgomAb Therapeutics NV | Epstein David R | Director | $86.3K | 10,000 | $8.63 | [Form 4](https://www.sec.gov/Archives/edgar/data/2020932/000144582626000013/0001445826-26-000013-index.htm) |

## Biggest insider sales · filed 2026-10-07

| Company | Insider | Role | Value | Shares | Avg price | Filing |
|---|---|---|---:|---:|---:|---|
| **HOOD** Robinhood Markets, Inc. | Tenev Vladimir | Chief Executive Officer, Director | $42.6M | 375,000 | $113.72 | [Form 4](https://www.sec.gov/Archives/edgar/data/1783879/000187100626000012/0001871006-26-000012-index.htm) |
| **NET** Cloudflare, Inc. | Zatlyn Michelle | President and Board Co-Chair, Director | $35.2M | 99,009 | $355.88 | [Form 4](https://www.sec.gov/Archives/edgar/data/1477333/000178695126000025/0001786951-26-000025-index.htm) |
| Partners Group Private Equity Fund, LLC | Partners Group Private Equity II, LLC |  | $30.0M | 13,619,649 | $2.20 | [Form 4](https://www.sec.gov/Archives/edgar/data/1447247/000175604126000003/0001756041-26-000003-index.htm) |
| **AXIA3** AXIA Energia S.A. | Batista de Lima Filho Pedro | Director | $26.4M | 2,237,300 | $11.81 | [Form 4](https://www.sec.gov/Archives/edgar/data/1439124/000121390026107647/0001213900-26-107647-index.htm) |
| **GAP** GAP INC | FISHER WILLIAM SYDNEY | Director, 10% Owner | $22.1M | 933,656 | $23.64 | [Form 4](https://www.sec.gov/Archives/edgar/data/1217081/000121708126000015/0001217081-26-000015-index.htm) |

Full list: [`data/insider/2026/10/2026-10-07.md`](data/insider/2026/10/2026-10-07.md)

## Latest weekly recap

[2026-W40](data/weekly/2026-W40.md)

## How it works

- [`scripts/update.py`](scripts/update.py) (Python stdlib only) runs every weekday via [`.github/workflows/daily.yml`](.github/workflows/daily.yml).
- **Insider trades:** reads SEC EDGAR's daily index, parses every Form 4, and keeps open-market purchases (code `P`) and sales (code `S`).
- **Market:** closing prices for major index ETFs, the 11 S&P sector ETFs, and 40 large-cap stocks.
- **Weekly recap:** every Monday, covering the week just ended, including cluster buys (multiple insiders buying the same company).
- Raw JSON lives in [`data/`](data) for anyone who wants to analyze it.

_Informational only, not investment advice. Data: SEC EDGAR (Form 4) and Yahoo Finance; may contain errors or delays._
