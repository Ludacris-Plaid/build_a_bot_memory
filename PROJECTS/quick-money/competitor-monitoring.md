# Competitor Monitoring Service

**Type:** Monthly subscription
**Price:** $97/mo (5 URLs), $297/mo (20 URLs)
**Effort:** 2/5 | **Value:** $300-1.5k/mo | **Scalability:** ★★★★

## Pipeline
```
n8n cron (daily at 6am)
  → scrape target URLs
  → hash content → compare with stored hash
  → if changed → AI summary → email alert
```

## n8n Workflow
- **Name:** `Competitor Monitor (Daily)`
- **File:** `/root/buildabot/data/n8n/templates/competitor-monitor.json`
- **Status:** Imported but inactive

## Target Market
- Any business with online competitors
- E-commerce stores tracking pricing changes
- SaaS companies monitoring feature announcements
- Marketing agencies tracking client competitors

## Brand
All alerts use Indications Media theme + footer.
