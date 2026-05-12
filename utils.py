import json
from dotenv import load_dotenv
load_dotenv()

import google.generativeai as google_genai
from google import genai
from google.genai import types
import os

print("API KEY LOADED:", bool(os.environ.get("GOOGLE_API_KEY")))
print("MODEL NAME:", os.environ.get("MODEL_NAME", "gemini-2.5-flash-lite"))

MODEL_NAME = os.getenv("MODEL_NAME", "gemini-2.5-flash-lite")

def clean_json_response(response_text):
    response_text = response_text.strip()

    if response_text.startswith("```json"):
        response_text = (
            response_text
            .replace("```json", "")
            .replace("```", "")
            .strip()
        )

    return response_text

def generate_gemini_response(prompt):
    google_genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
    generation_config = {
        "response_mime_type": "application/json"
    }
    model=google_genai.GenerativeModel(
        model_name = MODEL_NAME,
        generation_config= generation_config
    )
    response = model.generate_content(prompt)
    return clean_json_response(response.text)

def generate_gemini_response_new_sdk(prompt):
    client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])
    generate_content_config = types.GenerateContentConfig(
        temperature=0.2,
        response_mime_type="application/json"
    )
    response = client.models.generate_content(
        model = MODEL_NAME,
        contents = prompt,
        config = generate_content_config
    )
    return clean_json_response(response.text)

def get_difficulty(experience):
    if experience >= 3 and experience <= 5:
        return "intermediate"
    elif experience > 5:
        return "advanced"
    return "beginner"