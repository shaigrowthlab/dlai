from app.knowledge.loader import WebsiteLoader


loader = WebsiteLoader()

content = loader.load(
    "https://digitallinks.net"
)

print(content[:2000])