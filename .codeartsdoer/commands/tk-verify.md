---
description: Re-run verification only on existing TK deliverables — Senior BA, Senior SA and Document QA gates.
---

Re-verify the given TK deliverables (or the latest ones in
`.codeartsdoer/deliverables/<project>/`):

$ARGUMENTS

Launch the verifier roles with the `task` tool and report their verdicts:

1. `tk-senior-ba` on the requirements package `TK-BA-<PROJECT>-REQ-*.html`.
2. `tk-senior-sa` on the architecture pack `TK-SA-<PROJECT>-ARC-*.html`.
3. `tk-doc-qa` on both files together.

Summarise PASS/FAIL per gate and the consolidated fix list grouped by owner
(`tk-ba` / `tk-sa`). Do not rewrite the documents; report only. Do not claim a
gate passed unless the role ran it this session.