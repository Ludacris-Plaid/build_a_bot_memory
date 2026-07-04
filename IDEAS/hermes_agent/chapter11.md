---
created: 2026-07-03
type: reference
tags: [book, hermes, chapter]
chapter: 11
title: "Autonomous Coding — Turning Hermes into a Software Engineer"
section: "Part I: Building the Personal AI Operating System"
source: victoria-k-emails
---

# Chapter 11 — Autonomous Coding — Turning Hermes into a Software Engineer

“The moment an AI can reliably modify code, it stops being a tool and starts becoming a collaborator.”
Up to this point, Hermes can:
think and reason
remember context
use tools (MCP)
interact with your real systems
browse the web
run scheduled automation
manage communication channels
But there’s still one major gap:
👉 It cannot yet own and evolve software projects safely and systematically.

This chapter changes that.

We build a controlled autonomous coding environment.

11.1 What “Autonomous Coding” Actually Means
We are NOT building:
a bot that randomly edits files
a system that pushes unreviewed code to production
a chaotic self-modifying agent
We ARE building:
A structured software engineering assistant that can:
understand repositories
propose changes
run tests
debug failures
iterate safely
submit reviewable changes
11.2 The Architecture Shift
We introduce a dedicated layer:
Hermes Agent
│
MCP Tool Layer
│
┌────────────┼────────────┐
▼ ▼ ▼
Browser Email Calendar
│
▼
Coding Runtime (NEW)
│
▼
Git Repositories + Docker Sandbox

This is your software engineering subsystem.
11.3 Why We Use a Coding Runtime
Direct filesystem editing is dangerous.
Instead, we isolate coding inside:

containers
cloned repositories
test environments
So Hermes never directly touches production state.
It works like this:

Clone repo
↓
Work in sandbox
↓
Run tests
↓
Iterate
↓
Create patch
↓
Request approval
↓
Apply to main repo

11.4 Introducing OpenHands-Style Workflow
We replicate the idea of an autonomous coding agent loop:
The loop:
Understand codebase
Identify task
Plan changes
Modify code
Run tests
Fix errors
Repeat
Produce final diff
This loop is the foundation of modern coding agents.
11.5 Repository Workspace Structure
Inside your AI OS:
~/ai-os/projects/

Each repo becomes:
project-name/
repo/
sandbox/
logs/
tests/
notes/
patches/

Hermes never works directly on live repos.
Only sandbox copies.

11.6 Git Integration Layer
We extend MCP with Git capabilities:
Hermes can:

clone repositories
create branches
commit changes
generate diffs
revert commits
open pull requests (with approval)
But always inside controlled workflows.
11.7 Code Understanding Phase
Before making changes, Hermes must:
read project structure
identify entry points
understand dependencies
map architecture
detect test framework
This is critical.
Bad agents skip understanding.

Good agents analyze first.

11.8 Planning Layer (Very Important)
No code changes happen immediately.
Instead:

User request
↓
Analysis
↓
Plan generated
↓
User approval (optional but recommended)
↓
Execution

Example plan:
“Fix authentication bug in login module”
Plan:
locate auth handler
identify failure condition
add validation check
update unit tests
run test suite
11.9 Execution Sandbox
All code execution happens in Docker:
isolated filesystem
controlled network access
limited permissions
reproducible environment
This prevents:
system corruption
accidental file deletion
security issues
dependency conflicts
11.10 Test-Driven Loop
Hermes should always:
Run tests
Observe failure
Modify code
Retry
This loop continues until:
tests pass
or max iteration limit reached
11.11 Patch-Based Output
Instead of rewriting files blindly, Hermes outputs:
diffs
patches
commit messages
Example:
Fix: resolve null pointer in auth module

- added null check before token validation
- improved error handling
- updated unit test coverage

This makes review easy.
11.12 Safety Boundaries
We enforce strict rules:
Hermes must NOT:

modify system files
access secrets directly
execute production scripts
push without approval
delete repositories
Allowed:
sandbox edits
test execution
patch generation
proposal creation
11.13 Multi-Step Debugging Loop
When errors occur:
Run code
↓
Capture error
↓
Analyze stack trace
↓
Hypothesize cause
↓
Apply fix
↓
Retry

This is how real engineers work.
11.14 Logging Development Sessions
Every coding session is stored:
logs/
coding/
session-id/
plan.md
changes.diff
tests.log
decisions.md

This becomes part of your AI memory system.
11.15 First Real Autonomous Task
Try something like:
“Add input validation to my API server.”
Expected flow:
Hermes clones repo
analyzes API structure
identifies endpoints
adds validation logic
runs tests
fixes errors
outputs patch
requests approval
11.16 Why This Is a Major Milestone
Before this chapter:
Hermes could assist coding
After this chapter:
Hermes can participate in software development
This is the difference between:
“code helper”
and
“junior engineer inside your system”
11.17 What We Are NOT Doing Yet
We still avoid:
autonomous production deployments
self-writing large systems without review
uncontrolled multi-repo changes
continuous self-improvement loops
AI modifying its own core runtime
Those require governance layers we will build later.
11.18 System Behavior Shift
Your AI OS now has:
Capability Status
reasoning ✔
memory ✔
tools ✔
communication ✔
automation ✔
web access ✔
coding ✔
autonomous iteration ✔

End of Chapter 11
Your system can now:
understand codebases
modify software safely
test changes automatically
iterate like a developer
What’s Next
Chapter 12 is where everything starts converging into a unified system.
We will build:

a unified dashboard for Hermes
real-time system observability
centralized logs and traces
decision history tracking
tool usage analytics
memory visualization
workflow control panel
This is where your AI OS stops being a collection of services… and becomes a single coherent system you can observe and control.

On Fri, Jul 3, 2026 at 4:13 AM Victoria K <vkushelnyk@gmail.com> wrote:
