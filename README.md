# 📊 Market Radar

An automatically updated record of **insider trading** (SEC Form 4 open-market buys and sales) and **US market performance**, updated every weekday with a recap each Monday. Collected by GitHub Actions.

**Last updated:** 2026-11-18

## Market close · 2026-11-18

| Index | Close | Change |
|---|---:|---:|
| S&P 500 (SPY) | 730.20 | -0.31% |
| Nasdaq 100 (QQQ) | 659.51 | +0.39% |
| Dow 30 (DIA) | 501.73 | -1.10% |
| Russell 2000 (IWM) | 270.12 | +0.40% |

![Sector performance](charts/sectors-daily.svg)

**Top large-cap gainers:** **AMD** +5.31% · **DIS** +4.63% · **AMZN** +3.82% · **AVGO** +3.64% · **CSCO** +2.18%  
**Top large-cap decliners:** **UNH** -10.21% · **CVX** -4.74% · **XOM** -3.97% · **ADBE** -3.97% · **MRK** -3.90%

## Biggest insider buys · filed 2026-11-17

| Company | Insider | Role | Value | Shares | Avg price | Filing |
|---|---|---|---:|---:|---:|---|
| **PEPG** PepGen Inc. | RA CAPITAL MANAGEMENT, L.P., RA Capital Healthcare Fund LP, RA Capital Nexus Fund II, L.P., Kolchinsky Peter, Shah Rajeev M. | Director, 10% Owner | $43.1M | 8,625,000 | $5.00 | [Form 4](https://www.sec.gov/Archives/edgar/data/1384859/000123191926001588/0001231919-26-001588-index.htm) |
| **NFRX** 2023 ETF Series Trust | Harrison Street Real Assets Fund LLC | 10% Owner | $10.8M | 403,135 | $26.79 | [Form 4](https://www.sec.gov/Archives/edgar/data/1969674/000168789826000013/0001687898-26-000013-index.htm) |
| **ANGX** Angel Studios, Inc. | Sarowitz Steven I | Director | $4.6M | 1,000,000 | $4.63 | [Form 4](https://www.sec.gov/Archives/edgar/data/1865200/000186520026000102/0001865200-26-000102-index.htm) |
| **STUB** StubHub Holdings, Inc. | Raab Andrew John | Director | $2.0M | 400,000 | $5.12 | [Form 4](https://www.sec.gov/Archives/edgar/data/1560034/000162828026074600/0001628280-26-074600-index.htm) |
| **TEAM** Atlassian Corp | Cannon-Brookes Michael | CEO, Co-Founder, Director, 10% Owner | $2.0M | 13,400 | $149.16 | [Form 4](https://www.sec.gov/Archives/edgar/data/1650372/000166612026000036/0001666120-26-000036-index.htm) |
| **STUB** StubHub Holdings, Inc. | Bhargava Sameer | Director | $1.5M | 282,500 | $5.31 | [Form 4](https://www.sec.gov/Archives/edgar/data/2028011/000162828026074602/0001628280-26-074602-index.htm) |
| **HRNG** HALLADOR ENERGY CO | Wesley Charles Ray IV | Director | $1.1M | 100,000 | $10.70 | [Form 4](https://www.sec.gov/Archives/edgar/data/788965/000162828026074438/0001628280-26-074438-index.htm) |
| **DKNG** DraftKings Inc. | Kalish Matthew | Director | $1.0M | 55,000 | $18.22 | [Form 4](https://www.sec.gov/Archives/edgar/data/1883685/000181019026000018/0001810190-26-000018-index.htm) |
| **LPG** DORIAN LPG LTD. | HADJIPATERAS JOHN C | President and CEO, Director, 10% Owner | $961.5K | 20,000 | $48.07 | [Form 4](https://www.sec.gov/Archives/edgar/data/1596993/000091957426008172/0000919574-26-008172-index.htm) |
| **UPST** Upstart Holdings, Inc. | Gu Paul | Chief Executive Officer, Director | $950.0K | 50,000 | $19.00 | [Form 4](https://www.sec.gov/Archives/edgar/data/1832812/000183281226000014/0001832812-26-000014-index.htm) |

## Biggest insider sales · filed 2026-11-17

| Company | Insider | Role | Value | Shares | Avg price | Filing |
|---|---|---|---:|---:|---:|---|
| **ITGR** Integer Holdings Corp | Tarheel Investors III L.P., Tarheel Investors III GP LLC, KKR North America Fund XIV SCSp, KKR Associates North America XIV SCSp, KKR North America XIV S.a r.l., KKR Associates Group L.P., KKR Associates Group GP LLC | 10% Owner | $603.7M | 4,753,677 | $127.00 | [Form 4](https://www.sec.gov/Archives/edgar/data/1114483/000114036126044508/0001140361-26-044508-index.htm) |
| **ITGR** Integer Holdings Corp | KKR Group Partnership L.P., KKR Group Holdings Corp., KKR Group Co. Inc., KKR & Co. Inc., KKR Management LLP, KRAVIS HENRY R, ROBERTS GEORGE R | 10% Owner | $603.7M | 4,753,677 | $127.00 | [Form 4](https://www.sec.gov/Archives/edgar/data/1114483/000114036126044509/0001140361-26-044509-index.htm) |
| **TYL** TYLER TECHNOLOGIES INC | MOORE H LYNN JR | President and CEO, Director | $12.8M | 30,000 | $427.40 | [Form 4](https://www.sec.gov/Archives/edgar/data/1250902/000213003526000009/0002130035-26-000009-index.htm) |
| **WSM** WILLIAMS SONOMA INC | ALBER LAURA | PRESIDENT & CEO, Director | $8.9M | 35,000 | $254.03 | [Form 4](https://www.sec.gov/Archives/edgar/data/1225922/000071995526000239/0000719955-26-000239-index.htm) |
| **CSCO** CISCO SYSTEMS, INC. | Stahlkopf Deborah L | EVP and Chief Legal Officer | $7.9M | 83,345 | $94.64 | [Form 4](https://www.sec.gov/Archives/edgar/data/858877/000085887726000194/0000858877-26-000194-index.htm) |

Full list: [`data/insider/2026/11/2026-11-17.md`](data/insider/2026/11/2026-11-17.md)

## Latest weekly recap

[2026-W46](data/weekly/2026-W46.md)

## How it works

- [`scripts/update.py`](scripts/update.py) (Python stdlib only) runs every weekday via [`.github/workflows/daily.yml`](.github/workflows/daily.yml).
- **Insider trades:** reads SEC EDGAR's daily index, parses every Form 4, and keeps open-market purchases (code `P`) and sales (code `S`).
- **Market:** closing prices for major index ETFs, the 11 S&P sector ETFs, and 40 large-cap stocks.
- **Weekly recap:** every Monday, covering the week just ended, including cluster buys (multiple insiders buying the same company).
- Raw JSON lives in [`data/`](data) for anyone who wants to analyze it.

_Informational only, not investment advice. Data: SEC EDGAR (Form 4) and Yahoo Finance; may contain errors or delays._
