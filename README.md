# 📊 Market Radar

An automatically updated record of **insider trading** (SEC Form 4 open-market buys and sales) and **US market performance**, updated every weekday with a recap each Monday. Collected by GitHub Actions.

**Last updated:** 2026-10-13

## Market close · 2026-10-12

| Index | Close | Change |
|---|---:|---:|
| S&P 500 (SPY) | 778.10 | -0.06% |
| Nasdaq 100 (QQQ) | 746.04 | -0.70% |
| Dow 30 (DIA) | 517.91 | +0.35% |
| Russell 2000 (IWM) | 277.90 | -0.37% |

![Sector performance](charts/sectors-daily.svg)

**Top large-cap gainers:** **META** +3.38% · **CRM** +2.09% · **KO** +1.98% · **XOM** +1.90% · **ABBV** +1.68%  
**Top large-cap decliners:** **INTC** -3.20% · **ORCL** -2.84% · **CSCO** -2.58% · **AMD** -2.28% · **AVGO** -1.88%

## Biggest insider buys · filed 2026-10-09

| Company | Insider | Role | Value | Shares | Avg price | Filing |
|---|---|---|---:|---:|---:|---|
| **GGR** Gogoro Inc. | Yin Chung-Yao | Director | $35.1M | 14,158,991 | $2.48 | [Form 4](https://www.sec.gov/Archives/edgar/data/1886190/000119312526418446/0001193125-26-418446-index.htm) |
| **BBD** BANK BRADESCO | Alvarez Rubens Aguiar | Director | $32.0M | 1,845,000 | $17.37 | [Form 4](https://www.sec.gov/Archives/edgar/data/2126531/000129281426004880/0001292814-26-004880-index.htm) |
| **CRBG** Corebridge Financial, Inc. | NIPPON LIFE INSURANCE CO | 10% Owner | $20.9M | 606,912 | $34.40 | [Form 4](https://www.sec.gov/Archives/edgar/data/1889539/000119312526419124/0001193125-26-419124-index.htm) |
| **BPRE** Bluerock Private Real Estate Fund | KAMFAR RAMIN | Director | $8.5M | 651,063 | $13.06 | [Form 4](https://www.sec.gov/Archives/edgar/data/1551047/000139834426018110/0001398344-26-018110-index.htm) |
| **PRTA** PROTHENA CORP PUBLIC LTD CO | SCULLY WILLIAM P | 10% Owner | $1.8M | 215,000 | $8.47 | [Form 4](https://www.sec.gov/Archives/edgar/data/1559053/000104546326000020/0001045463-26-000020-index.htm) |
| **N.A.** Calamos Aksia Private Equity & Alternatives Fund | Aksia LLC |  | $909.7K | 82,053 | $11.09 | [Form 4](https://www.sec.gov/Archives/edgar/data/1939932/000193993226000012/0001939932-26-000012-index.htm) |
| **SAH** SONIC AUTOMOTIVE INC | Rusnak Paul P. | 10% Owner | $819.0K | 13,701 | $59.78 | [Form 4](https://www.sec.gov/Archives/edgar/data/1460471/000146047126000008/0001460471-26-000008-index.htm) |
| Calamos Aksia Hedged Strategies Fund | Aksia LLC |  | $792.8K | 76,828 | $10.32 | [Form 4](https://www.sec.gov/Archives/edgar/data/1939932/000193993226000013/0001939932-26-000013-index.htm) |
| Calamos Aksia Alternative Credit & Income Fund | Aksia LLC |  | $561.5K | 52,720 | $10.65 | [Form 4](https://www.sec.gov/Archives/edgar/data/1939932/000193993226000014/0001939932-26-000014-index.htm) |
| **VDTA** Vertical Data Inc. | Leverton Jaime | Director | $255.0K | 85,000 | $3.00 | [Form 4](https://www.sec.gov/Archives/edgar/data/1998054/000199805426000009/0001998054-26-000009-index.htm) |

## Biggest insider sales · filed 2026-10-09

| Company | Insider | Role | Value | Shares | Avg price | Filing |
|---|---|---|---:|---:|---:|---|
| **IHT** INNSUITES HOSPITALITY TRUST | WIRTH JAMES F | President & CEO, 10% Owner | $2.2B | 43,111 | $50,410.80 | [Form 4](https://www.sec.gov/Archives/edgar/data/82473/000149315226046636/0001493152-26-046636-index.htm) |
| **ANET** Arista Networks, Inc. | Ullal Jayshree | CEO and Chairperson, Director | $21.1M | 96,992 | $217.14 | [Form 4](https://www.sec.gov/Archives/edgar/data/1596532/000159653226000242/0001596532-26-000242-index.htm) |
| **DUOL** Duolingo, Inc. | von Ahn Luis | President & CEO, Co-Founder, Director, 10% Owner | $16.7M | 110,046 | $151.70 | [Form 4](https://www.sec.gov/Archives/edgar/data/1562088/000162828026065528/0001628280-26-065528-index.htm) |
| **DDOG** Datadog, Inc. | Le-Quoc Alexis | Chief Technology Officer, Director | $14.8M | 53,912 | $273.60 | [Form 4](https://www.sec.gov/Archives/edgar/data/1561550/000156155026000324/0001561550-26-000324-index.htm) |
| **AXIA3** AXIA Energia S.A. | Batista de Lima Filho Pedro | Director | $9.6M | 837,000 | $11.50 | [Form 4](https://www.sec.gov/Archives/edgar/data/1439124/000121390026108268/0001213900-26-108268-index.htm) |

Full list: [`data/insider/2026/10/2026-10-09.md`](data/insider/2026/10/2026-10-09.md)

## Latest weekly recap

[2026-W41](data/weekly/2026-W41.md)

## How it works

- [`scripts/update.py`](scripts/update.py) (Python stdlib only) runs every weekday via [`.github/workflows/daily.yml`](.github/workflows/daily.yml).
- **Insider trades:** reads SEC EDGAR's daily index, parses every Form 4, and keeps open-market purchases (code `P`) and sales (code `S`).
- **Market:** closing prices for major index ETFs, the 11 S&P sector ETFs, and 40 large-cap stocks.
- **Weekly recap:** every Monday, covering the week just ended, including cluster buys (multiple insiders buying the same company).
- Raw JSON lives in [`data/`](data) for anyone who wants to analyze it.

_Informational only, not investment advice. Data: SEC EDGAR (Form 4) and Yahoo Finance; may contain errors or delays._
