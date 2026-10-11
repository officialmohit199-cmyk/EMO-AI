"""API routes for story generation."""

from fastapi import APIRouter, HTTPException, status

from AI.story_generator import StoryGenerationError
from schemas.story_schema import StoryGenerateRequest, StoryGenerateResponse
from services.story_service import StoryService


router = APIRouter(tags=["story"])
_story_service = StoryService()


@router.post(
    "/story",
    response_model=StoryGenerateResponse,
    status_code=status.HTTP_200_OK,
    summary="Generate an emotionally engaging short story",
)
def generate_story(payload: StoryGenerateRequest) -> StoryGenerateResponse:
    """Generate a structured short story from a user's prompt."""
    try:
        generated_story = _story_service.generate_story(payload.prompt)
    except StoryGenerationError as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error),
        ) from error
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unable to generate a story at this time.",
        ) from error

    return StoryGenerateResponse(
        title=generated_story.title,
        story=generated_story.story,
        summary=generated_story.summary,
        moral=generated_story.moral,
    )
