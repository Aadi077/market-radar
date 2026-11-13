# 📊 Market Radar

An automatically updated record of **insider trading** (SEC Form 4 open-market buys and sales) and **US market performance**, updated every weekday with a recap each Monday. Collected by GitHub Actions.

**Last updated:** 2026-11-12

## Market close · 2026-11-12

| Index | Close | Change |
|---|---:|---:|
| S&P 500 (SPY) | 757.12 | -0.35% |
| Nasdaq 100 (QQQ) | 688.17 | -0.32% |
| Dow 30 (DIA) | 522.47 | -0.38% |
| Russell 2000 (IWM) | 278.44 | -1.64% |

![Sector performance](charts/sectors-daily.svg)

**Top large-cap gainers:** **AMD** +5.86% · **AVGO** +5.54% · **XOM** +1.84% · **GOOGL** +1.79% · **TSLA** +1.69%  
**Top large-cap decliners:** **NVDA** -4.34% · **GE** -3.47% · **NFLX** -2.87% · **TMO** -2.55% · **INTC** -2.08%

## Biggest insider buys · filed 2026-11-10

| Company | Insider | Role | Value | Shares | Avg price | Filing |
|---|---|---|---:|---:|---:|---|
| **NFRX** 2023 ETF Series Trust | Harrison Street Real Assets Fund LLC | 10% Owner | $24.5M | 932,977 | $26.22 | [Form 4](https://www.sec.gov/Archives/edgar/data/1969674/000168789826000011/0001687898-26-000011-index.htm) |
| **FUN** Six Flags Entertainment Corporation/NEW | JAFFER REHAN | Director | $14.9M | 1,450,000 | $10.30 | [Form 4](https://www.sec.gov/Archives/edgar/data/1364501/000199900126000113/0001999001-26-000113-index.htm) |
| **TXO** TXO Partners, L.P. | SIMPSON BOB R | Director, 10% Owner | $3.1M | 232,839 | $13.22 | [Form 4](https://www.sec.gov/Archives/edgar/data/1182684/000118268426000022/0001182684-26-000022-index.htm) |
| **MXF** MEXICO FUND INC | Saba Capital Management, L.P. | 10% Owner | $2.5M | 124,121 | $20.41 | [Form 4](https://www.sec.gov/Archives/edgar/data/65433/000151028126000425/0001510281-26-000425-index.htm) |
| **PSEC** PROSPECT CAPITAL CORP | Barry John F | CHIEF EXECUTIVE OFFICER, Director, 10% Owner | $1.7M | 1,222,704 | $1.41 | [Form 4](https://www.sec.gov/Archives/edgar/data/1294357/000129435726000018/0001294357-26-000018-index.htm) |
| **LBTY** Liberty Global Ltd. | MALONE JOHN C | 10% Owner | $1.5M | 150,000 | $9.73 | [Form 4](https://www.sec.gov/Archives/edgar/data/1570585/000093779726000037/0000937797-26-000037-index.htm) |
| **MX** MAGNACHIP SEMICONDUCTOR Corp | Amoruso Cristiano | Director | $1.4M | 568,009 | $2.41 | [Form 4](https://www.sec.gov/Archives/edgar/data/2069371/000119312526455960/0001193125-26-455960-index.htm) |
| **PRTA** PROTHENA CORP PUBLIC LTD CO | SCULLY WILLIAM P | 10% Owner | $1.2M | 140,000 | $8.53 | [Form 4](https://www.sec.gov/Archives/edgar/data/1559053/000104546326000024/0001045463-26-000024-index.htm) |
| **ETRA** Electra Therapeutics, Inc. | ORBIMED ADVISORS LLC, OrbiMed Capital GP VII LLC, OrbiMed Genesis GP LLC | Director, 10% Owner | $744.5K | 92,116 | $8.08 | [Form 4](https://www.sec.gov/Archives/edgar/data/2088082/000094787126001010/0000947871-26-001010-index.htm) |
| **ETRA** Electra Therapeutics, Inc. | GORDON CARL L | Director, 10% Owner | $744.5K | 92,116 | $8.08 | [Form 4](https://www.sec.gov/Archives/edgar/data/2088082/000094787126001011/0000947871-26-001011-index.htm) |

## Biggest insider sales · filed 2026-11-10

| Company | Insider | Role | Value | Shares | Avg price | Filing |
|---|---|---|---:|---:|---:|---|
| **RCL** ROYAL CARIBBEAN CRUISES LTD | Wilhelmsen Arne Alexander | Director | $159.8M | 476,674 | $335.29 | [Form 4](https://www.sec.gov/Archives/edgar/data/884887/000131734526000020/0001317345-26-000020-index.htm) |
| **CRBG** Corebridge Financial, Inc. | Argon Holdco LLC, Blackstone Holdings II L.P., Blackstone Holdings I/II GP L.L.C., Blackstone Inc., Blackstone Group Management L.L.C., SCHWARZMAN STEPHEN A | 10% Owner | $110.0M | 3,227,700 | $34.09 | [Form 4](https://www.sec.gov/Archives/edgar/data/2017585/000119312526455577/0001193125-26-455577-index.htm) |
| **ANET** Arista Networks, Inc. | BECHTOLSHEIM ANDREAS | 10% Owner | $43.9M | 260,000 | $168.96 | [Form 4](https://www.sec.gov/Archives/edgar/data/1596532/000159653226000262/0001596532-26-000262-index.htm) |
| **MSI** Motorola Solutions, Inc. | BROWN GREGORY Q | Chairman and CEO, Director | $36.4M | 70,780 | $514.14 | [Form 4](https://www.sec.gov/Archives/edgar/data/1201232/000120123226000019/0001201232-26-000019-index.htm) |
| **INCY** INCYTE CORP | Stein Steven H | CMO & Head of Late-Stage Dev. | $28.4M | 240,193 | $118.39 | [Form 4](https://www.sec.gov/Archives/edgar/data/879169/000167377626000022/0001673776-26-000022-index.htm) |

Full list: [`data/insider/2026/11/2026-11-10.md`](data/insider/2026/11/2026-11-10.md)

## Latest weekly recap

[2026-W45](data/weekly/2026-W45.md)

## How it works

- [`scripts/update.py`](scripts/update.py) (Python stdlib only) runs every weekday via [`.github/workflows/daily.yml`](.github/workflows/daily.yml).
- **Insider trades:** reads SEC EDGAR's daily index, parses every Form 4, and keeps open-market purchases (code `P`) and sales (code `S`).
- **Market:** closing prices for major index ETFs, the 11 S&P sector ETFs, and 40 large-cap stocks.
- **Weekly recap:** every Monday, covering the week just ended, including cluster buys (multiple insiders buying the same company).
- Raw JSON lives in [`data/`](data) for anyone who wants to analyze it.

_Informational only, not investment advice. Data: SEC EDGAR (Form 4) and Yahoo Finance; may contain errors or delays._
