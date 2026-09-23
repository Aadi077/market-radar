# 📊 Market Radar

A daily, automatically updated record of **insider trading** (SEC Form 4 open-market buys and sales) and **US market performance**, with a weekly recap every Sunday. Collected by GitHub Actions.

**Last updated:** 2026-09-22

## Market close · 2026-09-21

| Index | Close | Change |
|---|---:|---:|
| S&P 500 (SPY) | 773.50 | +1.55% |
| Nasdaq 100 (QQQ) | 741.47 | +2.77% |
| Dow 30 (DIA) | 519.78 | +0.76% |
| Russell 2000 (IWM) | 285.58 | +0.52% |

![Sector performance](charts/sectors-daily.svg)

**Top large-cap gainers:** **INTC** +12.14% · **META** +11.34% · **AMD** +9.95% · **PLTR** +3.07% · **TSLA** +3.03%  
**Top large-cap decliners:** **XOM** -3.20% · **CVX** -2.79% · **BRK-B** -1.52% · **KO** -1.28% · **HD** -0.93%

## Biggest insider buys · filed 2026-09-21

| Company | Insider | Role | Value | Shares | Avg price | Filing |
|---|---|---|---:|---:|---:|---|
| **LEN, LEN.B** LENNAR CORP /NEW/ | BERKSHIRE HATHAWAY INC, BUFFETT WARREN E | 10% Owner | $212.4M | 2,743,529 | $77.42 | [Form 4](https://www.sec.gov/Archives/edgar/data/1067983/000119312526397059/0001193125-26-397059-index.htm) |
| **GRAB** Grab Holdings Ltd | Tan Anthony Ping Yeow | Chief Executive Officer, Director | $29.9M | 10,350,000 | $2.89 | [Form 4](https://www.sec.gov/Archives/edgar/data/1855612/000189649726000009/0001896497-26-000009-index.htm) |
| **GSAT** Globalstar, Inc. | Monroe James III | Director, 10% Owner | $29.8M | 361,600 | $82.52 | [Form 4](https://www.sec.gov/Archives/edgar/data/1366868/000137966426000002/0001379664-26-000002-index.htm) |
| **GME** GameStop Corp. | Cohen Ryan | President, CEO and Chairman, Director | $26.4M | 1,150,680 | $22.94 | [Form 4](https://www.sec.gov/Archives/edgar/data/1767470/000092189526002608/0000921895-26-002608-index.htm) |
| **LNBIX** Lincoln Bain Capital Total Credit Fund | Lincoln Financial Investments Corp | 10% Owner | $25.0M | 2,460,630 | $10.16 | [Form 4](https://www.sec.gov/Archives/edgar/data/2054992/000119312526396327/0001193125-26-396327-index.htm) |
| **GPI** GROUP 1 AUTOMOTIVE INC | Conifer Management, L.L.C. | 10% Owner | $16.9M | 65,650 | $256.78 | [Form 4](https://www.sec.gov/Archives/edgar/data/1773994/000090514826004241/0000905148-26-004241-index.htm) |
| **ENHA** Enhanced Group Inc. | Apeiron Investment Group Ltd., Enhanced Holdings LP, Angermayer Christian | Director, 10% Owner | $7.0M | 6,080,047 | $1.15 | [Form 4](https://www.sec.gov/Archives/edgar/data/1845872/000119312526397056/0001193125-26-397056-index.htm) |
| **CRBG** Corebridge Financial, Inc. | NIPPON LIFE INSURANCE CO | 10% Owner | $6.2M | 174,760 | $35.20 | [Form 4](https://www.sec.gov/Archives/edgar/data/1889539/000119312526396726/0001193125-26-396726-index.htm) |
| **BBD** BANK BRADESCO | de Oliveira Andre Luis Duarte | Executive Officer | $5.6M | 309,111 | $17.98 | [Form 4](https://www.sec.gov/Archives/edgar/data/1160330/000129281426004621/0001292814-26-004621-index.htm) |
| **CYBN** CYBIN INC. | Halstead Michael | Chief Executive Officer | $1.3M | 100,000 | $13.47 | [Form 4](https://www.sec.gov/Archives/edgar/data/1833141/000091228226001293/0000912282-26-001293-index.htm) |

## Biggest insider sales · filed 2026-09-21

| Company | Insider | Role | Value | Shares | Avg price | Filing |
|---|---|---|---:|---:|---:|---|
| **BZ** Kanzhun Ltd | Zhao Peng Jonathan | Chief Executive Officer, Director, 10% Owner | $110.0M | 15,170,000 | $7.25 | [Form 4](https://www.sec.gov/Archives/edgar/data/1842827/000110465926109348/0001104659-26-109348-index.htm) |
| **ANET** Arista Networks, Inc. | BECHTOLSHEIM ANDREAS | 10% Owner | $59.7M | 300,000 | $198.95 | [Form 4](https://www.sec.gov/Archives/edgar/data/1596532/000159653226000230/0001596532-26-000230-index.htm) |
| **TWST** Twist Bioscience Corp | Leproust Emily M. | Chief Executive Officer, Director | $56.3M | 356,546 | $157.99 | [Form 4](https://www.sec.gov/Archives/edgar/data/1753655/000121465926011832/0001214659-26-011832-index.htm) |
| **SNDK** Sandisk Corp | Goeckeler David | Chairman & CEO, Director | $53.3M | 33,841 | $1,574.21 | [Form 4](https://www.sec.gov/Archives/edgar/data/1713941/000124264826000041/0001242648-26-000041-index.htm) |
| **DELL** Dell Technologies Inc. | Silver Lake Partners IV, L.P., Silver Lake Technology Associates IV, L.P., SLTA IV (GP), L.L.C., Silver Lake Group, L.L.C., Durban Egon | Director, 10% Owner | $30.7M | 52,488 | $585.77 | [Form 4](https://www.sec.gov/Archives/edgar/data/1571996/000119312526396718/0001193125-26-396718-index.htm) |

Full list: [`data/insider/2026/09/2026-09-21.md`](data/insider/2026/09/2026-09-21.md)

## Latest weekly recap

[2026-W38](data/weekly/2026-W38.md)

## How it works

- [`scripts/update.py`](scripts/update.py) (Python stdlib only) runs daily via [`.github/workflows/daily.yml`](.github/workflows/daily.yml).
- **Insider trades:** reads SEC EDGAR's daily index, parses every Form 4, and keeps open-market purchases (code `P`) and sales (code `S`).
- **Market:** closing prices for major index ETFs, the 11 S&P sector ETFs, and 40 large-cap stocks.
- **Weekly recap:** every Sunday, including cluster buys (multiple insiders buying the same company).
- Raw JSON lives in [`data/`](data) for anyone who wants to analyze it.

_Informational only, not investment advice. Data: SEC EDGAR (Form 4) and Yahoo Finance; may contain errors or delays._
