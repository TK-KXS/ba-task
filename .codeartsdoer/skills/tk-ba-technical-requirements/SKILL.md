---
name: tk-ba-technical-requirements
description: TK standard for writing Technical Requirements (TR), Non-Functional Requirements (NFR) and Integration Requirements (INT) — ID conventions, "The system shall" template, NFR coverage checklist. Use when writing or reviewing technical/functional requirements statements.
---

# TK BA — Technical Requirements

Every requirement has an ID and a single testable statement: **"The system shall …"**.

```
ID:          TR-RET-012
Title:       Retrieve order by receipt barcode
Statement:   The system shall retrieve the original sales order from POS within 2 seconds
             when a store user scans a receipt barcode (Code128 / QR).
Priority:    Must
Source:      Kickoff 22-Oct-2026, K.Nok
Rationale:   Removes manual re-keying, the #1 source of data errors in the current process.
Acceptance:  Given a valid receipt barcode, the order header and lines are displayed in ≤ 2s (p95).
Dependency:  INT-POS-01 (POS order API)
Status:      Draft | Reviewed | Approved
```

## ID convention

| Prefix | Meaning |
|---|---|
| `BR-` | Business Requirement (the why) |
| `TR-<MOD>-` | Technical / functional requirement per module |
| `NFR-<CAT>-` | Non-functional (PERF, SEC, AVAIL, SCAL, USAB, COMP, DATA) |
| `INT-<SYS>-` | Integration requirement |
| `BRL-` | Business rule |
| `US-` / `EP-` | User story / Epic |
| `AS-` / `OI-` | Assumption / Open issue |

## Integration requirement fields
System · Direction · Protocol · Trigger/frequency · Data objects · Volume · Error handling & retry · Owner.

## NFR checklist — cover every row (or mark N/A with reason)
Performance · Scalability (peak) · Availability & RTO/RPO · Security & access control ·
Privacy / PDPA (consent, retention, right to erasure) · Audit logging · Usability & accessibility ·
Localization (TH/EN) · Data retention & archiving · Supportability (logging, monitoring) · Browser/device support.

## Banned words without numbers
"fast", "user-friendly", "flexible", "etc.", "and so on", "robust", "scalable".
