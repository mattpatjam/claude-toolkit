---
name: villa-listing-information
description: Use when someone asks to format a villa listing, create a property listing, or sends a property URL to format for clients.
argument-hint: <property-url>
disable-model-invocation: true
---

## What This Skill Does

Takes a property listing URL, scrapes it with Firecrawl, and formats the details into the Bali Exception client-facing villa listing format.

## Steps

1. Scrape the URL provided in `` using `mcp__firecrawl__firecrawl_scrape`.
2. Extract the following fields from the scraped content (leave blank if not found):
   - Listing type (always: FOR SALE)
   - Number of bedrooms
   - Key selling feature / headline (e.g. "Rooftop Views", "Rice Field Views")
   - Location / area name
   - Nearby landmark (e.g. "1 minute from Nirvana Gym")
   - Price (with currency)
   - Tenure type (Leasehold / Freehold) and duration + extension info
   - Build year or construction period
   - Land size (m²)
   - Build size (m²)
   - Number of bedrooms and bathrooms
   - Interior features (living room, kitchen, etc.)
   - Outdoor features (terrace, views, etc.)
   - Pool details (number, type, location)
   - Furnishing status
   - Climate control (AC, fans)
   - Standout selling points (design, investment appeal, location perks)
   - Availability
3. Format the output using the template below.
4. Output the formatted listing directly to chat.

## Output Template

```
🏡 FOR SALE | [X]BR Villa with [Key Feature] – [Area]

💰 Price: [Currency + Amount]
📍 Location: [Area] – [Nearby landmark if available]
📜 [Leasehold/Freehold]: [Duration + extension info if available]
🏗 Built: [Year or period]

✨ PROPERTY DETAILS:
• Land [X] m² | Build ±[X] m²
• [X] bedrooms with [X] en suite bathrooms
• [Interior features]
• [Outdoor/terrace/view features]
• [Pool details]
• [Furnishing status]
• [Climate control]

🌟 WHY THIS VILLA STANDS OUT:
• [Standout point 1]
• [Standout point 2]
• [Standout point 3]
• [Location perk]

📅 Availability for sale: [Availability]


📲 DM for more information
```

## Notes

- Always use `FOR SALE` — never rental.
- Always output in English.
- If a field is not found on the page, omit that line entirely — do not write "N/A" or "TBD".
- The "WHY THIS VILLA STANDS OUT" section should synthesize the most compelling points from the listing — lead with design/uniqueness, then investment appeal, then location.
- Keep bullet points concise — one line each.
- Do not add commentary or explanation outside the formatted listing.
- **Run humanizer before delivery.** Invoke the `humanizer` skill on all copy before sending to a client. Remove em dashes, AI vocabulary, and promotional language.
