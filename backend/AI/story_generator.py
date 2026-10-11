"""LLM-based story generation logic for EMO-AI."""

from dataclasses import dataclass
import json
from typing import Protocol

from AI.prompts import build_story_messages


@dataclass(frozen=True)
class GeneratedStory:
    """The structured result produced by the story generator."""

    title: str
    story: str
    summary: str
    moral: str


class StoryGenerationError(Exception):
    """Raised when a story cannot be generated."""


class StoryLLMProvider(Protocol):
    """Contract implemented by adapters for a concrete LLM provider."""

    def generate(self, *, system_prompt: str, user_prompt: str) -> str:
        """Return the provider's raw JSON response for a story request."""


class StoryGenerator:
    """Generates structured stories through an injected LLM provider."""

    def __init__(self, provider: StoryLLMProvider | None = None) -> None:
        self._provider = provider

    def generate(self, user_prompt: str) -> GeneratedStory:
        """Generate and validate a story from the supplied user prompt."""
        if not user_prompt.strip():
            raise StoryGenerationError("A story prompt is required.")
        if self._provider is None:
            raise StoryGenerationError("No story-generation LLM provider is configured.")

        system_prompt, provider_prompt = build_story_messages(user_prompt)

        try:
            raw_response = self._provider.generate(
                system_prompt=system_prompt,
                user_prompt=provider_prompt,
            )
        except Exception as error:
            raise StoryGenerationError("The story-generation provider failed.") from error

        return self._parse_response(raw_response)

    @staticmethod
    def _parse_response(raw_response: str) -> GeneratedStory:
        """Validate the JSON contract returned by an LLM provider."""
        try:
            response = json.loads(raw_response)
        except (TypeError, json.JSONDecodeError) as error:
            raise StoryGenerationError(
                "The story-generation provider returned invalid JSON."
            ) from error

        if not isinstance(response, dict):
            raise StoryGenerationError(
                "The story-generation provider returned an invalid response shape."
            )

        required_fields = ("title", "story", "summary", "moral")
        values: dict[str, str] = {}
        for field_name in required_fields:
            value = response.get(field_name)
            if not isinstance(value, str) or not value.strip():
                raise StoryGenerationError(
                    f"The story-generation provider returned an invalid {field_name}."
                )
            values[field_name] = value.strip()

        return GeneratedStory(**values)
