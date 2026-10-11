from detector import detect_story_emotions


# Test Story

story = """
The lonely boy cried every night because he missed his family.

One day, he discovered a mysterious map and began an exciting adventure.

After many challenges, he happily returned home and celebrated with his friends.
"""


print("\nEMO-AI FINAL EMOTION REPORT\n")

report = detect_story_emotions(story)

print(report)
