# Mood mapping dictionary

MOOD_MAP = {
    "Happy": "Cheerful",
    "Sadness": "Emotional",
    "Love": "Warm",
    "Fear": "Tense",
    "Hope": "Inspirational",
    "Calm": "Peaceful",
    "Excitement": "Energetic",
    "Nostalgia": "Emotional",
    "Mystery": "Mysterious",
    "Adventure": "Energetic",
    "Suspense": "Tense",
    "Neutral": "Neutral"
}


def detect_mood(primary_emotion):
    """
    Detects the overall mood of a story
    using the primary emotion generated
    by emotion_classifier.py.

    Parameters:
        primary_emotion (str): The dominant emotion.

    Returns:
        Mood information for the story.
    """

    # Get the mood from the mood mapping dictionary
    mood = MOOD_MAP.get(primary_emotion, "Unknown")

    # Return the mood information
    return {
        "mood": mood
    }