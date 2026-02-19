from .chroma_client import ChromaClient
from langchain_core.documents import Document


class VectorMessageStore:

    def __init__(self):
        self.db = ChromaClient().get_db()

    def add_message(self, conversation_id: int, content: str, role: str):

        doc = Document(
            page_content=content,
            metadata={"conversation_id": conversation_id, "role": role},
        )

        self.db.add_documents([doc])

    def search_similar(self, conversation_id: int, query: str, k: int = 5):

        docs = self.db.similarity_search(
            query=query, k=k, filter={"conversation_id": conversation_id}
        )

        results = []
        for doc in docs:
            results.append({"role": doc.metadata["role"], "content": doc.page_content})
        return results
