Add a new persistent bottom nav tab: 📨 SMS Spam (position: after Dialer, before Scripts).

SMS Spam Screen Features:
- Single & Bulk send (CSV/TXT upload with phone numbers).
- Sender ID field: any alphanumeric string (e.g. "WellsFargo", "TD Bank Security").
- Message input with template variables.
- Premium AI buttons: "Generate with ScriptForge AI" and "Improve Message" (uses same Featherless 12B model with adapted prompt for SMS).
- Real-time progress, delivery status, history log.
- Pricing: Deduct tokens per message sent (higher for AI-generated).

Integrate GENSMS as primary SMS provider with custom Sender ID support. Create abstraction layer for easy addition of more gateways.