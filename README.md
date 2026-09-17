# 📊 Market Radar

A daily, automatically updated record of **insider trading** (SEC Form 4 open-market buys and sales) and **US market performance**, with a weekly recap every Sunday. Collected by GitHub Actions.

**Last updated:** 2026-09-16

## Market close · 2026-09-15

| Index | Close | Change |
|---|---:|---:|
| S&P 500 (SPY) | 757.39 | -0.46% |
| Nasdaq 100 (QQQ) | 704.54 | -0.65% |
| Dow 30 (DIA) | 521.23 | -0.62% |
| Russell 2000 (IWM) | 285.14 | -0.96% |

![Sector performance](charts/sectors-daily.svg)

**Top large-cap gainers:** **TMO** +4.53% · **CVX** +2.64% · **XOM** +2.57% · **AMD** +2.19% · **WFC** +1.14%  
**Top large-cap decliners:** **GE** -3.31% · **ORCL** -3.07% · **NFLX** -3.01% · **ADBE** -2.95% · **AMZN** -2.02%

## Biggest insider buys · filed 2026-09-15

| Company | Insider | Role | Value | Shares | Avg price | Filing |
|---|---|---|---:|---:|---:|---|
| **FTK** FLOTEK INDUSTRIES INC/CN/ | Wilks Matthew | Director | $34.3M | 1,319,493 | $26.01 | [Form 4](https://www.sec.gov/Archives/edgar/data/928054/000110465926108024/0001104659-26-108024-index.htm) |
| **CRBG** Corebridge Financial, Inc. | NIPPON LIFE INSURANCE CO | 10% Owner | $5.9M | 171,144 | $34.61 | [Form 4](https://www.sec.gov/Archives/edgar/data/1889539/000119312526391947/0001193125-26-391947-index.htm) |
| **GIII** G III APPAREL GROUP LTD /DE/ | GOLDFARB MORRIS | CEO, Director | $1.1M | 40,000 | $27.94 | [Form 4](https://www.sec.gov/Archives/edgar/data/821002/000082100226000041/0000821002-26-000041-index.htm) |
| **CELH** Celsius Holdings, Inc. | DeSantis Damon | Director | $1.0M | 36,000 | $27.78 | [Form 4](https://www.sec.gov/Archives/edgar/data/1341766/000162828026062057/0001628280-26-062057-index.htm) |
| **CSAN** Cosan S.A. | Cordes Burkhard Otto | Director | $696.0K | 159,000 | $4.38 | [Form 4](https://www.sec.gov/Archives/edgar/data/1974588/000129281426004562/0001292814-26-004562-index.htm) |
| **COO** COOPER COMPANIES, INC. | Rosebrough Walter M Jr | Director | $541.6K | 10,000 | $54.16 | [Form 4](https://www.sec.gov/Archives/edgar/data/711404/000141308726000007/0001413087-26-000007-index.htm) |
| **COO** COOPER COMPANIES, INC. | Kurzius Lawrence Erik | Director | $539.1K | 10,000 | $53.91 | [Form 4](https://www.sec.gov/Archives/edgar/data/711404/000135209026000007/0001352090-26-000007-index.htm) |
| **LMB** Limbach Holdings, Inc. | Horowitz Joshua, Palm Global Small Cap Master Fund LP | Director | $391.0K | 7,820 | $50.00 | [Form 4](https://www.sec.gov/Archives/edgar/data/1612424/000110465926108006/0001104659-26-108006-index.htm) |
| **RWT** REDWOOD TRUST INC | Abate Christopher J | Chief Executive Officer, Director | $383.9K | 100,000 | $3.84 | [Form 4](https://www.sec.gov/Archives/edgar/data/1453409/000110465926107867/0001104659-26-107867-index.htm) |
| **VENU** Venu Holding Corp | Finke Thomas M | Director | $350.0K | 200,000 | $1.75 | [Form 4](https://www.sec.gov/Archives/edgar/data/1363651/000149315226042742/0001493152-26-042742-index.htm) |

## Biggest insider sales · filed 2026-09-15

| Company | Insider | Role | Value | Shares | Avg price | Filing |
|---|---|---|---:|---:|---:|---|
| **LFST** LifeStance Health Group, Inc. | TPG GP A, LLC, COULTER JAMES G, WINKELRIED JON | 10% Owner | $226.3M | 18,409,705 | $12.29 | [Form 4](https://www.sec.gov/Archives/edgar/data/1099776/000199937126020559/0001999371-26-020559-index.htm) |
| **FTK** FLOTEK INDUSTRIES INC/CN/ | ProFrac GDM, LLC | 10% Owner | $60.0M | 2,306,806 | $26.01 | [Form 4](https://www.sec.gov/Archives/edgar/data/928054/000110465926108023/0001104659-26-108023-index.htm) |
| **DELL** Dell Technologies Inc. | Silver Lake Partners IV, L.P., Silver Lake Technology Associates IV, L.P., SLTA IV (GP), L.L.C., Silver Lake Group, L.L.C., Durban Egon | Director, 10% Owner | $45.2M | 80,972 | $558.79 | [Form 4](https://www.sec.gov/Archives/edgar/data/1571996/000119312526392079/0001193125-26-392079-index.htm) |
| **DELL** Dell Technologies Inc. | SL SPV-2, L.P., SLTA SPV-2, L.P., SLTA SPV-2 (GP), L.L.C., Silver Lake Group, L.L.C., Durban Egon | Director, 10% Owner | $40.3M | 72,148 | $558.74 | [Form 4](https://www.sec.gov/Archives/edgar/data/1571996/000119312526392089/0001193125-26-392089-index.htm) |
| **STX** Seagate Technology Holdings plc | Romano Gianluca | EVP & CFO | $38.1M | 45,898 | $830.01 | [Form 4](https://www.sec.gov/Archives/edgar/data/1764650/000113778926000240/0001137789-26-000240-index.htm) |

Full list: [`data/insider/2026/09/2026-09-15.md`](data/insider/2026/09/2026-09-15.md)

## How it works

- [`scripts/update.py`](scripts/update.py) (Python stdlib only) runs daily via [`.github/workflows/daily.yml`](.github/workflows/daily.yml).
- **Insider trades:** reads SEC EDGAR's daily index, parses every Form 4, and keeps open-market purchases (code `P`) and sales (code `S`).
- **Market:** closing prices for major index ETFs, the 11 S&P sector ETFs, and 40 large-cap stocks.
- **Weekly recap:** every Sunday, including cluster buys (multiple insiders buying the same company).
- Raw JSON lives in [`data/`](data) for anyone who wants to analyze it.

_Informational only, not investment advice. Data: SEC EDGAR (Form 4) and Yahoo Finance; may contain errors or delays._
