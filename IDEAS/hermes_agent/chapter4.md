---
created: 2026-07-03
type: reference
tags: [book, hermes, chapter]
chapter: 4
title: "Creating the AI Platform"
section: "Part I: Building the Personal AI Operating System"
source: victoria-k-emails
---

# Chapter 4 — Creating the AI Platform

"Today we stop preparing and start building."
Up to this point you've built a secure server and designed the architecture. This chapter is where your VPS begins to resemble an actual AI platform.

By the end of this chapter you will have:

Docker Compose configured properly
Traefik running
Automatic HTTPS certificates
A shared Docker network
Automatic service discovery
A project layout that can scale to dozens of services
The first production containers online
Chapter Goal
By the end of this chapter, you'll have an infrastructure that looks like
this:
Internet
│
▼
Cloudflare / DNS
│
▼
HTTPS (443)
│
▼
Traefik Reverse Proxy
│
┌──────────┼──────────┐
│ │ │
▼ ▼ ▼
Hermes n8n OpenHands
│
▼
Internal Docker Network
│
┌────┴─────────────┐
▼ ▼
PostgreSQL Qdrant

Only Traefik is exposed to the internet.
Everything else communicates privately.

This dramatically improves security.

4.1 Why Docker Compose?
You could manually launch containers one by one.
That quickly becomes impossible to manage.

Instead, every service in this book will have:

docker-compose.yml
.env
README.md

Starting a service becomes:
docker compose up -d

Stopping:
docker compose down

Updating:
docker compose pull
docker compose up -d

That's it.
4.2 Installing Docker Compose (if needed)
Most modern Docker installations already include the Compose plugin.
Verify:

docker compose version

Expected output:
Docker Compose version v2.x.x

If it works, you're ready.
4.3 Create the Shared Network
Create a permanent Docker network.
docker network create ai-network

Verify:
docker network ls

You should see:
ai-network
bridge
host
none

Every future service joins this network.
4.4 Create the Infrastructure Directory
Inside:
~/ai-os

Create:
compose/

Then:
compose/

traefik/

postgres/

redis/

qdrant/

hermes/

openhands/

n8n/

grafana/

prometheus/

This organization keeps each service isolated.
4.5 Installing Traefik
Traefik becomes the front door to your AI operating system.
Responsibilities:

HTTPS
SSL certificates
Routing
Load balancing
Automatic container discovery
Unlike Nginx, Traefik automatically discovers Docker containers. Launch a new service...

Traefik immediately knows about it.

4.6 Create Traefik Configuration
Create:
compose/traefik/

Inside:
docker-compose.yml

Traefik will:
expose ports 80 and 443
mount the Docker socket (read-only)
store Let's Encrypt certificates
join ai-network
restart automatically
watch Docker for new services
We'll keep all routing rules in Docker labels rather than large configuration files.
4.7 Automatic HTTPS
One of Traefik's biggest advantages is automatic certificate management.
Instead of manually creating certificates, Traefik will:

Detect a new hostname.
Request a certificate from Let's Encrypt.
Renew it automatically before expiration.
Redirect HTTP traffic to HTTPS.
Once configured, every new service can receive HTTPS with minimal additional configuration.
4.8 Prepare DNS
At your DNS provider, create records such as:
Type Name Target
A ai VPS IP
A hermes VPS IP
A n8n VPS IP
A grafana VPS IP
A api VPS IP

If you use Cloudflare, leave the proxy enabled unless a specific service requires direct access.
4.9 Docker Volumes
Containers are temporary.
Data isn't.

Create persistent storage:

data/

postgres/

redis/

qdrant/

traefik/

grafana/

prometheus/

hermes/

Every important service writes here.
Deleting a container never deletes your data.

4.10 Central Environment File
Inside:
~/ai-os

Create:
.env

Eventually it will contain:
DOMAIN=example.com

EMAIL=you@example.com

TZ=America/Edmonton

POSTGRES_USER=aiadmin

POSTGRES_PASSWORD=...

OPENAI_API_KEY=...

TELEGRAM_TOKEN=...

GITHUB_TOKEN=...

OBSIDIAN_PATH=/home/aiadmin/ai-os/obsidian

Never commit this file to Git.
4.11 Create Your First Service
Instead of deploying Hermes immediately, start with a simple container to verify your infrastructure.
A lightweight web server is enough to confirm:

Docker networking works.
Traefik routes correctly.
HTTPS certificates are issued.
DNS points to the correct machine.
Once this works, every future service follows the same pattern.
4.12 Service Labels
One of Traefik's strengths is that services describe themselves.
A typical service advertises:

its hostname (for example, hermes.example.com)
which internal port it listens on
whether HTTPS should be enabled
Traefik reads this metadata automatically and creates the routing rules without you editing a central configuration file.
4.13 Logging
Create:
logs/

traefik/

docker/

system/

Logs are invaluable when diagnosing:
certificate failures
DNS issues
container crashes
routing problems
Rotate logs regularly so they don't consume excessive disk space.
4.14 Health Checks
Every service should expose a health endpoint where possible. Docker can periodically test whether a service is responsive.

If a health check fails repeatedly, Docker can restart the container automatically.

This is one of the easiest ways to improve long-term reliability.

4.15 Verify the Platform
At this stage, you should be able to confirm:
Docker is running.
The ai-network network exists.
Traefik starts without errors.
DNS records resolve correctly.
HTTPS certificates are issued.
A test service is reachable through your chosen hostname.
Once those checks pass, you've built a reusable platform for every component that follows.
4.16 The Philosophy Behind the Stack
Notice what we've not done:
Installed Hermes.
Installed databases.
Installed automation tools.
That was intentional.
Infrastructure should come first.

Once the platform is solid, adding a new service becomes routine instead of risky.

What's Coming Next
Chapter 5 is where your AI operating system becomes genuinely intelligent.
We'll install and configure Hermes Agent itself, including:

Choosing a language model backend (cloud or local).
Connecting Hermes to your infrastructure.
Configuring its tool system.
Setting up its initial memory.
Understanding its architecture.
Running your first successful conversations.
From there, we'll begin expanding Hermes with persistent memory, coding capabilities, automation, and integrations until it becomes the central orchestrator of your personal AI operating system. A note before we continue As we move into Hermes, we'll shift from high-level planning to hands-on implementation. I'll include configuration examples where they're stable, but I won't invent or freeze commands for projects that change rapidly. Where a project's installation process evolves frequently, we'll follow the current official documentation and adapt it to fit the architecture we've built, rather than copying outdated snippets. That approach makes the book more durable and gives you a system that's easier to maintain as the AI ecosystem evolves.

On Fri, Jul 3, 2026 at 4:08 AM Victoria K <vkushelnyk@gmail.com> wrote:
