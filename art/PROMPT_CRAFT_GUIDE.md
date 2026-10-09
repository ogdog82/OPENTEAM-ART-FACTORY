# PREPARER prompt-crafting standard

Only PREPARER uses this document. GENERATOR receives the completed image prompt directly from PREPARER, never a GitHub path or technical instructions.

PREPARER's primary responsibility is to create excellent, consistent, extraction-friendly image-generation prompts from GitHub's asset descriptions and art-style rules.

Read art/queue.json and art/STYLE.md. For future batches, examine approved art references when they exist (not placeholders). Extract shared visual traits: elevated three-quarter viewpoint, lighting, outlines, restrained palette, material shading, cluster size, and level of detail.

For each four-asset batch, write one self-contained concise image prompt with:
- The four exact subjects in top-left, top-right, bottom-left and bottom-right positions, each visibly different.
- One unified original, professional pixel-art style with deliberate chunky pixel clusters readable at game scale. Avoid high-resolution illustrations with a pixel filter or dense individual-leaf noise.
- Consistent perspective, lighting, color family, outlining and detail density.
- Complete individual silhouettes, large empty margins and an obvious empty cross-shaped gutter; no overlaps or cropping.
- One easy-to-remove flat background (for the pilot, solid magenta #FF00FF); no scenery, shadows on the ground, grid, labels or UI.
- An explicit request for one NEW image, not edits to existing placeholder artwork.

Prioritize artistic quality and style cohesion first, then extraction suitability. Keep prompts focused, ideally 120–220 words; avoid piles of prohibitions. Do not put pixel dimensions, anchor coordinates, GitHub paths, filenames, Python methods, upload instructions, or extraction tasks in the image prompt. Exact technical requirements belong in a separate BATCH_SPEC to EXTRACTOR and UPLOADER.

Before passing GENERATION_PROMPT, PREPARER must check subject identity/order, consistent art direction, simple background, isolation, small-game readability, and that the prompt is complete by itself.

Deliver GENERATION_PROMPT to GENERATOR verbatim. Send BATCH_SPEC via the separate orchestrator handoff, never inside the generator's prompt.

GENERATOR ONLY creates the requested image and passes the original image bytes to EXTRACTOR, or reports the exact generation/transport error. It does not read GitHub, construct prompts, extract PNGs, review art, or upload.
