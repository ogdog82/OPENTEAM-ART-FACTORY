# Artifact bridge — actual bytes, multiple supported transports

The Art Factory is opt-in with ARTIFACT_BRIDGE: ON. PREPARER supplies the visual prompt; OpenTeam reads canonical batch specs from GitHub.

GENERATOR: OpenTeam captures the original rendered source image from the authenticated ChatGPT frame, including a restart-safe local checkpoint when download succeeds. OpenTeam still sends the second request in the SAME GENERATOR conversation to export the original (never regenerate it). A directly uploaded source.png at art/incoming/<prompt-id>/generated/ is another supported route; it is independently downloaded/verified before use.

EXTRACTOR: Output four individually rendered PNGs with the expected filenames for OpenTeam to capture, OR use connected GitHub access to upload their real PNG bytes under art/incoming/<run-id>/extracted/. The extension verifies the exact four files, PNG RGBA pixel format and canvas dimensions; a sandbox:/ path or text claim alone never substitutes for bytes.

Review agents download actual GitHub source/staging files and inspect pixels. Quality FAIL loops to the producer; unavailable bytes are BLOCKED_TRANSPORT, never an art quality judgment. After extraction PASS, OpenTeam promotes the files and approves the queue, and the UPLOADER audits actual commits. These agent transport choices are alternatives, not restrictions. Keep credentials private and do not copy binary attachments between ChatGPT conversations.

The extension is a browser integration: a complete live Chrome/ChatGPT/GitHub pipeline must be confirmed on the user's installed copy; isolated tests do not establish that.
