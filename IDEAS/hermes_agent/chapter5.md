---
created: 2026-07-03
type: reference
tags: [book, hermes, chapter]
chapter: 5
title: "Installing Hermes — The Heart of Your AI Operating System"
section: "Part I: Building the Personal AI Operating System"
source: victoria-k-emails
---

# Chapter 5 — Installing Hermes — The Heart of Your AI Operating System

"Today your server stops being a Linux machine and starts becoming an intelligent assistant." This is one of the most important chapters in the book. Everything we've done so far has been preparation. Now we're installing the component that will orchestrate your entire AI operating system.

By the end of this chapter, you will have:

A working Hermes installation
A connected language model
Your first successful conversation
A production-ready workspace
Docker sandboxing for tool execution
A foundation ready for memory, MCP, automation, and coding
The Hermes documentation recommends a simple progression: install Hermes, run the setup wizard, configure one model provider, verify a working terminal conversation, and only then begin adding integrations. We'll follow that approach before layering on the rest of the system. H Hermes Agent Logo +1
5.1 Understanding Hermes' Role
Hermes is not the language model.
Hermes is the agent runtime.

Think of it like this:

You
│
▼
Hermes Agent
│
┌───────────┼────────────┐
▼ ▼ ▼
LLM File System Tools
│
▼
Memory

Hermes decides:
Which tools to use
Which files to read
Whether to search memory
When to ask follow-up questions
How to break large tasks into smaller ones
The language model simply provides reasoning.
5.2 Choosing Your LLM
Hermes can connect to many providers through its setup process. H Hermes AI +1
For this book I recommend starting with:

Option A (Recommended)
OpenRouter
Advantages:

Access to many models
Easy to switch models
Pay only for usage
Good starting models:
Hermes
Qwen
DeepSeek
Claude
GPT
Option B
OpenAI
Very reliable.

Excellent coding.

Easy setup.

Option C
Local models using an OpenAI-compatible endpoint
Perfect once you own a GPU server.

We'll cover this later.

5.3 Install Hermes
The Hermes project provides an installer for Linux environments. Before running any installer you should review the script, then execute it if you're comfortable with what it does. The current installation guide and quickstart both recommend this workflow. H Hermes AI +1
After installation, verify:

hermes --version

Expected:
Hermes Agent x.x.x

5.4 Initial Setup
Run:
hermes setup

Hermes will ask:
Which LLM provider?
API key
Model name
Tool configuration
Hermes also includes a newer "Blank Slate" setup mode if you want to start with only the essentials (provider, terminal, and file tools) and add everything else later. R Reddit +1
For this book:

Choose Blank Slate if available.

We'll build everything manually.

5.5 Configure the Model
Run:
hermes model

You'll configure:
Provider

↓

API key

↓

Model

↓

Context length

↓

Connection test

Hermes supports switching models later without rebuilding your system. H Hermes AI

5.6 Verify Hermes
Launch:
hermes

Ask:
Hello Hermes.
You should receive a response.
Congratulations.

You now have a working AI agent.

5.7 Configure the Workspace
Create:
~/ai-os/workspace

This becomes Hermes' primary working directory.
Inside:

workspace/

projects/

scripts/

downloads/

notes/

scratch/

This keeps generated files separate from your infrastructure configuration.
5.8 Sandboxed Tool Execution
One of the first production decisions is where Hermes should execute commands.
Options include:

Directly on the host
Inside Docker
Over SSH to another machine
For an always-on VPS, I recommend Docker sandboxing for routine terminal tasks. Hermes supports changing the terminal backend, including Docker. H Hermes AI +1
Benefits:

Safer experimentation
Easier cleanup
Better isolation
5.9 Your First Real Task
The Hermes quickstart recommends using a real task instead of a toy prompt. H Hermes Agent Logo
Examples:

Summarize this Git repository.
or
Explain this Docker Compose stack.
or
Review this Python script for bugs.
Avoid:
Tell me a joke.
Real tasks expose configuration issues much faster.
5.10 Sessions
Hermes stores conversations.
That means you can continue later.

Example:

hermes --continue

This resumes the previous session instead of starting over.
H
Hermes AI
5.11 Skills
Hermes supports installable Skills.
Think of Skills as reusable expertise.

Examples:

Kubernetes
React
Docker
Rust
Git
Terraform
We'll install many of these later, after our core system is stable.
5.12 Keep the Core Small
Many people immediately install:
MCP
Voice
Telegram
Discord
Browser tools
Twenty Skills
Don't.
At this stage you only need:

One model
Terminal access
File operations
A stable conversation
Everything else comes later.
5.13 Configure Your Project
Inside:
~/ai-os

Create:
assistant/

knowledge/

memory/

prompts/

templates/

automation/

These directories will gradually become the brain of your AI operating system.
5.14 Create Your First System Prompt
Instead of relying on defaults, define the role you want Hermes to play.
For example:

Act as a software engineer.
Prefer safe actions over risky ones.
Ask before making irreversible changes.
Explain reasoning when proposing architectural changes.
Write maintainable, well-documented code.
Store reusable knowledge in the memory system when appropriate. We'll refine this prompt throughout the book.
5.15 What We Are Not Doing Yet
We are intentionally delaying:
Obsidian
Qdrant
PostgreSQL
GitHub
Telegram
Gmail
Calendar
Browser automation
Voice
Long-term memory
The temptation is to connect everything immediately.
Resist it.

A stable foundation is far more valuable than a large but fragile system.

5.16 Verify Your Installation
Before continuing, confirm:
Hermes launches successfully.
Your chosen model responds.
Sessions can be resumed.
Hermes can access its workspace.
Tool execution works using your chosen backend.
Configuration files are backed up.
Only when all of these checks pass should you continue.
What's Next
The next chapter is one of the biggest in the entire book.
We'll build long-term memory.

Specifically, we'll connect:

Obsidian
Markdown
Semantic search
Qdrant
Embeddings
Retrieval pipelines
By the end of Chapter 6, Hermes will no longer rely solely on the current conversation. Instead, it will begin developing a searchable, persistent knowledge base that grows with every project, note, and interaction. That's the point where it starts to feel less like a chatbot and more like a true personal AI operating system.

H
H
R
Sources

On Fri, Jul 3, 2026 at 4:09 AM Victoria K <vkushelnyk@gmail.com> wrote:
