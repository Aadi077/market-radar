# 📊 Market Radar

An automatically updated record of **insider trading** (SEC Form 4 open-market buys and sales) and **US market performance**, updated every weekday with a recap each Monday. Collected by GitHub Actions.

**Last updated:** 2026-11-19

## Market close · 2026-11-19

| Index | Close | Change |
|---|---:|---:|
| S&P 500 (SPY) | 715.87 | -1.96% |
| Nasdaq 100 (QQQ) | 645.04 | -2.19% |
| Dow 30 (DIA) | 490.79 | -2.18% |
| Russell 2000 (IWM) | 264.22 | -2.18% |

![Sector performance](charts/sectors-daily.svg)

**Top large-cap gainers:** **INTC** +1.92% · **CVX** +0.30% · **COST** -0.25% · **HD** -0.28% · **WFC** -0.38%  
**Top large-cap decliners:** **AMD** -7.72% · **UNH** -5.55% · **AMZN** -3.87% · **CRM** -3.72% · **MRK** -3.61%

## Biggest insider buys · filed 2026-11-18

| Company | Insider | Role | Value | Shares | Avg price | Filing |
|---|---|---|---:|---:|---:|---|
| **WWB** WINDWARD BIO GROUP AG | Stampacchia Otello | Director | $29.8M | 1,750,000 | $17.00 | [Form 4](https://www.sec.gov/Archives/edgar/data/1361712/000136171226000011/0001361712-26-000011-index.htm) |
| John Hancock GA Mortgage Trust | Manulife (International) Ltd | 10% Owner | $21.0M | 1,175,377 | $17.87 | [Form 4](https://www.sec.gov/Archives/edgar/data/1742952/000176551826000007/0001765518-26-000007-index.htm) |
| **WWB** WINDWARD BIO GROUP AG | Bonita David P | Director, 10% Owner | $20.0M | 1,176,471 | $17.00 | [Form 4](https://www.sec.gov/Archives/edgar/data/1572451/000094787126001039/0000947871-26-001039-index.htm) |
| **WWB** WINDWARD BIO GROUP AG | ORBIMED ADVISORS LLC, OrbiMed Capital GP IX LLC | Director, 10% Owner | $20.0M | 1,176,471 | $17.00 | [Form 4](https://www.sec.gov/Archives/edgar/data/1055951/000094787126001038/0000947871-26-001038-index.htm) |
| **ANAB** ANAPTYSBIO, INC | EcoR1 Capital, LLC, NODELMAN OLEG | Director, 10% Owner | $17.2M | 374,580 | $45.98 | [Form 4](https://www.sec.gov/Archives/edgar/data/1370053/000093583626000631/0000935836-26-000631-index.htm) |
| John Hancock GA Mortgage Trust | Manufacturers Life Reinsurance Ltd | 10% Owner | $9.0M | 503,733 | $17.87 | [Form 4](https://www.sec.gov/Archives/edgar/data/1742952/000176549626000021/0001765496-26-000021-index.htm) |
| John Hancock GA Mortgage Trust | Manulife (Singapore) Pte. Ltd. | 10% Owner | $9.0M | 503,733 | $17.87 | [Form 4](https://www.sec.gov/Archives/edgar/data/1742952/000183747826000019/0001837478-26-000019-index.htm) |
| **FUN** Six Flags Entertainment Corporation/NEW | JAFFER REHAN | Director | $6.4M | 550,000 | $11.55 | [Form 4](https://www.sec.gov/Archives/edgar/data/1364501/000199900126000121/0001999001-26-000121-index.htm) |
| **PAM** Pampa Energy Inc. | Mindlin Marcos Marcelo | Director, 10% Owner | $4.0M | 63,548 | $63.14 | [Form 4](https://www.sec.gov/Archives/edgar/data/2022936/000202293626000019/0002022936-26-000019-index.htm) |
| **BPRE** Bluerock Private Real Estate Fund | KAMFAR RAMIN | Director | $3.2M | 265,854 | $12.13 | [Form 4](https://www.sec.gov/Archives/edgar/data/1551047/000139834426020292/0001398344-26-020292-index.htm) |

## Biggest insider sales · filed 2026-11-18

| Company | Insider | Role | Value | Shares | Avg price | Filing |
|---|---|---|---:|---:|---:|---|
| **LOAR** Loar Holdings Inc. | ABRAMS CAPITAL MANAGEMENT, L.P., ABRAMS CAPITAL MANAGEMENT, LLC, ABRAMS CAPITAL, LLC, Abrams Capital Partners II, L.P., Riva Capital Management IV, LLC, Riva IV CV, L.P., Riva Capital Management V, LLC, Riva Capital Partners V, L.P. | 10% Owner | $182.9M | 2,661,613 | $68.70 | [Form 4](https://www.sec.gov/Archives/edgar/data/1358706/000119312526467217/0001193125-26-467217-index.htm) |
| **LOAR** Loar Holdings Inc. | Abrams David C | Director, 10% Owner | $182.9M | 2,661,613 | $68.70 | [Form 4](https://www.sec.gov/Archives/edgar/data/1292250/000119312526467230/0001193125-26-467230-index.htm) |
| **LOAR** Loar Holdings Inc. | Bobbili Raja | Director, 10% Owner | $182.9M | 2,661,613 | $68.70 | [Form 4](https://www.sec.gov/Archives/edgar/data/2021281/000119312526467208/0001193125-26-467208-index.htm) |
| **LOAR** Loar Holdings Inc. | Bomberg Alison | Director, 10% Owner | $182.9M | 2,661,613 | $68.70 | [Form 4](https://www.sec.gov/Archives/edgar/data/2021288/000119312526467225/0001193125-26-467225-index.htm) |
| **LOAR** Loar Holdings Inc. | Carpenito Anthony | Director, 10% Owner | $182.9M | 2,661,613 | $68.70 | [Form 4](https://www.sec.gov/Archives/edgar/data/2020972/000119312526467246/0001193125-26-467246-index.htm) |

Full list: [`data/insider/2026/11/2026-11-18.md`](data/insider/2026/11/2026-11-18.md)

## Latest weekly recap

[2026-W46](data/weekly/2026-W46.md)

## How it works

- [`scripts/update.py`](scripts/update.py) (Python stdlib only) runs every weekday via [`.github/workflows/daily.yml`](.github/workflows/daily.yml).
- **Insider trades:** reads SEC EDGAR's daily index, parses every Form 4, and keeps open-market purchases (code `P`) and sales (code `S`).
- **Market:** closing prices for major index ETFs, the 11 S&P sector ETFs, and 40 large-cap stocks.
- **Weekly recap:** every Monday, covering the week just ended, including cluster buys (multiple insiders buying the same company).
- Raw JSON lives in [`data/`](data) for anyone who wants to analyze it.

_Informational only, not investment advice. Data: SEC EDGAR (Form 4) and Yahoo Finance; may contain errors or delays._
