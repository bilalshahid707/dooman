from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings


class ChromaClient:
    def __init__(self):
        self.embeddings = OpenAIEmbeddings(
            api_key="sk-4DYqAK.b061f230dd803dd60ef3873e19c0d393044e147d5525e0edc756e9410b5be0db"
        )
        self.db = Chroma(
            collection_name="doorman_embeddings", persist_directory="./chromadb"
        )

    def get_db(self):
        return self.db
