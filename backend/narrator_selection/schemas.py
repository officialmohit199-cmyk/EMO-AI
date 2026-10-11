"""
Narrator Selection Schemas

This module defines the Pydantic schemas used by
the Narrator Selection Engine.
"""

from pydantic import BaseModel


class NarratorProfile(BaseModel):
    """Represents the final narrator profile selected for a story."""

    narrator_type: str
    narrator_personality: str
    voice_category: str
    storytelling_style: str