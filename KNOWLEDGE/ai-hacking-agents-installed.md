# AI Hacking Agents — Installation Report

**Generated:** 2026-07-05  
**Source:** [github.com/EvanThomasLuke/Awesome-AI-Hacking-Agents](https://github.com/EvanThomasLuke/Awesome-AI-Hacking-Agents) (88 tools listed)

---

## Install Summary

| # | Tool | Version | Method | Status | Notes |
|---|------|---------|--------|--------|-------|
| 83 | pentest-ai (`ptai`) | latest | `uv pip install ptai` | ✅ Installed | CLI: `ptai start <target>` or MCP: `claude mcp add pentest-ai -- ptai mcp` |
| 23 | raink (BishopFox) | latest | `go install` | ✅ Installed | `/usr/local/bin/raink` |
| 28 | fraim | 0.8.0 | `uv venv --python 3.12` + `uv pip install fraim` | ✅ Installed | Needs Python 3.12 venv at `/tmp/fraim-venv` |
| 85 | claude-mythos | prompts | `git clone` | ✅ Cloned | `/root/buildabot/tools/claude-mythos`. Feed `main_prompt.txt` to Claude |
| 75 | red-run (Black Lantern) | latest | `git clone` + `./install.sh` | ✅ Cloned | `/root/buildabot/tools/red-run`. Needs `claude` CLI (laptop) |
| 25 | ARTEMIS (Stanford) | latest | `git clone` + `cargo build --release` + `uv sync` | ✅ Built | 24MB codex binary. Needs `OPENROUTER_API_KEY` |
| 86 | AIMap (BishopFox) | latest | `git clone` + Docker MongoDB + Python deps | ✅ Set up | MongoDB on `127.0.0.1:27017`. Needs Shodan API key |
| 81 | redai | latest | `git clone` + `bun install` | 🔄 Compiling | `/root/buildabot/tools/redai` |
| 10 | vulnhuntr (Protect AI) | latest | n/a | ❌ Skipped | Requires Python 3.10 specifically (system has 3.12). Docker would work. |
| 54 | AgenticRed | latest | n/a | ❌ Skipped | Requires 3× L40 GPUs — not practical for this server |
| 72 | llmchainhunter | n/a | n/a | ❌ Skipped | Claude Code runbook/docs — not installable |
| 73 | operant-mcp | latest | `npm install -g operant-mcp` | ✅ Installed | 62 tools, all deps loaded |
| • | operant-mcp deps | • | `apt install` + `go install` | ✅ All 8 | tshark, olevba, oledump, vol3, nuclei, ffuf, arjun |

---

## Tool Details

### pentest-ai `ptai` (#83)
**Repo:** github.com/0xSteph/pentest-ai  
**Type:** AI-driven pentest tool with oracle verification  
**Install:** `pip install ptai`  
**Key features:**
- 14 verified vulnerability classes
- 100% precision, zero false positives on test honeypots
- 12 verified findings on OWASP Juice Shop in one scan
- Runs as CLI or MCP server
- `ptai setup --tier [core|recommended|full]` → auto-installs 200+ security tools
- **Run:** `ptai start https://target.com` or `ptai mcp`

### raink (#23)
**Repo:** github.com/BishopFox/raink  
**Type:** LLM document ranking for vulnerability identification  
**Install:** `git clone && cd raink && go install`  
**Usage:** `raink -f input.txt -p "prompt" -r 10 -s 10`  
**Use case:** Rank code diffs/patches by likelihood of fixing security bugs

### fraim (#28)
**Repo:** github.com/fraim-dev/fraim  
**Type:** Security engineer's AI toolkit  
**Install:** Python 3.12+ required. `pipx install fraim` or `uv venv --python 3.12` then `uv pip install fraim`  
**Features:**
- Risk Flagger — auto-flag PRs for security review
- Code Security Analysis — LLM-powered vulnerability scanning
- CI/CD integration via SARIF output
- **Run:** `fraim run code --location <repo>`

### claude-mythos (#85)
**Repo:** github.com/anshug/claude-mythos  
**Type:** Prompt framework / methodology  
**Install:** Clone repo. Feed `prompt/main_prompt.txt` to any LLM  
**Agents:** Recon → Hunter → Adversarial → Exploit → Triage → AI Security  
**Very easy to use** — just a text prompt with embedded multi-agent logic

### red-run (#75)
**Repo:** github.com/blacklanternsecurity/red-run  
**Type:** Security assessment toolkit for Claude Code  
**Install:** `git clone && ./install.sh`  
**Requires:** `claude` CLI, uv, Docker  
**Features:**
- Multi-phase CTF/lab engagement orchestration
- Persistent SQLite state across context compactions
- RAG skill retrieval from ChromaDB
- Agent teams in persistent tmux sessions
- MCP servers: nmap, shell, browser, skill-router
- `preflight.sh` checks: 18 passed / 17 missing / 67 optional on this server
- **Use on laptop:** `scp -r root@server:/root/buildabot/tools/red-run . && cd red-run && ./install.sh`

### ARTEMIS (#25)
**Repo:** github.com/Stanford-Trinity/ARTEMIS  
**Type:** Autonomous multi-agent vulnerability discovery  
**Install:** Complex — Rust build (~2 min) + Python uv sync  
**Architecture:**
- Rust `codex` binary — sandboxed code execution (24MB release build)
- Python supervisor — orchestrates multi-agent pipeline
- YAML configs for test scenarios (CTF, real-world)
- **Run:** `python -m supervisor.supervisor --config-file configs/tests/ctf_easy.yaml`

### AIMap (#86)
**Repo:** github.com/BishopFox/aimap  
**Type:** Internet-scale AI agent infrastructure discovery platform  
**Components:**
- FastAPI backend + MongoDB + Redis
- React/Vite frontend with 3D globe visualization  
- 32+ Shodan queries for AI infrastructure scanning  
**Detects:** MCP servers, Ollama, vLLM, LiteLLM, LangServe, Gradio, ComfyUI, Streamlit, etc.  
**Risk scoring:** 0–10 based on auth, tool exposure, CORS, TLS, prompt leakage  
**Needs:** Shodan API key in `.env`. MongoDB on `127.0.0.1:27017`.  
**Run:** `cd /root/buildabot/tools/aimap && docker compose up --build`

### redai (#81)
**Repo:** github.com/kpolley/redai  
**Type:** Terminal workbench for AI-driven vulnerability discovery with live validation in Chrome  
**Install:** `bun install -g @kpolley/redai` (or clone + `bun install`)  
**Architecture:**
- Scanner agents → candidate findings  
- Validator agents → prove/disprove in live Chrome/iOS simulator  
- Detailed Markdown/HTML/JSON report with PoC evidence  
- **Run:** `redai` (after install completes)  

### operant-mcp (#73)
**Repo:** github.com/operantlabs/operant-mcp  
**Type:** MCP server with 62 pentesting tools  
**Install:** `npm install -g operant-mcp` + `hermes mcp add operant --command operant-mcp`  
**Deps installed:** tshark, olevba, oledump, vol3, nuclei (v3.10.0), ffuf (v2.1.0), arjun  
**Tools include:** SQLi (16 patterns), XSS (8 contexts), SSRF, PCAP analysis, memory forensics, cloudtrail analysis, auth brute-force, GraphQL introspec+query, JWT attacks, race conditions, nuclei templates, ffuf fuzzing, param discovery, TLS analysis, CORS scanning

---

## Infrastructure Added

| Addition | Details |
|----------|---------|
| **MongoDB 7** | Docker container `re-ai-mongodb` on `127.0.0.1:27017` (for AIMap) |
| **Rust 1.96.1** | Installed via rustup for ARTEMIS codex build |
| **Bun** | Runtime at `/root/.bun/bin/bun` for redai |
| **libssl-dev** | Required by ARTEMIS Rust OpenSSL bindings |
| **Python 3.12** | Already present, used by fraim |

---

## Tools Directory

```
/root/buildabot/tools/
├── red-run/             # Black Lantern Claude Code toolkit
├── claude-mythos/       # Prompt methodology framework
├── fraim/               # Python security toolkit (cloned)
├── ARTEMIS/             # Stanford multi-agent vuln discovery (built)
├── aimap/               # BishopFox AI infra discovery (setup)
└── redai/               # Terminal vuln workbench (installing)
```

---

## Quick Reference — Run Commands

```bash
# pentest-ai
ptai start https://target.com                           # Scan a target
ptai demo                                                # Run demo
ptai mcp                                                 # Run as MCP server

# raink (doc ranking)
raink -f patches.txt -p "Which fixes the bug?" -r 10

# fraim (security toolkit)
fraim run code --location https://github.com/user/repo
fraim run risk_flagger --diff --base main --head feature

# ARTEMIS (Stanford)
cd /root/buildabot/tools/ARTEMIS
python -m supervisor.supervisor --config-file configs/tests/ctf_easy.yaml

# AIMap (infra discovery)
cd /root/buildabot/tools/aimap && docker compose up --build

# red-run (needs claude CLI)
cd /root/buildabot/tools/red-run && ./run.sh

# redai (vuln workbench)
cd /root/buildabot/tools/redai && bun run redai
```

---

## Notes

- Most tools need API keys (Anthropic, OpenAI, OpenRouter) — configure via `.env` files
- AIMap needs a Shodan API key to function
- red-run needs `claude` CLI — install and run on the laptop
- vulnhuntr can be run in Docker as a workaround for the Python 3.10 requirement
- ARTEMIS requires `OPENROUTER_API_KEY` in `.env` to run
- redai is still compiling dependencies via `bun install` from local checkout
