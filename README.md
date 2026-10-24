# 📊 Market Radar

An automatically updated record of **insider trading** (SEC Form 4 open-market buys and sales) and **US market performance**, updated every weekday with a recap each Monday. Collected by GitHub Actions.

**Last updated:** 2026-10-23

## Market close · 2026-10-22

| Index | Close | Change |
|---|---:|---:|
| S&P 500 (SPY) | 763.96 | -1.18% |
| Nasdaq 100 (QQQ) | 704.47 | -2.86% |
| Dow 30 (DIA) | 527.89 | +0.04% |
| Russell 2000 (IWM) | 276.67 | +0.07% |

![Sector performance](charts/sectors-daily.svg)

**Top large-cap gainers:** **ADBE** +6.07% · **PG** +5.58% · **HD** +4.33% · **JNJ** +3.81% · **CRM** +3.52%  
**Top large-cap decliners:** **AMD** -8.10% · **INTC** -8.04% · **META** -6.98% · **AMZN** -4.57% · **NVDA** -4.40%

## Biggest insider buys · filed 2026-10-22

| Company | Insider | Role | Value | Shares | Avg price | Filing |
|---|---|---|---:|---:|---:|---|
| 5C Lending Partners Corp. | MSD CAPITAL, L.P., MSD Portfolio L.P. - Investments, Noble Environmental Investments, LLC, DELL MICHAEL S | 10% Owner | $9.6M | 390,857 | $24.48 | [Form 4](https://www.sec.gov/Archives/edgar/data/1998387/000119312526429152/0001193125-26-429152-index.htm) |
| **DOLE** Dole plc | Pale Fire Capital SE, Pale Fire Capital SICAV a.s., Pale Fire Capital investicni spolecnost a.s., Senkypl Dusan, Barta Jan | 10% Owner | $8.6M | 648,356 | $13.19 | [Form 4](https://www.sec.gov/Archives/edgar/data/1892479/000092189526002845/0000921895-26-002845-index.htm) |
| **CRBG** Corebridge Financial, Inc. | NIPPON LIFE INSURANCE CO | 10% Owner | $6.8M | 193,357 | $35.01 | [Form 4](https://www.sec.gov/Archives/edgar/data/1889539/000119312526429089/0001193125-26-429089-index.htm) |
| **RAPP** Rapport Therapeutics, Inc. | PAUL STEVEN M | Director | $974.3K | 35,714 | $27.28 | [Form 4](https://www.sec.gov/Archives/edgar/data/1237564/000119312526429073/0001193125-26-429073-index.htm) |
| **MXF** MEXICO EQUITY & INCOME FUND INC | Saba Capital Management, L.P. | 10% Owner | $327.4K | 16,035 | $20.42 | [Form 4](https://www.sec.gov/Archives/edgar/data/863900/000151028126000373/0001510281-26-000373-index.htm) |
| **LEO** BNY MELLON STRATEGIC MUNICIPALS, INC. | Saba Capital Management, L.P. | 10% Owner | $262.6K | 45,831 | $5.73 | [Form 4](https://www.sec.gov/Archives/edgar/data/818972/000151028126000374/0001510281-26-000374-index.htm) |
| **RAPP** Rapport Therapeutics, Inc. | MARAGANORE JOHN | Director | $248.9K | 9,411 | $26.45 | [Form 4](https://www.sec.gov/Archives/edgar/data/1180432/000119312526429071/0001193125-26-429071-index.htm) |
| **API** Agora, Inc. | Zhao Bin | Chief Executive Officer, Director | $168.3K | 38,267 | $4.40 | [Form 4](https://www.sec.gov/Archives/edgar/data/1802883/000119312526429245/0001193125-26-429245-index.htm) |
| **DSM** BNY MELLON STRATEGIC MUNICIPAL BOND FUND, INC. | Saba Capital Management, L.P. | 10% Owner | $109.5K | 20,575 | $5.32 | [Form 4](https://www.sec.gov/Archives/edgar/data/855887/000151028126000372/0001510281-26-000372-index.htm) |
| **RAPP** Rapport Therapeutics, Inc. | Young Wendy B. | Director | $100.0K | 3,789 | $26.39 | [Form 4](https://www.sec.gov/Archives/edgar/data/2012593/000119312526429074/0001193125-26-429074-index.htm) |

## Biggest insider sales · filed 2026-10-22

| Company | Insider | Role | Value | Shares | Avg price | Filing |
|---|---|---|---:|---:|---:|---|
| **IHT** INNSUITES HOSPITALITY TRUST | WIRTH JAMES F | President & CEO, 10% Owner | $2.0B | 43,111 | $46,654.38 | [Form 4](https://www.sec.gov/Archives/edgar/data/82473/000149315226048149/0001493152-26-048149-index.htm) |
| **BRZE** Braze, Inc. | Hyman Jonathan | Chief Technology Officer | $13.2M | 295,000 | $44.81 | [Form 4](https://www.sec.gov/Archives/edgar/data/1676238/000188893526000028/0001888935-26-000028-index.htm) |
| **LIND** LINDBLAD EXPEDITIONS HOLDINGS, INC. | Lindblad Sven-Olof | Director, 10% Owner | $8.6M | 240,989 | $35.85 | [Form 4](https://www.sec.gov/Archives/edgar/data/1512499/000089706926001865/0000897069-26-001865-index.htm) |
| **ANET** Arista Networks, Inc. | Duda Kenneth | President and CTO, Director | $7.8M | 43,333 | $180.91 | [Form 4](https://www.sec.gov/Archives/edgar/data/1596532/000159653226000248/0001596532-26-000248-index.htm) |
| **ROIV** Roivant Sciences Ltd. | Venker Eric | President & Immunovant CEO | $7.0M | 200,000 | $35.11 | [Form 4](https://www.sec.gov/Archives/edgar/data/1635088/000163508826000116/0001635088-26-000116-index.htm) |

Full list: [`data/insider/2026/10/2026-10-22.md`](data/insider/2026/10/2026-10-22.md)

## Latest weekly recap

[2026-W42](data/weekly/2026-W42.md)

## How it works

- [`scripts/update.py`](scripts/update.py) (Python stdlib only) runs every weekday via [`.github/workflows/daily.yml`](.github/workflows/daily.yml).
- **Insider trades:** reads SEC EDGAR's daily index, parses every Form 4, and keeps open-market purchases (code `P`) and sales (code `S`).
- **Market:** closing prices for major index ETFs, the 11 S&P sector ETFs, and 40 large-cap stocks.
- **Weekly recap:** every Monday, covering the week just ended, including cluster buys (multiple insiders buying the same company).
- Raw JSON lives in [`data/`](data) for anyone who wants to analyze it.

_Informational only, not investment advice. Data: SEC EDGAR (Form 4) and Yahoo Finance; may contain errors or delays._
