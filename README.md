# 📊 Market Radar

An automatically updated record of **insider trading** (SEC Form 4 open-market buys and sales) and **US market performance**, updated every weekday with a recap each Monday. Collected by GitHub Actions.

**Last updated:** 2026-10-06

## Market close · 2026-10-06

| Index | Close | Change |
|---|---:|---:|
| S&P 500 (SPY) | 779.09 | +0.55% |
| Nasdaq 100 (QQQ) | 759.66 | +0.46% |
| Dow 30 (DIA) | 514.56 | +0.48% |
| Russell 2000 (IWM) | 281.34 | -0.72% |

![Sector performance](charts/sectors-daily.svg)

**Top large-cap gainers:** **CSCO** +4.54% · **AVGO** +3.67% · **AMD** +2.80% · **WMT** +2.03% · **HD** +1.97%  
**Top large-cap decliners:** **INTC** -3.18% · **TMO** -2.98% · **CRM** -2.09% · **UNH** -0.60% · **META** -0.41%

## Biggest insider buys · filed 2026-10-05

| Company | Insider | Role | Value | Shares | Avg price | Filing |
|---|---|---|---:|---:|---:|---|
| **LEN** LENNAR CORP /NEW/ | BERKSHIRE HATHAWAY INC, BUFFETT WARREN E | 10% Owner | $192.6M | 2,418,637 | $79.65 | [Form 4](https://www.sec.gov/Archives/edgar/data/1067983/000119312526414744/0001193125-26-414744-index.htm) |
| **BBD** BANK BRADESCO | Alvarez Denise Aguiar | Director | $33.6M | 1,950,000 | $17.22 | [Form 4](https://www.sec.gov/Archives/edgar/data/2126543/000129281426004850/0001292814-26-004850-index.htm) |
| **CRBG** Corebridge Financial, Inc. | NIPPON LIFE INSURANCE CO | 10% Owner | $9.0M | 272,208 | $33.07 | [Form 4](https://www.sec.gov/Archives/edgar/data/1889539/000119312526414288/0001193125-26-414288-index.htm) |
| **BBD** BANK BRADESCO | Alvarez Denise Aguiar | Director | $5.8M | 345,000 | $16.69 | [Form 4](https://www.sec.gov/Archives/edgar/data/2126543/000129281426004852/0001292814-26-004852-index.htm) |
| **ACCV** Accelevation Holdings Corp. | Rubiera Michael | Chief Executive Officer, Director | $3.7M | 203,200 | $18.00 | [Form 4](https://www.sec.gov/Archives/edgar/data/2141406/000162828026065167/0001628280-26-065167-index.htm) |
| **BPRE** Bluerock Private Real Estate Fund | KAMFAR RAMIN | Director | $3.4M | 269,164 | $12.66 | [Form 4](https://www.sec.gov/Archives/edgar/data/1551047/000139834426017906/0001398344-26-017906-index.htm) |
| **OM** Outset Medical, Inc. | Leonard Braden Michael | 10% Owner | $870.3K | 244,909 | $3.55 | [Form 4](https://www.sec.gov/Archives/edgar/data/1373603/000137360426000050/0001373604-26-000050-index.htm) |
| CAZ GP Stakes Growth Fund | Zook Christopher |  | $512.0K | 25,599 | $20.00 | [Form 4](https://www.sec.gov/Archives/edgar/data/2128311/000121390026106873/0001213900-26-106873-index.htm) |
| 83 Investment Group Income Fund | SELTER ERIC JAY |  | $500.0K | 48,924 | $10.22 | [Form 4](https://www.sec.gov/Archives/edgar/data/2036029/000158064226006725/0001580642-26-006725-index.htm) |
| **MXF** MEXICO FUND INC | Saba Capital Management, L.P. | 10% Owner | $389.5K | 19,494 | $19.98 | [Form 4](https://www.sec.gov/Archives/edgar/data/65433/000151028126000323/0001510281-26-000323-index.htm) |

## Biggest insider sales · filed 2026-10-05

| Company | Insider | Role | Value | Shares | Avg price | Filing |
|---|---|---|---:|---:|---:|---|
| **ACCV** Accelevation Holdings Corp. | OGP VIII, LLC, Accelevation Pubco Holdings LP, Accelevation Investment Holdings LLC, MORRIS ROBERT S | 10% Owner, Director | $360.0M | 20,000,000 | $18.00 | [Form 4](https://www.sec.gov/Archives/edgar/data/2141406/000162828026065149/0001628280-26-065149-index.htm) |
| **TH** Target Hospitality Corp. | TDR Capital II Investments LP, Arrow Holdings S.a.r.l., MFA Holding S.a.r.l., MFA Limited Partnership SLP, MFA Global S.a.r.l., TDR Capital LLP, Sapphire Holding S.a r.l., Lindsay Gary, DALE MANJIT, Mitchell Thomas Andrew | 10% Owner | $202.4M | 11,000,000 | $18.40 | [Form 4](https://www.sec.gov/Archives/edgar/data/1767017/000095014226002685/0000950142-26-002685-index.htm) |
| **AAPL** Apple Inc. | COOK TIMOTHY D | Executive Chair, Director | $63.8M | 191,753 | $332.96 | [Form 4](https://www.sec.gov/Archives/edgar/data/320193/000114036126038674/0001140361-26-038674-index.htm) |
| **WDAY** Workday, Inc. | DUFFIELD DAVID A | 10% Owner | $18.4M | 98,446 | $187.07 | [Form 4](https://www.sec.gov/Archives/edgar/data/938071/000093807126000063/0000938071-26-000063-index.htm) |
| **AAPL** Apple Inc. | O'BRIEN DEIRDRE | Senior Vice President | $15.5M | 46,389 | $333.42 | [Form 4](https://www.sec.gov/Archives/edgar/data/320193/000114036126038672/0001140361-26-038672-index.htm) |

Full list: [`data/insider/2026/10/2026-10-05.md`](data/insider/2026/10/2026-10-05.md)

## Latest weekly recap

[2026-W40](data/weekly/2026-W40.md)

## How it works

- [`scripts/update.py`](scripts/update.py) (Python stdlib only) runs every weekday via [`.github/workflows/daily.yml`](.github/workflows/daily.yml).
- **Insider trades:** reads SEC EDGAR's daily index, parses every Form 4, and keeps open-market purchases (code `P`) and sales (code `S`).
- **Market:** closing prices for major index ETFs, the 11 S&P sector ETFs, and 40 large-cap stocks.
- **Weekly recap:** every Monday, covering the week just ended, including cluster buys (multiple insiders buying the same company).
- Raw JSON lives in [`data/`](data) for anyone who wants to analyze it.

_Informational only, not investment advice. Data: SEC EDGAR (Form 4) and Yahoo Finance; may contain errors or delays._
