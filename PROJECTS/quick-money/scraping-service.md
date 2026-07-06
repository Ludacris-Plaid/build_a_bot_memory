# Web Scraping Service (On-Demand)

**Type:** One-off or recurring
**Price:** $97 one-time, $47/mo recurring
**Effort:** 2/5 | **Value:** $500-3k/mo | **Scalability:** ★★★★★

## Pipeline
```
Client POST → /webhook/scrape
  → validate URL
  → re-ai-scraper.py scrape (all 4 layers)
  → format output → email + HTTP response
```

## n8n Workflow
- **Name:** `Scraping Service (On-Demand)`
- **File:** `/root/buildabot/data/n8n/templates/scraping-service.json`
- **Webhook URL:** `https://outlets-result-cleaner-prove.trycloudflare.com/webhook/scrape`
- **Status:** Imported but inactive — activate per client

## Usage
```json
POST /webhook/scrape
{
  "url": "https://example.com",
  "format": "markdown",
  "hard_mode": false,
  "email": "client@example.com"
}
```

## Clients
- E-commerce stores wanting competitor pricing
- Real estate investors wanting MLS data
- Researchers needing bulk data extraction
- Marketing agencies wanting content analysis

## Branding
Results delivered via Indications Media themed emails.
