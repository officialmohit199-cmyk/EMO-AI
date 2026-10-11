# ============================================================
# EMO-AI - Emotion Classifier
# ============================================================

import re


# Emotion keyword dictionary
#
# Multiple word forms are included so that the classifier
# can recognize natural variations such as:
#
# cry, cried, crying
# miss, missed, missing
# happy, happiness
#
EMOTION_KEYWORDS = {

    "Happy": [
        "happy",
        "happiness",
        "smile",
        "smiled",
        "smiling",
        "joy",
        "joyful",
        "celebrate",
        "celebrated",
        "celebration",
        "laugh",
        "laughed",
        "laughing"
    ],

    "Sadness": [
        "sad",
        "sadness",
        "cry",
        "cried",
        "crying",
        "tears",
        "tear",
        "lonely",
        "loneliness",
        "loss",
        "lost",
        "grief",
        "grieving",
        "heartbroken",
        "heartbreak",
        "miss",
        "missed",
        "missing",
        "goodbye",
        "empty",
        "gone",
        "sorrow",
        "pain",
        "painful"
    ],

    "Love": [
        "love",
        "loved",
        "loving",
        "family",
        "friend",
        "friendship",
        "care",
        "caring",
        "mother",
        "father",
        "daughter",
        "son",
        "hug",
        "hugged"
    ],

    "Fear": [
        "fear",
        "afraid",
        "scared",
        "frightened",
        "danger",
        "dangerous",
        "darkness",
        "terrified",
        "terror",
        "worry",
        "worried"
    ],

    "Anger": [
        "anger",
        "angry",
        "furious",
        "fury",
        "revenge",
        "hate",
        "hated",
        "hatred",
        "rage",
        "raging"
    ],

    "Hope": [
        "hope",
        "hopeful",
        "dream",
        "dreams",
        "believe",
        "believed",
        "believing",
        "future",
        "possibility",
        "possible"
    ],

    "Calm": [
        "peaceful",
        "peace",
        "quiet",
        "gentle",
        "relax",
        "relaxed",
        "relaxing",
        "calm",
        "calmness",
        "serene"
    ],

    "Excitement": [
        "excited",
        "exciting",
        "thrilling",
        "thrill",
        "amazing",
        "amazement",
        "adventure",
        "wonderful"
    ],

    "Nostalgia": [
        "memory",
        "memories",
        "childhood",
        "old days",
        "remember",
        "remembered",
        "past"
    ],

    "Mystery": [
        "mystery",
        "mysterious",
        "secret",
        "unknown",
        "hidden",
        "strange",
        "stranger"
    ],

    "Adventure": [
        "journey",
        "explore",
        "explored",
        "exploring",
        "quest",
        "adventure",
        "travel",
        "discover",
        "discovered"
    ],

    "Suspense": [
        "tension",
        "tense",
        "waiting",
        "waited",
        "unexpected",
        "suddenly",
        "danger",
        "uncertain"
    ]
}


def _count_keyword(text: str, keyword: str) -> int:
    """
    Counts a keyword or phrase safely.

    Whole-word matching prevents accidental matches
    inside unrelated words.
    """

    pattern = r"\b" + re.escape(keyword) + r"\b"

    return len(re.findall(pattern, text))


def classify_emotions(story: str):
    """
    Detects the emotions present in a story.

    Returns:

        primary_emotion:
            Dominant emotion.

        secondary_emotion:
            Second strongest detected emotion.

        emotion_scores:
            Score for every emotion.
    """

    # Convert story to lowercase
    story = story.lower().strip()

    # --------------------------------------------------------
    # Empty story
    # --------------------------------------------------------

    if not story:

        return {
            "primary_emotion": "Neutral",
            "secondary_emotion": None,
            "emotion_scores": {}
        }

    # --------------------------------------------------------
    # Initialize scores
    # --------------------------------------------------------

    emotion_scores = {}

    for emotion in EMOTION_KEYWORDS:
        emotion_scores[emotion] = 0

    # --------------------------------------------------------
    # Count emotional keywords
    # --------------------------------------------------------

    for emotion, keywords in EMOTION_KEYWORDS.items():

        for keyword in keywords:

            count = _count_keyword(story, keyword)

            emotion_scores[emotion] += count

    # --------------------------------------------------------
    # Get detected emotions
    # --------------------------------------------------------

    detected_emotions = {
        emotion: score
        for emotion, score in emotion_scores.items()
        if score > 0
    }

    # --------------------------------------------------------
    # No emotion detected
    # --------------------------------------------------------

    if not detected_emotions:

        return {
            "primary_emotion": "Neutral",
            "secondary_emotion": None,
            "emotion_scores": emotion_scores
        }

    # --------------------------------------------------------
    # Sort emotions by score
    # --------------------------------------------------------

    sorted_emotions = sorted(
        detected_emotions.items(),
        key=lambda item: item[1],
        reverse=True
    )

    # --------------------------------------------------------
    # Primary emotion
    # --------------------------------------------------------

    primary_emotion = sorted_emotions[0][0]

    # --------------------------------------------------------
    # Secondary emotion
    # --------------------------------------------------------

    if len(sorted_emotions) > 1:

        secondary_emotion = sorted_emotions[1][0]

    else:

        secondary_emotion = None

    # --------------------------------------------------------
    # Return result
    # --------------------------------------------------------

    return {
        "primary_emotion": primary_emotion,
        "secondary_emotion": secondary_emotion,
        "emotion_scores": emotion_scores
    }