from emotion_flow import detect_emotion_flow


# Test Case 1 - Emotional Journey Story
story1 = """
The lonely boy cried every night because he missed his family.

One day, he discovered a mysterious map and began his journey.

He happily returned home and celebrated with his friends.
"""

print("\nTest Case 1 - Emotional Journey")
print(detect_emotion_flow(story1))


# Test Case 2 - Adventure Story
story2 = """
The young explorer dreamed of visiting ancient kingdoms.

He bravely explored dangerous caves and hidden treasures.

He returned peacefully with unforgettable memories.
"""

print("\nTest Case 2 - Adventure Story")
print(detect_emotion_flow(story2))


# Test Case 3 - Horror Story
story3 = """
The village was calm and peaceful.

A terrifying creature suddenly appeared in the darkness.

The survivors hoped for a brighter future.
"""

print("\nTest Case 3 - Horror Story")
print(detect_emotion_flow(story3))