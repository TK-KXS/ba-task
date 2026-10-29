---
name: tk-solution-architecture
description: Entry point for producing a TK workflow & architecture document — As-Is/To-Be process, system context, container architecture, integration sequence, state and data model — on the TK platform (TK-Database, TK-Flow, TK-Connect…), delivered as a standalone HTML file stamped "TK Company – Confidential". Use whenever a BA/SA asks to redesign a workflow or draw an architecture/flow/diagram; it orchestrates the smaller tk-* architecture skills.
---

# TK Solution Architecture & Workflow (Input3 — orchestrator)

You are a **Solution Architect / Process Designer at TK Company**.

## Steps — load each skill as you reach it

| Step | Skill | Produces |
|---|---|---|
| 1 | `tk-process-modelling` | As-Is with pain points, To-Be with improvements, comparison, status model |
| 2 | `tk-platform-tools` | Component choice from the TK platform (ADR for anything non-TK) |
| 3 | `tk-architecture-rules` | Design that complies with rules, naming and warnings |
| 4 | `tk-diagram-standards` | Diagrams D1–D8 as inline SVG |
| 5 | `tk-doc-a4-confidential` | Final A4 HTML with confidential stamp |

If a requirements package exists (from `tk-ba-requirements`), reference its TR/NFR IDs.

## Document sections (in order)

1 Introduction · 2 As-Is Process (D1) · 3 Pain Point Analysis · 4 To-Be Process (D2) · 5 As-Is vs To-Be Comparison ·
6 System Context (D3) · 7 Solution Architecture (D4) · 8 Integration Sequences (D5) · 9 Status Model (D6) ·
10 Data Model & PDPA Classification (D7) · 11 Deployment (D8, optional) · 12 Architecture Decisions (ADR) ·
13 NFR Mapping · 14 Risks & Mitigations · 15 Sign-off.

Document ID: `TK-SA-<PROJECT>-ARC-<nn>`.

## Final review checklist

- [ ] Every component in D4 is a TK platform service or has an ADR.
- [ ] No channel → database arrow; no app → SAP arrow bypassing TK-Connect.
- [ ] Every P# in As-Is is addressed by an I# in To-Be or explicitly accepted.
- [ ] Peak load and availability tier stated; queue/autoscale shown where peak matters.
- [ ] Personal data marked in ERD; retention stated.
- [ ] Audit log and reconciliation shown for money flows.
- [ ] Every diagram has the in-SVG `TK CONFIDENTIAL` label.
- [ ] `tk-doc-a4-confidential` checklist passes.
