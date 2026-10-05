---
name: investment-portfolio-update
description: Use when the user shares a screenshot of their investment portfolio (IBKR stocks or SwissBorg crypto). Parses the holdings and updates portfolio.json in the investment newsletter repo.
---

# Investment Portfolio Update

The user has shared a portfolio screenshot. Parse it and update `portfolio.json`.

## Steps

1. **Identify screenshot type**
   - IBKR: shows tickers, shares, last price, P&L
   - SwissBorg: shows crypto assets, amounts, USD values

2. **Parse all visible positions from the screenshot**

3. **Read current file**
   Path: `Automations/investment-newsletter/portfolio.json`

4. **Update the relevant section only**
   - IBKR screenshot → replace `stocks` array entirely
   - SwissBorg screenshot → replace `crypto` array entirely
   - Always update `last_updated` to today's date (YYYY-MM-DD)

5. **Write updated portfolio.json** using the Write tool

6. **Commit**
   ```
   git add Automations/investment-newsletter/portfolio.json
   git commit -m "chore: update portfolio holdings [date]"
   ```

7. **Confirm to user:** "Portfolio updated. X stocks / Y crypto positions recorded as of [date]. Next Friday's newsletter will use these holdings."

## portfolio.json format

```json
{
  "last_updated": "YYYY-MM-DD",
  "stocks": [
    {"ticker": "GOOGL", "name": "Alphabet", "shares": 10, "last_price": 405.27}
  ],
  "crypto": [
    {"asset": "SOL", "name": "Solana", "amount": 33.98, "value_usd": 3099.92}
  ]
}
```

## Notes
- Shares can be fractional (2.8 shares of AVGO is valid)
- Crypto amounts can be large (23,041 BORG is valid)
- last_price for stocks = last traded price shown in screenshot
- value_usd for crypto = USD value shown in screenshot
- Cash balances (USD Cash) are not included in stocks
