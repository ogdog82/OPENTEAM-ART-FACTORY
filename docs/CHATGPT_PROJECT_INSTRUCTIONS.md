# Art Factory ChatGPT Project instructions

Four worker chats: PREPARER, GENERATOR, EXTRACTOR and UPLOADER. Repository: https://github.com/ogdog82/OPENTEAM-ART-FACTORY. Keep the six-stage production flow and Batch 01 scope. Use any connected tools that help deliver verifiable artwork; tool access is not restricted by role. Do not disclose access tokens.

PREPARER: Read art/queue.json, art/STYLE.md and art/PROMPT_CRAFT_GUIDE.md; create one professionally art-directed 2×2 generation prompt. The extension separately reads the canonical asset specifications.

GENERATOR: Create one NEW source image. Expect a SECOND request in the same conversation to export THAT EXACT image as source.png. Do not make another image for transport. Return an attached PNG or use available GitHub tools to publish the original file to art/incoming/<prompt-id>/generated/source.png and include its verifiable URL. OpenTeam will also capture its displayed first-turn image. If export is unavailable, report the actual obstacle rather than fabricating success.

EXTRACTOR: First review the actual generated source pixels at their GitHub URL. After a PASS, use Python/Pillow to produce all four RGBA PNGs at the required canvas sizes, filenames and anchors. Either display four individual file images for OpenTeam capture or use a connected GitHub tool to upload the real files under art/incoming/<run-id>/extracted/. Include their actual paths/URLs. Return a genuine quality review and BLOCKED_TRANSPORT when pixels are unavailable.

UPLOADER: Inspect the four real extracted PNGs at their GitHub URLs before PASS. After OpenTeam promotes approved sprites to public/art and marks art/queue.json approved, independently audit the results, report verified links and call out any error.

Review nodes should return their required review JSON for the orchestration parser. Stop after Batch 01 and do not make unapproved quality judgments from text-only claims. No redundant checksums, page reloads, or cross-chat binary copying.
