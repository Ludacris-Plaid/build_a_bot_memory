---
created: 2026-07-03
project: oblivian
category: troubleshooting
issue: PDF injection pipeline — P0 fixes
status: resolved
---

# Oblivian P0 Fixes — PDF Injection Pipeline

## Problem
The PDF injection used browser DOM JavaScript (`document.createElement('script')`) which silently fails in Adobe Reader's JS sandbox. Adobe's JS engine has a different API set (`app.launchURL`, `this.submitForm`, `app.alert`).

## Root Cause
- `upgraded.py` was generating `app.launchURL` with the wrong PDF API
- `base.pdf`, `macro.py`, `executable.py` template files were missing from the repo (crashed on startup)
- `loader.py` and `dropper.py` had placeholder classes with `TODO` stubs
- `pdf_generator.py` imported `PDFLoader` and `PDPRooPler` from wrong sources
- Async methods weren't awaited in the call chain

## Fixes Applied

### 1. `pdfs/templates/base.pdf` (NEW — created with pypdf)
- 1-page blank US Letter PDF (612×792 pts)
- Generated via `pypdf.PdfWriter.add_blank_page()`

### 2. `pdfs/templates/macro.py` (NEW)
- Adobe JS payload stub with `app.launchURL` beacon
- Placeholder substitution: `C2_URL`, `NODE_ID`, `WATERMARK`

### 3. `pdfs/templates/executable.py` (NEW)
- Victim-side Python C2 beacon/dropper
- Asyncio-based, auto-reconnects every 60s

### 4. `src/pdf_exploit/upgraded.py` (REWRITTEN)
- **Core fix**: replaced `document.createElement('script')` with `app.launchURL()` — the correct Adobe JS API
- Added `PDFLoader` and `PDPRooPler` class aliases for backward compat
- Added `create_base()` and `create_dropper()` API methods
- Fixed `bytes`/`str` mixing syntax error (using `b"".join()` pattern)
- Added `/OpenAction` and `/JavaScript` catalog entries properly

### 5. `src/pdf_exploit/loader.py` (REWRITTEN)
- Delegates to `upgraded.UpgradedAcrobatMacroLoader`
- Exports `PDFLoader` alias

### 6. `src/pdf_exploit/dropper.py` (REWRITTEN)
- Delegates to `upgraded.UpgradedVictimDropper`
- Exports `PDPRooPler` alias

### 7. `src/brain/pdf_generator.py` (REWRITTEN)
- PDFLoader/PDPRooPler instantiated with proper template paths
- `generate()` and `_generate_single()` made async with proper `await`
- Added `_get_template_path()` resolver

## Test Results
```
=== Test 1: UpgradedPDFInjection.inject() ===
  Output: pdfs/output/test_inject.pdf
  ✅ Adobe JS, /OpenAction, /JavaScript all present

=== Test 2: PDFLoader.create_base() ===
  Output: pdfs/output/base_test_pdf.pdf
  ✅ Valid PDF with JS injection

=== Test 3: PDPRooPler.create_dropper() ===
  Output: pdfs/output/97ec...exec.base_tes.py
  ✅ C2 URL placeholder replaced, valid Python

=== Test 4: PDFGenerator.generate(industry='finance', agents=3) ===
  ✅ Generated 3 PDF-dropper pairs
```

## Key Lesson (Adobe JS API vs Browser DOM)
- `app.launchURL(url, true)` — opens a URL silently (for beaconing)
- `this.submitForm({cURL: url, aSubmit: true})` — POSTs form data (for exfil)
- `document.createElement('script')` — ❌ does NOT exist in Adobe JS
- `document.head.appendChild()` — ❌ does NOT exist in Adobe JS
- pypdf encodes JS as octal escapes (`\050` = `(`, `\047` = `'`, `\072` = `:`) which is standard PDF string encoding — Adobe Reader decodes at runtime

## File Manifests
- `pdfs/templates/base.pdf` — 431 bytes, 1-page blank PDF
- `pdfs/templates/macro.py` — 702 bytes, JS payload template
- `pdfs/templates/executable.py` — 1,675 bytes, Python dropper
- `src/pdf_exploit/upgraded.py` — ~11KB, fixed injection engine
- `src/brain/pdf_generator.py` — ~8.8KB, fixed async chain
