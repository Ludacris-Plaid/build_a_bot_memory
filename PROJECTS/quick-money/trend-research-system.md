# 🌡️ Trend Research System

> Find what's trending → figure out what to build → cash in.
> Updated daily via n8n cron.

---

## 🔌 Working APIs (Free, No Key)

### 1. Hacker News — Tech/Business Trends
**URL:** `https://hacker-news.firebaseio.com/v0/topstories.json`
**Returns:** IDs of top 500 stories
**Best for:** Tech, startup, business, programming trends
**How to use:**
```bash
# Get top story IDs
curl -s https://hacker-news.firebaseio.com/v0/topstories.json | python3 -c "import sys,json; ids=json.load(sys.stdin)[:10]; print(ids)"

# Get story details
curl -s https://hacker-news.firebaseio.com/v0/item/12345.json
```
**Limit:** 500 req/min (basically unlimited)

### 2. GitHub Trending — Dev Tool/Project Trends
**URL:** `https://github.com/trending`
**Best for:** What developers are building, what tools are hot
**How to use:** Scrape with User-Agent header
**Categories:** `?since=daily|weekly|monthly` + language filter

### 3. Reddit — Public Sentiment / Niche Trends
**URL:** `https://www.reddit.com/r/all/hot.json`
**Requires:** `User-Agent: Mozilla/5.0` header
**Best for:** What people are talking about in any niche
**Specific subreddits for trend spotting:**
- r/trendingsubreddits — trending communities
- r/all — everything popular
- r/Entrepreneur — business trends
- r/Startups — startup trends
- r/SaaS — SaaS ideas
- r/juststart — content/site trends
- r/FlutterDev — mobile dev trends
- r/webdev — web dev trends
- r/MachineLearning — AI/ML trends
- r/digital_marketing — marketing trends

### 4. GDELT Project — Global News Trends
**URL:** `https://api.gdeltproject.org/api/v2/doc/doc`
**Best for:** World events, industry trends, market shifts
**Query example:** `?query=[topic]&mode=artlist&format=json&maxrecords=10`
**Free:** Yes, no key needed

### 5. YouTube Trending
**URL:** `https://www.youtube.com/feed/trending`
**Best for:** Video content trends, what niches are growing
**How to use:** Scrape with browser/stealth (needs JS)

---

## 🔑 APIs (Free Tier, Need Signup)

| API | Free Tier | What It Gives | Signup URL |
|-----|-----------|--------------|-----------|
| **SerpAPI** | 100 searches/mo | Google Trends, search results, trending | serpapi.com |
| **Twitter/X API v2** | 500K tweets/mo | Trending topics, hashtags, keywords | developer.twitter.com |
| **YouTube Data API** | 10K units/day | Trending videos, search trends | console.cloud.google.com |
| **Reddit API** | 600 req/min | Hot posts, trending subreddits | reddit.com/prefs/apps |
| **Product Hunt API** | Rate limited | Trending products, launches | api.producthunt.com |
| **Amazon Product API** | Varies | Best sellers, trending products | affiliate-program.amazon.com |

---

## 🛠️ Built-in Script — `trend-scanner.py`

Location: `/root/buildabot/scripts/trend-scanner.py`

What it does:
- Fetches HN top stories → extracts topics
- Fetches Reddit hot → extracts trending themes
- Fetches GitHub trending → extracts tool trends
- Fetches GDELT → extracts news trends
- Summarizes everything into: **"Here's what's hot right now"**
- Saves to Obsidian: `PROJECTS/quick-money/trending-now.md`

**Usage:** `python3 /root/buildabot/scripts/trend-scanner.py`

---

## 🧠 Manual Trend Hunting (What to Watch)

### Watch These for Product Ideas

| Source | What to Look For | Why |
|--------|-----------------|-----|
| **r/SaaS** | "What problem should I solve?" posts | See what people will pay for |
| **r/Entrepreneur** | "I need a tool that does X" | Direct demand |
| **r/smallbusiness** | Business pain points | Easy software fixes |
| **Hacker News "Ask HN"** | "What tools do you wish existed?" | Goldmine for ideas |
| **Product Hunt launches** | What's getting funded/bought | Validate market |
| **AppSumo deals** | What software is selling | Shows demand |
| **Gumroad top sellers** | What people actually pay for | Shows price points |
| **X/Twitter trends** | What niches are growing | Early signals |
| **Google Trends** | Search volume growth | Raw demand data |

### Niche Signals (Where to Look for Opportunities)

| Niche | Signal | Look For |
|-------|--------|---------|
| Real Estate | Zillow/Redfin changes | API changes, new features |
| E-commerce | Amazon seller tools | Price wars, tracking needs |
| Marketing | HubSpot/ActiveCampaign updates | New integration needs |
| SEO | Google algorithm updates | New ranking factor tools |
| AI | New model releases | Wrapper/API opportunities |
| Content | Creator economy tools | Automation needs |
| Local biz | Google Maps updates | Data extraction needs |
| Legal | Court case databases | Public records access |
| Medical | Health data portals | Aggregation opportunities |
| Education | Online learning platforms | Data extraction needs |

---

## 📋 Weekly Trend Report (Automated)

The n8n cron job `trend-scanner` runs every Monday at 9am:
1. Scrape HN top 30 stories
2. Scrape GitHub trending (weekly)
3. Scrape Reddit r/all hot
4. AI summarizes: "3 things trending this week"
5. Saves to Obsidian
6. Option: email to us

---

## 🚀 Next Steps

1. [ ] Create `trend-scanner.py` script
2. [ ] Set up n8n weekly trend report
3. [ ] Sign up for SerpAPI free tier (Google Trends)
4. [ ] Sign up for Twitter/X API free tier
5. [ ] Start watching r/SaaS + r/Entrepreneur daily
