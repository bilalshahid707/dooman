from sqlmodel import Field, SQLModel
from enum import Enum
from datetime import datetime


class MessageRole(str, Enum):
    user = "user"
    assistant = "assistant"
    system = "system"


class Message(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    conversation_id: int = Field(foreign_key="conversation.id", index=True)
    content: str
    role: MessageRole
    created_at: datetime = Field(default=datetime.now())
