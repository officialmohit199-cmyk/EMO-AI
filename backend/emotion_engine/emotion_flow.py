from .emotion_classifier import classify_emotions
from .intensity_calculator import calculate_intensity


def detect_emotion_flow(story: str):
    """
    Detects the emotional progression of a story
    by analyzing its beginning, middle, and ending.

    It also calculates the overall emotional intensity
    of the story.
    """

    # Detect the overall emotion of the complete story
    overall_emotion = classify_emotions(story)

    # Calculate the overall emotional intensity
    intensity_result = calculate_intensity(
        overall_emotion["emotion_scores"]
    )

    # Split the story into words
    words = story.split()

    # Count the total number of words
    total_words = len(words)

    # Handle an empty story
    if total_words == 0:
        return {
            "primary_emotion": "Neutral",
            "secondary_emotion": None,
            "mood": "Neutral",
            "intensity_score": 0,
            "intensity_level": "None",
            "beginning_emotion": "Neutral",
            "middle_emotion": "Neutral",
            "ending_emotion": "Neutral"
        }

    # Calculate the size of each section
    section_size = total_words // 3

    # Handle very short stories
    if section_size == 0:
        primary_emotion = overall_emotion["primary_emotion"]

        return {
            "primary_emotion": primary_emotion,
            "secondary_emotion":
                overall_emotion["secondary_emotion"],
            "mood": primary_emotion,
            "intensity_score":
                intensity_result["intensity_score"],
            "intensity_level":
                intensity_result["intensity_level"],
            "beginning_emotion": primary_emotion,
            "middle_emotion": primary_emotion,
            "ending_emotion": primary_emotion
        }

    # Split the story into three sections
    beginning_words = words[:section_size]

    middle_words = words[
        section_size:section_size * 2
    ]

    ending_words = words[
        section_size * 2:
    ]

    # Convert sections back into strings
    beginning_story = " ".join(beginning_words)
    middle_story = " ".join(middle_words)
    ending_story = " ".join(ending_words)

    # Detect emotions in each section
    beginning_emotion = classify_emotions(beginning_story)
    middle_emotion = classify_emotions(middle_story)
    ending_emotion = classify_emotions(ending_story)

    # Get the primary overall emotion
    primary_emotion = overall_emotion["primary_emotion"]

    # Return the complete emotion flow report
    return {
        "primary_emotion": primary_emotion,

        "secondary_emotion":
            overall_emotion["secondary_emotion"],

        "mood": primary_emotion,

        "intensity_score":
            intensity_result["intensity_score"],

        "intensity_level":
            intensity_result["intensity_level"],

        "beginning_emotion":
            beginning_emotion["primary_emotion"],

        "middle_emotion":
            middle_emotion["primary_emotion"],

        "ending_emotion":
            ending_emotion["primary_emotion"]
    }