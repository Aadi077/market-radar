# 📊 Market Radar

An automatically updated record of **insider trading** (SEC Form 4 open-market buys and sales) and **US market performance**, updated every weekday with a recap each Monday. Collected by GitHub Actions.

**Last updated:** 2026-10-14

## Market close · 2026-10-14

| Index | Close | Change |
|---|---:|---:|
| S&P 500 (SPY) | 769.60 | -1.08% |
| Nasdaq 100 (QQQ) | 728.95 | -1.97% |
| Dow 30 (DIA) | 515.63 | -0.11% |
| Russell 2000 (IWM) | 271.37 | -1.93% |

![Sector performance](charts/sectors-daily.svg)

**Top large-cap gainers:** **UNH** +4.73% · **MRK** +3.80% · **LLY** +3.62% · **WMT** +3.46% · **COST** +2.87%  
**Top large-cap decliners:** **ORCL** -8.83% · **AMD** -5.73% · **BAC** -4.76% · **INTC** -4.56% · **NVDA** -3.16%

## Biggest insider buys · filed 2026-10-13

| Company | Insider | Role | Value | Shares | Avg price | Filing |
|---|---|---|---:|---:|---:|---|
| **GME** GameStop Corp. | Cohen Ryan | President, CEO and Chairman, Director | $22.8M | 844,130 | $26.98 | [Form 4](https://www.sec.gov/Archives/edgar/data/1767470/000092189526002784/0000921895-26-002784-index.htm) |
| **BORR** Borr Drilling Ltd | Troim Tor Olav | Director | $11.8M | 2,500,000 | $4.74 | [Form 4](https://www.sec.gov/Archives/edgar/data/1715497/000162828026065603/0001628280-26-065603-index.htm) |
| **CRBG** Corebridge Financial, Inc. | NIPPON LIFE INSURANCE CO | 10% Owner | $9.0M | 261,198 | $34.30 | [Form 4](https://www.sec.gov/Archives/edgar/data/1889539/000119312526420489/0001193125-26-420489-index.htm) |
| **PED** PEDEVCO CORP | KUKES SIMON G, SGK 2018 REVOCABLE TRUST | 10% Owner, Chief Executive Officer, Director | $1.9M | 147,070 | $13.00 | [Form 4](https://www.sec.gov/Archives/edgar/data/1222390/000165495426008905/0001654954-26-008905-index.htm) |
| **TRXB** TRex Bio, Inc. | SVLSF VI, LLC, SV Life Sciences Fund VI (GP), L.P., SV Life Sciences Fund VI, L.P. | 10% Owner | $1.3M | 92,857 | $14.00 | [Form 4](https://www.sec.gov/Archives/edgar/data/1717730/000182912626011084/0001829126-26-011084-index.htm) |
| **GOLD** Gold.com, Inc. | Tether Global Investments Fund, S.I.C.A.F., S.A., TPM, S.A. de C.V., Devasini Giancarlo | 10% Owner | $1.3M | 32,118 | $39.87 | [Form 4](https://www.sec.gov/Archives/edgar/data/2050373/000110465926115328/0001104659-26-115328-index.htm) |
| **IIPR** INNOVATIVE INDUSTRIAL PROPERTIES INC | Gold Alan D | EXECUTIVE CHAIRMAN, Director | $1.0M | 40,000 | $25.00 | [Form 4](https://www.sec.gov/Archives/edgar/data/1298786/000089706926001838/0000897069-26-001838-index.htm) |
| **ONMD** OneMedNet Corp | Kosasa Thomas | Director, 10% Owner | $750.0K | 129,758 | $5.78 | [Form 4](https://www.sec.gov/Archives/edgar/data/1989846/000149315226046909/0001493152-26-046909-index.htm) |
| **API** Agora, Inc. | Zhao Bin | Chief Executive Officer, Director | $695.7K | 167,385 | $4.16 | [Form 4](https://www.sec.gov/Archives/edgar/data/1802883/000119312526419691/0001193125-26-419691-index.htm) |
| **AVO** Mission Produce, Inc. | Gonzalez Luis A | Director | $594.8K | 52,022 | $11.43 | [Form 4](https://www.sec.gov/Archives/edgar/data/1825885/000182588526000008/0001825885-26-000008-index.htm) |

## Biggest insider sales · filed 2026-10-13

| Company | Insider | Role | Value | Shares | Avg price | Filing |
|---|---|---|---:|---:|---:|---|
| **MDLN** Medline Inc. | GIC Private Ltd, GIC Special Investments Pte Ltd, Hux Investment Pte. Ltd. | 10% Owner | $274.8M | 7,816,987 | $35.15 | [Form 4](https://www.sec.gov/Archives/edgar/data/936828/000119312526419824/0001193125-26-419824-index.htm) |
| **ESTC** Elastic N.V. | Schuurman Steven | Director | $188.3M | 2,000,000 | $94.15 | [Form 4](https://www.sec.gov/Archives/edgar/data/1707753/000112329226001388/0001123292-26-001388-index.htm) |
| **TALO** TALOS ENERGY INC. | Control Empresarial de Capitales S.A. de C.V. | 10% Owner | $106.8M | 6,240,000 | $17.12 | [Form 4](https://www.sec.gov/Archives/edgar/data/1273693/000114036126039478/0001140361-26-039478-index.htm) |
| **SBET** Sharplink, Inc. | Lubin Joseph Michael | Director | $47.6M | 5,676,952 | $8.39 | [Form 4](https://www.sec.gov/Archives/edgar/data/2071490/000149315226046898/0001493152-26-046898-index.htm) |
| **ANET** Arista Networks, Inc. | Ullal Jayshree | CEO and Chairperson, Director | $34.4M | 158,543 | $217.09 | [Form 4](https://www.sec.gov/Archives/edgar/data/1596532/000159653226000244/0001596532-26-000244-index.htm) |

Full list: [`data/insider/2026/10/2026-10-13.md`](data/insider/2026/10/2026-10-13.md)

## Latest weekly recap

[2026-W41](data/weekly/2026-W41.md)

## How it works

- [`scripts/update.py`](scripts/update.py) (Python stdlib only) runs every weekday via [`.github/workflows/daily.yml`](.github/workflows/daily.yml).
- **Insider trades:** reads SEC EDGAR's daily index, parses every Form 4, and keeps open-market purchases (code `P`) and sales (code `S`).
- **Market:** closing prices for major index ETFs, the 11 S&P sector ETFs, and 40 large-cap stocks.
- **Weekly recap:** every Monday, covering the week just ended, including cluster buys (multiple insiders buying the same company).
- Raw JSON lives in [`data/`](data) for anyone who wants to analyze it.

_Informational only, not investment advice. Data: SEC EDGAR (Form 4) and Yahoo Finance; may contain errors or delays._
