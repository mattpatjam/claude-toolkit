---
name: schedule-to-calendar
description: Use when Matthieu sends a new monthly planning PDF and needs Matt's office shifts uploaded to the "Matt BE" calendar in Apple Calendar (syncs to Google Calendar automatically).
argument-hint: "[attach or paste the monthly planning PDF content here]"
---

# Schedule to Calendar

Parse a monthly planning PDF and add Matt's office shifts to Apple Calendar via AppleScript.

## What you need

- The monthly planning PDF content (pasted or attached as `$ARGUMENTS`)
- Access to run: `osascript "/Users/matt/Desktop/Claude/My assistant/Bali Exception/add_matt_schedule.scpt"`

## Step 1 — Parse the schedule

Read the PDF and find every row where "Matt" appears. For each shift, extract:

- **Date** (day + month + year)
- **Time slot:**
  - 9h30–11h30
  - 11h30–14h30
  - 14h30–17h30
- **Co-worker** (always 2 people per shift — note the other person's name)

Also read the holiday section at the bottom of the PDF. Note all dates that fall within Matt's holiday periods. Skip any shifts that land on a holiday date.

## Step 2 — Build the AppleScript

Update (or create) the script at:

```
/Users/matt/Desktop/Claude/My assistant/Bali Exception/add_matt_schedule.scpt
```

Use this structure:

```applescript
-- Helper to build a date object
on makeDate(y, m, d, hours, mins)
    set theDate to current date
    set year of theDate to y
    set month of theDate to m
    set day of theDate to d
    set hours of theDate to hours
    set minutes of theDate to mins
    set seconds of theDate to 0
    return theDate
end makeDate

-- Add each shift as a calendar event
tell application "Calendar"
    tell calendar "Matt BE"

        -- Example entry (repeat for each shift):
        set startDate to makeDate(2026, 4, 22, 9, 30)
        set endDate to makeDate(2026, 4, 22, 11, 30)
        make new event with properties {summary:"Office Shift with [Name]", start date:startDate, end date:endDate}

    end tell
end tell
```

**Event title format:** `Office Shift with [Name]`  
**Calendar:** `Matt BE`  
**Google account behind this calendar:** matt.jammers.be@gmail.com  
**No Google Calendar auth needed** — events go into Apple Calendar directly and sync automatically.

## Step 3 — Run the script

```
osascript "/Users/matt/Desktop/Claude/My assistant/Bali Exception/add_matt_schedule.scpt"
```

Confirm it ran without errors. If Calendar prompts for permissions, grant them and re-run.

## Step 4 — Confirm

List the shifts that were added (date, time, co-worker) so Matthieu can verify at a glance.

## Edge cases

- If a shift falls on a holiday date → skip it, flag it in the confirmation output
- If the PDF is unclear on a date or name → ask before writing the script
- If the script errors → read the full error, fix, and rerun (no paid API calls involved, safe to retry freely)
