---
name: tk-platform-tools
description: Catalogue of TK Company's standard platform services — TK-Database, TK-Gateway, TK-Auth, TK-Flow, TK-Queue, TK-Notify, TK-Storage, TK-Connect, TK-DataLake, TK-Monitor, TK-Vault, TK-Cloud — with purpose, usage and limits. Use when choosing components for a solution or checking what a TK tool can do.
---

# TK Platform Tools

Always prefer TK platform services over third-party products. If a third-party product is
genuinely needed, record an **Architecture Decision Record (ADR)** with the reason.

| Tool | What it is | Use for | Notes / limits |
|---|---|---|---|
| **TK-Database** | Managed relational DB (PostgreSQL 16 based), HA pair + read replica, daily backup, PITR 14 days | All transactional data | One schema per domain service. Max 2 TB per instance. Encryption at rest on by default. |
| **TK-Gateway** | API gateway (REST/GraphQL), rate limiting, API keys, OAuth2 | **Every** external or cross-domain API call | Default rate limit 100 req/s per client. APIs versioned `/v1/…`. |
| **TK-Auth** | Identity & SSO (OIDC/SAML), AD/Azure AD federation, MFA | Staff login, customer login, service tokens | Customer and staff identities in separate realms. |
| **TK-Flow** | Workflow / BPM engine (BPMN 2.0), human tasks, SLA timers, escalation | Approvals, multi-step processes, status models | Business rules live in TK-Flow DMN tables, not hard-coded. |
| **TK-Queue** | Message broker (Kafka-compatible) | Async events, integration decoupling, peak buffering | Events `<domain>.<entity>.<event>`. Retention 7 days. |
| **TK-Notify** | Notification hub: email, SMS, LINE OA, push | All customer/staff notifications | Templates per language (TH/EN). SMS ~0.35–0.50 THB/msg billed to project. |
| **TK-Storage** | Object storage (S3-compatible) with lifecycle policies | Images, documents, exports | Signed URLs only; no public buckets. Cold tier after 90 days. |
| **TK-Connect** | Integration adapters (SAP RFC/BAPI/IDoc, SFTP, marketplace APIs) | Legacy & ERP integration | **Only** approved path to SAP. Built-in retry + dead-letter queue. |
| **TK-DataLake** | Analytics warehouse + BI dashboards | Reporting, KPIs, executive views | Fed by CDC from TK-Database or TK-Queue events. |
| **TK-Monitor** | Logs, metrics, tracing, alerting | Observability for every service | Structured JSON logs with `traceId`. |
| **TK-Vault** | Secrets & key management | Credentials, API keys, encryption keys | No secrets in code or git. |
| **TK-Cloud** | TK-hosted Kubernetes runtime (Bangkok DC primary, Chonburi DR) | Hosting all services | Data residency in Thailand by default. |

## Quick picker

| Need | Use |
|---|---|
| Store orders / requests | TK-Database |
| Approval with SLA | TK-Flow |
| Talk to SAP / POS / Shopee | TK-Connect |
| Customer status updates | TK-Notify (LINE OA / email first) |
| Photos, attachments | TK-Storage |
| Executive dashboard | TK-DataLake |
| Absorb 11.11 peak | TK-Queue + autoscale on TK-Cloud |
