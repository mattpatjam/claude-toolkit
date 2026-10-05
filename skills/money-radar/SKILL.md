---
name: money-radar
description: Use when the user wants an on-demand portfolio intelligence report — portfolio health check, Polymarket macro signals, trade setups (swing/intra-week/intra-day), and second-order opportunities. Trigger phrases: "money radar", "portfolio check", "trade ideas", "what should I be watching", "how's my portfolio", "any trade setups".
---

# Money Radar — On-Demand Portfolio Intelligence

Run a full portfolio intelligence sweep and output a structured report in chat.

## Step 1 — Load Portfolio

Read `Automations/investment-newsletter/portfolio.json` to get current holdings.

Build a quick summary:
- Stocks: ticker, shares, last price, implied value
- Crypto: asset, amount, USD value

## Step 2 — Fetch Polymarket Signals

Run this via Bash:

```bash
curl -s "https://gamma-api.polymarket.com/markets?active=true&closed=false&limit=200&sort=volumeNum&order=desc" | python3 -c "
import json, sys
data = json.load(sys.stdin)
keywords = ['fed', 'rate', 'inflation', 'tariff', 'oil', 'bitcoin', 'btc', 'eth', 'crypto', 'recession', 'iran', 'china', 'trade war', 'gdp', 'dollar', 'treasury', 'nasdaq']
results = []
for m in data:
    q = m.get('question', '').lower()
    if any(k in q for k in keywords):
        outcomes = json.loads(m.get('outcomes', '[]'))
        prices = json.loads(m.get('outcomePrices', '[]'))
        if len(outcomes) >= 2 and len(prices) >= 2:
            if len(outcomes) == 2:
                prob = float(prices[0]) * 100
                results.append(f'{m[\"question\"]}: {prob:.0f}% {outcomes[0]}')
            else:
                idx = max(range(len(prices)), key=lambda i: float(prices[i]))
                prob = float(prices[idx]) * 100
                results.append(f'{m[\"question\"]}: {outcomes[idx]} most likely ({prob:.0f}%)')
for r in results[:10]:
    print(r)
"
```

If the curl fails, note it and continue — Polymarket is a bonus signal, not a blocker.

## Step 3 — Scrape Latest News

Use Firecrawl to scrape news for each portfolio ticker. Run these searches:

- `"{TICKER1} {TICKER2} stock news this week"` — batch the top 4-5 stock positions
- `"macro market outlook fed rates inflation this week"`
- `"crypto bitcoin ethereum market this week"`

Cap at 3 Firecrawl calls. Extract only what's relevant to the portfolio or trade setups.

## Step 4 — Generate the Report

Using everything gathered, write a structured report directly in chat. Format with headers, bullets, and specific numbers. No HTML — plain markdown.

---

### MONEY RADAR — [Today's Date]

**Portfolio Summary**
[Total implied value from portfolio.json. List each position with shares × last_price. Flag any position where last_price is more than 2 weeks old — it may need updating via `/investment-portfolio-update`.]

---

**POLYMARKET SIGNALS**
[List 6-8 probabilities from Step 2. For each, one sentence on what it means for the portfolio. Lead with the ones most relevant to current holdings.]

---

**PORTFOLIO HEALTH CHECK**
[Given current macro conditions and Polymarket signals, rate each position: STRONG / HOLD / WATCH. One sentence per position. Be direct — if a position is out of sync with the current environment, say so.]

Target: Is this portfolio positioned for 10-15% annual return given today's conditions? One sentence verdict.

---

**SWING TRADE SETUPS (1-2 weeks, target 10-20%)**
[2 setups. For each: ticker, direction, entry zone, stop, TP1, TP2, risk/reward, kill switch. Only include if there is a clear catalyst from the news gathered.]

---

**INTRA-WEEK SETUPS (2-3 days, target 10-15%)**
[2 setups. Faster catalyst — earnings reaction, news event, macro release. Entry, stop, target, what kills it.]

---

**INTRA-DAY LEVELS (today's session)**
[For 3 top tickers: key support, key resistance, breakout trigger, breakdown trigger. One sentence on what to watch today.]

---

**SECOND-ORDER OPPORTUNITIES**
[1-2 stocks the market hasn't connected to this week's macro moves. Cause → obvious trade → what the market is missing → why this stock benefits → dislocation. Only include if the chain is verifiable from scraped news. Skip if nothing qualifies.]

---

**ONE SIGNAL TO WATCH**
[The single most important data point or event in the next 5 trading days. One sentence.]

---

## Rules

- Numbers always — never vague language
- If a price is not in source data, say "price not in source data"
- Polymarket probabilities override news sentiment for macro event calls
- If portfolio.json hasn't been updated in 14+ days, flag it at the top and suggest running `/investment-portfolio-update`
- Keep the full report under 600 words — signal only, no padding
