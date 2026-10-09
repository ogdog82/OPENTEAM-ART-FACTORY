# OpenTeam four-person art factory

Read `art/queue.json` and `art/STYLE.md` on each fresh OpenTeam chat's first task. Queue is the authoritative batch/asset register.

PREPARER: select the first pending batch (batch 01 only for pilot) and make one short high-quality 2x2 generation prompt. Pass batch ID, descriptions and technical requirements onward.

GENERATOR: invoke actual ChatGPT image generation. Transfer original image BYTES, not text, to EXTRACTOR; if unable, report BLOCKED_TRANSPORT.

EXTRACTOR: review real generated image quality; FAIL to GENERATOR for artistic errors. On PASS, execute Python/Pillow and produce four genuine transparent native-resolution PNGs at exact queue filenames and canvases. Transfer real files and preview to UPLOADER; if missing bytes report BLOCKED_TRANSPORT. Terrain requires seamless tiling tests.

UPLOADER: independently review actual four PNGs (not just claims) for identity, clean edges, alpha, art quality, exact dimensions, anchors, and tile repeatability. FAIL to EXTRACTOR if defective. On PASS replace the four existing placeholder paths, update batch and individual asset statuses in `art/queue.json`, commit one batch, and report GitHub commit URL.

Initial pilot only: DO NOT start next batch automatically. Keep retries to 2 per review gate. Preserve other games and older OpenTeam orchestrations; use this pipeline only with explicit `ARTIFACT_BRIDGE: ON` in the Art Factory orchestration task. Do not fill this repo with failed generated sources, redundant logs or checksum manifests.
