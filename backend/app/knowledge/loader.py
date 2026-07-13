import requests
from bs4 import BeautifulSoup


class WebsiteLoader:

    def load(self, url: str) -> str:

        response = requests.get(
            url,
            timeout=30,
            headers={
                "User-Agent": "DigitalLinks-AI-Bot"
            },
        )

        response.raise_for_status()

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        # Remove unwanted sections
        for tag in soup.find_all(
            [
                "script",
                "style",
                "nav",
                "footer",
                "header",
                "aside",
                "form",
            ]
        ):
            tag.decompose()

        # Remove empty lines
        text = soup.get_text(
            separator="\n"
        )

        lines = [
            line.strip()
            for line in text.splitlines()
            if line.strip()
        ]

        return "\n".join(lines)