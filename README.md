# 📊 Market Radar

A daily, automatically updated record of **insider trading** (SEC Form 4 open-market buys and sales) and **US market performance**, with a weekly recap every Sunday. Collected by GitHub Actions.

**Last updated:** 2026-09-15

## Market close · 2026-09-14

| Index | Close | Change |
|---|---:|---:|
| S&P 500 (SPY) | 760.88 | -0.45% |
| Nasdaq 100 (QQQ) | 709.18 | -0.80% |
| Dow 30 (DIA) | 524.49 | -0.25% |
| Russell 2000 (IWM) | 287.91 | -0.34% |

![Sector performance](charts/sectors-daily.svg)

**Top large-cap gainers:** **ADBE** +5.30% · **CRM** +4.73% · **NFLX** +3.77% · **PLTR** +3.64% · **GOOGL** +3.22%  
**Top large-cap decliners:** **INTC** -5.59% · **BAC** -5.14% · **AVGO** -4.77% · **AMD** -4.40% · **ORCL** -3.65%

## Biggest insider buys · filed 2026-09-14

| Company | Insider | Role | Value | Shares | Avg price | Filing |
|---|---|---|---:|---:|---:|---|
| **RSG** REPUBLIC SERVICES, INC. | CASCADE INVESTMENT, L.L.C., GATES WILLIAM H III | 10% Owner | $129.3M | 580,810 | $222.63 | [Form 4](https://www.sec.gov/Archives/edgar/data/1052192/000110465926107592/0001104659-26-107592-index.htm) |
| **PMTS** CPI Card Group Inc. | Tricor PMT25 Holdings Inc., Tricor Pacific Capital Inc. | 10% Owner | $11.3M | 525,000 | $21.50 | [Form 4](https://www.sec.gov/Archives/edgar/data/1641614/000110465926107610/0001104659-26-107610-index.htm) |
| **CRBG** Corebridge Financial, Inc. | NIPPON LIFE INSURANCE CO | 10% Owner | $6.0M | 176,300 | $34.01 | [Form 4](https://www.sec.gov/Archives/edgar/data/1889539/000119312526390651/0001193125-26-390651-index.htm) |
| **DGICA** DONEGAL GROUP INC | DONEGAL MUTUAL INSURANCE CO | 10% Owner | $1.1M | 54,725 | $19.23 | [Form 4](https://www.sec.gov/Archives/edgar/data/800457/000093559626000026/0000935596-26-000026-index.htm) |
| **ECL** ECOLAB INC. | Green Eric Mark | Director | $1.0M | 3,690 | $276.64 | [Form 4](https://www.sec.gov/Archives/edgar/data/31462/000162828026061859/0001628280-26-061859-index.htm) |
| **ANGX** Angel Studios, Inc. | Sarowitz Steven I | Director | $472.6K | 88,647 | $5.33 | [Form 4](https://www.sec.gov/Archives/edgar/data/1865200/000186520026000087/0001865200-26-000087-index.htm) |
| **CROX** Crocs, Inc. | SMACH THOMAS J | Director | $437.5K | 4,000 | $109.38 | [Form 4](https://www.sec.gov/Archives/edgar/data/1334036/000119410626000012/0001194106-26-000012-index.htm) |
| **PMTS** CPI Card Group Inc. | Riley H Sanford | Director | $300.0K | 13,953 | $21.50 | [Form 4](https://www.sec.gov/Archives/edgar/data/1641614/000131740626000006/0001317406-26-000006-index.htm) |
| **PMTS** CPI Card Group Inc. | Peters Nicholas | Director | $250.0K | 11,628 | $21.50 | [Form 4](https://www.sec.gov/Archives/edgar/data/1641614/000165477026000004/0001654770-26-000004-index.htm) |
| **ECVT** Ecovyst Inc. | Humble Patti A. | Director | $250.0K | 24,875 | $10.05 | [Form 4](https://www.sec.gov/Archives/edgar/data/1708035/000170803526000099/0001708035-26-000099-index.htm) |

## Biggest insider sales · filed 2026-09-14

| Company | Insider | Role | Value | Shares | Avg price | Filing |
|---|---|---|---:|---:|---:|---|
| **INGM** Ingram Micro Holding Corp | PLATINUM EQUITY, LLC, Platinum Equity Investment Holdings, LLC, Platinum Equity Investment Holdings IC (Cayman), LLC, Platinum Equity InvestCo, L.P., Platinum Equity Investment Holdings V, LLC, Platinum Equity Partners V, LLC, Platinum Equity Partners V, L.P., Imola JV Holdings, L.P., Ingram Holdco, LLC, Gores Tom | 10% Owner | $356.8M | 13,125,000 | $27.19 | [Form 4](https://www.sec.gov/Archives/edgar/data/1471783/000110465926107514/0001104659-26-107514-index.htm) |
| **PMTS** CPI Card Group Inc. | Parallel49 Equity, ULC, Tricor Pacific Capital Partners (Fund IV) U.S., LP, Tricor Pacific Capital Partners (Fund IV), LP | 10% Owner | $54.9M | 2,687,921 | $20.43 | [Form 4](https://www.sec.gov/Archives/edgar/data/1641614/000165514826000004/0001655148-26-000004-index.htm) |
| **AMD** ADVANCED MICRO DEVICES INC | Su Lisa T | Chair, President & CEO, Director | $48.1M | 95,000 | $506.80 | [Form 4](https://www.sec.gov/Archives/edgar/data/2488/000000248826000178/0000002488-26-000178-index.htm) |
| **HNGE** Hinge Health, Inc. | Mecklenburg Gabriel M.I. | Director | $22.2M | 250,000 | $88.97 | [Form 4](https://www.sec.gov/Archives/edgar/data/1673743/000206278126000022/0002062781-26-000022-index.htm) |
| **CHYM** Chime Financial, Inc. | CAROLAN SHAWN T | Director | $19.2M | 579,313 | $33.13 | [Form 4](https://www.sec.gov/Archives/edgar/data/1376066/000137606626000007/0001376066-26-000007-index.htm) |

Full list: [`data/insider/2026/09/2026-09-14.md`](data/insider/2026/09/2026-09-14.md)

## How it works

- [`scripts/update.py`](scripts/update.py) (Python stdlib only) runs daily via [`.github/workflows/daily.yml`](.github/workflows/daily.yml).
- **Insider trades:** reads SEC EDGAR's daily index, parses every Form 4, and keeps open-market purchases (code `P`) and sales (code `S`).
- **Market:** closing prices for major index ETFs, the 11 S&P sector ETFs, and 40 large-cap stocks.
- **Weekly recap:** every Sunday, including cluster buys (multiple insiders buying the same company).
- Raw JSON lives in [`data/`](data) for anyone who wants to analyze it.

_Informational only, not investment advice. Data: SEC EDGAR (Form 4) and Yahoo Finance; may contain errors or delays._
