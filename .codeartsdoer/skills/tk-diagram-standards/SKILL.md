---
name: tk-diagram-standards
description: TK standard set of architecture/flow diagrams (D1–D8: As-Is, To-Be, C4 context, container, sequence, state, ERD, deployment) and visual conventions for drawing them as inline SVG, including the in-diagram "TK CONFIDENTIAL" label. Use when drawing any TK architecture, flow or process diagram.
---

# TK Diagram Standards

## Required diagram set

| # | Diagram | Purpose |
|---|---|---|
| D1 | As-Is swimlane process | Current state with pain points |
| D2 | To-Be swimlane process | Improved process with improvement markers |
| D3 | System context (C4 level 1) | Solution, its users, external systems (SAP, POS, marketplaces, payment) |
| D4 | Container architecture (C4 level 2) | TK platform services used and how they connect |
| D5 | Key integration sequence | e.g. Refund: Approval → TK-Connect → SAP → Payment → Notify |
| D6 | State diagram | Status lifecycle of the core entity |
| D7 | Logical data model (ERD) | Main entities in TK-Database with PDPA classification |
| D8 | Deployment view (optional) | TK-Cloud DC/DR, DEV/SIT/UAT/PROD |

Under each diagram: a short **legend** and **notes** (assumptions, open points).

## Drawing rules

- Draw as **inline SVG** (works offline, prints sharply). Mermaid only if pinned
  (`https://cdn.jsdelivr.net/npm/mermaid@10.9.1/dist/mermaid.min.js`) and the document notes it needs internet.
- Wide diagrams go on landscape pages (`tk-doc-a4-confidential`).
- Max ~12 boxes per diagram — split if bigger. Fonts ≥ 9pt when printed.
- Every SVG carries a `TK CONFIDENTIAL` label in its bottom-right corner, so a screenshot of one diagram stays marked.

## Visual conventions

| Element | Style |
|---|---|
| TK platform service | Navy fill `#0b3d91`, white text, label prefixed `TK-` |
| Customer / external system | Grey outline `#5b6475`; dashed border if not yet confirmed |
| Human actor / lane | Lane background `#f3f5f9`, lane title on the left |
| Sync call | Solid arrow, label `REST` / `RFC` |
| Async event | Dashed arrow, label = event name |
| Pain point | Red circle `#c62828` with `P#` |
| Improvement | Green circle `#2e7d32` with `I#` |
| Data store | Cylinder shape |

## Page snippet

```html
<section class="page landscape">
  <div class="page-header"><span>TK-SA-SMR-ARC-01 · v0.1 · D2 To-Be Process</span><span class="confidential">TK COMPANY – CONFIDENTIAL</span></div>
  <h2>D2 · To-Be Return &amp; Refund Process</h2>
  <svg viewBox="0 0 1100 560" role="img" aria-label="To-Be swimlane">
    <!-- lanes, boxes, arrows -->
    <text x="1090" y="552" text-anchor="end" font-size="10" fill="#a40000">TK CONFIDENTIAL</text>
  </svg>
  <div class="notes">…legend & notes…</div>
  <div class="page-footer"><span class="confidential">TK Company – Confidential · Do not distribute without written consent</span><span>Page 4</span></div>
</section>
```
