#!/usr/bin/env python3
"""
Scrapes LinkedIn Creator Analytics top performing posts (7-day window).
Outputs JSON to stdout. Uses li_at session cookie from .env.

Usage:
    /Users/matt/Desktop/Claude/.venv/bin/python3 .claude/skills/linkedin-weekly-posts/linkedin_analytics.py
"""
import json
import os
import sys
from pathlib import Path

# Load .env from project root
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
        result = page.evaluate("""() => {
            // Check for login wall
            const loginBtn = document.querySelector('a[href*="/login"], button[data-tracking-control-name*="login"]');
            const isLoggedIn = !loginBtn && document.querySelector('nav, [class*="global-nav"]');

            // Get the main content text for parsing
            const main = document.querySelector('main') || document.body;
            const fullText = main ? main.innerText : document.body.innerText;

            // Try to find the "Top performing posts" section
            // LinkedIn renders this as a list of post cards with metrics
            const allText = document.body.innerText;
            const topPostsIdx = allText.indexOf('Top performing posts');
            const topPostsSection = topPostsIdx >= 0
                ? allText.substring(topPostsIdx, topPostsIdx + 4000)
                : '';

            // Try structured extraction: find elements with impression counts
            const metricEls = Array.from(document.querySelectorAll('[class*="metric"], [class*="insight"], [class*="analytics"]'));

            return {
                isLoggedIn: !!isLoggedIn,
                url: window.location.href,
                topPostsSection: topPostsSection,
                fullTextPreview: allText.substring(0, 6000),
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
    print(json.dumps({"error": _data["error"]}))
    sys.exit(1)

r = _data.get("result", {})

# Auth check
if not r.get("isLoggedIn") or "login" in r.get("url", "").lower():
    print(json.dumps({"error": "Not authenticated — li_at cookie may have expired"}))
    sys.exit(1)

# Parse top posts section into structured data
# Format: "[X]K? impressions • [Y] engagements\n\nView analytics\n\nFeed post\n\n[text...]"
import re

posts = []
section = r.get("topPostsSection", "")
if section:
    # Find all post headers (metric line), then slice out blocks between them
    header_pattern = re.compile(
        r'(?:^|\n)([\d,.]+K?) impressions\s*[•·]\s*([\d,.]+) engagements?',
        re.MULTILINE
    )
    matches = list(header_pattern.finditer(section))
    for i, m in enumerate(matches):
        impressions_raw = m.group(1)
        engagements_raw = m.group(2)

        # Normalize impressions: "2K" -> 2000, "389" -> 389
        if impressions_raw.upper().endswith("K"):
            impressions = int(float(impressions_raw[:-1]) * 1000)
        else:
            impressions = int(impressions_raw.replace(",", ""))

        engagements = int(engagements_raw.replace(",", ""))

        # Slice block content from this match to the next (or end)
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(section)
        block_text = section[start:end]

        # Extract post text (after "Feed post\n\n")
        text_match = re.search(r'Feed post\s*\n\n(.+)', block_text, re.DOTALL)
        post_text = text_match.group(1).strip() if text_match else ""

        # Hook = first line
        hook = post_text.split("\n")[0].strip() if post_text else ""

        posts.append({
            "impressions": impressions,
            "engagements": engagements,
            "hook": hook,
            "text_preview": post_text[:300],
        })

print(json.dumps({
    "window": "7 days",
    "posts": posts,
}, indent=2))
