from emotion_classifier import classify_emotions


# Test Case 1 - Empty Story
story1 = ""
print("\nTest Case 1 - Empty Story")
print(classify_emotions(story1))


# Test Case 2 - No Emotion Story
story2 = "The sky is blue. The grass is green."
print("\nTest Case 2 - No Emotion Story")
print(classify_emotions(story2))


# Test Case 3 - Single Emotion Story
story3 = "happy happy happy happy"
print("\nTest Case 3 - Single Emotion Story")
print(classify_emotions(story3))


# Test Case 4 - Two Emotion Story
story4 = "I love my family and I am happy."
print("\nTest Case 4 - Two Emotion Story")
print(classify_emotions(story4))


# Test Case 5 - Three Emotion Story
story5 = """
I love my family.
I am happy.
I believe in my future.
"""
print("\nTest Case 5 - Three Emotion Story")
print(classify_emotions(story5))


# Test Case 6 - Equal Scores
story6 = """
I love my family.
I have hope for my future.
"""
print("\nTest Case 6 - Equal Scores")
print(classify_emotions(story6))


# Test Case 7 - Long Emotional Story
story7 = """
The brave knight began his journey through the ancient kingdom.

He was excited to explore the mysterious forest.

Although he was scared of the darkness, he never gave up.

He believed that he would save his people and bring peace to the kingdom.
"""
print("\nTest Case 7 - Long Emotional Story")
print(classify_emotions(story7))