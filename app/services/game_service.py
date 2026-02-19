from .message_service import MessageService
from agents.doorman.doorman_agent import Doorman
from agents.judge.judge_agent import Judge
from services.progress_service import ProgressService
from vectorstores.vector_message_service import VectorMessageStore
from .conversation_service import ConversationService


class GameService:
    def __init__(self):
        self.doorman = Doorman()
        self.judge = Judge()
        self.progress_service = ProgressService()
        self.vectorStore = VectorMessageStore()
        self.message_service = MessageService()
        self.conversation_service = ConversationService()

    def handle_turn(self, user_message: str, conversation_id: int, session):

        self.message_service.save_message(
            session=session,
            conversation_id=conversation_id,
            content=user_message,
            role="user",
        )

        past_convo = self.message_service.get_messages_by_conversationID(
            session=session, conversation_id=conversation_id
        )

        semantic_history = self.vectorStore.search_similar(
            conversation_id=conversation_id, query=user_message
        )

        history = past_convo + semantic_history

        reply = self.doorman.reply(user_message=user_message, history=history)

        evaluation = self.judge.evaluate(user_message, reply, history)

        score = int(str(evaluation["influence_score"]).strip())

        self.progress_service.update_progress(
            conversation_id=conversation_id,
            session=session,
            score=score,
        )

        is_won = self.progress_service.is_won(session, conversation_id)
        is_lost = self.progress_service.is_lost(session, conversation_id)

        if is_won:
            self.conversation_service.update_status(session, conversation_id)
            reply = self.doorman.reply(user_message="", history=history, is_won=True)

        elif is_lost:
            self.conversation_service.update_status(session, conversation_id)
            reply = self.doorman.reply(user_message="", history=history, is_lost=True)

        self.message_service.save_message(
            session=session,
            conversation_id=conversation_id,
            content=reply,
            role="assistant",
        )

        self.vectorStore.add_message(
            conversation_id=conversation_id,
            content=user_message,
            role="user",
        )

        self.vectorStore.add_message(
            conversation_id=conversation_id,
            content=reply,
            role="assistant",
        )

        conversation = self.conversation_service.get_conversation_byID(
            session=session,
            conversation_id=conversation_id,
        )

        return {
            "reply": reply,
            "status": conversation.status,
            "progress": conversation.score,
        }
