---
name: tk-ba-functional-spec
description: TK template for Functional Specification (FS) sections — purpose, actors, pre/post-conditions, main/alternative/exception flows, business rules, screen field definitions, status model, notifications and reports. Use when specifying how a feature or module behaves.
---

# TK BA — Functional Specification

Write one FS section per feature/module (`FS-<MOD>-nn`):

1. **Purpose** – what the feature does, in one paragraph.
2. **Actors** – who uses it.
3. **Pre-conditions / Post-conditions**
4. **Main flow** – numbered steps, `User action → System response`.
5. **Alternative & exception flows** – e.g. `4a. Receipt not found → system shows manual search`.
6. **Business rules applied** – reference `BRL-` IDs (don't restate the logic).
7. **Screen / field definition**

   | Field | Type | Mandatory | Validation | Source | Remark |
   |---|---|---|---|---|---|

8. **Status model** – every status and allowed transitions, e.g.
   `Requested → Approved → Received → Refunded → Closed`, plus `Rejected`, `Cancelled`.
9. **Notifications**

   | Event | Channel | Recipient | Template | Timing |
   |---|---|---|---|---|

10. **Reports / data output** – if any.
11. **Linked requirements** – `TR-` / `US-` IDs.
