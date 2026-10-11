"""
Storytelling Style

This module determines the storytelling style based on
the mood, narration style, and intensity level.
"""


def get_storytelling_style(
    mood: str,
    narration_style: str,
    intensity_level: str,
) -> str:
    """
    Returns the storytelling style.

    Args:
        mood (str): Detected mood.
        narration_style (str): Narration style.
        intensity_level (str): Intensity level.

    Returns:
        str: Storytelling style.
    """

    # High intensity stories take priority.
    if intensity_level == "High":
        if mood == "Tense":
            return "Cinematic Storytelling"

        if mood == "Energetic":
            return "Adventure Storytelling"

    STYLE_MAPPING = {
        "Cheerful": "Joyful Storytelling",
        "Warm": "Cozy Storytelling",
        "Emotional": "Emotional Narrative",
        "Tense": "Suspenseful Storytelling",
        "Inspirational": "Inspirational Storytelling",
        "Peaceful": "Relaxing Storytelling",
        "Energetic": "Adventure Storytelling",
        "Mysterious": "Mysterious Storytelling",
        "Neutral": "Classic Storytelling",
    }

    return STYLE_MAPPING.get(mood, "Classic Storytelling")