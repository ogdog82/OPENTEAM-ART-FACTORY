# OpenTeam four-person art factory

Read `art/queue.json` and `art/STYLE.md` on each fresh OpenTeam chat's first task. Queue is the authoritative batch/asset register.

PREPARER: select the first pending batch (batch 01 only for pilot) and make one short high-quality 2x2 generation prompt. Pass batch ID, descriptions and technical requirements onward.

GENERATOR: request a **brand-new text-to-image creation**. Do not supply, open, or attach any existing placeholder PNG, old asset sheet, or repository artwork as a source image during Batch 01. Use a self-contained visual-only prompt; do not frame the request as an image edit, replacement, reference-based transformation, or crop. For a mode-classification tool error, retry once using `art/prompts/batch-01-fresh-image.txt` verbatim in a clean generator turn, with no prior image attached. If the same error recurs, report BLOCKED_GENERATION (not BLOCKED_TRANSPORT) with the actual error. Upon success, transfer original image BYTES to EXTRACTOR; if transfer fails report BLOCKED_TRANSPORT.

EXTRACTOR: review real generated image quality; FAIL to GENERATOR for artistic errors. On PASS, execute Python/Pillow and produce four genuine transparent native-resolution PNGs at exact queue filenames and canvases. Transfer real files and preview to UPLOADER; if missing bytes report BLOCKED_TRANSPORT. Terrain requires seamless tiling tests.

UPLOADER: independently review actual four PNGs (not just claims) for identity, clean edges, alpha, art quality, exact dimensions, anchors, and tile repeatability. FAIL to EXTRACTOR if defective. On PASS replace the four existing placeholder paths, update batch and individual asset statuses in `art/queue.json`, commit one batch, and report GitHub commit URL.

Initial pilot only: DO NOT start next batch automatically. Keep retries to 2 per review gate. Preserve other games and older OpenTeam orchestrations; use this pipeline only with explicit `ARTIFACT_BRIDGE: ON` in the Art Factory orchestration task. Do not fill this repo with failed generated sources, redundant logs or checksum manifests.
