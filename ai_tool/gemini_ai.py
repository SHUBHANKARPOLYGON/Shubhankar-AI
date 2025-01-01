# ai_tool/gemini_ai.py
import textwrap
from gtts import gTTS
import google.generativeai as genai

def configure_api(api_key):
    genai.configure(api_key=api_key)

def generate_answer(model_name, question):
    model = genai.GenerativeModel(model_name)
    prompt = f"Hey Gemini, give me an answer to this question: {question} in maximum 500 words."
    response = model.generate_content(prompt)
    return response.text
