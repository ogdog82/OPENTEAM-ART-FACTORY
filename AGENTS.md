# OpenTeam Art Factory — agent cooperation and file transport

The canonical 64-asset queue, exact output paths, canvases and anchors are in art/queue.json. The four workers remain PREPARER, GENERATOR, EXTRACTOR and UPLOADER, with EXTRACTOR and UPLOADER also serving as review agents. Work on pilot Batch 01 only until approved.

Agents may use their available tools, including GitHub and Python, to perform their assigned stage. There are no arbitrary tool prohibitions or exclusive communication modes. Real file bytes and genuine review decisions, not a claimed attachment or URL, determine whether the orchestration advances.

PREPARER: Read queue/style/prompt guide and craft a cohesive original 2×2 pixel-art prompt. The extension fetches technical specifications from the real GitHub queue.

GENERATOR: Create one new original image. On OpenTeam's subsequent message in the SAME chat, export that existing image as source.png without regenerating. The extension separately attempts to checkpoint original image pixels in the authenticated Chrome frame. If GitHub access is available, the agent may upload the actual PNG to art/incoming/<prompt-id>/generated/source.png and return its verified URL; an actual PNG attachment is also acceptable. A sandbox link alone is not proof of accessible image data.

EXTRACTOR: As generation reviewer, open the current GitHub source pixels before PASS/FAIL. As production agent, use real source pixels and Python/Pillow to make four distinct transparent PNGs meeting the queue's contracts. The four images may be captured from individually rendered PNGs, or uploaded by the agent to art/incoming/<run-id>/extracted/<filename>; OpenTeam verifies real GitHub bytes and dimensions either way.

UPLOADER: As extraction reviewer, inspect all four actual GitHub PNGs before PASS. After PASS, OpenTeam publishes the accepted files to public/art and approves the queue; the UPLOADER audits the final results and may report actionable discrepancies.

Six stages: PREPARER → GENERATOR → GENERATION REVIEW (EXTRACTOR) → EXTRACTOR → EXTRACTION REVIEW (UPLOADER) → UPLOADER. Artistic FAIL returns to the producing stage with at most two quality-review attempts per gate. Missing files/bytes = BLOCKED_TRANSPORT and must not be counted as a creative failure. Keep tokens private. The extension must not transfer binary blobs directly between agent conversations or disturb other OpenTeam workflows.
