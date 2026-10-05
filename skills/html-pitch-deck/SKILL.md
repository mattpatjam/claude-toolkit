---
name: html-pitch-deck
description: Use when someone asks to build a pitch deck, create an HTML presentation, make a proposal document, or generate a leave-behind as HTML or PDF. Produces a standalone A4-formatted HTML file that prints cleanly to PDF.
disable-model-invocation: true
argument-hint: [content brief or file path]
---

## What This Skill Does

Builds a standalone HTML pitch deck or proposal document formatted as discrete A4 pages (210mm × 297mm). What you see in the browser is exactly what prints to PDF. No dependencies — all CSS is inline, fonts via Google Fonts CDN.

**Default brand:** OLC Method (Cormorant + DM Sans + sage green palette). Override by specifying brand tokens in the brief.

---

## Inputs

- `` — content brief (inline text) or path to a brief/markdown file. If no argument, ask the user for the content.
- Optional in brief: `brand:` key with color overrides, font overrides, or logo path
- Optional in brief: `output:` key with target file path

---

## Step-by-Step Process

**Step 1 — Read the brief**

If `` is a file path, read the file. If it's inline text, use it directly. Extract:
- Pitch title and recipient name
- Sections and their content
- Any brand overrides (colors, fonts, logo)
- Output file path (if specified)

If output path is not specified, ask: "Where should I save this? (e.g., `clients/nirvana/deck.html`)"

**Step 2 — Plan the pages**

Map sections to A4 pages. Each page should contain one focused idea. Guidelines:
- Cover = 1 page
- Each major section = 1 page (split if content is too dense)
- Terms/pricing = 1 page
- Next step/CTA = 1 page (use the accent color background)
- Maximum ~10 pages for a pitch deck

**Step 3 — Apply the brand**

Check if brief specifies `brand:` overrides. If not, use OLC defaults:

```
--white:       #F9F8F4
--off-white:   #EFEDE7
--card:        #FFFFFF
--accent:      #4F6352   (sage green)
--accent-lt:   #6B8470
--accent-pale: #EDF1EE
--dark:        #0D100C
--text:        #0F1510
--text-dim:    #3D4D40
--text-muted:  #9BA89E
--border:      rgba(79,99,82,0.13)
--font-d:      'Cormorant', Georgia, serif
--font-b:      'DM Sans', system-ui, sans-serif
Google Fonts: Cormorant (ital,wght@0,300;0,400;0,600;1,300;1,400;1,600) + DM Sans (opsz,wght@9..40,300;9..40,400;9..40,500)
```

For a non-OLC brand, substitute the tokens above with the specified values. Choose a complementary serif for display if no display font is given.

**Step 4 — Build the HTML**

Use the A4 page structure from the reference file (`a4-template.md`). Key rules:
- Every page is a `<div class="page">` — `width: 210mm; min-height: 297mm; page-break-after: always`
- Last page: `page-break-after: auto`
- In screen view: body background is `#d0cfc9`, pages shown as elevated cards with shadow and `margin: 20px auto`
- In print view: body background is white, no shadow, no margin between pages
- `@page { size: A4; margin: 0; }` — page margins are controlled by padding inside `.page`, not by `@page`
- Standard page padding: `2.5cm 2.8cm` (top/bottom × left/right)
- All CSS lives in a single `<style>` block in `<head>`. No external CSS files.
- Google Fonts via CDN only. No other external dependencies.
- Logo: use `<img>` with the path from the brief, or the OLC default path if known from context

**Step 5 — Page patterns to use**

*Cover page* — accent-pale background, centered layout, logo top-center, eyebrow label, large serif H1 with italic accent color emphasis, recipient + date in muted text at bottom.

*Section page* — white or off-white background (alternate), label eyebrow, H2 heading, body content (stat cards, feature cards, table, bullet list, or prose depending on content type).

*Stat card row* — 3-column grid, each card has a large serif number, small uppercase label. Highlight one with accent color number.

*Feature cards* — 2-column grid, left accent border (3px solid accent), card tag pill, H3, description, bullet list with em-dash markers.

*Pricing/terms table* — full-width, header row in muted uppercase, rows with bold left column and serif right column for the number/rate.

*Highlight box* — accent-pale background, 1px border, 10px radius. Use for "what's being offered" or "in exchange" content.

*CTA/close page* — accent color background (e.g., `#4F6352`), white text, serif H2 with lighter italic, numbered steps with circle step numbers, footer note in low-opacity text.

**Step 6 — Write the file**

Use the Write tool to save the file at the specified output path. The file must be fully self-contained — open it in a browser and it works with no other files (except referenced images like logos).

**Step 7 — Run the humanizer**

Invoke the `humanizer` skill on all text content in the document. Remove em dashes, AI vocabulary (granular, pivotal, showcase, etc.), -ing phrases, and any promotional or soulless language. Every client-facing document must pass through humanizer before delivery.

**Step 8 — Open and confirm**

Run `open [output-path]` to open the file in the browser. Report: file path + page count.

---

## Output File Structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[Pitch Title]</title>
  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="[fonts url]" rel="stylesheet">
  <style>
    /* All CSS here — tokens, reset, page structure, components, print */
  </style>
</head>
<body>
  <div class="page"> <!-- page 1 --> </div>
  <div class="page"> <!-- page 2 --> </div>
  <!-- ... -->
  <div class="page last-page"> <!-- final page --> </div>
</body>
</html>
```

---

## A4 Page CSS (Required — always include this)

```css
/* A4 page container */
@page {
  size: A4;
  margin: 0;
}

body {
  margin: 0;
  padding: 0;
  background: #d0cfc9;
}

.page {
  width: 210mm;
  min-height: 297mm;
  padding: 2.5cm 2.8cm;
  margin: 20px auto;
  background: var(--white);
  box-sizing: border-box;
  position: relative;
  box-shadow: 0 4px 32px rgba(0,0,0,0.18);
  page-break-after: always;
  overflow: hidden;
}

.last-page {
  page-break-after: auto;
}

@media print {
  body {
    background: white;
  }
  .page {
    margin: 0;
    box-shadow: none;
    width: 210mm;
    min-height: 297mm;
  }
}
```

---

## Notes

- **Content density:** A4 at 96dpi screen is ~794px wide. Keep font sizes 13–16px for body, 28–48px for H1/H2. Don't cram — one idea per page is the rule.
- **Images/logos:** Use relative paths. OLC Method logos are kept locally at `website/OLC_beige_horizontal.jpg` and `website/OLC_beige_vertical.jpg` — always reference these, never `assets/`. The `assets/` folder lives in Google Drive only and is not available locally. The Nirvana logo is at `website/clients/Nirvana.png`. If another client logo is needed, download it from Google Drive first before referencing it in the HTML.
- **No JavaScript:** Pitch decks are static documents. No JS means no risk of broken interactivity in PDF.
- **Printing to PDF:** Browser → File → Print → Destination: Save as PDF → Paper size: A4 → Margins: None. Or use system print dialog with A4 selected.
- **Non-OLC brand:** If brand tokens are provided, substitute all sage green (#4F6352) references with the new accent color. Substitute fonts if specified. Keep the same page structure.
- **Reference file:** See `a4-template.md` for a minimal working A4 page boilerplate to copy from if needed.
