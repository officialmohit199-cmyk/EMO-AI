"""Small standalone smoke test for Semantic Emotion Intelligence."""

from backend.AI.semantic_emotion import (
    SemanticEmotionAnalysisError,
    SemanticEmotionAnalyzer,
)


LITERARY_STORY = """
Each evening, Mira set a second cup beside the window before the streetlights
stirred awake. The porcelain cooled untouched while rain traced the same old
paths down the glass. When the train passed beyond the hill, she folded the
newspaper carefully and listened until its last carriage became silence.
""".strip()


def print_result(label: str, result) -> None:
    """Display a Pydantic result as readable structured JSON."""
    print(f"\n{label}")
    print(result.model_dump_json(indent=2))


def main() -> None:
    """Run the standalone test without assuming an LLM provider exists."""
    analyzer = SemanticEmotionAnalyzer()

    print("===== SEMANTIC EMOTION INTELLIGENCE TEST =====")
    if analyzer.has_provider:
        print("Provider status: configured")
    else:
        print("Provider status: not configured")

    print("\nLiterary contextual-emotion story:")
    print(LITERARY_STORY)

    try:
        result = analyzer.analyze(LITERARY_STORY)
    except SemanticEmotionAnalysisError as error:
        print("\nSemantic analysis unavailable:")
        print(error)
    else:
        print_result("Semantic analysis result:", result)

    empty_result = analyzer.analyze("")
    print_result("Empty-input result:", empty_result)


if __name__ == "__main__":
    main()
