#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build TK-BA-SMR-REQ-01.html — SiamMart Returns requirements package.
Generates a single self-contained A4 HTML with confidential header+footer and
sequential page numbers on every page."""
import html as _html

DOCID = "TK-BA-SMR-REQ-01"
VERSION = "v1.0"
DATE = "29 October 2026"

CSS = """
@page { size: A4; margin: 0; }
@page landscape { size: A4 landscape; }
:root { --ink:#1b2333; --accent:#0b3d91; --line:#c9ced8; --muted:#5b6475; --danger:#a40000; --amber:#8a5a00; }
* { box-sizing:border-box; }
body { margin:0; background:#e9ebef; font-family:'Sarabun','IBM Plex Sans',sans-serif; color:var(--ink); font-size:10.5pt; line-height:1.32; }
.page { width:210mm; height:297mm; padding:24mm 20mm 20mm; background:#fff;
        box-sizing:border-box; position:relative; overflow:hidden; box-shadow:0 1px 4px rgba(0,0,0,.15);
        page-break-after:always; }
.page.landscape { width:297mm; height:210mm; page:landscape; }
@media screen { .page { margin:10mm auto; } }
.page-header, .page-footer { position:absolute; left:20mm; right:20mm; font-size:8pt; color:var(--muted);
        display:flex; justify-content:space-between; align-items:center; }
.page-header { top:9mm; border-bottom:1px solid var(--line); padding-bottom:1.5mm; }
.page-footer { bottom:8mm; border-top:1px solid var(--line); padding-top:1.5mm; }
.confidential { color:var(--danger); font-weight:700; letter-spacing:.05em; }
.watermark { position:absolute; top:50%; left:50%; transform:translate(-50%,-50%) rotate(-30deg);
        font-size:90px; font-weight:700; color:#0b3d91; opacity:.035; pointer-events:none; white-space:nowrap; z-index:0; }
.content { position:relative; z-index:1; }
h1 { font-size:16pt; color:var(--accent); margin:0 0 3mm; border-bottom:2px solid var(--accent); padding-bottom:1.5mm; }
h2 { font-size:12pt; color:var(--accent); margin:4mm 0 2mm; }
h3 { font-size:10.5pt; color:var(--ink); margin:3mm 0 1.5mm; }
p { margin:0 0 2mm; }
table { width:100%; border-collapse:collapse; font-size:8.4pt; margin:1.5mm 0 2mm; }
th, td { border:1px solid var(--line); padding:2.2px 4px; vertical-align:top; text-align:left; }
th { background:#eef1f6; font-weight:700; }
code, .id { font-family:'IBM Plex Mono',monospace; font-size:8pt; }
.cover { text-align:left; }
.cover .mark { font-size:26pt; font-weight:700; color:var(--accent); letter-spacing:.02em; }
.cover .rule { height:3px; background:var(--accent); width:60mm; margin:4mm 0 8mm; }
.cover .title { font-size:24pt; font-weight:700; line-height:1.15; margin:6mm 0 3mm; }
.cover .subtitle { font-size:13pt; color:var(--muted); margin-bottom:14mm; }
.cover .meta td { border:none; padding:1.5px 0; font-size:10pt; }
.cover .cls { margin-top:12mm; display:inline-block; border:2px solid var(--danger); color:var(--danger);
        font-weight:700; letter-spacing:.12em; padding:2mm 5mm; font-size:11pt; }
.tag { display:inline-block; font-size:7.5pt; padding:0 4px; border-radius:3px; font-weight:700; }
.must { background:#0b3d91; color:#fff; }
.should { background:#5b6475; color:#fff; }
.could { background:#c9ced8; color:#1b2333; }
.wont { background:#e2c4c4; color:#5a0000; }
.disputed { background:#fbe6c4; }
.ok { background:#d7ead7; }
.oi { background:#fbeaea; }
ul, ol { margin:1mm 0 2mm; padding-left:5mm; }
li { margin:0.6mm 0; }
.toc td { border:none; padding:1.4px 0; font-size:9.5pt; }
.toc .n { width:12mm; color:var(--accent); font-weight:700; }
.small { font-size:8.5pt; color:var(--muted); }
.kv td:first-child { width:34mm; font-weight:700; background:#f4f6fa; }
.story { border:1px solid var(--line); border-left:3px solid var(--accent); padding:2mm 3mm; margin:2mm 0; font-size:9pt; }
.story .hd { font-weight:700; }
.story .gherkin { font-family:'IBM Plex Mono',monospace; font-size:7.8pt; white-space:pre-wrap; background:#f7f8fb; border:1px solid var(--line); padding:1.5mm 2mm; margin-top:1.5mm; line-height:1.25; }
.note { background:#eef1f6; border-left:3px solid var(--accent); padding:2mm 3mm; font-size:9pt; margin:2mm 0; }
.warn { background:#fbeaea; border-left:3px solid var(--danger); padding:2mm 3mm; font-size:9pt; margin:2mm 0; }
.pass { color:#2e6b2e; font-weight:700; }
"""

PAGES = []
_counter = [0]


def page(content, landscape=False):
    _counter[0] += 1
    cls = "page landscape" if landscape else "page"
    return (f'<section class="{cls}">'
            f'<div class="page-header"><span>{DOCID} &middot; {VERSION}</span>'
            f'<span class="confidential">TK COMPANY &ndash; CONFIDENTIAL</span></div>'
            f'<div class="watermark">TK CONFIDENTIAL</div>'
            f'<div class="content">{content}</div>'
            f'<div class="page-footer"><span class="confidential">TK Company &ndash; Confidential &middot; Do not distribute without written consent</span>'
            f'<span>Page {_counter[0]}</span></div>'
            f'</section>')


def T(headers, rows, widths=None, cls=""):
    cg = ""
    if widths:
        cg = "<colgroup>" + "".join(f'<col style="width:{w}">' for w in widths) + "</colgroup>"
    h = "".join(f"<th>{c}</th>" for c in headers)
    body = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<table class="{cls}">{cg}<thead><tr>{h}</tr></thead><tbody>{body}</tbody></table>'


def badge(m):
    cls = {"Must": "must", "Should": "should", "Could": "could", "Won't": "wont"}.get(m, "")
    return f'<span class="tag {cls}">{m}</span>'


# =====================================================================
# PAGE 1 — COVER
# =====================================================================
PAGES.append(page("""
<div class="cover">
  <div class="mark">TK Company</div>
  <div class="rule"></div>
  <div class="title">SiamMart Returns<br>Requirements Package</div>
  <div class="subtitle">Scope, Technical Requirements, Functional Specification &amp; User Stories &mdash; Phase&nbsp;1</div>
  <table class="meta">
    <tr><td>Customer</td><td><b>SiamMart Co., Ltd.</b> (retail chain ~120 สาขา + online shop)</td></tr>
    <tr><td>Project</td><td>SiamMart Returns (SMR)</td></tr>
    <tr><td>Document ID</td><td><span class="id">TK-BA-SMR-REQ-01</span></td></tr>
    <tr><td>Version</td><td>%s</td></tr>
    <tr><td>Date</td><td>%s</td></tr>
    <tr><td>Prepared by</td><td>TK Company &mdash; Business Analysis Team</td></tr>
    <tr><td>Source input</td><td>Kickoff meeting notes, 22 Oct 2026 (room 3B + Teams)</td></tr>
    <tr><td>Classification</td><td>CONFIDENTIAL &mdash; TK Company &amp; SiamMart internal</td></tr>
  </table>
  <div class="cls">CONFIDENTIAL</div>
  <p class="small" style="margin-top:10mm;max-width:150mm;">
  This document translates the SiamMart returns kickoff meeting notes into a precise, testable and
  commercial-aware requirements package. It is Phase&nbsp;1 only; Shopee/Lazada (marketplace) returns are
  deferred to Phase&nbsp;2. Every unverified figure is sized with the higher value and flagged as an
  assumption (<span class="id">AS-</span>); every unresolved stakeholder conflict is recorded as an open
  issue (<span class="id">OI-</span>) with both positions, a decision owner and a due date.</p>
</div>
""" % (VERSION, DATE)))

# =====================================================================
# PAGE 2 — DOCUMENT CONTROL
# =====================================================================
PAGES.append(page("""
<h1>Document Control</h1>
<h2>Version history</h2>
""" + T(["Version", "Date", "Author", "Summary of change"],
        [["0.1", "24 Oct 2026", "TK BA", "First draft from kickoff notes"],
         ["0.9", "27 Oct 2026", "TK BA", "TR/NFR/INT, FS and stories added; OI/AS logged"],
         ["1.0", "29 Oct 2026", "TK BA", "Issued for senior-BA review", ],
        ]) + """
<h2>Reviewers &amp; approvers</h2>
""" + T(["Role", "Name / Organisation", "Responsibility", "Signature", "Date"],
        [["Author", "TK BA &mdash; TK Company", "Writes the package", "", ""],
         ["Technical reviewer", "TK SA &mdash; TK Company", "Consistency of TR/INT with architecture", "", ""],
         ["Independent verifier", "TK Senior BA &mdash; TK Company", "Verifies against BA standards", "", ""],
         ["Customer approver", "K.Somchai &mdash; Head of CS, SiamMart", "Business sign-off", "", ""],
         ["Customer approver", "K.Pim &mdash; Finance, SiamMart", "Financial / audit sign-off", "", ""],
         ["Customer IT", "K.Arthit &mdash; IT, SiamMart", "Integration &amp; security sign-off", "", ""],
        ]) + """
<h2>Distribution</h2>
<p class="small">Controlled copy. Section&nbsp;14 (Commercial Notes) is <b>TK-internal only</b> and must be
removed from any copy released to the customer. Do not distribute without written consent of TK Company.</p>
<h2>Document conventions used in this package</h2>
<ul class="small">
  <li><span class="id">BR-</span> business requirement (the "why") &middot; <span class="id">TR-&lt;MOD&gt;-</span> technical requirement &middot; <span class="id">NFR-&lt;CAT&gt;-</span> non-functional &middot; <span class="id">INT-&lt;SYS&gt;-</span> integration.</li>
  <li><span class="id">BRL-</span> business rule &middot; <span class="id">FS-&lt;MOD&gt;-</span> functional spec &middot; <span class="id">EP-</span>/<span class="id">US-</span> epic / user story &middot; <span class="id">AS-</span> assumption &middot; <span class="id">OI-</span> open issue.</li>
  <li>Priority uses MoSCoW (Must / Should / Could / Won't this time). "The system shall&hellip;" statements are individually testable.</li>
  <li>Unverified numbers are sized with the <b>higher</b> of conflicting figures and carried as an <span class="id">AS-</span> with an owner to confirm.</li>
</ul>
"""))

# =====================================================================
# PAGE 3 — TOC
# =====================================================================
PAGES.append(page("""
<h1>Table of Contents</h1>
<table class="toc">
<tr><td class="n">1</td><td>Introduction</td></tr>
<tr><td class="n">2</td><td>Business Context &amp; Objectives</td></tr>
<tr><td class="n">3</td><td>Scope (In / Out / Phasing / MoSCoW)</td></tr>
<tr><td class="n">4</td><td>Stakeholders &amp; RACI</td></tr>
<tr><td class="n">5</td><td>Business Rules (BRL)</td></tr>
<tr><td class="n">6</td><td>Technical Requirements (TR)</td></tr>
<tr><td class="n">7</td><td>Non-Functional Requirements (NFR) &amp; PDPA</td></tr>
<tr><td class="n">8</td><td>Integration Requirements (INT)</td></tr>
<tr><td class="n">9</td><td>Functional Specification (FS)</td></tr>
<tr><td class="n">10</td><td>User Stories &amp; Acceptance Criteria</td></tr>
<tr><td class="n">11</td><td>Traceability Matrix</td></tr>
<tr><td class="n">12</td><td>Assumptions, Constraints &amp; Dependencies</td></tr>
<tr><td class="n">13</td><td>Open Issues &amp; Conflicts</td></tr>
<tr><td class="n">14</td><td>Commercial Notes (internal only)</td></tr>
<tr><td class="n">15</td><td>Sign-off</td></tr>
<tr><td class="n">A</td><td>Appendix: Glossary (incl. Thai terms)</td></tr>
</table>
<h2>Sub-sections</h2>
<table class="toc">
<tr><td class="n">2.1</td><td>As-Is process (today)</td></tr>
<tr><td class="n">2.2</td><td>Statement log (every input statement classified)</td></tr>
<tr><td class="n">2.3</td><td>Business problem &amp; SMART objectives</td></tr>
<tr><td class="n">7.2</td><td>PDPA personal data inventory</td></tr>
<tr><td class="n">9.x</td><td>FS-RET / FS-APR / FS-RFD / FS-DSP / FS-NTF / FS-RPT / FS-FRD / FS-ADM</td></tr>
<tr><td class="n">10.x</td><td>EP-01 &hellip; EP-10 user-story epics</td></tr>
</table>
<p class="small" style="margin-top:6mm;">Tip: this package is designed to print to A4. Each numbered block
begins on its own page; long tables repeat their header and are split so nothing is clipped.</p>
"""))

# =====================================================================
# PAGE 4 — 1 INTRODUCTION
# =====================================================================
PAGES.append(page("""
<h1>1&nbsp;&nbsp;Introduction</h1>
<h2>1.1 Purpose</h2>
<p>SiamMart today runs returns and refunds on a fragile manual chain: paper/Excel at the branch, a LINE
group to HQ, and manual refunds in SAP every Friday. Refund lead time averages 14&nbsp;days (peer
benchmark 3&nbsp;days) and slow refunds are the company's #1 social-media complaint. This document
specifies a single, auditable returns system for <b>Phase&nbsp;1</b> that consolidates every return
request, applies policy and approval rules, drives refunds into SAP and tracks returned goods &mdash;
built as production-ready requirements that developers, testers and SiamMart can sign off on.</p>
<h2>1.2 Audience &amp; use</h2>
<ul>
  <li><b>Developer / tester team (TK)</b> &mdash; build and test directly from TR / NFR / INT / FS / US and their acceptance criteria.</li>
  <li><b>Solution architect (TK)</b> &mdash; reuses the <span class="id">TR-</span>/<span class="id">NFR-</span>/<span class="id">INT-</span> IDs verbatim in the architecture pack.</li>
  <li><b>SiamMart approvers</b> (K.Somchai, K.Pim, K.Arthit) &mdash; review, resolve <span class="id">OI-</span> items and sign off.</li>
</ul>
<h2>1.3 Scope of this document</h2>
<p>This is the <b>requirements package (Output 2)</b>. The matching solution architecture &amp; workflow
pack is <span class="id">TK-SA-SMR-ARC-01</span>. Everything here traces to the kickoff notes
(<span class="id">input.md</span>); nothing has been invented. Where the notes are silent or contradictory,
a requirement is written to the safest interpretation and the gap is logged as an <span class="id">AS-</span>
or <span class="id">OI-</span>.</p>
<h2>1.4 Document status</h2>
<div class="note">
Status: <b>Draft v1.0 &mdash; issued for senior-BA verification and customer review.</b>
Open issues (<span class="id">OI-01</span>&hellip;<span class="id">OI-08</span>) must be resolved before
functional sign-off. Assumptions (<span class="id">AS-01</span>&hellip;<span class="id">AS-11</span>) must
be confirmed before build freeze. No requirement marked Must is considered final until its blocking
<span class="id">OI-</span> is closed.
</div>
"""))

# =====================================================================
# PAGE 5 — 2.1 AS-IS
# =====================================================================
PAGES.append(page("""
<h1>2&nbsp;&nbsp;Business Context &amp; Objectives</h1>
<h2>2.1 As-Is process (today)</h2>
<p>SiamMart is a retail chain of ~120 สาขา plus an online shop (own website + Shopee / Lazada). Returns
arrive through three disconnected paths, all of which converge on manual, person-dependent handling:</p>
""" + T(["Channel", "Today (as observed in kickoff)", "Pain"],
        [["In-store return",
          "Customer returns at the counter &rarr; staff writes it on paper (some branches use Excel) &rarr; photo to the LINE group &ldquo;Return-HQ&rdquo; &rarr; HQ CS reviews and approves inside LINE.",
          "No system of record; approvals lost in chat; re-keying errors."],
         ["Online return",
          "Customer emails returns@siammart.co.th or opens chat &rarr; CS copies details into the shared-drive spreadsheet &ldquo;RETURN_MASTER_v7_final_FINAL.xlsx&rdquo;.",
          "One fragile spreadsheet; version chaos; no audit trail."],
         ["Refund (finance)",
          "HQ-approved returns are refunded manually in SAP by Finance, batched every Friday.",
          "Backlog; refunds take 14 days on average (10&ndash;21 day range), peers do 3 days."],
         ["Returned goods",
          "Returned stock piles behind the store; no rule on restock vs. return-to-DC/supplier vs. write-off.",
          "Inventory loss, stock shrinkage, unknown value."],
        ], widths=["24mm", "auto", "auto"]) + """
<p class="small">Consequence: slow refunds are the <b>#1 complaint</b> on social media last quarter
(~2,300 complaints &mdash; to be confirmed, <span class="id">AS-04</span>). There is also no visibility of
fraud (repeat returners) and no management reporting on return volume, reason or branch.</p>
<h2>The real business problem (why)</h2>
<div class="note">The customer's literal ask is &ldquo;one system where everything is in one place.&rdquo;
Drilled down, the measurable outcome is: <b>cut refund lead time from ~14 days to &le;3 days, stop the
manual spreadsheets/LINE approvals, and give Finance and executives an auditable, reconciled view &mdash;
without increasing fraud or losing returned stock.</b></div>
"""))

# =====================================================================
# PAGES 6-8 — 2.2 STATEMENT LOG
# =====================================================================
stmt_rows = [
 ["1", "SiamMart = retail chain ~120 สาขา + online shop (website + Shopee/Lazada)", "Context", "L11", "Confirmed background; basis for phased marketplace scope."],
 ["2", "ตอนนี้ลูกค้าคืนของ / ขอ refund วุ่นวายมาก (returns/refunds are chaotic today)", "Pain point", "L12", "Root 'why' for the project."],
 ["3", "In-store: paper / Excel → photo to LINE 'Return-HQ' → HQ CS approves in LINE", "Pain point", "L13", "Manual, un-auditable intake; drives BR-01 / TR-RET."],
 ["4", "Finance does manual refund in SAP every Friday", "Pain point", "L13", "Batching causes delay; drives BR-03 / TR-RFD."],
 ["5", "Online return via returns@ email / chat → copied into central shared Excel", "Pain point", "L14", "Single point of failure; drives unified intake."],
 ["6", "Refund averages 14 days (K.Pim: 10–21 days); competitor 3 days", "Pain point", "L15", "Baseline metric → SMART O1; range → AS-03."],
 ["7", "Slow-refund complaint = #1 on social last quarter (~2,300 complaints, unconfirmed)", "Pain point", "L16", "Baseline metric → SMART O2; count → AS-04."],
 ["8", "Returned goods pile behind store; no restock/DC/discard rule", "Pain point", "L17", "Drives BR-04 / FS-DSP."],
 ["9", "Want a return system where everything is in one place", "Goal", "L21", "Vision; translated into SMART objectives."],
 ["10", "Customer can request return via web/app (app doesn't exist; 'LINE OA ok')", "Requirement", "L22", "TR-RET-001/002; channel choice → OI-04."],
 ["11", "Store staff use tablet to scan receipt barcode, system pulls order", "Requirement", "L23", "TR-RET-003 / INT-POS-01."],
 ["12", "If price < 500 THB auto-approve (K.Somchai) BUT K.Pim: must pass finance every item per audit", "Conflict", "L24", "OI-01 (mandatory, unresolved)."],
 ["13", "If over 5,000 THB, manager must approve", "Requirement", "L25", "BRL-003 / TR-APR-002."],
 ["14", "Refund to credit card / PromptPay / store credit (store credit +5% bonus = unconfirmed marketing idea)", "Requirement", "L26", "TR-RFD-002/003; 5% bonus → AS-06."],
 ["15", "Must connect SAP (ECC 6.0, has RFC but no direct access allowed)", "Requirement", "L27", "INT-SAP-01 via TK-Connect; constraint noted."],
 ["16", "Must connect POS (vendor 'RetailPro'? or in-house? unsure)", "Requirement", "L28", "INT-POS-01; vendor identity → OI-05."],
 ["17", "Connect Shopee/Lazada returns — 'phase 2 maybe'", "Requirement", "L29", "OUT OF SCOPE Phase 2 (marketplace)."],
 ["18", "Executive dashboard: return count, reason, branch, fraud", "Requirement", "L30", "TR-RPT-001 / FS-RPT-01."],
 ["19", "Notify customer at every step (SMS? LINE? email?) 'like Kerry tracking'", "Requirement", "L31", "TR-NTF-001/002; channels → OI-07."],
 ["20", "Returned goods flow: restock / return to supplier / write-off", "Requirement", "L32", "BRL-010 / TR-DSP-001."],
 ["21", "Fraud: some customers return every week; system should flag them", "Requirement", "L33", "TR-FRD-001; rule threshold → AS-10."],
 ["22", "'Must be very easy to use, some staff are older'", "Requirement (quality)", "L34", "Translated to NFR-USAB-001 (≤5 taps, ≥16sp, ≤30-min training)."],
 ["23", "Must support peak after 11.11 / 12.12 (returns spike 4–5×)", "Requirement (quality)", "L35", "NFR-SCAL-001; multiplier → AS-09."],
 ["24", "Product photos must be kept (how many years? audit says 7? not sure)", "Requirement", "L36", "NFR-DATA-001; retention → AS-05."],
 ["25", "Customer data → PDPA!! (K.Arthit concern)", "Constraint", "L37", "NFR-PRIV-001 + §7.2 inventory."],
 ["26", "Language TH/EN", "Requirement", "L38", "TR-RET-009 / NFR-L10N-001."],
 ["27", "Budget not over 8M THB phase 1 (K.Somchai); Finance not fully agreeing", "Constraint + Conflict", "L42", "Budget → AS-12; disagreement → OI-02."],
 ["28", "Go-live before 11.11 next year (Nov 2027), 'must make it'", "Constraint", "L43", "Fixed-date risk → Commercial Notes."],
 ["29", "Pilot 10 Bangkok branches first", "Requirement", "L44", "Phasing: Pilot then Phase 1."],
 ["30", "SiamMart IT has only 4 people → wants TK to host + support (MA?)", "Constraint + Requirement", "L45", "Commercial Notes (MA/upsell)."],
 ["31", "Doesn't want to buy expensive licences", "Constraint", "L46", "Design constraint; Commercial Notes."],
 ["32", "Return policy: 7 / 14 / 30 days by category? ask K.Nok for policy doc", "Open question", "L50", "BRL-004; windows → AS-02 (needs policy doc)."],
 ["33", "Who owns this process — CS or Store Ops?", "Open question", "L51", "OI-03."],
 ["34", "Partial return (some items in an order) — probably yes", "Open question", "L52", "TR-RET-005; confirm → AS-07."],
 ["35", "Exchange (เปลี่ยนของ) in scope?", "Open question", "L53", "OI-06 (assume out of scope Phase 1)."],
 ["36", "Returns/month: K.Nok ~18k, K.Somchai ~25k", "Assumption", "L54", "Sized at 25,000 → AS-01."],
 ["37", "Migrate old Excel? '1 year back is enough'", "Requirement", "L55", "TR-MIG-001 / AS-08."],
 ["38", "SSO with SiamMart AD?", "Open question", "L56", "OI-08 / INT-AD-01."],
 ["39", "Liked competitor 'return QR code' idea (customer QR to present at store)", "Nice-to-have", "L60", "Could — Future opportunity (not Phase-1 Must)."],
 ["40", "K.Pim wants daily refund report exported to Excel", "Requirement", "L61", "TR-RPT-002 / FS-RPT-01."],
 ["41", "'AI check product-condition photo' — nice to have, ignore for now", "Nice-to-have", "L62", "OUT OF SCOPE — Future opportunity."],
 ["42", "Next meeting: walk-through store process at Bangna, date TBC", "Noise / meta", "L63", "Dependency: process walkthrough."],
 ["43", "Meeting date 22 Oct 2026 (??), attendees, notes by BA", "Noise / meta", "L3–L5", "Reference only."],
]

# split into 3 pages ~15 rows each
def _chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i+n]

for idx, part in enumerate(_chunks(stmt_rows, 15)):
    hdr = '<h1>2&nbsp;&nbsp;Business Context &amp; Objectives</h1><h2>2.2 Statement log &mdash; every input statement classified (' + str(idx+1) + ' of 3)</h2>' if idx == 0 else '<h2>2.2 Statement log (cont. ' + str(idx+1) + ' of 3)</h2>'
    PAGES.append(page(hdr + T(["#", "Input statement (as said)", "Class", "Line", "BA interpretation / mapping"],
        part, widths=["7mm", "auto", "20mm", "12mm", "auto"])))

# =====================================================================
# PAGE 9 — 2.3 SMART OBJECTIVES
# =====================================================================
PAGES.append(page("""
<h1>2&nbsp;&nbsp;Business Context &amp; Objectives (cont.)</h2>
<h2>2.3 SMART business objectives</h2>
""" + T(["ID", "Objective (SMART)", "Baseline (source)", "Target", "Measured by"],
        [["O1", "Reduce refund lead time for approved returns from request to money-back.",
          "Avg 14 days, range 10–21 days (K.Pim, L15)",
          "&le;3 calendar days for &ge;90% of approved refunds, within 3 months of go-live",
          "Refund timestamp minus approval timestamp, from system"],
         ["O2", "Reduce slow-refund social complaints.",
          "~2,300 complaints/quarter, #1 topic (L16, AS-04)",
          "&le;690 complaints/quarter (−70%) within 6 months of go-live",
          "CS complaint log, quarterly"],
         ["O3", "Consolidate 100% of return requests into one system of record.",
          "Two fragmented manual channels (LINE + spreadsheet) (L13–14)",
          "0 return approvals by LINE group / spreadsheet at 3 months post go-live",
          "% of returns created in system vs sampled manual"],
         ["O4", "Automate refund execution to SAP and reconcile daily.",
          "Manual Friday batch in SAP (L13)",
          "100% of refunds raised via TK-Connect&rarr;SAP, 100% reconciled daily, 0 duplicate postings",
          "Daily reconciliation report (§7 TR-RFD-005)"],
         ["O5", "Give management a factual returns view.",
          "None today (L30)",
          "Executive dashboard live at go-live, refreshed daily: volume, reason, branch, fraud flag",
          "Dashboard availability check"],
        ], widths=["8mm", "auto", "auto", "auto", "auto"]) + """
<h2>2.4 Business value (why it matters)</h2>
<ul class="small">
  <li><b>Customer retention</b>: moving from 14&rarr;3 days removes the #1 complaint driver and protects repeat revenue.</li>
  <li><b>Cost/loss control</b>: a disposition rule for returned goods stops inventory shrinkage and unclear write-offs.</li>
  <li><b>Audit &amp; finance integrity</b>: one system of record replaces a spreadsheet; refunds become reconciled and duplicate-proof.</li>
  <li><b>Fraud</b>: repeat returners become visible, protecting margin.</li>
</ul>
<p class="small">All targets are drafted from the customer's own numbers. Where the number is unverified it
is explicitly flagged (<span class="id">AS-01</span>, <span class="id">AS-03</span>,
<span class="id">AS-04</span>) and the objective will be re-baselined once confirmed.</p>
"""))

# =====================================================================
# PAGE 10 — 3 SCOPE IN
# =====================================================================
PAGES.append(page("""
<h1>3&nbsp;&nbsp;Scope</h1>
<h2>3.1 In scope (Phase 1)</h2>
<p class="small">Capabilities are grouped by module. Priority is MoSCoW; see §3.4 and each TR for detail.</p>
""" + T(["#", "Capability", "Module", "Priority", "Phase"],
        [["1", "Customer self-service return request (responsive web portal + LINE OA)", "RET", badge("Must"), "1"],
         ["2", "Store tablet return intake with receipt-barcode scan and manual fallback", "RET", badge("Must"), "1"],
         ["3", "Capture return reason, item condition and photo evidence", "RET", badge("Must"), "1"],
         ["4", "Partial return (subset of order lines)", "RET", badge("Must"), "1"],
         ["5", "Policy eligibility check by category and return window", "RET/APR", badge("Must"), "1"],
         ["6", "Approval workflow: auto / manager / finance (subject to OI-01)", "APR", badge("Must"), "1"],
         ["7", "Refund calculation (net of discounts, partial lines)", "RFD", badge("Must"), "1"],
         ["8", "Refund disbursement to original payment method + store credit", "RFD", badge("Must"), "1"],
         ["9", "Idempotent refund execution and daily reconciliation vs SAP", "RFD", badge("Must"), "1"],
         ["10", "Returned-goods disposition workflow (restock / supplier / write-off)", "DSP", badge("Must"), "1"],
         ["11", "Customer notifications at every status change + tracking page", "NTF", badge("Must"), "1"],
         ["12", "Executive dashboard (volume, reason, branch, fraud)", "RPT", badge("Must"), "1"],
         ["13", "Daily refund report export to Excel", "RPT", badge("Should"), "1"],
         ["14", "Fraud flagging for repeat returners", "FRD", badge("Should"), "1"],
         ["15", "Policy / threshold admin configuration", "ADM", badge("Must"), "1"],
         ["16", "Role-based access control (staff / manager / finance / CS / admin)", "ADM", badge("Must"), "1"],
         ["17", "SSO with SiamMart AD (subject to OI-08)", "ADM/INT", badge("Should"), "1"],
         ["18", "Integration: SAP ECC 6.0 and POS via TK-Connect only", "INT", badge("Must"), "1"],
         ["19", "Migrate 1 year of historical return records", "MIG", badge("Must"), "1"],
         ["20", "Bilingual UI (TH / EN)", "ALL", badge("Must"), "1"],
         ["21", "Pilot rollout to 10 Bangkok branches, then all stores", "OPS", badge("Must"), "Pilot"],
        ], widths=["7mm", "auto", "14mm", "16mm", "14mm"]) + """
<div class="note"><b>Architecture rule (binding on all in-scope work):</b> SAP, POS and marketplace traffic
may only traverse <b>TK-Connect</b>. No component may call SAP RFC, POS or marketplace APIs directly.
Money flows are idempotent, reconciled and audited. See §8.</div>
"""))

# =====================================================================
# PAGE 11 — 3.2 OUT OF SCOPE + 3.3 PHASING
# =====================================================================
PAGES.append(page("""
<h1>3&nbsp;&nbsp;Scope (cont.)</h1>
<h2>3.2 Out of scope (Phase 1) — each with a reason</h2>
""" + T(["#", "Item", "Reason / destination"],
        [["O-1", "Shopee / Lazada marketplace returns", "Customer said 'phase 2 maybe' (L29). Deferred to Phase 2 (INT-MKT-01)."],
         ["O-2", "Exchange (เปลี่ยนของ) / product swap", "Undecided (L53) &rarr; OI-06. Assumed out of Phase 1 to protect scope; revisit after OI-06."],
         ["O-3", "AI product-condition image inspection", "Explicitly 'nice to have, ignore for now' (L62). Future opportunity, not committed."],
         ["O-4", "Native mobile app build", "App does not exist (L22). Phase-1 channel is web + LINE OA; native app is a follow-on."],
         ["O-5", "Procurement of tablets / barcode scanners / branch hardware", "Customer responsibility (assumption AS-08 device availability); not a TK deliverable."],
         ["O-6", "Warranty / repair management", "Not requested in kickoff."],
         ["O-7", "Loyalty / marketing platform and store-credit bonus engine config", "Only the refund credit mechanism is in scope; campaigns are not. 5% bonus unconfirmed (AS-06)."],
         ["O-8", "Fraud prosecution / case management workflow", "Only flagging is requested (L33); downstream investigation is manual/out of scope."],
         ["O-9", "Full ERP replacement or non-returns modules", "Not requested."],
        ], widths=["10mm", "auto", "auto"]) + """
<h2>3.3 Phasing</h2>
""" + T(["Phase", "Content", "Indicative timeline", "Gate"],
        [["Pilot", "10 Bangkok branches (incl. Bangna walkthrough branch); core intake + approval + refund + notifications.",
          "Q2–Q3 2027", "Pilot acceptance &amp; process sign-off"],
         ["Phase 1", "All ~120 branches + online channels; disposition, dashboard, fraud, admin, full migration.",
          "By Nov 2027 (before 11.11)", "Go-live before 11.11 peak"],
         ["Phase 2", "Shopee / Lazada marketplace returns, exchange (if approved), AI image inspection.",
          "Post-2027 (TBC)", "Separate scope &amp; budget"],
        ], widths=["16mm", "auto", "28mm", "auto"]) + """
<h2>3.4 MoSCoW summary</h2>
<p class="small"><b>Must</b> = 24 TRs (see §6). <b>Should</b> = daily Excel report, fraud flagging, AD SSO, disposition HQ tracking, approval SLA.
<b>Could</b> = QR-code drop-off (L60), operational ageing report. <b>Won't this time</b> = marketplace returns, exchange, AI inspection, native app.</p>
"""))

# =====================================================================
# PAGE 12 — 4 STAKEHOLDERS RACI
# =====================================================================
PAGES.append(page("""
<h1>4&nbsp;&nbsp;Stakeholders &amp; RACI</h1>
<h2>4.1 Stakeholder register</h2>
""" + T(["Name", "Role", "Organisation", "Interest / influence"],
        [["K.Somchai", "Head of Customer Service (project sponsor)", "SiamMart", "Wants fast, unified returns; wants auto-approval <500 THB."],
         ["K.Nok", "Store Operations", "SiamMart", "Front-line process, return policy owner-contributor."],
         ["K.Pim", "Finance", "SiamMart", "Audit &amp; control; insists every refund pass Finance. Budget gatekeeper."],
         ["K.Arthit", "IT", "SiamMart", "SAP/POS integration, PDPA, SSO; only 4 IT staff."],
         ["TK BA", "Business Analyst (author)", "TK Company", "Requirements author."],
         ["TK SA", "Solution Architect", "TK Company", "Architecture pack TK-SA-SMR-ARC-01."],
         ["TK Senior BA / QA", "Independent verifier", "TK Company", "Verification &amp; document gate."],
        ], widths=["20mm", "auto", "24mm", "auto"]) + """
<h2>4.2 RACI matrix</h2>
<p class="small">R = Responsible, A = Accountable, C = Consulted, I = Informed.</p>
<table>
<thead><tr><th>Activity</th><th>K.Somchai (CS)</th><th>K.Nok (Store Ops)</th><th>K.Pim (Finance)</th><th>K.Arthit (IT)</th><th>TK BA</th><th>TK SA</th></tr></thead>
<tbody>
<tr><td>Approve requirements (this document)</td><td>A</td><td>C</td><td>C</td><td>C</td><td>R</td><td>C</td></tr>
<tr><td>Return policy rules (windows/categories)</td><td>C</td><td>A/R</td><td>C</td><td>I</td><td>C</td><td>I</td></tr>
<tr><td>Approval &amp; refund controls (OI-01)</td><td>A</td><td>C</td><td>A/R</td><td>C</td><td>R</td><td>C</td></tr>
<tr><td>SAP / POS integration</td><td>I</td><td>I</td><td>C</td><td>A/R</td><td>C</td><td>R</td></tr>
<tr><td>PDPA &amp; security sign-off</td><td>I</td><td>I</td><td>C</td><td>A/R</td><td>C</td><td>C</td></tr>
<tr><td>Budget approval (8M THB)</td><td>A</td><td>I</td><td>A/R</td><td>C</td><td>I</td><td>C</td></tr>
<tr><td>Pilot &amp; store rollout readiness</td><td>C</td><td>A/R</td><td>I</td><td>C</td><td>C</td><td>I</td></tr>
<tr><td>UAT &amp; acceptance</td><td>A</td><td>R</td><td>C</td><td>C</td><td>C</td><td>C</td></tr>
<tr><td>Document verification &amp; gate</td><td>I</td><td>I</td><td>I</td><td>I</td><td>R</td><td>C</td></tr>
</tbody></table>
<div class="warn"><b>Ownership unresolved.</b> The kickoff left open &ldquo;who owns this process — CS or
Store Ops?&rdquo; (L51). Until <span class="id">OI-03</span> is closed, both K.Somchai (CS) and K.Nok
(Store Ops) are consulted for process decisions; K.Somchai is taken as interim accountable for sign-off.</div>
"""))

# =====================================================================
# PAGES 13-14 — 5 BUSINESS RULES
# =====================================================================
brl_rows = [
 ["BRL-001", "Auto-approval threshold", "Refund amount &lt; 500 THB (per item/claim)", "Approve automatically without finance step", "K.Somchai (L24)", '<span class="warn" style="padding:0 3px">DISPUTED &mdash; OI-01</span>'],
 ["BRL-002", "Finance approval of refunds", "Every refund request", "Route to Finance approval queue before refund", "K.Pim (L24)", '<span class="warn" style="padding:0 3px">DISPUTED &mdash; OI-01</span>'],
 ["BRL-003", "Manager approval (high value)", "Refund amount &gt; 5,000 THB", "Route to store manager approval before finance", "K.Somchai (L25)", '<span class="pass" style="padding:0 3px">Confirmed</span>'],
 ["BRL-004", "Return window by category", "Category-based: electronics 7 days; others 30 days; default 14 days", "Reject / disable items outside their window", "L50 (policy doc @K.Nok)", '<span class="warn" style="padding:0 3px">UNCONFIRMED &mdash; AS-02</span>'],
 ["BRL-005", "Refund method", "Original payment method (card / PromptPay) or store credit", "Refund to source (default) or issue store credit if chosen", "L26", '<span class="pass" style="padding:0 3px">Confirmed</span>'],
 ["BRL-006", "Store-credit bonus", "If store credit chosen, add +5% bonus", "Increase issued credit by 5% (configurable, can be 0)", "L26 (marketing idea)", '<span class="warn" style="padding:0 3px">UNCONFIRMED &mdash; AS-06</span>'],
 ["BRL-007", "Partial return", "A subset of an order&rsquo;s lines may be returned", "Compute refund on selected lines only", "L52", '<span class="warn" style="padding:0 3px">ASSUMED YES &mdash; AS-07</span>'],
 ["BRL-008", "Refund lead-time target", "Approved refund", "Complete refund within 3 calendar days", "Derived from O1 / L15", '<span class="pass" style="padding:0 3px">Business target</span>'],
 ["BRL-009", "Evidence / audit retention", "Product photos + transaction records", "Retain 7 years (accounting/audit)", "L36 (audit, unconfirmed)", '<span class="warn" style="padding:0 3px">UNCONFIRMED &mdash; AS-05</span>'],
 ["BRL-010", "Disposition decision", "Returned item condition", "Restock → return-to-supplier → write-off (decision tree)", "L32", '<span class="pass" style="padding:0 3px">Confirmed (rules to detail)</span>'],
 ["BRL-011", "Fraud flag", "Customer with &ge;3 returns in rolling 30 days", "Flag customer/return for CS review (does not auto-block)", "L33 (proposed)", '<span class="warn" style="padding:0 3px">PROPOSED &mdash; AS-10</span>'],
 ["BRL-012", "Eligibility validation", "Item within policy window AND resalable per category rules", "Only eligible lines selectable; ineligible disabled with reason", "Derived (L50/L23)", '<span class="pass" style="padding:0 3px">Business rule</span>'],
]
for idx, part in enumerate(_chunks(brl_rows, 6)):
    hdr = '<h1>5&nbsp;&nbsp;Business Rules (BRL)</h1><p class="small">Decision logic is pulled out of prose so it is testable and configurable. Status flags every rule whose number/decision is not yet final.</p>' if idx==0 else '<h2>5.1 Business rules (cont.)</h2>'
    PAGES.append(page(hdr + T(["ID", "Rule", "Condition", "Action", "Source", "Status"],
        part, widths=["15mm","26mm","auto","auto","24mm","26mm"])))

# PAGE 15 — BRL note + derived rules
PAGES.append(page("""
<h1>5&nbsp;&nbsp;Business Rules (cont.)</h1>
<h2>5.2 Rule-governance notes</h2>
<div class="warn"><b>BRL-001 vs BRL-002 are mutually exclusive and unresolved.</b> They encode the
K.Somchai / K.Pim conflict. The system must support <i>both</i> as configuration so that whichever way
<span class="id">OI-01</span> is decided, it is a configuration change, not a re-build. Phase-1 default
until decided: <b>BRL-002 (all refunds to Finance)</b> &mdash; the more conservative, audit-safe option.</div>
<h3>Why default to the conservative option</h3>
<p class="small">Choosing auto-approval before Finance agrees risks an audit finding and re-work; choosing
Finance-approval only costs some speed but is reversible via configuration. OI-01 must still be formally
closed with the customer before functional sign-off.</p>
<h2>5.3 Configurable parameters (exposed in FS-ADM-01)</h2>
""" + T(["Parameter", "Default", "Source rule", "Editable by"],
        [["Auto-approval threshold (THB)", "0 (disabled pending OI-01)", "BRL-001", "Admin"],
         ["Manager-approval threshold (THB)", "5,000", "BRL-003", "Admin"],
         ["Return window — electronics (days)", "7", "BRL-004 / AS-02", "Admin"],
         ["Return window — other (days)", "30", "BRL-004 / AS-02", "Admin"],
         ["Return window — default (days)", "14", "BRL-004 / AS-02", "Admin"],
         ["Store-credit bonus (%)", "5 (can be set 0)", "BRL-006 / AS-06", "Admin"],
         ["Fraud threshold (returns / window)", "3 / 30 days", "BRL-011 / AS-10", "Admin"],
         ["Evidence retention (years)", "7", "BRL-009 / AS-05", "Admin"],
         ["Refund SLA target (days)", "3", "BRL-008", "Admin"],
        ], widths=["auto","auto","auto","20mm"]) + """
<p class="small">All rules must be evaluated server-side (never trusted to the client) and every evaluation
must be written to the audit log with the inputs used (see NFR-AUDIT-001).</p>
"""))

# =====================================================================
# PAGES 15-17 — 6 TECHNICAL REQUIREMENTS
# =====================================================================
tr_rows = [
 ["TR-RET-001", "The system shall let a customer raise a return request through a responsive web portal for any order in the last 12 months, in &le;5 steps.", "Must", "L22", "Given a logged-in customer, a complete return request is submitted and a case ID is returned."],
 ["TR-RET-002", "The system shall let a customer raise a return request through the LINE OA channel, landing in the same unified case queue as web.", "Must", "L22 / OI-04", "A LINE-initiated request appears in the CS queue with the same fields as web."],
 ["TR-RET-003", "The system shall retrieve the original sales order from POS within 2 seconds (p95) when a store user scans a receipt barcode (Code128/QR).", "Must", "L23", "Scan of valid barcode shows order header+lines in &le;2s p95."],
 ["TR-RET-004", "The system shall capture return reason (coded list), item condition and 1–5 photo attachments per claim.", "Must", "L14/L23", "A claim cannot be saved without reason; photos stored against the claim."],
 ["TR-RET-005", "The system shall support partial returns by letting the user select a subset of order lines and quantities.", "Must", "L52 / AS-07", "Selecting 2 of 4 lines refunds only those 2 lines."],
 ["TR-RET-006", "The system shall validate each item against its category return window and mark ineligible items as disabled with the reason shown.", "Must", "L50 / BRL-004", "An electronics item 9 days after sale is disabled with reason 'outside 7-day window'."],
 ["TR-RET-007", "The system shall ingest online return requests received at returns@siammart.co.th into the unified case queue (no manual re-keying).", "Must", "L14", "A test email creates a case with parsed order/contact fields."],
 ["TR-RET-008", "The system shall offer manual order search (order no. / phone / receipt no.) when a barcode match is not found.", "Must", "L23 (exception)", "Unknown barcode shows 'not found' and a working manual search."],
 ["TR-RET-009", "The system shall provide a TH/EN language toggle on every user-facing screen, persisting the user's choice.", "Must", "L38", "Toggling TH/EN switches all labels; choice persists across sessions."],
 ["TR-APR-001", "The system shall auto-approve refunds below a configurable threshold (default 500 THB) when that rule is enabled (subject to OI-01).", "Must", "L24 / BRL-001", "With rule enabled, a 400 THB refund is approved without finance and logged."],
 ["TR-APR-002", "The system shall route any refund above 5,000 THB to store-manager approval before finance.", "Must", "L25 / BRL-003", "A 5,500 THB refund cannot reach finance until manager approves."],
 ["TR-APR-003", "The system shall route refunds requiring finance to a Finance approval queue with full claim detail and approve/reject actions.", "Must", "L24 / BRL-002 / OI-01", "A configured finance-required refund appears in Finance queue and blocks refund until action."],
 ["TR-APR-004", "The system shall track an approval SLA timer per queue and escalate to the next approver after the SLA is exceeded.", "Should", "L13 (delay)", "An unattended approval past SLA is escalated and logged."],
 ["TR-RFD-001", "The system shall compute the refund amount net of discounts, promotions and non-returned lines, per the original order.", "Must", "L26", "Refund of a discounted item equals net paid amount, not list price."],
 ["TR-RFD-002", "The system shall disburse refunds to the original payment method via TK-Connect&rarr;SAP, recording the SAP document number.", "Must", "L26/L27", "Approved card refund posts to SAP and the document no. is stored on the case."],
 ["TR-RFD-003", "The system shall issue store credit (with configurable bonus, default 5%) as an alternative refund method when selected.", "Must", "L26 / AS-06", "Choosing store credit issues a credit equal to net refund + configured bonus."],
 ["TR-RFD-004", "The system shall make refund execution idempotent so a retry or double-click never creates a duplicate refund.", "Must", "L13 (finance) / std", "Replaying the same refund request yields exactly one SAP posting."],
 ["TR-RFD-005", "The system shall produce a daily automated reconciliation comparing system refunds to SAP postings and flag any mismatch.", "Must", "L13 (finance)", "A seeded mismatch appears in the reconciliation report next day."],
 ["TR-DSP-001", "The system shall record a disposition decision (restock / return-to-supplier / write-off) for each returned item.", "Must", "L32 / BRL-010", "A received item cannot close without a disposition value."],
 ["TR-DSP-002", "The system shall let HQ Operations track disposition status by branch.", "Should", "L17/L32", "HQ sees counts by disposition and branch."],
 ["TR-NTF-001", "The system shall send a notification on every status change via a configurable channel (SMS / LINE / email) chosen per event.", "Must", "L31 / OI-07", "Status change triggers the configured channel within 60s."],
 ["TR-NTF-002", "The system shall provide a customer tracking page showing the return status timeline ('like parcel tracking').", "Must", "L31", "Tracking link shows current step and history."],
 ["TR-RPT-001", "The system shall provide an executive dashboard with return volume, reason mix, branch ranking and fraud-flag count, refreshed daily.", "Must", "L30", "Dashboard values equal source data for a sampled day."],
 ["TR-RPT-002", "The system shall export a daily refund report to Excel on demand and on schedule.", "Should", "L61", "Export produces a valid .xlsx with the day's refunds."],
 ["TR-RPT-003", "The system shall provide an operational ageing report of open claims by status and age.", "Could", "L13", "Report lists open claims bucketed by age."],
 ["TR-FRD-001", "The system shall flag a customer/claim when return frequency exceeds a configurable threshold (default 3 in 30 days).", "Should", "L33 / AS-10", "A 4th return in 30 days is flagged in the queue and dashboard."],
 ["TR-ADM-001", "The system shall provide an admin console to configure thresholds, return windows, categories and notification templates.", "Must", "L50/L25", "Admin can change manager threshold and it takes effect without redeploy."],
 ["TR-ADM-002", "The system shall enforce role-based access for Store Staff, Store Manager, Finance, CS and Admin.", "Must", "L37/L30", "Finance cannot perform store intake; staff cannot approve refunds."],
 ["TR-ADM-003", "The system shall support SSO with SiamMart Active Directory (subject to OI-08).", "Should", "L56 / OI-08", "AD user signs in via SSO without a separate password."],
 ["TR-MIG-001", "The system shall migrate 1 year of historical return records from the legacy Excel source with record counts reconciled.", "Must", "L55 / AS-08", "Migrated row count equals source count (net of rejected rows reported)."],
]
for idx, part in enumerate(_chunks(tr_rows, 11)):
    hdr = ('<h1>6&nbsp;&nbsp;Technical Requirements (TR)</h1><p class="small">Each requirement is one testable '
           '"The system shall&hellip;" statement with ID, priority, source and measurable acceptance. '
           '24 of the 30 TRs are Must. All SAP/POS calls route via TK-Connect (see §8).</p>') if idx==0 else '<h2>6.1 Technical requirements (cont.)</h2>'
    PAGES.append(page(hdr + T(["ID", "Requirement (The system shall&hellip;)", "Pri.", "Source", "Acceptance"],
        part, widths=["17mm","auto","11mm","16mm","auto"])))

# =====================================================================
# PAGES — 7 NFR
# =====================================================================
nfr_rows = [
 ["NFR-PERF-001", "Performance", "Interactive screens render in &le;2s p95; order retrieval &le;2s p95; refund posting accepted in &le;5s.", "Load test at peak proves p95 thresholds."],
 ["NFR-SCAL-001", "Scalability (peak)", "Sustain peak of 5&times; average (AS-09): assumed avg 25,000 returns/month (~833/day) &rarr; size for &ge;4,200 returns/day, &ge;1,000 concurrent customer sessions and &ge;100 concurrent store tablets with 30% headroom.", "Peak load test at 4,200/day passes with headroom."],
 ["NFR-AVAIL-001", "Availability &amp; RTO/RPO", "Availability &ge;99.5%/month; RTO &le;4h; RPO &le;1h; no planned downtime during 11.11/12.12 windows.", "Failover drill meets RTO/RPO."],
 ["NFR-SEC-001", "Security &amp; access", "TLS 1.2+ in transit; AES-256 at rest; RBAC enforced server-side; MFA for admin; secrets in TK-Vault; OWASP Top-10 addressed.", "Security scan + RBAC test pass."],
 ["NFR-PRIV-001", "Privacy / PDPA", "PDPA-compliant: lawful basis per data element, consent capture where needed, right-to-access/erasure, masking in non-prod, retention-bound (§7.2).", "PDPA review sign-off by K.Arthit."],
 ["NFR-AUDIT-001", "Audit logging", "Immutable audit log of every state change and rule evaluation (who, what, when, inputs), retained 7 years, tamper-evident.", "Audit log reconstructs a sampled refund end-to-end."],
 ["NFR-USAB-001", "Usability &amp; accessibility", "Store return creation in &le;5 taps after scan; font &ge;16sp default; WCAG 2.1 AA; new-staff training &le;30 min.", "Usability test with 5 store staff meets targets."],
 ["NFR-L10N-001", "Localization", "Full TH/EN UI; Thai fonts (Sarabun); dates/numbers localized; no hard-coded strings.", "Both locales verified on all screens."],
 ["NFR-DATA-001", "Data retention &amp; archiving", "Transaction &amp; evidence retained 7 years (AS-05); personal data per PDPA retention; archive after active period; purged on erasure where lawful.", "Retention job + archive verified."],
 ["NFR-SUPP-001", "Supportability", "Centralized logging, health monitoring, alerting (TK-Monitor); run-books; TK-hosted with MA option (L45).", "Monitoring dashboards + alerts demonstrated."],
 ["NFR-COMP-001", "Browser / device", "Support current Chrome, Edge, Safari; store tablets on Android &amp; iPadOS; responsive from 360px to desktop.", "Device matrix test pass."],
 ["NFR-MAINT-002 (N/A note)", "Maintainability", "N/A as a separate line — covered by TK platform standards &amp; code review; no bespoke metric required for Phase 1.", "Review checklist."],
]
for idx, part in enumerate(_chunks(nfr_rows, 6)):
    hdr = ('<h1>7&nbsp;&nbsp;Non-Functional Requirements (NFR)</h1><p class="small">Every row of the '
           'tk-ba-technical-requirements NFR checklist is answered (Performance, Scalability, Availability/RTO-RPO, '
           'Security, Privacy/PDPA, Audit, Usability, Localization, Data retention, Supportability, Browser/device). '
           'One row is explicitly N/A with a reason.</p>') if idx==0 else '<h2>7.1 NFR (cont.)</h2>'
    PAGES.append(page(hdr + T(["ID", "Category", "Requirement / target", "Verification"],
        part, widths=["24mm","22mm","auto","auto"])))

# NFR checklist coverage page + PDPA inventory
PAGES.append(page("""
<h1>7&nbsp;&nbsp;NFR (cont.)</h1>
<h2>7.1a NFR checklist coverage</h2>
""" + T(["Checklist item", "Covered by", "Status"],
        [["Performance", "NFR-PERF-001", "Covered"],
         ["Scalability (peak 11.11/12.12)", "NFR-SCAL-001", "Covered"],
         ["Availability &amp; RTO/RPO", "NFR-AVAIL-001", "Covered"],
         ["Security &amp; access control", "NFR-SEC-001", "Covered"],
         ["Privacy / PDPA (consent, retention, erasure)", "NFR-PRIV-001 + §7.2", "Covered"],
         ["Audit logging", "NFR-AUDIT-001", "Covered"],
         ["Usability &amp; accessibility", "NFR-USAB-001", "Covered"],
         ["Localization (TH/EN)", "NFR-L10N-001", "Covered"],
         ["Data retention &amp; archiving", "NFR-DATA-001", "Covered"],
         ["Supportability (logging, monitoring)", "NFR-SUPP-001", "Covered"],
         ["Browser / device support", "NFR-COMP-001", "Covered"],
         ["Maintainability", "N/A — TK platform standards &amp; code review", "N/A (reason given)"],
        ], widths=["auto","auto","26mm"]) + """
<h2>7.2 PDPA personal-data inventory</h2>
<p class="small">Legal basis is per Thailand PDPA (พ.ร.บ.คุ้มครองข้อมูลส่วนบุคคล พ.ศ. 2562). Retention aligns
with the Revenue Code accounting period (7 years) unless a shorter lawful period applies. Masking applies in
non-production and to users who do not need the raw value.</p>
"""))

PAGES.append(page("""
<h1>7&nbsp;&nbsp;PDPA personal-data inventory (cont.)</h1>
""" + T(["Data element", "Class.", "Source", "Purpose", "Legal basis", "Retention", "Masking", "Access role"],
        [["Customer name", "PII", "Customer / order", "Identify claimant &amp; refund", "Contract performance", "7y (txn)", "Partial (K. Som…) non-prod", "CS, Finance"],
         ["Mobile phone", "PII", "Customer / order", "Notifications, lookup", "Contract performance", "7y", "****1234", "CS, Store"],
         ["Email", "PII", "Customer / order", "Notifications, receipts", "Contract performance", "7y", "a***@domain", "CS"],
         ["Delivery address", "PII", "Order", "Return pickup if needed", "Contract performance", "7y", "Masked non-prod", "CS"],
         ["Receipt / order no.", "Txn", "POS / order", "Link return to sale", "Contract performance", "7y", "None (not PII alone)", "All ops"],
         ["Payment card (last 4 / token)", "Sensitive", "POS / PSP", "Refund to source", "Contract performance", "7y (token)", "**** **** **** 1234", "Finance"],
         ["PromptPay / bank account", "Sensitive", "Customer", "Refund disbursement", "Contract performance", "7y", "masked acct", "Finance"],
         ["Product return photos", "Txn/evidence", "Customer / staff", "Condition evidence &amp; audit", "Legitimate interest / legal obligation", "7y (AS-05)", "N/A (product only)", "CS, Store, Ops"],
         ["Return reason / condition", "Txn", "Customer / staff", "Process &amp; analytics", "Contract performance", "7y", "N/A", "CS, Ops, Exec"],
         ["Chat / email transcripts", "PII", "returns@ mailbox, chat", "Case handling", "Contract performance", "2y", "Masked non-prod", "CS"],
         ["Device / IP / session logs", "Telemetry", "System", "Security &amp; audit", "Legitimate interest", "1y", "Truncated IP", "IT/Admin"],
         ["Staff user identity (AD)", "PII", "SiamMart AD", "Auth &amp; audit of approvals", "Legitimate interest", "7y (audit)", "N/A", "Admin/IT"],
        ], widths=["24mm","14mm","20mm","auto","auto","14mm","22mm","18mm"]) + """
<div class="note"><b>PDPA controls required</b> (traced to NFR-PRIV-001): consent/notice at intake where basis is
consent; data-subject access &amp; erasure endpoints; minimisation (collect only what a return needs);
masking in non-production; encryption at rest &amp; in transit; documented retention; and DPIA review with
K.Arthit before go-live. AI image inspection (out of scope) would require a separate PDPA assessment.</div>
"""))

# =====================================================================
# PAGES — 8 INTEGRATION REQUIREMENTS (full fields)
# =====================================================================
def int_block(iid, name, system, direction, protocol, trigger, dataobj, volume, errhandling, owner, rule):
    return f"""
<h2>{iid} &mdash; {name}</h2>
<table class="kv">
<tr><td>System</td><td>{system}</td></tr>
<tr><td>Direction</td><td>{direction}</td></tr>
<tr><td>Protocol / pattern</td><td>{protocol}</td></tr>
<tr><td>Trigger / frequency</td><td>{trigger}</td></tr>
<tr><td>Data objects</td><td>{dataobj}</td></tr>
<tr><td>Volume</td><td>{volume}</td></tr>
<tr><td>Error handling &amp; retry</td><td>{errhandling}</td></tr>
<tr><td>Owner</td><td>{owner}</td></tr>
<tr><td>Architecture rule</td><td>{rule}</td></tr>
</table>"""

PAGES.append(page('<h1>8&nbsp;&nbsp;Integration Requirements (INT)</h1>'
 '<p class="small"><b>Binding architecture rule:</b> every integration below traverses <b>TK-Connect</b>. '
 'No component may call SAP RFC, POS or marketplace APIs directly. SAP ECC 6.0 exposes RFC today, but per '
 'K.Arthit (L27) nobody may touch it directly &mdash; TK-Connect fronts it. Money flows are idempotent, '
 'reconciled and audited.</p>'
 + int_block("INT-SAP-01", "SAP ECC 6.0 refund posting &amp; reconciliation", "SAP ECC 6.0 (Finance)",
   "Bi-directional (post refund out, confirm/status in)", "TK-Connect connector (OData/IDoc adapter); no direct RFC from any channel",
   "Per approved refund (near-real-time) + nightly reconciliation batch",
   "Refund document (amount, currency, payment method, order ref, customer ref), posting result/status",
   "≈25,000 returns/month peak; refund postings similar order of magnitude",
   "At-least-once with idempotency key; exponential backoff; dead-letter queue; manual replay; daily mismatch report (TR-RFD-005)",
   "K.Arthit (SiamMart IT) / TK SA", "No direct RFC &mdash; TK-Connect only") +
 '<div class="warn">INT-SAP-01 is the critical money path. Duplicate prevention (TR-RFD-004) and daily reconciliation (TR-RFD-005) are mandatory, not optional.</div>'))

PAGES.append(page('<h1>8&nbsp;&nbsp;Integration Requirements (cont.)</h1>'
 + int_block("INT-POS-01", "POS order retrieval by receipt", "POS (vendor RetailPro or in-house &mdash; OI-05)",
   "Inbound (read order/line/receipt data)", "TK-Connect connector to POS API/DB view (read-only); protocol confirmed after OI-05",
   "On demand (receipt scan) + periodic reference sync",
   "Order header, lines, prices, discounts, payment method, tender, store/date",
   "≈number of in-store returns; bursty at peak",
   "≤2s p95 target; timeout → manual search fallback (TR-RET-008); retry with backoff; circuit-breaker",
   "K.Arthit / TK SA", "No direct POS access &mdash; TK-Connect only") +
 int_block("INT-AD-01", "SSO with SiamMart Active Directory", "SiamMart AD / IdP",
   "Inbound authentication", "SAML 2.0 / OIDC via TK-Auth federated to AD",
   "On login; token refresh",
   "User identity, groups/roles, session",
   "All internal users",
   "Auth failure → clear error, fallback local admin break-glass; token expiry re-auth",
   "K.Arthit / TK SA", "Subject to OI-08") +
 '<p class="small">Additional integration: <b>INT-NTF-01</b> &mdash; outbound notifications to SMS / LINE / email gateways via TK-Notify (event-driven, per TR-NTF-001, channel selection = OI-07). <b>INT-MIG-01</b> &mdash; one-off batch migration of 1 year of legacy Excel returns via TK-Connect staging (per TR-MIG-001).</p>'))

PAGES.append(page('<h1>8&nbsp;&nbsp;Integration Requirements (cont.)</h1>'
 + int_block("INT-NTF-01", "Customer notification gateways", "SMS / LINE Messaging / Email providers",
   "Outbound", "TK-Notify abstraction over provider APIs",
   "On every status-change event (TR-NTF-001)",
   "Recipient, template code, template variables, channel",
   "Multiple messages per return; peak-scaled",
   "Provider failover to next channel; retry; delivery-status capture; do-not-loop guard",
   "TK SA", "Channels via TK-Notify; selection = OI-07") +
 int_block("INT-MIG-01", "Legacy return-data migration (1 year)", "Legacy Excel (RETURN_MASTER + branch files)",
   "Inbound one-off", "Batch extract → TK-Connect staging → load with validation",
   "One-off during cutover (and pilot subset earlier)",
   "Historical return cases, items, refund status, evidence links",
   "~1 year history (AS-08); counts reconciled",
   "Row-level validation; rejected-row report; re-runnable idempotent load; count reconciliation",
   "TK BA / TK SA", "Customer provides source files (dependency D-6)") +
 '<div class="note"><b>Phase 2 (out of scope):</b> INT-MKT-01 &mdash; Shopee / Lazada marketplace returns via TK-Connect, deferred (L29). It will reuse the same intake and refund core.</div>'))

# =====================================================================
# SECTION 9 — FUNCTIONAL SPECIFICATION (one FS per module)
# =====================================================================
def fs_page(fid, title, purpose, actors, pre, post, flow, alt, brls, fields, status, notif, reports, linked):
    rows = "".join(f"<tr><td>{i+1}</td><td>{f}</td></tr>" for i, f in enumerate(flow))
    altrows = "".join(f"<tr><td>{a[0]}</td><td>{a[1]}</td></tr>" for a in alt)
    fld = T(["Field", "Type", "Mand.", "Validation", "Source", "Remark"], fields,
            widths=["24mm","18mm","10mm","auto","18mm","20mm"])
    nt = T(["Event", "Channel", "Recipient", "Template", "Timing"], notif, widths=["auto","18mm","20mm","auto","16mm"]) if notif else '<p class="small">No notifications raised by this module.</p>'
    top = page(f"""
<h1>9&nbsp;&nbsp;Functional Specification &mdash; {fid}</h1>
<h2>{fid} &mdash; {title}</h2>
<h3>Purpose</h3><p>{purpose}</p>
<h3>Actors</h3><p>{actors}</p>
<h3>Pre-conditions / Post-conditions</h3>
<table class="kv"><tr><td>Pre</td><td>{pre}</td></tr><tr><td>Post</td><td>{post}</td></tr></table>
<h3>Main flow</h3>
<table><thead><tr><th style="width:8mm">#</th><th>User action &rarr; System response</th></tr></thead><tbody>{rows}</tbody></table>
<h3>Alternative / exception flows</h3>
<table><thead><tr><th style="width:12mm">Step</th><th>Branch</th></tr></thead><tbody>{altrows}</tbody></table>
<h3>Business rules applied</h3><p class="small">{brls}</p>
""")
    bottom = page(f"""
<h1>9&nbsp;&nbsp;Functional Specification &mdash; {fid} <span class="small">(cont.)</span></h1>
<h3>Screen / field definition</h3>{fld}
<h3>Status model</h3><p class="small">{status}</p>
<h3>Notifications</h3>{nt}
<h3>Reports / data output</h3><p class="small">{reports}</p>
<h3>Linked requirements</h3><p class="small">{linked}</p>
""")
    return top + bottom

# FS-RET-01
PAGES.append(fs_page("FS-RET-01", "Return Request Intake (customer web/LINE + store tablet)",
 "Captures a return request from three intake paths — customer self-service (web portal, LINE OA) and staff-assisted store tablet — into one unified, validated case with item selection, reason, condition and photo evidence.",
 "Customer; Store Staff; CS Agent.",
 "Customer/staff authenticated; order exists in POS or online order store.",
 "A validated return case exists in status <i>Requested</i> with selected lines, evidence and computed refund preview.",
 ["Staff taps 'New return' → system shows scan/order capture screen.",
  "Staff scans receipt barcode → system retrieves order within 2s and lists returnable lines.",
  "User selects lines &amp; quantities (partial allowed) → system validates each against policy window/category and disables ineligible lines with reason.",
  "User picks coded return reason &amp; item condition, attaches 1–5 photos → system validates required fields.",
  "User confirms → system computes refund preview (net) and creates the case (status Requested).",
  "Online path: request arrives via web form or returns@ mailbox/LINE → system parses &amp; creates case in same queue."],
 [("2a","Barcode not found → system offers manual search by order/receipt/phone (TR-RET-008)."),
  ("3a","All lines ineligible → system blocks submission and explains window/category."),
  ("4a","Photo exceeds size/format → system rejects with guidance."),
  ("6a","Email cannot be parsed to an order → case created as 'unmatched' for CS triage.")],
 "BRL-004 (return window), BRL-005 (refund method preview), BRL-007 (partial return), BRL-012 (eligibility). Subject to AS-02/AS-07.",
 [["Receipt barcode","scan/text","Y","valid SiamMart order","POS","Code128/QR"],
  ["Order no. / phone","text","N","matches an order","POS","manual fallback"],
  ["Selected lines &amp; qty","multi-select","Y","≥1 line, qty ≤ purchased","order","partial ok"],
  ["Return reason","coded list","Y","one of configured reasons","admin","BRL"],
  ["Item condition","coded list","Y","new/used/damaged","staff",""],
  ["Photo(s)","file 1–5","Y","jpg/png ≤10MB","camera","evidence"],
  ["Refund method","radio","Y","card/PromptPay/store credit","customer","BRL-005"],
  ["Language","toggle","N","TH/EN","user","TR-RET-009"]],
 "Requested → (Validated) → Pending Approval → Approved / Rejected → Received → Refunded → Closed; plus Cancelled.",
 [["Case created","SMS/LINE/email","Customer","RCPT-CREATED","immediate"],
  ["Needs more info","email/LINE","Customer","RCPT-INFO","immediate"]],
 "Case record + evidence stored; feeds dashboard (FS-RPT-01).",
 "TR-RET-001, TR-RET-002, TR-RET-003, TR-RET-004, TR-RET-005, TR-RET-006, TR-RET-007, TR-RET-008, TR-RET-009, INT-POS-01; US-001…US-006, US-026."))

# FS-APR-01
PAGES.append(fs_page("FS-APR-01", "Approval Workflow",
 "Applies policy and amount rules to a Requested case and routes it to the correct approver(s): automatic approval, store-manager approval and/or finance approval, with SLA tracking. Supports both sides of OI-01 as configuration.",
 "Store Manager; Finance Officer; CS Agent; System (rule engine).",
 "Case in status Requested/Validated.",
 "Case approved or rejected with a recorded, auditable approver decision and rationale.",
 ["System evaluates BRL-003 (amount > 5,000 → manager) and BRL-001/BRL-002 (auto vs finance, per OI-01 configuration).",
  "If manager required → case routed to store-manager queue; manager approves/rejects with comment.",
  "If finance required → case routed to Finance queue; Finance approves/rejects.",
  "If auto-approval enabled and amount below threshold → system approves automatically and logs rule inputs.",
  "On approval → case moves to Approved and triggers refund (FS-RFD-01).",
  "SLA timer runs per queue; on breach → escalate to next approver/manager."],
 [("1a","OI-01 unresolved → system runs conservative default (all to Finance) and flags case."),
  ("2a","Manager rejects → case Rejected; customer notified; ends."),
  ("3a","Finance requests info → case returns to CS for completeness."),
  ("4a","Auto-approval disabled → all cases require finance.")],
 "BRL-001, BRL-002, BRL-003, BRL-008. OI-01 governs switching.",
 [["Refund amount","computed","Y","≥0","order","drives routing"],
  ["Approval decision","radio","Y","approve/reject","approver",""],
  ["Comment","text","N","≤500 chars","approver","audit"],
  ["Approver identity","system","Y","from AD/session","auth","audit"]],
 "Requested/Validated → Pending Manager → Pending Finance → Approved / Rejected; Escalated as overlay.",
 [["Sent for approval","email/in-app","Approver","APR-TO-APPROVER","immediate"],
  ["Approved","SMS/LINE/email","Customer","RCPT-APPROVED","immediate"],
  ["Rejected","SMS/LINE/email","Customer","RCPT-REJECTED","immediate"],
  ["SLA breach","email","Next approver/manager","APR-ESCALATE","on breach"]],
 "Approval audit trail; feeds ageing report (TR-RPT-003).",
 "TR-APR-001…TR-APR-004, TR-ADM-001, TR-ADM-002; US-007, US-008, US-009; OI-01."))

# FS-RFD-01
PAGES.append(fs_page("FS-RFD-01", "Refund Processing &amp; Disbursement",
 "Computes the refund net of discounts and partial lines, disburses to the original payment method via TK-Connect→SAP (or issues store credit), guarantees idempotency and reconciles daily against SAP.",
 "Finance Officer; System; SAP (via TK-Connect).",
 "Case in status Approved with an approved amount.",
 "Refund posted (or store credit issued), SAP document recorded, case Refunded, reconciliation entry created.",
 ["System computes net refund amount for approved lines (BRL refund calc).",
  "Finance/customer confirms refund method (original method or store credit).",
  "System creates an idempotent refund instruction and posts to SAP via TK-Connect (INT-SAP-01).",
  "SAP returns posting result/document no. → system stores it and sets case Refunded.",
  "Nightly batch reconciles system refunds vs SAP postings and flags mismatches.",
  "If store credit → system issues credit (+ configurable bonus, default 5%)."],
 [("3a","SAP unavailable → instruction queued with retry; case stays Approved-PendingRefund."),
  ("3b","Duplicate detected (same idempotency key) → suppressed, no second posting."),
  ("5a","Reconciliation mismatch → flagged to Finance for manual review; case noted.")],
 "BRL-005, BRL-006, BRL-008; TR-RFD-001…005.",
 [["Approved amount","computed","Y","matches approved claim","claim",""],
  ["Refund method","radio","Y","card/PromptPay/store credit","customer/finance","BRL-005"],
  ["Bonus %","computed","N","0–configured max","admin","BRL-006"],
  ["SAP document no.","system","Y","returned by SAP","SAP","audit"]],
 "Approved → Refund Pending → Refunded (or Refund-Failed→retry); Closed after disposition.",
 [["Refund initiated","SMS/LINE/email","Customer","RCPT-REFUND-START","immediate"],
  ["Refund completed","SMS/LINE/email","Customer","RCPT-REFUNDED","on SAP confirm"]],
 "Daily refund report (TR-RPT-002); daily reconciliation report (TR-RFD-005).",
 "TR-RFD-001…TR-RFD-005, INT-SAP-01, INT-NTF-01; US-010, US-011, US-012, US-024; OI-01."))

# FS-DSP-01
PAGES.append(fs_page("FS-DSP-01", "Returned-Goods Disposition",
 "Records what happens to each returned item (restock / return-to-supplier / write-off) at the store and lets HQ Operations track disposition status by branch, closing the 'pile behind the store' gap.",
 "Store Staff; HQ Operations.",
 "Item physically received at store against a case.",
 "Each received item has a disposition recorded; case can close.",
 ["Staff marks items received against the case.",
  "Staff inspects condition and selects disposition per item (restock / supplier / write-off) per BRL-010.",
  "System records disposition with reason; restock items feed inventory adjustment note.",
  "HQ Ops views disposition status by branch/date.",
  "When all items dispositioned and refund complete → case Closed."],
 [("2a","Item missing/damaged → disposition 'write-off' with mandatory reason."),
  ("2b","Supplier-return requires RMA ref → captured in free-text/ref field.")],
 "BRL-010.",
 [["Item","list","Y","from case lines","claim",""],
  ["Disposition","coded","Y","restock/supplier/write-off","staff","BRL-010"],
  ["Reason/ref","text","cond.","required for write-off / supplier","staff",""],
  ["Received date","date","Y","≤ today","system",""]],
 "Received → Dispositioned → Closed.",
 [],
 "Disposition status report by branch (TR-DSP-002).",
 "TR-DSP-001, TR-DSP-002; US-013, US-014."))

# FS-NTF-01
PAGES.append(fs_page("FS-NTF-01", "Customer Notifications &amp; Tracking",
 "Notifies the customer at every status change on the configured channel(s) and provides a tracking page with a status timeline, giving 'like parcel tracking' transparency.",
 "Customer; System; Notification gateways.",
 "Case exists.",
 "Customer has been notified of each transition; tracking page reflects current status.",
 ["A status-change event is published by FS-APR/RFD/DSP.",
  "System resolves recipient + template + channel preference (per OI-07 configuration).",
  "System sends via TK-Notify (INT-NTF-01) and records delivery status.",
  "Customer opens tracking link → sees status timeline and next expected step."],
 [("2a","Channel unavailable → failover to next channel; log failure."),
  ("3a","Customer has no contact → in-app only; CS alerted.")],
 "Notification matrix; channels per OI-07.",
 [["Event","system","Y","defined events","workflow",""],
  ["Channel","config","Y","SMS/LINE/email","admin","OI-07"],
  ["Template","admin","Y","exists","admin",""],
  ["Tracking token","system","Y","signed, expiring","system",""]],
 "Notification status: Queued → Sent → Delivered / Failed.",
 [["Every status change","SMS/LINE/email","Customer","RCPT-<STATUS>","per event"]],
 "Delivery report (internal).",
 "TR-NTF-001, TR-NTF-002, INT-NTF-01; US-015, US-016; OI-07."))

# FS-RPT-01
PAGES.append(fs_page("FS-RPT-01", "Reporting &amp; Executive Dashboard",
 "Gives executives a daily dashboard of return volume, reason mix, branch ranking and fraud flags, and gives Finance a daily refund report export to Excel.",
 "Executive; Finance; CS Manager.",
 "Cases exist (live + migrated).",
 "Dashboard and export reflect source data for the selected period.",
 ["Executive opens dashboard → selects period/region → system shows KPIs.",
  "System computes: returns count, reason breakdown, branch ranking, fraud-flag count, refund lead time.",
  "Finance requests daily refund report → system generates .xlsx (on demand or scheduled).",
  "Operational users view ageing report of open claims."],
 [("1a","No data for period → dashboard shows zero-state, not error."),
  ("3a","Export too large → system generates async and notifies when ready.")],
 "KPI definitions; TR-RPT-001…003.",
 [["Period","date range","Y","valid range","user",""],
  ["Region/branch","filter","N","valid","user",""],
  ["Report type","select","Y","refund/ageing","user",""]],
 "N/A (read-only outputs).",
 [],
 "Executive dashboard (TR-RPT-001); daily refund .xlsx (TR-RPT-002); operational ageing (TR-RPT-003).",
 "TR-RPT-001, TR-RPT-002, TR-RPT-003; US-017, US-018."))

# FS-FRD-01
PAGES.append(fs_page("FS-FRD-01", "Fraud Flagging",
 "Flags customers or claims that exceed a configurable return-frequency threshold (default 3 returns in a rolling 30 days) so CS can review repeat returners, without auto-blocking.",
 "CS Agent; System.",
 "Cases exist for the customer.",
 "Flagged cases/customers are visible in the queue and dashboard for review.",
 ["On case creation/approval, system evaluates BRL-011 against the customer's history.",
  "If threshold exceeded → case flagged and customer tagged 'repeat-returner'.",
  "CS sees flag in queue and dashboard and can annotate the case.",
  "Flag is advisory only; it does not auto-reject."],
 [("1a","No history → no flag."),
  ("2a","Customer disputes → CS clears/maintains flag with comment (audited).")],
 "BRL-011 (threshold = AS-10).",
 [["Threshold","config","N","3 / 30 days default","admin","AS-10"],
  ["Flag","system","—","—","rules","advisory"],
  ["CS note","text","N","≤500","CS","audit"]],
 "Flag: none / flagged / cleared (on claim).",
 [],
 "Fraud-flag count on dashboard (TR-RPT-001).",
 "TR-FRD-001; US-019; AS-10."))

# FS-ADM-01
PAGES.append(fs_page("FS-ADM-01", "Policy &amp; Administration Configuration",
 "Lets authorised admins configure thresholds, return windows, categories, notification templates and role permissions — so policy changes (incl. OI-01 outcome) are configuration, not code — and enforces role-based access.",
 "Admin; IT.",
 "Admin authenticated with admin role.",
 "Configuration saved and effective without redeploy; RBAC enforced.",
 ["Admin opens config console → edits parameters (see §5.3) → validates → saves.",
  "System versions the change and writes an audit entry (who/what/when).",
  "Admin manages roles (Store Staff/Manager/Finance/CS/Admin) and permissions.",
  "Changes take effect immediately for new evaluations; live cases keep rule version used."],
 [("1a","Invalid value (e.g., threshold &gt; manager threshold) → validation error."),
  ("3a","Removing own admin role → prevented (last-admin guard).")],
 "BRL-001…BRL-011 thresholds; TR-ADM-001, TR-ADM-002, TR-ADM-003.",
 [["Parameter","input","Y","within bounds","§5.3",""],
  ["Role","select","Y","predefined","RBAC",""],
  ["Permission","checkbox","Y","permission set","RBAC",""]],
 "Config version: Draft → Active → Superseded.",
 [["Config changed","in-app/email","Admin, IT","ADM-CHANGED","immediate"]],
 "Config change log (audit).",
 "TR-ADM-001, TR-ADM-002, TR-ADM-003; US-020, US-021, US-022; OI-08."))

# =====================================================================
# SECTION 10 — USER STORIES
# =====================================================================
PAGES.append(page("""
<h1>10&nbsp;&nbsp;User Stories &amp; Acceptance Criteria</h1>
<h2>10.0 Epics overview</h2>
<p class="small">26 stories across 10 epics. Every Must story has at least one negative Gherkin scenario.
Sizes are T-shirt placeholders (S/M/L). Full INVEST stories and Gherkin acceptance criteria follow.</p>
""" + T(["Epic", "Name", "# Stories", "Primary TRs"],
        [["EP-01", "Customer Return Request", "3", "TR-RET-001/002/004"],
         ["EP-02", "Store Return Intake", "3", "TR-RET-003/005/008"],
         ["EP-03", "Approval Workflow", "3", "TR-APR-001…004"],
         ["EP-04", "Refund &amp; Disbursement", "3", "TR-RFD-001…005"],
         ["EP-05", "Returned-Goods Disposition", "2", "TR-DSP-001/002"],
         ["EP-06", "Notifications &amp; Tracking", "2", "TR-NTF-001/002"],
         ["EP-07", "Reporting &amp; Dashboard", "2", "TR-RPT-001/002"],
         ["EP-08", "Fraud Detection", "1", "TR-FRD-001"],
         ["EP-09", "Administration &amp; Policy", "3", "TR-ADM-001/002/003"],
         ["EP-10", "Integration &amp; Migration", "4", "INT-SAP-01, INT-POS-01, TR-MIG-001, TR-RET-009"],
        ], widths=["14mm","auto","18mm","auto"])))

def story(sid, epic, role, want, so_that, priority, size, trs, gherkin=None):
    g = f'<div class="gherkin">{gherkin}</div>' if gherkin else ""
    return (f'<div class="story"><div class="hd">{sid} &middot; {badge(priority)} &middot; {size} &middot; '
            f'<span class="small">TR: {trs}</span></div>'
            f'As a <b>{role}</b>, I want to <b>{want}</b> so that <b>{so_that}</b>.{g}</div>')

PAGES.append(page("<h1>10&nbsp;&nbsp;User Stories &mdash; EP-01 Customer Return Request</h1>"
 + "<h2>EP-01 Customer Return Request</h2>"
 + story("US-001","EP-01","customer","raise a return from the web portal","I don't have to phone or email and wait",
   "Must","M","TR-RET-001",
   "Scenario: valid self-service return\n  Given I am a logged-in customer with order \"SO-1001\" within policy\n  When I select 1 item, a reason and confirm\n  Then a return case is created and I see a case ID\n\nScenario: item outside return window (negative)\n  Given my order is 40 days old (electronics category)\n  When I try to return it\n  Then the item is disabled with reason \"outside 7-day window\" and I cannot submit")
 + story("US-002","EP-01","customer","attach photos and a reason","CS can assess condition without me visiting",
   "Must","S","TR-RET-004",
   "Scenario: photo required\n  Given I am creating a return\n  When I press submit without any photo\n  Then the system blocks submission and asks for a photo\n\nScenario: oversized file (negative)\n  Given I attach a 20MB image\n  Then the system rejects it and asks for ≤10MB")
 + story("US-003","EP-01","customer","raise a return via LINE OA","I can use the channel I already have",
   "Must","M","TR-RET-002",
   "Scenario: LINE request lands in queue\n  Given I submit a return through LINE OA\n  Then a case appears in the CS queue with the same fields as web\n\nScenario: unparseable message (negative)\n  Given my LINE message has no order reference\n  Then the case is created as 'unmatched' for CS triage, not lost")
))
PAGES.append(page("<h1>10&nbsp;&nbsp;User Stories &mdash; EP-02 Store Return Intake</h1>"
 + "<h2>EP-02 Store Return Intake</h2>"
 + story("US-004","EP-02","store staff","scan the customer's receipt","I don't have to re-type order details",
   "Must","M","TR-RET-003, INT-POS-01",
   "Scenario: valid receipt\n  Given I am store staff at branch \"Bangna\"\n  When I scan receipt \"R-2026-000123\"\n  Then the order lines eligible for return appear in ≤2s\n\nScenario: foreign barcode (negative)\n  Given I scan a non-SiamMart barcode\n  Then the system shows \"Receipt not found\" and offers manual search")
 + story("US-005","EP-02","store staff","choose only some items to return","a customer can return part of an order",
   "Must","S","TR-RET-005",
   "Scenario: partial return\n  Given an order has 4 lines\n  When I select 2 lines and confirm\n  Then only those 2 lines are refunded\n\nScenario: over-quantity (negative)\n  Given I try to return 3 of 2 purchased units\n  Then the system caps qty at 2 and warns me")
 + story("US-006","EP-02","store staff","search for the order manually","a damaged barcode doesn't stop the return",
   "Must","S","TR-RET-008",
   "Scenario: manual search\n  Given a barcode is unreadable\n  When I search by phone number\n  Then matching orders are shown\n\nScenario: no match (negative)\n  Given no order matches the phone\n  Then the system shows 'no order found' and offers to create an unmatched case")
))
PAGES.append(page("<h1>10&nbsp;&nbsp;User Stories &mdash; EP-03 Approval Workflow</h1>"
 + "<h2>EP-03 Approval Workflow</h2>"
 + story("US-007","EP-03","CS/finance process owner","have small refunds auto-approved when the rule is enabled","low-value refunds aren't delayed",
   "Must","S","TR-APR-001, OI-01",
   "Scenario: auto-approve enabled\n  Given auto-approval is enabled at ≤500 THB\n  When a 400 THB refund is validated\n  Then it is approved automatically and the rule inputs are logged\n\nScenario: rule disabled (negative)\n  Given OI-01 resolved to 'finance approves all'\n  When a 400 THB refund is validated\n  Then it goes to Finance, not auto-approved")
 + story("US-008","EP-03","store manager","approve refunds above 5,000 THB","high-value refunds are controlled",
   "Must","S","TR-APR-002",
   "Scenario: high value needs manager\n  Given a refund of 5,500 THB\n  Then it is blocked from Finance until a store manager approves\n\nScenario: manager rejects (negative)\n  Given the manager rejects the case\n  Then the case is Rejected and the customer is notified")
 + story("US-009","EP-03","finance officer","review a finance approval queue","audit-compliant control is maintained",
   "Must","M","TR-APR-003",
   "Scenario: finance queue\n  Given a case requires finance approval\n  Then it appears in my queue with full detail and approve/reject actions\n\nScenario: cannot bypass (negative)\n  Given a case needs finance approval\n  When someone tries to refund without it\n  Then the system blocks the refund")
 + "</p>"))

PAGES.append(page("<h1>10&nbsp;&nbsp;User Stories &mdash; EP-04 Refund &amp; Disbursement</h1>"
 + "<h2>EP-04 Refund &amp; Disbursement</h2>"
 + story("US-010","EP-04","finance officer","refund to the original payment method via SAP","money goes back the way it came, traceably",
   "Must","M","TR-RFD-001/002, INT-SAP-01",
   "Scenario: card refund\n  Given an approved 1,000 THB card refund\n  When I post it\n  Then it posts to SAP via TK-Connect and the SAP document no. is stored\n\nScenario: SAP down (negative)\n  Given SAP is unavailable\n  Then the refund is queued with retry and not double-posted")
 + story("US-011","EP-04","customer","receive store credit with a bonus","I get an incentive to shop again",
   "Must","S","TR-RFD-003",
   "Scenario: store credit with bonus\n  Given bonus is configured at 5%\n  When I choose store credit on a 1,000 THB refund\n  Then I receive 1,050 THB credit\n\nScenario: bonus set to 0 (negative)\n  Given bonus is 0%\n  Then store credit equals the net refund exactly")
 + story("US-012","EP-04","finance officer","get a daily reconciliation","I can prove no refund was duplicated or lost",
   "Must","M","TR-RFD-004/005",
   "Scenario: reconciliation clean\n  Given a day's refunds all posted once\n  Then the reconciliation report shows zero mismatches\n\nScenario: mismatch detected (negative)\n  Given one refund has no SAP posting\n  Then it is flagged in the next day's reconciliation report")
))
PAGES.append(page("<h1>10&nbsp;&nbsp;User Stories &mdash; EP-05 to EP-06</h1>"
 + "<h2>EP-05 Returned-Goods Disposition</h2>"
 + story("US-013","EP-05","store staff","record what happens to each returned item","stock isn't lost behind the store",
   "Must","S","TR-DSP-001",
   "Scenario: restock\n  Given I receive a resalable item\n  When I choose 'restock'\n  Then it is recorded for inventory adjustment\n\nScenario: close without disposition (negative)\n  Given items received but no disposition\n  Then the case cannot be closed")
 + story("US-014","EP-05","HQ operations","track disposition status by branch","I can see where stock is going",
   "Should","S","TR-DSP-002",
   "Scenario: branch view\n  Given multiple branches have dispositions\n  Then I can see counts by disposition and branch")
 + "<h2>EP-06 Notifications &amp; Tracking</h2>"
 + story("US-015","EP-06","customer","be told at every step","I know what's happening without calling",
   "Must","S","TR-NTF-001, INT-NTF-01",
   "Scenario: status change notifies\n  Given my case moves to Approved\n  Then I get a notification on my chosen channel within 60s\n\nScenario: channel fails (negative)\n  Given SMS gateway is down\n  Then the system fails over to the next channel and logs it")
 + story("US-016","EP-06","customer","track my return like a parcel","I trust it's progressing",
   "Must","S","TR-NTF-002",
   "Scenario: tracking page\n  Given my case ID\n  Then I see a status timeline with the next step\n\nScenario: invalid token (negative)\n  Given an expired tracking link\n  Then access is denied and CS can re-issue")
 + "</p>"))

PAGES.append(page("<h1>10&nbsp;&nbsp;User Stories &mdash; EP-07 to EP-08</h1>"
 + "<h2>EP-07 Reporting &amp; Dashboard</h2>"
 + story("US-017","EP-07","executive","view a returns dashboard","I can manage by facts",
   "Must","M","TR-RPT-001",
   "Scenario: dashboard\n  Given a selected period\n  Then I see volume, reason mix, branch ranking and fraud count\n\nScenario: empty period (negative)\n  Given a period with no returns\n  Then the dashboard shows a zero-state, not an error")
 + story("US-018","EP-07","finance officer","export the daily refund report to Excel","I can do my daily control",
   "Should","S","TR-RPT-002",
   "Scenario: export\n  Given today's refunds\n  Then I receive a valid .xlsx export\n\nScenario: large export (negative)\n  Given a very large day\n  Then the export runs async and notifies me when ready")
 + "<h2>EP-08 Fraud Detection</h2>"
 + story("US-019","EP-08","CS agent","see repeat-returner flags","I can review possible fraud",
   "Should","S","TR-FRD-001, AS-10",
   "Scenario: flag on 4th return\n  Given a customer's 4th return within 30 days\n  Then the case is flagged for review\n\nScenario: not auto-blocked (negative)\n  Given a flagged customer\n  Then the return is not auto-rejected; CS decides")
))
PAGES.append(page("<h1>10&nbsp;&nbsp;User Stories &mdash; EP-09 Administration &amp; Policy</h1>"
 + "<h2>EP-09 Administration &amp; Policy</h2>"
 + story("US-020","EP-09","admin","configure thresholds and windows","policy changes don't need code changes",
   "Must","S","TR-ADM-001",
   "Scenario: change threshold\n  Given I lower the manager threshold\n  Then new evaluations use it without redeploy\n\nScenario: invalid config (negative)\n  Given a threshold higher than the manager threshold\n  Then validation blocks the save")
 + story("US-021","EP-09","admin","manage roles and permissions","access is controlled",
   "Must","S","TR-ADM-002",
   "Scenario: RBAC\n  Given a Finance user\n  Then the user cannot perform store intake\n\nScenario: last admin guard (negative)\n  Given I try to remove my own admin role as the only admin\n  Then the system prevents it")
 + story("US-022","EP-09","SiamMart IT","sign in with AD SSO","staff use one corporate login",
   "Should","S","TR-ADM-003, OI-08",
   "Scenario: SSO success\n  Given a SiamMart AD user\n  Then they sign in via SSO without a separate password\n\nScenario: SSO failure (negative)\n  Given the IdP is unreachable\n  Then break-glass admin login is available and logged")
))
PAGES.append(page("<h1>10&nbsp;&nbsp;User Stories &mdash; EP-10 Integration &amp; Migration</h1>"
 + "<h2>EP-10 Integration &amp; Migration</h2>"
 + story("US-023","EP-10","SiamMart IT","retrieve POS order data via TK-Connect","no direct POS access is needed",
   "Must","M","INT-POS-01",
   "Scenario: order fetch\n  Given a receipt scan\n  Then the order is fetched via TK-Connect in ≤2s\n\nScenario: POS timeout (negative)\n  Then a circuit-breaker trips and manual search is offered")
 + story("US-024","EP-10","finance","post refunds to SAP only via TK-Connect","no direct RFC is used",
   "Must","M","INT-SAP-01",
   "Scenario: SAP via TK-Connect\n  Given a refund posting\n  Then it goes through TK-Connect, never a direct RFC\n\nScenario: direct-call attempt (negative)\n  Given any component tries a direct SAP RFC\n  Then it is blocked/denied by design")
 + story("US-025","EP-10","CS agent","access 1 year of migrated history","I can handle queries about past returns",
   "Must","M","TR-MIG-001, INT-MIG-01",
   "Scenario: migrated history\n  Given migration complete\n  Then I can search 1 year of prior returns\n\nScenario: count mismatch (negative)\n  Given a migration row fails validation\n  Then it is listed in a rejected-row report and counts are reconciled")
 + story("US-026","EP-10","any user","switch between TH and EN","I can work in my language",
   "Must","S","TR-RET-009",
   "Scenario: switch language\n  Given I toggle to EN\n  Then all labels switch and my choice persists\n\nScenario: missing translation (negative)\n  Given a missing EN string\n  Then it falls back to TH and is logged for fix")
 + "</p>"))

# =====================================================================
# SECTION 11 — TRACEABILITY MATRIX
# =====================================================================
PAGES.append(page("""
<h1>11&nbsp;&nbsp;Traceability Matrix</h1>
<p class="small">Maps every business requirement (the <i>why</i>) to its technical/non-functional/integration
requirements, functional spec, user stories and the key acceptance criterion. Every Must TR traces to at
least one BR and one US.</p>
""" + T(["BR", "TR / NFR / INT", "FS", "US", "Key acceptance criterion"],
 [["BR-01 Unified return intake (all channels)", "TR-RET-001…009", "FS-RET-01", "US-001…006, US-026", "A web, LINE and store request each create a case in one queue"],
  ["BR-02 Policy-driven eligibility &amp; approval", "TR-APR-001…004, TR-ADM-001, BRL-001…004", "FS-APR-01, FS-ADM-01", "US-007…009, US-020", "Correct router selected; ineligible items disabled with reason"],
  ["BR-03 Automated refund &amp; disbursement", "TR-RFD-001…005, INT-SAP-01", "FS-RFD-01", "US-010…012, US-024", "Refund posts to SAP once and reconciles daily"],
  ["BR-04 Returned-goods disposition", "TR-DSP-001, TR-DSP-002", "FS-DSP-01", "US-013, US-014", "Item cannot close without a disposition"],
  ["BR-05 Customer notifications &amp; tracking", "TR-NTF-001, TR-NTF-002, INT-NTF-01", "FS-NTF-01", "US-015, US-016", "Notification on each status change; tracking timeline"],
  ["BR-06 Reporting &amp; dashboard", "TR-RPT-001…003", "FS-RPT-01", "US-017, US-018", "Dashboard matches source data; Excel export valid"],
  ["BR-07 Fraud detection &amp; flagging", "TR-FRD-001 (AS-10)", "FS-FRD-01", "US-019", "4th return in 30 days flagged, not blocked"],
  ["BR-08 SAP &amp; POS integration (TK-Connect only)", "TR-RET-003, INT-POS-01, INT-SAP-01, US-023/024", "FS-RET-01, FS-RFD-01", "US-004, US-023, US-024", "No direct RFC/POS access; all via TK-Connect"],
  ["BR-09 PDPA compliance &amp; audit trail", "NFR-PRIV-001, NFR-AUDIT-001, NFR-SEC-001", "FS-ADM-01 (+§7.2)", "US-021", "Every state change auditable; PDPA inventory enforced"],
  ["BR-10 Migration &amp; localization", "TR-MIG-001, INT-MIG-01, TR-RET-009", "FS-ADM-01", "US-025, US-026", "1-year history migrated; TH/EN toggle works"],
 ], widths=["42mm","auto","26mm","26mm","auto"]) + """
<h2>11.1 Coverage checks</h2>
<ul class="small">
  <li><b>Must TR &rarr; US &amp; BR:</b> every one of the 24 Must TRs appears in §6 and maps to at least one US and one BR above.</li>
  <li><b>Conflict &rarr; design:</b> OI-01 is represented by BRL-001/BRL-002 and TR-APR-001/003, configurable either way (FS-ADM-01 / §5.3).</li>
  <li><b>Assumption &rarr; requirement:</b> every AS feeding a rule is referenced at the rule (BRL-004/006/009/011) and in §12.</li>
  <li><b>Gap scan:</b> no Must TR is orphaned; no BR lacks a FS; no Must story lacks a negative scenario.</li>
</ul>
"""))

# =====================================================================
# SECTION 12 — ASSUMPTIONS, CONSTRAINTS, DEPENDENCIES
# =====================================================================
PAGES.append(page("""
<h1>12&nbsp;&nbsp;Assumptions, Constraints &amp; Dependencies</h1>
<h2>12.1 Assumptions (AS) — each sized to the higher figure, owner to confirm</h2>
""" + T(["ID", "Assumption (how sized)", "Impact if wrong", "Owner to confirm"],
 [["AS-01", "Returns/month = <b>25,000</b> (higher of K.Nok ~18k vs K.Somchai ~25k); all capacity sizing uses this.", "If actual is 18k, capacity is over-provided (cost); if higher, sizing/peak insufficient.", "K.Somchai / K.Nok"],
  ["AS-02", "Return windows: electronics 7 days, others 30 days, default 14 days (L50; policy doc pending).", "Wrong windows reject valid returns or accept invalid ones.", "K.Nok (policy document)"],
  ["AS-03", "Baseline refund lead time up to <b>21 days</b> (of the 10–21 range) for benefit measurement.", "Benefit case overstated if true baseline is 10 days.", "K.Pim"],
  ["AS-04", "Slow-refund complaints ≈ <b>2,300/quarter</b> (L16, unconfirmed).", "Complaint-reduction KPI mis-based.", "CS / Marketing"],
  ["AS-05", "Evidence &amp; audit retention = <b>7 years</b> (L36, 'audit says 7?').", "Retention too short → audit non-compliance; too long → storage cost/PDPA.", "K.Arthit / Audit"],
  ["AS-06", "Store-credit +5% bonus is a marketing idea, not confirmed; configurable (default 5%).", "Margin impact if enabled without approval.", "K.Somchai / Marketing"],
  ["AS-07", "Partial returns are allowed ('probably yes', L52).", "If only full returns, refund logic simplifies but UX changes.", "K.Nok"],
  ["AS-08", "Historical migration = <b>1 year</b> only (L55).", "More history = more effort/cost.", "K.Somchai"],
  ["AS-09", "Peak multiplier = <b>5×</b> average for 11.11/12.12 (L35 says 4–5×).", "Under-sizing risks peak outage.", "K.Nok"],
  ["AS-10", "Fraud rule: ≥<b>3</b> returns in rolling <b>30</b> days → flag (proposed, L33).", "Wrong threshold floods CS or misses fraud.", "CS (K.Somchai)"],
  ["AS-11", "SAP ECC 6.0 is reachable only through TK-Connect; RFC exists but is not to be called directly (L27).", "If direct RFC were allowed, integration effort changes (but rule forbids it).", "K.Arthit"],
  ["AS-12", "Phase-1 budget envelope = <b>8,000,000 THB</b> (K.Somchai, L42); Finance has not yet agreed (OI-02).", "If Finance reduces the envelope, Must-scope must be re-phased.", "K.Pim / K.Somchai"],
 ], widths=["12mm","auto","auto","28mm"]) + """
<h2>12.2 Constraints (C)</h2>
""" + T(["ID", "Constraint", "Source"],
 [["C-01", "Phase-1 budget &le; 8,000,000 THB (Finance partly disagrees — OI-02).", "L42"],
  ["C-02", "Go-live before 11.11 2027 (Nov 2027) — fixed date tied to peak.", "L43"],
  ["C-03", "SiamMart IT has only 4 staff → TK to host and support (MA).", "L45"],
  ["C-04", "Avoid expensive third-party licence costs.", "L46"],
  ["C-05", "No direct SAP RFC / POS / marketplace access — TK-Connect only.", "Rule + L27"],
  ["C-06", "PDPA compliance mandatory (K.Arthit).", "L37"],
  ["C-07", "Data residency / hosting to be confirmed with K.Arthit (TK host).", "L45 / OI"],
 ], widths=["12mm","auto","16mm"]) + """
<h2>12.3 Dependencies (D)</h2>
<p class="small">D-1 Return policy document (K.Nok) · D-2 POS API access &amp; vendor confirmation (K.Arthit, OI-05) ·
D-3 SAP access &amp; test client via TK-Connect (K.Arthit) · D-4 AD/IdP details for SSO (K.Arthit, OI-08) ·
D-5 SMS/LINE/email gateway contracts (K.Somchai/TK) · D-6 Legacy Excel source files for migration (K.Somchai) ·
D-7 Bangna store process walk-through + test accounts/store devices · D-8 UAT participants from CS/Store/Finance.</p>
"""))

# =====================================================================
# SECTION 13 — OPEN ISSUES & CONFLICTS
# =====================================================================
PAGES.append(page("""
<h1>13&nbsp;&nbsp;Open Issues &amp; Conflicts</h1>
<p class="small">No conflict is resolved by assumption. Each carries both positions, a decision owner and a due date.</p>
""" + T(["ID", "Topic", "Position A", "Position B", "Decision owner", "Due"],
 [["OI-01", "<b>Auto-approval ≤500 THB</b> (CONFLICT)", "K.Somchai (Head of CS): refunds under 500 THB should be <b>auto-approved</b> to cut delay.</span>", "K.Pim (Finance): <b>no</b> auto-approval — <b>every refund must pass Finance</b> per audit control.", "K.Somchai + K.Pim; escalate to CEO/CFO if unresolved", "15 Nov 2026 (before FS sign-off)"],
  ["OI-02", "Phase-1 budget ≤8M THB (DISAGREEMENT)", "K.Somchai: budget &le; 8M THB for phase 1.", "Finance (K.Pim): not fully agreeing to the 8M envelope.", "K.Pim (Finance) with K.Somchai", "30 Nov 2026"],
  ["OI-03", "Process ownership", "CS (K.Somchai) owns the returns process.", "Store Ops (K.Nok) owns the branch process.", "K.Somchai (interim accountable)", "20 Nov 2026"],
  ["OI-04", "Self-service channel", "Web + native app (but app does not exist).", "LINE OA ('LINE OA ก็ได้' — K.Somchai).", "K.Somchai", "20 Nov 2026"],
  ["OI-05", "POS vendor &amp; API", "'RetailPro' (possible vendor).", "In-house POS — K.Arthit not sure.", "K.Arthit", "30 Nov 2026"],
  ["OI-06", "Exchange (เปลี่ยนของ) in scope", "Include exchange in Phase 1.", "Exclude — returns/refunds focus.", "K.Somchai", "20 Nov 2026"],
  ["OI-07", "Notification channels", "SMS", "LINE and/or email — selection unresolved (L31).", "CS (K.Somchai)", "30 Nov 2026"],
  ["OI-08", "SSO with SiamMart AD", "Use AD SSO.", "Local accounts acceptable for Phase 1.", "K.Arthit", "30 Nov 2026"],
 ], widths=["13mm","30mm","auto","auto","30mm","30mm"]) + """
<div class="oi" style="border-left:3px solid #a40000;padding:2mm 3mm;font-size:9pt">
<b>OI-01 in detail (mandatory).</b> This is the single most important open decision. It determines whether
FS-APR-01 auto-routes low-value refunds or sends everything to Finance. The package is built so either
outcome is a configuration change (§5.3, FS-ADM-01), with the audit-safe Finance-approval default in force
until decided. <b>Both positions, the decision owners (K.Somchai &amp; K.Pim) and the 15-Nov-2026 due date
must be confirmed in the next meeting.</b>
</div>
"""))

# =====================================================================
# SECTION 14 — COMMERCIAL NOTES (INTERNAL ONLY, landscape)
# =====================================================================
PAGES.append(page("""
<h1>14&nbsp;&nbsp;Commercial Notes &mdash; <span style="color:#a40000">TK INTERNAL ONLY</span></h1>
<div class="warn"><b>INTERNAL USE ONLY — REMOVE BEFORE CUSTOMER DELIVERY.</b> Contains TK's margin, budget and risk view; not for SiamMart. Figures are indicative planning estimates, not a quotation.</div>
<h2>14.1 Budget fit vs Must-scope (Phase 1 ≤ 8M THB)</h2>
""" + T(["Item", "Note", "Indicative impact (THB)", "Action"],
 [["Must-scope build", "Intake (web/LINE/store), approval, refund via SAP, disposition, notifications, dashboard, fraud, admin, 2 integrations, 1-year migration, TH/EN.", "≈ 6.5–8.5M (planning range)", "Phase carefully; see below"],
  ["Budget vs scope", "Must-set is large for an 8M ceiling — at the top of / potentially above budget if fraud, full dashboard and disposition automation are all Must. K.Pim is not convinced by 8M (OI-02).", "Risk of overshoot / commercial risk", "Move Should/Could to Phase 1b; re-confirm price after OI-02"],
 ], widths=["34mm","auto","34mm","40mm"]) + """
<h2>14.2 Hidden costs to surface</h2>
""" + T(["Hidden cost", "Note", "Impact", "Action"],
 [["SMS/LINE/email", "Per-message fees × several notifications × 25k returns/month (AS-01).", "Recurring OPEX", "Budget pass-through / MA"],
  ["SAP/POS integration", "Middleware effort, test client, reconciliation build — deceptively large.", "Effort", "Fixed-price exclusions / CR"],
  ["Data migration", "1-year Excel cleanup &amp; validation.", "Effort", "Separate migration line"],
  ["Branch hardware", "Tablets/scanners — customer's responsibility (AS-08).", "Customer cost", "State exclusions clearly"],
  ["Hypercare &amp; MA/hosting", "SiamMart IT is 4 people; TK will host + support (C-03).", "Recurring revenue for TK", "Propose MA contract"],
  ["Marketplace fees", "Phase-2 Shopee/Lazada API fees.", "Future", "Phase 2 budget"],
 ], widths=["30mm","auto","30mm","36mm"]) + """
<h2>14.3 Commercial risks</h2>
<ul class="small">
  <li><b>Fixed go-live vs 11.11 2027.</b> Hard deadline tied to peak. Any OI delay (esp. OI-01) compresses build. Reserve buffer + contingency; record as project risk.</li>
  <li><b>OI-01 resolution could expand finance scope</b> (if all refunds go to Finance) or change UX (auto-approval). Either way, keep it configurable to avoid re-work cost.</li>
  <li><b>Budget dissent (OI-02)</b> — do not commit to 8M scope until Finance confirms; prepare a Phase 1a/1b split option.</li>
</ul>
<h2>14.4 Upsell / future opportunities (do not commit now)</h2>
<p class="small">MA &amp; hosting (explicitly wanted, C-03) · Fraud analytics add-on · Phase-2 marketplace returns · AI product-condition image inspection (L62, out of scope) · QR-code drop-off (L60, Could).</p>
""", landscape=True))

# =====================================================================
# SECTION 15 — SIGN-OFF
# =====================================================================
PAGES.append(page("""
<h1>15&nbsp;&nbsp;Sign-off</h1>
<p>By signing, the parties confirm the requirements in this document (excluding §14 Commercial Notes, which
is TK-internal and removed before issue) are an accurate and agreed basis for Phase&nbsp;1, subject to the
open issues in §13 being resolved by their due dates and assumptions in §12.1 being confirmed.</p>
<table>
<thead><tr><th>Role</th><th>Name</th><th>Signature</th><th>Date</th></tr></thead>
<tbody>
<tr><td>Customer sponsor (Head of CS)</td><td>K.Somchai</td><td style="height:12mm"></td><td></td></tr>
<tr><td>Customer Finance</td><td>K.Pim</td><td style="height:12mm"></td><td></td></tr>
<tr><td>Customer IT</td><td>K.Arthit</td><td style="height:12mm"></td><td></td></tr>
<tr><td>Store Operations (consulted)</td><td>K.Nok</td><td style="height:12mm"></td><td></td></tr>
<tr><td>TK Company (author)</td><td>TK BA</td><td style="height:12mm"></td><td></td></tr>
<tr><td>TK Company (verified)</td><td>TK Senior BA</td><td style="height:12mm"></td><td></td></tr>
</tbody></table>
<div class="note" style="margin-top:6mm">
<b>Conditions of sign-off:</b>
<ol class="small">
<li>OI-01 (auto-approval ≤500 THB) closed by 15 Nov 2026 — blocking for FS-APR-01.</li>
<li>OI-02 (budget) and OI-05 (POS vendor) confirmed before build freeze.</li>
<li>AS-01, AS-02, AS-03, AS-05 confirmed before detailed design.</li>
<li>DPIA / PDPA review completed with K.Arthit before go-live.</li>
</ol></div>
"""))

# =====================================================================
# APPENDIX — GLOSSARY
# =====================================================================
PAGES.append(page("""
<h1>Appendix A&nbsp;&nbsp;Glossary (incl. Thai business terms)</h1>
""" + T(["Term / Thai", "Meaning"],
 [["สาขา (sathaan)", "Branch / store outlet. SiamMart has ~120."],
  ["คืนของ (kheun khong)", "Return goods — a customer returning purchased items."],
  ["ขอ refund", "Request a refund."],
  ["เปลี่ยนของ (plian khong)", "Exchange goods — swap for another item. Scope undecided (OI-06)."],
  ["ใบเสร็จ (bai set)", "Receipt — used for barcode order retrieval (TR-RET-003)."],
  ["ผู้จัดการ / manager", "Store manager — approves refunds &gt; 5,000 THB (BRL-003)."],
  ["DC", "Distribution Centre — destination option for returned goods (BRL-010)."],
  ["PDPA", "Thailand Personal Data Protection Act B.E. 2562 (2019) — privacy law governing customer data."],
  ["TK-Connect", "TK platform integration gateway — the ONLY path to SAP/POS/marketplace."],
  ["TK-Database / TK-Flow / TK-Notify / TK-Auth / TK-Monitor / TK-Vault", "TK platform services used across the solution (DB, workflow, notifications, auth/SSO, monitoring, secrets)."],
  ["BRL / TR / NFR / INT / FS / US / AS / OI", "Business rule / Technical req. / Non-functional req. / Integration req. / Functional spec / User story / Assumption / Open issue."],
  ["RET, APR, RFD, DSP, NTF, RPT, FRD, ADM, MIG", "Module codes: intake, approval, refund, disposition, notifications, reporting, fraud, admin, migration."],
  ["MoSCoW", "Prioritisation: Must / Should / Could / Won't (this time)."],
  ["RTO / RPO", "Recovery Time Objective / Recovery Point Objective (availability)."],
  ["p95", "95th percentile — the value below which 95% of measured cases fall."],
  ["Idempotent", "An operation that has the same effect whether run once or many times (no duplicate refunds)."],
  ["UAT", "User Acceptance Testing."],
  ["MA", "Maintenance &amp; Support agreement."],
 ], widths=["auto","auto"]) + """
<p class="small" style="margin-top:4mm">— End of document <span class="id">TK-BA-SMR-REQ-01</span> v1.0 —</p>
"""))

# =====================================================================
# ASSEMBLE
# =====================================================================
HTML = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>SiamMart Returns &ndash; Requirements Specification ({DOCID})</title>
<link href="https://fonts.googleapis.com/css2?family=Sarabun:wght@400;600;700&family=IBM+Plex+Mono&family=IBM+Plex+Sans:wght@400;600;700&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
{''.join(PAGES)}
</body>
</html>"""

OUT = "/Users/karitsookpreedee/Desktop/Huawei/codearts-agent/ba-task/.codeartsdoer/deliverables/smr/TK-BA-SMR-REQ-01.html"
with open(OUT, "w", encoding="utf-8") as f:
    f.write(HTML)
print("WROTE", OUT)
print("total pages:", len(PAGES))
