---
created: 2026-07-04
type: client
tags: [client, business, buildabot]
status: active
name: buildabot.ca
contact: Dysthemix
---

# buildabot.ca

**Type:** Your own business / new venture
**Status:** Active — RE-Ai demo live
**RE-Ai branding:** Name: RE-Ai (pronounced "REAH") — Real Estate Artificial Intelligence

## Products
1. Custom AI agents for real estate agents (live demo: @REAi_bot → @n8n_pers0nass1sstant_bot)
2. Build-to-order bots (general)

## Progress
- ✅ Memory: Qdrant (4 collections) + Obsidian vault
- ✅ Vault integration (Ch 7 — vault.py script created, LEADS/DAILY/KNOWLEDGE/INTERACTIONS templates, SOUL.md updated with vault workflows)
- ✅ MCP: filesystem server (vault + buildabot) + PostgreSQL server
|- ✅ Email + Calendar tools (Ch 8 — SendGrid send ✅, Gmail inbox ✅, Calendar script written ⚠️ needs OAuth consent, nagging reminder system active every 1h)
- ✅ n8n automation (Ch 10 — Lead Alert v4 working, DB pipeline active)
- ✅ Multi-Agent workflows (Ch 13 — Lead Follow-up, Property Matching, Appointment Scheduler deployed via CLI)
- ✅ Production Hardening (Ch 15 — Gateway restart, .env centralized, secrets cleaned, WTCM watchdog every 30m)
|- ✅ Browser automation (Ch 9 — Triple-layer scraper: Firecrawl + Lightpanda + Playwright, hard mode for cookie walls)
- [x] Ch 11 — Coding Tools (OpenClaude + Codex CLI, see [[../../SYSTEMS/coding-tools|coding-tools]])
- [ ] Ch 12 — Control Center (Observability)
- [x] Ch 13 — Multi-Agent Intelligence
- [ ] Ch 14 — Goals & Self-Improvement
- [x] Ch 15 — Production Hardening
- [ ] Ch 16-21 — RE-AI Pivot (MVP, Twilio, Sales, GTM)
**Domain:** buildabot.ca

## What It Is

A new AI services business. The demo agent (per `[[../../JOBS/buildabot-demo-agent|buildabot-demo-agent]]`) will be the public-facing demonstration of what's on offer.

## Service Offering (TBD)

Pending decision in buildabot-demo-agent plan.

## Tech Stack

Following the architecture from `IDEAS/hermes_agent/`:
- Hermes Agent as primary reasoning
- OpenRouter (or other) for LLM API
- Docker for service isolation
- Qdrant for vector memory
- n8n for automation
- Obsidian vault for human-readable memory
- MCP for tool standard

## Notes

- 

## Work Log

- **2026-07-04** — Initial planning, env scan, scoping questions drafted
## Email Status
- ✅ Send via SendGrid API (HTTPS port 443)
- ✅ Read inbox via Gmail Atom Feed (HTTPS port 443)
- ✅ Script: `/root/buildabot/scripts/re-ai-email.py`
- ⚠️ Search limited (Atom feed search endpoint not reliable)
- ~~SMTP/IMAP ports 587/993 blocked by provider~~ (worked around)

## n8n Status (Chapter 10)
- ✅ n8n running on port 5678 (Docker)
- ✅ Owner account: REAiPersonalAssistsnt@gmail.com
- ✅ SendGrid credential (ID: Mv0giXs7xwoOheiV) — also hardcoded in Code node as fallback
- ✅ Postgres credential (ID: suVGg6XFIKOjad2M) — host: `172.18.0.3:5432` (Docker internal), no SSL
- ✅ **Lead Alert v4** workflow — active, fully working
- ✅ Pipeline: Webhook (`POST /webhook/lead`) → Code node (flatten) → **Postgres INSERT** + **SendGrid email** (parallel)
- ✅ DB tables: `leads`, `properties`, `lead_properties`, `lead_activities`
- ✅ `/root/buildabot/data/n8n/pg-credential.json` — Postgres credential export
- ✅ `/root/buildabot/scripts/cleanup-n8n.py` — cleans archived workflows

## Dev Notes
- n8n Code node: use `this.helpers.httpRequest(options)` for API calls (not `fetch`)
- Postgres: IPv4 `172.18.0.3` (Docker IP) — IPv6 `::1` refused; `127.0.0.1` points to n8n container
- No SSL on Postgres — credential must omit `ssl` field entirely
- Webhook → Code node for flattening → Postgres auto-map works best
- Fan-out connections: both nodes in same `main[0]` array

## Remaining To-Do
- ❌ Restart main Hermes gateway (SOUL.md changes for CHatz pending)
- ❌ Provider still blocking ports 587/993 (worked around)
- [ ] Build more n8n workflows (follow-ups, scheduling, DB logging)
- [ ] Database schema for leads/properties
- [ ] Land buildabot.ca domain
