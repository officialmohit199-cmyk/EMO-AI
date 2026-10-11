from typing import Final, Literal


DeliveryStyleType = Literal[
    "gentle",
    "calm",
    "serious",
    "dramatic",
    "energetic",
    "warm",
    "mysterious",
]


DELIVERY_STYLES: Final = {
    "gentle": "Soft, careful, and emotionally restrained delivery.",
    "calm": "Relaxed, steady, and controlled delivery.",
    "serious": "Focused, firm, and authoritative delivery.",
    "dramatic": "Expressive delivery with strong emotional presence.",
    "energetic": "Lively, enthusiastic, and dynamic delivery.",
    "warm": "Friendly, comforting, and emotionally engaging delivery.",
    "mysterious": "Subtle, suspenseful, and intriguing delivery.",
}