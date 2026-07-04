---
created: 2026-07-03
type: reference
tags: [book, hermes, chapter]
chapter: 2
title: "Building the Foundation – VPS, Domain, and Secure Linux Server"
section: "Part I: Building the Personal AI Operating System"
source: victoria-k-emails
---

# Chapter 2 — Building the Foundation – VPS, Domain, and Secure Linux Server

"A house is only as strong as its foundation."
Before we install a single AI component, we need infrastructure that is reliable, secure, and easy to maintain. Many AI tutorials jump straight into running a model. That works for experiments, but if you're building something that will manage your emails, code repositories, documents, and personal knowledge, you want an environment you can trust.

By the end of this chapter, you'll have:

A VPS running Ubuntu Server LTS
SSH key authentication
A hardened Linux server
A configured firewall
Automatic security updates
Docker prerequisites installed
A registered domain name pointing at your server
A clean project structure ready for the AI operating system
2.1 Choosing a VPS Provider
You do not need a GPU server to begin. Hermes can use cloud-hosted models while all of your automation, memory, and tooling run on your VPS.
Look for these minimum specifications:

Component Recommended
CPU 4–8 vCPUs
RAM 16 GB minimum (32 GB preferred)
Storage 200 GB NVMe SSD
OS Ubuntu Server 24.04 LTS
IPv4 Dedicated static address
Backups Daily snapshots

Good providers include:
DigitalOcean
Hetzner
Vultr
Linode
OVHcloud
For this book, we'll assume Ubuntu Server 24.04 LTS.
2.2 Registering a Domain
You'll eventually expose services like:
ai.yourdomain.com

n8n.yourdomain.com

api.yourdomain.com

grafana.yourdomain.com

vault.yourdomain.com

Keeping services on subdomains makes SSL certificates and reverse proxy configuration much easier later.
2.3 Creating the VPS
After creating your VPS:
Choose:

Ubuntu Server 24.04 LTS

Region:

Choose one geographically close to you.

Disk:

At least 200 GB.

Enable:

Daily backups
Monitoring
IPv4
IPv6 (optional)
2.4 Generating SSH Keys
Never log in using passwords.
On Linux/macOS:

ssh-keygen -t ed25519 -C "your@email.com"

Windows PowerShell:
ssh-keygen

This creates:
~/.ssh/id_ed25519

and
~/.ssh/id_ed25519.pub

Upload the public key to your VPS provider during creation.
2.5 First Login
Connect:
ssh root@YOUR_SERVER_IP

If successful:
Welcome to Ubuntu 24.04 LTS

Congratulations.
You now own a Linux server.

2.6 Update Everything
Immediately update packages.
apt update

apt upgrade -y

Install useful utilities:
apt install -y \
git \
curl \
wget \
htop \
vim \
nano \
unzip \
zip \
build-essential \
ca-certificates

2.7 Create a Non-Root User
Never work as root.
Create a new user:

adduser aiadmin

Add to sudo:
usermod -aG sudo aiadmin

Copy SSH keys:
rsync --archive --chown=aiadmin:aiadmin ~/.ssh /home/aiadmin

Log out.
Reconnect:

ssh aiadmin@YOUR_SERVER_IP

2.8 Disable Root Login
Edit:
sudo nano /etc/ssh/sshd_config

Set:
PermitRootLogin no
PasswordAuthentication no
PubkeyAuthentication yes

Restart SSH:
sudo systemctl restart ssh

Now only SSH keys work.
2.9 Configure the Firewall
Ubuntu includes UFW.
Enable:

sudo ufw allow OpenSSH

Later we'll open:
80
443

Enable:
sudo ufw enable

Check:
sudo ufw status

Expected:
22 ALLOW

2.10 Automatic Security Updates
Install:
sudo apt install unattended-upgrades

Enable:
sudo dpkg-reconfigure unattended-upgrades

Now security patches install automatically.
2.11 Set Timezone
sudo timedatectl set-timezone America/Edmonton

Verify:
timedatectl

Accurate time matters for logs, certificates, and scheduled workflows.
2.12 Install Fail2Ban
Fail2Ban helps protect against repeated login attempts.
sudo apt install fail2ban

Enable:
sudo systemctl enable fail2ban
sudo systemctl start fail2ban

Check status:
sudo systemctl status fail2ban

2.13 Install Docker
Remove old versions if present:
sudo apt remove docker docker-engine docker.io containerd runc

Install prerequisites:
sudo apt install \
ca-certificates \
curl \
gnupg

Create the keyring directory:
sudo install -m 0755 -d /etc/apt/keyrings

Download Docker's GPG key:
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | \
sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

Add the Docker repository:
echo \
"deb [arch=$(dpkg --print-architecture)
signed-by=/etc/apt/keyrings/docker.gpg] \
https://download.docker.com/linux/ubuntu \
$(. /etc/os-release && echo $VERSION_CODENAME) stable" | \
sudo tee /etc/apt/sources.list.d/docker.list

Update:
sudo apt update

Install Docker:
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

Verify:
docker --version

2.14 Allow Docker Without sudo
sudo usermod -aG docker $USER

Log out.
Log back in.

Verify:

docker ps

No errors means success.
2.15 Create Your Project Structure
Under your home directory:
~/ai-os/

Inside:
ai-os/
│
├── docker/
├── configs/
├── backups/
├── logs/
├── scripts/
├── data/
├── compose/
├── secrets/
├── docs/
├── projects/
├── obsidian/
└── monitoring/

Create it:
mkdir -p
~/ai-os/{docker,configs,backups,logs,scripts,data,compose,secrets,docs,projects,obsidian,monitoring}

2.16 Initialize Git
cd ~/ai-os

git init

Create:
.gitignore

Example:
.env
*.key
*.pem
secrets/

Commit:
git add .
git commit -m "Initial AI operating system structure"

2.17 Plan for Secrets
Never hard-code:
API keys
Passwords
OAuth tokens
SSH keys
We'll use .env files for local development and migrate to a proper secrets manager later.
2.18 Verify the Foundation
Before moving on, confirm:
SSH keys work
Root login is disabled
Firewall is active
Automatic updates are enabled
Fail2Ban is running
Docker is installed
Docker Compose is available
Git is initialized
Project directories exist
At this point, you have a secure, clean Linux server that can host the rest of your AI operating system. What's Next?
In Chapter 3, we'll transform this server into a production platform by:
Installing a reverse proxy
Obtaining free HTTPS certificates
Configuring DNS
Setting up Docker Compose for multiple services
Creating an internal Docker network
Adding health checks and restart policies
Preparing the infrastructure that every future component—Hermes, Qdrant, PostgreSQL, n8n, and more—will use By the end of the next chapter, you'll have the production-grade hosting environment that the rest of the AI operating system will run on. From there, we'll begin installing the core AI components themselves.

On Fri, Jul 3, 2026 at 4:07 AM Victoria K <vkushelnyk@gmail.com> wrote:
