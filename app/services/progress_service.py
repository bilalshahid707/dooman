from .conversation_service import ConversationService
from sqlmodel import Session


class ProgressService:
    def __init__(self):
        self.conversation_service = ConversationService()

    def update_progress(self, score: int, conversation_id: int, session: Session):
        new_progress = self.conversation_service.update_score(
            session, score, conversation_id
        )
        return new_progress

    def update_status(self, session: Session):
        conversation = self.conversation_service.update_status(session=session)
        return conversation

    def is_won(self, session, conversation_id):
        conversation = self.conversation_service.get_conversation_byID(
            session=session, conversation_id=conversation_id
        )
        return conversation.score >= 50

    def is_lost(self, session, conversation_id):
        conversation = self.conversation_service.get_conversation_byID(
            session=session, conversation_id=conversation_id
        )
        return conversation.score < 0
