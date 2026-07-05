# System Status & Security Report — 2026-07-05

## Overview

Full security audit and hardening completed. All Docker ports locked, firewall active, fail2ban running, auto-updates configured, laptop LLM daemonized.

---

## What Changed

### Docker Ports Locked
Postgres, Redis, Qdrant, n8n — all bound to `127.0.0.1` only. No internet-facing database/queue/automation ports.

### Reverse Proxy (Caddy) Installed
- Listens on `127.0.0.1:8080`, bound to localhost only
- Routes `/api/*` → `localhost:8081` (chat proxy)
- Routes `/webhook/*`, `/rest/*`, `/static/*` → `localhost:5678` (n8n)
- Serves static production build from `/var/www/buildabot`

### Cloudflare Tunnel → Systemd Service
- Quick tunnel daemonized: `/etc/systemd/system/cloudflared-tunnel.service`
- Connects to `http://localhost:8080`
- **URL:** `https://hint-sphere-alerts-plan.trycloudflare.com`
- Auto-starts on boot, restarts on failure

### Website Production Build
- `npm run build` (takes ~500ms)
- Served statically by Caddy (no more Vite dev server)
- Output: `/root/buildabot/site/dist/` → copied to `/var/www/buildabot`

### Docker Healthchecks Added
| Container | Healthcheck | Purpose |
|-----------|-------------|---------|
| postgres | `pg_isready -U re_ai` | DB connectivity |
| redis | `redis-cli ping` | Cache availability |
| qdrant | `bash -c 'echo > /dev/tcp/localhost/6333'` | Vector DB port |
| n8n | `wget -q http://localhost:5678/healthz` | Automation engine |

### Docker Daemon Hardened
- `/etc/docker/daemon.json` — no-new-privileges, log limits (10MB/3 files), live-restore, inter-container isolation (icc: false)

### Unattended Upgrades Enabled
- Security patches only (no automatic reboots)
- Includes ESM (Extended Security Maintenance) repos

### UFW Firewall Active
```
Status: active
Default: deny (incoming), allow (outgoing)
Rules:
  22/tcp (OpenSSH)     ALLOW    — SSH
  587/tcp               ALLOW    — SMTP-Submission (VPSNet default)
  993/tcp               ALLOW    — IMAPS (VPSNet default)
```

### SSH Hardened
- `PermitRootLogin prohibit-password` — root login key-only
- `PasswordAuthentication yes` — user password auth (for Android) **kept on**
- `MaxAuthTries 3` — lockout after 3 failures
- `ClientAliveInterval 300` / `ClientAliveCountMax 2` — drop dead connections

### fail2ban Active
- Jail: `sshd`
- 3 failed attempts in 10 min → 1 hour ban
- Total failed attempts seen: 12

### Chat Proxy (Port 8081) Locked
- `chat-proxy.mjs` now binds to `127.0.0.1:8081` instead of `0.0.0.0`
- Only reachable through Caddy reverse proxy → tunnel

### Laptop: Ollama Stopped, llama.cpp Daemonized
- Ollama stopped and disabled
- `llama-server.service` created and enabled on boot
- Model: `Qwen3.5-9B-Uncensored-HauhauCS-Aggressive-Q4_K_M.gguf`
- Endpoint: `0.0.0.0:9000` (Tailscale-accessible from server)
- Flags: `--ctx-size 40960 --fit on --threads 16 --batch-size 512 --ubatch-size 256 --no-warmup --reasoning off --jinja`

### Laptop Disk Cleaned
- Partial LLM downloads deleted: ~14 GB freed
  - Qwen3.6-27B `.part` (9.4 GB)
  - HuggingFace `.incomplete` (4.2 GB)
  - Aria2 orphaned control file + lock file
- Disk: **83% → 78%** (106 GB free) — *after user ran `apt clean + journalctl --vacuum`*
- Still needs: `sudo apt clean && sudo apt autoremove -y && sudo journalctl --vacuum-time=7d` (~7 GB more)

### Pixel Watchdog
- Systemd service: `pixel-wake.service` — runs on boot, pings `100.107.174.67`
- Cron: `pixel-watchdog` — rechecks every 30 min (silent, no nagging)
- Log: `/var/log/pixel-wake.log`

### Broken Crons Paused
- `daily-log` (paused) — replaced by `nightly-logs`
- `morning-briefing` (paused) — replaced by `mental-health-check`

### Go 1.22 Installed
- On server for pentest tools (subfinder, httpx, etc.)

### Audit Report
- Initial audit: `SYSTEMS/audit-2026-07-05.md` in Obsidian vault
- Laptop: pull latest from GitHub to see it

---

## Current Architecture

```
Cloudflare Tunnel (:8080 outside)
  ↓ connects locally
Caddy (127.0.0.1:8080)
  ├── /api/* → chat-proxy (127.0.0.1:8081)
  ├── /webhook/*, /rest/*, /static/* → n8n (127.0.0.1:5678)
  └── /* → static site (/var/www/buildabot/)
```

## Docker Stack

```
/root/buildabot/docker-compose.yml
  Services: qdrant, postgres, n8n, redis
  Network: re-ai-network (bridge)
  Data: ./data/{qdrant,postgres,n8n,redis}/
```

**Commands:**
```bash
cd /root/buildabot
docker compose up -d       # Start stack
docker compose down        # Stop stack
docker compose logs -f     # Follow all logs
docker ps --format 'table {{.Names}}\t{{.Status}}'  # Health check
```

---

## Important Commands

### Server Management
```bash
# Tunnel URL — check if running
systemctl status cloudflared-tunnel

# Restart tunnel (new URL generated)
systemctl restart cloudflared-tunnel

# Caddy management
systemctl reload caddy          # Apply config changes
caddy validate --config /etc/caddy/Caddyfile  # Validate before reload

# Chat proxy restart
kill $(lsof -t -i :8081)
cd /root/buildabot/server && node chat-proxy.mjs &

# fail2ban
fail2ban-client status sshd           # Check bans
fail2ban-client set sshd unbanip <ip> # Unban if needed

# UFW
sudo ufw status numbered
sudo ufw delete <number>

# SSH config
sudo systemctl restart ssh
```

### Laptop Access
```bash
# SSH in
tailscale ssh dysthemix@parrot-1
# Or: ssh dysthemix@100.102.204.115

# Sudo password: single apostrophe (')
```

### LLM on Laptop
```bash
systemctl status llama-server                    # Check status
journalctl -u llama-server --no-pager -n 20      # Check logs
# Model served on port 9000, auto-starts on boot
```

---

## Cron Jobs (Active)

| Name | Schedule | Type | Status |
|------|----------|------|--------|
| `vault-watcher` | 06:00, 18:00 UTC | Script (no agent) | ✅ Active |
| `mental-health-check` | 16:00, 18:00, 00:00, 04:00 UTC | Agent | ✅ Active |
| `nightly-logs` | 06:00 UTC (midnight MT) | Script (no agent) | ✅ Active |
| `reminder-nagger` | Every 60 min | Script (no agent) | ✅ Active |
| `WTCM Watchdog` | Every 30 min | Script (no agent) | ✅ Active |
| `pixel-watchdog` | Every 30 min | Script (no agent, silent) | ✅ Active |

**Paused:**
- `daily-log` — replaced by `nightly-logs`
- `morning-briefing` — replaced by `mental-health-check`

---

## Things to Monitor

### 🟢 Currently Fine
- **Disk**: Server fine (96 GB free as root). Laptop 78% — `apt clean` will free ~7GB more
- **Memory**: Docker stack ~500MB, llama.cpp ~6GB (on laptop)
- **fail2ban**: 12 failed SSH attempts logged, 0 bans triggered (threshold 3)
- **Tunnel**: Running, routes working, chat + website + webhooks all 200
- **Uncensored LLM**: Responding, ~500ms per request over Tailscale

### 🟡 Watch
- **Laptop uptime**: Booted at 00:36 MT today — verify llama-server auto-starts on next reboot
- **Laptop disk**: Still 78% — `sudo apt clean && sudo journalctl --vacuum-time=7d` would reclaim ~7GB
- **Git push**: Vault remote is HTTPS — no credential helper configured. Cron pushes may fail silently
- **Phone (Pixel)**: Shows offline in Tailscale (100.107.174.67). Watchdog checks every 30 min
- **Kali testing**: If you run heavy pentools, server disk could fill from scans/logs
- **Broken crons**: `daily-log` and `morning-briefing` paused — if you miss them, unpause or delete

### 🔴 Would Fix Next
- **Production domain**: Quick tunnel URL changes on restart. Permanent URL needs Cloudflare auth + domain
- **Brand unification**: Landing page is purple, site uses amber. Post-prod polish
- **Telegram restriction**: Config set (`allowlist`) but not active — needs gateway restart
- **laptop Git auto-push**: No cron for backing up laptop vault to GitHub
- **Chat proxy persistence**: Started manually in background — no systemd service. Dies on server restart

---

## Storage

| Location | Path | Notes |
|----------|------|-------|
| Vault (server) | `/root/obsidian-vault/` | Git remote: `build_a_bot` → GitHub |
| Vault (laptop) | `/home/dysthemix/projects/build_a_bot/sample_bot/build_a_bot_memory/` | Same remote |
| Docker data | `/root/buildabot/data/{postgres,redis,qdrant,n8n}/` | Back up postgres regularly |
| Nightly logs | Generated by script → pushed to vault | `/root/.hermes/scripts/nightly-log.py` |
| Website build | `/root/buildabot/site/dist/` → `/var/www/buildabot/` | Rebuild on site changes |

---

*Report generated by CHatz on 2026-07-05. Tunnel URL at time of writing: `https://hint-sphere-alerts-plan.trycloudflare.com`*
