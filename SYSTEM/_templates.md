---
created: 2026-07-03
type: system
---

# 📋 Templates

## Session Log (DIARY)

```markdown
---
created: {{date}}
type: diary
tags: [session]
---

# {{date}} — {{title}}

**Topics:** 
**Key Decisions:**

## Summary


## Action Items

- [ ]
```

## Project Note (JOBS)

```markdown
---
created: {{date}}
type: job
tags: []
status: active
---

# {{title}}

**Status:** Active
**Priority:** Medium
**Deadline:**

## Context


## Tasks

- [ ] 
```

## Client Note (CLIENTS)

```markdown
---
created: {{date}}
type: client
tags: [client]
status: active
---

# {{name}}

**Contact:**
**Scope:**
**Rate:**
**Status:** Active

## Notes


## Work Log

- {{date}} — 
```

## Lead (LEADS)

```markdown
---
created: {{date}}
type: lead
tags: [lead]
status: warm
---

# {{name}}

**Contact:**
**Source:**
**Stage:** Discovery
**Next Action:**

## Notes

```

## Idea (IDEAS)

```markdown
---
created: {{date}}
type: idea
tags: [idea]
status: draft
---

# {{title}}

**Viability:** High / Medium / Low
**Effort:** Small / Medium / Large

## The Idea


## Potential Next Steps

- [ ]
```