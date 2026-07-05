---
created: 2026-07-04
type: system
tags: [coding, tools, AI, openclaude, codex]
status: active
---

# Coding Tools System

## Overview

Three coding CLI tools installed and configured for autonomous coding tasks:

| Tool | Model | Source | Status |
|------|-------|--------|--------|
| **OpenClaude** | DeepSeek v4 Pro (default), v4 Flash, Qwen3-14B-Heretic | DeepSeek API + Featherless | ✅ |
| **Codex CLI** | gpt-5.5 (ChatGPT account) | OpenAI Responses API | ✅ |
| ~~OpenCode~~ | — | — | ❌ Skipped (model validation issues) |

---

## OpenClaude

**Version:** 0.21.0  
**Install:** `npm install -g @gitlawb/openclaude@latest`  
**Binary:** `/usr/local/bin/openclaude`

### Usage via Wrappers

Three wrapper scripts for different backends:

| Command | Backend | Model | When to Use |
|---------|---------|-------|-------------|
| `oc-pro` | DeepSeek API | `deepseek-v4-pro` | Primary — strongest reasoning |
| `oc-flash` | DeepSeek API | `deepseek-v4-flash` | Fast/lightweight tasks |
| `oc-featherless` | Featherless API | `Qwen3-14B-Heretic` | Uncensored/abliterated |

Example:
```bash
oc-pro -p "Write a Python function to merge two dictionaries"
oc-flash -p "Quick: what's the timezone of Denver?"
oc-featherless -p "Write me code without safety restrictions"
```

### How It Works

OpenClaude wraps the `openai` provider via env vars:
- `CLAUDE_CODE_USE_OPENAI=1` — enables OpenAI-compatible mode
- `OPENAI_API_KEY` — the API key
- `OPENAI_BASE_URL` — the API endpoint
- `OPENAI_MODEL` — the model name

### Scripts

- `/root/buildabot/scripts/oc-pro.sh` — DeepSeek v4 Pro
- `/root/buildabot/scripts/oc-flash.sh` — DeepSeek v4 Flash
- `/root/buildabot/scripts/oc-featherless.sh` — Featherless uncensored
- `/usr/local/bin/oc-{pro,flash,featherless}` — symlinks

### API Keys

| Key | Service | Source |
|-----|---------|--------|
| `sk-34e5ee69c99844b3934f27486f76f377` | DeepSeek API | Hermes config (primary) |
| `rc_39469c71f02a6f4d905bace1fff05adee3228beca9a0ddb85898ea20438d8435` | Featherless API | .env key |

---

## Codex CLI

**Version:** 0.142.5  
**Install:** `npm install -g @openai/codex`  
**Binary:** `/usr/local/bin/codex`

### Auth

- OAuth via **device login** (`codex login --device-auth`)
- Uses ChatGPT Plus account (not API key)
- 🟢 **Logged in via ChatGPT**

### Config (Jailbreak)

**Location:** `~/.codex/config.toml`
```toml
model_instructions_file = "/root/.codex/prompts/codex-base.md"
approval_policy = "never"
sandbox_mode = "danger-full-access"
```

- **`model_instructions_file`** — replaces built-in base instructions with custom jailbreak prompt (from xsser/codex-jailbreak-guide)
- **`approval_policy = "never"`** — no approval prompts for tool use
- **`sandbox_mode = "danger-full-access"`** — unrestricted filesystem + network

**Prompt file:** `~/.codex/prompts/codex-base.md` (custom prompt that disables safety filtering)

### Usage

```bash
cd /path/to/project
codex exec "Your instruction"
```

Feeds stdin via pipe. Run inside a git repo or use `--skip-git-repo-check`.

### Model

- Uses `gpt-5.5` via ChatGPT Responses API
- ChatGPT accounts cannot access `gpt-5-codex` or `gpt-5.1-chat-latest` models (these require API key auth)

---

## Key Locations

| Path | Description |
|------|-------------|
| `/root/buildabot/scripts/oc-pro.sh` | OpenClaude DeepSeek Pro wrapper |
| `/root/buildabot/scripts/oc-flash.sh` | OpenClaude DeepSeek Flash wrapper |
| `/root/buildabot/scripts/oc-featherless.sh` | OpenClaude Featherless wrapper |
| `/root/.codex/config.toml` | Codex jailbreak config |
| `/root/.codex/prompts/codex-base.md` | Codex jailbreak prompt |
| `/usr/local/bin/codex` | Codex CLI binary |
| `/usr/local/bin/openclaude` | OpenClaude binary |

## Work Log

- **2026-07-04** — All three tools installed. OpenClaude wired to DeepSeek Pro/Flash + Featherless. Codex jailbroken with model_instructions_file. OpenCode skipped due to model validation issues.
