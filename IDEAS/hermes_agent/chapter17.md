---
created: 2026-07-03
type: reference
tags: [book, hermes, chapter]
chapter: 17
title: "Building the RE-AI MVP in 7-14 Days"
section: "Part II: The Real Estate Pivot (RE-AI)"
source: victoria-k-emails
---

# Chapter 17 — Building the RE-AI MVP in 7-14 Days

Alright—this is where we stop talking architecture and turn it into something you can actually ship. We’ll design a real MVP (minimum viable product) for a Real Estate AI Agent that you can build in ~7–14 days on top of your existing Hermes-style stack.

No fluff. Just the smallest system that actually creates value for realtors.

🏡 Real Estate AI Agent MVP (RE-AI v1)
🎯 MVP Goal
Automate the 3 highest-value realtor pain points:
⚡ Instant lead response (speed to lead)
🔁 Follow-up automation (most deals happen here)
📅 Showing + calendar coordination
Everything else is later.
🧠 1. MVP System Overview
You are building this:
Incoming Lead Sources
(Website / Email / SMS / Forms)
│
▼
Lead Intake Service
│
▼
RE-AI Orchestrator
│
┌──────────────┼──────────────┐
▼ ▼ ▼
Lead Reply CRM Update Calendar Booking
│ │ │
└──────────────┼──────────────┘
▼
Telegram Approval / Alerts

🧱 2. Tech Stack (Simple, Practical)
You already have most of this:
Core
Docker
Node.js or Python (either works)
Postgres (or Supabase)
Redis (optional but helpful)
Automation
n8n (you already installed this)
Telegram Bot API
AI Layer
OpenAI / Claude / OpenRouter
Simple “agent router” (NOT full Hermes yet)
Communication
Email (Gmail API)
SMS (Twilio recommended)
Telegram (control panel)
🧩 3. MVP Modules (ONLY 4)
We strip everything down:
🧲 MODULE 1: Lead Intake Service
Purpose:
Capture leads from anywhere.
Inputs:
website form
email inquiry
SMS
Facebook ads (later)
Output:
Normalized lead object:
{
"name": "John Smith",
"phone": "+1...",
"email": "...",
"message": "Is this house still available?",
"source": "website",
"timestamp": "..."
}

🧠 Implementation (simple)
Use:
n8n webhook OR simple API endpoint
Store into Postgres:
CREATE TABLE leads (
id SERIAL PRIMARY KEY,
name TEXT,
email TEXT,
phone TEXT,
message TEXT,
status TEXT DEFAULT 'new',
created_at TIMESTAMP
);

⚡ MODULE 2: Instant Response Agent (CRITICAL)
Purpose:
Respond to leads in <60 seconds.
This is where money is made.

Logic:
New lead arrives
→ AI classifies intent
→ Generate response
→ Send via email/SMS
→ Log interaction
→ Update CRM status

Example prompt behavior:
Lead:
“Is this still available?”
Agent reply:
“Yes it is. Are you looking to move in the next 1–3 months, or just exploring options?”
Then:
tag lead = “buyer”
stage = “new → engaged”
Tools needed:
LLM API
SMS/email sender
Postgres update
🔁 MODULE 3: Follow-Up Engine
Purpose:
Automatically follow up with leads until they respond or go cold.
Schedule:
Run via n8n cron:
Day 1: instant response
Day 2: follow-up
Day 5: soft check-in
Day 10: final nudge
Example follow-up messages:
Day 2:
“Just checking in—are you still looking for a home in this area?”
Day 5:
“I can send you a few updated listings if you’re still interested.”
Logic:
If lead.status != closed
AND no response in X days
→ send follow-up
→ log message

📅 MODULE 4: Calendar + Showing Scheduler
Purpose:
Turn interest into booked showings.
Flow:
Client asks for viewing
→ AI suggests times
→ checks Google Calendar
→ books event
→ sends confirmation

Rules:
never double-book
always confirm time
always send reminder
🧠 4. AI Brain (Simple Version)
You do NOT need full Hermes.
Just a single “agent router”:

Input → classify intent:
- inquiry
- scheduling
- follow-up
- general question

Then route:
→ response generator
→ calendar handler
→ CRM updater

🗃️ 5. Database (Minimal Schema)
Leads
id
name
email
phone
message
status (new / contacted / hot / cold / closed)
created_at
last_contacted

Interactions
id
lead_id
type (sms/email/call)
content
timestamp

Appointments
id
lead_id
datetime
location
status

🔌 6. n8n Workflows (CORE OF MVP)
You will build only 3 workflows:
Workflow 1: Lead Intake
Trigger:
webhook
Steps:
save lead
call AI
send response
notify Telegram
Workflow 2: Follow-Up Scheduler
Trigger:
cron (every day)
Steps:
query stale leads
generate follow-up message
send SMS/email
Workflow 3: Showing Scheduler
Trigger:
incoming message
Steps:
parse request
check calendar
propose times
book event
💬 7. Telegram Control Panel (VERY IMPORTANT)
You will control everything via Telegram:
Commands:

/leads → show hot leads
/followups → pending follow-ups
/today → schedule
/lead john → lead summary
🧠 8. What Makes This MVP Valuable
Even in this simple form:
It does 3 things better than most agents:
Responds instantly (most agents are slow)
Never forgets follow-ups (huge revenue impact)
Keeps calendar structured automatically
💰 9. Why This Works in Real Estate
Because real estate is:
speed sensitive
follow-up dependent
communication heavy
This MVP directly improves:
conversion rate
response time
deal volume
🚀 10. Build Order (VERY IMPORTANT)
Do NOT build everything at once.
Follow this order:

Day 1–2
Postgres schema
lead intake API
Day 3–4
instant response agent
Day 5–6
follow-up automation (n8n)
Day 7
calendar scheduling
Day 8+
Telegram control panel
⚠️ 11. What NOT to Build Yet
Avoid:
browser automation
multi-agent system
Obsidian memory layer
vector DB
MCP complexity
advanced Hermes orchestration
This is intentionally SIMPLE.
🧭 Final Result
You end up with:
A real-time AI assistant that captures leads, responds instantly, follows up automatically, and books showings. That alone can outperform most realtors’ manual workflows. If you want next step
I can take this further and give you:
exact n8n workflow JSON exports
full API code (Node or Python)
Telegram bot code
prompt templates for responses
CRM upgrade path
SaaS version architecture
Just say:
👉 “build the codebase”

On Fri, Jul 3, 2026 at 4:18 AM Victoria K <vkushelnyk@gmail.com> wrote:
