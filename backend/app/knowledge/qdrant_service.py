from qdrant_client import QdrantClient
from qdrant_client.models import (
    VectorParams,
    Distance,
    PointStruct,
)

from app.core.config import settings


class QdrantService:

    def __init__(self):
        self.client = QdrantClient(
            url=settings.QDRANT_URL
        )

    def create_collection(
        self,
        collection_name: str
    ):
        collections = (
            self.client
            .get_collections()
            .collections
        )

        exists = any(
            c.name == collection_name
            for c in collections
        )

        if not exists:
            self.client.create_collection(
                collection_name=collection_name,
                vectors_config=VectorParams(
                    size=768,
                    distance=Distance.COSINE,
                ),
            )

    def add_document(
        self,
        collection_name: str,
        vector: list[float],
        text: str,
        document_id: int,
    ):

        self.create_collection(
            collection_name
        )

        self.client.upsert(
            collection_name=collection_name,
            points=[
                PointStruct(
                    id=document_id,
                    vector=vector,
                    payload={
                        "text": text
                    },
                )
            ],
        )

    def search(
        self,
        collection_name: str,
        vector: list[float],
        limit: int = 5,
    ):

        results = self.client.query_points(
            collection_name=collection_name,
            query=vector,
            limit=limit,
        )

        return results.points