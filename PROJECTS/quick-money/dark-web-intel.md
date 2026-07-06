# 🌑 Dark Web Intelligence Service

> We already have Tor installed. torsocks ready. Just need to build the pipeline.
> Potential: $500-5K/mo selling dark web intelligence and fresh .onion lists.

---

## 🛠️ What We Have Right Now

| Tool | Status | Purpose |
|------|--------|---------|
| **Tor 0.4.8.10** | ✅ Installed | Access .onion sites |
| **torsocks** | ✅ Installed | Route any command through Tor |
| **Ahmia.fi** | ✅ Free, no key | Clearnet search engine indexing .onion sites |
| **Python** | ✅ Installed | Build crawler scripts |
| **Stealth browser** | ✅ Works | Can probe live .onion sites through Tor |
| **Our server** | ✅ Available | Run 24/7 light scans |

---

## 🎯 The Product — $500-5K/mo

### Tier 1: Fresh .onion Directory ($97-197/mo subscription)

Daily updated list of **newly discovered** .onion sites, categorized:

| Category | Sample | What We Deliver |
|----------|--------|-----------------|
| Active sites | Live .onion URLs | CSV with status, title, category |
| New today | Sites < 24h old | Fresh list / daily |
| Down today | Sites that went offline | Churn tracker |
| Categorized | Market, forum, blog, etc. | Ready for use |

**Buyers:** Security researchers, threat intel firms, journalists

### Tier 2: Brand Monitoring ($297-497/mo)

Monitor dark web for mentions of a company/brand:
- Forum mentions
- Stolen credentials
- Leaked data
- Impersonation sites

**Buyers:** Mid-size companies, law firms, enterprise security teams

### Tier 3: One-Time Intelligence Reports ($500-2K)

Deep dive into specific niches:
- "All active hacking forums this quarter"
- "Marketplaces currently accepting new vendors"
- "Ransomware groups: active domains and communication channels"

**Buyers:** Government agencies, insurance companies, compliance firms

### Tier 4: Custom Dark Web Scraping ($1K-5K/project)

Need data from a specific .onion site? We build a custom crawler.
- Extract forum posts
- Download marketplace listings  
- Monitor specific threads
- Archive site content

**Buyers:** Anyone with specific dark web intelligence needs

---

## 🧪 Proof of Concept — Build in 4 Hours

### Phase 1: Ahmia Scraper (Clearnet, No Tor Needed)

Ahmia indexes .onion sites from the clearnet. We can:
1. Search Ahmia for keywords
2. Extract .onion URLs
3. Check if they're still alive
4. Categorize them
5. Track changes daily

**Script:** `/root/buildabot/scripts/dark-web-scanner.py`

### Phase 2: Tor Scanner (Needs Running Tor)

Once Tor is running on our server:
1. Use torsocks + our stealth browser to visit .onion sites
2. Grab page titles, descriptions, metadata
3. Classify the type of site
4. Take screenshots (for verification)
5. Store in PostgreSQL

### Phase 3: Continuous Monitor

n8n cron job:
- Run Ahmia scan daily → check new .onion sites
- Test each site → check if alive
- Update database
- Generate report for subscribers

### Phase 4: Payment & Delivery

- Crypto payments (Monero preferred for this market)
- Email delivery to subscribers
- Separate from Indications Media — use the grey brand

---

## 🧰 Technical Setup

### Step 1: Start Tor Service
```bash
# On our server
sudo systemctl enable tor
sudo systemctl start tor
# Tor runs as SOCKS5 proxy on 127.0.0.1:9050
```

### Step 2: Install Python Tor Tools
```bash
pip3 install stem requests[socks]
```

### Step 3: Build Ahmia Scraper
Python script that:
- Fetches new .onion sites from Ahmia
- Saves to PostgreSQL with timestamps  
- Compares against previous lists
- Generates "New Today" and "Gone Today" reports

### Step 4: Build Tor Probe
Python script using `requests` with SOCKS5 proxy at `127.0.0.1:9050`:
- Probes each .onion URL
- Gets HTTP status, page title, response time
- Classifies (market, forum, blog, search, etc.)

### Step 5: Build n8n Workflow
- Daily cron: run scanner → check sites → send report
- Weekly: full database export for paying subscribers

---

## ⚠️ Risks & Mitigations

| Risk | Mitigation |
|------|-----------|
| **Accessing illegal content** | Don't access proven illegal sites. Stick to indexable/searchable .onion sites. Block known CP/harmful sites. |
| **Server gets flagged** | Run Tor and scraping in Docker container. Nothing links to this server's IP (Tor). |
| **Legal exposure** | Selling *intelligence* is legal. Selling access to illegal content is not. Stay on the right side. |
| **Reputational risk** | Keep separate from Indications Media. Use grey brand ([[grey-brand-separation]]). |
| **Tor exit node issues** | We're accessing .onion sites, not using exit nodes. Lower risk profile. |

---

## 📦 Delivery — What Customers Get

> Sample daily report subject: *"🌑 Dark Web Report — 14 new .onion sites, 3 went down"*

```
Dark Web Intelligence Report
Indications Media (grey brand) - July 5, 2026

NEW SITES TODAY (14):
├── forsaken-forum[.]onion — Hacking forum (active, 3 topics today)
├── market-alpha[.]onion — Marketplace (active, 12 listings)
├── leak-dump[.]onion — Data leak archive (requires auth)
├── ...

SITES THAT WENT DOWN (3):
├── old-market[.]onion — Dead >48h
├── forum-xyz[.]onion — DNS not resolving
├── blog-archive[.]onion — Gone

TOTAL TRACKED: 847 live .onion sites
NEW THIS WEEK: 63
DOWN THIS WEEK: 19
```

---

## 💰 Pricing Strategy

| Tier | Price | What They Get |
|------|-------|--------------|
| **Weekly List** | $47/mo | Fresh .onion sites, emailed weekly |
| **Daily List** | $97/mo | New sites daily + status changes |
| **Brand Monitor** | $297/mo | Daily scans for their brand/keywords |
| **Pro (API Access)** | $497/mo | API + daily lists + brand monitor + raw data |
| **Custom** | $1K-5K/project | Build whatever they need |

---

## 🚀 Next Steps

1. [ ] Start Tor on our server
2. [ ] Build the Ahmia scraper (Phase 1) — 2 hours
3. [ ] Build the Tor probe (Phase 2) — 2 hours
4. [ ] Test with 100 .onion sites — verify it works
5. [ ] Set up n8n workflow for daily scanning
6. [ ] Create Gumroad product page for the lists
7. [ ] First sale: post on BHW, Reddit r/OSINT, security forums

Want me to start building Phase 1 now? The Ahmia scraper is pure clearnet — no Tor needed, works today. We can have a working prototype in <2 hours.
