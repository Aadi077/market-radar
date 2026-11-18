# 📊 Market Radar

An automatically updated record of **insider trading** (SEC Form 4 open-market buys and sales) and **US market performance**, updated every weekday with a recap each Monday. Collected by GitHub Actions.

**Last updated:** 2026-11-17

## Market close · 2026-11-17

| Index | Close | Change |
|---|---:|---:|
| S&P 500 (SPY) | 732.44 | -1.01% |
| Nasdaq 100 (QQQ) | 656.95 | -0.73% |
| Dow 30 (DIA) | 507.31 | -1.62% |
| Russell 2000 (IWM) | 269.05 | -1.43% |

![Sector performance](charts/sectors-daily.svg)

**Top large-cap gainers:** **AVGO** +2.46% · **CSCO** +0.62% · **MCD** +0.42% · **GE** +0.38% · **XOM** +0.20%  
**Top large-cap decliners:** **CRM** -9.45% · **UNH** -5.42% · **IBM** -4.71% · **ADBE** -4.25% · **ORCL** -3.43%

## Biggest insider buys · filed 2026-11-16

| Company | Insider | Role | Value | Shares | Avg price | Filing |
|---|---|---|---:|---:|---:|---|
| **EMO** ClearBridge Energy Midstream Opportunity Fund Inc. | PRUDENTIAL FINANCIAL INC, PRUCO LIFE INSURANCE CO | 10% Owner | $35.0M | 1,000,000 | $35.00 | [Form 4](https://www.sec.gov/Archives/edgar/data/1517518/000113777426000240/0001137774-26-000240-index.htm) |
| **HUBS** HUBSPOT INC | Halligan Brian | Chief Executive Officer, Director | $5.0M | 22,985 | $217.44 | [Form 4](https://www.sec.gov/Archives/edgar/data/1404655/000119312526462154/0001193125-26-462154-index.htm) |
| **TEAM** Atlassian Corp | Cannon-Brookes Michael | CEO, Co-Founder, Director, 10% Owner | $2.0M | 13,400 | $150.06 | [Form 4](https://www.sec.gov/Archives/edgar/data/1650372/000166612026000035/0001666120-26-000035-index.htm) |
| **SONO** Sonos Inc | Kennedy Joseph Jude | Director | $1.9M | 100,000 | $18.71 | [Form 4](https://www.sec.gov/Archives/edgar/data/1806159/000131472726000106/0001314727-26-000106-index.htm) |
| **KURA** Kura Oncology, Inc. | WILSON TROY EDWARD | President and CEO, Director | $1.5M | 200,000 | $7.52 | [Form 4](https://www.sec.gov/Archives/edgar/data/1422143/000119312526464166/0001193125-26-464166-index.htm) |
| **PAM** Pampa Energy Inc. | Mindlin Damian Miguel | Vicepresident | $1.4M | 22,700 | $63.29 | [Form 4](https://www.sec.gov/Archives/edgar/data/2028916/000202891626000015/0002028916-26-000015-index.htm) |
| **OIG** Orion180 Insurance Group Inc. | Gregg Kenneth | Chief Executive Officer, Director, 10% Owner | $1.0M | 96,150 | $10.66 | [Form 4](https://www.sec.gov/Archives/edgar/data/2135086/000149315226052496/0001493152-26-052496-index.htm) |
| **SKYD** Skydance Corp | Cardinale Gerald J. | Director | $1.0M | 129,650 | $7.72 | [Form 4](https://www.sec.gov/Archives/edgar/data/1447258/000089534526000491/0000895345-26-000491-index.htm) |
| **BRSP** BrightSpire Capital, Inc. | Mazzei Michael | CEO, Director | $1.0M | 309,113 | $3.24 | [Form 4](https://www.sec.gov/Archives/edgar/data/1717547/000159842426000011/0001598424-26-000011-index.htm) |
| **AMG** AFFILIATED MANAGERS GROUP, INC. | Cates G. Staley | Director | $1.0M | 2,500 | $400.00 | [Form 4](https://www.sec.gov/Archives/edgar/data/1004434/000100443426000110/0001004434-26-000110-index.htm) |

## Biggest insider sales · filed 2026-11-16

| Company | Insider | Role | Value | Shares | Avg price | Filing |
|---|---|---|---:|---:|---:|---|
| **LFST** LifeStance Health Group, Inc. | TPG GP A, LLC, COULTER JAMES G, WINKELRIED JON | 10% Owner | $484.8M | 37,233,110 | $13.02 | [Form 4](https://www.sec.gov/Archives/edgar/data/1099776/000199937126025503/0001999371-26-025503-index.htm) |
| **CPRI** Capri Holdings Ltd | IDOL JOHN D | Chairman & CEO, Director | $46.9M | 2,384,806 | $19.68 | [Form 4](https://www.sec.gov/Archives/edgar/data/1530721/000095014226003079/0000950142-26-003079-index.htm) |
| **RCL** ROYAL CARIBBEAN CRUISES LTD | Wilhelmsen Arne Alexander | Director | $28.4M | 88,326 | $321.80 | [Form 4](https://www.sec.gov/Archives/edgar/data/884887/000131734526000024/0001317345-26-000024-index.htm) |
| **DBX** DROPBOX, INC. | Houston Andrew | Co-CEO, Director, 10% Owner | $26.7M | 798,744 | $33.47 | [Form 4](https://www.sec.gov/Archives/edgar/data/1467623/000173456326000027/0001734563-26-000027-index.htm) |
| **MSI** Motorola Solutions, Inc. | BROWN GREGORY Q | Chairman and CEO, Director | $21.6M | 40,500 | $533.53 | [Form 4](https://www.sec.gov/Archives/edgar/data/1201232/000120123226000025/0001201232-26-000025-index.htm) |

Full list: [`data/insider/2026/11/2026-11-16.md`](data/insider/2026/11/2026-11-16.md)

## Latest weekly recap

[2026-W46](data/weekly/2026-W46.md)

## How it works

- [`scripts/update.py`](scripts/update.py) (Python stdlib only) runs every weekday via [`.github/workflows/daily.yml`](.github/workflows/daily.yml).
- **Insider trades:** reads SEC EDGAR's daily index, parses every Form 4, and keeps open-market purchases (code `P`) and sales (code `S`).
- **Market:** closing prices for major index ETFs, the 11 S&P sector ETFs, and 40 large-cap stocks.
- **Weekly recap:** every Monday, covering the week just ended, including cluster buys (multiple insiders buying the same company).
- Raw JSON lives in [`data/`](data) for anyone who wants to analyze it.

_Informational only, not investment advice. Data: SEC EDGAR (Form 4) and Yahoo Finance; may contain errors or delays._
