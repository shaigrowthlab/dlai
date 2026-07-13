class TextChunker:

    def __init__(
        self,
        chunk_size: int = 300,
        overlap: int = 100,
    ):
        self.chunk_size = chunk_size
        self.overlap = overlap


    def split(self, text: str) -> list[str]:

        words = text.split()

        chunks = []

        start = 0

        while start < len(words):

            end = start + self.chunk_size

            chunk = " ".join(
                words[start:end]
            )

            chunks.append(chunk)

            start += (
                self.chunk_size
                - self.overlap
            )

        return chunks