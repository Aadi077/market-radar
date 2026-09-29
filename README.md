# 📊 Market Radar

A daily, automatically updated record of **insider trading** (SEC Form 4 open-market buys and sales) and **US market performance**, with a weekly recap every Sunday. Collected by GitHub Actions.

**Last updated:** 2026-09-28

## Market close · 2026-09-28

| Index | Close | Change |
|---|---:|---:|
| S&P 500 (SPY) | 765.61 | -0.74% |
| Nasdaq 100 (QQQ) | 736.53 | -1.07% |
| Dow 30 (DIA) | 514.02 | -0.67% |
| Russell 2000 (IWM) | 280.02 | -0.69% |

![Sector performance](charts/sectors-daily.svg)

**Top large-cap gainers:** **PG** +1.91% · **NVDA** +1.68% · **XOM** +1.20% · **CVX** +0.94% · **ABBV** +0.73%  
**Top large-cap decliners:** **INTC** -5.67% · **META** -4.79% · **TSLA** -3.94% · **AMD** -3.61% · **ORCL** -3.28%

## Biggest insider buys · filed 2026-09-25

| Company | Insider | Role | Value | Shares | Avg price | Filing |
|---|---|---|---:|---:|---:|---|
| **LEN** LENNAR CORP /NEW/ | BERKSHIRE HATHAWAY INC, BUFFETT WARREN E | 10% Owner | $136.4M | 1,679,700 | $81.19 | [Form 4](https://www.sec.gov/Archives/edgar/data/1067983/000119312526403089/0001193125-26-403089-index.htm) |
| **CRBG** Corebridge Financial, Inc. | NIPPON LIFE INSURANCE CO | 10% Owner | $7.5M | 219,273 | $34.13 | [Form 4](https://www.sec.gov/Archives/edgar/data/1889539/000119312526402895/0001193125-26-402895-index.htm) |
| Calamos Aksia Hedged Strategies Fund | Calamos Aksia Hedged Strategies Fund (Offshore), Ltd. | 10% Owner | $7.5M | 714,183 | $10.47 | [Form 4](https://www.sec.gov/Archives/edgar/data/2063706/000212577326000013/0002125773-26-000013-index.htm) |
| **CX** CEMEX SAB DE CV | Zambrano Lozano Rogelio | Director | $6.9M | 400,800 | $17.28 | [Form 4](https://www.sec.gov/Archives/edgar/data/1076378/000203524426000009/0002035244-26-000009-index.htm) |
| **KBDC** Kayne Anderson BDC, Inc. | ROBO JAMES L | Director | $1.4M | 105,000 | $13.05 | [Form 4](https://www.sec.gov/Archives/edgar/data/1747172/000118325426000007/0001183254-26-000007-index.htm) |
| **NCT** Intercont (Cayman) Ltd | Zhu Muchun | CEO and Chairman, Director | $650.0K | 1,625,000 | $0.40 | [Form 4](https://www.sec.gov/Archives/edgar/data/2018529/000149315226044229/0001493152-26-044229-index.htm) |
| **HRGN** Harvard Apparatus Regenerative Technology, Inc. | He Junli | CEO, Director | $394.5K | 368,630 | $1.07 | [Form 4](https://www.sec.gov/Archives/edgar/data/1563665/000143774926031181/0001437749-26-031181-index.htm) |
| **MX** MAGNACHIP SEMICONDUCTOR Corp | LEE CHAE | Chief Executive Officer, Director | $318.5K | 100,000 | $3.18 | [Form 4](https://www.sec.gov/Archives/edgar/data/1548322/000119312526402849/0001193125-26-402849-index.htm) |
| **MSC** STUDIO CITY INTERNATIONAL HOLDINGS Ltd | HO LAWRENCE YAU LUNG | Director | $206.3K | 1,043,600 | $0.20 | [Form 4](https://www.sec.gov/Archives/edgar/data/1958709/000119312526401498/0001193125-26-401498-index.htm) |
| **ANIX** Anixa Biosciences Inc | Titterton Lewis H jr | Director | $131.9K | 49,036 | $2.69 | [Form 4](https://www.sec.gov/Archives/edgar/data/715446/000149315226044250/0001493152-26-044250-index.htm) |

## Biggest insider sales · filed 2026-09-25

| Company | Insider | Role | Value | Shares | Avg price | Filing |
|---|---|---|---:|---:|---:|---|
| **AVGO** Broadcom Inc. | SAMUELI HENRY | Director | $250.0M | 702,190 | $356.04 | [Form 4](https://www.sec.gov/Archives/edgar/data/1730168/000110465926110983/0001104659-26-110983-index.htm) |
| **CRWD** CrowdStrike Holdings, Inc. | Podbere Burt W. | CHIEF FINANCIAL OFFICER | $125.5M | 480,000 | $261.44 | [Form 4](https://www.sec.gov/Archives/edgar/data/1535527/000177861026000024/0001778610-26-000024-index.htm) |
| **MEDP** Medpace Holdings, Inc. | Troendle August J. | President & CEO, Director, 10% Owner | $27.4M | 43,916 | $624.01 | [Form 4](https://www.sec.gov/Archives/edgar/data/1668397/000162205826000018/0001622058-26-000018-index.htm) |
| **FSLY** Fastly, Inc. | Bergman Artur | Chief Technology Officer, Director | $11.4M | 379,602 | $30.16 | [Form 4](https://www.sec.gov/Archives/edgar/data/1769490/000151741326000298/0001517413-26-000298-index.htm) |
| **DDOG** Datadog, Inc. | Le-Quoc Alexis | Chief Technology Officer, Director | $10.9M | 43,224 | $252.17 | [Form 4](https://www.sec.gov/Archives/edgar/data/1561550/000156155026000320/0001561550-26-000320-index.htm) |

Full list: [`data/insider/2026/09/2026-09-25.md`](data/insider/2026/09/2026-09-25.md)

## Latest weekly recap

[2026-W39](data/weekly/2026-W39.md)

## How it works

- [`scripts/update.py`](scripts/update.py) (Python stdlib only) runs daily via [`.github/workflows/daily.yml`](.github/workflows/daily.yml).
- **Insider trades:** reads SEC EDGAR's daily index, parses every Form 4, and keeps open-market purchases (code `P`) and sales (code `S`).
- **Market:** closing prices for major index ETFs, the 11 S&P sector ETFs, and 40 large-cap stocks.
- **Weekly recap:** every Sunday, including cluster buys (multiple insiders buying the same company).
- Raw JSON lives in [`data/`](data) for anyone who wants to analyze it.

_Informational only, not investment advice. Data: SEC EDGAR (Form 4) and Yahoo Finance; may contain errors or delays._
