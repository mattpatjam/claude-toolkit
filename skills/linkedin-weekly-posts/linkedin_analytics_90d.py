#!/usr/bin/env python3
"""
Scrapes LinkedIn Creator Analytics top performing posts, switched to the 90-day window.
Outputs JSON to stdout. Uses li_at session cookie from .env.
Monthly companion to linkedin_analytics.py (which only reads the default 7-day window).

Usage:
    /Users/matt/Desktop/Claude/.venv/bin/python3 .claude/skills/linkedin-weekly-posts/linkedin_analytics_90d.py
"""
import json
import os
import sys
from pathlib import Path

env_path = Path(__file__).parent.parent.parent.parent / ".env"
if env_path.exists():
    for line in env_path.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, val = line.split("=", 1)
            os.environ.setdefault(key.strip(), val.strip())

LI_AT = os.environ.get("LI_AT", "")
if not LI_AT:
    print(json.dumps({"error": "LI_AT not set in .env"}))
    sys.exit(1)

from scrapling.fetchers import DynamicFetcher

_data = {}


def _setup(page):
    page.context.add_cookies([{
        "name": "li_at",
        "value": LI_AT,
        "domain": ".linkedin.com",
        "path": "/",
        "secure": True,
        "httpOnly": True,
    }])


def _extract(page):
    try:
        # Open the time-range dropdown (defaults to "7 days") and switch to 90 days.
        page.get_by_text("7 days", exact=True).first.click(timeout=10000)
        page.wait_for_timeout(1200)

        # Debug: dump whatever menu/listbox appeared so we can see the real option text.
        menu_dump = page.evaluate("""() => {
            const candidates = Array.from(document.querySelectorAll(
                '[role="listbox"], [role="menu"], ul, [class*="dropdown"], [class*="menu"]'
            ));
            return candidates
                .filter(el => el.innerText && el.innerText.trim().length > 0 && el.innerText.length < 500)
                .map(el => el.innerText.trim())
                .slice(0, 15);
        }""")
        _data["menu_dump"] = menu_dump

        # LinkedIn's menu options are usually phrased "Past 90 days".
        clicked = False
        for label in ["Past 90 days", "90 days"]:
            try:
                page.get_by_text(label, exact=False).first.click(timeout=3000)
                clicked = True
                break
            except Exception:
                continue

        _data["clicked_90d_option"] = clicked
        if not clicked:
            _data["error"] = "Could not find a 90-day option in the dropdown menu"
            return

        page.wait_for_timeout(4000)
        try:
            page.wait_for_load_state("networkidle", timeout=6000)
        except Exception:
            pass

        result = page.evaluate("""() => {
            const loginBtn = document.querySelector('a[href*="/login"], button[data-tracking-control-name*="login"]');
            const isLoggedIn = !loginBtn && document.querySelector('nav, [class*="global-nav"]');

            const allText = document.body.innerText;
            const topPostsIdx = allText.indexOf('Top performing posts');
            const topPostsSection = topPostsIdx >= 0
                ? allText.substring(topPostsIdx, topPostsIdx + 6000)
                : '';

            const rangeLabelMatch = allText.match(/(7 days|28 days|90 days|Past \\d+ days)/);

            return {
                isLoggedIn: !!isLoggedIn,
                url: window.location.href,
                rangeLabel: rangeLabelMatch ? rangeLabelMatch[0] : null,
                topPostsSection: topPostsSection,
            };
        }""")
        _data["result"] = result
    except Exception as e:
        _data["error"] = str(e)


DynamicFetcher.fetch(
    "https://www.linkedin.com/analytics/creator/content/",
    page_setup=_setup,
    page_action=_extract,
    network_idle=True,
    wait=4000,
    headless=True,
)

if "error" in _data:
    print(json.dumps({
        "error": _data["error"],
        "menu_dump": _data.get("menu_dump"),
        "clicked_90d_option": _data.get("clicked_90d_option"),
    }))
    sys.exit(1)

r = _data.get("result", {})

if not r.get("isLoggedIn") or "login" in r.get("url", "").lower():
    print(json.dumps({"error": "Not authenticated — li_at cookie may have expired"}))
    sys.exit(1)

import re

posts = []
section = r.get("topPostsSection", "")
if section:
    header_pattern = re.compile(
        r'(?:^|\n)([\d,.]+K?) impressions\s*[•·]\s*([\d,.]+) engagements?',
        re.MULTILINE
    )
    matches = list(header_pattern.finditer(section))
    for i, m in enumerate(matches):
        impressions_raw = m.group(1)
        engagements_raw = m.group(2)

        if impressions_raw.upper().endswith("K"):
            impressions = int(float(impressions_raw[:-1]) * 1000)
        else:
            impressions = int(impressions_raw.replace(",", ""))

        engagements = int(engagements_raw.replace(",", ""))

        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(section)
        block_text = section[start:end]

        text_match = re.search(r'Feed post\s*\n\n(.+)', block_text, re.DOTALL)
        post_text = text_match.group(1).strip() if text_match else ""
        hook = post_text.split("\n")[0].strip() if post_text else ""

        posts.append({
            "impressions": impressions,
            "engagements": engagements,
            "hook": hook,
            "text_preview": post_text[:300],
        })

print(json.dumps({
    "window": r.get("rangeLabel", "90 days (unconfirmed)"),
    "posts": posts,
    "menu_dump": _data.get("menu_dump"),
    "clicked_90d_option": _data.get("clicked_90d_option"),
}, indent=2))
