# Workflow: Build a Landing Page from a Screenshot

## Objective
Reproduce a website landing page as a single, self-contained HTML file from a screenshot and/or design tokens provided by the user.

## Required Inputs
- Screenshot of the target page (or detailed description)
- CSS design tokens / color variables (if available)
- Brand name and copy (headlines, body text, CTAs)

## Steps

### 1. Analyze the Design
- Extract color tokens (background, text, accent, muted, borders)
- Identify font family (or closest system/Google Font match)
- Map out all page sections top to bottom
- Note interactive elements (toggles, accordions, sliders, animations)

### 2. Check for Existing Tools
- Look in `tools/` for any reusable scripts (e.g., image downloaders, asset fetchers, HTML validators)
- Only create new tools if a deterministic, reusable step is needed

### 3. Build the HTML File
Execute `tools/build_html.py` with the section config, OR write the file directly if no parameterized generation is needed.

The file should be:
- A single `.html` file with embedded CSS and JS (no external dependencies except fonts/images)
- Fully responsive (breakpoint at 900px minimum)
- Named after the brand: `{brand}.html`
- Saved to the project root

### 4. Sections Checklist
Confirm each section is present and correct:
- [ ] Fixed navigation (logo, links, CTA button)
- [ ] Hero (full-bleed image/video, headline, subtext, CTA, trust signals)
- [ ] Logo/brand marquee (infinite scroll animation)
- [ ] Feature sections (alternating image + text layout)
- [ ] Interactive component (calculator, pricing table, etc.)
- [ ] Social proof band (logos, testimonials)
- [ ] FAQ accordion
- [ ] Footer (links grid, copyright, social icons)

### 5. Verify
- Open in browser: `open {brand}.html`
- Check layout at full width and mobile
- Confirm all interactive elements work (accordion, slider, toggles)

## Expected Output
- `{brand}.html` at project root — self-contained, opens in any browser

## Edge Cases
- **No screenshot, only description**: Ask for key sections, colors, and copy before building
- **Missing images**: Use Unsplash URLs with descriptive search terms; note replacements in comments
- **Brand font unknown**: Default to Inter via Google Fonts; note in file comments
- **Complex animations**: Use CSS-only where possible; JS only for stateful interactions

## Notes
- Images from Unsplash are placeholders — replace with licensed assets for production
- Design tokens from Framer/Figma CSS output map directly to CSS custom properties
