# OPENTEAM ART FACTORY — single-batch role-isolation and artifact-transfer pilot
# Paste the body below into OpenTeam's Orchestration Task field.

ARTIFACT_BRIDGE: ON

Repository: https://github.com/ogdog82/OPENTEAM-ART-FACTORY
Branch: main
Batch: batch-01-broadleaf-trees
Stop after Batch 01 completes; do not run the other 15 batches.

Six-node graph using four people:
PREPARER (execution) → GENERATOR (execution) → GENERATION REVIEW (EXTRACTOR) → EXTRACTOR (execution) → EXTRACTION REVIEW (UPLOADER) → UPLOADER (execution).
Generation review FAIL → GENERATOR; extraction review FAIL → EXTRACTOR. Max 2 review attempts per gate; stop on exhaustion. Max 20 node executions.

ROLE ISOLATION IS NON-NEGOTIABLE. Each worker receives only its input and may perform only its assigned job. Do not tell all four chats to read GitHub.

1. PREPARER: **Only PREPARER reads** `art/queue.json`, `art/STYLE.md`, and `art/PROMPT_CRAFT_GUIDE.md` to choose Batch 01's four assets. PREPARER is accountable for art-directing the prompt: use GitHub's exact asset identity and style rules, maintain strong cross-batch visual consistency, and specify clean separable silhouettes/background without burying the image model in irrelevant technical details. Critically assess the prompt before handoff. Produce exactly two distinct outputs:
   - GENERATION_PROMPT: one fully self-contained short, artistic prompt requesting a NEW 2x2 image containing oak (top-left), ash (top-right), birch (bottom-left), maple (bottom-right), with cohesive professional pixel-art style, clearly separated silhouettes and an extraction-friendly background. Do not mention GitHub, placeholders, filenames, dimensions, anchors, extraction, editing, uploading, or workflow in the image prompt. Send the exact prompt text directly to GENERATOR—never a GitHub link or filename.
   - BATCH_SPEC: the four exact asset IDs, requested paths, canvas dimensions, anchor coordinates, quadrant order, and extraction constraints from the queue. Send this separately to EXTRACTOR and UPLOADER through the orchestrator's task context/handoff. If the orchestrator cannot deliver it to those nodes, stop and report BLOCKED_SPEC_HANDOFF. Do not leak technical spec or repository tasks into GENERATOR's message.

2. GENERATOR: Receive PREPARER's final GENERATION_PROMPT verbatim; do not improve, research, or rewrite it. Operate only on that prompt. Create a **brand-new image from text** using native ChatGPT image generation. Do not retrieve anything from GitHub, inspect placeholders, follow GitHub links, or do any extraction/upload. Transfer actual image bytes to EXTRACTOR/generation review. If the tool refuses creation, report BLOCKED_GENERATION with its real error; do not invent an explanation. If image bytes cannot be transferred, report BLOCKED_TRANSPORT. Quality feedback from EXTRACTOR returns here for regeneration.

3. GENERATION REVIEW (EXTRACTOR): Open the actual generated image and read BATCH_SPEC from PREPARER handoff. Inspect four subjects, matching quadrants, strong art, consistent pixel style, silhouettes, spacing, suitability for reduction. PASS to EXTRACTOR only if source is genuinely acceptable; art-quality FAIL returns to GENERATOR with at most 3 corrections. If image bytes or BATCH_SPEC are inaccessible, stop with BLOCKED_TRANSPORT or BLOCKED_SPEC_HANDOFF instead of pretending to review.

4. EXTRACTOR: With actual image and BATCH_SPEC, execute Python/Pillow to produce four separately named transparent PNGs of the exact requested canvas sizes and ground anchors. Preserve the accepted artwork and visually inspect the native-sized sprites. Hand the actual four PNG files to UPLOADER/extraction review. Do not access GitHub or alter any queue. Missing bytes = BLOCKED_TRANSPORT.

5. EXTRACTION REVIEW (UPLOADER): Open all four actual PNG files and check identity, exact filenames, dimensions, real alpha, clean edges, good aesthetics, proportionality and anchors. PASS only with inspectable pixels; otherwise FAIL back to EXTRACTOR with at most 3 repair instructions. File transfer issues = BLOCKED_TRANSPORT.

6. UPLOADER: Only after PASS, read GitHub to verify Batch 01 destination paths and specs, then replace exactly the four placeholder PNGs, update statuses to approved in `art/queue.json`, commit and verify the resulting paths. Report real commit URL. Do not create/edit art or modify gameplay. STOP.

Important: GitHub URL and path in THIS controller task are for PREPARER and UPLOADER only. The orchestrator MUST NOT copy these controller instructions wholesale into GENERATOR's image-generation prompt.
