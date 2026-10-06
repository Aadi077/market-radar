# 📊 Market Radar

An automatically updated record of **insider trading** (SEC Form 4 open-market buys and sales) and **US market performance**, updated every weekday with a recap each Monday. Collected by GitHub Actions.

**Last updated:** 2026-10-05

## Market close · 2026-10-05

| Index | Close | Change |
|---|---:|---:|
| S&P 500 (SPY) | 774.83 | +0.67% |
| Nasdaq 100 (QQQ) | 756.20 | +0.88% |
| Dow 30 (DIA) | 512.11 | +0.20% |
| Russell 2000 (IWM) | 283.38 | +0.66% |

![Sector performance](charts/sectors-daily.svg)

**Top large-cap gainers:** **TMO** +3.35% · **V** +2.51% · **MA** +2.23% · **TSLA** +2.20% · **NVDA** +2.12%  
**Top large-cap decliners:** **MRK** -3.30% · **INTC** -2.63% · **CRM** -2.09% · **JNJ** -1.21% · **GE** -1.04%

## Biggest insider buys · filed 2026-10-02

| Company | Insider | Role | Value | Shares | Avg price | Filing |
|---|---|---|---:|---:|---:|---|
| Fortress Net Lease REIT | TIEDEMANN ADVISORS, LLC, TTC MULTI-STRATEGY FUND QP, LP, Tiedemann Advisors GP, LLC, AlTi Global, Inc., AlTi Wealth & Capital Solutions Holdings, LLC, AlTi Global Holdings, LLC, AlTi Global Topco Ltd, AlTI Global Capital, LLC | 10% Owner | $20.0M | 1,860,569 | $10.75 | [Form 4](https://www.sec.gov/Archives/edgar/data/2046389/000091957426006648/0000919574-26-006648-index.htm) |
| **GME** GameStop Corp. | Cohen Ryan | President, CEO and Chairman, Director | $17.1M | 700,000 | $24.41 | [Form 4](https://www.sec.gov/Archives/edgar/data/1767470/000092189526002719/0000921895-26-002719-index.htm) |
| **CRBG** Corebridge Financial, Inc. | NIPPON LIFE INSURANCE CO | 10% Owner | $11.7M | 348,215 | $33.65 | [Form 4](https://www.sec.gov/Archives/edgar/data/1889539/000119312526412414/0001193125-26-412414-index.htm) |
| **PAM** Pampa Energy Inc. | Mindlin Damian Miguel | Vicepresident | $5.6M | 1,432,197 | $3.89 | [Form 4](https://www.sec.gov/Archives/edgar/data/2028916/000202891626000011/0002028916-26-000011-index.htm) |
| **PORT.U** Southport Acquisition Corp. II | SOUTHPORT ACQUISITION SPONSOR II LLC | 10% Owner | $5.0M | 500,000 | $10.00 | [Form 4](https://www.sec.gov/Archives/edgar/data/2151492/000118518526004542/0001185185-26-004542-index.htm) |
| **PORT.U** Southport Acquisition Corp. II | SPENCER JEB S., SOUTHPORT SPONSOR MANAGEMENT II, LLC | CEO and CFO, Director, 10% Owner | $5.0M | 500,000 | $10.00 | [Form 4](https://www.sec.gov/Archives/edgar/data/2151215/000118518526004541/0001185185-26-004541-index.htm) |
| **NYAX** Nayax Ltd. | Nechmad Yair | CEO, Co Founder & Chairman | $2.1M | 44,148 | $47.84 | [Form 4](https://www.sec.gov/Archives/edgar/data/1901279/000197640826000880/0001976408-26-000880-index.htm) |
| **FGBI** First Guaranty Bancshares, Inc. | Smith Edgar R. III | Director, 10% Owner | $822.0K | 99,277 | $8.28 | [Form 4](https://www.sec.gov/Archives/edgar/data/1408534/000143774926031876/0001437749-26-031876-index.htm) |
| **DLHC** DLH Holdings Corp. | Mink Brook Asset Management LLC | 10% Owner | $736.7K | 199,099 | $3.70 | [Form 4](https://www.sec.gov/Archives/edgar/data/785557/000162828026064396/0001628280-26-064396-index.htm) |
| **ACOG** Alpha Cognition Inc. | Opaleye Management Inc. | 10% Owner | $165.6K | 19,050 | $8.69 | [Form 4](https://www.sec.gov/Archives/edgar/data/1655923/000149315226045511/0001493152-26-045511-index.htm) |

## Biggest insider sales · filed 2026-10-02

| Company | Insider | Role | Value | Shares | Avg price | Filing |
|---|---|---|---:|---:|---:|---|
| **CRWD** CrowdStrike Holdings, Inc. | Sentonas Michael | PRESIDENT | $64.2M | 241,944 | $265.45 | [Form 4](https://www.sec.gov/Archives/edgar/data/1535527/000095010326015176/0000950103-26-015176-index.htm) |
| **LITE** Lumentum Holdings Inc. | Ali Wajid | EVP & CHIEF FINANCIAL OFFICER | $25.7M | 24,542 | $1,048.50 | [Form 4](https://www.sec.gov/Archives/edgar/data/1561100/000156110026000008/0001561100-26-000008-index.htm) |
| **SNOW** Snowflake Inc. | Speiser Michael L | Director | $17.5M | 50,741 | $344.00 | [Form 4](https://www.sec.gov/Archives/edgar/data/1640147/000143364426000017/0001433644-26-000017-index.htm) |
| **STX** Seagate Technology Holdings plc | MOSLEY WILLIAM D | CEO, Director | $17.4M | 18,998 | $914.67 | [Form 4](https://www.sec.gov/Archives/edgar/data/1388390/000113778926000261/0001137789-26-000261-index.htm) |
| **BABA** Alibaba Group Holding Ltd | Jiang Fang | Chief People Officer | $12.0M | 885,272 | $13.55 | [Form 4](https://www.sec.gov/Archives/edgar/data/1577552/000119312526411206/0001193125-26-411206-index.htm) |

Full list: [`data/insider/2026/10/2026-10-02.md`](data/insider/2026/10/2026-10-02.md)

## Latest weekly recap

[2026-W40](data/weekly/2026-W40.md)

## How it works

- [`scripts/update.py`](scripts/update.py) (Python stdlib only) runs every weekday via [`.github/workflows/daily.yml`](.github/workflows/daily.yml).
- **Insider trades:** reads SEC EDGAR's daily index, parses every Form 4, and keeps open-market purchases (code `P`) and sales (code `S`).
- **Market:** closing prices for major index ETFs, the 11 S&P sector ETFs, and 40 large-cap stocks.
- **Weekly recap:** every Monday, covering the week just ended, including cluster buys (multiple insiders buying the same company).
- Raw JSON lives in [`data/`](data) for anyone who wants to analyze it.

_Informational only, not investment advice. Data: SEC EDGAR (Form 4) and Yahoo Finance; may contain errors or delays._
