---
name: invoice-generator
description: Use when someone asks to create an invoice, bill a client for services, or generate an invoice from any of Matthieu's companies (PT Swiss Hospitality Consulting or Scalrize).
---

# Invoice Generator

Creates a professional HTML invoice from one of Matthieu's entities, then exports to PDF. Supports two sender profiles. Always asks for the current exchange rate when converting to IDR.

---

## Step 1 — Collect Required Inputs

Ask the user for any missing information:

| Field | Required | Notes |
|---|---|---|
| Sender company | Yes | "PT Swiss Hospitality Consulting" or "Scalrize" |
| Client name | Yes | Full company name |
| Client contact | Optional | e.g. "Attn: Toby" |
| Invoice date | Yes | DD.MM.YYYY |
| Concerns | Yes | Short description, e.g. "Sales Training" |
| Line items | Yes | Description + price for each |
| Invoice currency | Yes | IDR, USD, EUR, CHF |
| Invoice number | Yes | Format: INV-YYYY-NNN (check existing files to auto-increment) |
| Payment split | Optional | e.g. "50% today, 50% before start" |
| Save location | Yes | Default depends on project context |

**If invoice currency is IDR:** Always ask "What is the current USD/IDR exchange rate?" — never use a cached rate.

---

## Step 2 — Sender Profiles

### PT Swiss Hospitality Consulting

**Address:**
Jalan Sunset Road No. 28
Seminyak, Kuta
Kabupaten Badung, Bali 80361
Indonesia

**Bank details (IDR):**
- Bank: Bank Mandiri
- Account number: 175-00-0313369-0
- Account holder: PT Swiss Hospitality Consulting
- Currency: IDR
- Branch: Bali

---

### Scalrize

No company address.

**Design system (use for all Scalrize invoices):**
- Logo: use horizontal logo at `Scalrize/Website/assets.Scalrize/company.logo.horizontal.jpg` — embed via `<img>` tag with absolute file path
- Heading font: Fraunces (serif) — load from Google Fonts: `https://fonts.googleapis.com/css2?family=Fraunces:wght@600;700&family=DM+Sans:wght@400;500;600&display=swap`
- Body font: DM Sans (sans-serif)
- Colors:
  - Primary (sage): `#4f6352`
  - Primary dark: `#3d4e3f`
  - Primary pale: `#e8ede9`
  - Text (ink): `#141917`
  - Text soft: `#242c25`
  - Border: `#e4e8e5`
  - Background: `#ffffff`
- Invoice header: sage background `#4f6352` with white text, logo top-left, INVOICE label top-right
- Table header row: sage `#4f6352` with white text
- Table body rows: alternate `#f0f4f1` / `#ffffff`
- Grand total row: `#141917` background, white text
- "Due Now" badge: sage `#4f6352`
- Bill To block: left border `#4f6352`, background `#f0f4f1`

**Bank details — ask the client's currency, then use the matching Wise account:**

**CHF / international:**
- Name: Matthieu Patrick Jammers
- IBAN: GB61 TRWI 2308 0145 5737 43
- Swift/BIC: TRWIGB2LXXX
- Bank: Wise Payments Limited, 1st Floor, Worship Square, 65 Clifton Street, London, EC2A 4JE, United Kingdom

**USD (from US — domestic):**
- Name: Matthieu Patrick Jammers
- Account type: Checking
- Routing number: 101019628
- Account number: 218566780366
- Bank: Wise US Inc, 108 W 13th St, Wilmington, DE 19801, United States
- Swift/BIC (international): TRWIUS35XXX

**EUR:**
- Name: Matthieu Patrick Jammers
- IBAN: BE81 9057 2093 4824
- Swift/BIC: TRWIBEB1XXX (outside SEPA) / domestic SEPA transfer otherwise
- Bank: Wise, Rue du Trône 100, 3rd floor, Brussels, 1050, Belgium

---

## Step 3 — Calculate Amounts

If invoicing in IDR:
- IDR amount = USD amount × exchange rate
- Format: `X XXX XXX,00` (spaces as thousands separator, comma as decimal)

If invoicing in USD/EUR/CHF: display amounts directly in that currency.

---

## Step 4 — Generate the HTML Invoice

Two design templates depending on sender:

**PT Swiss Hospitality Consulting** — use `reference-invoice.html` (bundled template, see TODO in this skill) as visual reference:
- Header: company name + address (left) | INVOICE label + number (right)
- Meta row: Date, Location (Bali), Concerns
- Bill To block: left border `#1a1a1a`, background `#f7f7f5`
- Items table: header row light blue `#c8dce8`, body rows alternate `#eef4f8` / `#e4edf3`
- Grand total row: `#1a1a1a` background, white text
- Payment schedule: "Due Now" badge in amber `#e8a820`
- FX note (IDR only): italic small text: "Exchange rate: 1 USD = IDR X,XX on [Dth of Month, YYYY]"
- Bank details: Mandiri / IDR profile

**Scalrize** — apply the Scalrize design system from the profile above:
- Header: full-width sage `#4f6352` band, logo left (horizontal JPG), "INVOICE" right in white Fraunces
- No address block under logo
- Meta row: Date, Concerns (no Location needed)
- Bill To block: left border `#4f6352`, background `#f0f4f1`
- Items table: header row sage `#4f6352` white text, body rows alternate `#f0f4f1` / `#ffffff`
- Grand total row: `#141917` background, white text
- Payment schedule: "Due Now" badge in sage `#4f6352`
- FX note (IDR only): same format as above
- Bank details: Wise account matching invoice currency

---

## Step 5 — Save HTML and Export PDF

File naming: `invoice-[client-slug]-[NNN].html` / `.pdf`

Save HTML, then immediately export PDF using Chrome headless:
```
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless --disable-gpu \
  --print-to-pdf="[same path but .pdf]" \
  --print-to-pdf-no-header \
  "file:///[absolute path to .html]"
```

---

## Step 6 — Confirm

Report back:
- HTML + PDF saved at: `[path]`
- Amount due now: [amount in invoice currency]
- Exchange rate used (if IDR): 1 USD = IDR X,XX
