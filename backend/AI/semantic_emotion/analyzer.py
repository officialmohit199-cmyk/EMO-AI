"""Provider-independent semantic emotion analysis."""

import json
from typing import Protocol

from pydantic import ValidationError

from .prompts import build_semantic_emotion_messages
from .schemas import SemanticEmotionResult


class SemanticEmotionAnalysisError(Exception):
    """Raised when semantic emotion analysis cannot produce a valid result."""


class SemanticEmotionProviderError(Exception):
    """Raised by a provider adapter when its known LLM/API operation fails.

    Provider adapters should translate only their provider-specific operational
    failures into this exception. This lets the analyzer hide API details while
    leaving unrelated programming errors visible during development.
    """


class SemanticEmotionLLMProvider(Protocol):
    """Contract that a concrete LLM provider adapter must implement."""

    def generate(self, *, system_prompt: str, user_prompt: str) -> str:
        """Return a raw JSON response for a semantic emotion request."""


class SemanticEmotionAnalyzer:
    """Analyze stories through an injected provider without choosing an LLM."""

    def __init__(self, provider: SemanticEmotionLLMProvider | None = None) -> None:
        self._provider = provider

    @property
    def has_provider(self) -> bool:
        """Whether this analyzer can process non-empty stories."""
        return self._provider is not None

    def analyze(self, story: str) -> SemanticEmotionResult:
        """Return a validated semantic emotion result for ``story``.

        Empty input has a deterministic neutral result. A non-empty story
        requires an injected provider because this experimental module never
        fabricates semantic analysis from keywords or fallback heuristics.
        """
        if not isinstance(story, str):
            raise TypeError("story must be a string")

        cleaned_story = story.strip()
        if not cleaned_story:
            return SemanticEmotionResult(
                primary_emotion="Neutral",
                secondary_emotions=[],
                intensity_score=0.0,
                emotional_tone="neutral",
                confidence=1.0,
            )

        if self._provider is None:
            raise SemanticEmotionAnalysisError(
                "No Semantic Emotion Intelligence provider is configured."
            )

        system_prompt, user_prompt = build_semantic_emotion_messages(cleaned_story)

        try:
            raw_response = self._provider.generate(
                system_prompt=system_prompt,
                user_prompt=user_prompt,
            )
        except SemanticEmotionProviderError as error:
            raise SemanticEmotionAnalysisError(
                "The semantic emotion provider could not analyze the story."
            ) from error

        return self._parse_response(raw_response)

    @staticmethod
    def _parse_response(raw_response: str) -> SemanticEmotionResult:
        """Parse and validate the JSON contract returned by a provider."""
        try:
            response = json.loads(raw_response)
        except (TypeError, json.JSONDecodeError) as error:
            raise SemanticEmotionAnalysisError(
                "The semantic emotion provider returned invalid JSON."
            ) from error

        if not isinstance(response, dict):
            raise SemanticEmotionAnalysisError(
                "The semantic emotion provider returned an invalid response shape."
            )

        try:
            return SemanticEmotionResult.model_validate(response)
        except ValidationError as error:
            raise SemanticEmotionAnalysisError(
                "The semantic emotion provider returned an invalid result."
            ) from error


def analyze_emotion(
    story: str,
    provider: SemanticEmotionLLMProvider | None = None,
) -> SemanticEmotionResult:
    """Convenience interface for future consumers of semantic emotion data."""
    return SemanticEmotionAnalyzer(provider=provider).analyze(story)
