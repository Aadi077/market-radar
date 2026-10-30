# 📊 Market Radar

An automatically updated record of **insider trading** (SEC Form 4 open-market buys and sales) and **US market performance**, updated every weekday with a recap each Monday. Collected by GitHub Actions.

**Last updated:** 2026-10-29

## Market close · 2026-10-29

| Index | Close | Change |
|---|---:|---:|
| S&P 500 (SPY) | 769.36 | -0.38% |
| Nasdaq 100 (QQQ) | 715.34 | -1.42% |
| Dow 30 (DIA) | 522.73 | -0.37% |
| Russell 2000 (IWM) | 284.01 | +0.97% |

![Sector performance](charts/sectors-daily.svg)

**Top large-cap gainers:** **LLY** +6.63% · **MA** +4.16% · **GE** +3.96% · **MRK** +3.83% · **HD** +3.60%  
**Top large-cap decliners:** **GOOGL** -12.64% · **CRM** -4.63% · **AMZN** -4.25% · **INTC** -3.62% · **ORCL** -3.45%

## Biggest insider buys · filed 2026-10-28

| Company | Insider | Role | Value | Shares | Avg price | Filing |
|---|---|---|---:|---:|---:|---|
| **LONA** LeonaBio, Inc. | Portman David J. | 10% Owner | $9.9B | 3,149,470 | $3,149.47 | [Form 4](https://www.sec.gov/Archives/edgar/data/1620463/000212618626000002/0002126186-26-000002-index.htm) |
| **CRBG** Corebridge Financial, Inc. | NIPPON LIFE INSURANCE CO | 10% Owner | $6.4M | 182,826 | $34.95 | [Form 4](https://www.sec.gov/Archives/edgar/data/1889539/000119312526436365/0001193125-26-436365-index.htm) |
| **GOLD** Gold.com, Inc. | Tether Global Investments Fund, S.I.C.A.F., S.A., TPM, S.A. de C.V., Devasini Giancarlo | 10% Owner | $3.9M | 100,000 | $39.27 | [Form 4](https://www.sec.gov/Archives/edgar/data/2050373/000110465926119719/0001104659-26-119719-index.htm) |
| **ACN** Accenture plc | Sweet Julie Spellman | Chair and CEO, Director | $3.0M | 12,200 | $245.99 | [Form 4](https://www.sec.gov/Archives/edgar/data/1467373/000148763026000022/0001487630-26-000022-index.htm) |
| **BPRE** Bluerock Private Real Estate Fund | KAMFAR RAMIN | Director | $2.2M | 178,677 | $12.48 | [Form 4](https://www.sec.gov/Archives/edgar/data/1551047/000139834426019008/0001398344-26-019008-index.htm) |
| **TTMI** TTM TECHNOLOGIES INC | Ali Wajid | Director | $902.5K | 10,000 | $90.25 | [Form 4](https://www.sec.gov/Archives/edgar/data/1561100/000119312526436557/0001193125-26-436557-index.htm) |
| **XBIT** XBiotech Inc. | SIMARD JOHN | Director, 10% Owner | $711.3K | 368,524 | $1.93 | [Form 4](https://www.sec.gov/Archives/edgar/data/1639078/000119312526435894/0001193125-26-435894-index.htm) |
| Willow Tree Capital Corp | LIBERTY MUTUAL HOLDING Co INC. | 10% Owner | $529.3K | 33,187 | $15.95 | [Form 4](https://www.sec.gov/Archives/edgar/data/1142872/000119312526435749/0001193125-26-435749-index.htm) |
| **TTMI** TTM TECHNOLOGIES INC | Roks Edwin | President and CEO, Director | $440.4K | 5,000 | $88.07 | [Form 4](https://www.sec.gov/Archives/edgar/data/1705520/000119312526436562/0001193125-26-436562-index.htm) |
| **RCT** RedCloud Holdings plc | Senn Nikolaus Beat | Director, 10% Owner | $425.0K | 1,700,000 | $0.25 | [Form 4](https://www.sec.gov/Archives/edgar/data/2027360/000149315226048958/0001493152-26-048958-index.htm) |

## Biggest insider sales · filed 2026-10-28

| Company | Insider | Role | Value | Shares | Avg price | Filing |
|---|---|---|---:|---:|---:|---|
| **INSW** International Seaways, Inc. | Famatown Finance Ltd, GREENWICH HOLDINGS LTD., C.K. Ltd | 10% Owner | $25.0M | 203,738 | $122.76 | [Form 4](https://www.sec.gov/Archives/edgar/data/1731638/000091957426007290/0000919574-26-007290-index.htm) |
| **MEDP** Medpace Holdings, Inc. | BURWIG SUSAN E | Exec. VP, Operations | $13.5M | 20,000 | $677.00 | [Form 4](https://www.sec.gov/Archives/edgar/data/1677418/000167741826000018/0001677418-26-000018-index.htm) |
| **R** RYDER SYSTEM INC | SANCHEZ ROBERT E | Director | $9.7M | 34,614 | $281.66 | [Form 4](https://www.sec.gov/Archives/edgar/data/85961/000121693126000014/0001216931-26-000014-index.htm) |
| **BNY** Bank of New York Mellon Corp | Vince Robin A. | Chairman & CEO, Director | $7.4M | 50,000 | $147.81 | [Form 4](https://www.sec.gov/Archives/edgar/data/1390777/000119312526436233/0001193125-26-436233-index.htm) |
| **CBRS** Cerebras Systems Inc. | Lie Sean | Chief Technology Officer | $6.9M | 60,000 | $115.79 | [Form 4](https://www.sec.gov/Archives/edgar/data/2021728/000162828026067978/0001628280-26-067978-index.htm) |

Full list: [`data/insider/2026/10/2026-10-28.md`](data/insider/2026/10/2026-10-28.md)

## Latest weekly recap

[2026-W43](data/weekly/2026-W43.md)

## How it works

- [`scripts/update.py`](scripts/update.py) (Python stdlib only) runs every weekday via [`.github/workflows/daily.yml`](.github/workflows/daily.yml).
- **Insider trades:** reads SEC EDGAR's daily index, parses every Form 4, and keeps open-market purchases (code `P`) and sales (code `S`).
- **Market:** closing prices for major index ETFs, the 11 S&P sector ETFs, and 40 large-cap stocks.
- **Weekly recap:** every Monday, covering the week just ended, including cluster buys (multiple insiders buying the same company).
- Raw JSON lives in [`data/`](data) for anyone who wants to analyze it.

_Informational only, not investment advice. Data: SEC EDGAR (Form 4) and Yahoo Finance; may contain errors or delays._
