# Narration style mapping dictionary

NARRATION_STYLE_MAP = {

    ("Warm", "Low"): "Gentle",
    ("Warm", "High"): "Emotional",

    ("Emotional", "Medium"): "Calm Emotional",

    ("Tense", "High"): "Dramatic",

    ("Energetic", "High"): "Excited",

    ("Peaceful", "Low"): "Relaxing",

    ("Mysterious", "Medium"): "Cinematic",

    ("Inspirational", "Medium"): "Motivational",

    ("Neutral", "Very Low"): "Standard",

    ("Neutral", "Low"): "Standard"

}


def detect_narration_style(mood, intensity_level):
    """
    Detects the narration style of a story
    using its mood and emotional intensity.

    Parameters:
        mood (str): Overall mood of the story.
        intensity_level (str): Emotional intensity level.

    Returns:
        Narration style information.
    """

    # Get the narration style from the dictionary
    narration_style = NARRATION_STYLE_MAP.get(
        (mood, intensity_level),
        "Standard"
    )

    # Return the narration style
    return {
        "narration_style": narration_style
    }