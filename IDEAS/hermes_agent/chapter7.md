---
created: 2026-07-03
type: reference
tags: [book, hermes, chapter]
chapter: 7
title: "Tooling the Agent — Introducing MCP and External Capabilities"
section: "Part I: Building the Personal AI Operating System"
source: victoria-k-emails
---

# Chapter 7 — Tooling the Agent — Introducing MCP and External Capabilities

“Memory makes an AI informed. Tools make it useful.”
At this point, Hermes can:
Run on your VPS
Talk to you
Use a model backend
Store structured memory in Obsidian + Qdrant
But there’s a hard limitation:
👉 It still cannot reliably do things in the world.

It can reason about your Git repo…
but it cannot safely operate Git.

It can suggest email replies…
but it cannot send them.

It can describe a Docker fix…
but it cannot execute it.

This chapter fixes that.

We introduce MCP (Model Context Protocol) as the standardized tool layer between Hermes and the real world.

7.1 What MCP Actually Is
MCP is a tool interface layer for AI agents.
Instead of hardcoding integrations like:

“write a Gmail plugin”
“write a GitHub plugin”
“write a filesystem tool”
“write a database connector”
You instead plug everything into one standard:
Hermes
↓
MCP Client
↓
MCP Servers (tools)
↓
Real systems (Git, FS, DB, APIs)

Each tool becomes a small independent service.
7.2 Why MCP Is Critical
Without MCP, every integration becomes custom code.
That leads to:

messy architecture
duplicated logic
security issues
fragile integrations
With MCP:
every tool follows the same interface
tools are interchangeable
permissions are centralized
new capabilities plug in instantly
This is what makes your system scalable beyond 10–20 tools.
7.3 The Tool Philosophy
We are NOT building:
a chatbot with plugins
We ARE building:
a general-purpose agent runtime with a tool ecosystem
Think of MCP as:
“USB ports for intelligence”
You can plug anything in.
Unplug it anytime.

7.4 Core Tool Categories
We will eventually connect Hermes to:
File System Tools
read/write files
search directories
edit codebases
Developer Tools
Git
GitHub
CI/CD triggers
Docker
Data Tools
PostgreSQL
Qdrant
Redis
Communication Tools
Email (Gmail API)
Telegram bot
Slack (optional)
Automation Tools
n8n workflows
scheduled tasks
cron jobs
Research Tools
web search
documentation lookup
scraping (Playwright)
7.5 MCP Architecture Overview
Hermes Agent
│
MCP Client Layer
│
┌───────────────┼────────────────┐
▼ ▼ ▼
Filesystem GitHub PostgreSQL
▼ ▼ ▼
Local files Repos Structured data

Each MCP server is:
independent
sandboxed
replaceable
restartable
auditable
7.6 Installing the MCP Host Layer
We now extend your ai-os stack.
Inside:

~/ai-os/compose/mcp/

We will eventually run multiple MCP servers as containers.
But first, create the structure:

mkdir -p ~/ai-os/compose/mcp
mkdir -p ~/ai-os/services/mcp

7.7 MCP Security Model
This is important.
MCP servers must NEVER:

run as root
have unrestricted filesystem access
expose public ports directly
store secrets unencrypted
Instead:
run in Docker
connect only to Hermes internally
expose minimal API surface
use explicit permission rules
7.8 Filesystem MCP (First Tool)
We start simple: filesystem access.
Why?

Because everything Hermes does eventually touches files.

This MCP server allows:

reading project files
writing notes
editing code
searching directories
But it will be sandboxed to:
~/ai-os/workspace

Nothing outside this folder.
7.9 Git MCP (Second Tool)
Next:
Git integration.

Capabilities:

status
commit
diff
branch
pull
push (requires approval)
This is what turns Hermes into a real coding assistant.
Without Git tools, it’s just writing suggestions.

With Git tools, it becomes a developer.

7.10 Database MCP (Third Tool)
We connect:
PostgreSQL
Qdrant
Redis (later)
This allows Hermes to:
query structured data
store memory efficiently
manage embeddings
track system state
7.11 Tool Permission System
We introduce a critical concept:
Tool permission levels
Level Meaning
read-only safe inspection
suggest can propose changes
draft can create outputs
execute can run actions (restricted)
admin never default

Example:
Hermes can READ emails
It can DRAFT replies
It cannot SEND without approval
7.12 MCP Client in Hermes
Hermes must be configured to:
discover MCP servers
list available tools
request execution
handle responses
log all tool calls
This creates a traceable chain of actions.
7.13 Tool Call Lifecycle
Every action follows this flow:
User request
↓
Hermes reasoning
↓
Select tool
↓
MCP call request
↓
Tool executes in sandbox
↓
Result returned
↓
Hermes continues reasoning

This is how agents become reliable instead of chaotic.
7.14 First Real Use Case
Once MCP is working, Hermes can:
“Open my AI project and fix the Docker Compose issue.”
Then:
Reads filesystem
Finds compose file
Detects misconfiguration
Proposes fix
Applies patch (if approved)
Runs container
Reports result
This is the first moment your system becomes agentic.
7.15 Logging Everything
Every tool call must be logged:
tool name
inputs
outputs
timestamps
success/failure
user approval status
Stored in:
~/ai-os/logs/mcp/

This is critical for debugging and trust.
7.16 Why MCP Beats Traditional Plugins
Old model:
each tool is custom code
tightly coupled to agent
hard to maintain
MCP model:
standardized protocol
tool isolation
easy swapping
scalable architecture
multi-agent compatibility
This is why modern agent systems are moving toward it.
7.17 What We Are NOT Doing Yet
We are NOT yet connecting:
Gmail
Telegram
Browser automation
Calendar
Voice
External APIs
Reason:
If we connect everything at once, debugging becomes impossible.

We build incrementally.

7.18 Verification Checklist
Before moving on:
MCP folder structure exists
filesystem tool restricted to workspace
Git operations are sandboxed
tool calls are logged
Hermes can list available tools
at least one tool executes successfully
permission system is enforced
If any of these fail, fix before continuing.
End of Chapter 7
You now have the missing piece that transforms Hermes from:
“an AI that talks”
into:
“an AI that acts”
But it is still isolated from your real workflows.
Right now it can:

read files
edit projects
manage code
But it cannot yet touch your life systems:
email
messaging
scheduling
external communication
What’s Next
Chapter 8 is where everything starts connecting.
We will integrate:

Gmail (email intelligence)
Telegram (real-time communication)
Calendar (time management)
Notification system (alerts + approvals)
This is the chapter where Hermes starts becoming a personal executive assistant, not just a developer tool. From this point forward, each chapter will dramatically increase how much of your real-world workload the system can handle.

On Fri, Jul 3, 2026 at 4:11 AM Victoria K <vkushelnyk@gmail.com> wrote:
