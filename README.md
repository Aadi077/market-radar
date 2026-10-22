# 📊 Market Radar

An automatically updated record of **insider trading** (SEC Form 4 open-market buys and sales) and **US market performance**, updated every weekday with a recap each Monday. Collected by GitHub Actions.

**Last updated:** 2026-10-21

## Market close · 2026-10-20

| Index | Close | Change |
|---|---:|---:|
| S&P 500 (SPY) | 769.05 | +0.34% |
| Nasdaq 100 (QQQ) | 717.63 | -0.10% |
| Dow 30 (DIA) | 524.36 | +1.05% |
| Russell 2000 (IWM) | 275.78 | +1.66% |

![Sector performance](charts/sectors-daily.svg)

**Top large-cap gainers:** **ADBE** +3.90% · **LLY** +3.49% · **MRK** +3.25% · **UNH** +3.04% · **IBM** +2.34%  
**Top large-cap decliners:** **GE** -3.67% · **NFLX** -1.66% · **META** -1.59% · **GOOGL** -1.13% · **AAPL** -1.00%

## Biggest insider buys · filed 2026-10-20

| Company | Insider | Role | Value | Shares | Avg price | Filing |
|---|---|---|---:|---:|---:|---|
| **CRBG** Corebridge Financial, Inc. | NIPPON LIFE INSURANCE CO | 10% Owner | $12.1M | 347,195 | $34.71 | [Form 4](https://www.sec.gov/Archives/edgar/data/1889539/000119312526426865/0001193125-26-426865-index.htm) |
| **SCISX** MA Specialty Credit Income Fund | MA Eagle II Holdings Fund | 10% Owner | $2.4M | 96,931 | $24.76 | [Form 4](https://www.sec.gov/Archives/edgar/data/2049114/000094562126001274/0000945621-26-001274-index.htm) |
| **LEO** BNY MELLON STRATEGIC MUNICIPALS, INC. | Saba Capital Management, L.P. | 10% Owner | $1.9M | 338,104 | $5.65 | [Form 4](https://www.sec.gov/Archives/edgar/data/818972/000151028126000365/0001510281-26-000365-index.htm) |
| **DSM** BNY MELLON STRATEGIC MUNICIPAL BOND FUND, INC. | Saba Capital Management, L.P. | 10% Owner | $1.1M | 207,722 | $5.28 | [Form 4](https://www.sec.gov/Archives/edgar/data/855887/000151028126000362/0001510281-26-000362-index.htm) |
| **JOF** JAPAN SMALLER CAPITALIZATION FUND INC | Saba Capital Management, L.P. | 10% Owner | $551.9K | 46,222 | $11.94 | [Form 4](https://www.sec.gov/Archives/edgar/data/859796/000151028126000363/0001510281-26-000363-index.htm) |
| **ECF** ELLSWORTH GROWTH & INCOME FUND LTD | Saba Capital Management, L.P. | 10% Owner | $386.3K | 33,426 | $11.56 | [Form 4](https://www.sec.gov/Archives/edgar/data/793040/000151028126000360/0001510281-26-000360-index.htm) |
| **BOLD** Boundless Bio, Inc. | TANG KEVIN, TANG CAPITAL MANAGEMENT LLC | 10% Owner | $349.6K | 149,474 | $2.34 | [Form 4](https://www.sec.gov/Archives/edgar/data/1782303/000117857926000019/0001178579-26-000019-index.htm) |
| **GF** NEW GERMANY FUND INC | Saba Capital Management, L.P. | 10% Owner | $310.7K | 30,088 | $10.33 | [Form 4](https://www.sec.gov/Archives/edgar/data/858706/000151028126000361/0001510281-26-000361-index.htm) |
| **DX** DYNEX CAPITAL INC | Popenoe Smriti Laxman | Co-CEO and President, Director | $156.6K | 12,000 | $13.05 | [Form 4](https://www.sec.gov/Archives/edgar/data/826675/000082667526000121/0000826675-26-000121-index.htm) |
| **GRF** EAGLE CAPITAL GROWTH FUND, INC. | Sims David C | CFO, CCO, Secretary, Treasurer, Director | $108.6K | 10,787 | $10.07 | [Form 4](https://www.sec.gov/Archives/edgar/data/850027/000140161226000005/0001401612-26-000005-index.htm) |

## Biggest insider sales · filed 2026-10-20

| Company | Insider | Role | Value | Shares | Avg price | Filing |
|---|---|---|---:|---:|---:|---|
| **MU** MICRON TECHNOLOGY INC | Deboer Scott J | Pres. & Chief Tech & Prod Offr | $25.7M | 28,545 | $900.00 | [Form 4](https://www.sec.gov/Archives/edgar/data/1568238/000156823826000003/0001568238-26-000003-index.htm) |
| **NZF** Nuveen Municipal Credit Income Fund | Robert Young L |  | $17.6M | 16,131 | $1,093.00 | [Form 4](https://www.sec.gov/Archives/edgar/data/1137887/000122520826008478/0001225208-26-008478-index.htm) |
| **GRND** Grindr Inc. | Zage George Raymond III | Director, 10% Owner | $7.1M | 500,000 | $14.12 | [Form 4](https://www.sec.gov/Archives/edgar/data/1820144/000183367826000007/0001833678-26-000007-index.htm) |
| **UTHR** UNITED THERAPEUTICS Corp | ROTHBLATT MARTINE A | Chairperson & CEO, Director | $5.2M | 9,500 | $543.32 | [Form 4](https://www.sec.gov/Archives/edgar/data/1106578/000110657826000167/0001106578-26-000167-index.htm) |
| **VG** Venture Global, Inc. | Thayer Jonathan W | Chief Financial Officer | $2.8M | 222,222 | $12.69 | [Form 4](https://www.sec.gov/Archives/edgar/data/1448765/000144876526000017/0001448765-26-000017-index.htm) |

Full list: [`data/insider/2026/10/2026-10-20.md`](data/insider/2026/10/2026-10-20.md)

## Latest weekly recap

[2026-W42](data/weekly/2026-W42.md)

## How it works

- [`scripts/update.py`](scripts/update.py) (Python stdlib only) runs every weekday via [`.github/workflows/daily.yml`](.github/workflows/daily.yml).
- **Insider trades:** reads SEC EDGAR's daily index, parses every Form 4, and keeps open-market purchases (code `P`) and sales (code `S`).
- **Market:** closing prices for major index ETFs, the 11 S&P sector ETFs, and 40 large-cap stocks.
- **Weekly recap:** every Monday, covering the week just ended, including cluster buys (multiple insiders buying the same company).
- Raw JSON lives in [`data/`](data) for anyone who wants to analyze it.

_Informational only, not investment advice. Data: SEC EDGAR (Form 4) and Yahoo Finance; may contain errors or delays._
