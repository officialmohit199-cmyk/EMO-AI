"""Pydantic schemas for story generation."""

from pydantic import BaseModel, Field, field_validator


class StoryGenerateRequest(BaseModel):
    """Input accepted by the story generation endpoint."""

    prompt: str = Field(
        ...,
        min_length=3,
        max_length=2_000,
        description="A prompt describing the story to generate.",
    )

    @field_validator("prompt")
    @classmethod
    def validate_prompt(cls, value: str) -> str:
        cleaned_value = " ".join(value.split())
        if not cleaned_value:
            raise ValueError("Prompt must not be blank.")
        return cleaned_value


class StoryGenerateResponse(BaseModel):
    """Structured result returned after generating a story."""

    title: str
    story: str
    summary: str
    moral: str
