# OPENTEAM ART FACTORY

Independent four-agent production pilot for **64 reusable pixel-RPG assets**, specified in [art/queue.json](art/queue.json) (16 batches of 4).

**STRICT role separation:** PREPARER reads the queue and creates prompts → GENERATOR only generates a new image from the supplied prompt → EXTRACTOR only judges generated art and processes source pixels to four PNGs → UPLOADER only reviews extracted PNGs and commits approved files to GitHub.

- [Asset queue](art/queue.json) — 64 requests, with Batch 01 pending.
- [Art style](art/STYLE.md) — read by PREPARER, not GENERATOR.
- [Agent boundaries](AGENTS.md) — distinct file-access and handoff responsibilities.
- [OpenTeam orchestration task](docs/ORCHESTRATION_TASK.md) — controller and node duties.
- [Project instructions](docs/CHATGPT_PROJECT_INSTRUCTIONS.md) — role-isolating shared ChatGPT Project instructions.
- [Transport contract](docs/TRANSPORT.md) — verified binary handoff requirement.
- [Placeholder creation tool](tools/make_placeholders.py) — optional creation of missing future placeholders.

Four actual placeholder PNGs already exist in `public/art/` for Batch 01 (oak, ash, birch, maple). The remaining 60 requests are planned and not ready for production. The pilot ends after these four replacements are committed successfully. No other game repository or orchestrator configuration is touched.
