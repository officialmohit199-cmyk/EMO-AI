from typing import Literal

from pydantic import BaseModel, Field


SpeakingRate = Literal["slow", "normal", "fast"]
PitchLevel = Literal["low", "medium", "high"]
EnergyLevel = Literal["low", "medium", "high"]
PauseStyle = Literal["short", "normal", "long"]
EmphasisLevel = Literal["subtle", "moderate", "strong"]
DeliveryStyle = Literal[
    "gentle",
    "calm",
    "serious",
    "dramatic",
    "energetic",
    "warm",
    "mysterious",
]


class VoiceProfile(BaseModel):
    """
    Defines how a selected narrator should deliver a story.

    This model represents voice-direction data for the future
    TTS/audio generation layer.
    """

    speaking_rate: SpeakingRate = Field(
        default="normal",
        description="Controls the speaking speed."
    )

    pitch: PitchLevel = Field(
        default="medium",
        description="Defines the overall pitch level."
    )

    energy: EnergyLevel = Field(
        default="medium",
        description="Controls vocal energy and intensity."
    )

    pause_style: PauseStyle = Field(
        default="normal",
        description="Defines the length and frequency of pauses."
    )

    emphasis: EmphasisLevel = Field(
        default="moderate",
        description="Controls emphasis on important words or phrases."
    )

    delivery_style: DeliveryStyle = Field(
        default="warm",
        description="Defines the overall narration delivery style."
    )

    voice_direction: str = Field(
        default="Deliver the story naturally with clear and expressive narration.",
        min_length=1,
        description="Human-readable instructions for future TTS/audio systems."
    )