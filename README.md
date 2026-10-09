# OPENTEAM ART FACTORY

A standalone four-agent production pilot for **64 reusable pixel-RPG assets**, specified in [art/queue.json](art/queue.json) (16 batches of 4).

**Roles:** PREPARER → GENERATOR → GENERATION REVIEW by EXTRACTOR → EXTRACTOR → EXTRACTION REVIEW by UPLOADER → UPLOADER.

## Start here

- [Batch and asset queue](art/queue.json) — 64 detailed requests, exact PNG paths/dimensions/anchors. **Batch 01 is pending.**
- [Pixel-art style](art/STYLE.md) — consistent production requirements.
- [Orchestration task](docs/ORCHESTRATION_TASK.md) — paste into OpenTeam's task field.
- [Project instructions](docs/CHATGPT_PROJECT_INSTRUCTIONS.md) — paste into the ChatGPT Art Factory Project.
- [Artifact handoff guide](docs/TRANSPORT.md) — required real image transfers.
- [Placeholder generator](tools/make_placeholders.py) — generates missing placeholders for future batches.

**Four real placeholder PNGs are committed under `public/art/` for the first batch** (oak, ash, birch and maple). The next 60 requests are planned, and their placeholders can be seeded only when ready. First pilot must stop after Batch 01 is committed. No other game repository is used.
