# 💰 Money Research — Full Playbook

> Everything here is something we can actually build. $0 startup. Our existing stack.  
> No pipe dreams. No VC funding needed. Just code, automation, and execution.

---

## 🔥 TIER 1: Ship This Week ($0, already have everything)

### 1.1 Local Business Lead Lists

**What:** Scrape Google Maps for business contacts in any niche. Sell the lists.

**Pipeline:**
```
Stealth browser → Google Maps search "plumbers Toronto"
  → extract: name, phone, email, website, rating, reviews
  → format as CSV
  → $47 per list
```

**Target buyers:** Marketing agencies, sales teams, anyone doing cold outreach
**Our edge:** Stealth browser handles Google's anti-bot — rivals can't do this
**$ potential:** $500-3K/mo (sell 10-60 lists at $47-97 each)
**Time to first $:** 1 day

**Variations:** Restaurants, dentists, real estate agents, lawyers, contractors — any niche

---

### 1.2 E-commerce Price Monitoring

**What:** Client gives us their competitor URLs. We scrape prices daily. Alert on drops.

**Pipeline:**
```
n8n cron (daily)
  → scrape product URLs (already works)
  → compare price vs yesterday
  → if dropped → email alert
```

**Target:** Amazon sellers, Shopify stores, e-commerce brands
**Pricing:** $47/mo for 5 products, $97/mo for 20
**Our edge:** We can scrape sites others can't (stealth layer)
**$ potential:** $500-2K/mo
**Time to first $:** Today (workflow is built)

---

### 1.3 Rental/Property Lead Gen

**What:** Scrape Kijiji/FB Marketplace/Craigslist for new rental listings. Sell weekly lists.

**Pipeline:**
```
n8n cron (every 6h)
  → scrape "apartment for rent" in target city
  → extract: price, beds, location, photos
  → dedupe → format CSV
  → email to property managers
```

**Target:** Property managers, landlords, RE investors
**Pricing:** $47/mo per city, $147/mo for 5 cities
**$ potential:** $500-1.5K/mo
**Time to first $:** Today

---

### 1.4 Government Contract Alert Service

**What:** Monitor government procurement sites for new contract tenders. Email clients when relevant ones drop.

**Pipeline:**
```
n8n cron (hourly)
  → scrape procurement sites (SAM.gov, Canada Buys, provincial)
  → filter by keywords (client-defined)
  → email alert with details
```

**Target:** Government contractors, consultants, construction companies
**Pricing:** $97/mo per keyword set
**Our edge:** Stealth browser can scrape government sites that block headless browsers
**$ potential:** $1K-5K/mo
**Time to first $:** 2 days

---

### 1.5 Instagram DM Lead Gen

**What:** Scrape followers of competitor/broker accounts. Auto-extract contact info. Sell leads.

**Pipeline:**
```
Stealth browser → login to IG
  → scrape followers of target accounts
  → extract: username, bio, posts count
  → attempt email/phone extraction
  → CSV list
```

**Target:** Real estate agents, local businesses, influencers
**Pricing:** $97/mo per account monitored
**$ potential:** $500-2K/mo
**Time to first $:** 2 days
**Risk:** Low-medium (IG can ban accounts)

---

## 🔥 TIER 2: Ship This Month ($0, 2-5 days build)

### 2.1 LinkedIn Connector Bot

**What:** Auto-connect and message decision makers on LinkedIn.

**Pipeline:**
```
Stealth browser → LinkedIn
  → search for target titles (e.g., "Head of Marketing" + "Toronto")
  → send connection requests (30-50/day)
  → after accepted → send DM with offer
```

**Target:** B2B sales teams, agencies, recruiters
**Pricing:** $197/mo per account, $497/mo for 3 accounts
**$ potential:** $1K-5K/mo
**Time to first $:** 3 days

---

### 2.2 Document Autopilot (PDF → Data)

**What:** Clients upload PDFs (invoices, statements, reports). We auto-extract data to CSV/Excel.

**Pipeline:**
```
Client uploads PDF (web form or email)
  → PDF parsing (pymupdf, marker-pdf)
  → AI extraction of key fields
  → format as structured data
  → return CSV
```

**Target:** Accountants, bookkeepers, logistics companies, real estate agents
**Pricing:** $0.50/page, or $97/mo for 500 pages
**Our edge:** We have the PDF tools installed
**$ potential:** $300-1K/mo
**Time to first $:** 1 day

---

### 2.3 API Arbitrage (Dropservicing 2.0)

**What:** Wrap third-party APIs (scraping, data enrichment) and resell at markup. All automated.

**Pipeline:**
```
Client → our API/webhook
  → we call upstream API
  → reformat response
  → deliver to client
  → profit on spread
```

**Examples:**
- ScrapingBee costs $49/mo → we charge $97/mo
- BrightData costs $500/mo → we charge $297/mo (we use stealth instead)
- Any API we can call and reformat

**Target:** Developers who want simplified APIs, businesses who want curated data
**Pricing:** 2-10x markup on upstream costs
**$ potential:** $0 - unlimited (scales with usage)
**Time to first $:** 1 day

---

### 2.4 Auto-Responder for Reviews

**What:** Monitor Google/Yelp/Facebook reviews. Auto-generate and post responses using AI.

**Pipeline:**
```
n8n cron (hourly)
  → scrape client's review pages
  → if new review → AI generates response (matches tone)
  → STEALTH: auto-post response (or manual approval)
```

**Target:** Local businesses, restaurants, dentists, doctors
**Pricing:** $97/mo for auto-response, $197/mo with manual review queue
**$ potential:** $500-2K/mo
**Time to first $:** 2 days

---

### 2.5 Newsletters-as-a-Service

**What:** Auto-generate and send industry-specific newsletters. AI curates + writes.

**Pipeline:**
```
n8n cron (weekly)
  → scrape 10-20 industry RSS feeds / news sites
  → AI summarizes top 5-10 stories
  → AI writes newsletter (matching client brand voice)
  → SendGrid sends to subscriber list
```

**Target:** Anyone with an email list (RE agents, lawyers, consultants)
**Pricing:** $197/mo for weekly newsletter
**$ potential:** $500-2K/mo
**Time to first $:** 1 day

---

### 2.6 YouTube Title/Description Optimizer

**What:** Scrape competitor YouTube channels. Analyze title patterns, keywords, tags. Generate optimized titles.

**Pipeline:**
```
Stealth browser → scrape YouTube search results
  → extract titles, tags, description patterns
  → AI analysis of what ranks
  → generate 10 optimized title options
```

**Target:** YouTubers, content creators, marketing agencies
**Pricing:** $47/mo for 10 analyses
**$ potential:** $300-1K/mo
**Time to first $:** 2 days

---

## 🔥 TIER 3: High Potential (1-2 week build)

### 3.1 Instagram Growth Automation

**What:** Auto-follow, auto-like, auto-comment based on hashtags/location. Grows accounts while client sleeps.

**Pipeline:**
```
Stealth browser → Instagram
  → target hashtags + locations
  → auto-like + follow (100-200/day)
  → intelligent auto-comment (AI generated, varied)
  → track follow-back rate
```

**Target:** Influencers, businesses, anyone wanting IG growth
**Pricing:** $147/mo for 3 months, $97/mo ongoing
**$ potential:** $1K-5K/mo
**Risk:** Medium (IG bans aggressive accounts)

---

### 3.2 SEO Rank Tracker

**What:** Track keyword rankings in Google. Report weekly.

**Pipeline:**
```
n8n cron (weekly)
  → stealth browser → Google search target keywords
  → check position of client website
  → track over time → weekly PDF report
```

**Target:** SEO agencies, businesses with websites
**Pricing:** $47/mo for 10 keywords, $97/mo for 50
**Our edge:** Stealth browser avoids Google's anti-automation
**$ potential:** $500-2K/mo
**Time to first $:** 3 days

---

### 3.3 The "Reverse 9-5" Machine

**What:** Monitor Upwork/Fiverr for gigs we can automate. Auto-bid. Auto-fulfill.

**Pipeline:**
```
Stealth browser → Upwork search "web scraping" "data entry" "research"
  → AI generates custom proposal
  → auto-submit bid
  → on win → auto-fulfill via our scraper
  → auto-deliver result
  → collect payment
```

**Target:** Demand on freelancer platforms
**Pricing:** Whatever the market bears ($50-500/gig)
**$ potential:** $1K-5K/mo
**Risk:** High (platform ToS, account bans)
**Time to first $:** 1 week

---

### 3.4 Podcast Show Notes Generator

**What:** Clients upload podcast audio. We transcribe + AI-generate show notes, timestamps, social posts.

**Pipeline:**
```
Client uploads MP3/webhook
  → audio transcription (Whisper or API)
  → AI generates: summary, key points, timestamps, social posts, SEO keywords
  → deliver as formatted doc
```

**Target:** Podcasters, content creators
**Pricing:** $9/episode or $47/mo for 8 episodes
**$ potential:** $500-2K/mo
**Time to first $:** 3 days

---

### 3.5 Review/Reputation Management (Grey)

**What:** Generate reviews for client businesses. Post from real-looking accounts.

**Pipeline:**
```
n8n → AI writes review text (matches client, varies per account)
  → stealth browser → login to Google/Yelp/FB account
  → post review with natural timing (1-2/day per account)
  → rotate accounts + proxies
```

**Target:** Businesses with poor reputation, new businesses
**Pricing:** $197/mo for 5 reviews/mo, $497/mo for 20
**$ potential:** $1K-5K/mo
**Risk:** High (platform bans, legal grey area)
**Time to first $:** 1 week

---

## 💣 BONUS: Darker Ideas (More Risk, More Reward)

These are higher risk. Platform bans, account losses, potential legal issues. But the money is real.

| Idea | Revenue Potential | Primary Risk | Execution |
|------|------------------|-------------|-----------|
| **Facebook Marketplace auto-list** - import product catalogs, auto-list across FB | $1K-3K/mo | FB bans | 3 days |
| **Craigslist/Kijiji ad blaster** - post 100s of ads for clients | $1K-5K/mo | Flagged accounts | 3 days |
| **Click/impression farm** - drive traffic to client sites | $500-2K/mo | Bot detection | 1 week |
| **Account farm** - create bulk accounts across platforms | $1K-5K/mo | Verification costs | 1 week |
| **App store review generator** - 5-star reviews for apps | $500-2K/mo | Apple/Google bans | 1 week |
| **Ticket scalping bot** - buy limited drops instantly | Varies wildly | Legal, ToS | 1 week |

---

## 📊 What We Should Build FIRST

Based on: **$0 startup** × **our existing stack** × **fastest to ship** × **highest demand**

| Rank | Project | Can Ship | Est. $/mo | Why First |
|------|---------|----------|-----------|-----------|
| 1 | **Local Business Lead Lists** | Today | $500-3K | Already have scraper + stealth |
| 2 | **Rental Lead Gen** | Today | $500-1.5K | Already works, n8n ready |
| 3 | **E-commerce Price Monitor** | Today | $500-2K | Workflow already built |
| 4 | **Newsletter-as-a-Service** | 1 day | $500-2K | SendGrid + AI = done |
| 5 | **Government Contract Alerts** | 2 days | $1K-5K | High value, low competition |
| 6 | **LinkedIn Connector Bot** | 3 days | $1K-5K | B2B pays well |
| 7 | **SEO Rank Tracker** | 3 days | $500-2K | Stealth = advantage |
| 8 | **Instagram Growth** | 3 days | $1K-5K | Huge demand |
| 9 | **Document Autopilot** | 1 day | $300-1K | PDF tools ready |
| 10 | **API Arbitrage** | 1 day | Unlimited | Pure automation |

---

## 🚀 The First 10 Customers (Who to Sell To)

| Project | Who to Sell To | Where to Find Them |
|---------|---------------|-------------------|
| Lead Lists | Marketing agencies, sales teams | LinkedIn, cold email |
| Rental Leads | Property managers | Kijiji listings, FB groups |
| Price Monitor | Amazon sellers, Shopify stores | Reddit (r/FulfillmentByAmazon), FB groups |
| Newsletters | RE agents, consultants, lawyers | LinkedIn |
| Gov Contracts | Government contractors | LinkedIn, industry associations |
| LinkedIn Bot | B2B sales teams | LinkedIn (meta) |
| SEO Tracker | SEO agencies, marketing directors | Reddit (r/SEO), LinkedIn |
| IG Growth | Influencers, local businesses | Instagram DMs |
| Document Auto | Accountants, logistics managers | LinkedIn, cold email |
| API Arbitrage | Developers | Dev.to, Reddit (r/webdev) |
