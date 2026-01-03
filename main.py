from dotenv import load_dotenv
from pydantic import BaseModel
from google import genai

load_dotenv()
client = genai.Client()
response = client.models.generate_content(
    model="gemini-3-pro-preview",
    contents="Hello Gemini!")
print(response.text)