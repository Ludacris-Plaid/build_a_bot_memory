---
created: 2026-07-04
type: system
tags: [scraper, web, firecrawl, lightpanda, playwright, re-ai]
status: active
engine: re-ai-scraper
source: Chapter 9 Browser Automation
---

# RE-Ai Triple-Layer Web Scraper

A production-grade web scraping system with three fallback engines designed for real estate research, lead enrichment, and competitive intelligence. Automatically escalates through layers as target difficulty increases.

## Architecture

```
User Request (URL / Search Query / Crawl Target)
         │
    ┌────▼────┐    
    │ LAYER 1 │  Firecrawl Cloud API
    │  smart  │  Handles 95% of targets. Built-in anti-bot,
    └────┬────┘  JS rendering, clean Markdown output.
         │
    ┌────▼────┐    
    │ LAYER 1b│  Firecrawl + Interactive Browser
    │  hard   │  Cookie dismissal, form interaction, scroll/wait
    └────┬────┘  before scraping. For sites behind cookie walls.
         │
    ┌────▼────┐    
    │ LAYER 2 │  Lightpanda Browser
    │  fast   │  9x faster, 16x less memory than Chromium.
    └────┬────┘  CDP server at ws://127.0.0.1:9222.
         │       Best for speed-critical bulk scraping.
    ┌────▼────┐    
    │ LAYER 3 │  Playwright (Standalone Chromium)
    │  compat │  Full browser engine. Handles complex SPAs,
    └────┬────┘  enterprise bot protection, and the hardest 1%
         │       of targets.
         ❌ Report all failures with error chain
```

## Capabilities

| Command | Description | Example |
|---------|-------------|---------|
| `search` | Web search with full-page content | "homes for sale Calgary 3 bedroom" |
| `scrape` | Extract URL → Markdown/HTML | realtor.ca listing URL |
| `scrape --hard` | Interactive scrape (cookie bypass) | REALTOR.ca / MLS sites |
| `scrape --format screenshot` | Full-page screenshot | Visual verification |
| `crawl` | Map + scrape entire domain | Brokerage website |
| `interact` | Click, fill forms, scroll | Login-gated content |

## Smart Content Detection

The scraper automatically detects and rejects low-quality content:

- **Cookie walls**: "we use cookies", "privacy policy", "accept cookies" (3+ signals = reject)
- **Login walls**: "sign in", "create account", "log in"
- **JS-required**: "enable javascript", "please enable javascript"
- **Short content**: Under 50 chars is treated as failure

Detection triggers automatic escalation to the next layer.

## Installation & Configuration

```bash
# Firecrawl Cloud API
pip install firecrawl-py
export FIRECRAWL_API_KEY=fc-4e2f2f5b95e743f48ea986ffc07e7f27

# Lightpanda (CDP server)
docker run -d --name lightpanda -p 127.0.0.1:9222:9222 lightpanda/browser:nightly

# Playwright (Chromium, auto-installed with Hermes)
pip install playwright
python3 -m playwright install chromium
```

## Performance Benchmarks

| Metric | Lightpanda | Chromium | Difference |
|--------|-----------|----------|------------|
| Memory (100 pages) | 123MB | 2GB | ~16x less |
| Execution (100 pages) | 5s | 46s | ~9x faster |
| Download size | ~15MB | ~300MB | ~20x smaller |

## Hard Target Strategy

For sites behind enterprise bot protection (Incapsula, Cloudflare, DataDome):

1. **Start with search instead of scrape** — find the target on a more accessible source (Zillow, Redfin)
2. **Use `--hard` flag** for Firecrawl interact mode (click dismiss, wait for render, scroll)
3. **Alternative sources**: If realtor.ca blocks, try Zillow, Redfin, or the specific brokerage site
4. **Direct integration**: Only guaranteed bypass for Incapsula is direct MLS access or API

## File Locations

| Component | Path |
|-----------|------|
| Scraper script | `~/buildabot/scripts/re-ai-scraper.py` |
| Hermes skill | `/root/.hermes/skills/re-ai/re-ai-scraper/` |
| RE-Ai SOUL.md | `/root/.hermes/profiles/re-ai-demo/SOUL.md` |
| Nagging reminders | `~/buildabot/scripts/re-ai-nagger.py` |

## Related

- [[buildabot-ca]] — Client progress tracking
- [[../software/buildabot-stack]] — Full infrastructure overview
