# 📊 Market Radar

A daily, automatically updated record of **insider trading** (SEC Form 4 open-market buys and sales) and **US market performance**, with a weekly recap every Sunday. Collected by GitHub Actions.

**Last updated:** 2026-09-23

## Market close · 2026-09-22

| Index | Close | Change |
|---|---:|---:|
| S&P 500 (SPY) | 773.38 | -0.02% |
| Nasdaq 100 (QQQ) | 747.46 | +0.81% |
| Russell 2000 (IWM) | 287.21 | +0.57% |

![Sector performance](charts/sectors-daily.svg)

**Top large-cap gainers:** **WMT** +2.49% · **INTC** +1.71% · **AMD** +1.34% · **PLTR** +1.04% · **MCD** +1.00%  
**Top large-cap decliners:** **ADBE** -4.52% · **CSCO** -4.50% · **JPM** -3.42% · **BAC** -3.04% · **NFLX** -1.64%

## Biggest insider buys · filed 2026-09-22

| Company | Insider | Role | Value | Shares | Avg price | Filing |
|---|---|---|---:|---:|---:|---|
| **CRBG** Corebridge Financial, Inc. | NIPPON LIFE INSURANCE CO | 10% Owner | $4.6M | 131,333 | $34.88 | [Form 4](https://www.sec.gov/Archives/edgar/data/1889539/000119312526397991/0001193125-26-397991-index.htm) |
| **BBD** BANK BRADESCO | Alvarez Denise Aguiar | Director | $2.3M | 130,596 | $17.98 | [Form 4](https://www.sec.gov/Archives/edgar/data/2126543/000129281426004635/0001292814-26-004635-index.htm) |
| **BBD** BANK BRADESCO | Paris Roberto de Jesus | Executive Officer | $1.7M | 96,702 | $17.98 | [Form 4](https://www.sec.gov/Archives/edgar/data/1160330/000129281426004658/0001292814-26-004658-index.htm) |
| **TPVG** TriplePoint Venture Growth BDC Corp. | Labe James | Chief Executive Officer, Director | $1.5M | 313,865 | $4.71 | [Form 4](https://www.sec.gov/Archives/edgar/data/1594983/000159498326000015/0001594983-26-000015-index.htm) |
| **BBD** BANK BRADESCO | Fernandes Oswaldo Tadeu | Executive Officer | $1.4M | 79,782 | $17.98 | [Form 4](https://www.sec.gov/Archives/edgar/data/1160330/000129281426004654/0001292814-26-004654-index.htm) |
| **BCBP** BCB BANCORP INC | OBrien Thomas M | CHIEF EXECUTIVE OFFICER, Director | $1.2M | 160,000 | $7.75 | [Form 4](https://www.sec.gov/Archives/edgar/data/1228454/000119312526397677/0001193125-26-397677-index.htm) |
| **BBD** BANK BRADESCO | Ramalho Miranda Jose Augusto | Executive Officer | $1.1M | 63,719 | $17.98 | [Form 4](https://www.sec.gov/Archives/edgar/data/1160330/000129281426004646/0001292814-26-004646-index.htm) |
| **BBD** BANK BRADESCO | Machado Silvana Rosa | Executive Officer | $1.1M | 62,048 | $17.98 | [Form 4](https://www.sec.gov/Archives/edgar/data/1160330/000129281426004660/0001292814-26-004660-index.htm) |
| **BBD** BANK BRADESCO | Marcilio Juliano Ribeiro | Executive Officer | $1.1M | 60,779 | $17.98 | [Form 4](https://www.sec.gov/Archives/edgar/data/1160330/000129281426004642/0001292814-26-004642-index.htm) |
| **BBD** BANK BRADESCO | Favarao Vinicius Urias | Executive Officer | $1.1M | 60,492 | $17.98 | [Form 4](https://www.sec.gov/Archives/edgar/data/1160330/000129281426004664/0001292814-26-004664-index.htm) |

## Biggest insider sales · filed 2026-09-22

| Company | Insider | Role | Value | Shares | Avg price | Filing |
|---|---|---|---:|---:|---:|---|
| **NVDA** NVIDIA CORP | STEVENS MARK A | Director | $300.1M | 1,366,000 | $219.73 | [Form 4](https://www.sec.gov/Archives/edgar/data/1045810/000119903926000016/0001199039-26-000016-index.htm) |
| **SNOW** Snowflake Inc. | Slootman Frank | Director | $100.3M | 300,000 | $334.49 | [Form 4](https://www.sec.gov/Archives/edgar/data/1402348/000162828026063114/0001628280-26-063114-index.htm) |
| **CRWD** CrowdStrike Holdings, Inc. | Kurtz George | PRESIDENT AND CEO, Director | $19.5M | 81,501 | $239.77 | [Form 4](https://www.sec.gov/Archives/edgar/data/1535527/000177856426000168/0001778564-26-000168-index.htm) |
| **TEVA** TEVA PHARMACEUTICAL INDUSTRIES LTD | MIGNONE ROBERTO | Director | $14.4M | 367,600 | $39.06 | [Form 4](https://www.sec.gov/Archives/edgar/data/1258394/000119312526397959/0001193125-26-397959-index.htm) |
| **CRWD** CrowdStrike Holdings, Inc. | Sentonas Michael | PRESIDENT | $11.6M | 49,863 | $231.74 | [Form 4](https://www.sec.gov/Archives/edgar/data/1535527/000196827026000015/0001968270-26-000015-index.htm) |

Full list: [`data/insider/2026/09/2026-09-22.md`](data/insider/2026/09/2026-09-22.md)

## Latest weekly recap

[2026-W38](data/weekly/2026-W38.md)

## How it works

- [`scripts/update.py`](scripts/update.py) (Python stdlib only) runs daily via [`.github/workflows/daily.yml`](.github/workflows/daily.yml).
- **Insider trades:** reads SEC EDGAR's daily index, parses every Form 4, and keeps open-market purchases (code `P`) and sales (code `S`).
- **Market:** closing prices for major index ETFs, the 11 S&P sector ETFs, and 40 large-cap stocks.
- **Weekly recap:** every Sunday, including cluster buys (multiple insiders buying the same company).
- Raw JSON lives in [`data/`](data) for anyone who wants to analyze it.

_Informational only, not investment advice. Data: SEC EDGAR (Form 4) and Yahoo Finance; may contain errors or delays._
