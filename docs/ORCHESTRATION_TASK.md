OPENTEAM ART FACTORY — GITHUB HANDOFF PILOT
ARTIFACT_BRIDGE: ON
Repository: https://github.com/ogdog82/OPENTEAM-ART-FACTORY
Branch: main
Batch: batch-01-broadleaf-trees

Preserve the six-node graph: PREPARER → GENERATOR → GENERATION REVIEW (EXTRACTOR) → EXTRACTOR → EXTRACTION REVIEW (UPLOADER) → UPLOADER. Generation quality FAIL returns to GENERATOR; extraction quality FAIL returns to EXTRACTOR. Max two review attempts per gate. Run only Batch 01.

PREPARER reads art/queue.json, art/STYLE.md and art/PROMPT_CRAFT_GUIDE.md; crafts one complete, highly polished image-only 2×2 generation prompt. No technical JSON is needed; OpenTeam reads specifications directly from GitHub.

GENERATOR receives the finished visual prompt, creates ONE new image using native ChatGPT image generation, and then MUST add a separate plain-text line after the image: IMAGE_READY. Do not draw IMAGE_READY inside the image or say it before the image exists. OpenTeam independently captures the actual image bytes and stages them under art/incoming/RUN_ID/generated/; if the response is image-only, OpenTeam may add an acknowledgment after successful capture. GENERATOR does not read/write GitHub or upload files.

GENERATION REVIEW (EXTRACTOR) downloads and visually inspects the exact GitHub source image, returning real PASS/FAIL. If it cannot open the image, report BLOCKED_TRANSPORT.

EXTRACTOR downloads the approved source from its GitHub URL; uses Python/Pillow to produce four separately named transparent PNGs with exact canvas/anchor specifications. Display/attach all four individual PNGs in the reply with matching filename alt text so OpenTeam can capture them. ZIP-only/text-only outputs are not sufficient; EXTRACTOR must not commit files.

EXTRACTION REVIEW (UPLOADER) downloads and inspects the four staged PNGs under art/incoming/RUN_ID/extracted/. Real conversion-quality FAIL returns to EXTRACTOR. Missing bytes are BLOCKED_TRANSPORT, not artistic failure.

After extraction review PASS, OpenTeam uploads four validated PNGs to public/art/ and updates art/queue.json to approved. UPLOADER's final node audits actual file/commit URLs and reports results; no duplicate upload is needed.

Do not refresh agent chat windows, resend prompts, or transfer binary files between agent conversations. No other OpenTeam workflow is modified.
