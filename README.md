# 📊 Market Radar

A daily, automatically updated record of **insider trading** (SEC Form 4 open-market buys and sales) and **US market performance**, with a weekly recap every Sunday. Collected by GitHub Actions.

**Last updated:** 2026-09-30

## Market close · 2026-09-29

| Index | Close | Change |
|---|---:|---:|
| S&P 500 (SPY) | 764.20 | -0.18% |
| Nasdaq 100 (QQQ) | 737.93 | +0.19% |
| Dow 30 (DIA) | 512.88 | -0.22% |
| Russell 2000 (IWM) | 279.01 | -0.36% |

![Sector performance](charts/sectors-daily.svg)

**Top large-cap gainers:** **ORCL** +3.91% · **META** +3.24% · **AVGO** +1.58% · **NFLX** +1.55% · **ADBE** +0.94%  
**Top large-cap decliners:** **AAPL** -2.66% · **WMT** -1.78% · **JNJ** -1.61% · **TSLA** -1.29% · **ABBV** -1.12%

## Biggest insider buys · filed 2026-09-29

| Company | Insider | Role | Value | Shares | Avg price | Filing |
|---|---|---|---:|---:|---:|---|
| **ADRX** ADARx Pharmaceuticals, Inc. | George Simeon | Director, 10% Owner | $27.2M | 1,600,000 | $17.00 | [Form 4](https://www.sec.gov/Archives/edgar/data/1802369/000119312526408061/0001193125-26-408061-index.htm) |
| **ADRX** ADARx Pharmaceuticals, Inc. | SR ONE CAPITAL MANAGEMENT, LLC | 10% Owner | $27.2M | 1,600,000 | $17.00 | [Form 4](https://www.sec.gov/Archives/edgar/data/1802369/000119312526408064/0001193125-26-408064-index.htm) |
| **COUR** Coursera, Inc. | Pale Fire Capital SE, Pale Fire Capital SICAV a.s., Pale Fire Capital investicni spolecnost a.s., Senkypl Dusan, Barta Jan | 10% Owner | $11.4M | 2,332,742 | $4.87 | [Form 4](https://www.sec.gov/Archives/edgar/data/1892479/000092189526002677/0000921895-26-002677-index.htm) |
| **GME** GameStop Corp. | Cohen Ryan | President, CEO and Chairman, Director | $10.6M | 450,000 | $23.48 | [Form 4](https://www.sec.gov/Archives/edgar/data/1767470/000092189526002670/0000921895-26-002670-index.htm) |
| **CRBG** Corebridge Financial, Inc. | NIPPON LIFE INSURANCE CO | 10% Owner | $6.2M | 178,840 | $34.52 | [Form 4](https://www.sec.gov/Archives/edgar/data/1889539/000119312526407701/0001193125-26-407701-index.htm) |
| **PAM** Pampa Energy Inc. | Mariani Gustavo | Vicepresident | $2.0M | 25,000 | $78.26 | [Form 4](https://www.sec.gov/Archives/edgar/data/2028917/000202891726000003/0002028917-26-000003-index.htm) |
| **PRTA** PROTHENA CORP PUBLIC LTD CO | SCULLY WILLIAM P | 10% Owner | $889.9K | 103,500 | $8.60 | [Form 4](https://www.sec.gov/Archives/edgar/data/1559053/000104546326000017/0001045463-26-000017-index.htm) |
| **HGBL** Heritage Global Inc. | Burnham William L | Director | $399.0K | 300,000 | $1.33 | [Form 4](https://www.sec.gov/Archives/edgar/data/1248150/000119312526407271/0001193125-26-407271-index.htm) |
| **CRAFX** Cascade Real Assets Fund | Williams Paul Jay | Director | $300.0K | 30,000 | $10.00 | [Form 4](https://www.sec.gov/Archives/edgar/data/2114459/000121390026104418/0001213900-26-104418-index.htm) |
| **QTEX** QTREX Quantum Ltd. | Ben-Noon Dagi Shahar | Chief Executive Officer, Director | $119.5K | 168,894 | $0.71 | [Form 4](https://www.sec.gov/Archives/edgar/data/1911928/000118518526004397/0001185185-26-004397-index.htm) |

## Biggest insider sales · filed 2026-09-29

| Company | Insider | Role | Value | Shares | Avg price | Filing |
|---|---|---|---:|---:|---:|---|
| **BEKE** KE Holdings Inc. | Peng Yongdong | Chief Executive Officer, Director | $84.6M | 16,033,983 | $5.27 | [Form 4](https://www.sec.gov/Archives/edgar/data/1809587/000119312526405896/0001193125-26-405896-index.htm) |
| **CRDO** Credo Technology Group Holding Ltd | Lam Yat Tung | Chief Operating Officer, Director | $20.6M | 100,000 | $206.29 | [Form 4](https://www.sec.gov/Archives/edgar/data/1807794/000162828026063815/0001628280-26-063815-index.htm) |
| **BRK.A** BERKSHIRE HATHAWAY INC | Jain Ajit | Vice Chairman, Director | $20.0M | 39,700 | $503.09 | [Form 4](https://www.sec.gov/Archives/edgar/data/1067983/000172845126000004/0001728451-26-000004-index.htm) |
| **ANET** Arista Networks, Inc. | Ullal Jayshree | CEO and Chairperson, Director | $13.2M | 62,622 | $211.40 | [Form 4](https://www.sec.gov/Archives/edgar/data/1596532/000159653226000234/0001596532-26-000234-index.htm) |
| **P** Everpure, Inc. | Colgrove John | Chief Visionary Officer, Director | $12.5M | 100,000 | $124.63 | [Form 4](https://www.sec.gov/Archives/edgar/data/1651902/000147443226000096/0001474432-26-000096-index.htm) |

Full list: [`data/insider/2026/09/2026-09-29.md`](data/insider/2026/09/2026-09-29.md)

## Latest weekly recap

[2026-W39](data/weekly/2026-W39.md)

## How it works

- [`scripts/update.py`](scripts/update.py) (Python stdlib only) runs daily via [`.github/workflows/daily.yml`](.github/workflows/daily.yml).
- **Insider trades:** reads SEC EDGAR's daily index, parses every Form 4, and keeps open-market purchases (code `P`) and sales (code `S`).
- **Market:** closing prices for major index ETFs, the 11 S&P sector ETFs, and 40 large-cap stocks.
- **Weekly recap:** every Sunday, including cluster buys (multiple insiders buying the same company).
- Raw JSON lives in [`data/`](data) for anyone who wants to analyze it.

_Informational only, not investment advice. Data: SEC EDGAR (Form 4) and Yahoo Finance; may contain errors or delays._
