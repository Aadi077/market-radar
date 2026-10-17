# 📊 Market Radar

An automatically updated record of **insider trading** (SEC Form 4 open-market buys and sales) and **US market performance**, updated every weekday with a recap each Monday. Collected by GitHub Actions.

**Last updated:** 2026-10-16

## Market close · 2026-10-15

| Index | Close | Change |
|---|---:|---:|
| S&P 500 (SPY) | 771.79 | +0.28% |
| Nasdaq 100 (QQQ) | 728.00 | -0.13% |
| Dow 30 (DIA) | 521.18 | +1.08% |
| Russell 2000 (IWM) | 275.08 | +1.37% |

![Sector performance](charts/sectors-daily.svg)

**Top large-cap gainers:** **ADBE** +4.57% · **CRM** +4.57% · **HD** +4.31% · **LLY** +3.55% · **TMO** +3.46%  
**Top large-cap decliners:** **CSCO** -3.34% · **INTC** -2.80% · **NVDA** -1.84% · **AMD** -1.50% · **MRK** -1.48%

## Biggest insider buys · filed 2026-10-15

| Company | Insider | Role | Value | Shares | Avg price | Filing |
|---|---|---|---:|---:|---:|---|
| **CRBG** Corebridge Financial, Inc. | NIPPON LIFE INSURANCE CO | 10% Owner | $8.8M | 253,776 | $34.68 | [Form 4](https://www.sec.gov/Archives/edgar/data/1889539/000119312526422935/0001193125-26-422935-index.htm) |
| **BORR** Borr Drilling Ltd | Troim Tor Olav | Director | $3.5M | 750,000 | $4.72 | [Form 4](https://www.sec.gov/Archives/edgar/data/1715497/000162828026065947/0001628280-26-065947-index.htm) |
| **FLSC** Frazier Life Sciences Acquisition Corp. II | Cha Albert, Frazier Life Sciences Holdings II LLC, Frazier Life Sciences Public Fund, L.P., FHMLSP, L.P., FHMLSP, L.L.C. | Chief Executive Officer, Director, 10% Owner | $3.0M | 300,000 | $10.00 | [Form 4](https://www.sec.gov/Archives/edgar/data/1397906/000119312526422957/0001193125-26-422957-index.htm) |
| **GOLD** Gold.com, Inc. | Tether Global Investments Fund, S.I.C.A.F., S.A., TPM, S.A. de C.V., Devasini Giancarlo | 10% Owner | $2.7M | 67,882 | $39.81 | [Form 4](https://www.sec.gov/Archives/edgar/data/2050373/000110465926116094/0001104659-26-116094-index.htm) |
| **TRXB** TRex Bio, Inc. | Alexandria Venture Investments, LLC | 10% Owner | $2.5M | 178,571 | $14.00 | [Form 4](https://www.sec.gov/Archives/edgar/data/1722024/000172202426000004/0001722024-26-000004-index.htm) |
| **PRTA** PROTHENA CORP PUBLIC LTD CO | SCULLY WILLIAM P | 10% Owner | $920.0K | 110,000 | $8.36 | [Form 4](https://www.sec.gov/Archives/edgar/data/1559053/000104546326000021/0001045463-26-000021-index.htm) |
| **CXM** Sprinklr, Inc. | WARD JR STEPHEN M | Director | $850.5K | 150,000 | $5.67 | [Form 4](https://www.sec.gov/Archives/edgar/data/1569345/000116464426000008/0001164644-26-000008-index.htm) |
| **ECF** ELLSWORTH GROWTH & INCOME FUND LTD | Saba Capital Management, L.P. | 10% Owner | $658.4K | 56,083 | $11.74 | [Form 4](https://www.sec.gov/Archives/edgar/data/793040/000151028126000349/0001510281-26-000349-index.htm) |
| **MXF** MEXICO EQUITY & INCOME FUND INC | Saba Capital Management, L.P. | 10% Owner | $254.3K | 12,791 | $19.88 | [Form 4](https://www.sec.gov/Archives/edgar/data/863900/000151028126000351/0001510281-26-000351-index.htm) |
| **API** Agora, Inc. | Zhao Bin | Chief Executive Officer, Director | $101.5K | 24,132 | $4.21 | [Form 4](https://www.sec.gov/Archives/edgar/data/1802883/000119312526422252/0001193125-26-422252-index.htm) |

## Biggest insider sales · filed 2026-10-15

| Company | Insider | Role | Value | Shares | Avg price | Filing |
|---|---|---|---:|---:|---:|---|
| **KNTK** Kinetik Holdings Inc. | ISQ Global Fund II GP LLC, I Squared Capital, LLC, ISQ Holdings, LLC, Wahba Sadek, Bhandari Gautam | 10% Owner | $109.5M | 2,000,000 | $54.77 | [Form 4](https://www.sec.gov/Archives/edgar/data/2020876/000090514826004480/0000905148-26-004480-index.htm) |
| **TALO** TALOS ENERGY INC. | Control Empresarial de Capitales S.A. de C.V. | 10% Owner | $51.9M | 2,965,446 | $17.49 | [Form 4](https://www.sec.gov/Archives/edgar/data/1273693/000114036126039793/0001140361-26-039793-index.htm) |
| **BJ** BJ's Wholesale Club Holdings, Inc. | Eddy Robert W. | President & CEO, Director | $19.7M | 192,584 | $102.14 | [Form 4](https://www.sec.gov/Archives/edgar/data/1531152/000153115226000073/0001531152-26-000073-index.htm) |
| **FRMI** Fermi Inc. | NEUGEBAUER TOBY R, Melissa A. Neugebauer 2020 Trust | 10% Owner | $14.4M | 4,047,200 | $3.55 | [Form 4](https://www.sec.gov/Archives/edgar/data/2071778/000090514826004482/0000905148-26-004482-index.htm) |
| **IOT** Samsara Inc. | Biswas Sanjit | CHIEF EXECUTIVE OFFICER, Director, 10% Owner | $11.0M | 263,900 | $41.68 | [Form 4](https://www.sec.gov/Archives/edgar/data/1895111/000189511126000020/0001895111-26-000020-index.htm) |

Full list: [`data/insider/2026/10/2026-10-15.md`](data/insider/2026/10/2026-10-15.md)

## Latest weekly recap

[2026-W41](data/weekly/2026-W41.md)

## How it works

- [`scripts/update.py`](scripts/update.py) (Python stdlib only) runs every weekday via [`.github/workflows/daily.yml`](.github/workflows/daily.yml).
- **Insider trades:** reads SEC EDGAR's daily index, parses every Form 4, and keeps open-market purchases (code `P`) and sales (code `S`).
- **Market:** closing prices for major index ETFs, the 11 S&P sector ETFs, and 40 large-cap stocks.
- **Weekly recap:** every Monday, covering the week just ended, including cluster buys (multiple insiders buying the same company).
- Raw JSON lives in [`data/`](data) for anyone who wants to analyze it.

_Informational only, not investment advice. Data: SEC EDGAR (Form 4) and Yahoo Finance; may contain errors or delays._
