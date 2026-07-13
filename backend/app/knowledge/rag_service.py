from app.knowledge.embedding_factory import (
    get_embedding_provider
)

from app.knowledge.qdrant_service import (
    QdrantService
)


class RAGService:

    def __init__(self):
        self.embedding = get_embedding_provider()
        self.qdrant = QdrantService()

    def search(
        self,
        question: str,
        collection_name: str = "digitallinks",
    ):

        vector = self.embedding.embed(
            question
        )

        results = self.qdrant.search(
            collection_name=collection_name,
            vector=vector,
            limit=3,
        )

        contexts = []

        for result in results:
            contexts.append(
                result.payload["text"]
            )

        return contexts