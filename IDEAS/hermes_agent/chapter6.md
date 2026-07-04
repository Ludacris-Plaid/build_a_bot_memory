---
created: 2026-07-03
type: reference
tags: [book, hermes, chapter]
chapter: 6
title: "Building Long-Term Memory — Giving Hermes a Second Brain"
section: "Part I: Building the Personal AI Operating System"
source: victoria-k-emails
---

# Chapter 6 — Building Long-Term Memory — Giving Hermes a Second Brain

"Intelligence is knowing things. Wisdom is remembering what matters." One of the biggest limitations of most AI assistants is that they forget. You may spend hours explaining your project, your coding style, your business, and your preferences, only to repeat yourself in the next conversation.

That isn't acceptable for a personal AI operating system.

This chapter solves that problem.

By the end of this chapter, Hermes will have:

A human-readable knowledge base
Persistent memory
Semantic search
Automatic memory retrieval
Project documentation
Daily journals
A "second brain" that grows over time
This is where your AI stops acting like a chatbot and starts acting like a colleague.
6.1 Understanding Memory
Memory is often misunderstood.
Many people think:

"The AI should remember everything."
That sounds useful until you realize it becomes expensive, slow, and noisy. Instead, we want layered memory.

Our system will have four types of memory:

Active Conversation
│
Working Memory
│
Project Memory
│
Long-Term Knowledge

Each layer has a different purpose.
6.2 The Four Memory Layers
Layer 1 – Conversation Memory
This is the current chat.
It exists only while you're working.

Example:

Fix the login page.
Hermes remembers the discussion until the task is complete.
Layer 2 – Working Memory
Temporary notes for ongoing work.
Examples:

Current bug
Next task
Test results
TODO list
This memory changes constantly.
Layer 3 – Project Memory
Every project gets its own documentation.
Example:

Projects/

AI Operating System/

README.md

Architecture.md

Known Bugs.md

Roadmap.md

Meeting Notes.md

TODO.md

Months later, Hermes immediately understands the project.
Layer 4 – Long-Term Memory
Everything worth remembering eventually ends up here.
Examples:

Your coding preferences
Favorite libraries
API keys (never stored in plain text)
Business ideas
Research
Documentation
Design decisions
Meeting summaries
This becomes your digital brain.
6.3 Why Obsidian?
Many AI systems store memory inside a database.
That works...

Until the software disappears.

Instead, we're going to store almost everything as Markdown.

Advantages:

Human readable
Future proof
Git compatible
Easy backup
Works without AI
No vendor lock-in
Your AI memory remains useful even if Hermes disappears tomorrow.
6.4 Installing Obsidian
Although Obsidian is a desktop application, think of it as the editor for your AI's knowledge base.
Create a vault called:

AI Brain

Store the vault inside your synchronized project directory so it can be backed up and version-controlled.
6.5 Folder Structure
Create the following structure:
AI Brain/

Daily Notes/

Projects/

Programming/

Research/

People/

Meetings/

Ideas/

Business/

Health/

Learning/

Books/

Articles/

Scratchpad/

Templates/

Archive/

Don't over-organize.
Folders help.

Links help more.

6.6 The Philosophy of Notes
Good notes answer questions.
Bad notes collect information.

Instead of writing:

Docker

Write:
Why did we choose Docker?

Advantages

Disadvantages

Alternatives

Lessons learned

Useful commands

Your future AI can reason much better from structured notes.
6.7 Linking Notes
One of Obsidian's superpowers is linking.
Example:

[[Hermes]]

[[OpenHands]]

[[Qdrant]]

[[Telegram Automation]]

After a year you'll have a knowledge graph instead of isolated documents. Hermes can use these relationships to provide richer answers.

6.8 Daily Notes
Create one note every day.
Example:

2026-07-03

Today's goals

Finished:

Installed Hermes

Problems:

Docker networking

Ideas:

Multi-agent architecture

Tomorrow:

Install Qdrant

Hermes will eventually help generate these automatically.
6.9 Templates
Create reusable templates.
Example:

Project template:

# Project

## Purpose

## Architecture

## Technologies

## TODO

## Decisions

## Problems

## References

Meeting template:
# Meeting

Participants

Agenda

Notes

Actions

Follow-up

Consistency improves retrieval.
6.10 Semantic Search
Folders aren't enough.
Imagine asking:

"Find every note where I discussed vector databases."
You don't remember whether it was called:
Qdrant
Embeddings
AI Memory
Database Research
Semantic search solves this.
Instead of matching words...

It matches meaning.

6.11 Vector Embeddings
This is how semantic memory works.
Markdown

↓

Chunking

↓

Embedding Model

↓

Vector Database

↓

Semantic Search

↓

Hermes

Hermes asks:
"What memories relate to this conversation?"
The vector database answers.
6.12 Choosing a Vector Database
There are many excellent options:
Database Notes
Qdrant Fast, simple, open source
Chroma Lightweight
Weaviate Powerful but larger
LanceDB Excellent for local development
pgvector Good if you already use PostgreSQL

For this book we'll use Qdrant because it's reliable, actively maintained, and integrates well with retrieval pipelines.
6.13 What Should Be Embedded?
Not everything.
Good candidates:

Notes
Documentation
Research
Project plans
Meeting summaries
Books
Code explanations
API documentation
Avoid embedding:
Large binary files
Passwords
Private keys
Certificates
Encrypted secrets
Those belong in secure storage.
6.14 Automatic Memory Pipeline
Eventually the system will look like this:
Conversation

↓

Summarize

↓

Extract useful knowledge

↓

Write Markdown

↓

Create embedding

↓

Store in Qdrant

↓

Future retrieval

You don't manually decide what to remember.
Hermes helps curate the knowledge base.

6.15 Memory Retrieval
Suppose you ask:
"Continue working on the Telegram bot."
Hermes should retrieve:
Project notes
Architecture decisions
Previous conversations
Outstanding TODOs
Related documentation
Before answering.
That makes responses far more useful.

6.16 Designing Good Memories
Not every conversation deserves permanent storage.
A useful heuristic is:

Store:

Decisions
Preferences
Long-term goals
Completed research
Project status
Lessons learned
Don't store:
Small talk
Temporary mistakes
Duplicate information
One-off questions
Quality beats quantity.
6.17 Git for Knowledge
Initialize your Obsidian vault as a Git repository.
Benefits:

Version history
Easy backup
Rollback
Synchronization
Branching for experiments
Your knowledge becomes software.
6.18 Security
Your second brain will eventually contain:
Business plans
Research
Personal notes
Internal documentation
Treat it like source code.
Back it up.

Encrypt sensitive devices.

Control access carefully.

6.19 Looking Ahead
Right now:
Hermes has memory.

But it still can't do much.

It doesn't know how to:

Read GitHub repositories
Search your filesystem
Use Docker
Query databases
Browse the web
Manage email
Control Telegram
To unlock those capabilities, we need a standardized way for Hermes to communicate with external tools. End of Chapter 6 Congratulations. Your AI now has the foundations of a persistent memory system.

Instead of forgetting everything after each session, it can begin building a durable, searchable knowledge base that grows alongside your work.

What's Next
Chapter 7 introduces Model Context Protocol (MCP)—the technology that allows Hermes to securely interact with tools and services.
We'll cover:

What MCP is and why it matters.
Installing an MCP host.
Connecting filesystem, Git, GitHub, Docker, and database tools. Permission models and security. Building your first custom MCP server. Once Hermes has both memory and tools, it becomes capable of taking meaningful actions rather than simply answering questions. From that point on, each chapter will expand its abilities until it resembles the always-on AI operating system we envisioned at the beginning of the book.

On Fri, Jul 3, 2026 at 4:10 AM Victoria K <vkushelnyk@gmail.com> wrote:
