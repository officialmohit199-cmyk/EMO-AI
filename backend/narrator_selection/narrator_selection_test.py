from narrator_selection.detector import detect_narrator


def test_all_moods():
    test_cases = [
        ("Cheerful", "Gentle", "Low"),
        ("Warm", "Gentle", "Low"),
        ("Emotional", "Emotional", "High"),
        ("Tense", "Dramatic", "High"),
        ("Inspirational", "Motivational", "Medium"),
        ("Peaceful", "Relaxing", "Low"),
        ("Energetic", "Excited", "High"),
        ("Mysterious", "Cinematic", "Medium"),
        ("Neutral", "Neutral", "Low"),
    ]

    for mood, narration_style, intensity_level in test_cases:
        result = detect_narrator(
            mood=mood,
            narration_style=narration_style,
            intensity_level=intensity_level,
        )

        print(f"\nMood: {mood}")
        print(f"Narrator Type: {result.narrator_type}")
        print(f"Personality: {result.narrator_personality}")
        print(f"Voice Category: {result.voice_category}")
        print(f"Storytelling Style: {result.storytelling_style}")


def test_unknown_mood():
    result = detect_narrator(
        mood="Unknown",
        narration_style="Neutral",
        intensity_level="Low",
    )

    print("\nUnknown Mood Test")
    print(f"Narrator Type: {result.narrator_type}")
    print(f"Personality: {result.narrator_personality}")
    print(f"Voice Category: {result.voice_category}")
    print(f"Storytelling Style: {result.storytelling_style}")


if __name__ == "__main__":
    test_all_moods()
    test_unknown_mood()