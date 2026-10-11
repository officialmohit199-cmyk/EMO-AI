"""
Narrator Selection Detector

This module acts as the master controller for the
Narrator Selection Engine.

It coordinates the narrator selection components
and returns the final NarratorProfile.
"""

from .narrator_selector import select_narrator
from .narrator_personality import get_narrator_personality
from .voice_category import get_voice_category
from .storytelling_style import get_storytelling_style
from .schemas import NarratorProfile


def detect_narrator(
    mood: str,
    narration_style: str,
    intensity_level: str,
) -> NarratorProfile:
    """
    Creates a complete narrator profile from emotion analysis results.

    Args:
        mood (str): Mood detected by the Emotion Detection Engine.
        narration_style (str): Narration style detected by the Emotion Engine.
        intensity_level (str): Emotional intensity level.

    Returns:
        NarratorProfile: Complete narrator selection result.
    """

    narrator_type = select_narrator(mood)

    narrator_personality = get_narrator_personality(
        narrator_type
    )

    voice_category = get_voice_category(
        narrator_type
    )

    storytelling_style = get_storytelling_style(
        mood,
        narration_style,
        intensity_level,
    )

    return NarratorProfile(
        narrator_type=narrator_type,
        narrator_personality=narrator_personality,
        voice_category=voice_category,
        storytelling_style=storytelling_style,
    )