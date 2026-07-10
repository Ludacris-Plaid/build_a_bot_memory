# PWNKIT — Quick Action Guide

> All tools installed at `/root/buildabot/tools/`  
> Reports auto-save to `/root/obsidian-vault/PWNKIT/`

---

## 🏆 pwnkit — One-Command Recon & Scanning

*The most useful tool — chains everything together.*

### Recon a target:
```bash
# Basic scan (TLS, headers, CORS, cookies, nuclei vulns, AI analysis)
pwnkit recon https://example.com

# Scan internal services too
pwnkit recon http://192.168.1.100:8000
pwnkit recon http://internal-app.local
```

### Scan code for vulnerabilities:
```bash
# Basic scan (code stats + AI analysis)
pwnkit code /path/to/project

# Full scan (if ANTHROPIC_API_KEY is set — runs vulnhuntr deep scan)
export ANTHROPIC_API_KEY=sk-...
pwnkit code /path/to/project claude
```

### Hunt for exposed AI endpoints:
```bash
# Probes 25 common AI endpoints (Ollama, vLLM, MCP, Gradio, ComfyUI, etc.)
pwnkit ai-scan http://10.0.0.50:8080
pwnkit ai-scan https://ai-service.example.com
```

### Manage reports:
```bash
pwnkit report list          # List all reports
pwnkit report view 1        # View report #1
pwnkit report merge 1 2 3   # Merge reports into one
pwnkit report delete 3      # Delete report #3
```

### See what's available:
```bash
pwnkit list
```

---

## 🐍 vulnhuntr — Deep Code Vulnerability Hunter

*Autonomous Python code scanning — found real 0-days in ComfyUI, Langflow, etc.*

```bash
# Requires: ANTHROPIC_API_KEY or OPENAI_API_KEY
export ANTHROPIC_API_KEY=sk-...

# Scan a repository for vulnerabilities
vulnhuntr -r /path/to/repo -l claude

# Full output with all report formats
vulnhuntr -r /path/to/repo -l claude \
  --markdown /tmp/report.md \
  --html /tmp/report.html \
  --json /tmp/findings.json \
  --sarif /tmp/report.sarif

# With budget limit ($2 max)
vulnhuntr -r /path/to/repo -l claude --budget 2

# Create GitHub issues for found vulns
vulnhuntr -r /path/to/repo -l claude --github-issue
```

**Pro tip:** vulnhuntr is EXPENSIVE if you let it run wild. Always set `--budget`.

---

## 🎯 raink — LLM-Powered Document Ranking

*Rank security patches, CVEs, or findings by severity.*

```bash
# Requires: OPENAI_API_KEY
export OPENAI_API_KEY=sk-...

# Rank vulnerability patches (input file has one patch per line)
raink -f patches.txt -p "Rank these patches by security impact" -r 3

# Rank output from other tools
cat scan_results.txt | raink -p "Which findings need immediate attention?" -r 5

# Batch processing for large documents
raink -f cve_list.txt -p "Rank these CVEs by criticality" -r 10 -s 5
```

---

## 🎛️ redai — Interactive Vuln Workbench

*Terminal-based AI security tool with live validation.*

```bash
# Interactive mode (browse and analyze)
redai

# Direct analysis
redai --target /path/to/code
redai --issue "Injection vulnerability in user input handler"
```

---

## 🔬 fraim — AI Code Security Engineer

*Code scanning, IaC analysis, and PR risk flagging.*

```bash
# Code security scan
fraim run code --location /path/to/repo

# Infrastructure as Code scan
fraim run iac --location /path/to/terraform

# PR risk assessment
fraim run risk_flagger --pr-url https://github.com/org/repo/pull/42

# View SARIF results as HTML
fraim view results.sarif > report.html
```

---

## 🕸️ operant-mcp — 62 Pentesting Tools

*Only available inside Hermes agent sessions, not from terminal.*

```bash
# Inside a Hermes conversation:
# Start a scan
nuclei -u https://target.com -severity critical,high

# Directory fuzzing
ffuf -u https://target.com/FUZZ -w /usr/share/wordlists/dirb/common.txt -c -t 50

# Port scanning
naabu -host target.com -p 1-65535

# Subdomain discovery
subfinder -d target.com

# All operant tools: use hermes mcp call operant <tool> from agent context
```

---

## 🗺️ AIMap — AI Infrastructure Discovery

*Maps exposed AI agents and endpoints globally.*

```bash
# Requires: Shodan API key (already in .env)
cd /root/buildabot/tools/aimap && docker compose up --build

# Then access: http://localhost:5000
```

---

## 📋 Quick Reference Card

| What | Command | Needs |
|------|---------|-------|
| Full target recon | `pwnkit recon <url>` | Nothing |
| Code vuln scan | `pwnkit code <path>` | Nothing (basic) |
| AI endpoint hunt | `pwnkit ai-scan <url>` | Nothing |
| List reports | `pwnkit report list` | Nothing |
| Deep code vuln scan | `vulnhuntr -r <path>` | Anthropic API key |
| Rank documents | `raink -f <file> -p "<prompt>"` | OpenAI API key |
| Interactive vuln tool | `redai` | Nothing |
| Code security scan | `fraim run code --location <path>` | API key |
| Port scan (60s) | `naabu -host <target> -top-ports 1000` | Nothing |
| Directory brute | `ffuf -u <url>/FUZZ -w <wordlist>` | Nothing |
| Subdomain discovery | `subfinder -d <domain>` | Nothing |
| Vuln scanner | `nuclei -u <url> -severity critical,high` | Nothing |
| AIMap dashboard | `cd tools/aimap && docker compose up` | Shodan key |

---

## 🔧 API Keys Setup

```bash
# Add these to /root/buildabot/.env:
echo "ANTHROPIC_API_KEY=sk-..." >> /root/buildabot/.env
echo "OPENAI_API_KEY=sk-..." >> /root/buildabot/.env
```

Or export per session:
```bash
export ANTHROPIC_API_KEY=sk-...
export OPENAI_API_KEY=sk-...
```

---

*All reports saved to `/root/obsidian-vault/PWNKIT/` — automatically versioned in git.*
