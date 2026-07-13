from app.knowledge.embedding_factory import get_embedding_provider


provider = get_embedding_provider()

vector = provider.embed(
    "DigitalLinks provides SEO and digital marketing services"
)

print(len(vector))
print(vector[:5])