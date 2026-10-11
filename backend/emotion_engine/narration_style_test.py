from narration_style import detect_narration_style


# Test Case 1 - Warm + Low
print("\nTest Case 1 - Warm + Low")
print(detect_narration_style("Warm", "Low"))


# Test Case 2 - Warm + High
print("\nTest Case 2 - Warm + High")
print(detect_narration_style("Warm", "High"))


# Test Case 3 - Emotional + Medium
print("\nTest Case 3 - Emotional + Medium")
print(detect_narration_style("Emotional", "Medium"))


# Test Case 4 - Tense + High
print("\nTest Case 4 - Tense + High")
print(detect_narration_style("Tense", "High"))


# Test Case 5 - Energetic + High
print("\nTest Case 5 - Energetic + High")
print(detect_narration_style("Energetic", "High"))


# Test Case 6 - Peaceful + Low
print("\nTest Case 6 - Peaceful + Low")
print(detect_narration_style("Peaceful", "Low"))


# Test Case 7 - Mysterious + Medium
print("\nTest Case 7 - Mysterious + Medium")
print(detect_narration_style("Mysterious", "Medium"))


# Test Case 8 - Inspirational + Medium
print("\nTest Case 8 - Inspirational + Medium")
print(detect_narration_style("Inspirational", "Medium"))


# Test Case 9 - Unknown Combination
print("\nTest Case 9 - Unknown Combination")
print(detect_narration_style("Warm", "Extreme"))