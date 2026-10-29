---
name: tk-process-modelling
description: TK method for modelling business workflows As-Is and redesigning them To-Be — swimlanes, pain-point and improvement markers, waste/control/visibility analysis, comparison table and status model. Use when mapping a current process or proposing an improved one.
---

# TK Process Modelling (As-Is → To-Be)

1. **As-Is** – draw the current process exactly as it happens today (LINE groups, paper, Excel, manual re-keying). Do not "clean it up".
   - **Swimlanes** per actor (Customer, Store Staff, CS HQ, Finance, Warehouse/DC, Systems).
   - Mark every **pain point** with a red numbered marker (P1, P2…) and list them under the diagram with impact (time, cost, error, risk).
   - Show measured/stated lead time per step where known.
2. **Analyse** – classify each pain point:
   - *Waste* – waiting, re-keying, handoffs
   - *Control gap* – no audit, fraud exposure
   - *Visibility gap* – no tracking, no status for customer
3. **To-Be** – redesign:
   - Eliminate manual handoffs and re-keying.
   - Automate rule-based decisions (TK-Flow DMN); keep humans for exceptions.
   - Add customer self-service and proactive notification.
   - Mark each improvement with a green marker (I1, I2…) mapped to the pain point it fixes.
4. **Compare**

   | Measure | As-Is | To-Be | Change |
   |---|---|---|---|
   | Steps | | | |
   | Handoffs | | | |
   | Lead time | | | |
   | Manual touches | | | |
   | Systems touched | | | |

5. **Status model** – state diagram of the main business object (e.g. Return Request), every status and allowed transition.

## Pain point → improvement map

| P# | Pain point | Type | Impact | Fixed by I# | Component |
|---|---|---|---|---|---|

Every P# must map to an I# or be explicitly accepted with a reason.
