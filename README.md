# 📊 Market Radar

An automatically updated record of **insider trading** (SEC Form 4 open-market buys and sales) and **US market performance**, updated every weekday with a recap each Monday. Collected by GitHub Actions.

**Last updated:** 2026-11-02

## Market close · 2026-11-02

| Index | Close | Change |
|---|---:|---:|
| S&P 500 (SPY) | 752.10 | -0.48% |
| Nasdaq 100 (QQQ) | 681.09 | -1.36% |
| Dow 30 (DIA) | 519.34 | +0.43% |
| Russell 2000 (IWM) | 279.14 | -0.07% |

![Sector performance](charts/sectors-daily.svg)

**Top large-cap gainers:** **GE** +4.63% · **HD** +3.63% · **WMT** +3.38% · **MA** +3.15% · **WFC** +2.99%  
**Top large-cap decliners:** **INTC** -8.80% · **ORCL** -8.76% · **AMD** -7.52% · **XOM** -4.05% · **CVX** -3.29%

## Biggest insider buys · filed 2026-10-30

| Company | Insider | Role | Value | Shares | Avg price | Filing |
|---|---|---|---:|---:|---:|---|
| **RAPP** Rapport Therapeutics, Inc. | HEALY JAMES | Director | $20.4M | 969,480 | $21.00 | [Form 4](https://www.sec.gov/Archives/edgar/data/1245624/000110465926120789/0001104659-26-120789-index.htm) |
| **CRBG** Corebridge Financial, Inc. | NIPPON LIFE INSURANCE CO | 10% Owner | $8.7M | 245,898 | $35.26 | [Form 4](https://www.sec.gov/Archives/edgar/data/1889539/000119312526441956/0001193125-26-441956-index.htm) |
| **LYCA** Lycia Therapeutics, Inc. | Venrock Healthcare Capital Partners III, L.P., VHCP Co-Investment Holdings III, LLC, VHCP Management III, LLC, Venrock Healthcare Capital Partners EG, L.P., VHCP Management EG, LLC, Venrock Healthcare Capital Partners XP, L.P., VHCP Management XP, LLC, Koh Bong Y, Shah Nimish P | 10% Owner | $644.7K | 25,004 | $25.78 | [Form 4](https://www.sec.gov/Archives/edgar/data/1615979/000123191926001519/0001231919-26-001519-index.htm) |
| **BFH** BREAD FINANCIAL HOLDINGS, INC. | Fawcett John J. | Director | $123.5K | 5,000 | $24.70 | [Form 4](https://www.sec.gov/Archives/edgar/data/1101215/000161414326000006/0001614143-26-000006-index.htm) |
| **FFIN** FIRST FINANCIAL BANKSHARES INC | Denny Michael B. | Director | $99.8K | 3,245 | $30.76 | [Form 4](https://www.sec.gov/Archives/edgar/data/1774246/000119312526441381/0001193125-26-441381-index.htm) |
| **OCFC** OCEANFIRST FINANCIAL CORP | Barrett Patrick Sean | Senior EVP & CFO | $89.5K | 5,000 | $17.90 | [Form 4](https://www.sec.gov/Archives/edgar/data/1591893/000159189326000006/0001591893-26-000006-index.htm) |
| **ECF** ELLSWORTH GROWTH & INCOME FUND LTD | Saba Capital Management, L.P. | 10% Owner | $70.9K | 5,975 | $11.87 | [Form 4](https://www.sec.gov/Archives/edgar/data/793040/000151028126000396/0001510281-26-000396-index.htm) |
| **MED** MEDIFAST INC | Kiai Parsa | Director | $68.0K | 5,557 | $12.24 | [Form 4](https://www.sec.gov/Archives/edgar/data/1766850/000121390026114242/0001213900-26-114242-index.htm) |
| **PKBK** PARKE BANCORP, INC. | PANTILIONE VITO S | President & CEO, Director | $42.7K | 1,300 | $32.86 | [Form 4](https://www.sec.gov/Archives/edgar/data/1323979/000143774926034164/0001437749-26-034164-index.htm) |
| **BHRB** Burke & Herbert Financial Services Corp. | McLaughlin Shawn Patrick | Director | $35.5K | 500 | $71.00 | [Form 4](https://www.sec.gov/Archives/edgar/data/1964333/000196449326000010/0001964493-26-000010-index.htm) |

## Biggest insider sales · filed 2026-10-30

| Company | Insider | Role | Value | Shares | Avg price | Filing |
|---|---|---|---:|---:|---:|---|
| **HLT** Hilton Worldwide Holdings Inc. | Jacobs Kevin J | See Remarks | $53.8M | 151,050 | $356.19 | [Form 4](https://www.sec.gov/Archives/edgar/data/1585689/000159315626000010/0001593156-26-000010-index.htm) |
| **BROS** Dutch Bros Inc. | Boersma Travis | Executive Chairman of Board, Director, 10% Owner | $18.0M | 408,023 | $44.03 | [Form 4](https://www.sec.gov/Archives/edgar/data/1883154/000186658126000164/0001866581-26-000164-index.htm) |
| **WRLD** WORLD ACCEPTANCE CORP | Prescott General Partners LLC | 10% Owner | $15.0M | 88,324 | $169.83 | [Form 4](https://www.sec.gov/Archives/edgar/data/1538653/000110465926120643/0001104659-26-120643-index.htm) |
| **DDOG** Datadog, Inc. | Le-Quoc Alexis | Chief Technology Officer, Director | $12.1M | 43,224 | $278.90 | [Form 4](https://www.sec.gov/Archives/edgar/data/1561550/000156155026000326/0001561550-26-000326-index.htm) |
| **BROS** Dutch Bros Inc. | DM Trust Aggregator, LLC | 10% Owner | $11.7M | 266,000 | $44.03 | [Form 4](https://www.sec.gov/Archives/edgar/data/1883105/000186658126000166/0001866581-26-000166-index.htm) |

Full list: [`data/insider/2026/10/2026-10-30.md`](data/insider/2026/10/2026-10-30.md)

## Latest weekly recap

[2026-W44](data/weekly/2026-W44.md)

## How it works

- [`scripts/update.py`](scripts/update.py) (Python stdlib only) runs every weekday via [`.github/workflows/daily.yml`](.github/workflows/daily.yml).
- **Insider trades:** reads SEC EDGAR's daily index, parses every Form 4, and keeps open-market purchases (code `P`) and sales (code `S`).
- **Market:** closing prices for major index ETFs, the 11 S&P sector ETFs, and 40 large-cap stocks.
- **Weekly recap:** every Monday, covering the week just ended, including cluster buys (multiple insiders buying the same company).
- Raw JSON lives in [`data/`](data) for anyone who wants to analyze it.

_Informational only, not investment advice. Data: SEC EDGAR (Form 4) and Yahoo Finance; may contain errors or delays._
