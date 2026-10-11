"""Prompt definitions for the LLM-based Story Generator module."""

STORY_SYSTEM_PROMPT = """
You are EMO-AI's Story Generator. Write original, emotionally engaging short
stories that remain faithful to the user's story prompt. Give each story a
clear beginning, meaningful challenge, emotional resolution, and an authentic
moral. Keep the content suitable for a general audience.
""".strip()

STORY_GENERATION_PROMPT_TEMPLATE = """
Create a short story based directly on the following user prompt:

<user_prompt>
{user_prompt}
</user_prompt>

Return only a valid JSON object with exactly these string fields:
{{
  "title": "A concise, fitting title",
  "story": "The complete short story",
  "summary": "A concise summary of the story",
  "moral": "The story's moral or lesson"
}}

Do not wrap the JSON in Markdown or include commentary outside the JSON object.
""".strip()


def build_story_messages(user_prompt: str) -> tuple[str, str]:
    """Build the system and user messages for a story-generation provider."""
    return STORY_SYSTEM_PROMPT, STORY_GENERATION_PROMPT_TEMPLATE.format(
        user_prompt=user_prompt
    )


STORY_ANALYSIS_SYSTEM_PROMPT = """
You are EMO-AI's Story Analyzer. Analyze only the supplied story and infer its
core narrative elements faithfully. Do not invent facts that are not supported
by the story. Keep each analysis field concise, clear, and suitable for a
general audience.
""".strip()

STORY_ANALYSIS_PROMPT_TEMPLATE = """
Analyze the following generated story:

<story>
{story}
</story>

Return only a valid JSON object with exactly these string fields:
{{
  "main_character": "The primary character or protagonist",
  "setting": "The story's primary time and place",
  "theme": "The central idea or message",
  "conflict": "The primary challenge or tension",
  "story_arc": "A concise beginning, middle, and resolution overview",
  "target_audience": "The most suitable audience"
}}

Do not wrap the JSON in Markdown or include commentary outside the JSON object.
""".strip()


def build_story_analysis_messages(story: str) -> tuple[str, str]:
    """Build the system and user messages for a story-analysis provider."""
    return STORY_ANALYSIS_SYSTEM_PROMPT, STORY_ANALYSIS_PROMPT_TEMPLATE.format(
        story=story
    )
