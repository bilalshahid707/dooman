from sqlmodel import Session, select
from models.conversation_model import Conversation
from models.conversation_model import ConversationStatus


class ConversationService:

    def create_conversation(self, session: Session):
        conversation = Conversation(score=0)
        session.add(conversation)
        session.commit()
        session.refresh(conversation)
        return conversation

    def update_score(self, session: Session, score: int, conversation_id: int):
        # print(score)
        stmt = select(Conversation).where(Conversation.id == conversation_id)
        conversation = session.exec(stmt).one()
        # print(conversation.score)
        conversation.score += score
        # print(conversation.score)
        session.add(conversation)
        session.commit()
        session.refresh(conversation)
        return conversation

    def update_status(self, session: Session, conversation_id: int):
        stmt = select(Conversation).where(Conversation.id == conversation_id)
        conversation = session.exec(stmt).one()
        conversation.status = ConversationStatus.ended
        return conversation

    def get_conversation_byID(self, session: Session, conversation_id: int):
        stmt = select(Conversation).where(Conversation.id == conversation_id)
        conversation = session.exec(stmt).one()
        return conversation
