"""
EMO-AI Full Storytelling Pipeline Test

Tests the complete flow:

Story
→ Emotion Detection
→ Mood
→ Intensity
→ Narration Style
→ Narrator Selection
→ Voice Intelligence
"""

from backend.emotion_engine.emotion_classifier import classify_emotions
from backend.emotion_engine.mood_detector import detect_mood
from backend.emotion_engine.intensity_calculator import calculate_intensity
from backend.emotion_engine.narration_style import detect_narration_style

from backend.narrator_selection.detector import detect_narrator
from backend.voice_intelligence.voice_intelligence import VoiceIntelligenceEngine


def run_pipeline_test(story: str):

    print("=" * 60)
    print("EMO-AI FULL STORYTELLING PIPELINE")
    print("=" * 60)

    # ==========================================================
    # MODULE 3 — EMOTION DETECTION
    # ==========================================================

    print("\n[MODULE 3] Emotion Detection")

    emotion_result = classify_emotions(story)

    primary_emotion = emotion_result["primary_emotion"]
    secondary_emotion = emotion_result["secondary_emotion"]

    print("Primary Emotion:", primary_emotion)
    print("Secondary Emotion:", secondary_emotion)

    # ==========================================================
    # MOOD DETECTION
    # ==========================================================

    mood_result = detect_mood(primary_emotion)

    mood = mood_result["mood"]

    print("Mood:", mood)

    # ==========================================================
    # INTENSITY CALCULATION
    # ==========================================================

    intensity_result = calculate_intensity(
        emotion_result["emotion_scores"]
    )

    intensity_level = intensity_result["intensity_level"]

    print("Intensity:", intensity_level)

    # ==========================================================
    # NARRATION STYLE
    # ==========================================================

    narration_result = detect_narration_style(
        mood,
        intensity_level
    )

    narration_style = narration_result["narration_style"]

    print("Narration Style:", narration_style)

    # ==========================================================
    # MODULE 4 — NARRATOR SELECTION
    # ==========================================================

    print("\n[MODULE 4] Narrator Selection")

    narrator_profile = detect_narrator(
        mood,
        narration_style,
        intensity_level
    )

    print("Narrator Type:", narrator_profile.narrator_type)
    print("Narrator Personality:", narrator_profile.narrator_personality)
    print("Voice Category:", narrator_profile.voice_category)
    print("Storytelling Style:", narrator_profile.storytelling_style)

    # ==========================================================
    # VOICE INTELLIGENCE ENGINE
    # ==========================================================

    print("\n[VOICE INTELLIGENCE ENGINE]")

    engine = VoiceIntelligenceEngine()

    voice_profile = engine.generate_from_narrator_profile(
        mood,
        intensity_level,
        narrator_profile
    )

    print("Voice Profile:")
    print(voice_profile)

    # ==========================================================
    # FINAL PIPELINE RESULT
    # ==========================================================

    print("\n" + "=" * 60)
    print("FINAL STORYTELLING PROFILE")
    print("=" * 60)

    print("Emotion:", primary_emotion)
    print("Secondary Emotion:", secondary_emotion)
    print("Mood:", mood)
    print("Intensity:", intensity_level)
    print("Narration Style:", narration_style)
    print("Narrator Type:", narrator_profile.narrator_type)
    print("Narrator Personality:", narrator_profile.narrator_personality)
    print("Voice Category:", narrator_profile.voice_category)
    print("Storytelling Style:", narrator_profile.storytelling_style)

    print("\nVoice Intelligence:")
    print(voice_profile)

    print("=" * 60)


# ==============================================================
# TEST STORY
# ==============================================================

if __name__ == "__main__":

    story = """
  “‘Oh, I am so grateful to you! You see, I close my eyes and think: if everyone else believes, then why do I feel all this? And now people say that it all stems in the first place from a fear of nature’s frightening manifestations and that none of it is based in reality. But wait, I think: all my life I’ve believed that I shall die, and that suddenly there will be nothing there, only “burdock growing on a grave”,¹ as I read in the work of a certain writer. That is dreadful! How, how am I to restore my faith? Though actually, I only had it when I was a little girl, it was something automatic, something I didn’t even need to think about . . . How, how can it be proven? I have come now to abase myself before you and ask you for this. I mean, if I let this opportunity pass me by, then no one will give me an answer for the rest of my life. How can it be proven, how can one be convinced it is true? Oh, it’s too unfortunate! I stand and look around me and see that no one could care less, or practically no one, no one worries about this any more, and I’m the only person who cannot endure it. It is murderous, murderous!’
    """

    run_pipeline_test(story)