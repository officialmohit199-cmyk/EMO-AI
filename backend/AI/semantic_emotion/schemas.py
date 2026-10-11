"""Pydantic models for the Semantic Emotion Intelligence component."""

from pydantic import BaseModel, ConfigDict, Field, field_validator


class SemanticEmotionResult(BaseModel):
    """A validated semantic reading of the emotional meaning of a story."""

    model_config = ConfigDict(extra="forbid")

    primary_emotion: str = Field(
        min_length=1,
        description="The dominant emotion supported by the story.",
    )
    secondary_emotions: list[str] = Field(
        default_factory=list,
        description="Meaningful supporting emotions, ordered by relevance.",
    )
    intensity_score: float = Field(
        ge=0.0,
        le=1.0,
        description="Emotional intensity from 0.0 (minimal) to 1.0 (extreme).",
    )
    emotional_tone: str = Field(
        min_length=1,
        description="A concise description of the story's overall emotional tone.",
    )
    confidence: float = Field(
        ge=0.0,
        le=1.0,
        description="Confidence in the semantic interpretation from 0.0 to 1.0.",
    )

    @field_validator("primary_emotion", "emotional_tone")
    @classmethod
    def require_non_blank_text(cls, value: str) -> str:
        """Strip provider output and reject labels that contain only whitespace."""
        value = value.strip()
        if not value:
            raise ValueError("must not be blank")
        return value

    @field_validator("secondary_emotions")
    @classmethod
    def normalize_secondary_emotions(cls, values: list[str]) -> list[str]:
        """Keep only meaningful, non-blank secondary-emotion labels."""
        normalized_values = []
        for value in values:
            normalized_value = value.strip()
            if not normalized_value:
                raise ValueError("secondary emotions must not be blank")
            normalized_values.append(normalized_value)
        return normalized_values
