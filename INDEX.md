---
created: 2026-07-03
updated: 2026-07-03
type: meta
---

# 📇 Vault Index

Welcome to the persistent brain. Everything here is shared between you and CHatz.

## Structure

| Folder | Purpose |
|--------|---------|
| `DIARY/` | Session logs + daily notes (Calendar plugin) |
| `CLIENTS/` | Client profiles, contacts, notes |
| `IDEAS/` | Your drop zone — throw notes here, I pick them up |
| `JOBS/` | Projects, tasks, ongoing work |
| `LEADS/` | Opportunities, contacts, deals |
| `HEALTH/` | Mental health check-ins (daily mood, sleep, anxiety) |
| `SYSTEM/` | Conventions, templates, vault config |
| `REFERENCE/` | External docs and research |

## How It Works

- **You** drop a note → I detect it within ~5 min and read it
- **You** create `SYNC.md` in the vault root → I re-read the entire vault
- **You** push to git → I auto-pull
- **I** write session summaries to `DIARY/` after every conversation
- **Daily log** auto-generates at midnight MST
- **Morning briefing** auto-delivers at 10 AM MST

## Quick Links

- [[DIARY/2026-07-03|Today's Diary]]
- [[SYSTEM/_conventions|Note Conventions]]
- [[SYSTEM/_templates|Templates]]
- [[SYSTEM/_health-tracking|Mental Health Tracking]]

---

## 📊 Active Projects

```dataview
TABLE status, priority, deadline
FROM "JOBS"
WHERE status = "active"
SORT priority DESC
```

---

## 📋 Open Tasks

```dataview
TASK
FROM "JOBS" OR "CLIENTS"
WHERE !completed
GROUP BY file.link
```

---

## 🧠 Recent Health Check-Ins

```dataview
TABLE mood, anxiety, energy, sleep_hours
FROM "HEALTH"
SORT file.day DESC
LIMIT 10
```

---

## 📕 Last 7 Days

```dataview
LIST
FROM "DIARY"
WHERE file.name != "INDEX" AND file.day >= (date(today) - dur(7 days))
SORT file.day DESC
```

---

## 🔄 Sync

To trigger a full vault re-read, create a file named `SYNC.md` in the vault root with any content. I'll detect it, consume it, and re-scan everything.