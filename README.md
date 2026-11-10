# 📊 Market Radar

An automatically updated record of **insider trading** (SEC Form 4 open-market buys and sales) and **US market performance**, updated every weekday with a recap each Monday. Collected by GitHub Actions.

**Last updated:** 2026-11-09

## Market close · 2026-11-09

| Index | Close | Change |
|---|---:|---:|
| S&P 500 (SPY) | 752.69 | +2.37% |
| Nasdaq 100 (QQQ) | 679.35 | +3.54% |
| Dow 30 (DIA) | 523.33 | +2.17% |
| Russell 2000 (IWM) | 282.51 | +3.23% |

![Sector performance](charts/sectors-daily.svg)

**Top large-cap gainers:** **AMD** +13.26% · **AVGO** +8.78% · **TSLA** +5.54% · **PLTR** +5.50% · **INTC** +5.49%  
**Top large-cap decliners:** **NVDA** -4.27% · **CVX** -0.86% · **ADBE** -0.83% · **XOM** -0.69% · **V** -0.12%

## Biggest insider buys · filed 2026-11-06

| Company | Insider | Role | Value | Shares | Avg price | Filing |
|---|---|---|---:|---:|---:|---|
| **MDGL** MADRIGAL PHARMACEUTICALS, INC. | BAKER BROS. ADVISORS LP, Baker Bros. Advisors (GP) LLC, BAKER FELIX, BAKER JULIAN, 667, L.P., Baker Brothers Life Sciences LP | Director | $35.0M | 91,806 | $381.49 | [Form 4](https://www.sec.gov/Archives/edgar/data/1551139/000119312526452132/0001193125-26-452132-index.htm) |
| **KOD** Kodiak Sciences Inc. | BAKER BROS. ADVISORS LP, 667, L.P., Baker Bros. Advisors (GP) LLC, Baker Brothers Life Sciences LP, BAKER FELIX, BAKER JULIAN | Director, 10% Owner | $24.3M | 247,090 | $98.51 | [Form 4](https://www.sec.gov/Archives/edgar/data/1551139/000119312526451994/0001193125-26-451994-index.htm) |
| **KMI** KINDER MORGAN, INC. | KINDER RICHARD D | Executive Chairman, Director, 10% Owner | $15.0M | 500,000 | $29.99 | [Form 4](https://www.sec.gov/Archives/edgar/data/1506307/000150630726000139/0001506307-26-000139-index.htm) |
| **ANVS** Annovis Bio, Inc. | Hoffman Michael B | Director | $5.0M | 5,000,000 | $1.00 | [Form 4](https://www.sec.gov/Archives/edgar/data/1477845/000110465926123905/0001104659-26-123905-index.htm) |
| **CVS** CVS HEALTH Corp | Shah Prem S | EVP and Group President | $2.0M | 23,855 | $83.89 | [Form 4](https://www.sec.gov/Archives/edgar/data/64803/000006480326000112/0000064803-26-000112-index.htm) |
| **MXF** MEXICO EQUITY & INCOME FUND INC | Saba Capital Management, L.P. | 10% Owner | $499.7K | 24,115 | $20.72 | [Form 4](https://www.sec.gov/Archives/edgar/data/863900/000151028126000419/0001510281-26-000419-index.htm) |
| **YPF** YPF SOCIEDAD ANONIMA | Francos Guillermo Alberto | Director | $356.3K | 6,930 | $51.42 | [Form 4](https://www.sec.gov/Archives/edgar/data/2120097/000129281426005166/0001292814-26-005166-index.htm) |
| **KYN** Kayne Anderson Energy Infrastructure Fund, Inc. | Baker James C | President, Director | $331.1K | 25,000 | $13.24 | [Form 4](https://www.sec.gov/Archives/edgar/data/1331674/000133167426000005/0001331674-26-000005-index.htm) |
| **JOF** JAPAN SMALLER CAPITALIZATION FUND INC | Saba Capital Management, L.P. | 10% Owner | $299.3K | 28,208 | $10.61 | [Form 4](https://www.sec.gov/Archives/edgar/data/859796/000151028126000420/0001510281-26-000420-index.htm) |
| **TRNS** TRANSCAT INC | IRICK JAIME A | President and CEO, Director | $230.4K | 2,275 | $101.26 | [Form 4](https://www.sec.gov/Archives/edgar/data/1695807/000089183926000478/0000891839-26-000478-index.htm) |

## Biggest insider sales · filed 2026-11-06

| Company | Insider | Role | Value | Shares | Avg price | Filing |
|---|---|---|---:|---:|---:|---|
| **INGM** Ingram Micro Holding Corp | PLATINUM EQUITY, LLC, Platinum Equity Investment Holdings, LLC, Platinum Equity Investment Holdings IC (Cayman), LLC, Platinum Equity InvestCo, L.P., Platinum Equity Investment Holdings V, LLC, Platinum Equity Partners V, LLC, Platinum Equity Partners V, L.P., Imola JV Holdings, L.P., Ingram Holdco, LLC, Gores Tom | 10% Owner | $325.8M | 12,650,000 | $25.76 | [Form 4](https://www.sec.gov/Archives/edgar/data/1471783/000110465926123883/0001104659-26-123883-index.htm) |
| **AXP** AMERICAN EXPRESS CO | Squeri Stephen J | Chairman and CEO, Director | $99.4M | 299,401 | $332.16 | [Form 4](https://www.sec.gov/Archives/edgar/data/4962/000000496226000429/0000004962-26-000429-index.htm) |
| **RCL** ROYAL CARIBBEAN CRUISES LTD | Wilhelmsen Arne Alexander | Director | $82.1M | 250,000 | $328.56 | [Form 4](https://www.sec.gov/Archives/edgar/data/884887/000131734526000018/0001317345-26-000018-index.htm) |
| **LIN** LINDE PLC | White Matthew J | Chief Financial Officer | $45.3M | 86,833 | $521.21 | [Form 4](https://www.sec.gov/Archives/edgar/data/1707925/000162828026071528/0001628280-26-071528-index.htm) |
| **MAR** MARRIOTT INTERNATIONAL INC /MD/ | Capuano Anthony | President & CEO, Director | $26.6M | 63,355 | $420.12 | [Form 4](https://www.sec.gov/Archives/edgar/data/1461996/000122520826008743/0001225208-26-008743-index.htm) |

Full list: [`data/insider/2026/11/2026-11-06.md`](data/insider/2026/11/2026-11-06.md)

## Latest weekly recap

[2026-W45](data/weekly/2026-W45.md)

## How it works

- [`scripts/update.py`](scripts/update.py) (Python stdlib only) runs every weekday via [`.github/workflows/daily.yml`](.github/workflows/daily.yml).
- **Insider trades:** reads SEC EDGAR's daily index, parses every Form 4, and keeps open-market purchases (code `P`) and sales (code `S`).
- **Market:** closing prices for major index ETFs, the 11 S&P sector ETFs, and 40 large-cap stocks.
- **Weekly recap:** every Monday, covering the week just ended, including cluster buys (multiple insiders buying the same company).
- Raw JSON lives in [`data/`](data) for anyone who wants to analyze it.

_Informational only, not investment advice. Data: SEC EDGAR (Form 4) and Yahoo Finance; may contain errors or delays._
