---
created: 2026-07-04
type: system
tags: [n8n, automation, multi-agent, workflows]
status: active
---

# Chapter 13 — Multi-Agent Workflows (n8n)

Three new n8n workflows deployed via CLI import, creating a multi-agent pipeline for RE-Ai.

## Architecture

```
Webhook (lead) ──→ Lead Alert v4 ──→ DB insert + Email notification
                                       │
Schedule (6h) ──→ Lead Follow-up ──→ Stale lead check → Email follow-up
                                       │
Webhook (property) ──→ Property Matching ──→ DB query → Match notification
                                       │
Webhook (schedule) ──→ Appointment Scheduler ──→ Time slots → Email → DB log
```

## Workflow 1: Lead Follow-up
- **Trigger:** Schedule (every 6 hours)
- **Flow:** Query DB for stale leads (no follow-up in 24h) → Build personalized email → Send via SendGrid → Update DB status
- **ID:** `LZ4VJEYzRcISaqPe`
- **Status:** Imported (inactive)

## Workflow 2: Property Matching
- **Trigger:** Webhook `POST /webhook/property`
- **Flow:** Extract property data → Query DB for matching leads → Build notification → Send via SendGrid → Log match
- **ID:** `vsDtCYuPgGvC4wJN`  
- **Status:** Imported (inactive)

## Workflow 3: Appointment Scheduler
- **Trigger:** Webhook `POST /webhook/schedule`
- **Flow:** Parse request → Generate time slots → Send options email → Log to DB
- **ID:** `bWsNL3vtLiGefiBU`
- **Status:** Imported (inactive)

## Deploying Templates from CLI

```bash
docker exec re-ai-n8n n8n import:workflow --input=/path/to/workflow.json
```

Requirements for the JSON:
- Must be wrapped in `[{...}]` array
- Must include `id` field (16-char alphanumeric)
- Must include `versionId` field
- File must be owned by UID 1000 (node user in container)

## Workflow JSON Templates

Stored at `/root/buildabot/data/n8n/templates/`:
- `lead-followup.json`
- `property-matching.json`
- `appointment-scheduler.json`
- `lead-alert-v4.json` (reference copy of active workflow)
