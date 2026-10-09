# OpenTeam Art Factory — GitHub artifact transport

The repository's 64 requests and exact required canvas/anchor/filename data live in art/queue.json. The OpenTeam extension stages generated and extracted images under art/incoming/<run-id>/ and promotes approved PNGs to public/art/. No AI-authored technical JSON or agent-to-agent binary upload is required.

PREPARER reads art/queue.json, art/STYLE.md and art/PROMPT_CRAFT_GUIDE.md, then crafts an excellent image-only 2×2 prompt with consistent palette, perspective, lighting, clean silhouettes and extraction-friendly gaps. No image generation or asset JSON.

GENERATOR uses ChatGPT image generation to make ONE new image from PREPARER's artistic prompt. It must not read/write GitHub or perform extraction. OpenTeam captures the generated image from its response and uploads it to GitHub staging.

EXTRACTOR reviews the staged source image after fetching actual pixels from its GitHub URL. Upon PASS, use Python/Pillow to create four exact-size, named, transparent PNGs, each independently displayed/attached in the chat (exact filename image alt). OpenTeam captures those outputs and stages them to GitHub. No queue changes or direct GitHub commits by EXTRACTOR.

UPLOADER reviews all four staged PNG files after fetching actual pixels. Quality FAIL returns to EXTRACTOR. After PASS, the extension performs final PNG publication and queue approval; UPLOADER verifies the committed results and reports URLs rather than uploading files again.

Six stages: PREPARER → GENERATOR → GENERATION REVIEW (EXTRACTOR) → EXTRACTOR → EXTRACTION REVIEW (UPLOADER) → UPLOADER. Two review attempts max, pilot Batch 01 only. Missing real image bytes = BLOCKED_TRANSPORT. Enable only via ARTIFACT_BRIDGE: ON plus OPENTEAM ART FACTORY; other workflows stay unchanged. No forced browser reloads, no cross-chat binary attachments, no credentials in prompts.