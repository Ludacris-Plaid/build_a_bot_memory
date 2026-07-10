# Property Alert Service

**Type:** Recurring subscription
**Price:** $29-49/mo per alert
**Effort:** 2/5 | **Value:** $500-2k/mo | **Scalability:** ★★★★★

## Pipeline
```
n8n cron (daily at 8am)
  → re-ai-scraper.py scrape Zillow URL
  → Python filter (price, beds, baths)
  → SendGrid email with Amber/dark theme
```

## n8n Workflow
- **Name:** `Property Alert (Daily)`
- **File:** `/root/buildabot/data/n8n/templates/property-alert-daily.json`
- **Status:** Imported but inactive — activate per client

## Client Setup
1. Copy workflow for each client
2. Set their Zillow search URL, email, filter criteria
3. Set the cron schedule
4. Activate workflow

## Branding
All emails use Indications Media dark theme (#030806 + #f59e0b) with footer: "Built by **Indications Media**"

## Next
- [ ] Build simple landing page for signups
- [ ] Set up Stripe payment link
- [ ] Create client onboarding form (n8n webhook)
