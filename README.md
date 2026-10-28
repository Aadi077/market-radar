# 📊 Market Radar

An automatically updated record of **insider trading** (SEC Form 4 open-market buys and sales) and **US market performance**, updated every weekday with a recap each Monday. Collected by GitHub Actions.

**Last updated:** 2026-10-27

## Market close · 2026-10-26

| Index | Close | Change |
|---|---:|---:|
| S&P 500 (SPY) | 765.37 | +0.71% |
| Nasdaq 100 (QQQ) | 712.20 | +1.11% |
| Dow 30 (DIA) | 522.97 | +0.31% |
| Russell 2000 (IWM) | 276.99 | +0.45% |

![Sector performance](charts/sectors-daily.svg)

**Top large-cap gainers:** **TSLA** +5.21% · **INTC** +4.04% · **CSCO** +3.51% · **AMD** +2.80% · **NVDA** +2.39%  
**Top large-cap decliners:** **MRK** -3.21% · **NFLX** -2.96% · **ADBE** -1.97% · **META** -1.88% · **DIS** -1.88%

## Biggest insider buys · filed 2026-10-26

| Company | Insider | Role | Value | Shares | Avg price | Filing |
|---|---|---|---:|---:|---:|---|
| **GPI** GROUP 1 AUTOMOTIVE INC | Conifer Management, L.L.C. | 10% Owner | $24.2M | 100,000 | $242.32 | [Form 4](https://www.sec.gov/Archives/edgar/data/1773994/000090514826004561/0000905148-26-004561-index.htm) |
| **CRBG** Corebridge Financial, Inc. | NIPPON LIFE INSURANCE CO | 10% Owner | $8.7M | 246,440 | $35.15 | [Form 4](https://www.sec.gov/Archives/edgar/data/1889539/000119312526432280/0001193125-26-432280-index.htm) |
| **BPRE** Bluerock Private Real Estate Fund | KAMFAR RAMIN | Director | $2.1M | 170,320 | $12.48 | [Form 4](https://www.sec.gov/Archives/edgar/data/1551047/000139834426018736/0001398344-26-018736-index.htm) |
| **PRTA** PROTHENA CORP PUBLIC LTD CO | SCULLY WILLIAM P | 10% Owner | $1.2M | 150,000 | $8.15 | [Form 4](https://www.sec.gov/Archives/edgar/data/1559053/000104546326000022/0001045463-26-000022-index.htm) |
| **OPTU** Optimum Communications, Inc. | SUBIN NEIL S, MILFAM LLC, MILFAM GP, LLC, Dark Mirage, LP | 10% Owner | $1.2M | 2,228,007 | $0.52 | [Form 4](https://www.sec.gov/Archives/edgar/data/2023628/000121390026112593/0001213900-26-112593-index.htm) |
| **KRRO** Korro Bio, Inc. | Lynx1 Capital Management LP, Nichols Weston | 10% Owner | $884.8K | 79,809 | $11.09 | [Form 4](https://www.sec.gov/Archives/edgar/data/1703647/000090266426004286/0000902664-26-004286-index.htm) |
| Blackstone Multi-Strategy Hedge Fund L.P. | Abrahams Riad M | Chief Executive Officer, Director | $795.0K | 31,213 | $25.47 | [Form 4](https://www.sec.gov/Archives/edgar/data/1370104/000119312526432266/0001193125-26-432266-index.htm) |
| **THRM** Gentherm Inc | MASCARENAS PAUL ANTHONY | Director | $532.6K | 20,000 | $26.63 | [Form 4](https://www.sec.gov/Archives/edgar/data/903129/000119312526432218/0001193125-26-432218-index.htm) |
| **CITR** CitroTech Inc. | HUFF CRAIG A, BoltRock Holdings LLC | Director, 10% Owner | $500.0K | 200,000 | $2.50 | [Form 4](https://www.sec.gov/Archives/edgar/data/2061007/000119312526432001/0001193125-26-432001-index.htm) |
| **LEO** BNY MELLON STRATEGIC MUNICIPALS, INC. | Saba Capital Management, L.P. | 10% Owner | $369.2K | 65,000 | $5.68 | [Form 4](https://www.sec.gov/Archives/edgar/data/818972/000151028126000377/0001510281-26-000377-index.htm) |

## Biggest insider sales · filed 2026-10-26

| Company | Insider | Role | Value | Shares | Avg price | Filing |
|---|---|---|---:|---:|---:|---|
| **ISRG** INTUITIVE SURGICAL INC | GUTHART GARY S | Director | $9.1M | 20,095 | $451.61 | [Form 4](https://www.sec.gov/Archives/edgar/data/1280628/000128062826000016/0001280628-26-000016-index.htm) |
| **CRL** CHARLES RIVER LABORATORIES INTERNATIONAL, INC. | FOSTER JAMES C | Director | $8.4M | 24,042 | $350.00 | [Form 4](https://www.sec.gov/Archives/edgar/data/1100682/000110068226000153/0001100682-26-000153-index.htm) |
| **LRCX** LAM RESEARCH CORP | ARCHER TIMOTHY | President and CEO | $7.1M | 31,400 | $227.02 | [Form 4](https://www.sec.gov/Archives/edgar/data/1343600/000134360026000015/0001343600-26-000015-index.htm) |
| **PG** PROCTER & GAMBLE Co | Jejurikar Shailesh | Chairman, President and CEO, Director | $5.7M | 35,000 | $163.09 | [Form 4](https://www.sec.gov/Archives/edgar/data/1746310/000008042426000263/0000080424-26-000263-index.htm) |
| **UTHR** UNITED THERAPEUTICS Corp | ROTHBLATT MARTINE A | Chairperson & CEO, Director | $5.5M | 9,500 | $582.76 | [Form 4](https://www.sec.gov/Archives/edgar/data/1106578/000110657826000171/0001106578-26-000171-index.htm) |

Full list: [`data/insider/2026/10/2026-10-26.md`](data/insider/2026/10/2026-10-26.md)

## Latest weekly recap

[2026-W43](data/weekly/2026-W43.md)

## How it works

- [`scripts/update.py`](scripts/update.py) (Python stdlib only) runs every weekday via [`.github/workflows/daily.yml`](.github/workflows/daily.yml).
- **Insider trades:** reads SEC EDGAR's daily index, parses every Form 4, and keeps open-market purchases (code `P`) and sales (code `S`).
- **Market:** closing prices for major index ETFs, the 11 S&P sector ETFs, and 40 large-cap stocks.
- **Weekly recap:** every Monday, covering the week just ended, including cluster buys (multiple insiders buying the same company).
- Raw JSON lives in [`data/`](data) for anyone who wants to analyze it.

_Informational only, not investment advice. Data: SEC EDGAR (Form 4) and Yahoo Finance; may contain errors or delays._
