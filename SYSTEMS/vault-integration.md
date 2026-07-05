---
created: 2026-07-04
type: system
tags: [vault, integration, RE-Ai, memory]
status: active
---

# Vault Integration — RE-Ai's Human-Readable Memory

The Obsidian vault at `/root/obsidian-vault` is RE-Ai's transparent memory layer. Every lead, property, and interaction is stored as structured markdown notes the user can browse.

## Directory Structure

```
obsidian-vault/
├── LEADS/         # Lead profiles → contact info, property interest, status
├── DAILY/         # Daily summaries → what RE-Ai did today
├── KNOWLEDGE/     # Property info, market data, research findings
├── INTERACTIONS/  # Conversation summaries with leads
├── CLIENTS/       # Agent/client onboarding info
├── SYSTEMS/       # Technical docs (how RE-Ai works, coding tools, pentest)
├── Calendar/      # Events, appointments, showings
├── IDEAS/         # Architecture and planning docs
├── JOBS/          # Job descriptions for RE-Ai roles
└── KEYS/          # API key documentation (redacted)
```

## The Integration Script

```bash
# Create a lead note
python3 ~/buildabot/scripts/vault.py lead-create "Name" "email" "phone" "source" "status" "interest" "summary"

# Find leads by name/email/content
python3 ~/buildabot/scripts/vault.py lead-find "query"

# Search everything
python3 ~/buildabot/scripts/vault.py search "query"

# Get full context before a conversation
python3 ~/buildabot/scripts/vault.py context "lead-name"

# Save market research
python3 ~/buildabot/scripts/vault.py knowledge-save "topic" "summary" "details" "source"

# Write daily summary
python3 ~/buildabot/scripts/vault.py daily-write "interactions" "leads" "actions" "followups" "notes"

# Vault stats
python3 ~/buildabot/scripts/vault.py stats
```

## What Changed

1. **MCP filesystem server** now includes `/root/obsidian-vault` (requires gateway restart)
2. **Templates created** in `LEADS/`, `DAILY/`, `KNOWLEDGE/`, `INTERACTIONS/`
3. **`vault.py` script** at `~/buildabot/scripts/vault.py`
4. **SOUL.md updated** with vault workflows and when-to-use-what guidance
