# 📊 Market Radar

An automatically updated record of **insider trading** (SEC Form 4 open-market buys and sales) and **US market performance**, updated every weekday with a recap each Monday. Collected by GitHub Actions.

**Last updated:** 2026-11-05

## Market close · 2026-11-05

| Index | Close | Change |
|---|---:|---:|
| S&P 500 (SPY) | 733.00 | -4.41% |
| Nasdaq 100 (QQQ) | 647.05 | -6.49% |
| Dow 30 (DIA) | 514.27 | -3.53% |
| Russell 2000 (IWM) | 270.98 | -4.59% |

![Sector performance](charts/sectors-daily.svg)

**Top large-cap gainers:** **COST** +1.83% · **PEP** +0.20% · **KO** -0.07% · **PG** -0.13% · **MCD** -0.78%  
**Top large-cap decliners:** **AMD** -17.26% · **TSLA** -10.77% · **AVGO** -10.43% · **INTC** -10.33% · **PLTR** -9.73%

## Biggest insider buys · filed 2026-11-04

| Company | Insider | Role | Value | Shares | Avg price | Filing |
|---|---|---|---:|---:|---:|---|
| **KNOP** KNOT Offshore Partners LP | Seglem Trygve | Director | $43.5M | 2,083,333 | $20.88 | [Form 4](https://www.sec.gov/Archives/edgar/data/1564180/000110465926122691/0001104659-26-122691-index.htm) |
| Partners Group Growth, LLC | Partners Group Finance (USD) AG |  | $20.0M | 9,513,390 | $2.10 | [Form 4](https://www.sec.gov/Archives/edgar/data/2089261/000208926126000008/0002089261-26-000008-index.htm) |
| **ASPE** Aspen Neuroscience, Inc. | ORBIMED ADVISORS LLC, OrbiMed Capital GP VII LLC | Director, 10% Owner | $15.0M | 1,000,000 | $15.00 | [Form 4](https://www.sec.gov/Archives/edgar/data/2124080/000094787126000980/0000947871-26-000980-index.htm) |
| **ASPE** Aspen Neuroscience, Inc. | Thompson Peter A. | Director, 10% Owner | $15.0M | 1,000,000 | $15.00 | [Form 4](https://www.sec.gov/Archives/edgar/data/2124080/000094787126000981/0000947871-26-000981-index.htm) |
| **DOLE** Dole plc | Pale Fire Capital SE, Pale Fire Capital SICAV a.s., Pale Fire Capital investicni spolecnost a.s., Senkypl Dusan, Barta Jan | 10% Owner | $12.9M | 986,557 | $13.10 | [Form 4](https://www.sec.gov/Archives/edgar/data/1892479/000092189526002932/0000921895-26-002932-index.htm) |
| **INTC** INTEL CORP | TAN LIP BU | CEO, Director | $9.7M | 150,000 | $64.73 | [Form 4](https://www.sec.gov/Archives/edgar/data/50863/000005086326000195/0000050863-26-000195-index.htm) |
| **CRBG** Corebridge Financial, Inc. | NIPPON LIFE INSURANCE CO | 10% Owner | $6.7M | 190,251 | $35.23 | [Form 4](https://www.sec.gov/Archives/edgar/data/1889539/000119312526447693/0001193125-26-447693-index.htm) |
| **LRN** Stride, Inc. | Shepherd Brian A. | Director | $1.7M | 22,000 | $75.90 | [Form 4](https://www.sec.gov/Archives/edgar/data/1567675/000156767526000007/0001567675-26-000007-index.htm) |
| **CACC** CREDIT ACCEPTANCE CORP | TRYFOROS THOMAS N | Director | $1.5M | 3,000 | $485.20 | [Form 4](https://www.sec.gov/Archives/edgar/data/885550/000088555026000203/0000885550-26-000203-index.htm) |
| **AN** AUTONATION, INC. | Manley Michael Mark | CEO and Director, Director | $1.0M | 5,600 | $184.11 | [Form 4](https://www.sec.gov/Archives/edgar/data/350698/000151899226000004/0001518992-26-000004-index.htm) |

## Biggest insider sales · filed 2026-11-04

| Company | Insider | Role | Value | Shares | Avg price | Filing |
|---|---|---|---:|---:|---:|---|
| **BROS** Dutch Bros Inc. | Boersma Travis | Executive Chairman of Board, Director, 10% Owner | $106.4M | 2,388,812 | $44.55 | [Form 4](https://www.sec.gov/Archives/edgar/data/1883154/000186658126000188/0001866581-26-000188-index.htm) |
| **BROS** Dutch Bros Inc. | DM Trust Aggregator, LLC | 10% Owner | $69.4M | 1,557,332 | $44.55 | [Form 4](https://www.sec.gov/Archives/edgar/data/1883105/000186658126000184/0001866581-26-000184-index.htm) |
| **BROS** Dutch Bros Inc. | DM Individual Aggregator, LLC | 10% Owner | $37.0M | 831,480 | $44.55 | [Form 4](https://www.sec.gov/Archives/edgar/data/1883096/000186658126000186/0001866581-26-000186-index.htm) |
| **REGN** REGENERON PHARMACEUTICALS, INC. | SING GEORGE L | Director | $20.4M | 21,129 | $964.38 | [Form 4](https://www.sec.gov/Archives/edgar/data/872589/000122547126000004/0001225471-26-000004-index.htm) |
| **DBX** DROPBOX, INC. | Houston Andrew | Co-CEO, Director, 10% Owner | $13.7M | 383,800 | $35.81 | [Form 4](https://www.sec.gov/Archives/edgar/data/1467623/000173456326000024/0001734563-26-000024-index.htm) |

Full list: [`data/insider/2026/11/2026-11-04.md`](data/insider/2026/11/2026-11-04.md)

## Latest weekly recap

[2026-W44](data/weekly/2026-W44.md)

## How it works

- [`scripts/update.py`](scripts/update.py) (Python stdlib only) runs every weekday via [`.github/workflows/daily.yml`](.github/workflows/daily.yml).
- **Insider trades:** reads SEC EDGAR's daily index, parses every Form 4, and keeps open-market purchases (code `P`) and sales (code `S`).
- **Market:** closing prices for major index ETFs, the 11 S&P sector ETFs, and 40 large-cap stocks.
- **Weekly recap:** every Monday, covering the week just ended, including cluster buys (multiple insiders buying the same company).
- Raw JSON lives in [`data/`](data) for anyone who wants to analyze it.

_Informational only, not investment advice. Data: SEC EDGAR (Form 4) and Yahoo Finance; may contain errors or delays._
