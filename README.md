# 📊 Market Radar

An automatically updated record of **insider trading** (SEC Form 4 open-market buys and sales) and **US market performance**, updated every weekday with a recap each Monday. Collected by GitHub Actions.

**Last updated:** 2026-10-20

## Market close · 2026-10-19

| Index | Close | Change |
|---|---:|---:|
| S&P 500 (SPY) | 766.48 | +0.42% |
| Nasdaq 100 (QQQ) | 718.36 | +1.21% |
| Dow 30 (DIA) | 518.92 | -0.03% |
| Russell 2000 (IWM) | 271.28 | +0.31% |

![Sector performance](charts/sectors-daily.svg)

**Top large-cap gainers:** **AMZN** +4.98% · **PLTR** +4.36% · **TSLA** +3.76% · **INTC** +2.43% · **IBM** +1.83%  
**Top large-cap decliners:** **WFC** -2.47% · **JPM** -1.82% · **BAC** -1.64% · **MRK** -1.59% · **TMO** -1.54%

## Biggest insider buys · filed 2026-10-19

| Company | Insider | Role | Value | Shares | Avg price | Filing |
|---|---|---|---:|---:|---:|---|
| **LNBIX** Lincoln Bain Capital Total Credit Fund | Lincoln Financial Investments Corp | 10% Owner | $25.0M | 2,477,701 | $10.09 | [Form 4](https://www.sec.gov/Archives/edgar/data/2054992/000119312526425009/0001193125-26-425009-index.htm) |
| **CRBG** Corebridge Financial, Inc. | NIPPON LIFE INSURANCE CO | 10% Owner | $17.1M | 510,873 | $33.43 | [Form 4](https://www.sec.gov/Archives/edgar/data/1889539/000119312526425300/0001193125-26-425300-index.htm) |
| **IAM** Iambic Therapeutics, Inc. | Rachlin Evan Lockwood | Director | $11.5M | 718,750 | $16.00 | [Form 4](https://www.sec.gov/Archives/edgar/data/1997038/000215167826000007/0002151678-26-000007-index.htm) |
| **APLD** Applied Digital Corp. | Zhang Jason Gechen | President | $5.7M | 300,000 | $18.86 | [Form 4](https://www.sec.gov/Archives/edgar/data/1144879/000190044526000006/0001900445-26-000006-index.htm) |
| **CTY** CITY THERAPEUTICS, INC. | ARCH Venture Partners XII, LLC, ARCH Venture Partners XII, L.P., ARCH Venture Fund XII, L.P., CRANDELL KEITH, Burow Kristina, GILLIS STEVEN | 10% Owner | $3.1M | 170,000 | $18.00 | [Form 4](https://www.sec.gov/Archives/edgar/data/1906837/000110465926116966/0001104659-26-116966-index.htm) |
| **CTY** CITY THERAPEUTICS, INC. | NELSEN ROBERT | Director, 10% Owner | $3.1M | 170,000 | $18.00 | [Form 4](https://www.sec.gov/Archives/edgar/data/2143850/000110465926116965/0001104659-26-116965-index.htm) |
| **BPRE** Bluerock Private Real Estate Fund | KAMFAR RAMIN | Director | $2.4M | 194,228 | $12.47 | [Form 4](https://www.sec.gov/Archives/edgar/data/1551047/000139834426018404/0001398344-26-018404-index.htm) |
| **APLD** Applied Digital Corp. | Cummins Wes | CEO; Chairman, Director | $1.0M | 55,803 | $18.04 | [Form 4](https://www.sec.gov/Archives/edgar/data/1144879/000139193526000009/0001391935-26-000009-index.htm) |
| **SNES** SenesTech, Inc. | GLENBROOK CAPITAL MANAGEMENT | 10% Owner | $706.1K | 983,804 | $0.72 | [Form 4](https://www.sec.gov/Archives/edgar/data/1273782/000090266426004215/0000902664-26-004215-index.htm) |
| **CNXU** Conexeu Sciences Inc. | Purcell Lynn Sebastian | Director, 10% Owner | $500.0K | 166,666 | $3.00 | [Form 4](https://www.sec.gov/Archives/edgar/data/2066836/000212846926000009/0002128469-26-000009-index.htm) |

## Biggest insider sales · filed 2026-10-19

| Company | Insider | Role | Value | Shares | Avg price | Filing |
|---|---|---|---:|---:|---:|---|
| **TALO** TALOS ENERGY INC. | Control Empresarial de Capitales S.A. de C.V. | 10% Owner | $47.3M | 2,752,000 | $17.19 | [Form 4](https://www.sec.gov/Archives/edgar/data/1273693/000114036126040135/0001140361-26-040135-index.htm) |
| **PATH** UiPath, Inc. | Dines Daniel | CEO and Chairman, Director, 10% Owner | $33.1M | 2,500,000 | $13.23 | [Form 4](https://www.sec.gov/Archives/edgar/data/1855767/000185576726000019/0001855767-26-000019-index.htm) |
| **AFL** AFLAC INC | Japan Post Holdings Co., Ltd. | 10% Owner | $13.5M | 113,611 | $118.53 | [Form 4](https://www.sec.gov/Archives/edgar/data/4977/000110465926116752/0001104659-26-116752-index.htm) |
| **TVTX** Travere Therapeutics, Inc. | Dube Eric M | CHIEF EXECUTIVE OFFICER, Director | $13.1M | 243,735 | $53.82 | [Form 4](https://www.sec.gov/Archives/edgar/data/1763494/000176349426000008/0001763494-26-000008-index.htm) |
| **W** Wayfair Inc. | Conine Steven | Director | $13.0M | 117,000 | $111.25 | [Form 4](https://www.sec.gov/Archives/edgar/data/1620052/000161670726000176/0001616707-26-000176-index.htm) |

Full list: [`data/insider/2026/10/2026-10-19.md`](data/insider/2026/10/2026-10-19.md)

## Latest weekly recap

[2026-W42](data/weekly/2026-W42.md)

## How it works

- [`scripts/update.py`](scripts/update.py) (Python stdlib only) runs every weekday via [`.github/workflows/daily.yml`](.github/workflows/daily.yml).
- **Insider trades:** reads SEC EDGAR's daily index, parses every Form 4, and keeps open-market purchases (code `P`) and sales (code `S`).
- **Market:** closing prices for major index ETFs, the 11 S&P sector ETFs, and 40 large-cap stocks.
- **Weekly recap:** every Monday, covering the week just ended, including cluster buys (multiple insiders buying the same company).
- Raw JSON lives in [`data/`](data) for anyone who wants to analyze it.

_Informational only, not investment advice. Data: SEC EDGAR (Form 4) and Yahoo Finance; may contain errors or delays._
