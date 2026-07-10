# Final System Report — 2026-07-05

## Overview

Complete security hardening, infrastructure lockdown, and feature upgrades. All services secured behind localhost binding with Cloudflare tunnel as the sole public ingress.

## Tunnel

- **Current URL:** `https://shanghai-september-chest-albuquerque.trycloudflare.com`
- **⚠️ IMPORTANT:** This URL changes every time the server reboots (Cloudflare quick tunnel limitation)
- **Routes:**
  - `/` → Production website (Vite/React build)
  - `/uncensored` → Uncensored LLM chat client (v2)
  - `/api/*` → Chat API (RE-Ai censored + uncensored)
  - `/webhook/*` → n8n webhooks
  - `/rest/*`, `/static/*` → n8n backend

## Security Posture

| Layer | Status | Detail |
|-------|--------|--------|
| **UFW firewall** | ✅ Active | SSH (22), SMTP (587), IMAPS (993) only |
| **fail2ban** | ✅ Active | 26 total failed SSH attempts, 2 banned IPs so far |
| **Docker ports** | ✅ Locked | All 4 containers bound to 127.0.0.1 |
| **Caddy** | ✅ Locked | `bind 127.0.0.1:8080` — tunnel-only |
| **Chat proxy** | ✅ Locked | `bind 127.0.0.1:8081` — Caddy proxied |
| **Docker daemon** | ✅ Hardened | no-new-privileges, log max-size 10m, live-restore |
| **Unattended upgrades** | ✅ Active | Security patches only, auto-install |
| **SSH** | ✅ Hardened | Root key-only, 3 max auth tries, 300s timeout, fail2ban |
| **Root login** | ✅ Locked | `PermitRootLogin prohibit-password` |
| **Auto-start** | ✅ | cloudflared-tunnel, fail2ban, unattended-upgrades all enabled on boot |

## Containers (all healthy)

| Service | Image | Port | Purpose |
|---------|-------|------|---------|
| postgres | postgres:16 | 5432 | Main database |
| redis | redis:7-alpine | 6379 | Cache/queue |
| qdrant | qdrant/qdrant | 6333-6334 | Vector embeddings |
| n8n | n8nio/n8n | 5678 | Automation workflows |

## Systemd Services (auto-start on boot)

| Service | Status | Purpose |
|---------|--------|---------|
| caddy | ✅ active | Reverse proxy |
| cloudflared-tunnel | ✅ active (enabled) | Cloudflare ingress |
| fail2ban | ✅ active (enabled) | SSH brute-force protection |
| unattended-upgrades | ✅ active (enabled) | Security auto-updates |
| pixel-wake | ⚡ oneshot (enabled) | Pings Pixel 7 on boot |

## Laptop (parrot-1 — 100.102.204.115)

| Component | Status |
|-----------|--------|
| **Disk** | 78% (370G used, 106G free) |
| **llama-server** | ✅ systemd auto-start, enabled |
| **Model loaded** | `Qwen3.5-9B-Uncensored-HauhauCS-Aggressive-Q4_K_M.gguf` on :9000 |
| **Ollama** | ❌ Dead and disabled |
| **Tailscale** | ✅ Connected — 6 devices on tailnet |
| **TorBot** | Available for OSINT/onion routing |
| **Other models available** | Darkidol-27B, XORTRON-27B, Poe-8B, Gemma-4-heretic (via llama-server restart) |

## Uncensored Chat Client v2

**URL:** `/uncensored`

| Feature | How |
|---------|------|
| Streaming (SSE) | Replies word-by-word via fetch + ReadableStream |
| Markdown rendering | marked.js library, tables, lists, headings |
| Syntax highlighting | highlight.js + GitHub Dark theme |
| Copy code button | Every `<pre><code>` block gets a clipboard button |
| Voice input | 🎤 mic button → Web SpeechRecognition (Chrome/Android) |
| Conversation persistence | localStorage — survives refresh |
| Temperature slider | 0.0–1.5, per-session adjustable |
| System prompt presets | Saved to `/root/buildabot/data/uncensored-presets.json` |
| Auto-log | Every exchange → `UNSENSORED/YYYY-MM-DD.md` |
| Code extraction | Code blocks auto-extracted to `UNSENSORED/code/` |
| Model info | Displays current model name from llama.cpp |

**Default presets:** Unfiltered Assistant, Expert Programmer, DAN (Do Anything Now), Creative Writer

## Cron Jobs

| Name | Schedule | Type | Purpose |
|------|----------|------|---------|
| vault-watcher | 0 6,18 * * * UTC | no_agent | Git auto-sync vault |
| nightly-logs | 0 6 * * * UTC | LLM | System log summary |
| mental-health-check | 0 16,18,0,4 * * * UTC | LLM | Periodic well-being |
| reminder-nagger | hourly | LLM | Nag about events |
| WTCM Watchdog | every 30m | no_agent | Service health check |
| pixel-watchdog | every 30m | no_agent | Pixel 7 online check |
| daily-log | — | PAUSED | — |
| morning-briefing | — | PAUSED | — |

## Vault Structure

```
OBSIDIAN_VAULT/
├── SYSTEMS/              # System reports & audit docs
│   ├── security-report-2026-07-05.md
│   └── final-system-report-2026-07-05.md
├── UNSENSORED/           # Uncensored LLM conversation logs
│   ├── 2026-07-05.md
│   └── code/             # Extracted code blocks
├── CRON/                 # Cron job outputs
└── ... (existing notes)
```

## Key Commands

```bash
# Check tunnel URL
sudo journalctl -u cloudflared-tunnel --no-pager | grep trycloudflare

# Restart tunnel (gets new URL)
sudo systemctl restart cloudflared-tunnel

# Check fail2ban status
sudo fail2ban-client status sshd

# Query uncensored model directly (for CHatz)
python3 /root/buildabot/scripts/ask-uncensored.py "your prompt"

# Check laptop llama-server
tailscale ssh dysthemix@parrot-1 "systemctl status llama-server"

# Rebuild site
cd /root/buildabot && npm run build && sudo cp -r site/dist/* /var/www/buildabot/

# Deploy n8n workflow
docker exec -i re-ai-n8n n8n import:workflow --input=- < workflow.json

# Check all container health
docker ps --format 'table {{.Names}}\t{{.Status}}'
```

## Monitoring Points

1. **Tunnel URL changes on every reboot** — get the new URL from `journalctl`
2. **Laptop disk at 78%** — run `sudo apt clean && sudo journalctl --vacuum-time=7d` when over 85%
3. **Pixel 7 goes offline** — last seen ~hours ago, check `tailscale status` for `pixel-7`
4. **fail2ban bans** — currently 0 active bans, 26 total failed attempts logged
5. **Laptop sleep** — if laptop sleeps, llama-server goes down. Wake it and check `systemctl status llama-server`
6. **No permanent domain** — quick tunnel URL is ephemeral. Consider Namecheap domain + Cloudflare DNS tunnel for persistence

## Network Map

```
Pixel 7 ───┐
            ├─ Tailscale ─┐
Laptop ─────┘             │
                          ├── SSH (22, UFW)
                          │
Server (fc3130197) ───────┘
  │
  ├─ :8080 (Caddy, 127.0.0.1 only) ── Cloudflare tunnel ── Internet
  │    ├─ / → static site
  │    ├─ /uncensored → chat proxy :8081
  │    ├─ /api/* → chat proxy :8081
  │    └─ /webhook/* → n8n :5678
  │
  ├─ :8081 (chat proxy, 127.0.0.1)
  │    ├─ RE-Ai chat (DeepSeek Flash)
  │    ├─ Uncensored chat → laptop :9000 (Tailscale)
  │    └─ Presets API
  │
  └─ Docker (all 127.0.0.1)
       ├─ postgres:5432
       ├─ redis:6379
       ├─ qdrant:6333-6334
       └─ n8n:5678
```

### Tailscale IPs

| Device | IP | Hostname |
|--------|----|----------|
| Server | 100.87.20.48 | fc3130197 |
| Laptop | 100.102.204.115 | parrot-1 |
| Pixel 7 | 100.107.174.67 | pixel-7 |
| Other | 100.100.7.102 | parrot |
| Other | 100.109.225.90 | desktop-fl5c0kf |
| Other | 100.116.39.52 | hush-brain-a100 |

## Data Flow

```
You (Telegram) ←→ CHatz ←→ Tools / MCP / Docker / Vault
                                      │
Pixel web browser ←→ Cloudflare tunnel ←→ Caddy ←→ Chat proxy ←→ Laptop llama.cpp
                                      │
                                      ├── RE-Ai API (DeepSeek)
                                      └── n8n webhooks
```

## Recent Changes (2026-07-05)

1. Full security audit & hardening (UFW, fail2ban, SSH, Docker, Caddy, proxy lockdown)
2. Laptop disk cleanup — removed 14GB of partial LLM downloads
3. llama-server as systemd service (auto-start on boot, ollama killed)
4. Cloudflare tunnel as systemd service (auto-start on boot)
5. Production build deployment to `/var/www/buildabot/`
6. Uncensored chat client v2 (streaming, markdown, voice, presets, copy buttons)
7. Auto-log all uncensored exchanges to vault (`UNSENSORED/`)
8. Pixel 7 watchdog (boot ping + 30-minute health check cron)
9. Obsidian vault git push + laptop sync
