"""
Narrator Selector

This module selects the most appropriate narrator type
based on the mood detected by the Emotion Detection Engine.
"""

NARRATOR_MAPPING = {
    "Cheerful": "Friendly Storyteller",
    "Warm": "Warm Storyteller",
    "Emotional": "Emotional Storyteller",
    "Tense": "Cinematic Narrator",
    "Inspirational": "Wise Storyteller",
    "Peaceful": "Relaxing Narrator",
    "Energetic": "Adventure Narrator",
    "Mysterious": "Mystery Narrator",
    "Neutral": "Classic Narrator",
}


def select_narrator(mood: str) -> str:
    """
    Select the narrator type based on the detected mood.

    Args:
        mood (str): Mood from the Emotion Detection Engine.

    Returns:
        str: Selected narrator type.
    """
    return NARRATOR_MAPPING.get(mood, "Classic Narrator")