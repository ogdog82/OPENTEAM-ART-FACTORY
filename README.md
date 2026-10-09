# OPENTEAM ART FACTORY

Four-agent pixel-art production pilot for **64 reusable pixel-RPG assets**, specified in [art/queue.json](art/queue.json) (16 batches of four). Batch 01 is the current pilot.

The six stages are PREPARER → GENERATOR → GENERATION REVIEW (EXTRACTOR) → EXTRACTOR → EXTRACTION REVIEW (UPLOADER) → UPLOADER. PREPARER designs the visual prompt; GENERATOR produces an original source image; EXTRACTOR reviews that source and creates four transparent sprites; UPLOADER reviews and audits the publication. Agents can use available tools, including GitHub, rather than being arbitrarily locked into a single file-transport method.

- [Asset queue](art/queue.json) — required filenames, dimensions and anchors; authority for approvals.
- [Art style](art/STYLE.md) and [prompt guide](art/PROMPT_CRAFT_GUIDE.md) — art direction.
- [Agent collaboration](AGENTS.md) — responsibilities and verified image transport choices.
- [OpenTeam orchestration task](docs/ORCHESTRATION_TASK.md) — active six-node pipeline.
- [ChatGPT Project instructions](docs/CHATGPT_PROJECT_INSTRUCTIONS.md) — project-wide workflow.
- [Transport contract](docs/TRANSPORT.md) — original pixels through local capture or verified GitHub uploads.

Real generated and extracted files are staged under art/incoming/<run-id>/, then approved sprites are promoted to public/art only after extraction review PASS. Four placeholder PNGs are already present for Batch 01. No other project or OpenTeam workflow needs to change.
