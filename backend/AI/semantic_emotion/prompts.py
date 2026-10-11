"""Prompt definitions for semantic emotion analysis."""

SEMANTIC_EMOTION_SYSTEM_PROMPT = """
You are EMO-AI's Semantic Emotion Intelligence layer. Analyze the emotional
meaning of the supplied story, not the frequency of emotion-related words.
Use context, subtext, imagery, narrative progression, and psychological state
to identify emotions. Consider the overall narrative before deciding which
emotion is dominant.

Only identify emotions that are supported by the story. Secondary emotions are
optional and should be included only when they add meaningful context. Do not
invent emotions or treat a single isolated word as decisive evidence.
""".strip()

SEMANTIC_EMOTION_PROMPT_TEMPLATE = """
Analyze the following story:

<story>
{story}
</story>

Return only one valid JSON object with exactly these fields:
{{
  "primary_emotion": "Dominant contextual emotion",
  "secondary_emotions": ["Meaningful supporting emotion"],
  "intensity_score": 0.0,
  "emotional_tone": "Concise description of the overall tone",
  "confidence": 0.0
}}

Both intensity_score and confidence must be numbers from 0.0 to 1.0.
Use an empty secondary_emotions list when no secondary emotion is meaningful.
Do not wrap the JSON in Markdown or include commentary outside the JSON object.
""".strip()


def build_semantic_emotion_messages(story: str) -> tuple[str, str]:
    """Build the provider-neutral prompts for a semantic emotion request."""
    return SEMANTIC_EMOTION_SYSTEM_PROMPT, SEMANTIC_EMOTION_PROMPT_TEMPLATE.format(
        story=story
    )
