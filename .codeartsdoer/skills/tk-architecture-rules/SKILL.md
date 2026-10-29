---
name: tk-architecture-rules
description: TK Company mandatory architecture rules, naming conventions and known warnings/pitfalls (SAP direct access, auto-approval of money, Excel integration, SMS cost, image retention, marketplace APIs, pilot rollout). Use when designing or reviewing any TK solution architecture.
---

# TK Architecture Rules & Conventions

## Mandatory rules

**Structure**
1. **Domain separation** – one service owns its data. Others access it only via API (TK-Gateway) or events (TK-Queue). **No cross-schema SQL joins.**
2. **Layering** – Channel (Web / Tablet / LINE OA) → TK-Gateway → Domain services → TK-Database / TK-Storage. Channels never talk to databases.
3. **Integration** – synchronous only when the user is waiting; everything else async via TK-Queue.
4. **Legacy/ERP** – all SAP, POS or marketplace traffic goes through TK-Connect.
5. **Workflow** – any process with human approval, SLA or > 3 statuses is modelled in TK-Flow, not application if/else.
6. **Reporting** – dashboards read from TK-DataLake, never from production TK-Database.

**Security & compliance**
7. **PDPA** – classify every entity (Public / Internal / Confidential / Personal / Sensitive Personal). Personal data: encrypted in transit and at rest, masked in logs, retention + deletion job defined.
8. **Least privilege** – role-based access via TK-Auth; branch-level data scoping for store staff.
9. **Audit trail** – every approval, refund and status change goes to an immutable audit log (who, what, when, before/after).
10. **Financial data** – refunds/payments are idempotent (idempotency key) and reconciled daily.

**Operations**
11. **Availability tiers** – Tier 1 (customer-facing, money): 99.9%, RTO 1h, RPO 15 min. Tier 2 (internal): 99.5%, RTO 4h, RPO 1h.
12. **Peak readiness** – size for documented peak × 1.5; TK-Queue absorbs bursts; stateless services autoscale.
13. **Observability** – health endpoint, metrics and alerts defined in TK-Monitor before go-live.

## Naming conventions

- Services: `tk-<customer>-<domain>-svc` e.g. `tk-smr-returns-svc`
- DB schema: `<domain>` lower_snake_case; plural tables (`return_requests`); PK `id` UUID; `created_at`, `updated_at` in UTC.
- APIs: `/v1/<resource>` plural, kebab-case; e.g. `POST /v1/return-requests`.
- Events: `<domain>.<entity>.<past-tense-verb>` e.g. `returns.request.approved`.

## Warnings, remarks & notices

> ⚠ **WARNING – SAP direct access**: customer IT often offers RFC credentials "to go faster". Decline; use TK-Connect. Direct RFC calls have caused month-end lockouts on past projects.

> ⚠ **WARNING – Auto-approval of money**: any rule releasing money without a human needs written sign-off from the customer's Finance/Audit owner. Model it as a configurable DMN rule in TK-Flow so the threshold can change (or be 0) without deployment.

> ⚠ **WARNING – Excel as integration**: "daily Excel export" is fine as a report, never as an interface between systems.

> ℹ **REMARK – SMS cost**: prefer LINE OA / email for status updates; SMS only for OTP and critical events.

> ℹ **REMARK – Image storage**: with 7-year retention, compress photos to ≤ 500 KB and move to cold tier after 90 days.

> ℹ **NOTICE – Marketplaces**: Shopee/Lazada APIs change without notice and are rate-limited. Isolate behind TK-Connect; treat as a separate phase.

> ℹ **NOTICE – Pilot rollout**: use per-branch feature flags so pilot branches run the new process while others stay on the old one.
