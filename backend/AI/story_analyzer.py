"""LLM-based story analysis logic for EMO-AI."""

from dataclasses import dataclass
import json
from typing import Protocol

from AI.prompts import build_story_analysis_messages


@dataclass(frozen=True)
class GeneratedStoryAnalysis:
    """The structured result produced by the story analyzer."""

    main_character: str
    setting: str
    theme: str
    conflict: str
    story_arc: str
    target_audience: str


class StoryAnalysisError(Exception):
    """Raised when a story cannot be analyzed."""


class StoryAnalysisLLMProvider(Protocol):
    """Contract implemented by adapters for a concrete LLM provider."""

    def generate(self, *, system_prompt: str, user_prompt: str) -> str:
        """Return the provider's raw JSON response for an analysis request."""


class StoryAnalyzer:
    """Analyzes a generated story through an injected LLM provider."""

    def __init__(self, provider: StoryAnalysisLLMProvider | None = None) -> None:
        self._provider = provider

    def analyze(self, story: str) -> GeneratedStoryAnalysis:
        """Analyze and validate the supplied generated story."""
        if not story.strip():
            raise StoryAnalysisError("A story is required for analysis.")
        if self._provider is None:
            raise StoryAnalysisError("No story-analysis LLM provider is configured.")

        system_prompt, provider_prompt = build_story_analysis_messages(story)

        try:
            raw_response = self._provider.generate(
                system_prompt=system_prompt,
                user_prompt=provider_prompt,
            )
        except Exception as error:
            raise StoryAnalysisError("The story-analysis provider failed.") from error

        return self._parse_response(raw_response)

    @staticmethod
    def _parse_response(raw_response: str) -> GeneratedStoryAnalysis:
        """Validate the JSON contract returned by an LLM provider."""
        try:
            response = json.loads(raw_response)
        except (TypeError, json.JSONDecodeError) as error:
            raise StoryAnalysisError(
                "The story-analysis provider returned invalid JSON."
            ) from error

        if not isinstance(response, dict):
            raise StoryAnalysisError(
                "The story-analysis provider returned an invalid response shape."
            )

        required_fields = (
            "main_character",
            "setting",
            "theme",
            "conflict",
            "story_arc",
            "target_audience",
        )
        values: dict[str, str] = {}
        for field_name in required_fields:
            value = response.get(field_name)
            if not isinstance(value, str) or not value.strip():
                raise StoryAnalysisError(
                    f"The story-analysis provider returned an invalid {field_name}."
                )
            values[field_name] = value.strip()

        return GeneratedStoryAnalysis(**values)
