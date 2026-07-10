# Buildabot — Pricing Model & Projections

## DeepSeek V4 Flash Costs

| Category | $/M tokens |
|----------|-----------|
| Input (cache hit) | $0.0028 |
| Input (cache miss) | $0.14 |
| Output | $0.28 |
| **Blended** (60% cache, 70/30 in/out split) | **~$0.13/M** |

A typical client conversation (10 msg) ≈ $0.0015 in API cost.

---

## Pricing Package

### Setup Fees (One-Time)

| Tier | Fee | Covers |
|------|-----|--------|
| Standard | $399 | Bot config, deploy, domain, 1 integration |
| Premium | $799 | Standard + branding, voice, 3 integrations |
| Enterprise | $1,999 | Multi-agent, custom infra, training, SLA |

### Monthly Packages

| | Lite | Regular | Heavy |
|---|---|---|---|
| **Price** | $97/mo | $297/mo | $597/mo |
| **Tokens incl.** | 1M | 5M | 20M |
| **~Conv/mo** | 80 | 400 | 1,600 |
| **DS cost** | $0.13 | $0.65 | $2.60 |
| **Gross margin** | **$96.87** | **$296.35** | **$594.40** |
| **Overage** | $1.50/M | $1.00/M | $0.75/M |

---

## Projections

### Scenario A: Conservative — 5 clients/mo first year

| Month | New Clients | Total Clients | Mix | Setup Rev | MRR | Total Rev |
|------|------------|--------------|-----|-----------|-----|-----------|
| 1 | 3 | 3 | 2 Lite, 1 Regular | $1,197 | $491 | **$1,688** |
| 2 | 2 | 5 | 3 Lite, 2 Regular | $798 | $885 | **$1,683** |
| 3 | 3 | 8 | 5 Lite, 3 Regular | $1,197 | $1,376 | **$2,573** |
| 6 | 3 | 17 | 10 Lite, 6 Regular, 1 Heavy | $1,197 | $3,169 | **$4,366** |
| 12 | 5 | 35 | 20 Lite, 12 Regular, 3 Heavy | $1,995 | $7,355 | **$9,350** |

**Year 1 total:** ~$62K revenue, ~$60K profit (DeepSeek cost < $50/mo)

### Scenario B: Moderate — 8 clients/mo

| Month | Clients | Mix | Setup Rev | MRR | Total Rev |
|------|--------|-----|-----------|-----|-----------|
| 1 | 5 | 3L, 2R | $1,995 | $885 | $2,880 |
| 3 | 17 | 9L, 6R, 2H | $2,792 | $3,893 | $6,685 |
| 6 | 38 | 20L, 14R, 4H | $2,792 | $8,190 | $10,982 |
| 12 | 65 | 35L, 23R, 7H | $3,590 | $14,075 | **$17,665/mo** |

**Year 1 total:** ~$135K revenue, DeepSeek cost ~$200 total

### Scenario C: Aggressive — 15 clients/mo (with VA/outsourcing)

| Month | Clients | Mix | Setup Rev | MRR | Total Rev |
|------|--------|-----|-----------|-----|-----------|
| 1 | 10 | 6L, 3R, 1H | $3,990 | $2,070 | $6,060 |
| 3 | 35 | 20L, 12R, 3H | $4,788 | $7,355 | $12,143 |
| 6 | 70 | 38L, 24R, 8H | $4,788 | $15,446 | $20,234 |
| 12 | 120 | 65L, 42R, 13H | $5,586 | $26,160 | **$31,746/mo** |

**Year 1 total:** ~$255K revenue

---

## Key Numbers

| Metric | Value |
|--------|-------|
| Client acquisition cost (your time) | 2-5 hrs @ ~$50-100/hr |
| Per-client server cost (shared infra) | ~$2-5/mo |
| DeepSeek cost per Heavy client (20M tokens) | $2.60/mo |
| Break-even clients (server costs) | 1 client on Lite |
| MRR at 35 clients (moderate year 1) | $7,355/mo |
| MRR at 65 clients (moderate year 2 month 1) | $14,075/mo |
| CAKE number — $/client/mo | $217 avg |
| **Effective setup fee + 4 months MRR** | **~$1,267/client** |

---

## Margin Reality Check

Heavy client pays $597/mo, costs you $2.60 in API + ~$3 in infra.

**Margin: 99.1%.**

Even after support time, payment processing (2.9%), and your own server, you're above 90% on every client past month one.
