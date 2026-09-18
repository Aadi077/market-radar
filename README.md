# 📊 Market Radar

A daily, automatically updated record of **insider trading** (SEC Form 4 open-market buys and sales) and **US market performance**, with a weekly recap every Sunday. Collected by GitHub Actions.

**Last updated:** 2026-09-17

## Market close · 2026-09-16

| Index | Close | Change |
|---|---:|---:|
| S&P 500 (SPY) | 754.05 | -0.44% |
| Nasdaq 100 (QQQ) | 704.72 | +0.03% |
| Dow 30 (DIA) | 515.22 | -1.15% |
| Russell 2000 (IWM) | 283.92 | -0.43% |

![Sector performance](charts/sectors-daily.svg)

**Top large-cap gainers:** **INTC** +4.03% · **ORCL** +2.00% · **GE** +1.91% · **AMD** +1.65% · **TMO** +1.10%  
**Top large-cap decliners:** **IBM** -4.38% · **XOM** -3.54% · **WFC** -2.98% · **CVX** -2.86% · **ADBE** -2.82%

## Biggest insider buys · filed 2026-09-16

| Company | Insider | Role | Value | Shares | Avg price | Filing |
|---|---|---|---:|---:|---:|---|
| **USO** United States Oil Fund, LP | HRT FINANCIAL LP | 10% Owner | $16.6M | 105,195 | $157.88 | [Form 4](https://www.sec.gov/Archives/edgar/data/1475597/000147559726000246/0001475597-26-000246-index.htm) |
| **CRBG** Corebridge Financial, Inc. | NIPPON LIFE INSURANCE CO | 10% Owner | $10.3M | 295,967 | $34.86 | [Form 4](https://www.sec.gov/Archives/edgar/data/1889539/000119312526393133/0001193125-26-393133-index.htm) |
| **FOX** Fox Corp | MURDOCH LACHLAN K | Executive Chair, CEO, Director | $10.3M | 149,934 | $68.53 | [Form 4](https://www.sec.gov/Archives/edgar/data/1754301/000162828026062330/0001628280-26-062330-index.htm) |
| Privacore VPC Asset Backed Credit Fund | BANKERS LIFE & CASUALTY CO | 10% Owner | $8.0M | 785,083 | $10.19 | [Form 4](https://www.sec.gov/Archives/edgar/data/903939/000090393926000030/0000903939-26-000030-index.htm) |
| **ARDC** Ares Dynamic Credit Allocation Fund, Inc. | THRIVENT FINANCIAL FOR LUTHERANS | 10% Owner | $6.0M | 240,000 | $25.00 | [Form 4](https://www.sec.gov/Archives/edgar/data/1515324/000031498426000042/0000314984-26-000042-index.htm) |
| **AXIA3** AXIA Energia S.A. | Batista de Lima Filho Pedro | Director | $5.4M | 512,900 | $10.49 | [Form 4](https://www.sec.gov/Archives/edgar/data/1439124/000121390026100498/0001213900-26-100498-index.htm) |
| **KBDC** Kayne Anderson BDC, Inc. | ROBO JAMES L | Director | $5.2M | 400,000 | $13.03 | [Form 4](https://www.sec.gov/Archives/edgar/data/1747172/000118325426000005/0001183254-26-000005-index.htm) |
| **TLAC** Three Lions Acquisition Corp. | Three Lions Sponsor, LLC | Director | $2.0M | 200,000 | $10.00 | [Form 4](https://www.sec.gov/Archives/edgar/data/2128462/000119312526392735/0001193125-26-392735-index.htm) |
| **MNR** MACH NATURAL RESOURCES LP | WARD TOM L. | See Remarks, Director, 10% Owner | $2.0M | 172,413 | $11.60 | [Form 4](https://www.sec.gov/Archives/edgar/data/1980088/000121390026100673/0001213900-26-100673-index.htm) |
| **AAT** American Assets Trust, Inc. | RADY ERNEST S | Executive Chairman, Director, 10% Owner | $1.1M | 50,000 | $21.65 | [Form 4](https://www.sec.gov/Archives/edgar/data/1500217/000122135926000057/0001221359-26-000057-index.htm) |

## Biggest insider sales · filed 2026-09-16

| Company | Insider | Role | Value | Shares | Avg price | Filing |
|---|---|---|---:|---:|---:|---|
| **CHYM** Chime Financial, Inc. | DST Global Advisors Ltd, Cardew Services Ltd, Galileo (PTC) Ltd, Zinonos Despoina | 10% Owner | $109.3M | 3,216,189 | $33.99 | [Form 4](https://www.sec.gov/Archives/edgar/data/1550169/000119312526393444/0001193125-26-393444-index.htm) |
| **CHYM** Chime Financial, Inc. | DST Global Advisors Ltd, DST Global VI, L.P., DST Global VII, L.P., DST Investments XXI, L.P., DSTG VI Investments, L.P., DSTG VI Investments-A, L.P., DSTG VII Investments-1, L.P., DSTG VII Investments-4, L.P., DST Managers VI Ltd, DST Managers VII Ltd | 10% Owner | $109.3M | 3,216,189 | $33.99 | [Form 4](https://www.sec.gov/Archives/edgar/data/1795586/000119312526393439/0001193125-26-393439-index.htm) |
| **STX** Seagate Technology Holdings plc | MOSLEY WILLIAM D | CEO, Director | $75.6M | 97,889 | $772.14 | [Form 4](https://www.sec.gov/Archives/edgar/data/1388390/000113778926000252/0001137789-26-000252-index.htm) |
| **SNDK** Sandisk Corp | Goeckeler David | Chairman & CEO, Director | $51.7M | 33,838 | $1,527.87 | [Form 4](https://www.sec.gov/Archives/edgar/data/1713941/000124264826000032/0001242648-26-000032-index.htm) |
| **STX** Seagate Technology Holdings plc | Teh Ban Seng | EVP & Chief Commercial Officer | $41.2M | 52,730 | $782.08 | [Form 4](https://www.sec.gov/Archives/edgar/data/1137789/000113778926000251/0001137789-26-000251-index.htm) |

Full list: [`data/insider/2026/09/2026-09-16.md`](data/insider/2026/09/2026-09-16.md)

## How it works

- [`scripts/update.py`](scripts/update.py) (Python stdlib only) runs daily via [`.github/workflows/daily.yml`](.github/workflows/daily.yml).
- **Insider trades:** reads SEC EDGAR's daily index, parses every Form 4, and keeps open-market purchases (code `P`) and sales (code `S`).
- **Market:** closing prices for major index ETFs, the 11 S&P sector ETFs, and 40 large-cap stocks.
- **Weekly recap:** every Sunday, including cluster buys (multiple insiders buying the same company).
- Raw JSON lives in [`data/`](data) for anyone who wants to analyze it.

_Informational only, not investment advice. Data: SEC EDGAR (Form 4) and Yahoo Finance; may contain errors or delays._
