from app.knowledge.embedding_factory import (
    get_embedding_provider
)

from app.knowledge.qdrant_service import (
    QdrantService
)


embedding = get_embedding_provider()
qdrant = QdrantService()


text = """
DigitalLinks is a digital marketing agency
specializing in SEO, web design, branding,
and AI automation services.
"""


vector = embedding.embed(text)


qdrant.add_document(
    collection_name="digitallinks",
    vector=vector,
    text=text,
    document_id=1,
)


print("Document stored successfully")


results = qdrant.search(
    collection_name="digitallinks",
    vector=vector,
)


for result in results:
    print(result.payload)