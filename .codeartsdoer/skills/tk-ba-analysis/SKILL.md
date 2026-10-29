---
name: tk-ba-analysis
description: TK BA method for analysing rough customer input (meeting notes, emails, messy .md) — classify statements, find the real business problem, flag stakeholder conflicts, translate vague business language into measurable technical terms, and extract business rules. Use as the first step before writing scope, TRs, functional specs or user stories.
---

# TK BA — Requirement Analysis & Translation

## 1. Extract
Read the raw input line by line and tag every statement as one of:
`Goal` · `Pain point` · `Requirement (want)` · `Constraint` · `Assumption` · `Conflict` · `Open question` · `Noise`.
Keep the source reference (e.g. "Kickoff 22-Oct, K.Somchai").

## 2. Find the real problem
For every "want", ask *why* until you reach a measurable business outcome.
"อยากได้ระบบที่ทุกอย่างอยู่ที่เดียว" → *Reduce refund lead time from 14 days to ≤ 3 days.*

## 3. Resolve or flag
Conflicts between stakeholders are **never** silently resolved by the BA.
Record them as Open Issues (`OI-xx`) with both positions, decision owner and due date.

| ID | Topic | Position A | Position B | Decision owner | Due |
|---|---|---|---|---|---|

## 4. Translate (Business → Technical)

| Business says | BA must turn it into |
|---|---|
| "ต้องเร็ว", "fast" | A number: p95 response time, throughput, SLA hours |
| "ใช้ง่าย" | Measurable UX: ≤ N taps per task, font size, task time, training ≤ 30 min |
| "ปลอดภัย", "PDPA" | Controls: data classification, encryption, consent, retention, access roles |
| "รองรับ peak" | Load figure with source: e.g. 5× average = 4,200 returns/day, 50 concurrent users |
| "เชื่อมระบบ X" | Integration: system, direction, protocol, frequency, data objects, owner, error handling |
| "dashboard" | KPI list with formula, source, refresh frequency, audience |
| "แจ้งเตือน" | Event → channel → recipient → template → timing table |
| "auto approve" | A business rule with ID, condition, action, exception path |
| Vague number (18k? 25k?) | Size with the higher value, flag as assumption, assign owner to confirm |

**Rule of thumb:** if a tester cannot write a pass/fail test from the sentence, it is not a requirement yet.

## 5. Business rules
Pull every piece of decision logic into a rule table — don't bury rules inside stories.

| ID | Rule | Condition | Action | Source | Status |
|---|---|---|---|---|---|
| BRL-001 | Manager approval | Refund amount > 5,000 THB | Route to store manager | Kickoff, K.Somchai | Confirmed |

## Output of this step
Statement log · Business objectives (SMART) · Business rules (BRL) · Open issues & conflicts (OI) · Assumptions (AS).
These feed `tk-ba-scope`, `tk-ba-technical-requirements`, `tk-ba-functional-spec` and `tk-ba-user-stories`.
