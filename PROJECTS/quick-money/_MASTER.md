# Quick-Money Projects — Indications Media

**Brand:** Indications Media — "Creative digital experiences that blend story, art & technology."
**Site:** indicationsmedia.vercel.app
**Tagline for all client-facing work:** Built by Indications Media

---

## Why We Win

| Asset | How It Generates Cash |
|-------|----------------------|
| Scraper (Firecrawl + Stealth) | Data collection for any niche |
| n8n automation | Deliver services on autopilot |
| SendGrid email | Outreach at scale |
| Telegram bots (RE-Ai) | Chat-based services |
| AI agent (Hermes) | Custom build-outs fast |
| Zillow/Redfin feeds | Real estate is the beachhead |

---

## Project Rankings

Quick score: **Effort** (1-5, lower=easier) × **Value** ($/mo potential) × **Scalability** (how repeatable)

| # | Project | Effort | Value/mo | Scalability | Score | Timeline |
|---|---------|--------|----------|-------------|-------|----------|
| 1 | Property Alert Service | 2 | $500-2k | ★★★★★ | **Top** | 1-2 days |
| 2 | Real Estate Lead Gen | 3 | $1k-5k | ★★★★ | **High** | 3-5 days |
| 3 | Web Scraping as a Service | 2 | $500-3k | ★★★★★ | **Top** | 1-2 days |
| 4 | AI Content Service | 3 | $1k-3k | ★★★★ | **High** | 2-3 days |
| 5 | Competitor Monitoring | 2 | $300-1.5k | ★★★★ | **High** | 1-2 days |
| 6 | Email Outreach Agency | 3 | $2k-5k | ★★★★ | **High** | 3-5 days |
| 7 | Review Management | 2 | $500-2k | ★★★ | **Med** | 1-2 days |
| 8 | Social Media Auto-Pilot | 4 | $1k-3k | ★★★★ | **Med** | 3-5 days |

---

## Project Details

### 1. Property Alert Service

**What:** Users tell us what they want (city, budget, beds/baths), we scrape Zillow/Redfin daily and email them when matching listings appear.

**Why it works:**
- Zero content generation needed — just forwarding data
- Recurring subscription ($29-49/mo per alert)
- n8n handles the whole loop (scrape → filter → email)
- One setup per market, then it runs forever

**Tech pipeline:**
```
n8n cron (daily)
  → re-ai-scraper.py scrape Zillow search URL
  → Python filter (match criteria)
  → SendGrid email with listing summary
  → Postgres store (seen IDs, avoid duplicates)
```

**n8n Workflow:** `property-alert-daily`

**Pricing:** $29/mo per search filter, $49/mo pro (unlimited filters)
**Target:** Real estate agents, home buyers, investors

---

### 2. Real Estate Lead Gen

**What:** Scrape Zillow/Redfin for FSBO / expired listings / motivated sellers. Build a list. Sell to agents.

**Why it works:**
- Agents pay $200-500/mo for quality leads
- No paid ads needed — we mine existing data
- The scraper already works

**Pipeline:**
```
n8n cron (weekly)
  → scrape Zillow "coming soon" / "newest"
  → enrich contact info (reverse address lookup)
  → format as CSV/CRM import
  → email to client agents
```

**Pricing:** $297/mo per agent territory (same as RE-Ai Regular tier)
**Target:** Real estate agents who hate Zillow's lead costs

---

### 3. Web Scraping as a Service

**What:** "Give us a URL, get clean data back." One-off or recurring.

**Why it works:**
- Our stack is already built
- Every business needs competitor data
- No recurring infrastructure cost

**Pipeline:**
```
Client request (email/form)
  → n8n trigger
  → re-ai-scraper.py scrape
  → format result (CSV/JSON/excel)
  → email back
```

**Pricing:** $97/site one-time, $47/mo recurring for weekly updates
**Target:** E-commerce, research firms, RE investors

---

### 4. AI Content Service

**What:** Write blog posts, social captions, emails, product descriptions using AI for local businesses.

**Pipeline:**
```
n8n cron (weekly/daily)
  → AI generates content from topic/brief
  → format as blog post / social post / email
  → deliver (email, WordPress API, social scheduler)
```

**Pricing:** $197/mo for 4 blog posts, $297/mo for 8 posts + social
**Target:** Local businesses who can't write

---

### 5. Competitor Monitoring

**What:** Track competitor websites for changes — pricing, new products, job postings, content changes.

**Pipeline:**
```
n8n cron (daily)
  → scrape competitor URLs
  → compare with last snapshot (hash check)
  → if changed → summarize diff with AI → email alert
```

**Pricing:** $97/mo per 5 URLs, $297/mo per 20 URLs
**Target:** Any business with competitors

---

## Go-To-Market

**Phase 1 (This Week):** Property Alert Service + Web Scraping Service
- Both use existing infrastructure
- Zero new code needed
- Can onboard first client in hours

**Phase 2 (Next Week):** Real Estate Lead Gen + Content Service
- Build on Phase 1 pipeline
- Slightly more setup per client
- Higher value per client

**Phase 3 (Month 2):** Monitoring + Email Outreach
- Most complex to deliver
- Highest recurring revenue potential

---

## The "Made by Indications Media" Footer

Every client-facing output needs this branding:
- Emails: "[Company Name] — A service by **Indications Media**"
- Reports: "Powered by Indications Media"
- Landing pages: Footer "Built by Indications Media"
- Bot messages: "🤖 Built by Indications Media"

---

## Free / Cheap Advertising

| Method | Cost | Reach/Wk | Best For |
|--------|------|----------|----------|
| Kijiji postings | $0 | 500-2K views | Local services |
| Craigslist postings | $0 | 500-2K views | Local + national |
| Facebook Marketplace | $0 | 1K-5K views | RE leads, services |
| Facebook Groups | $0 | 1K-5K views | Niche targeting |
| X/Twitter organic | $0 | 1K-10K impressions | Build in public |
| LinkedIn organic | $0 | 500-3K views | B2B |
| Cold email (SendGrid) | $0 | 500 sends/wk | Direct B2B |
| Reddit organic | $0 | 500-3K views | Tech + niches |
| YouTube tutorials | $0 | 100-1K views | Evergreen SEO |
| Medium articles | $0 | 100-500 views | SEO + authority |

**Strategy:** Post don't sell. Show the work. A video of the scraper pulling 642 Zillow listings in 30s sells itself.

---

## New Projects (Marketplace Automation)

| # | Project | Effort | $/mo Potential | Time to $ |
|---|---------|--------|----------------|-----------|
| 6 | Rental Lead Gen | Easy | $500-1.5K | 🚀 Today |
| 7 | Price Tracker | Easy | $500-2K | 🚀 Today |
| 8 | Marketplace Arbitrage Bot | Medium | $500-2K | 1-2 days |
| 9 | Job Board Data Mining | Easy | $300-1K | 1 day |
| 10 | Cash Offer Finder (RE) | Medium | $1K-5K | 2-3 days |
| 11 | Classifieds Auto-Poster | High | $1K-3K | 3-5 days |
| 12 | Reverse 9-5 (Upwork/Fiverr) | High | $1K-5K | 1 week |
| 13 | Review / Reputation Generator | High | $1K-5K | 1 week |

See [[marketplace-projects]] for full breakdown of each.

---

## Social Media Accounts

| Platform | Handle | Priority | Status |
|----------|--------|----------|--------|
| X/Twitter | @IndicationsMedia | P1 | 🔧 Create |
| Instagram | @indicationsmedia | P1 | 🔧 Create |
| LinkedIn | Indications Media (Company) | P1 | 🔧 Create |
| Facebook | Indications Media (Page) | P1 | 🔧 Create |
| TikTok | @indicationsmedia | P2 | 📅 Next wave |
| YouTube | Indications Media | P2 | 📅 Next wave |
| Medium | indicationsmedia.medium.com | P2 | 📅 Next wave |

See [[social-media-setup]] for bios, content strategy, and posting cadence.

---

## Next Actions (This Week)

- [ ] Fix Vercel token → deploy scraper site (DONE ✅)
- [ ] Create X/Twitter account → first thread: "I built a bot that scrapes Zillow"
- [ ] Create FB/Instagram/LinkedIn accounts
- [ ] Post first Kijiji ad: "Web data extraction — $97/site"
- [ ] Cold email 10 RE agents with free sample offer
- [ ] Activate Property Alert n8n workflow for a demo run
- [ ] **Build Local Business Lead List generator** (highest ROI, fastest ship)
- [ ] **Start traffic push** — X/Twitter + Reddit + cold email (day 1)

See [[money-research]] for the full 25+ idea playbook
See [[traffic-playbook]] for distribution channels & day-by-day plan
