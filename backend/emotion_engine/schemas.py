from pydantic import BaseModel
from typing import Dict, Optional


class EmotionReport(BaseModel):

    primary_emotion: str

    secondary_emotion: Optional[str]

    emotion_scores: Dict[str, int]

    intensity_score: int

    intensity_level: str

    mood: str

    beginning_emotion: str

    middle_emotion: str

    ending_emotion: str

    narration_style: str