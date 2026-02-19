from sqlmodel import SQLModel, Field
from datetime import datetime
from enum import Enum


class ConversationStatus(Enum):
    ongoing = "ongoing"
    ended = "ended"


class Conversation(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    score: int = Field(default=0, nullable=False)
    status: ConversationStatus = Field(default=ConversationStatus.ongoing)
    created_at: datetime = Field(default=datetime.now())
