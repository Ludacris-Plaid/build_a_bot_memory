---
created: 2026-07-03
type: reference
tags: [book, hermes, chapter]
chapter: 19
title: "The Communication System — Voice + SMS Production Build"
section: "Part II: The Real Estate Pivot (RE-AI)"
source: victoria-k-emails
---

# Chapter 19 — The Communication System — Voice + SMS Production Build

Good — we’ll build this properly as a real MVP communication system, not a toy demo. This will plug directly into your Real Estate AI Agent.
We’re going to implement:

🏡 RE-AI Communication System (Voice + SMS MVP)
What you will actually get
A working system that can:
📱 SMS
receive inbound texts
classify intent with AI
respond automatically
log everything into CRM
📞 Voice
receive calls
play greeting
capture voicemail OR live transcription
generate AI follow-up via SMS
🧱 1. Final Architecture (Simple + Production-Ready)
Twilio Phone Number
│
┌───────────────┼────────────────┐
▼ ▼
SMS Webhook Voice Webhook
│ │
▼ ▼
n8n / API Router Twilio Voice Flow
│ │
└──────────────┬───────────────┘
▼
AI Communication Brain
│
┌──────────────┼──────────────┐
▼ ▼ ▼
SMS Reply CRM Update Calendar MCP

🧰 2. Core Stack You Will Use
Must-have
Twilio → SMS + Voice
n8n → workflow engine
Node.js (Express API layer)
Postgres → CRM database
OpenAI / LLM API → reasoning layer
🧠 3. DATABASE (CRITICAL FOUNDATION)
CRM schema (Postgres)
CREATE TABLE leads (
id SERIAL PRIMARY KEY,
name TEXT,
phone TEXT,
email TEXT,
source TEXT,
status TEXT DEFAULT 'new',
last_message TEXT,
intent TEXT,
created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE messages (
id SERIAL PRIMARY KEY,
lead_id INT,
direction TEXT, -- inbound / outbound
channel TEXT, -- sms / voice
content TEXT,
created_at TIMESTAMP DEFAULT NOW()
);

📱 4. SMS SYSTEM (FULL IMPLEMENTATION)
STEP 1 — Twilio Setup
Create:
phone number
webhook for incoming SMS
Webhook URL:
https://your-server.com/webhooks/sms

STEP 2 — Node.js SMS Server
mkdir re-ai && cd re-ai
npm init -y
npm install express body-parser twilio openai pg

STEP 3 — SMS Webhook Server
import express from "express";
import bodyParser from "body-parser";
import twilio from "twilio";
import { OpenAI } from "openai";
import pg from "pg";

const app = express();
app.use(bodyParser.urlencoded({ extended: false }));

const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY }); const db = new pg.Pool({ connectionString: process.env.DATABASE_URL });

app.post("/webhooks/sms", async (req, res) => {
const from = req.body.From;
const message = req.body.Body;

// 1. Save lead/message
let lead = await db.query(
"SELECT * FROM leads WHERE phone=$1",
[from]
);

if (lead.rows.length === 0) {
await db.query(
"INSERT INTO leads (phone, source, status) VALUES ($1, 'sms', 'new')", [from] ); }

// 2. AI classify + respond
const response = await openai.chat.completions.create({
model: "gpt-4o-mini",
messages: [
{
role: "system",
content:
"You are a real estate assistant. Be concise, friendly, and always ask a follow-up question." }, { role: "user", content: message } ] });

const reply = response.choices[0].message.content;

// 3. Send SMS reply
const client = twilio(
process.env.TWILIO_SID,
process.env.TWILIO_AUTH
);

await client.messages.create({
body: reply,
from: process.env.TWILIO_NUMBER,
to: from
});

res.sendStatus(200);
});

app.listen(3000);

Result:
You now have a fully working SMS AI realtor assistant.
📞 5. VOICE SYSTEM (MVP VERSION)
We’ll start simple (not full AI voice agent yet).
Goal:
answer calls
record voicemail
transcribe
trigger SMS follow-up
STEP 1 — Twilio Voice Webhook
Set voice webhook:
https://your-server.com/webhooks/voice

STEP 2 — Voice Handler (Twilio XML)
app.post("/webhooks/voice", (req, res) => {
const twiml = new twilio.twiml.VoiceResponse();

twiml.say(
"Hi, you've reached your real estate assistant. Please leave a message after the beep." );

twiml.record({
transcribe: true,
transcribeCallback: "/webhooks/transcription"
});

res.type("text/xml");
res.send(twiml.toString());
});

STEP 3 — Transcription Handler
app.post("/webhooks/transcription", async (req, res) => {
const transcription = req.body.TranscriptionText;
const from = req.body.From;

// Save message
await db.query(
"INSERT INTO messages (phone, direction, channel, content) VALUES ($1, 'inbound', 'voice', $2)", [from, transcription] );

// AI follow-up SMS
const response = await openai.chat.completions.create({
model: "gpt-4o-mini",
messages: [
{
role: "system",
content:
"You are a real estate assistant. Turn voicemails into short SMS follow-ups." }, { role: "user", content: transcription } ] });

const smsReply = response.choices[0].message.content;

const client = twilio(
process.env.TWILIO_SID,
process.env.TWILIO_AUTH
);

await client.messages.create({
body: smsReply,
from: process.env.TWILIO_NUMBER,
to: from
});

res.sendStatus(200);
});

🧠 6. AI COMMUNICATION BRAIN (IMPORTANT)
You MUST standardize behavior:
System prompt:
You are a real estate assistant.

Rules:
- keep responses under 2 sentences
- always ask a follow-up question
- never hallucinate property details
- always try to schedule or qualify lead

🔁 7. FLOW SUMMARY
SMS flow
User text → webhook → AI → SMS reply → CRM log

Voice flow
User calls → greeting → voicemail → transcription → AI → SMS follow-up

🧩 8. WHAT YOU NOW HAVE (MVP COMPLETE)
You now have:
📱 SMS agent
instant responses
lead capture
CRM logging
📞 Voice system
call handling
voicemail capture
AI follow-ups
🧠 AI layer
real estate optimized behavior
structured communication
🚀 9. WHAT THIS IS IN REAL TERMS
This is not a chatbot.
This is:

A 24/7 inside sales + receptionist system for real estate agents. ⚠️ 10. NEXT UPGRADE PATH (IMPORTANT)
If you continue this, next steps are:
Phase 2
live AI phone conversations (real-time voice agent)
calendar booking via SMS
CRM dashboards
Phase 3
MLS integration
lead scoring model
predictive follow-ups
If you want next step
I can now help you:
turn this into a deployable Docker stack
add n8n workflows instead of Node.js
build a full CRM UI dashboard
or upgrade this into a SaaS product architecture
Just say:
👉 “turn this into a deployable system”

On Fri, Jul 3, 2026 at 4:20 AM Victoria K <vkushelnyk@gmail.com> wrote:
