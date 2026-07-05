---
created: 2026-07-04
updated: 2026-07-04
type: job
tags: [build, hermes, buildabot, demo-agent]
status: in-progress
priority: high
---

# 🏗️ buildabot.ca — Demo Agent Build

**Status:** RE-Ai LIVE on Telegram @REAi_bot

## Completed ✅

- [x] Docker 29.6.1 + Docker Compose v5.3.0
- [x] RE-AI Hermes profile (`re-ai-demo`)
- [x] DeepSeek v4-Flash (working)
- [x] SOUL.md identity: RE-Ai ("REAH") — Real Estate Artificial Intelligence
- [x] Postgres, Redis, Qdrant, n8n
- [x] Qdrant vector memory (4 collections)
- [x] Obsidian vault access (LEADS/, PROPERTIES/)
- [x] Landing page (port 8080)
- [x] Telegram bot wired
- [x] Memory helper scripts (memory.py, vault.py)
- [x] MCP servers: re-ai-fs (filesystem) + re-ai-pg (PostgreSQL)

## Next Up (Chapter Order)

1. ✅ Ch6 — Memory (Qdrant + Obsidian)
2. ✅ Ch7 — MCP (filesystem + PostgreSQL servers)
3. [ ] Ch8 — Email + Calendar integrations
4. [ ] Ch10 — n8n automation workflows
5. [ ] Ch16-21 — RE-AI lead pipeline, SMS, sales

## Quick Reference

- **RE-Ai Telegram:** @REAi_bot (handle: @n8n_pers0nass1sstant_bot)
- **Profile:** `hermes chat --profile re-ai-demo`
- **Config:** `~/.hermes/profiles/re-ai-demo/config.yaml`
- **Landing:** `http://localhost:8080`
- **n8n:** `http://localhost:5678`
- **Qdrant:** `localhost:6333`
- **Postgres:** `localhost:5432` (user: re_ai, pass: re_ai_local_dev, db: re_ai)
- **MCP servers:** re-ai-fs (filesystem) + re-ai-pg (postgresql)
