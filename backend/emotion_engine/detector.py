from emotion_classifier import classify_emotions
from intensity_calculator import calculate_intensity
from mood_detector import detect_mood
from emotion_flow import detect_emotion_flow
from narration_style import detect_narration_style


def detect_story_emotions(story: str):
    """
    Master emotion detection function for EMO-AI.

    Parameters:
        story (str): Complete story text.

    Returns:
        Complete emotional analysis report.
    """

    # Detect emotions
    emotion_report = classify_emotions(story)

    # Calculate emotional intensity
    intensity_report = calculate_intensity(
        emotion_report["emotion_scores"]
    )

    # Detect overall mood
    mood_report = detect_mood(
        emotion_report["primary_emotion"]
    )

    # Detect emotional progression
    emotion_flow_report = detect_emotion_flow(story)

    # Detect narration style
    narration_style_report = detect_narration_style(
        mood_report["mood"],
        intensity_report["intensity_level"]
    )

    # Combine all reports
    final_report = {

        **emotion_report,

        **intensity_report,

        **mood_report,

        **emotion_flow_report,

        **narration_style_report

    }

    # Return the final report
    return final_report