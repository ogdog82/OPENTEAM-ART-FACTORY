# Paste this whole text into OpenTeam's Orchestration Task field

OPENTEAM ART FACTORY — FOUR-TREE BINARY TRANSPORT PILOT

ARTIFACT_BRIDGE: ON

Repository: https://github.com/ogdog82/OPENTEAM-ART-FACTORY
Branch: main

Use existing six-node graph: PREPARER (execution) → GENERATOR (execution) → GENERATION REVIEW (reviewer EXTRACTOR) → EXTRACTOR (execution) → EXTRACTION REVIEW (reviewer UPLOADER) → UPLOADER (execution). Review FAIL routes to corresponding prior execution node. Max 2 failures per review, stop on exhaustion. Max 20 node executions. Finish after UPLOADER succeeds: DO NOT auto-advance to Batch 02.

PREPARER: Read `art/queue.json` and `art/STYLE.md` from GitHub. Batch 01's exact four assets are oak, ash, birch, maple, in listed 2x2 quadrant order. The four real placeholder PNGs already exist under `public/art/`. Create one short high-quality generator prompt and pass exact queue metadata to EXTRACTOR and UPLOADER.

GENERATOR: This is an ORIGINAL TEXT-TO-IMAGE creation, NOT an editing task. Use a new image-generation invocation and the short visual-only prompt in `art/prompts/batch-01-fresh-image.txt`, or PREPARER's equivalent image-only prompt. Do not open, attach, or supply the existing placeholder PNGs as input images. Existing files in GitHub are output destinations for UPLOADER, not inputs to GENERATOR. Never include GitHub, filenames, extraction, upload, or replacement instructions inside the image-rendering request. If the image tool wrongly asks for an image to edit, retry ONE time with the exact standalone prompt and no attachments. If the second attempt fails, stop with BLOCKED_GENERATION and the verbatim tool error; do not label it an art-quality or bridge failure. Once an image is produced, transfer its actual bytes to EXTRACTOR via the opt-in artifact bridge. Do not claim success with text only.

GENERATION REVIEW (EXTRACTOR): Open the actual generated source image. Require correct object count/identity, clean separation, pleasing silhouettes, coherent pixel art/perspective/palette and plausible extractability. PASS only when inspected; FAIL to GENERATOR with up to 3 visual corrections. If bytes are inaccessible, report BLOCKED_TRANSPORT rather than regenerating the image.

EXTRACTOR: Execute Python/Pillow on the actual image, review transparency removal and quality at native resolution, and export exactly four separate RGBA PNGs with names/sizes and ground anchors from `art/queue.json`. Show four separately named PNG images and deliver actual image files; not a ZIP-only or text-only handoff.

EXTRACTION REVIEW (UPLOADER): Open and inspect each actual PNG for source identity, dimensions, alpha, clean edges, silhouette, proportionality, exact anchor, and attractive pixel clusters at native scale. PASS only if real files can be inspected and quality is acceptable; FAIL back to EXTRACTOR with at most 3 exact fixes. Missing image bytes = BLOCKED_TRANSPORT.

UPLOADER: Replace the four existing Batch 01 placeholder PNGs at their exact `public/art/` paths, update Batch 01 and its four assets to `approved` in `art/queue.json`, commit as one logical batch, verify exact paths and report GitHub commit URL. Do not alter art specs/dimensions, unrelated files, or game code. STOP after the first confirmed commit.
