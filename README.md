# 📊 Market Radar

A daily, automatically updated record of **insider trading** (SEC Form 4 open-market buys and sales) and **US market performance**, with a weekly recap every Sunday. Collected by GitHub Actions.

**Last updated:** 2026-09-29

## Market close · 2026-09-28

| Index | Close | Change |
|---|---:|---:|
| S&P 500 (SPY) | 765.61 | -0.74% |
| Nasdaq 100 (QQQ) | 736.53 | -1.07% |
| Dow 30 (DIA) | 514.02 | -0.67% |
| Russell 2000 (IWM) | 280.02 | -0.69% |

![Sector performance](charts/sectors-daily.svg)

**Top large-cap gainers:** **PG** +1.91% · **NVDA** +1.68% · **XOM** +1.20% · **CVX** +0.94% · **ABBV** +0.73%  
**Top large-cap decliners:** **INTC** -5.67% · **META** -4.79% · **TSLA** -3.94% · **AMD** -3.61% · **ORCL** -3.28%

## Biggest insider buys · filed 2026-09-28

| Company | Insider | Role | Value | Shares | Avg price | Filing |
|---|---|---|---:|---:|---:|---|
| **GPI** GROUP 1 AUTOMOTIVE INC | Conifer Management, L.L.C. | 10% Owner | $31.5M | 126,288 | $249.62 | [Form 4](https://www.sec.gov/Archives/edgar/data/1773994/000090514826004278/0000905148-26-004278-index.htm) |
| **CRBG** Corebridge Financial, Inc. | NIPPON LIFE INSURANCE CO | 10% Owner | $8.8M | 258,878 | $33.85 | [Form 4](https://www.sec.gov/Archives/edgar/data/1889539/000119312526405404/0001193125-26-405404-index.htm) |
| **LLYVK** Liberty Live Holdings, Inc. | MALONE JOHN C | 10% Owner | $2.9M | 28,333 | $102.53 | [Form 4](https://www.sec.gov/Archives/edgar/data/2078416/000122520826007970/0001225208-26-007970-index.htm) |
| **QVCG** QVC Group, Inc. | GOLDENTREE ASSET MANAGEMENT LP, GoldenTree Asset Management LLC, Tananbaum Steven A. | 10% Owner | $1.1M | 80,000 | $14.35 | [Form 4](https://www.sec.gov/Archives/edgar/data/1278951/000149315226044626/0001493152-26-044626-index.htm) |
| **INBX** Inhibrx Biosciences, Inc. | Lappe Mark | Chief Executive Officer, Director | $998.8K | 10,000 | $99.88 | [Form 4](https://www.sec.gov/Archives/edgar/data/2007919/000136607426000004/0001366074-26-000004-index.htm) |
| **HDSN** HUDSON TECHNOLOGIES INC /NY | Hartree Partners, LP | 10% Owner | $604.4K | 118,549 | $5.10 | [Form 4](https://www.sec.gov/Archives/edgar/data/925528/000092189526002658/0000921895-26-002658-index.htm) |
| **LILA** Liberty Latin America Ltd. | MALONE JOHN C | 10% Owner | $458.7K | 22,442 | $20.44 | [Form 4](https://www.sec.gov/Archives/edgar/data/1712184/000093779726000032/0000937797-26-000032-index.htm) |
| **INR** INFINITY NATURAL RESOURCES, INC. | Baetz Cary D | EVP and CFO | $300.0K | 22,316 | $13.44 | [Form 4](https://www.sec.gov/Archives/edgar/data/1331940/000202911826000113/0002029118-26-000113-index.htm) |
| **AOMR** Angel Oak Mortgage REIT, Inc. | Fierman Michael | Director, 10% Owner | $290.5K | 38,726 | $7.50 | [Form 4](https://www.sec.gov/Archives/edgar/data/1766478/000176647826000056/0001766478-26-000056-index.htm) |
| **ACOG** Alpha Cognition Inc. | Opaleye Management Inc. | 10% Owner | $270.8K | 31,763 | $8.53 | [Form 4](https://www.sec.gov/Archives/edgar/data/1655923/000149315226044690/0001493152-26-044690-index.htm) |

## Biggest insider sales · filed 2026-09-28

| Company | Insider | Role | Value | Shares | Avg price | Filing |
|---|---|---|---:|---:|---:|---|
| **GTLB** Gitlab Inc. | Sijbrandij Sytse | Director | $101.1M | 2,116,200 | $47.77 | [Form 4](https://www.sec.gov/Archives/edgar/data/1653482/000165348226000170/0001653482-26-000170-index.htm) |
| **INNV** InnovAge Holding Corp. | IGNITE AGGREGATOR LP, APAX X (GUERNSEY) USD AIV LP, IGNITE GP INC., Apax X EUR L.P., Apax X USD L.P., Apax X GP Co. Ltd | 10% Owner | $92.5M | 10,000,000 | $9.25 | [Form 4](https://www.sec.gov/Archives/edgar/data/1848852/000119312526405347/0001193125-26-405347-index.htm) |
| **INNV** InnovAge Holding Corp. | TCO GROUP HOLDINGS, L.P. | 10% Owner | $92.5M | 10,000,000 | $9.25 | [Form 4](https://www.sec.gov/Archives/edgar/data/1834376/000119312526405348/0001193125-26-405348-index.htm) |
| **CBRS** Cerebras Systems Inc. | Lie Sean | Chief Technology Officer | $25.1M | 120,000 | $208.97 | [Form 4](https://www.sec.gov/Archives/edgar/data/2021728/000162828026063713/0001628280-26-063713-index.htm) |
| **META** Meta Platforms, Inc. | Zuckerberg Mark | COB and CEO, Director, 10% Owner | $21.4M | 27,474 | $777.44 | [Form 4](https://www.sec.gov/Archives/edgar/data/1326801/000095010326014647/0000950103-26-014647-index.htm) |

Full list: [`data/insider/2026/09/2026-09-28.md`](data/insider/2026/09/2026-09-28.md)

## Latest weekly recap

[2026-W39](data/weekly/2026-W39.md)

## How it works

- [`scripts/update.py`](scripts/update.py) (Python stdlib only) runs daily via [`.github/workflows/daily.yml`](.github/workflows/daily.yml).
- **Insider trades:** reads SEC EDGAR's daily index, parses every Form 4, and keeps open-market purchases (code `P`) and sales (code `S`).
- **Market:** closing prices for major index ETFs, the 11 S&P sector ETFs, and 40 large-cap stocks.
- **Weekly recap:** every Sunday, including cluster buys (multiple insiders buying the same company).
- Raw JSON lives in [`data/`](data) for anyone who wants to analyze it.

_Informational only, not investment advice. Data: SEC EDGAR (Form 4) and Yahoo Finance; may contain errors or delays._
