---
created: 2026-07-04
type: system
tags: [production, hardening, env, secrets, monitoring]
status: active
---

# Chapter 15 — Production Hardening

## 1. Gateway Restart

Default profile gateway restarted. RE-Ai gateway also restarted. Both running:

```bash
# Check both gateways
ps aux | grep "hermes.*gateway" | grep -v grep
```

## 2. Environment Variables

Secrets centralized to `/root/buildabot/.env`. This file is the **single source of truth** for all API keys.

**Source it:**
```bash
source /root/buildabot/.env
```

**Keys stored:**
| Variable | Purpose |
|----------|---------|
| `DEEPSEEK_API_KEY` | DeepSeek v4 Pro and Flash |
| `FEATHERLESS_API_KEY` | Featherless uncensored models |
| `SENDGRID_API_KEY` | Email sending |
| `FIRECRAWL_API_KEY` | Web scraping |
| `POSTGRES_*` | Database connection |
| `GMAIL_*` | Email reading |
| `LIGHTPANDA_WS` | Browser automation |

**Scripts updated to use env vars:**
- `oc-pro.sh` → `${DEEPSEEK_API_KEY}`
- `oc-flash.sh` → `${DEEPSEEK_API_KEY}`
- `oc-featherless.sh` → `${FEATHERLESS_API_KEY}`

**Known remaining:** n8n workflow templates at `/root/buildabot/data/n8n/templates/` contain hardcoded SendGrid keys. These are snapshot files used for CLI import — the active credentials live in n8n's credential store.

## 3. WTCM Watchdog

**Watch The Clock Mate** — silent infrastructure monitor.

- **Script:** `wtcm-watchdog.py` at `/root/buildabot/scripts/`
- **Cron:** Every 30 minutes via no_agent
- **Pattern:** Silent when healthy, alerts this chat when anything goes down

**Checks:**
| Check | Method |
|-------|--------|
| Postgres | TCP 127.0.0.1:5432 |
| Redis | TCP 127.0.0.1:6379 |
| Qdrant | TCP 127.0.0.1:6333 |
| n8n | TCP 127.0.0.1:5678 |
| Lightpanda | TCP 127.0.0.1:9222 |
| Docker containers | `docker ps` check |
| Gateways | `pgrep -f` process check |
| Disk space | Alarm at <10% free |

## Secrets Audit Summary

The `.env` audit scanned 67 potential secret locations:
- **Critical:** 3 API keys hardcoded in scripts → moved to `.env` ✅
- **Medium:** SendGrid keys in n8n templates → documented as snapshots ✅
- **Low:** Example/placeholder keys in skill docs (ComfyUI, Airtable, Notion) → harmless
