---
name: tk-ba-user-stories
description: TK standard for writing user stories — epics, "As a / I want / so that" format, INVEST, Gherkin acceptance criteria with negative scenarios, sizing and links to TRs. Use when writing or reviewing user stories or acceptance criteria.
---

# TK BA — User Stories

Format:
> **US-012** · As a **store staff**, I want to **scan the customer's receipt** so that **I don't have to type the order details**.

- Follow **INVEST** (Independent, Negotiable, Valuable, Estimable, Small, Testable).
- Group stories under **Epics** (`EP-01 Customer Return Request`, …).
- Each story lists: priority (MoSCoW), size placeholder (story points or T-shirt), linked `TR-` IDs.
- **Acceptance criteria in Gherkin**, at least one negative scenario per Must story:

```
Scenario: Valid receipt scanned
  Given I am logged in as store staff at branch "Bangna"
  When I scan receipt barcode "R-2026-000123"
  Then the system shows the order lines eligible for return
  And items outside the return window are shown as disabled with the reason

Scenario: Receipt from another retailer
  Given I am logged in as store staff
  When I scan a barcode that does not match any SiamMart order
  Then the system shows "Receipt not found" and offers manual search
```

## Story table

| ID | Epic | Story | Priority | Size | TR links |
|---|---|---|---|---|---|
