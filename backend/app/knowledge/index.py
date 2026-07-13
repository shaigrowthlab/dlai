import sys

from app.knowledge.loader import WebsiteLoader
from app.knowledge.chunker import TextChunker
from app.knowledge.embedding_factory import (
    get_embedding_provider
)
from app.knowledge.qdrant_service import (
    QdrantService
)


def index_website(url: str):

    print("Loading website...")

    loader = WebsiteLoader()

    content = loader.load(url)


    print(
        "Characters loaded:",
        len(content)
    )


    print("Creating chunks...")

    chunker = TextChunker()

    chunks = chunker.split(content)


    print(
        "Chunks created:",
        len(chunks)
    )


    embedding = get_embedding_provider()

    qdrant = QdrantService()


    collection = "digitallinks"


    for index, chunk in enumerate(chunks):

        print(
            f"Embedding chunk {index + 1}/{len(chunks)}"
        )


        vector = embedding.embed(chunk)


        qdrant.add_document(
            collection_name=collection,
            vector=vector,
            text=chunk,
            document_id=index + 1,
        )


    print("Indexing complete!")


if __name__ == "__main__":

    url = sys.argv[1]

    index_website(url)