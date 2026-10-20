# 📊 Market Radar

An automatically updated record of **insider trading** (SEC Form 4 open-market buys and sales) and **US market performance**, updated every weekday with a recap each Monday. Collected by GitHub Actions.

**Last updated:** 2026-10-19

## Market close · 2026-10-16

| Index | Close | Change |
|---|---:|---:|
| S&P 500 (SPY) | 763.25 | -1.11% |
| Nasdaq 100 (QQQ) | 709.80 | -2.50% |
| Dow 30 (DIA) | 519.10 | -0.40% |
| Russell 2000 (IWM) | 270.44 | -1.69% |

![Sector performance](charts/sectors-daily.svg)

**Top large-cap gainers:** **CVX** +2.59% · **XOM** +2.46% · **PEP** +2.42% · **KO** +2.07% · **PG** +1.45%  
**Top large-cap decliners:** **PLTR** -7.22% · **AMD** -5.95% · **INTC** -5.79% · **ORCL** -4.64% · **AVGO** -4.52%

## Biggest insider buys · filed 2026-10-16

| Company | Insider | Role | Value | Shares | Avg price | Filing |
|---|---|---|---:|---:|---:|---|
| **SAFX** XCF Global, Inc. | EEME Energy SPV I, LLC | 10% Owner | $142.1M | 119,397,858 | $1.19 | [Form 4](https://www.sec.gov/Archives/edgar/data/2106572/000210657226000003/0002106572-26-000003-index.htm) |
| **PAM** Pampa Energy Inc. | Mindlin Marcos Marcelo | Director, 10% Owner | $35.1M | 435,000 | $80.78 | [Form 4](https://www.sec.gov/Archives/edgar/data/2022936/000202293626000017/0002022936-26-000017-index.htm) |
| **PEP** PEPSICO INC | POHLAD ROBERT C | Director | $23.7M | 184,646 | $128.28 | [Form 4](https://www.sec.gov/Archives/edgar/data/77476/000106127226000004/0001061272-26-000004-index.htm) |
| **CRBG** Corebridge Financial, Inc. | NIPPON LIFE INSURANCE CO | 10% Owner | $20.5M | 602,103 | $34.03 | [Form 4](https://www.sec.gov/Archives/edgar/data/1889539/000119312526424142/0001193125-26-424142-index.htm) |
| Keenova Therapeutics plc | GOLDENTREE ASSET MANAGEMENT LP, GoldenTree Asset Management LLC, Tananbaum Steven A. | 10% Owner | $12.3M | 137,000 | $90.00 | [Form 4](https://www.sec.gov/Archives/edgar/data/1278951/000149315226047403/0001493152-26-047403-index.htm) |
| **BORR** Borr Drilling Ltd | Troim Tor Olav | Director | $2.3M | 500,000 | $4.60 | [Form 4](https://www.sec.gov/Archives/edgar/data/1715497/000162828026066045/0001628280-26-066045-index.htm) |
| **BORR** Borr Drilling Ltd | Snowling Harvey Edward | Chief Operating Officer | $1.5M | 300,000 | $4.91 | [Form 4](https://www.sec.gov/Archives/edgar/data/1715497/000162828026066061/0001628280-26-066061-index.htm) |
| **SAH** SONIC AUTOMOTIVE INC | Rusnak Paul P. | 10% Owner | $752.0K | 12,555 | $59.90 | [Form 4](https://www.sec.gov/Archives/edgar/data/1460471/000146047126000009/0001460471-26-000009-index.htm) |
| **JOF** JAPAN SMALLER CAPITALIZATION FUND INC | Saba Capital Management, L.P. | 10% Owner | $161.9K | 13,133 | $12.33 | [Form 4](https://www.sec.gov/Archives/edgar/data/859796/000151028126000353/0001510281-26-000353-index.htm) |
| **GRCE** Grace Therapeutics, Inc. | Opaleye Management Inc. | 10% Owner | $136.2K | 71,065 | $1.92 | [Form 4](https://www.sec.gov/Archives/edgar/data/1444192/000149315226047473/0001493152-26-047473-index.htm) |

## Biggest insider sales · filed 2026-10-16

| Company | Insider | Role | Value | Shares | Avg price | Filing |
|---|---|---|---:|---:|---:|---|
| **INSW** International Seaways, Inc. | Famatown Finance Ltd, GREENWICH HOLDINGS LTD., C.K. Ltd | 10% Owner | $107.3M | 1,106,190 | $97.01 | [Form 4](https://www.sec.gov/Archives/edgar/data/1731638/000091957426007000/0000919574-26-007000-index.htm) |
| **NTRA** Natera, Inc. | Rabinowitz Matthew | EXECUTIVE CHAIRMAN, Director | $20.1M | 50,000 | $402.64 | [Form 4](https://www.sec.gov/Archives/edgar/data/1604821/000164638226000023/0001646382-26-000023-index.htm) |
| **MRNA** Moderna, Inc. | Hoge Stephen | President | $17.0M | 78,369 | $217.10 | [Form 4](https://www.sec.gov/Archives/edgar/data/1760669/000168285226000187/0001682852-26-000187-index.htm) |
| **NUAI** New ERA Energy & Digital, Inc. | MCCARTHY KENT C, KCM Capital Inc, AMC Fund, L.P. | 10% Owner | $15.5M | 4,290,000 | $3.62 | [Form 4](https://www.sec.gov/Archives/edgar/data/2160027/000122502826000007/0001225028-26-000007-index.htm) |
| **P** Everpure, Inc. | Colgrove John | Chief Visionary Officer, Director | $14.5M | 100,000 | $145.00 | [Form 4](https://www.sec.gov/Archives/edgar/data/1651902/000147443226000103/0001474432-26-000103-index.htm) |

Full list: [`data/insider/2026/10/2026-10-16.md`](data/insider/2026/10/2026-10-16.md)

## Latest weekly recap

[2026-W42](data/weekly/2026-W42.md)

## How it works

- [`scripts/update.py`](scripts/update.py) (Python stdlib only) runs every weekday via [`.github/workflows/daily.yml`](.github/workflows/daily.yml).
- **Insider trades:** reads SEC EDGAR's daily index, parses every Form 4, and keeps open-market purchases (code `P`) and sales (code `S`).
- **Market:** closing prices for major index ETFs, the 11 S&P sector ETFs, and 40 large-cap stocks.
- **Weekly recap:** every Monday, covering the week just ended, including cluster buys (multiple insiders buying the same company).
- Raw JSON lives in [`data/`](data) for anyone who wants to analyze it.

_Informational only, not investment advice. Data: SEC EDGAR (Form 4) and Yahoo Finance; may contain errors or delays._
