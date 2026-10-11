"""Application service for the story generation workflow."""

from AI.story_generator import GeneratedStory, StoryGenerator


class StoryService:
    """Coordinates story generation for API consumers."""

    def __init__(self, generator: StoryGenerator | None = None) -> None:
        self._generator = generator or StoryGenerator()

    def generate_story(self, prompt: str) -> GeneratedStory:
        """Generate a story from a validated user prompt."""
        return self._generator.generate(prompt)
