"""
Voice Category

This module assigns a voice category to the selected narrator type.
The voice category is a descriptive label and does not represent
an actual Text-to-Speech voice.
"""

VOICE_CATEGORIES = {
    "Friendly Storyteller": "Soft Voice",
    "Warm Storyteller": "Warm Voice",
    "Emotional Storyteller": "Gentle Voice",
    "Cinematic Narrator": "Deep Voice",
    "Wise Storyteller": "Inspirational Voice",
    "Relaxing Narrator": "Calm Voice",
    "Adventure Narrator": "Energetic Voice",
    "Mystery Narrator": "Mysterious Voice",
    "Classic Narrator": "Neutral Voice",
}


def get_voice_category(narrator_type: str) -> str:
    """
    Returns the voice category associated with the selected narrator type.

    Args:
        narrator_type (str): The selected narrator type.

    Returns:
        str: The voice category.
    """
    return VOICE_CATEGORIES.get(
        narrator_type,
        "Neutral Voice"
    )