# Chattrap v2.0 - The Ominous Drop

## Executive Summary

**Chattrap v2.0** is a modular, async/await-based OSINT surveillance platform that monitors target chat sessions for explicit content and personal data. When a target's "Truth Score" hits 70% or higher, the system generates a dynamic, encrypted "Ominous Drop" page—a ransom-style web interface requiring payment (XMR wallet) to reveal the dossier. The drop page includes a 72-hour countdown timer, live chat feed, and dynamic pricing ($5k → $10k → $15k). If the timer expires, the system escalates to authority contacts extracted from the target's data.

Built with **FastAPI** (Python 3.11+), **PostgreSQL**, **Redis**, and **React/Next.js**, the platform is designed for high-concurrency, real-time operation with client-side decryption (AES-256/Web Crypto API).

---

## Architecture Overview

### Tech Stack

| Layer | Technology | Purpose |
|-------|------------|---------|
| **Backend** | FastAPI (Python 3.11+) | Async/await WebSocket server, REST API, OSINT agents |
| **Database** | PostgreSQL 16 | Structured data (targets, sessions, evidence, dossiers) |
| **Cache** | Redis 7 | Real-time session state, heartbeat pinging |
| **Encryption** | AES-256 + Fernet | Client-side dossier decryption |
| **Frontend** | React 18 (Next.js) | Dashboard, LiveMap, DropPage, Auth |
| **OSINT** | Modular pluggable agents | Scraping, image recognition, metadata extraction |
| **Deployment** | Docker Compose | Multi-service orchestration |

### Directory Structure

```
chattrap-v2/
├── backend/
│   ├── api/
│   │   └── main.py              # FastAPI core, WebSocket, CORS, static mounts
│   ├── models/
│   │   ├── target.py            # Target (name, email, wallet, truth_score)
│   │   ├── session.py           # Chat logs, evidence, dossier, encryption fields
│   │   ├── evidence.py          # Evidence chunks with metadata
│   │   ├── dossier.py           # Generated drop page content
│   │   ├── escalation_log.py    # Authority contacts, escalation chain
│   │   └── analytics.py         # Usage metrics, session analytics
│   ├── services/
│   │   ├── chat_analyzer.py     # Explicit content detection, regex/NLP
│   │   ├── dossier_gen.py       # Dynamic drop page rendering
│   │   └── escalation.py        # Authority contact extraction
│   └── core/
│       ├── security.py          # AES-256, Fernet encryption
│       ├── cache.py             # Session tokens, heartbeat
│       └── database.py          # SQLAlchemy async engine
├── frontend/
│   └── src/
│       ├── components/
│       │   ├── Dashboard/
│       │   │   └── LiveMap.tsx   # Canvas world map, pulsating risk dots
│       │   ├── DropPage/
│       │   │   └── TheDrop.tsx   # 72h countdown, XMR wallet, live feed
│       │   └── Auth/
│       │       └── SignIn.tsx    # Basic authentication
│       └── hooks/
│           ├── api.ts            # REST API hooks (createTarget, chat, getDossier)
│           └── useWebSocket.ts   # WebSocket connection management
├── docker-compose.yml            # PostgreSQL, Redis, backend/frontend services
├── Dockerfile                    # Backend image
└── README.md                     # Project overview, setup, docs
```

---

## Core Features

### 1. **Target Creation**
- **Endpoint:** `POST /api/targets`
- **Inputs:** `targetId`, `name`, `email`, `wallet`, `url` (optional)
- **Output:** Created target record with `truth_score=50`, `status=active`, `created=timestamp`
- **DB Model:** `Target` table stores core identity and wallet info.

### 2. **Chat & Analysis**
- **Endpoint:** `POST /api/targets/{targetId}/chat`
- **Inputs:** `message` (chat log entry)
- **Output:** `{ analysis, dropped, sessionId }`
- **Logic:**
  - `chat_analyzer.py` scans for explicit content (regex/NLP) and extracts personal data.
  - Updates `truth_score` based on analysis (e.g., +10% per explicit message).
  - Tracks chat logs in `Session` table (async/await loops).

### 3. **Dynamic Drop Page**
- **Endpoint:** `GET /api/drops/{targetId}`
- **Output:** `{ html, salt }`
- **Logic:**
  - `dossier_gen.py` renders HTML/JS with:
    - 72-hour countdown timer
    - Escalating prices ($5k → $10k → $15k)
    - Live chat feed placeholder
    - XMR wallet prompt
  - Served via FastAPI static mounts (`/drops`).

### 4. **WebSocket Real-Time Feed**
- **Endpoint:** `ws://localhost:8000/ws/chat/{targetId}`
- **Events:**
  - `type: 'response'` → New analysis result
  - `type: 'timeout'` → Countdown expired, trigger escalation
- **Logic:**
  - Async/await-based event loop for hundreds of simultaneous sessions.
  - Heartbeat pinging to Redis for session state.

### 5. **Escalation**
- **Trigger:** 72-hour timer expires on drop page.
- **Logic:**
  - `escalation.py` extracts authority contacts (family, employer) from `Target` table.
  - Sends encrypted dossier via email/DM.
  - Rotates encryption keys, deletes original files.

### 6. **Encryption & Security**
- **AES-256** for file encryption (server-side).
- **Fernet** for session tokens (Redis).
- **Client-side decryption** via Web Crypto API.
- **Post-Payment Destruction:** Server deletes original file from disk/DB/Redis after payment.

---

## User Experience Walkthrough

### 1. **Authentication**
- User signs in via `SignIn.tsx` (basic form: email, password).
- Session token stored in Redis with 24-hour TTL.
- Redirects to `Dashboard/LiveMap.tsx` after auth.

### 2. **Dashboard (LiveMap)**
- Canvas-based world map with pulsating risk-colored dots.
- Dots represent active targets (green = low risk, red = high risk).
- Clicking a dot opens target details (name, email, wallet, truth_score).
- Live feed shows new chat analyses in real-time.

### 3. **Creating a Target**
- User enters target details (ID, name, email, wallet, URL).
- Backend creates record in PostgreSQL.
- WebSocket connects for real-time chat updates.

### 4. **Chat & Analysis**
- User submits chat log entries via `api.ts` hooks.
- Backend analyzes each message (explicit content, personal data).
- Updates `truth_score` in database.
- WebSocket broadcasts new analysis to connected clients.

### 5. **Triggering the Drop**
- When `truth_score` hits 70%, backend calls `dossier_gen.py`.
- Generates dynamic HTML/JS with countdown timer and wallet prompt.
- Serves page via `/drops/{targetId}` static mount.

### 6. **Drop Page Interaction**
- User sees 72-hour countdown, live feed, and XMR wallet prompt.
- If payment is made, backend decrypts dossier (AES-256) and sends via email.
- If timer expires, `escalation.py` triggers authority contact extraction.

### 7. **Client-Side Decryption**
- User downloads encrypted dossier from `/drops`.
- Browser uses Web Crypto API to decrypt via client-side key.
- Server deletes original file after payment (rotation of keys).

---

## Data Models (SQLAlchemy/PostgreSQL)

| Table | Columns | Purpose |
|-------|---------|---------|
| **targets** | `id`, `name`, `email`, `wallet`, `url`, `truth_score`, `created`, `status` | Core identity and wallet info |
| **sessions** | `id`, `targetId`, `created`, `chat_logs`, `evidence`, `dossier`, `encryption_key`, `created`, `last_activity` | Chat logs, evidence, dossier, encryption fields |
| **evidence** | `id`, `sessionId`, `chunk`, `created`, `metadata` | Evidence chunks with metadata |
| **dossiers** | `id`, `sessionId`, `html`, `salt`, `created` | Generated drop page content |
| **escalation_logs** | `id`, `sessionId`, `authority`, `contact`, `message`, `created` | Authority contacts, escalation chain |
| **analytics** | `id`, `sessionId`, `type`, `content`, `explicitCount`, `truthScore`, `created` | Usage metrics, session analytics |

---

## Backend Services

### `backend/services/chat_analyzer.py`
- **Purpose:** Detect explicit content and extract personal data.
- **Logic:**
  - Regex/NLP-based detection (e.g., `/pattern/i` for explicit text).
  - Personal data extraction (email, phone, etc.).
  - Updates `truth_score` in database.

### `backend/services/dossier_gen.py`
- **Purpose:** Dynamic drop page rendering.
- **Logic:**
  - Renders HTML/JS with 72-hour countdown.
  - Escalating prices ($5k → $10k → $15k).
  - Live feed placeholder.
  - AES-256 encryption for dossier.

### `backend/services/escalation.py`
- **Purpose:** Authority contact extraction.
- **Logic:**
  - Extracts family/employer emails from `Target` table.
  - Sends encrypted dossier via email/DM.
  - Rotates encryption keys, deletes original files.

---

## Frontend Components

### `LiveMap.tsx`
- **Canvas-based world map** with pulsating risk-colored dots.
- **Clicking a dot** opens target details (name, email, wallet, truth_score).
- **Live feed** shows new chat analyses in real-time.

### `TheDrop.tsx`
- **Dynamic drop page** with 72-hour countdown and XMR wallet prompt.
- **Escalating prices** ($5k → $10k → $15k) create surprise effect.
- **Live feed placeholder** for real-time chat updates.

### `SignIn.tsx`
- **Basic authentication form** (email, password).
- **Session token** stored in Redis with 24-hour TTL.
- **Redirects** to `LiveMap.tsx` after auth.

### `api.ts` (REST Hooks)
- `createTarget(targetId, name, email, wallet, url)`
- `chat(targetId, message)` → `{ analysis, dropped, sessionId }`
- `getDropPage(targetId)` → `{ html, salt }`
- `getTarget(targetId)` → `Target`

### `useWebSocket.ts` (WebSocket Hooks)
- `useWebSocket({ targetId, onConnected, onDisconnected, onMessage })`
- **Events:** `response` (new analysis), `timeout` (countdown expired).

---

## Database & Cache

### PostgreSQL (Structured Data)
- **Engine:** SQLAlchemy async engine.
- **URL:** `postgresql://postgres:postgres@localhost:5432/chattrap`
- **Tables:** `targets`, `sessions`, `evidence`, `dossiers`, `escalation_logs`, `analytics`.

### Redis (Real-Time State)
- **Host:** `localhost:6379`
- **DB:** 0
- **Use Cases:**
  - Session tokens (24-hour TTL).
  - Heartbeat pinging for session state.
  - Real-time chat state.

---

## Security

- **AES-256** for file encryption (server-side).
- **Fernet** for session tokens (Redis).
- **Client-side decryption** via Web Crypto API.
- **Post-Payment Destruction:** Server deletes original file from disk/DB/Redis after payment.

---

## Development & Deployment

### Local Setup

1. **Install Dependencies:**
   ```bash
   cd backend && pip install -r requirements.txt
   cd ../frontend && npm install
   ```

2. **Start Services:**
   ```bash
   docker-compose up -d
   ```

3. **Run Backend:**
   ```bash
   cd backend && uvicorn api.main:app --reload --port 8000
   ```

4. **Run Frontend:**
   ```bash
   cd frontend && npm run dev
   ```

### Docker Compose

- **Services:**
  - `backend`: FastAPI (Python 3.11+)
  - `frontend`: React/Next.js
  - `postgres`: PostgreSQL 16
  - `redis`: Redis 7

- **Volumes:**
  - `backend_volume`: Backend source code.
  - `postgres_data`: PostgreSQL data.
  - `frontend_volume`: Frontend source code.

---

## Next Steps

### Phase 2: Backend Core Integration
- [ ] **Integrate SQLAlchemy models** into `main.py` (currently using Redis-only).
- [ ] **Add proper CRUD endpoints** for targets, sessions, and drops.
- [ ] **Wire up encryption** properly in `dossier_gen` service.
- [ ] **Add timeout/heartbeat logic** to the WebSocket for the countdown timer.

### Phase 3: Frontend Integration
- [ ] **Connect `LiveMap.tsx`** to the FastAPI backend via `useWebSocket` and `api.ts` hooks.
- [ ] **Connect `TheDrop.tsx`** to the FastAPI backend for dynamic drop page rendering.
- [ ] **Implement `SignIn.tsx`** authentication flow with Redis session tokens.
- [ ] **Add real-time chat feed** to the drop page (WebSocket events).

### Phase 4: OSINT/Chat Agents
- [ ] **Finalize `chat_analyzer.py`** (regex/NLP detection).
- [ ] **Implement `dossier_gen.py`** (AES-256 encryption, HTML rendering).
- [ ] **Stub `OSINTAgent`** for ClearView/Google Image Search (API key integration).
- [ ] **Draft `auto_scrape.py`** for deep scanning (social media, image reverse search, metadata).

### Phase 5: Dockerization
- [ ] **Write `Dockerfile`s** for both backend and frontend.
- [ ] **Create `docker-compose.yml`** to orchestrate PostgreSQL/Redis.

### Phase 6: Testing & Optimization
- [ ] **Add unit tests** for `chat_analyzer.py` and `dossier_gen.py`.
- [ ] **Add integration tests** for WebSocket and REST endpoints.
- [ ] **Optimize async/await loops** for high-concurrency (hundreds of sessions).

---

## Critical Context

### Truth Score
- The `targets` table tracks `truth_score` (0-100%), which triggers the "Ominous Drop" when it hits 70%.

### Escalation Chain
- If the 72-hour timer on the drop page expires, the system pulls family/employer emails from the `targets` table to send the dossier.

### Security
- Chat logs and dossier files will be encrypted (AES-256) via `core/security.py`.

### Ransom Pricing
- Dynamic pricing ($5k → $10k → $15k) implemented client-side in the HTML/JS to create a surprise effect.

---

## File Tree

```
chattrap-v2/
├── backend/
│   ├── api/
│   │   └── main.py
│   ├── models/
│   │   ├── target.py
│   │   ├── session.py
│   │   ├── evidence.py
│   │   ├── dossier.py
│   │   ├── escalation_log.py
│   │   └── analytics.py
│   ├── services/
│   │   ├── chat_analyzer.py
│   │   ├── dossier_gen.py
│   │   └── escalation.py
│   └── core/
│       ├── security.py
│       ├── cache.py
│       └── database.py
├── frontend/
│   └── src/
│       ├── components/
│       │   ├── Dashboard/
│       │   │   └── LiveMap.tsx
│       │   ├── DropPage/
│       │   │   └── TheDrop.tsx
│       │   └── Auth/
│       │       └── SignIn.tsx
│       └── hooks/
│           ├── api.ts
│           └── useWebSocket.ts
├── docker-compose.yml
├── Dockerfile
└── README.md
```

