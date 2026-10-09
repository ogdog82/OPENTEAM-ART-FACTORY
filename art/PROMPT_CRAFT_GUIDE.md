# PREPARER prompt-crafting standard

PREPARER's primary responsibility is to create excellent, consistent, extraction-friendly image-generation prompts from art/queue.json and art/STYLE.md. The GENERATOR receives that artistic prompt plus OpenTeam's transport follow-up after image generation.

Read the current batch specifications and art style. Later approved sprites can serve as reference material; placeholders should not.

For each four-asset batch, create one self-contained prompt with:
- Four clearly different subjects in exactly their assigned top-left, top-right, bottom-left and bottom-right positions.
- Professional original fantasy pixel art with readable deliberate pixel clusters rather than filtered illustration.
- Unified perspective, lighting, palette, outlines and detail density.
- Full silhouettes, sufficient margins and empty cross-shaped extraction gutters.
- A simple removable background, preferably magenta #FF00FF; no accidental labels or overlaps.
- A request for ONE new source image with distinct subjects.

Prioritize visual quality and cohesion. Around 120–220 words is a useful starting point, not a rigid limit. Avoid excessive prohibitions. Technical canvas sizes and ground anchors are fetched separately from the queue by OpenTeam and sent to the EXTRACTOR. The PREPARER may use available tools and references; no generic prohibition on GitHub access applies to any agent.

Deliver the completed artistic prompt, ideally between GENERATION_PROMPT_BEGIN and GENERATION_PROMPT_END. The extension handles the separate follow-up asking GENERATOR to export that original image without a second image generation.
