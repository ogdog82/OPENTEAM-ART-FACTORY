OPENTEAM ART FACTORY — GITHUB HANDOFF PILOT
ARTIFACT_BRIDGE: ON
Repository: https://github.com/ogdog82/OPENTEAM-ART-FACTORY
Branch: main
Batch: batch-01-broadleaf-trees

Preserve the configured six-node graph: PREPARER → GENERATOR → GENERATION REVIEW (EXTRACTOR) → EXTRACTOR → EXTRACTION REVIEW (UPLOADER) → UPLOADER. Generation quality FAIL → GENERATOR; extraction quality FAIL → EXTRACTOR. Two quality-review attempts maximum per gate. Pilot Batch 01 only.

PREPARER: Read art/queue.json, art/STYLE.md and art/PROMPT_CRAFT_GUIDE.md; create a polished, standalone 2×2 image-generation prompt. The extension retrieves the canonical canvas, filenames and anchor specifications directly from GitHub.

GENERATOR: Create ONE new image using ChatGPT image generation. OpenTeam sends a SECOND message in this same chat asking you to export the EXISTING image as source.png, not generate another image. You are free to use connected tools to upload real source pixels under art/incoming/<prompt-id>/generated/source.png and return the verified GitHub URL, or return an attached source.png. OpenTeam also attempts to capture the original rendered image bytes itself. Do not claim upload success without real bytes.

GENERATION REVIEW (EXTRACTOR): Inspect the actual staged GitHub source image and return real PASS/FAIL using the required review schema. If pixels cannot be opened, report BLOCKED_TRANSPORT; this is not an artistic failure.

EXTRACTOR: Use the approved source pixels and Python/Pillow to create four distinct RGBA PNGs that obey the four filenames, canvases and anchors. Return four individually displayed PNGs that OpenTeam can capture, OR upload all four real files under art/incoming/<run-id>/extracted/<exact-filename> with available GitHub tools and return their verified URLs. OpenTeam independently checks every file's bytes, names, dimensions and transparency. ZIP-only and prose-only claims are not sufficient.

EXTRACTION REVIEW (UPLOADER): Inspect the actual four staged PNG files from GitHub and return a genuine review decision. Artistic FAIL → EXTRACTOR; missing bytes → BLOCKED_TRANSPORT.

FINAL UPLOADER: After a PASS, OpenTeam promotes the verified PNGs to public/art/ and updates art/queue.json. Use your available tools to audit those actual commits and report the file links and any genuine discrepancies.

Use available agent tools as needed. No agent is prohibited from GitHub access or independent validation. Do not disclose tokens, pretend files exist, regenerate merely to repair a transport error, refresh ChatGPT windows, or move binary files between agent chats. Other OpenTeam workflows are unchanged.
