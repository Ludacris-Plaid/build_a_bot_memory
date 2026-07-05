---
date: 2026-07-04
to: UAB ESNET (VPS Provider)
subject: Outbound Port Opening Request (587 / 993)
status: unsent
---

Hi,

Could you please open outbound TCP ports **587** (SMTP submission) and **993** (IMAPS) on my VPS?

IP: [your VPS IP here]

These are needed for email functionality — sending via SMTP and reading via IMAP over TLS. Current outbound filtering appears to be blocking these ports, and I've confirmed both work from other networks.

Thanks.

---

**Ports requested:**
| Port | Protocol | Service |
|------|----------|---------|
| 587 | TCP | SMTP Submission (STARTTLS) |
| 993 | TCP | IMAP over TLS |

**Status:** unsent
**Provider:** UAB ESNET
**Account:** REAiPersonalAssistsnt@gmail.com (Gmail)
