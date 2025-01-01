# config.py
from dotenv import load_dotenv
import os

load_dotenv()

# Replace 'your_gemini_api_key_here' with your actual API key.
class Config:
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
