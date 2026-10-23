# 📊 Market Radar

An automatically updated record of **insider trading** (SEC Form 4 open-market buys and sales) and **US market performance**, updated every weekday with a recap each Monday. Collected by GitHub Actions.

**Last updated:** 2026-10-22

## Market close · 2026-10-21

| Index | Close | Change |
|---|---:|---:|
| S&P 500 (SPY) | 773.09 | +0.53% |
| Nasdaq 100 (QQQ) | 725.20 | +1.05% |
| Dow 30 (DIA) | 527.70 | +0.64% |
| Russell 2000 (IWM) | 276.48 | +0.25% |

![Sector performance](charts/sectors-daily.svg)

**Top large-cap gainers:** **PLTR** +4.74% · **IBM** +3.94% · **TSLA** +3.41% · **AMD** +3.36% · **NVDA** +2.54%  
**Top large-cap decliners:** **NFLX** -5.31% · **GOOGL** -1.62% · **PG** -1.56% · **ORCL** -1.53% · **ABBV** -1.48%

## Biggest insider buys · filed 2026-10-21

| Company | Insider | Role | Value | Shares | Avg price | Filing |
|---|---|---|---:|---:|---:|---|
| **GXVIX** Global X Venture & Innovation Fund | GLOBAL X MANAGEMENT COMPANY, INC. | 10% Owner | $25.0M | 1,945,525 | $12.85 | [Form 4](https://www.sec.gov/Archives/edgar/data/1579960/000121390026111339/0001213900-26-111339-index.htm) |
| **CRBG** Corebridge Financial, Inc. | NIPPON LIFE INSURANCE CO | 10% Owner | $5.6M | 162,024 | $34.51 | [Form 4](https://www.sec.gov/Archives/edgar/data/1889539/000119312526427950/0001193125-26-427950-index.htm) |
| **BPRE** Bluerock Private Real Estate Fund | KAMFAR RAMIN | Director | $3.3M | 271,555 | $12.32 | [Form 4](https://www.sec.gov/Archives/edgar/data/1551047/000139834426018550/0001398344-26-018550-index.htm) |
| **FBK** FB Financial Corp | INGRAM ORRIN H II | Director | $1.5M | 29,081 | $52.88 | [Form 4](https://www.sec.gov/Archives/edgar/data/1649749/000119147326000008/0001191473-26-000008-index.htm) |
| **TENX** TENAX THERAPEUTICS, INC. | ADAR1 Capital Management, LLC, Schneeberger Daniel | 10% Owner | $1.5M | 922,849 | $1.59 | [Form 4](https://www.sec.gov/Archives/edgar/data/1940272/000194027226000027/0001940272-26-000027-index.htm) |
| **GF** NEW GERMANY FUND INC | Saba Capital Management, L.P. | 10% Owner | $906.9K | 87,623 | $10.35 | [Form 4](https://www.sec.gov/Archives/edgar/data/858706/000151028126000367/0001510281-26-000367-index.htm) |
| MSD Investment Corp. | Williams Brian S | See Remarks | $310.9K | 13,130 | $23.68 | [Form 4](https://www.sec.gov/Archives/edgar/data/1849894/000119312526427983/0001193125-26-427983-index.htm) |
| **RAPP** Rapport Therapeutics, Inc. | Ignelzi Troy A. | Chief Financial Officer | $143.6K | 5,500 | $26.10 | [Form 4](https://www.sec.gov/Archives/edgar/data/1579829/000119312526428018/0001193125-26-428018-index.htm) |
| **CRF** CORNERSTONE TOTAL RETURN FUND INC | Bradshaw Joshua | Vice Chairman and President, Director | $117.6K | 20,000 | $5.88 | [Form 4](https://www.sec.gov/Archives/edgar/data/1892951/000139834426018542/0001398344-26-018542-index.htm) |
| **DX** DYNEX CAPITAL INC | BOSTON BYRON L | Co-CEO & Chairman of the Board, Director | $100.0K | 9,180 | $10.89 | [Form 4](https://www.sec.gov/Archives/edgar/data/1283563/000082667526000124/0000826675-26-000124-index.htm) |

## Biggest insider sales · filed 2026-10-21

| Company | Insider | Role | Value | Shares | Avg price | Filing |
|---|---|---|---:|---:|---:|---|
| **SNOW** Snowflake Inc. | Slootman Frank | Director | $94.9M | 300,000 | $316.43 | [Form 4](https://www.sec.gov/Archives/edgar/data/1402348/000140234826000020/0001402348-26-000020-index.htm) |
| **TALO** TALOS ENERGY INC. | Control Empresarial de Capitales S.A. de C.V. | 10% Owner | $38.6M | 2,141,590 | $18.01 | [Form 4](https://www.sec.gov/Archives/edgar/data/1273693/000114036126040419/0001140361-26-040419-index.htm) |
| **CVX** CHEVRON CORP | Pate R. Hewitt | Chief Legal Officer | $9.8M | 43,100 | $226.59 | [Form 4](https://www.sec.gov/Archives/edgar/data/93410/000009341026000194/0000093410-26-000194-index.htm) |
| **GTLB** Gitlab Inc. | Sijbrandij Sytse | Director | $6.2M | 116,200 | $53.27 | [Form 4](https://www.sec.gov/Archives/edgar/data/1653482/000165348226000176/0001653482-26-000176-index.htm) |
| **ALMR** Alamar Biosciences, Inc. | Qiming Corporate GP VI, Ltd., Qiming Managing Directors Fund VI, L.P., Qiming Venture Partners VI, L.P., Qiming GP VIII, LLC, Qiming Venture Partners VIII Investments, LLC, Qiming GP VIII-HC, LLC, Qiming Venture Partners VIII-HC, L.P. | 10% Owner | $5.9M | 217,512 | $27.35 | [Form 4](https://www.sec.gov/Archives/edgar/data/2104204/000123191926001485/0001231919-26-001485-index.htm) |

Full list: [`data/insider/2026/10/2026-10-21.md`](data/insider/2026/10/2026-10-21.md)

## Latest weekly recap

[2026-W42](data/weekly/2026-W42.md)

## How it works

- [`scripts/update.py`](scripts/update.py) (Python stdlib only) runs every weekday via [`.github/workflows/daily.yml`](.github/workflows/daily.yml).
- **Insider trades:** reads SEC EDGAR's daily index, parses every Form 4, and keeps open-market purchases (code `P`) and sales (code `S`).
- **Market:** closing prices for major index ETFs, the 11 S&P sector ETFs, and 40 large-cap stocks.
- **Weekly recap:** every Monday, covering the week just ended, including cluster buys (multiple insiders buying the same company).
- Raw JSON lives in [`data/`](data) for anyone who wants to analyze it.

_Informational only, not investment advice. Data: SEC EDGAR (Form 4) and Yahoo Finance; may contain errors or delays._
