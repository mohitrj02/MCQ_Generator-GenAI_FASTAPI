from fastapi import FastAPI

from dotenv import load_dotenv
load_dotenv()

from utils import generate_gemini_response, generate_gemini_response_new_sdk, get_difficulty
import json
from enum import Enum
from typing import List, Dict, Optional

app = FastAPI()

class SDKType(Enum):
    OLD = "old"
    NEW = "new"

@app.get("/")
def read_root():
    return {"Hello": "Students", "message": "We are going to learn FastAPI"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@app.get("/country/{country_name}")
def get_country_capital(country_name: str, sdk_type: Optional[SDKType] = None) -> dict:
    prompt = (
        f"What is the capital of {country_name}? "
        'Return ONLY a JSON object in this exact format: {"capital": "CityName"}'
    )
    if sdk_type == SDKType.OLD:
        response = json.loads(generate_gemini_response(prompt))
    elif sdk_type == SDKType.NEW:
        response = json.loads(generate_gemini_response_new_sdk(prompt))
    else:
        return {"error": "No SDK selected, please select one."}
    return {"country": country_name, "capital": response["capital"]}

@app.get("/generate-mcq/{topic}/{experience}/{questions_limit}")
def generate_mcq(topic: str, experience: int, questions_limit: int, sdk_type: Optional[SDKType] = None) -> List[Dict] | Dict:
    
    difficulty = get_difficulty(int(experience))

    prompt = f"""
    Generate {questions_limit} multiple choice questions (MCQs) about {topic} for a {difficulty} level audience.
    Each question must have exactly 4 options (a, b, c, d) and only one correct answer key.
    The complexity should match with {experience} years of experience.
    I need the output in a list of json.
    Example structure:
    [
        {{
            "1": {{
                "question": "Your Question",
                "options": [
                    {{
                    "a": "First Option",
                    "b": "Second Option",
                    "c": "Third Option",
                    "d": "Fourth Option",
                    "answer": "Correct Option among a, b, c, d"
                    }}
                ]
            }}
        }}
    ]
    """
    if sdk_type == SDKType.OLD:
        response = generate_gemini_response(prompt)
    elif sdk_type == SDKType.NEW:
        response = generate_gemini_response_new_sdk(prompt)
    else:
        return {"error": "No SDK selected, please select one."}
    return json.loads(response)