# 📊 Market Radar

A daily, automatically updated record of **insider trading** (SEC Form 4 open-market buys and sales) and **US market performance**, with a weekly recap every Sunday. Collected by GitHub Actions.

**Last updated:** 2026-09-19

## Market close · 2026-09-18

| Index | Close | Change |
|---|---:|---:|
| S&P 500 (SPY) | 761.69 | -0.12% |
| Nasdaq 100 (QQQ) | 721.45 | +0.63% |
| Dow 30 (DIA) | 515.88 | -0.48% |
| Russell 2000 (IWM) | 284.10 | -0.47% |

![Sector performance](charts/sectors-daily.svg)

**Top large-cap gainers:** **AVGO** +2.97% · **AMD** +2.70% · **NVDA** +1.34% · **AMZN** +1.00% · **PLTR** +0.79%  
**Top large-cap decliners:** **NFLX** -4.67% · **IBM** -3.45% · **PEP** -2.93% · **DIS** -2.54% · **META** -2.43%

## Biggest insider buys · filed 2026-09-18

| Company | Insider | Role | Value | Shares | Avg price | Filing |
|---|---|---|---:|---:|---:|---|
| **CRBG** Corebridge Financial, Inc. | NIPPON LIFE INSURANCE CO | 10% Owner | $11.2M | 320,785 | $35.02 | [Form 4](https://www.sec.gov/Archives/edgar/data/1889539/000119312526395554/0001193125-26-395554-index.htm) |
| 5C Lending Partners Corp. | LIBERTY MUTUAL HOLDING Co INC. | 10% Owner | $9.8M | 398,774 | $24.48 | [Form 4](https://www.sec.gov/Archives/edgar/data/1998387/000119312526395720/0001193125-26-395720-index.htm) |
| **CV** CapsoVision, Inc | Shen Ching Hang | 10% Owner | $5.0M | 878,734 | $5.69 | [Form 4](https://www.sec.gov/Archives/edgar/data/1378325/000210230426000003/0002102304-26-000003-index.htm) |
| **TFC** TRUIST FINANCIAL CORP | Lyons Michael P. | President & CEO, Director | $1.0M | 21,000 | $48.36 | [Form 4](https://www.sec.gov/Archives/edgar/data/1534574/000153457426000016/0001534574-26-000016-index.htm) |
| **KRMN** Karman Holdings Inc. | Stinnett David | Director | $1.0M | 27,000 | $37.32 | [Form 4](https://www.sec.gov/Archives/edgar/data/2040127/000119312526395098/0001193125-26-395098-index.htm) |
| **LILA** Liberty Latin America Ltd. | MALONE JOHN C | 10% Owner | $757.8K | 37,082 | $20.43 | [Form 4](https://www.sec.gov/Archives/edgar/data/1712184/000093779726000030/0000937797-26-000030-index.htm) |
| **BORR** Borr Drilling Ltd | Troim Tor Olav | Director | $656.9K | 150,000 | $4.38 | [Form 4](https://www.sec.gov/Archives/edgar/data/1715497/000162828026062623/0001628280-26-062623-index.htm) |
| **BPRE** Bluerock Private Real Estate Fund | MacDonald Ryan S |  | $248.0K | 20,745 | $11.96 | [Form 4](https://www.sec.gov/Archives/edgar/data/1551047/000139834426017226/0001398344-26-017226-index.htm) |
| **ELOG** Eastern International Ltd. | Wong Albert | Chief Executive Officer, Director, 10% Owner | $200.0K | 200,000 | $1.00 | [Form 4](https://www.sec.gov/Archives/edgar/data/2013320/000149315226043376/0001493152-26-043376-index.htm) |
| **THM** INTERNATIONAL TOWER HILL MINES LTD | Wiens David Victor | Chief Executive Officer, Director | $200.0K | 83,682 | $2.39 | [Form 4](https://www.sec.gov/Archives/edgar/data/1134115/000112329226001319/0001123292-26-001319-index.htm) |

## Biggest insider sales · filed 2026-09-18

| Company | Insider | Role | Value | Shares | Avg price | Filing |
|---|---|---|---:|---:|---:|---|
| **IHT** INNSUITES HOSPITALITY TRUST | BERG MARC E | EVP & Secretary/Treasurer | $361.5M | 16,000 | $22,593.60 | [Form 4](https://www.sec.gov/Archives/edgar/data/1248349/000149315226043445/0001493152-26-043445-index.htm) |
| **DELL** Dell Technologies Inc. | Silver Lake Partners IV, L.P., Silver Lake Technology Associates IV, L.P., SLTA IV (GP), L.L.C., Silver Lake Group, L.L.C., Durban Egon | Director, 10% Owner | $32.3M | 56,794 | $567.89 | [Form 4](https://www.sec.gov/Archives/edgar/data/1571996/000119312526395615/0001193125-26-395615-index.htm) |
| **ADBE** ADOBE INC. | NARAYEN SHANTANU | Chair and CEO, Director | $31.3M | 125,000 | $250.76 | [Form 4](https://www.sec.gov/Archives/edgar/data/796343/000122415426000003/0001224154-26-000003-index.htm) |
| **BBY** BEST BUY CO INC | SCHULZE RICHARD M |  | $27.8M | 300,000 | $92.51 | [Form 4](https://www.sec.gov/Archives/edgar/data/764478/000122520826007890/0001225208-26-007890-index.htm) |
| **DELL** Dell Technologies Inc. | SL SPV-2, L.P., SLTA SPV-2, L.P., SLTA SPV-2 (GP), L.L.C., Silver Lake Group, L.L.C., Durban Egon | Director, 10% Owner | $26.7M | 46,994 | $567.88 | [Form 4](https://www.sec.gov/Archives/edgar/data/1571996/000119312526395616/0001193125-26-395616-index.htm) |

Full list: [`data/insider/2026/09/2026-09-18.md`](data/insider/2026/09/2026-09-18.md)

## How it works

- [`scripts/update.py`](scripts/update.py) (Python stdlib only) runs daily via [`.github/workflows/daily.yml`](.github/workflows/daily.yml).
- **Insider trades:** reads SEC EDGAR's daily index, parses every Form 4, and keeps open-market purchases (code `P`) and sales (code `S`).
- **Market:** closing prices for major index ETFs, the 11 S&P sector ETFs, and 40 large-cap stocks.
- **Weekly recap:** every Sunday, including cluster buys (multiple insiders buying the same company).
- Raw JSON lives in [`data/`](data) for anyone who wants to analyze it.

_Informational only, not investment advice. Data: SEC EDGAR (Form 4) and Yahoo Finance; may contain errors or delays._
