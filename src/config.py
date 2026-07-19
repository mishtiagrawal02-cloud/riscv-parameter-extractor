import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

if not API_KEY:
    raise ValueError("GROQ_API_KEY not found in .env")

MODEL_NAME = "llama-3.3-70b-versatile"

client = Groq(api_key=API_KEY)