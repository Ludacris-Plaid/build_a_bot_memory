---
created: 2026-07-03
type: reference
tags: [book, hermes, chapter]
chapter: 9
title: "Giving Hermes Eyes — Browser Automation and Web Intelligence"
section: "Part I: Building the Personal AI Operating System"
source: victoria-k-emails
---

# Chapter 9 — Giving Hermes Eyes — Browser Automation and Web Intelligence

“An agent that cannot see the web is operating blind in a world that lives online.”
At this point, Hermes can:
Read and write files
Use MCP tools
Manage email
Handle Telegram
Work with your calendar
Store and retrieve memory
But there is still a major gap.
It cannot reliably interact with the web itself.

This chapter fixes that by giving Hermes controlled browser access through automation.

9.1 Why Browser Access Matters
Almost everything you do lives on the web:
Research
Documentation
SaaS tools
Dashboards
GitHub browsing
APIs
Admin panels
Without browser access, Hermes must rely on:
APIs (limited)
manual copy/paste
or your instructions
With browser automation, Hermes can:
navigate websites
extract structured data
fill forms
download files
compare information across sources
perform research workflows
9.2 The Architecture Upgrade
We add a new tool layer:
Hermes Agent
│
MCP Tool Layer
│
┌───────────────┼────────────────┐
▼ ▼ ▼
Email Telegram Calendar
│
▼
Browser Automation (NEW)
│
▼
Web / SaaS / APIs / Dashboards

9.3 Choosing the Browser Engine
We use:
Playwright
Why:
modern automation framework
supports Chromium, Firefox, WebKit
stable headless mode
strong selector system
excellent for scraping and workflows
9.4 Installing Playwright on the VPS
Inside your VPS:
sudo apt update
sudo apt install -y nodejs npm

Install Playwright:
npm init -y
npm install playwright

Install browsers:
npx playwright install

Verify:
npx playwright test

9.5 Creating the Browser MCP Server
We wrap Playwright in an MCP server.
Location:

~/ai-os/services/mcp/browser/

Capabilities:
open page
click element
type text
extract content
screenshot page
download file
run structured scraping tasks
9.6 Browser Security Model
This is extremely important.
Hermes must NEVER have:

unrestricted browser access to your accounts
ability to bypass CAPTCHAs
access to password managers
uncontrolled session persistence
We enforce:
Rule Behavior
No saved credentials required login prompts
No hidden browsing all actions logged
Session isolation per-task browser instance
Screenshot logging every step traceable
Time limits prevents infinite loops

9.7 Browser Sandboxing
Each task runs in a fresh containerized session:
Task starts
↓
New browser instance
↓
Execute steps
↓
Capture logs + screenshots
↓
Destroy session

This prevents memory leaks and credential leakage.
9.8 First Capability: Web Navigation
Hermes can now:
“Go to GitHub and find repositories about AI memory systems.”
Flow:
Open browser
Navigate to GitHub
Search query
Filter results
Extract top repositories
Return structured summary
9.9 Structured Web Extraction
Instead of dumping raw HTML, we convert results into structured data:
Title
URL
Description
Stars
Last updated
Relevance score

This is critical for combining browser data with memory systems later.
9.10 Research Agent Workflow
We define a standard research pipeline:
User question
↓
Plan search strategy
↓
Open multiple pages
↓
Extract structured data
↓
Cross-check sources
↓
Summarize findings
↓
Store in memory

9.11 Example Use Case: Competitor Research
Prompt:
“Compare vector databases for AI agents.”
Hermes will:
search documentation sites
open product pages
extract features
compare pricing
summarize tradeoffs
store results in Obsidian
9.12 Screenshot-Based Verification
Hermes can capture screenshots at each step:
Step 1: homepage.png
Step 2: search_results.png
Step 3: details_page.png

This makes debugging deterministic.
9.13 Browser + MCP Integration
We expose Playwright through MCP:
Capabilities exposed:

navigate(url)
click(selector)
type(selector, text)
extract(selector)
screenshot()
evaluate(script)
Hermes calls these as tools.
9.14 Rate Limiting and Safety
To prevent abuse or runaway automation:
limit requests per minute
enforce max page visits per task
require confirmation for login actions
block sensitive domains if needed
9.15 Combining Browser + Memory
This is where things become powerful.
Example flow:

Hermes researches topic
Extracts structured data
Saves to Obsidian
Embeds into Qdrant
Future queries use that knowledge instantly
The web becomes a live ingestion pipeline for your brain system.
9.16 First Full Test
Try:
“Find the best frameworks for building AI agents in 2026 and summarize them.”
Expected:
browser opens multiple sources
extracts frameworks
compares capabilities
stores summary in memory
returns structured answer
9.17 What We Are NOT Doing Yet
We are NOT yet enabling:
autonomous login to sensitive accounts
scraping behind paywalls
CAPTCHA solving
continuous background browsing
financial transactions
These require stricter governance layers we will build later.
9.18 Why This Chapter Is Important
Before this chapter:
Hermes knew your system
Hermes knew your memory
Hermes knew your communication tools
After this chapter:
👉 Hermes can learn from the entire internet

This is what transforms it from:

assistant
into:
research + automation intelligence layer
End of Chapter 9
You now have a system that can:
think
remember
communicate
schedule
and explore the web
That combination is extremely powerful.
What’s Next
Chapter 10 is where we move into true automation engineering.
We will build:

scheduled workflows (cron + n8n)
background agents
recurring research tasks
automated reporting systems
self-updating memory pipelines
This is where Hermes stops being reactive…
…and starts running processes continuously in the background like a real operating system.

On Fri, Jul 3, 2026 at 4:12 AM Victoria K <vkushelnyk@gmail.com> wrote:
