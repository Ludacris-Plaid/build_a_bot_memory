Chapter 1

I'd be happy to. I also think we should do it properly instead of rushing
through it.
We'll write it as if it were a professional technical book that you can
actually build from. Every chapter will be detailed enough that you can
complete it before moving on to the next. By the end, you'll have a
production-ready AI operating system running on your own infrastructure.

The Personal AI Operating System
Building a Production-Grade Hermes Agent with Memory, Automation, and
Autonomous Coding
Author: ChatGPT (OpenAI) & You
Chapter 1
Designing Your Personal AI Operating System
"Before writing a single command, we need to decide what we're building."
One of the biggest mistakes people make is starting by installing software.
They install Docker.

Then Ollama.

Then Obsidian.

Then a vector database.

Then some random GitHub repository.

After a week they have twenty containers running that barely communicate
with one another.

Eventually they give up.

We're not going to do that.

Instead, we're going to design the system first.

What We're Actually Building
This is not a chatbot.
It is not an AI assistant.

It is not another wrapper around a language model.

We're building a personal AI operating system.

Think of it as hiring an extremely capable junior engineer, executive
assistant, researcher, and knowledge manager who works 24 hours a day.

The AI should become an extension of your mind.

It should remember what you're building.

It should know your current projects.

It should know your coding style.

It should remember conversations from months ago.

It should help finish software.

It should organize your life.

It should automate repetitive work.

Most importantly, it should continue improving alongside you.

Design Philosophy
Every major design decision in this book follows six principles.
Principle 1: Modularity
Every component should be replaceable.
If a better language model appears next month, you should swap it in
without rebuilding everything else.

If you decide to replace your vector database, nothing else should break.

Loose coupling keeps the system maintainable.

Principle 2: Local Ownership
Your knowledge belongs to you.
Your notes.

Your projects.

Your memories.

Your documents.

Whenever practical, store them in open formats like Markdown and Git
repositories rather than proprietary databases.

Principle 3: Human Approval for High-Risk Actions
The system can:
classify emails
summarize documents
draft replies
write code
organize notes
But before it:
sends an email
deletes files
pushes to production
spends money
grants permissions
=E2=80=A6it should ask for approval until you intentionally relax those saf=
eguards.
Principle 4: Long-Term Memory
Most AI assistants forget everything after the conversation ends.
Our system won't.

Every useful interaction becomes structured knowledge.

Over time, the AI develops a searchable memory of your work.

Principle 5: Automation Without Chaos
Automation is only useful if it's predictable.
Every automated workflow should be:

observable
logged
reversible
testable
If something goes wrong, you should be able to understand why.
Principle 6: Open Standards
Where possible, we'll use:
Docker
Git
Markdown
Model Context Protocol (MCP)
REST APIs
PostgreSQL
Open-source components
This makes the system easier to migrate and extend.
The High-Level Architecture
Imagine the system as five layers.
YOU
=E2=94=82
=E2=94=8C=E2=94=80=E2=94=80=E2=94=80=E2=94=80=E2=94=80=E2=94=80=E2=94=80=E2=
=94=80=E2=94=80=E2=94=80=E2=94=80=E2=94=B4=E2=94=80=E2=94=80=E2=94=80=E2=94=
=80=E2=94=80=E2=94=80=E2=94=80=E2=94=80=E2=94=80=E2=94=80=E2=94=80=E2=94=90
=E2=94=82 Voice =E2=80=A2 Chat =E2=80=A2 Web UI =E2=94=82
=E2=94=94=E2=94=80=E2=94=80=E2=94=80=E2=94=80=E2=94=80=E2=94=80=E2=94=80=E2=
=94=80=E2=94=80=E2=94=80=E2=94=80=E2=94=AC=E2=94=80=E2=94=80=E2=94=80=E2=94=
=80=E2=94=80=E2=94=80=E2=94=80=E2=94=80=E2=94=80=E2=94=80=E2=94=80=E2=94=98
=E2=94=82
Hermes Agent
=E2=94=82
=E2=94=8C=E2=94=80=E2=94=80=E2=94=80=E2=94=80=E2=94=80=E2=94=80=E2=94=80=E2=
=94=80=E2=94=80=E2=94=80=E2=94=80=E2=94=80=E2=94=80=E2=94=80=E2=94=80=E2=94=
=BC=E2=94=80=E2=94=80=E2=94=80=E2=94=80=E2=94=80=E2=94=80=E2=94=80=E2=94=80=
=E2=94=80=E2=94=80=E2=94=80=E2=94=80=E2=94=80=E2=94=80=E2=94=80=E2=94=80=E2=
=94=90
=E2=94=82 =E2=94=82 =E2=94=82
=E2=96=BC =E2=96=BC =E2=96=BC
Memory Tool Layer Reasoning
(Obsidian + (MCP Servers) (LLM)
Qdrant)
=E2=94=82 =E2=94=82
=E2=94=94=E2=94=80=E2=94=80=E2=94=80=E2=94=80=E2=94=80=E2=94=80=E2=94=80=E2=
=94=80=E2=94=80=E2=94=80=E2=94=80=E2=94=80=E2=94=80=E2=94=80=E2=94=80=E2=94=
=98
=E2=94=82
Your Digital Life

Each layer has a specific responsibility.
Layer 1 =E2=80=93 The User Interface
This is how you interact with the system.
Initially we'll use:

a web interface
a terminal
Telegram
Later we'll add:
voice
desktop notifications
mobile access
The interface is intentionally simple because intelligence belongs in the
backend.
Layer 2 =E2=80=93 Hermes Agent
Hermes acts as the orchestrator.
It doesn't just answer questions.

It decides:

which tools to use
when to retrieve memory
whether to search documentation
whether code needs to be executed
when to ask for clarification
Think of Hermes as the operating system's scheduler.
Layer 3 =E2=80=93 Memory
Memory is split into two parts.
Human-readable memory
Markdown files stored in Obsidian.
These contain:

project notes
meeting notes
ideas
documentation
journals
reference material
You can open and edit these yourself.
Machine-searchable memory
The same notes are embedded into a vector database.
This allows Hermes to search semantically rather than by exact keywords.

Example:

You ask:

"What database were we considering six months ago?"
Instead of searching filenames, Hermes retrieves notes based on meaning.
Layer 4 =E2=80=93 Tools
Hermes becomes useful because it can use tools.
Examples include:

Filesystem

Git

GitHub

Docker

Browser automation

Email

Telegram

Google Calendar

Databases

Shell commands

Each tool is isolated and permissioned.

Layer 5 =E2=80=93 Intelligence
The reasoning model is intentionally separate from everything else.
This means:

Hermes today.

Another model tomorrow.

Nothing else changes.

Choosing a Hosting Strategy
There are three realistic options.
Option A =E2=80=93 Cloud APIs
Examples:
OpenAI
Anthropic
Google
Together AI
OpenRouter
Pros:
best reasoning
no GPU costs
simple
Cons:
monthly API costs
internet required
Option B =E2=80=93 Local GPU Server
Pros:
complete privacy
no API fees
Cons:
expensive hardware
maintenance
power usage
Option C =E2=80=93 Hybrid (Recommended)
This book assumes a hybrid architecture.
Reasoning:

Cloud LLM

Memory:

Local

Automation:

Local

Code:

Local containers

Sensitive documents:

Local

This gives you strong performance while keeping control of your own data.

Why a VPS?
The VPS is the always-on backbone of the system.
It will:

host Hermes
expose secure endpoints
run scheduled jobs
store memory
connect to APIs
orchestrate automations
Your laptop can sleep; the AI keeps working.
Recommended VPS Specifications
For a production setup:
4=E2=80=938 vCPUs
16=E2=80=9332 GB RAM
200 GB SSD (or more if you expect many repositories and documents)
Ubuntu Server LTS
Daily snapshots or backups
Static IPv4 address
If you plan to run large local models, you'll eventually want a
GPU-equipped machine or dedicated GPU provider, but you can begin with
API-hosted models.
Naming Your Infrastructure
Use clear, consistent names from day one.
For example:

ai.example.com =E2=80=93 Main interface
api.example.com =E2=80=93 Backend APIs
n8n.example.com =E2=80=93 Workflow automation
obsidian-sync =E2=80=93 Knowledge repository
qdrant =E2=80=93 Vector database
postgres =E2=80=93 Application database
A naming convention pays off as the system grows.
Security Starts Now
Before installing anything, decide on a few rules:
Use SSH keys instead of passwords.
Create a non-root administrative user.
Enable automatic security updates.
Keep secrets in a dedicated secrets manager or encrypted environment files.
Expose only the services that need to be reachable from the internet.
Put everything else on an internal Docker network.
These habits are much easier to establish now than to retrofit later.
The Development Workflow
Every change to your AI operating system should follow a simple cycle:
Write or modify configuration.
Commit it to Git.
Test it in a development environment.
Deploy it to the VPS.
Verify logs and health checks.
Back up important state.
Treat your AI infrastructure like a software project, because that's
exactly what it is.
What We'll Build Next
In the next chapter we'll leave the whiteboard and start assembling the
infrastructure.
By the end of Chapter 2 you'll have:

Chosen a VPS provider.
Registered (or reused) a domain name.
Installed Ubuntu Server.
Hardened SSH access.
Configured the firewall.
Enabled automatic security updates.
Prepared the server for Docker and the rest of the stack.
From that point onward, every chapter will add a working component until
the entire AI operating system comes together.
End of Chapter 1
This chapter serves as the blueprint. We now know what we're building, why
each component exists, and the principles that will guide every technical
decision in the chapters that follow.


On Fri, Jul 3, 2026 at 4:04=E2=80=AFAM Victoria K <vkushelnyk@gmail.com> wr=
ote:

> What you're describing is essentially a personal AI operating system, not
> just a chatbot.
> The goal is to build an agent that can:
>
> Manage email autonomously
> Respond on Telegram
> Organize your notes and knowledge
> Write software
> Continue long-term coding projects
> Search the web
> Remember previous conversations
> Schedule tasks
> Interface with your computer
> Chain together multiple tools automatically
> Learn your preferences over time
> This is absolutely possible today, although no single project does all of
> it perfectly. The best systems combine several open-source projects rathe=
r
> than relying on one "AI agent."
> The Architecture
> I would build it like this.
> You
> =E2=94=82
> =E2=94=82
> Voice / Telegram / Desktop
> =E2=94=82
> =E2=96=BC
> Hermes (Main Reasoning LLM)
> =E2=94=82
> =E2=94=8C=E2=94=80=E2=94=80=E2=94=80=E2=94=80=E2=94=80=E2=94=80=E2=94=80=
=E2=94=80=E2=94=80=E2=94=80=E2=94=80=E2=94=80=E2=94=80=E2=94=80=E2=94=80=E2=
=94=BC=E2=94=80=E2=94=80=E2=94=80=E2=94=80=E2=94=80=E2=94=80=E2=94=80=E2=94=
=80=E2=94=80=E2=94=80=E2=94=80=E2=94=80=E2=94=80=E2=94=80=E2=94=80=E2=94=80=
=E2=94=80=E2=94=80=E2=94=90
> =E2=94=82 =E2=94=82 =E2=94=82
> =E2=96=BC =E2=96=BC =E2=96=BC
> Memory Agent Runtime Tool Calling
> (Obsidian) (OpenHands) MCP Servers
> =E2=94=82 =E2=94=82 =E2=94=82
> =E2=94=82 =E2=94=82 =E2=94=82
> =E2=96=BC =E2=96=BC =E2=96=BC
> Notes Coding Projects Gmail
> Knowledge Python Telegram
> Tasks GitHub Calendar
> Ideas Docker Browser
>
> The Brain
> Hermes should be the reasoning model.
> Current recommendations:
>
> Hermes 3 405B
> Hermes 4 when stable
> Qwen3 235B
> DeepSeek R1
> Kimi K2
> Hermes has excellent tool calling and personality.
> Run through:
>
> Ollama (easy)
> vLLM
> llama.cpp
> OpenRouter
> Together AI
> If you have GPUs:
> Use vLLM.
>
> If you don't:
>
> Use OpenRouter.
>
> Long-Term Memory
> This is where Obsidian comes in.
> Instead of keeping memory inside the LLM, every important interaction
> becomes markdown.
>
> Example:
>
> Memory/
>
> Projects/
>
> Life/
>
> Programming/
>
> Business/
>
> Ideas/
>
> People/
>
> Meetings/
>
> Research/
>
> Each file:
> Programming/
> Hermes Agent.md
>
> Business/
> Startup Ideas.md
>
> Projects/
> Discord Bot.md
>
>
> Hermes constantly writes notes into Obsidian.
> Example
>
> ## Learned today
>
> User prefers Rust.
>
> Current project
>
> Agent framework
>
> Problems
>
> Telegram API failing
>
> Then the memory system retrieves relevant notes before every conversation=
.
> That is effectively infinite memory.
>
> Vector Database
> Obsidian alone isn't enough.
> Use embeddings.
>
> Choices:
>
> Chroma
> Qdrant
> Weaviate
> LanceDB
> I recommend
> Qdrant
>
> Pipeline:
>
> Obsidian Markdown
>
> =E2=86=93
>
> Chunk files
>
> =E2=86=93
>
> Embedding Model
>
> =E2=86=93
>
> Qdrant
>
> =E2=86=93
>
> Semantic Search
>
> =E2=86=93
>
> Hermes
>
> Now Hermes remembers everything.
> Agent Runtime
> This is the most important component.
> I'd recommend:
>
> OpenHands
> Excellent coding agent.
> Can:
>
> modify code
> run tests
> execute terminals
> debug
> Git
> Docker
> Alternative
> Claude Code
>
> Still arguably the strongest coding workflow, though it's not fully open
> source.
>
> For local:
> OpenHands + Hermes
>
> MCP (Model Context Protocol)
> MCP is becoming the standard way for LLMs to use tools.
> Instead of hardcoding Gmail, Telegram, GitHub, etc., Hermes connects to
> MCP servers.
>
> Examples:
>
> Filesystem
>
> GitHub
>
> Git
>
> Docker
>
> SQLite
>
> Postgres
>
> Browser
>
> Slack
>
> Discord
>
> Telegram
>
> Email
>
> Google Drive
>
> Calendar
>
> Obsidian
>
> Notion
>
> Spotify
>
> Weather
>
> Search
>
> ArXiv
>
> Wikipedia
>
> GitLab
>
> AWS
>
> Azure
>
> Kubernetes
>
> Literally hundreds now exist.
>
> Email Automation
> Gmail API.
> Workflow
>
> Unread email
>
> =E2=86=93
>
> Hermes reads
>
> =E2=86=93
>
> Classify
>
> =E2=86=93
>
> If advertisement
>
> Archive
>
> =E2=86=93
>
> If invoice
>
> Move to Finance
>
> =E2=86=93
>
> If GitHub notification
>
> Project folder
>
> =E2=86=93
>
> If personal
>
> Notify you
>
> =E2=86=93
>
> If simple response
>
> Draft reply
>
> =E2=86=93
>
> If urgent
>
> Telegram notification
>
> Never allow automatic sending initially.
> Only drafts.
>
> Telegram
> Telegram Bot API.
> Hermes can:
>
> Read messages
>
> Summarize
>
> Reply
>
> Schedule
>
> Forward
>
> Translate
>
> Answer FAQs
>
> Example
>
> Friend:
>
> "Coming tonight?"
>
> Hermes:
>
> "I'm finishing work right now. I'll let you know in about an hour."
>
> You approve.
>
> Eventually:
>
> Automatic approval for trusted contacts.
>
> Calendar
> Google Calendar API.
> Hermes can
>
> Schedule
>
> Reschedule
>
> Find conflicts
>
> Estimate travel
>
> Create reminders
>
> Coding Assistant
> OpenHands.
> Capabilities:
>
> Open project
>
> Read files
>
> Understand architecture
>
> Write code
>
> Run tests
>
> Fix errors
>
> Commit changes
>
> Open pull requests
>
> This is probably the strongest coding setup today.
>
> Browser Automation
> Playwright.
> Hermes can
>
> Fill forms
>
> Download files
>
> Research
>
> Compare prices
>
> Read dashboards
>
> Navigate websites
>
> Scrape information
>
> Voice
> Use
> Whisper
>
> or
>
> Whisper.cpp
>
> Speech
>
> =E2=86=93
>
> Text
>
> =E2=86=93
>
> Hermes
>
> =E2=86=93
>
> ElevenLabs
>
> or
>
> Piper
>
> =E2=86=93
>
> Voice
>
> Task Manager
> Instead of ChatGPT Tasks.
> Use
>
> Todo.md
>
> Projects.md
>
> Waiting.md
>
> Ideas.md
>
> Hermes updates them automatically.
> Daily Journal
> Automatically generated.
> Today
>
> Emails answered
>
> Projects worked
>
> Ideas
>
> Meetings
>
> Expenses
>
> Health
>
> Mood
>
> Tomorrow
>
> Stored in Obsidian.
> Project Memory
> Every coding project gets
> README
>
> Architecture
>
> Progress
>
> Problems
>
> TODO
>
> Ideas
>
> Files changed
>
> Hermes updates automatically.
> GitHub Integration
> Hermes can
> Clone repos
>
> Commit
>
> Push
>
> Review PRs
>
> Write documentation
>
> Generate issues
>
> Read Discussions
>
> Explain code
>
> Research Mode
> Use multiple search providers.
> Perplexity
>
> Tavily
>
> Brave Search
>
> SerpAPI
>
> Wikipedia
>
> ArXiv
>
> GitHub
>
> Then summarize.
>
> Local Execution
> Docker.
> Every coding task runs in isolated containers.
>
> Never let Hermes execute directly on your host.
>
> Security
> Separate permissions.
> Hermes should ask before:
>
> Deleting files
>
> Sending emails
>
> Purchasing anything
>
> Git push
>
> SSH
>
> Database deletion
>
> Everything else can be autonomous.
>
> Memory Pipeline
> Conversation
>
> =E2=86=93
>
> Summarize
>
> =E2=86=93
>
> Extract facts
>
> =E2=86=93
>
> Save markdown
>
> =E2=86=93
>
> Embed
>
> =E2=86=93
>
> Store Qdrant
>
> =E2=86=93
>
> Retrieve later
>
> =E2=86=93
>
> Inject into prompt
>
> This becomes lifelong memory.
> Knowledge Graph
> Better than plain notes.
> Store relationships.
>
> Example
>
> John
>
> works at
>
> OpenAI
>
> John
>
> likes
>
> Rust
>
> Rust
>
> used in
>
> Current Project
>
> Use a graph database like Neo4j if you want rich relationship queries, or
> keep it simpler by linking markdown notes in Obsidian.
> Suggested Technology Stack
> Layer Recommendation
> LLM Hermes 3/4 or Qwen3
> Memory Obsidian
> Semantic Search Qdrant
> Embeddings BAAI bge-m3 or nomic-embed-text
> Coding Agent OpenHands
> Workflow Automation n8n
> Tool Protocol MCP
> Browser Automation Playwright
> Email Gmail API
> Messaging Telegram Bot API
> Voice Input Whisper.cpp
> Voice Output Piper or ElevenLabs
> Containerization Docker
> Source Control Git + GitHub
> Runtime Python (FastAPI)
> Scheduling APScheduler or Temporal
> Monitoring Langfuse or OpenTelemetry
>
> Development Roadmap
> Rather than trying to build everything at once, I'd approach it in phases=
:
> Foundation: Set up Hermes, Docker, Git, Obsidian, Qdrant, and a simple
> FastAPI service. Get retrieval from Obsidian working before adding
> automation.
> Core Tools: Add MCP servers for the filesystem, Git, GitHub, browser
> automation, and email. Ensure every tool call requires explicit
> confirmation for sensitive actions.
> Coding Agent: Integrate OpenHands so the agent can inspect repositories,
> edit code, run tests, and propose commits.
> Productivity Automation: Connect Gmail, Telegram, Google Calendar, and
> your task system. Start with suggestions and draft responses rather than
> fully autonomous actions.
> Memory & Learning: Automatically summarize conversations, update Obsidian
> notes, generate embeddings, and retrieve relevant context for future
> sessions.
> Advanced Features: Add voice interaction, research pipelines, dashboards,
> scheduled jobs, and eventually selective autonomous workflows for trusted=
,
> low-risk tasks.
> What I'd build today
> If I were starting from scratch in 2026, I'd aim for a modular
> "Jarvis"-style assistant with these core pieces:
> Hermes as the primary reasoning model.
> OpenHands dedicated to software engineering tasks.
> Obsidian as the human-readable long-term knowledge base.
> Qdrant for semantic memory retrieval.
> MCP as the standard interface for tools and services.
> n8n to orchestrate recurring workflows and integrations.
> FastAPI as the central backend that coordinates requests.
> Docker to isolate services and safely execute code.
> Playwright for browser-based automation.
> GitHub as the source of truth for all code and projects.
> This architecture is scalable, vendor-neutral, and lets you swap
> individual components (models, vector databases, automation tools) withou=
t
> redesigning the entire system.
> For someone serious about creating a powerful personal AI assistant, this
> is the direction I'd recommend over a monolithic agent framework. It give=
s
> you a system that's easier to maintain, extend, and trust as it takes on
> more responsibility.