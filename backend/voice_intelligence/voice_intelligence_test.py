from backend.voice_intelligence.voice_intelligence import VoiceIntelligenceEngine


def test_voice_profile(mood, intensity):
    engine = VoiceIntelligenceEngine()

    profile = engine.generate_voice_profile(mood, intensity)

    print("\n--------------------------------")
    print("Mood:", mood)
    print("Intensity:", intensity)
    print("Voice Profile:")
    print(profile)
    print("--------------------------------")


def main():
    print("\n===== MODULE 5 TEST =====")

    # Test 1: Sad emotion
    test_voice_profile("sad", "high")

    # Test 2: Happy emotion
    test_voice_profile("happy", "medium")

    # Test 3: Angry emotion
    test_voice_profile("angry", "high")

    # Test 4: Fear emotion
    test_voice_profile("fear", "high")

    # Test 5: Calm emotion
    test_voice_profile("calm", "low")

    # Test 6: Unknown mood
    test_voice_profile("unknown", "medium")

    # Test 7: Unknown intensity
    test_voice_profile("happy", "unknown")

    print("\n===== ALL TESTS COMPLETED =====")


if __name__ == "__main__":
    main()