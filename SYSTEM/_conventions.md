---
created: 2026-07-03
type: system
---

# 📐 Note Conventions

## Frontmatter

Every note gets YAML frontmatter:

```yaml
---
created: 2026-07-03
type: diary | client | idea | job | lead | reference | system
tags: [tag1, tag2]
status: active | archived | draft
---
```

## Naming

- Files: `YYYY-MM-DD.md` for diary, `kebab-case-name.md` for everything else
- No spaces in filenames
- Use `[[WikiLinks]]` to cross-reference

## Diary Format

```markdown
---
created: 2026-07-03
type: diary
tags: [session]
---

# 2026-07-03 — Session Title

**Topics:** what we covered
**Key Decisions:** 
- Decision 1
- Decision 2

## Summary

Freeform session summary.

## Action Items

- [ ] Task 1
- [ ] Task 2
```

## Tags

- `#session` — auto-logged conversation
- `#idea` — brainstorm
- `#active` — current work
- `#archived` — done/dead
- `#client` — client-related
- `#lead` — sales/opportunity