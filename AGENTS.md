# OpenTeam art factory — strict separation of duties

This repository holds a 64-asset queue. It is NOT a shared to-do list that every participant must read. The OpenTeam orchestrator supplies each person only what their role requires.

## Role boundaries

### PREPARER — requirements and prompt ONLY
- The sole GitHub **reader** during asset preparation. Read `art/queue.json` and `art/STYLE.md`; choose the next pending four-asset batch.
- Prepare two separate handoffs: (A) **GENERATION_PROMPT**, a complete standalone image-only prompt containing only appearance, composition, and style; (B) **BATCH_SPEC**, structured asset IDs, quadrant order, dimensions, anchors, destination filenames, and applicable extraction constraints for EXTRACTOR and UPLOADER.
- Send GENERATOR only GENERATION_PROMPT. Route BATCH_SPEC as task metadata to EXTRACTOR/UPLOADER through OpenTeam. Never ask GENERATOR to open a repository file, access placeholder PNGs, or interpret the queue.
- PREPARER does not generate or extract images, review quality, or commit GitHub changes.

### GENERATOR — image generation ONLY
- Receive the fully formed GENERATION_PROMPT directly from PREPARER in the current message.
- Generate **one NEW image from text** using ChatGPT's image generation; the four assets must be in the prompt's specified positions.
- Hand off the actual original image to EXTRACTOR (or its review node) using the opt-in binary bridge.
- On art-quality FAIL, use the review feedback to regenerate. On a mode/tool error, report BLOCKED_GENERATION with the exact error rather than guessing its cause.
- **Never read or write GitHub. Never fetch a prompt from a file. Never inspect placeholder PNGs, specifications, paths, sizes, anchors, source code, or queue state. Never extract PNGs or publish them.**
- If a source image is missing, report BLOCKED_GENERATION; if produced but not transferable, report BLOCKED_TRANSPORT.

### EXTRACTOR — source review and pixel processing ONLY
- Receive generated **image bytes** plus BATCH_SPEC from the orchestration handoff. Do not fetch asset requirements from GitHub; if BATCH_SPEC is missing report BLOCKED_SPEC_HANDOFF.
- Judge generation quality and return artistic failures to GENERATOR. On PASS use Python/Pillow to create four exact-size, correctly named transparent PNGs preserving the generated art. Inspect quality and transfer actual files to UPLOADER.
- Never generate substitute art or commit to GitHub. No queue/status edits. Failure to receive bytes = BLOCKED_TRANSPORT.

### UPLOADER — final quality and Git publication ONLY
- Receive four actual final PNGs and BATCH_SPEC. Independently inspect art quality, dimensions, alpha, anchor, filenames; return conversion failures to EXTRACTOR.
- Only after review PASS, read GitHub to check the current exact paths/specs and commit accepted final PNG replacements. Update `art/queue.json` status, and verify publication.
- Never generate images, modify extraction output, or prepare prompts.

## Orchestration

PREPARER → GENERATOR → GENERATION REVIEW (EXTRACTOR) → EXTRACTOR → EXTRACTION REVIEW (UPLOADER) → UPLOADER.

Review FAIL returns to its immediately preceding worker. Two review attempts max; stop on exhausted budget. Batch 01 only until binary transfer and publication both pass. Activate binary forwarding only when `ARTIFACT_BRIDGE: ON` is in this factory task, never in the separate Lantern Vale group.

A file path, download link inaccessible to the recipient, or claim of success is NOT a binary transfer. Avoid costly integrity ceremony; judge actual functioning and visual quality.
