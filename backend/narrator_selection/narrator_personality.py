"""
Narrator Personality

This module defines the personality associated with each narrator type.
It helps maintain a consistent storytelling experience by assigning
a suitable personality to the selected narrator.
"""

NARRATOR_PERSONALITIES = {
    "Friendly Storyteller": "Cheerful & Friendly",
    "Warm Storyteller": "Warm & Caring",
    "Emotional Storyteller": "Gentle & Emotional",
    "Cinematic Narrator": "Bold & Intense",
    "Wise Storyteller": "Wise & Motivational",
    "Relaxing Narrator": "Calm & Peaceful",
    "Adventure Narrator": "Energetic & Brave",
    "Mystery Narrator": "Deep & Mysterious",
    "Classic Narrator": "Neutral & Professional",
}


def get_narrator_personality(narrator_type: str) -> str:
    """
    Returns the personality associated with the selected narrator type.

    Args:
        narrator_type (str): The narrator type selected by the Narrator Selector.

    Returns:
        str: The narrator personality.
    """
    return NARRATOR_PERSONALITIES.get(
        narrator_type,
        "Neutral & Professional"
    )