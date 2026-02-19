from sqlmodel import Session, select
from models.message_model import Message
from helpers.helpers import create_messages


class MessageService:

    def save_message(
        self, session: Session, conversation_id: int, content: str, role: str
    ) -> Message:

        message = Message(conversation_id=conversation_id, content=content, role=role)

        session.add(message)
        session.commit()
        session.refresh(message)

        return message

    def get_messages_by_conversationID(
        self,
        session: Session,
        conversation_id: int,
    ):

        stmt = (
            select(Message)
            .where(Message.conversation_id == conversation_id)
            .order_by(Message.created_at.desc())
            .limit(10)
        )

        result = session.exec(stmt).all()
        messages = create_messages(result)
        return messages
