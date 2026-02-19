from fastapi import APIRouter, HTTPException, status, Depends

from sqlalchemy.orm import Session
from core.database import get_session
from services.game_service import GameService
from pydantic import BaseModel


class Turn(BaseModel):
    conversation_id: int
    user_msg: str


router = APIRouter(prefix="/api/v1/games", tags=["games"])
game_service = GameService()


@router.post("/", status_code=status.HTTP_201_CREATED)
def handle_turn(data: Turn, session: Session = Depends(get_session)):
    return game_service.handle_turn(
        user_message=data.user_msg,
        conversation_id=data.conversation_id,
        session=session,
    )
