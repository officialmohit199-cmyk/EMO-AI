from intensity_calculator import calculate_intensity


# Test Case 1 - No Emotion
emotion_scores_1 = {
    "Happy": 0,
    "Sadness": 0,
    "Love": 0,
    "Fear": 0
}

print("\nTest Case 1 - No Emotion")
print(calculate_intensity(emotion_scores_1))


# Test Case 2 - Very Low Intensity
emotion_scores_2 = {
    "Happy": 1,
    "Sadness": 0,
    "Love": 0,
    "Fear": 0
}

print("\nTest Case 2 - Very Low Intensity")
print(calculate_intensity(emotion_scores_2))


# Test Case 3 - Low Intensity
emotion_scores_3 = {
    "Happy": 2,
    "Love": 1
}

print("\nTest Case 3 - Low Intensity")
print(calculate_intensity(emotion_scores_3))


# Test Case 4 - Medium Intensity
emotion_scores_4 = {
    "Love": 3,
    "Hope": 2
}

print("\nTest Case 4 - Medium Intensity")
print(calculate_intensity(emotion_scores_4))


# Test Case 5 - High Intensity
emotion_scores_5 = {
    "Fear": 5,
    "Hope": 2
}

print("\nTest Case 5 - High Intensity")
print(calculate_intensity(emotion_scores_5))


# Test Case 6 - Extreme Intensity
emotion_scores_6 = {
    "Fear": 15
}

print("\nTest Case 6 - Extreme Intensity")
print(calculate_intensity(emotion_scores_6))