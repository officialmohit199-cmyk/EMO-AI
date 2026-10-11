from .schemas import VoiceProfile
from .voice_rules import get_voice_rule


class VoiceIntelligenceEngine:
    """
    Main engine for converting emotional context
    into a structured VoiceProfile.
    """

    def generate_voice_profile(
        self,
        mood: str,
        intensity: str
    ) -> VoiceProfile:
        """
        Generate a VoiceProfile using mood and intensity.
        """

        voice_rule = get_voice_rule(mood, intensity)

        return VoiceProfile(
            speaking_rate=voice_rule["speaking_rate"],
            pitch=voice_rule["pitch"],
            energy=voice_rule["energy"],
            pause_style=voice_rule["pause_style"],
            emphasis=voice_rule["emphasis"],
            delivery_style=voice_rule["delivery_style"],
            voice_direction=self._create_voice_direction(voice_rule),
        )

    def _create_voice_direction(self, voice_rule: dict) -> str:
        """
        Creates a human-readable voice direction.
        """

        return (
            f"Speak {voice_rule['speaking_rate']} with "
            f"{voice_rule['pitch']} pitch, "
            f"{voice_rule['energy']} energy, "
            f"{voice_rule['pause_style']} pauses, "
            f"{voice_rule['emphasis']} emphasis, "
            f"and a {voice_rule['delivery_style']} delivery."
        )

    def generate_from_narrator_profile(
        self,
        mood: str,
        intensity: str,
        narrator_profile
    ) -> VoiceProfile:
        """
        Generate a VoiceProfile using emotional context
        and the narrator profile selected by Module 4.
        """

        voice_profile = self.generate_voice_profile(
            mood,
            intensity
        )

        voice_profile.voice_direction = (
            f"{voice_profile.voice_direction} "
            f"Narrator personality: "
            f"{narrator_profile.narrator_personality}. "
            f"Voice category: "
            f"{narrator_profile.voice_category}. "
            f"Storytelling style: "
            f"{narrator_profile.storytelling_style}."
        )

        return voice_profile
    