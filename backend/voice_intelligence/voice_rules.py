from typing import Dict


VOICE_RULES: Dict[str, Dict[str, str]] = {
    "sad": {
        "low": {
            "speaking_rate": "slow",
            "pitch": "low",
            "energy": "low",
            "pause_style": "normal",
            "emphasis": "moderate",
            "delivery_style": "gentle",
        },
        "medium": {
            "speaking_rate": "slow",
            "pitch": "low",
            "energy": "low",
            "pause_style": "long",
            "emphasis": "moderate",
            "delivery_style": "gentle",
        },
        "high": {
            "speaking_rate": "slow",
            "pitch": "low",
            "energy": "low",
            "pause_style": "long",
            "emphasis": "strong",
            "delivery_style": "gentle",
        },
    },

    "happy": {
        "low": {
            "speaking_rate": "normal",
            "pitch": "medium",
            "energy": "medium",
            "pause_style": "normal",
            "emphasis": "subtle",
            "delivery_style": "warm",
        },
        "medium": {
            "speaking_rate": "normal",
            "pitch": "high",
            "energy": "high",
            "pause_style": "normal",
            "emphasis": "moderate",
            "delivery_style": "warm",
        },
        "high": {
            "speaking_rate": "fast",
            "pitch": "high",
            "energy": "high",
            "pause_style": "short",
            "emphasis": "strong",
            "delivery_style": "energetic",
        },
    },

    "angry": {
        "low": {
            "speaking_rate": "normal",
            "pitch": "low",
            "energy": "medium",
            "pause_style": "normal",
            "emphasis": "moderate",
            "delivery_style": "serious",
        },
        "medium": {
            "speaking_rate": "fast",
            "pitch": "low",
            "energy": "high",
            "pause_style": "short",
            "emphasis": "strong",
            "delivery_style": "serious",
        },
        "high": {
            "speaking_rate": "fast",
            "pitch": "low",
            "energy": "high",
            "pause_style": "short",
            "emphasis": "strong",
            "delivery_style": "dramatic",
        },
    },

    "fear": {
        "low": {
            "speaking_rate": "normal",
            "pitch": "high",
            "energy": "medium",
            "pause_style": "normal",
            "emphasis": "moderate",
            "delivery_style": "mysterious",
        },
        "medium": {
            "speaking_rate": "slow",
            "pitch": "high",
            "energy": "medium",
            "pause_style": "long",
            "emphasis": "strong",
            "delivery_style": "mysterious",
        },
        "high": {
            "speaking_rate": "slow",
            "pitch": "high",
            "energy": "high",
            "pause_style": "long",
            "emphasis": "strong",
            "delivery_style": "mysterious",
        },
    },

    "calm": {
        "low": {
            "speaking_rate": "slow",
            "pitch": "medium",
            "energy": "low",
            "pause_style": "normal",
            "emphasis": "subtle",
            "delivery_style": "calm",
        },
        "medium": {
            "speaking_rate": "slow",
            "pitch": "medium",
            "energy": "low",
            "pause_style": "normal",
            "emphasis": "moderate",
            "delivery_style": "calm",
        },
        "high": {
            "speaking_rate": "normal",
            "pitch": "medium",
            "energy": "medium",
            "pause_style": "normal",
            "emphasis": "moderate",
            "delivery_style": "calm",
        },
    },
}


def get_voice_rule(mood: str, intensity: str) -> Dict[str, str]:
    """
    Returns voice parameters based on mood and emotional intensity.
    """

    mood = mood.lower()
    intensity = intensity.lower()

    if mood not in VOICE_RULES:
        mood = "calm"

    if intensity not in VOICE_RULES[mood]:
        intensity = "medium"

    return VOICE_RULES[mood][intensity]