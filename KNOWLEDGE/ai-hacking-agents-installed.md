# AI Hacking Agents — Installation Report

**Generated:** 2026-07-05  
**Source:** [github.com/EvanThomasLuke/Awesome-AI-Hacking-Agents](https://github.com/EvanThomasLuke/Awesome-AI-Hacking-Agents) (88 tools listed)

---

## Install Summary

| Tool | Version | Method | Status | Notes |
|------|---------|--------|--------|-------|
| pentest-ai (`ptai`) | latest | `uv pip install ptai` | ✅ Installed | CLI: `ptai start <target>` or MCP: `claude mcp add pentest-ai -- ptai mcp` |
| raink (BishopFox) | latest | `go install` | ✅ Installed | `/usr/local/bin/raink` |
| fraim | 0.8.0 | `uv venv --python 3.12` + `uv pip install fraim` | ✅ Installed | Needs Python 3.12 venv at `/tmp/fraim-venv` |
| claude-mythos | prompt framework | `git clone` | ✅ Cloned | `/root/buildabot/tools/claude-mythos` |
| red-run (Black Lantern) | latest | `git clone` + `./install.sh` | ✅ Cloned | `/root/buildabot/tools/red-run`. Needs `claude` CLI runtime |
| ARTEMIS (Stanford) | latest | `git clone` + `cargo build` + `uv sync` | ✅ Built | `/root/buildabot/tools/ARTEMIS`. 24MB codex binary. Needs `OPENROUTER_API_KEY` |
| AIMap (BishopFox) | latest | `git clone` + MongoDB + pip deps | ✅ Set up | `/root/buildabot/tools/aimap`. MongoDB in Docker. Needs Shodan API key. |
| redai | latest | `bun install -g @kpolley/redai` | 🔄 Compiling | 5+ min TypeScript build |
| vulnhuntr (Protect AI) | latest | `pipx install` | ❌ Skipped | Requires Python 3.10 specifically (Ubuntu 24.04 ships 3.12) |
| AgenticRed | research | `git clone` | ❌ Skipped | Requires 3× GPUs (L40+) |
| llmchainhunter | runbook | n/a | ❌ Skipped | Claude Code design docs for Java deserialization research |

---

## Tool Details

### pentest-ai (`ptai`)
- **Type:** AI-driven pentest tool with oracle verification
- **Install:** `pip install ptai`
- **Key features:**
  - 14 verified vulnerability classes
  - 100% precision, zero false positives on test honeypots
  - 12 verified findings on OWASP Juice Shop in one scan
  - Runs as CLI or MCP server
  - `ptai setup --tier [core|recommended|full]` → auto-installs 200+ security tools
- **API key:** Anthropic or OpenAI
- **Run:** `ptai start https://target.com` or `claude mcp add pentest-ai -- ptai mcp`

### raink (BishopFox)
- **Type:** LLM document ranking for vulnerability identification
- **Install:** `git clone && cd raink && go install`
- **Usage:** `raink -f input.txt -p "prompt" -r 10 -s 10`
- **API key:** OpenAI
- **Use case:** Rank code diffs or patches by likelihood of fixing security bugs

### fraim
- **Type:** Security engineer's AI toolkit (CLI + GitHub Action)
- **Install:** `pipx install fraim` (Python 3.12+)
- **Key features:**
  - Risk Flagger — auto-flag PRs for security review
  - Code Security Analysis — LLM-powered vulnerability scanning
  - CI/CD integration via SARIF output
- **API key:** Anthropic, OpenAI, or Gemini

### claude-mythos
- **Type:** Prompt framework / methodology, not a standalone tool
- **Install:** Clone repo, feed `prompt/main_prompt.txt` to Claude
- **Agents:** Recon → Hunter → Adversarial → Exploit → Triage → AI Security
- **Use case:** Multi-agent red teaming methodology in a single prompt

### red-run (Black Lantern Security)
- **Type:** Security assessment toolkit for Claude Code
- **Install:** `git clone && ./install.sh`
- **Requires:** `claude` CLI (laptop), uv, Docker
- **Features:**
  - Multi-phase CTF/lab engagement orchestration
  - Persistent SQLite state across context compactions
  - RAG skill retrieval from ChromaDB
  - Agent teams in persistent tmux sessions
  - MCP servers: nmap, shell, browser, skill-router
- **Install on laptop via:** `scp -r root@server:/root/buildabot/tools/red-run . && cd red-run && ./install.sh`

### ARTEMIS (Stanford Trinity)
- **Type:** Autonomous multi-agent vulnerability discovery
- **Install:** Complex — Rust build (2 min) + Python uv sync
- **Architecture:**
  - Rust codex binary — sandboxed code execution
  - Python supervisor — orchestrates multi-agent pipeline
  - YAML configs for test scenarios
- **API key:** OpenRouter or OpenAI
- **Run:** `python -m supervisor.supervisor --config-file configs/tests/ctf_easy.yaml`

### AIMap (BishopFox)
- **Type:** Internet-scale AI agent infrastructure discovery platform
- **Install:** Docker Compose or local development
- **Components:**
  - FastAPI backend + MongoDB + Redis
  - React/Vite frontend with 3D globe visualization
  - 32+ Shodan queries for AI infrastructure
- **Detects:** MCP servers, Ollama, vLLM, LiteLLM, LangServe, Gradio, ComfyUI, Streamlit, HuggingFace TGI, Open WebUI, LibreChat
- **Key capability:** Risk scoring (0–10) based on auth, tool exposure, CORS, TLS, prompt leakage
- **Needs:** Shodan API key (MongoDB already in Docker on `127.0.0.1:27017`)

### redai
- **Type:** Terminal workbench for AI-driven vulnerability discovery with live validation
- **Install:** `bun install -g @kpolley/redai` (heavy TypeScript build)
- **Architecture:**
  - Scanner agents → produce candidate findings
  - Validator agents → prove/disprove in live environment (Chrome/iOS simulator)
  - Markdown/HTML/JSON report with PoC evidence
- **API key:** Anthropic or OpenAI

---

## Dependencies Added

| Dependency | For Tool | Status |
|-----------|----------|--------|
| libssl-dev | ARTEMIS Rust build | ✅ |
| Rust 1.96.1 | ARTEMIS codex build | ✅ |
| bun | redai | ✅ |
| MongoDB 7 | AIMap (Docker) | ✅ |
| Python 3.12 | fraim | ✅ (was already installed) |
| tshark | operant-mcp PCAP | ✅ |
| olevba + oledump.py | operant-mcp malware | ✅ |
| vol3 | operant-mcp memory forensics | ✅ |
| nuclei 3.10.0 | operant-mcp scanning | ✅ |
| ffuf 2.1.0 | operant-mcp fuzzing | ✅ |
| arjun | operant-mcp param discovery | ✅ |

---

## Tools Directory

```
/root/buildabot/tools/
├── claude-mythos/     # Prompt methodology framework
├── fraim/             # Python security toolkit (cloned)
├── ARTEMIS/           # Stanford multi-agent vuln discovery (built)
├── aimap/             # BishopFox AI infra discovery (setup)
├── red-run/           # Claude Code security toolkit (cloned)
```

---

## Quick Reference — Common Commands

```bash
# pentest-ai
ptai start https://target.com                           # Scan a target
ptai demo                                               # Run demo on bundled app
ptai mcp                                                # Run as MCP server
ptai setup --tier core                                  # Install tool deps

# raink
raink -f patches.txt -p "Which fixes the security bug?" -r 10   # Rank patches

# fraim
fraim run code --location https://github.com/user/repo           # Scan a repo
fraim run risk_flagger --diff --base main --head feature         # Flag PR risks

# ARTEMIS
cd /root/buildabot/tools/ARTEMIS
python -m supervisor.supervisor --config-file configs/tests/ctf_easy.yaml

# AIMap (Docker)
cd /root/buildabot/tools/aimap
docker compose up --build                               # Start full stack

# red-run (needs Claude Code)
cd /root/buildabot/tools/red-run
bash preflight.sh                                        # Check dependencies
./run.sh                                                 # Start engagement

# redai
redai                                                    # Launch terminal workbench
```

---

## Notes

- **redai** build is still compiling (5+ min TypeScript via bun)
- **vulnhuntr** needs Python 3.10 — could be run in Docker as workaround
- **red-run** requires `claude` CLI — install on laptop for usage
- **AIMap** needs Shodan API key to function (set in `.env`)
- Most tools need API keys (Anthropic, OpenAI, OpenRouter) — config via `.env` or env vars
