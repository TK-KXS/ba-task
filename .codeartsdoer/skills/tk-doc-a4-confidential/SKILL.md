---
name: tk-doc-a4-confidential
description: TK Company house format for formal deliverables — standalone A4 HTML document (portrait and landscape pages) with "TK Company – Confidential" stamped in the header and footer of every page, cover page, document control and page numbers. Use whenever producing any TK document or diagram pack as HTML (requirements spec, functional spec, architecture/flow document).
---

# TK A4 Confidential Document Format

Shared by all TK document skills (`tk-ba-requirements`, `tk-solution-architecture`).

## Mandatory

1. **One self-contained `.html` file** — no external CSS/JS except Google Fonts (must still render if fonts fail). Pinned CDN scripts only when a skill explicitly allows it.
2. **"TK Company – Confidential" in the header *and* footer of every page**, on screen and in print, plus **page number** in the footer.
3. **Document ID** in the header: `TK-<TEAM>-<PROJECT>-<TYPE>-<nn>` (e.g. `TK-BA-SMR-REQ-01`, `TK-SA-SMR-ARC-01`) and version.
4. **Cover page**: TK text mark, document title, project, customer, document ID, version, date, classification "CONFIDENTIAL".
5. **Document control**: version history table, author, reviewers, approvers with signature/date lines.
6. **Table of contents** with section numbers.
7. Optional faint diagonal watermark `TK CONFIDENTIAL` per page (opacity ≤ 0.05).

## Layout rules

- Each page is a `<section class="page">`: portrait 210 × 297 mm, or `class="page landscape"` 297 × 210 mm for wide diagrams. 20 mm side margins.
- Content must never overflow a page. Split long tables across pages and repeat the table header.
- Formal look: *Sarabun* (Thai) + *IBM Plex Sans/Mono*, dark-navy ink, one accent colour, thin table borders, no emoji, no gradients.
- IDs in monospace.

## Skeleton

```html
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>SiamMart Returns – Requirements Specification</title>
<link href="https://fonts.googleapis.com/css2?family=Sarabun:wght@400;600;700&family=IBM+Plex+Mono&display=swap" rel="stylesheet">
<style>
  @page { size: A4; margin: 0; }
  @page landscape { size: A4 landscape; }
  :root { --ink:#1b2333; --accent:#0b3d91; --line:#c9ced8; --muted:#5b6475; }
  body { margin:0; background:#e9ebef; font-family:'Sarabun',sans-serif; color:var(--ink); font-size:11pt; }
  .page { width:210mm; height:297mm; padding:24mm 20mm 22mm; margin:10mm auto; background:#fff;
          box-sizing:border-box; position:relative; overflow:hidden; box-shadow:0 1px 4px rgba(0,0,0,.15);
          page-break-after:always; }
  .page.landscape { width:297mm; height:210mm; page:landscape; }
  .page-header, .page-footer { position:absolute; left:20mm; right:20mm; font-size:8.5pt; color:var(--muted);
          display:flex; justify-content:space-between; }
  .page-header { top:10mm; border-bottom:1px solid var(--line); padding-bottom:2mm; }
  .page-footer { bottom:10mm; border-top:1px solid var(--line); padding-top:2mm; }
  .confidential { color:#a40000; font-weight:700; letter-spacing:.06em; }
  table { width:100%; border-collapse:collapse; font-size:9.5pt; }
  th, td { border:1px solid var(--line); padding:4px 6px; vertical-align:top; text-align:left; }
  th { background:#eef1f6; }
  code, .id { font-family:'IBM Plex Mono',monospace; font-size:9pt; }
  @media print { body { background:#fff; } .page { margin:0; box-shadow:none; } }
</style>
</head>
<body>
  <section class="page">
    <div class="page-header"><span>TK-BA-SMR-REQ-01 · v0.1</span><span class="confidential">TK COMPANY – CONFIDENTIAL</span></div>
    <!-- page content -->
    <div class="page-footer"><span class="confidential">TK Company – Confidential · Do not distribute without written consent</span><span>Page 1</span></div>
  </section>
</body>
</html>
```

## Checklist

- [ ] "TK Company – Confidential" in header and footer of **every** page, with page number.
- [ ] Cover, document control, TOC present.
- [ ] Opens offline as a single file; prints to A4 with nothing clipped.
