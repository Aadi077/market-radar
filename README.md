# 📊 Market Radar

A daily, automatically updated record of **insider trading** (SEC Form 4 open-market buys and sales) and **US market performance**, with a weekly recap every Sunday. Collected by GitHub Actions.

**Last updated:** 2026-10-02

## Market close · 2026-10-01

| Index | Close | Change |
|---|---:|---:|
| S&P 500 (SPY) | 763.99 | +0.18% |
| Nasdaq 100 (QQQ) | 742.03 | +0.31% |
| Dow 30 (DIA) | 508.62 | +0.01% |
| Russell 2000 (IWM) | 279.02 | +0.41% |

![Sector performance](charts/sectors-daily.svg)

**Top large-cap gainers:** **CRM** +3.10% · **IBM** +2.59% · **PLTR** +1.60% · **CVX** +1.42% · **NVDA** +1.09%  
**Top large-cap decliners:** **DIS** -3.40% · **TMO** -3.34% · **NFLX** -2.49% · **JNJ** -2.30% · **AVGO** -2.15%

## Biggest insider buys · filed 2026-10-01

| Company | Insider | Role | Value | Shares | Avg price | Filing |
|---|---|---|---:|---:|---:|---|
| **SLBT** SL Science Holding Ltd | Wang Ching-Dong | Chief Executive Officer, Director, 10% Owner | $10329.9B | 4,545,306 | $2,272,653.00 | [Form 4](https://www.sec.gov/Archives/edgar/data/2070534/000110465926112844/0001104659-26-112844-index.htm) |
| **UUU** UNIVERSAL SAFETY PRODUCTS, INC. | AULT MILTON C III | Director, 10% Owner | $92.4M | 18,000 | $5,134.00 | [Form 4](https://www.sec.gov/Archives/edgar/data/1212502/000121465926012438/0001214659-26-012438-index.htm) |
| John Hancock GA Senior Loan Trust | Manufacturers Life Reinsurance Ltd | 10% Owner | $31.0M | 1,931,123 | $16.05 | [Form 4](https://www.sec.gov/Archives/edgar/data/1742951/000176549626000018/0001765496-26-000018-index.htm) |
| John Hancock GA Mortgage Trust | Manulife (International) Ltd | 10% Owner | $26.0M | 1,476,118 | $17.61 | [Form 4](https://www.sec.gov/Archives/edgar/data/1742952/000176551826000006/0001765518-26-000006-index.htm) |
| John Hancock GA Senior Loan Trust | Manufacturers Life Insurance Co (Bermuda Branch) | 10% Owner | $12.0M | 747,531 | $16.05 | [Form 4](https://www.sec.gov/Archives/edgar/data/1742951/000183368326000018/0001833683-26-000018-index.htm) |
| John Hancock GA Mortgage Trust | Manufacturers Life Reinsurance Ltd | 10% Owner | $9.0M | 510,964 | $17.61 | [Form 4](https://www.sec.gov/Archives/edgar/data/1742952/000176549626000019/0001765496-26-000019-index.htm) |
| **CRBG** Corebridge Financial, Inc. | NIPPON LIFE INSURANCE CO | 10% Owner | $7.3M | 216,818 | $33.67 | [Form 4](https://www.sec.gov/Archives/edgar/data/1889539/000119312526410677/0001193125-26-410677-index.htm) |
| **GPUS** Hyperscale Data, Inc. | AULT MILTON C III, Ault & Company, Inc. | Executive Chairman, Director, 10% Owner | $5.1M | 10,313,474 | $0.49 | [Form 4](https://www.sec.gov/Archives/edgar/data/1212502/000121465926012383/0001214659-26-012383-index.htm) |
| CNL Strategic Residential Credit, Inc. | SENEFF JAMES M JR | 10% Owner | $5.0M | 206,101 | $24.26 | [Form 4](https://www.sec.gov/Archives/edgar/data/2066337/000143774926031762/0001437749-26-031762-index.htm) |
| John Hancock GA Mortgage Trust | Manulife (Singapore) Pte. Ltd. | 10% Owner | $4.0M | 227,095 | $17.61 | [Form 4](https://www.sec.gov/Archives/edgar/data/1742952/000183747826000018/0001837478-26-000018-index.htm) |

## Biggest insider sales · filed 2026-10-01

| Company | Insider | Role | Value | Shares | Avg price | Filing |
|---|---|---|---:|---:|---:|---|
| **ACT** Enact Holdings, Inc. | Genworth Holdings, Inc. | 10% Owner | $37.1M | 762,894 | $48.65 | [Form 4](https://www.sec.gov/Archives/edgar/data/1823529/000157298326000021/0001572983-26-000021-index.htm) |
| **MEDP** Medpace Holdings, Inc. | Troendle August J. | President & CEO, Director, 10% Owner | $30.3M | 48,667 | $623.03 | [Form 4](https://www.sec.gov/Archives/edgar/data/1668397/000162205826000022/0001622058-26-000022-index.htm) |
| **CRWV** CoreWeave, Inc. | Intrator Michael N | CEO and President, Director, 10% Owner | $26.7M | 307,692 | $86.65 | [Form 4](https://www.sec.gov/Archives/edgar/data/1769628/000176962826000437/0001769628-26-000437-index.htm) |
| **NTAP** NetApp, Inc. | Kurian George | CEO, Director | $10.5M | 50,000 | $209.95 | [Form 4](https://www.sec.gov/Archives/edgar/data/1586813/000119312526410739/0001193125-26-410739-index.htm) |
| **IOT** Samsara Inc. | Biswas Sanjit | CHIEF EXECUTIVE OFFICER, Director, 10% Owner | $10.0M | 263,900 | $38.03 | [Form 4](https://www.sec.gov/Archives/edgar/data/1895111/000189511126000019/0001895111-26-000019-index.htm) |

Full list: [`data/insider/2026/10/2026-10-01.md`](data/insider/2026/10/2026-10-01.md)

## Latest weekly recap

[2026-W39](data/weekly/2026-W39.md)

## How it works

- [`scripts/update.py`](scripts/update.py) (Python stdlib only) runs daily via [`.github/workflows/daily.yml`](.github/workflows/daily.yml).
- **Insider trades:** reads SEC EDGAR's daily index, parses every Form 4, and keeps open-market purchases (code `P`) and sales (code `S`).
- **Market:** closing prices for major index ETFs, the 11 S&P sector ETFs, and 40 large-cap stocks.
- **Weekly recap:** every Sunday, including cluster buys (multiple insiders buying the same company).
- Raw JSON lives in [`data/`](data) for anyone who wants to analyze it.

_Informational only, not investment advice. Data: SEC EDGAR (Form 4) and Yahoo Finance; may contain errors or delays._
