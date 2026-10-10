# 📊 Market Radar

An automatically updated record of **insider trading** (SEC Form 4 open-market buys and sales) and **US market performance**, updated every weekday with a recap each Monday. Collected by GitHub Actions.

**Last updated:** 2026-10-09

## Market close · 2026-10-09

| Index | Close | Change |
|---|---:|---:|
| S&P 500 (SPY) | 778.57 | +0.60% |
| Nasdaq 100 (QQQ) | 751.27 | +0.49% |
| Dow 30 (DIA) | 516.11 | +0.87% |
| Russell 2000 (IWM) | 278.94 | +0.49% |

![Sector performance](charts/sectors-daily.svg)

**Top large-cap gainers:** **PLTR** +5.17% · **ORCL** +4.21% · **AMZN** +3.29% · **CSCO** +3.05% · **V** +2.76%  
**Top large-cap decliners:** **INTC** -2.22% · **AMD** -2.03% · **PEP** -1.85% · **NFLX** -1.77% · **HD** -1.60%

## Biggest insider buys · filed 2026-10-08

| Company | Insider | Role | Value | Shares | Avg price | Filing |
|---|---|---|---:|---:|---:|---|
| **COE** 51Talk Online Education Group | Huang Jack Jiajia | Chief Executive Officer, Director, 10% Owner | $32.3M | 2,812,140 | $11.50 | [Form 4](https://www.sec.gov/Archives/edgar/data/1659494/000202976026000010/0002029760-26-000010-index.htm) |
| **BORR** Borr Drilling Ltd | Troim Tor Olav | Director | $5.4M | 1,250,000 | $4.31 | [Form 4](https://www.sec.gov/Archives/edgar/data/1715497/000162828026065416/0001628280-26-065416-index.htm) |
| **CRBG** Corebridge Financial, Inc. | NIPPON LIFE INSURANCE CO | 10% Owner | $4.1M | 116,345 | $35.23 | [Form 4](https://www.sec.gov/Archives/edgar/data/1889539/000119312526417973/0001193125-26-417973-index.htm) |
| **AVR** Anteris Technologies Global Corp. | L1 Capital Pty Ltd | 10% Owner | $2.0M | 272,695 | $7.18 | [Form 4](https://www.sec.gov/Archives/edgar/data/2011514/000181764626000032/0001817646-26-000032-index.htm) |
| **FUL** FULLER H B CO | BAILLY R JEFFREY | Director | $500.0K | 10,000 | $50.00 | [Form 4](https://www.sec.gov/Archives/edgar/data/1033284/000122520826008325/0001225208-26-008325-index.htm) |
| **IMMR** IMMERSION CORP | Singer Eric | President and CEO, Director | $292.8K | 41,000 | $7.14 | [Form 4](https://www.sec.gov/Archives/edgar/data/1058811/000119312526418131/0001193125-26-418131-index.htm) |
| **PDI** PIMCO Dynamic Income Fund | FLATTUM DAVID C | Director | $249.5K | 17,448 | $14.30 | [Form 4](https://www.sec.gov/Archives/edgar/data/1201917/000120191726000004/0001201917-26-000004-index.htm) |
| **PHK** PIMCO HIGH INCOME FUND | FLATTUM DAVID C | Director | $249.2K | 60,204 | $4.14 | [Form 4](https://www.sec.gov/Archives/edgar/data/1201917/000120191726000005/0001201917-26-000005-index.htm) |
| **GF** NEW GERMANY FUND INC | Saba Capital Management, L.P. | 10% Owner | $57.6K | 5,497 | $10.47 | [Form 4](https://www.sec.gov/Archives/edgar/data/858706/000151028126000332/0001510281-26-000332-index.htm) |
| **CINT** CI&T Inc | Martins Fernando Matt Borges | Director, 10% Owner | $49.3K | 15,745 | $3.13 | [Form 4](https://www.sec.gov/Archives/edgar/data/1868995/000129281426004872/0001292814-26-004872-index.htm) |

## Biggest insider sales · filed 2026-10-08

| Company | Insider | Role | Value | Shares | Avg price | Filing |
|---|---|---|---:|---:|---:|---|
| **ANET** Arista Networks, Inc. | Ullal Jayshree | CEO and Chairperson, Director | $97.6M | 460,374 | $212.09 | [Form 4](https://www.sec.gov/Archives/edgar/data/1596532/000159653226000240/0001596532-26-000240-index.htm) |
| **CBL** CBL & ASSOCIATES PROPERTIES INC | CANYON CAPITAL ADVISORS LLC, Julis Mitchell R, Friedman Joshua S |  | $68.2M | 1,307,500 | $52.19 | [Form 4](https://www.sec.gov/Archives/edgar/data/1074034/000119312526418127/0001193125-26-418127-index.htm) |
| **DELL** Dell Technologies Inc. | Silver Lake Partners IV, L.P., Silver Lake Technology Associates IV, L.P., SLTA IV (GP), L.L.C., Silver Lake Group, L.L.C., Durban Egon | Director, 10% Owner | $31.2M | 54,236 | $575.24 | [Form 4](https://www.sec.gov/Archives/edgar/data/1571996/000119312526417976/0001193125-26-417976-index.htm) |
| **NTNX** Nutanix, Inc. | RAMASWAMI RAJIV | Chief Executive Officer, Director | $29.5M | 400,000 | $73.65 | [Form 4](https://www.sec.gov/Archives/edgar/data/1618732/000119312526418024/0001193125-26-418024-index.htm) |
| **DELL** Dell Technologies Inc. | SL SPV-2, L.P., SLTA SPV-2, L.P., SLTA SPV-2 (GP), L.L.C., Silver Lake Group, L.L.C., Durban Egon | Director, 10% Owner | $26.7M | 46,323 | $575.43 | [Form 4](https://www.sec.gov/Archives/edgar/data/1571996/000119312526417972/0001193125-26-417972-index.htm) |

Full list: [`data/insider/2026/10/2026-10-08.md`](data/insider/2026/10/2026-10-08.md)

## Latest weekly recap

[2026-W40](data/weekly/2026-W40.md)

## How it works

- [`scripts/update.py`](scripts/update.py) (Python stdlib only) runs every weekday via [`.github/workflows/daily.yml`](.github/workflows/daily.yml).
- **Insider trades:** reads SEC EDGAR's daily index, parses every Form 4, and keeps open-market purchases (code `P`) and sales (code `S`).
- **Market:** closing prices for major index ETFs, the 11 S&P sector ETFs, and 40 large-cap stocks.
- **Weekly recap:** every Monday, covering the week just ended, including cluster buys (multiple insiders buying the same company).
- Raw JSON lives in [`data/`](data) for anyone who wants to analyze it.

_Informational only, not investment advice. Data: SEC EDGAR (Form 4) and Yahoo Finance; may contain errors or delays._
