from typing import Final


# Speaking rate controls how quickly the narrator speaks.
SPEAKING_RATES: Final = {
    "slow": 0.80,
    "normal": 1.00,
    "fast": 1.20,
}


# Pitch levels represent the relative pitch direction.
PITCH_LEVELS: Final = {
    "low": "low",
    "medium": "medium",
    "high": "high",
}


# Energy levels represent the intensity of vocal delivery.
ENERGY_LEVELS: Final = {
    "low": "low",
    "medium": "medium",
    "high": "high",
}


# Pause styles describe the general length of pauses.
PAUSE_STYLES: Final = {
    "short": 0.5,
    "normal": 1.0,
    "long": 1.5,
}


# Emphasis levels describe how strongly important words should be delivered.
EMPHASIS_LEVELS: Final = {
    "subtle": "subtle",
    "moderate": "moderate",
    "strong": "strong",
}