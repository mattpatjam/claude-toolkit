# A4 HTML Pitch Deck — Minimal Boilerplate

Copy this as the skeleton for any new pitch deck. Replace tokens and add pages.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Pitch Title</title>

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant:ital,wght@0,300;0,400;0,600;1,300;1,400;1,600&family=DM+Sans:opsz,wght@9..40,300;9..40,400;9..40,500&display=swap" rel="stylesheet">

  <style>
    /* ─── TOKENS ─────────────────────────────── */
    :root {
      --white:        #F9F8F4;
      --off-white:    #EFEDE7;
      --card:         #FFFFFF;
      --accent:       #4F6352;
      --accent-lt:    #6B8470;
      --accent-pale:  #EDF1EE;
      --dark:         #0D100C;
      --text:         #0F1510;
      --text-dim:     #3D4D40;
      --text-muted:   #9BA89E;
      --border:       rgba(79,99,82,0.13);
      --shadow:       0 2px 16px rgba(15,21,16,0.06);
      --font-d:       'Cormorant', Georgia, serif;
      --font-b:       'DM Sans', system-ui, sans-serif;
    }

    /* ─── RESET ──────────────────────────────── */
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      background: #d0cfc9;
      font-family: var(--font-b);
      font-size: 15px;
      line-height: 1.7;
      -webkit-font-smoothing: antialiased;
    }
    img { max-width: 100%; display: block; }
    a { color: inherit; text-decoration: none; }

    /* ─── A4 PAGE ────────────────────────────── */
    @page { size: A4; margin: 0; }

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
    .last-page { page-break-after: auto; }

    /* ─── PRINT ──────────────────────────────── */
    @media print {
      body { background: white; }
      .page { margin: 0; box-shadow: none; }
    }

    /* ─── TYPOGRAPHY ─────────────────────────── */
    .label {
      font-family: var(--font-b);
      font-size: 10px;
      font-weight: 500;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      color: var(--accent);
      display: block;
      margin-bottom: 0.75rem;
    }
    .label--light { color: rgba(255,255,255,0.55); }
    h1, h2 { font-family: var(--font-d); font-weight: 400; line-height: 1.05; color: var(--dark); }
    h1 { font-size: 52px; }
    h2 { font-size: 36px; }
    h3 { font-family: var(--font-b); font-weight: 500; font-size: 16px; line-height: 1.3; color: var(--dark); }
    p  { color: var(--text-dim); font-size: 14px; line-height: 1.8; }
    em { font-style: italic; color: var(--accent); }

    /* ─── COVER HELPERS ──────────────────────── */
    .cover-center {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      min-height: 297mm;
      text-align: center;
      padding: 2.5cm 2.8cm;
      margin: -2.5cm -2.8cm; /* bleed to page edges */
    }
    .cover-center .logo { height: 72px; width: auto; margin: 0 auto 2.5rem; }
    .cover-center h1 { margin-bottom: 1rem; }
    .cover-center .sub { font-size: 13px; color: var(--text-muted); margin-top: 0.5rem; }

    .badge {
      display: inline-flex; align-items: center; gap: 0.5rem;
      background: rgba(79,99,82,0.1);
      border: 1px solid var(--border);
      border-radius: 20px;
      padding: 0.3rem 0.9rem;
      margin-bottom: 1.5rem;
    }
    .badge span { font-size: 10px; font-weight: 500; letter-spacing: 0.14em; text-transform: uppercase; color: var(--accent); }
    .badge-dot { width: 5px; height: 5px; border-radius: 50%; background: var(--accent); flex-shrink: 0; }

    /* ─── STAT CARDS ─────────────────────────── */
    .stats-row { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; margin: 1.5rem 0; }
    .stat-card {
      background: var(--card); border: 1px solid var(--border);
      border-radius: 8px; padding: 1.5rem 1.25rem; text-align: center;
      box-shadow: var(--shadow);
    }
    .stat-card .num {
      font-family: var(--font-d); font-size: 52px; font-weight: 300;
      color: var(--dark); line-height: 1; display: block; margin-bottom: 0.3rem;
    }
    .stat-card.hi .num { color: var(--accent); }
    .stat-card .lbl { font-size: 10px; font-weight: 500; letter-spacing: 0.12em; text-transform: uppercase; color: var(--text-muted); }

    /* ─── FEATURE CARDS ──────────────────────── */
    .two-col { display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-top: 1.5rem; }
    .card {
      background: var(--card); border: 1px solid var(--border);
      border-radius: 10px; padding: 1.75rem 1.5rem;
      box-shadow: var(--shadow); position: relative; overflow: hidden;
    }
    .card::before {
      content: ''; position: absolute; top: 0; left: 0;
      width: 3px; height: 100%; background: var(--accent);
    }
    .card-tag {
      display: inline-block; background: var(--accent-pale); color: var(--accent);
      font-size: 9px; font-weight: 500; letter-spacing: 0.14em; text-transform: uppercase;
      border-radius: 3px; padding: 0.2rem 0.5rem; margin-bottom: 1rem;
    }
    .card h3 { font-size: 15px; margin-bottom: 0.5rem; }
    .card p  { font-size: 13px; margin-bottom: 1rem; }
    .card ul { list-style: none; display: flex; flex-direction: column; gap: 0.5rem; }
    .card ul li { display: flex; align-items: flex-start; gap: 0.5rem; font-size: 13px; color: var(--text-dim); line-height: 1.5; }
    .card ul li::before { content: '—'; color: var(--accent); font-weight: 500; flex-shrink: 0; }

    /* ─── TABLE ──────────────────────────────── */
    .price-table { width: 100%; border-collapse: collapse; font-size: 13px; margin: 1.25rem 0; }
    .price-table th { text-align: left; font-size: 9px; font-weight: 500; letter-spacing: 0.16em; text-transform: uppercase; color: var(--text-muted); padding: 0 0 0.6rem; border-bottom: 1px solid var(--border); }
    .price-table th:last-child { text-align: right; }
    .price-table td { padding: 0.9rem 0; border-bottom: 1px solid var(--border); color: var(--text-dim); }
    .price-table td:first-child { color: var(--dark); font-weight: 500; font-size: 14px; }
    .price-table td:last-child { text-align: right; font-family: var(--font-d); font-size: 22px; color: var(--dark); }

    /* ─── HIGHLIGHT BOX ──────────────────────── */
    .hi-box {
      background: var(--accent-pale); border: 1px solid var(--border);
      border-radius: 8px; padding: 1.5rem 1.75rem; margin-top: 1.25rem;
    }
    .hi-box .hi-label { font-size: 9px; font-weight: 500; letter-spacing: 0.14em; text-transform: uppercase; color: var(--accent); display: block; margin-bottom: 0.75rem; }
    .hi-box ul { list-style: none; display: flex; flex-direction: column; gap: 0.6rem; }
    .hi-box ul li { display: flex; align-items: flex-start; gap: 0.6rem; font-size: 14px; color: var(--text-dim); line-height: 1.5; }
    .hi-box ul li::before { content: ''; width: 5px; height: 5px; border-radius: 50%; background: var(--accent); flex-shrink: 0; margin-top: 7px; }

    /* ─── CTA PAGE ───────────────────────────── */
    .page.cta { background: var(--accent); }
    .page.cta .label { color: rgba(255,255,255,0.55); }
    .page.cta h2 { color: #F9F8F4; font-size: 42px; margin-bottom: 2rem; }
    .page.cta em { color: rgba(249,248,244,0.6); }
    .steps { display: flex; flex-direction: column; gap: 1rem; margin-bottom: 2rem; }
    .step { display: flex; align-items: flex-start; gap: 1rem; }
    .step-num { width: 28px; height: 28px; border-radius: 50%; background: rgba(249,248,244,0.15); border: 1px solid rgba(249,248,244,0.25); display: flex; align-items: center; justify-content: center; font-family: var(--font-d); font-size: 15px; color: #F9F8F4; flex-shrink: 0; margin-top: 2px; }
    .step-text { color: rgba(249,248,244,0.8); font-size: 14px; line-height: 1.6; }
    .step-text strong { color: #F9F8F4; font-weight: 500; }
    .cta-note { font-size: 12px; color: rgba(249,248,244,0.45); border-top: 1px solid rgba(249,248,244,0.15); padding-top: 1.25rem; line-height: 1.6; }

    /* ─── PAGE FOOTER ────────────────────────── */
    .page-footer {
      position: absolute; bottom: 1.5cm; left: 2.8cm; right: 2.8cm;
      display: flex; justify-content: space-between; align-items: center;
      border-top: 1px solid var(--border); padding-top: 0.6rem;
    }
    .page-footer .pf-logo { height: 28px; width: auto; }
    .page-footer .pf-meta { font-size: 10px; color: var(--text-muted); }
  </style>
</head>
<body>

<!-- PAGE 1 — COVER -->
<div class="page" style="background: var(--accent-pale); padding: 0;">
  <div class="cover-center">
    <img src="[logo-path]" alt="Logo" class="logo">
    <div class="badge"><span class="badge-dot"></span><span>A partnership proposal</span></div>
    <h1>[Pitch Title with <em>emphasis</em>]</h1>
    <p class="sub">Prepared for [Recipient] &nbsp;·&nbsp; [Month Year]</p>
  </div>
</div>

<!-- PAGE 2 — SECTION EXAMPLE (white) -->
<div class="page">
  <span class="label">Section label</span>
  <h2>[Section heading with <em>italic accent</em>]</h2>
  <p>[Opening paragraph]</p>

  <div class="stats-row">
    <div class="stat-card"><span class="num">32</span><span class="lbl">Total units</span></div>
    <div class="stat-card"><span class="num">18</span><span class="lbl">Sold</span></div>
    <div class="stat-card hi"><span class="num">14</span><span class="lbl">Remaining</span></div>
  </div>

  <div class="page-footer">
    <img src="[logo-path]" alt="Logo" class="pf-logo">
    <span class="pf-meta">Confidential · [Date]</span>
  </div>
</div>

<!-- PAGE 3 — TWO CARDS (off-white) -->
<div class="page" style="background: var(--off-white);">
  <span class="label">Section label</span>
  <h2>[Heading]</h2>

  <div class="two-col">
    <div class="card">
      <span class="card-tag">Card One</span>
      <h3>Card title</h3>
      <p>Card description.</p>
      <ul>
        <li>Point one</li>
        <li>Point two</li>
      </ul>
    </div>
    <div class="card">
      <span class="card-tag">Card Two</span>
      <h3>Card title</h3>
      <p>Card description.</p>
      <ul>
        <li>Point one</li>
        <li>Point two</li>
      </ul>
    </div>
  </div>

  <div class="page-footer">
    <img src="[logo-path]" alt="Logo" class="pf-logo">
    <span class="pf-meta">Confidential · [Date]</span>
  </div>
</div>

<!-- PAGE 4 — CTA (accent bg, last page) -->
<div class="page cta last-page">
  <span class="label label--light">Next step</span>
  <h2>Two things.<br><em>That's it.</em></h2>
  <div class="steps">
    <div class="step">
      <div class="step-num">1</div>
      <div class="step-text"><strong>Action one.</strong> Description of what this means.</div>
    </div>
    <div class="step">
      <div class="step-num">2</div>
      <div class="step-text"><strong>Action two.</strong> Description of what this means.</div>
    </div>
  </div>
  <p class="cta-note">Footer note or clarification.</p>
</div>

</body>
</html>
```
