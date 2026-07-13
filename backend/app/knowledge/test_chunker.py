from app.knowledge.loader import WebsiteLoader
from app.knowledge.chunker import TextChunker


loader = WebsiteLoader()

content = loader.load(
    "https://digitallinks.net"
)


chunker = TextChunker()

chunks = chunker.split(content)


print(
    "Total chunks:",
    len(chunks)
)


for i, chunk in enumerate(chunks[:3]):
    print("\nCHUNK", i + 1)
    print(chunk[:300])