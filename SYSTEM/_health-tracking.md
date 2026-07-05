---
created: 2026-07-03
type: system
tags: [health, system]
---

# 🧠 Mental Health Tracking

## Location
Daily check-ins go in `HEALTH/YYYY-MM-DD.md`

## Structure
Every check-in follows this format:

```markdown
---
created: YYYY-MM-DD
type: health
tags: [health, checkin]
mood: 1-10
sleep_hours: X
energy: 1-10
anxiety: 1-10
social_interaction: yes/no
---

# YYYY-MM-DD — Daily Check-In

## How I'm feeling
[Free text]

## What's on my mind
[Anything weighing, stressors, wins]

## Sleep
[X] hours — [quality notes]

## What helped today
[Things that made a difference]

## What didn't
[Triggers, setbacks]

## Tomorrow's intention
[One thing to focus on]
```

## Fields
- `mood`: 1-10 (1 = worst, 10 = best)
- `sleep_hours`: approximate hours
- `energy`: 1-10
- `anxiety`: 1-10
- `social_interaction`: yes/no/mixed

## Built for Analysis
The YAML frontmatter is structured so Dataview can query across months:
```dataview
TABLE mood, anxiety, energy, sleep_hours, social_interaction
FROM "HEALTH"
SORT file.day DESC
```

This lets you spot correlations — low sleep + high anxiety, good energy + social interaction, etc.