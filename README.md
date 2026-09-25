# 📊 Market Radar

A daily, automatically updated record of **insider trading** (SEC Form 4 open-market buys and sales) and **US market performance**, with a weekly recap every Sunday. Collected by GitHub Actions.

**Last updated:** 2026-09-24

## Market close · 2026-09-23

| Index | Close | Change |
|---|---:|---:|
| S&P 500 (SPY) | 767.81 | -0.72% |
| Nasdaq 100 (QQQ) | 741.21 | -0.84% |
| Dow 30 (DIA) | 514.30 | -1.05% |
| Russell 2000 (IWM) | 281.92 | -1.84% |

![Sector performance](charts/sectors-daily.svg)

**Top large-cap gainers:** **PLTR** +3.68% · **XOM** +1.85% · **KO** +1.11% · **BRK-B** +1.03% · **ADBE** +1.02%  
**Top large-cap decliners:** **WFC** -5.36% · **MCD** -4.81% · **GOOGL** -3.80% · **ORCL** -3.11% · **AVGO** -2.62%

## Biggest insider buys · filed 2026-09-23

| Company | Insider | Role | Value | Shares | Avg price | Filing |
|---|---|---|---:|---:|---:|---|
| **ETRA** Electra Therapeutics, Inc. | ORBIMED ADVISORS LLC, OrbiMed Capital GP VII LLC, OrbiMed Genesis GP LLC | Director, 10% Owner | $20.0M | 1,333,333 | $15.00 | [Form 4](https://www.sec.gov/Archives/edgar/data/2088082/000094787126000880/0000947871-26-000880-index.htm) |
| **ETRA** Electra Therapeutics, Inc. | GORDON CARL L | Director, 10% Owner | $20.0M | 1,333,333 | $15.00 | [Form 4](https://www.sec.gov/Archives/edgar/data/2088082/000094787126000881/0000947871-26-000881-index.htm) |
| **CV** CapsoVision, Inc | HARARI ELIYAHOU ET AL | 10% Owner | $10.0M | 1,757,469 | $5.69 | [Form 4](https://www.sec.gov/Archives/edgar/data/1378325/000100916526000009/0001009165-26-000009-index.htm) |
| **CRBG** Corebridge Financial, Inc. | NIPPON LIFE INSURANCE CO | 10% Owner | $7.5M | 212,828 | $35.08 | [Form 4](https://www.sec.gov/Archives/edgar/data/1889539/000119312526399477/0001193125-26-399477-index.htm) |
| **CRAFX** Cascade Real Assets Fund | Nesbitt Stephen Lane | President, Director | $5.0M | 500,000 | $10.00 | [Form 4](https://www.sec.gov/Archives/edgar/data/2114459/000121390026102533/0001213900-26-102533-index.htm) |
| **KBDC** Kayne Anderson BDC, Inc. | ROBO JAMES L | Director | $1.5M | 114,961 | $13.09 | [Form 4](https://www.sec.gov/Archives/edgar/data/1747172/000118325426000006/0001183254-26-000006-index.htm) |
| Diameter Dynamic Credit Fund | Lewinsohn Jonathan | Co-President | $1.0M | 98,814 | $10.12 | [Form 4](https://www.sec.gov/Archives/edgar/data/2067955/000119312526399896/0001193125-26-399896-index.htm) |
| **AXIA3** AXIA Energia S.A. | Batista de Lima Filho Pedro | Director | $960.0K | 91,000 | $10.55 | [Form 4](https://www.sec.gov/Archives/edgar/data/1439124/000121390026102459/0001213900-26-102459-index.htm) |
| **INBX** Inhibrx Biosciences, Inc. | Kayyem Jon Faiz | Director | $500.0K | 5,000 | $100.00 | [Form 4](https://www.sec.gov/Archives/edgar/data/2007919/000136626826000011/0001366268-26-000011-index.htm) |
| **INR** INFINITY NATURAL RESOURCES, INC. | Gieselman Scott | Director | $363.8K | 28,467 | $12.78 | [Form 4](https://www.sec.gov/Archives/edgar/data/1477713/000202911826000108/0002029118-26-000108-index.htm) |

## Biggest insider sales · filed 2026-09-23

| Company | Insider | Role | Value | Shares | Avg price | Filing |
|---|---|---|---:|---:|---:|---|
| **MEDP** Medpace Holdings, Inc. | Troendle August J. | President & CEO, Director, 10% Owner | $44.4M | 70,901 | $626.62 | [Form 4](https://www.sec.gov/Archives/edgar/data/1668397/000162205826000016/0001622058-26-000016-index.htm) |
| **HOOD** Robinhood Markets, Inc. | Tenev Vladimir | Chief Executive Officer, Director | $32.5M | 259,166 | $125.58 | [Form 4](https://www.sec.gov/Archives/edgar/data/1783879/000187100626000008/0001871006-26-000008-index.htm) |
| **META** Meta Platforms, Inc. | Cox Christopher K | Chief Product Officer | $28.5M | 40,000 | $712.76 | [Form 4](https://www.sec.gov/Archives/edgar/data/1607459/000095010326014403/0000950103-26-014403-index.htm) |
| **BEKE** KE Holdings Inc. | Shan Yigang | Executive Director, Director | $18.1M | 3,326,670 | $5.44 | [Form 4](https://www.sec.gov/Archives/edgar/data/1809587/000119312526398439/0001193125-26-398439-index.htm) |
| **AUGO** Aura Minerals Inc. | Sousa Mauad Bruno | Director | $15.0M | 166,000 | $90.65 | [Form 4](https://www.sec.gov/Archives/edgar/data/1468642/000211790526000042/0002117905-26-000042-index.htm) |

Full list: [`data/insider/2026/09/2026-09-23.md`](data/insider/2026/09/2026-09-23.md)

## Latest weekly recap

[2026-W38](data/weekly/2026-W38.md)

## How it works

- [`scripts/update.py`](scripts/update.py) (Python stdlib only) runs daily via [`.github/workflows/daily.yml`](.github/workflows/daily.yml).
- **Insider trades:** reads SEC EDGAR's daily index, parses every Form 4, and keeps open-market purchases (code `P`) and sales (code `S`).
- **Market:** closing prices for major index ETFs, the 11 S&P sector ETFs, and 40 large-cap stocks.
- **Weekly recap:** every Sunday, including cluster buys (multiple insiders buying the same company).
- Raw JSON lives in [`data/`](data) for anyone who wants to analyze it.

_Informational only, not investment advice. Data: SEC EDGAR (Form 4) and Yahoo Finance; may contain errors or delays._
