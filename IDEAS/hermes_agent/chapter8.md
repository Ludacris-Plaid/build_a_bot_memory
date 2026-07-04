---
created: 2026-07-03
type: reference
tags: [book, hermes, chapter]
chapter: 8
title: "Connecting Your Life — Email, Telegram, and Calendar Integration"
section: "Part I: Building the Personal AI Operating System"
source: victoria-k-emails
---

# Chapter 8 — Connecting Your Life — Email, Telegram, and Calendar Integration

“An AI agent becomes powerful when it stops living in isolation.”
At this point, Hermes can:
Reason
Use tools via MCP
Read and write files
Work inside your coding environment
But it still cannot interact with your actual day-to-day life. This chapter changes that.

We will connect Hermes to:

Email (Gmail API)
Telegram (real-time messaging)
Google Calendar (time management)
This is the moment your system stops being “a developer tool” and starts becoming a personal operations assistant.
8.1 The New Architecture Layer
We are adding a new layer to the system:
Hermes Agent
│
MCP Tool Layer
│
┌─────────────┼─────────────┐
▼ ▼ ▼
Email Telegram Calendar
(Gmail API) (Bot API) (Google API)

Each system becomes:
a tool
exposed through MCP
controlled with permissions
logged for auditability
8.2 Design Principle: Inbox ≠ Autonomy
We will NOT allow full autonomy yet.
Instead, we follow this rule:

Action Behavior
Read email Allowed
Summarize email Allowed
Draft reply Allowed
Send email Requires approval
Delete email Requires explicit approval
Schedule event Suggest + confirm

This prevents accidental actions from becoming irreversible problems.
8.3 Gmail Integration (Email Intelligence Layer)
Step 1 — Google Cloud Setup
Go to:
Google Cloud Console
Create a new project
Enable Gmail API
Create credentials:
OAuth client ID
Desktop or Web application
Download:
credentials.json

Store securely:
~/ai-os/secrets/gmail/

Step 2 — MCP Email Tool
We wrap Gmail inside an MCP server.
Capabilities:

list inbox
read emails
classify emails
draft responses
label emails
search history
We explicitly do NOT allow silent sending.
Step 3 — Email Workflow Logic
Hermes will process email like this:
New email arrives
↓
Classify intent
↓
┌──────────────┬──────────────┐
▼ ▼ ▼
Spam Informational Action Required
▼ ▼ ▼
Archive Summarize Draft reply
↓
Request approval

Step 4 — Email Memory Integration
Important emails are:
summarized
stored in Obsidian
embedded into Qdrant
This allows Hermes to later answer:
“What did that client say last month?”
8.4 Telegram Integration (Real-Time Interface)
Telegram becomes your live control channel.
You can:

send commands
receive alerts
approve actions
interact with Hermes remotely
Step 1 — Create Bot
In Telegram:
Open BotFather
Create bot
Save API token
Store:
~/ai-os/secrets/telegram/token.env

Step 2 — MCP Telegram Server
Capabilities:
receive messages
send responses
send alerts
request approvals
forward summaries
Step 3 — Notification System
Hermes uses Telegram for:
urgent emails
failed workflows
scheduled reminders
system alerts
“approval required” requests
Example:
Hermes:
"I found 3 emails requiring responses.
Draft replies ready.
Approve sending?"
[Approve] [Edit] [Reject]

8.5 Calendar Integration (Time Awareness Layer)
Without a calendar, AI assistants are blind to time.
We integrate Google Calendar.

Step 1 — Google Calendar API
Enable:
Google Calendar API
OAuth credentials
Store securely in:
~/ai-os/secrets/calendar/

Step 2 — MCP Calendar Tool
Capabilities:
list events
create events
reschedule events
detect conflicts
suggest time slots
Step 3 — Scheduling Intelligence
Hermes can now reason about time:
Example:

“Schedule a meeting with John next week.”
Flow:
Check availability
↓
Suggest slots
↓
Ask confirmation
↓
Create event

8.6 Unified Inbox Concept
We now define a key abstraction:
Everything is an “event stream.”
Source Type
Email messages
Telegram messages
Calendar time events
MCP tools actions
System logs alerts

Hermes treats all of these as inputs into one system.
8.7 Notification Layer
We introduce a central notification rule:
Hermes must notify you when:

action requires approval
system error occurs
email is high priority
task is completed
scheduled event is approaching
All notifications go through Telegram first.
Later we can expand to:

mobile push
email digests
desktop alerts
8.8 Action Approval System
We define three action levels:
Level 1 — Auto
Level 2 — Suggest + Wait
Level 3 — Require explicit approval

Examples:
Action Level
Read email 1
Summarize email 1
Draft reply 2
Send email 3
Create calendar event 2
Delete data 3

This prevents catastrophic automation mistakes.
8.9 Logging & Audit Trail
Every external action is logged:
logs/
email/
telegram/
calendar/
actions/

Each log includes:
input
decision
tool used
outcome
approval status
This is critical for debugging and trust.
8.10 First End-to-End Test
Once everything is connected:
Send yourself an email like:

“Can we meet next Tuesday at 3pm?”
Expected flow:
Gmail MCP detects email
Hermes reads and classifies it
Calendar MCP checks availability
Hermes drafts response
Telegram sends approval request
You approve
Email is sent
Calendar event is created (if needed)
Logs are stored
This is your first real-world autonomous workflow
8.11 What We Are NOT Doing Yet
We are NOT yet adding:
browser automation
voice control
full autonomous email sending
financial transactions
multi-agent systems
Reason:
We need stability before autonomy.

8.12 Why This Chapter Is a Turning Point
Before this chapter:
Hermes lived inside your server
After this chapter:
Hermes lives inside your life systems
It can now:
communicate with people
manage your schedule
process your inbox
notify you in real time
This is the point where it becomes a true personal assistant system, not just a technical tool. End of Chapter 8 You now have a working bridge between Hermes and your real-world communication channels.
It can:

read your messages
manage your time
draft responses
request approvals
keep everything synchronized
What’s Next
Chapter 9 is where things become significantly more powerful.
We will add:

browser automation (Playwright)
research agent capabilities
web scraping and structured extraction
document ingestion pipelines
real-time knowledge retrieval
This is where Hermes begins to understand and navigate the internet itself, not just your personal systems.

On Fri, Jul 3, 2026 at 4:11 AM Victoria K <vkushelnyk@gmail.com> wrote:
