---
created: 2026-07-03
type: reference
tags: [book, hermes, chapter]
chapter: 10
title: "Making It Run on Its Own — Automation, Scheduling, and Background Agents"
section: "Part I: Building the Personal AI Operating System"
source: victoria-k-emails
---

# Chapter 10 — Making It Run on Its Own — Automation, Scheduling, and Background Agents

“An assistant that only responds is useful. An assistant that acts on its own schedule becomes infrastructure.”
Up to this point, Hermes is powerful—but still fundamentally reactive:
You ask → it responds
You trigger → it acts
That’s not an operating system yet.
An operating system has processes running in the background, even when you’re not actively using it.

This chapter introduces that layer.

10.1 What We Are Building Now
We are adding autonomous background execution:
Hermes Agent
│
Automation Scheduler
│
┌───────────────┼────────────────┐
▼ ▼ ▼
Cron Jobs Event Triggers Workflow Engine
▼ ▼ ▼
Reports Monitoring Actions (MCP tools)

Hermes will now:
run tasks on a schedule
monitor systems continuously
generate reports automatically
react to external events
trigger workflows without being asked
10.2 Two Types of Automation
We separate automation into two categories:
1. Scheduled Automation (Predictable)
Runs at fixed intervals:
every hour
daily
weekly
monthly
Examples:
daily email summary
weekly project report
system health checks
2. Event-Based Automation (Reactive)
Runs when something happens:
email received
message sent on Telegram
file updated
API event triggered
Examples:
new email → classify + draft reply
GitHub PR → review code
server error → notify Telegram
10.3 Introducing n8n (Workflow Engine)
We use:
n8n
Why:
visual workflow builder
supports webhooks
supports cron schedules
integrates with APIs easily
self-hostable on VPS
works well with MCP tools
10.4 Installing n8n
Inside your server:
mkdir -p ~/ai-os/compose/n8n
cd ~/ai-os/compose/n8n

Create Docker Compose file:
version: "3.9"

services:
n8n:
image: n8nio/n8n:latest
restart: unless-stopped
ports:
- "5678:5678"
environment:
- TZ=America/Edmonton
- N8N_BASIC_AUTH_ACTIVE=true
- N8N_BASIC_AUTH_USER=admin
- N8N_BASIC_AUTH_PASSWORD=change_this
volumes:
- ../../data/n8n:/home/node/.n8n
networks:
- ai-network

networks:
ai-network:
external: true

Start it:
docker compose up -d

Access:
http://YOUR_VPS_IP:5678

10.5 First Workflow: Daily System Report
We build your first automation.
Goal:
Every morning Hermes generates a report:
system health
inbox summary
calendar overview
active projects
pending tasks
Workflow Steps:
Cron trigger (8:00 AM)
Call Hermes MCP tool:
gather system data
Summarize results
Store in Obsidian
Send Telegram message
10.6 Cron Scheduling Concept
n8n uses cron expressions:
0 8 * * *

Meaning:
Every day at 08:00
We will use this pattern constantly.
10.7 Event-Driven Automation
Now we connect real-time triggers.
Example:

Gmail → n8n → Hermes
Flow:
New email arrives
↓
Webhook trigger
↓
n8n workflow starts
↓
Hermes classifies email
↓
Stores in memory
↓
Optional: draft reply
↓
Telegram notification

10.8 Telegram as Control Panel
Telegram becomes your:
approval system
notification system
emergency interface
remote control panel
Example:
Hermes:
"New email requires response.
Draft:
'Thanks, I will review this today.'
Approve?"

[Approve] [Edit] [Reject]

10.9 Background Agent Pattern
We define a key concept:
“Always-on workers”
Instead of one big AI, we run multiple small processes:
Worker Purpose
Email Worker inbox processing
Calendar Worker scheduling
System Worker monitoring
Research Worker web ingestion
Memory Worker summarization

Each runs independently.
10.10 System Monitoring Agent
We add a continuous system observer:
Every 5–10 minutes:

CPU usage
RAM usage
disk space
container health
failed services
If something breaks:
→ Telegram alert

10.11 Memory Automation Pipeline
We now automate memory creation:
New conversation or event
↓
Summarize
↓
Extract key insights
↓
Write Markdown note
↓
Embed into Qdrant
↓
Store in Obsidian

No manual note-taking required.
10.12 Scheduled Research Agent
Once per day:
Hermes will:

browse selected topics
update knowledge base
track changes in tools
summarize updates
Example:
“What changed in AI agent frameworks today?”
10.13 Workflow Reliability Design
Every workflow must include:
retry logic
timeout limits
failure notifications
logging
We never assume automation always works.
We design for failure.

10.14 Avoiding Automation Chaos
A critical rule:
Never let multiple workflows modify the same system state without coordination.
We avoid:
duplicate email replies
conflicting calendar events
repeated API calls
memory duplication
We introduce:
locking
deduplication
idempotent operations
10.15 Logging Everything
We expand logging:
logs/
workflows/
cron/
triggers/
failures/

Each entry includes:
trigger source
execution steps
outcome
duration
errors (if any)
10.16 First End-to-End Autonomous System
After this chapter, your system can:
Every morning:

check system health
summarize inbox
review calendar
update memory
send you a report
Without you asking.
This is the first true autonomous layer of your AI OS.

10.17 What We Are NOT Doing Yet
We still avoid:
full autonomous email sending without approval
autonomous purchases
uncontrolled API usage
long-running web scraping loops
multi-agent self-replication
Those come later with stricter governance.
10.18 Why This Chapter Matters
Before this chapter:
Hermes was reactive
After this chapter:
Hermes becomes proactive
That shift is fundamental.
You are no longer “using an AI.”

You are now running an AI system in the background of your life.

End of Chapter 10
Your AI operating system now has:
reasoning (Hermes)
memory (Obsidian + Qdrant)
tools (MCP)
real-world integration (email, Telegram, calendar)
web access (Playwright)
and now automation (n8n + scheduled agents)
What’s Next
Chapter 11 is where we take a major leap:
We will build OpenHands-style autonomous coding capability:

repository understanding
automated debugging
code generation pipelines
test execution loops
pull request creation
self-healing software workflows
This is where Hermes stops just assisting development…
and starts becoming a software engineer inside your system.

On Fri, Jul 3, 2026 at 4:12 AM Victoria K <vkushelnyk@gmail.com> wrote:
