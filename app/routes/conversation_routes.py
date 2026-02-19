from fastapi import APIRouter, status, Depends

from sqlalchemy.orm import Session
from core.database import get_session
from services.conversation_service import ConversationService


router = APIRouter(prefix="/api/v1/conversations", tags=["conversations"])
conversation_service = ConversationService()


@router.get("/", status_code=status.HTTP_200_OK)
def list_conversations(session: Session = Depends(get_session)):
    return {"status": "ok"}


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_issue(session: Session = Depends(get_session)):
    return conversation_service.create_conversation(session)
