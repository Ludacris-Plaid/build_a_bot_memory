---
created: 2026-07-03
type: reference
tags: [book, hermes, chapter]
chapter: 3
title: "Building the Production Platform"
section: "Part I: Building the Personal AI Operating System"
source: victoria-k-emails
---

# Chapter 3 — Building the Production Platform

"A good server runs software. A great server runs services reliably." In the previous chapter, we built a secure Linux server. Now we're going to transform it into a platform capable of running dozens of AI services that work together.
By the end of this chapter, you'll have:

A production Docker environment
Automatic HTTPS
A reverse proxy
Internal Docker networking
DNS configured
Centralized environment variables
A scalable directory layout
Monitoring foundations
Automatic container restarts
After this chapter, every future component (Hermes, Qdrant, PostgreSQL, n8n, OpenHands, Grafana, etc.) will simply plug into the platform.
3.1 Thinking Like an Infrastructure Engineer
A common mistake is running every application independently:
docker run postgres
docker run qdrant
docker run hermes
docker run redis
docker run nginx

That quickly becomes difficult to manage.
Instead, we'll organize services using Docker Compose.

Every service will have:

its own configuration
persistent storage
internal networking
restart policy
health checks
backups
3.2 The Final Architecture
By the end of the book your VPS will look like this:
Internet
│
Cloudflare DNS
│
Reverse Proxy
(Traefik)
│
┌─────────────────┼──────────────────┐
│ │ │
▼ ▼ ▼
Hermes Agent n8n OpenHands
│
▼
MCP Servers
│
┌────┴─────────────┐
▼ ▼
Qdrant PostgreSQL
│
▼
Obsidian Vault

Every service communicates internally.
Only Traefik is exposed to the public Internet.

3.3 Why Traefik?
Many tutorials recommend Nginx.
Nginx is excellent.

However, Traefik is designed for Docker.

Advantages:

Automatic HTTPS
Automatic service discovery
Automatic SSL renewal
Docker integration
Simple labels
Easy scaling
Whenever we launch a new container, Traefik immediately discovers it. No configuration files need updating.

3.4 Domain Configuration
Suppose your domain is:
example.com

Create these DNS records:
Host Points To
ai VPS IP
api VPS IP
n8n VPS IP
qdrant VPS IP
grafana VPS IP
hermes VPS IP

If using Cloudflare:
Enable:

Proxy
Automatic HTTPS
DNSSEC (optional)
3.5 Directory Structure
Expand the folders we created.
ai-os/

compose/

configs/

logs/

data/

services/

scripts/

monitoring/

backups/

obsidian/

projects/

Inside compose:
compose/

traefik/

postgres/

qdrant/

hermes/

n8n/

openhands/

grafana/

prometheus/

redis/

Every service receives:
docker-compose.yml

.env

README.md

Keeping services isolated makes upgrades much easier.
3.6 Docker Networks
We'll create two Docker networks.
public

Used only by:
Traefik
Everything else stays on:
internal

This means your database is never directly accessible from the Internet. This is one of the biggest security improvements you can make.

3.7 Persistent Storage
Containers should be disposable.
Data should not.

Every service stores data outside the container.

Example:

data/

postgres/

qdrant/

redis/

grafana/

hermes/

If a container crashes:
Delete it.

Recreate it.

Your data survives.

3.8 Environment Variables
Never hardcode secrets.
Instead create:

.env

Example:
POSTGRES_USER=aiadmin

POSTGRES_PASSWORD=...

OPENAI_API_KEY=...

TELEGRAM_TOKEN=...

GITHUB_TOKEN=...

Docker automatically loads these values.
3.9 Automatic Restarts
Every container should include:
restart: unless-stopped

If the VPS reboots:
Everything starts automatically.

3.10 Health Checks
A container running isn't necessarily healthy.
Each service should expose a health endpoint.

Docker periodically asks:

Are you alive?

If not:
Restart.

This prevents many subtle failures.

3.11 Logging
Instead of every container writing logs everywhere, create:
logs/

traefik/

hermes/

n8n/

postgres/

Centralized logs make debugging much easier.
3.12 Monitoring
Eventually we'll install:
Prometheus
Grafana
cAdvisor
Node Exporter
These provide:
CPU

RAM

Disk

Network

Container health

Temperature (where supported)

Database performance

API latency

LLM usage

You'll know immediately if something fails.

3.13 Backup Strategy
Never trust a single disk.
Daily:

Database dump

Weekly:

Obsidian backup

Monthly:

Entire Docker volumes

Also back up:

configs/

compose/

scripts/

These files are often more valuable than the containers themselves.
3.14 GitHub Repository
Create a private repository.
Example:

AI-Operating-System

Commit:
compose/

scripts/

configs/

docs/

Never commit:
.env

keys

certificates

tokens

database dumps

3.15 Documentation
Create:
docs/

Document everything.
Example:

Server Architecture.md

Network Diagram.md

Secrets.md

Deployment.md

Troubleshooting.md

Future you will thank present you.
3.16 Planning the Services
Here's what we'll install over the next several chapters.
Service Purpose
Traefik Reverse proxy
PostgreSQL Main relational database
Redis Cache and message broker
Qdrant Vector database
Hermes Agent AI orchestrator
OpenHands Coding agent
n8n Workflow automation
Grafana Dashboards
Prometheus Metrics
Obsidian Sync Long-term knowledge
MCP Servers Tool integrations
Playwright Browser automation

Each will run in its own container.
Each can be updated independently.

3.17 Security Philosophy
Everything inside the server should follow least privilege.
Examples:

Hermes should not have root access.

OpenHands should not control Docker directly.

The browser automation service should run in an isolated container.

Databases should not be exposed publicly.

Treat every service as potentially vulnerable.

Isolation limits the damage if something goes wrong.

3.18 Resource Planning
Estimated idle memory usage:
Service RAM
Traefik 80 MB
PostgreSQL 300 MB
Redis 100 MB
Qdrant 500 MB
Hermes Variable
n8n 400 MB
OpenHands 1–2 GB
Grafana 250 MB
Prometheus 400 MB

A 16 GB VPS is enough to get started, though 32 GB gives you more room as you add services.
3.19 Your Infrastructure Is Ready
At this point you've designed a platform that can grow from five containers to fifty without needing to be rebuilt. That scalability is intentional.

As new AI tools appear, you'll add them as independent services instead of tearing apart the existing system.

End of Chapter 3
Your server is no longer "just a VPS." It's a production platform ready to host a complete AI operating system. What's Coming Next Chapter 4 is where the real fun begins.
We'll deploy:

Traefik
Automatic HTTPS with Let's Encrypt
Docker Compose stacks
Internal Docker networking
Your first production services
By the end of Chapter 4, you'll be able to visit https://ai.yourdomain.com (or a similar subdomain you choose) and see your own infrastructure responding over HTTPS. That marks the transition from preparing the platform to actually deploying the services that will power your personal AI operating system. A note on keeping this book current One thing I'd like to improve over a traditional printed book is to keep the build aligned with current best practices. AI infrastructure changes quickly—projects evolve, APIs change, and new tools emerge every few months.
As we continue, I'll favor:

Official documentation over outdated community examples.
Stable, actively maintained components.
Configurations that are practical in production rather than just enough to get something running. Explanations of why we're making a choice, so you can substitute components later if the ecosystem changes. That way, the end result isn't just a snapshot of today's tools—it's an architecture that can adapt over time.

On Fri, Jul 3, 2026 at 4:07 AM Victoria K <vkushelnyk@gmail.com> wrote:
