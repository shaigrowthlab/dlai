import os
from dotenv import load_dotenv
from google import genai

# Load the .env file
load_dotenv()

# Create Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Send a prompt
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Write an SEO title for a dentist in New York."
)

print("\nGemini Response:\n")
print(response.text)