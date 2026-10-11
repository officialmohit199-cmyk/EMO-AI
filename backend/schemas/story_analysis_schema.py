"""Pydantic schemas for story analysis."""

from pydantic import BaseModel, Field, field_validator


class StoryAnalysisRequest(BaseModel):
    """Input accepted by the story analysis workflow."""

    story: str = Field(
        ...,
        min_length=3,
        max_length=20_000,
        description="The generated story to analyze.",
    )

    @field_validator("story")
    @classmethod
    def validate_story(cls, value: str) -> str:
        cleaned_value = " ".join(value.split())
        if not cleaned_value:
            raise ValueError("Story must not be blank.")
        return cleaned_value


class StoryAnalysisResponse(BaseModel):
    """Structured narrative analysis returned for a generated story."""

    main_character: str
    setting: str
    theme: str
    conflict: str
    story_arc: str
    target_audience: str
