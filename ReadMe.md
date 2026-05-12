# AI-Powered MCQ Generator using FastAPI and Gemini AI

An end-to-end Generative AI project built using **FastAPI** and **Google Gemini API** that dynamically generates Multiple Choice Questions (MCQs) based on a given topic and experience level.

This project demonstrates the integration of:
- FastAPI backend development
- Generative AI APIs
- Prompt Engineering
- JSON response handling
- REST API creation
- Environment variable management
- Structured AI-generated outputs

---

# Project Overview

This application allows users to generate AI-powered MCQs by providing:
- Topic name
- Experience level
- Number of questions required

The system uses Google's Gemini model to dynamically create structured MCQs in JSON format.

---

# Features

- Generate MCQs dynamically using Generative AI
- Experience-based difficulty levels
- FastAPI REST API integration
- Gemini AI integration using both:
  - Old SDK (`google-generativeai`)
  - New SDK (`google-genai`)
- JSON formatted AI responses
- Environment variable configuration using `.env`
- Automatic API documentation with Swagger UI
- Clean project structure

---

# Tech Stack

| Technology | Purpose |
|---|---|
| Python | Programming Language |
| FastAPI | Backend API Framework |
| Gemini API | Generative AI Model |
| Google Generative AI SDK | Old Gemini SDK |
| Google GenAI SDK | New Gemini SDK |
| Uvicorn | ASGI Server |
| dotenv | Environment Variable Management |

---

# Project Structure

```bash
FastAPI/
│
├── env/
├── .env
├── main.py
├── utils.py
├── requirements.txt
└── README.md
```

---

# Installation and Setup

## Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
```

---

## Step 2: Move into the Project Directory

```bash
cd your-repo-name
```

---

## Step 3: Create Virtual Environment

### Windows

```bash
python -m venv env
```

### Mac/Linux

```bash
python3 -m venv env
```

---

## Step 4: Activate Virtual Environment

### Windows

```bash
env\Scripts\activate
```

### Mac/Linux

```bash
source env/bin/activate
```

---

## Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the root directory.

```env
GOOGLE_API_KEY=YOUR_API_KEY
MODEL_NAME=gemini-2.5-flash-lite
```

---

# Generate Gemini API Key

1. Visit Google AI Studio
2. Create an API Key
3. Copy the API key
4. Paste it inside the `.env` file

---

# Requirements

```txt
fastapi[standard]
google-generativeai
python-dotenv
google-genai
```

---

# Running the Application

Run the FastAPI server using:

```bash
uvicorn main:app --reload
```

---

# Access the Application

## Local Server

```bash
http://127.0.0.1:8000
```

---

# Swagger API Documentation

FastAPI automatically generates API documentation.

Open:

```bash
http://127.0.0.1:8000/docs
```

---

# API Endpoints

# 1. Root Endpoint

## Endpoint

```http
GET /
```

## Response

```json
{
  "Hello": "Students",
  "message": "We are going to learn FastAPI"
}
```

---

# 2. Item Endpoint

## Endpoint

```http
GET /items/{item_id}
```

## Example

```http
GET /items/1?q=python
```

## Response

```json
{
  "item_id": 1,
  "q": "python"
}
```

---

# 3. Country Capital Generator using Gemini AI

## Endpoint

```http
GET /country/{country_name}
```

## Example

```http
GET /country/India?sdk_type=NEW
```

## Response

```json
{
  "country": "India",
  "capital": "New Delhi"
}
```

---

# 4. AI MCQ Generator Endpoint

## Endpoint

```http
GET /generate-mcq/{topic}/{experience}/{questions_limit}
```

## Example

```http
GET /generate-mcq/python/2/5?sdk_type=NEW
```

---

# Parameters

| Parameter | Description |
|---|---|
| topic | Topic for MCQ generation |
| experience | Experience level in years |
| questions_limit | Number of questions required |
| sdk_type | OLD or NEW Gemini SDK |

---

# Example Response

```json
[
  {
    "1": {
      "question": "What is Python?",
      "options": [
        {
          "a": "Programming Language",
          "b": "Database",
          "c": "Cloud Service",
          "d": "Operating System",
          "answer": "a"
        }
      ]
    }
  }
]
```

---

# Difficulty Levels Logic

The application dynamically determines the difficulty level using experience.

| Experience | Difficulty |
|---|---|
| 0-2 Years | Beginner |
| 3-5 Years | Intermediate |
| 5+ Years | Advanced |

---

# Prompt Engineering Used

The project uses prompt engineering to enforce:
- JSON-only output
- Structured MCQ format
- Controlled difficulty level
- Exactly 4 options
- Single correct answer

Example Prompt:

```python
Generate 5 multiple choice questions (MCQs) about Python for a beginner level audience.
Each question must have exactly 4 options (a, b, c, d) and only one correct answer key.
The complexity should match with 2 years of experience.
Return the output in JSON format only.
```

---

# SDKs Used

## Old Gemini SDK

```python
import google.generativeai as google_genai
```

---

## New Gemini SDK

```python
from google import genai
```

---

# JSON Cleaning Logic

The project includes a utility function to clean AI-generated responses.

```python
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
```

This helps remove markdown wrappers generated by LLMs.

---

# Project Workflow

```text
User Request
     ↓
FastAPI Endpoint
     ↓
Prompt Creation
     ↓
Gemini API Call
     ↓
AI Generated JSON Response
     ↓
JSON Cleaning
     ↓
API Response to User
```

---

# Key Learnings from this Project

- FastAPI fundamentals
- REST API development
- Generative AI integration
- Gemini API usage
- Prompt engineering
- Environment variable handling
- JSON parsing
- Structured AI outputs
- API testing using Swagger

---

# Future Improvements

- Add Pydantic models
- Add async support
- Add error handling
- Add retry logic
- Add logging system
- Add authentication
- Add frontend integration
- Store MCQs in database
- Add export to PDF/Excel
- Add topic-wise analytics
- Add difficulty customization
- Deploy on Render/AWS/GCP

---

# Possible Use Cases

- Interview preparation platform
- AI-based learning systems
- Quiz generation platforms
- Educational applications
- Technical assessment systems
- EdTech products

---

# Common Errors and Fixes

## 1. API Key Error

### Error

```bash
KeyError: GOOGLE_API_KEY
```

### Fix

Check `.env` file and ensure:

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

---

## 2. JSON Decode Error

### Error

```bash
json.decoder.JSONDecodeError
```

### Cause

Gemini returned markdown-wrapped JSON.

### Fix

Use `clean_json_response()` before `json.loads()`.

---

## 3. Uvicorn Not Found

### Fix

```bash
pip install "fastapi[standard]"
```

---

# Security Note

Do NOT upload your `.env` file to GitHub.

Add this to `.gitignore`:

```gitignore
.env
env/
__pycache__/
```

---

# Author

## Mohit Raj

B.Tech CSE Graduate | Data Analytics & Generative AI Enthusiast

---

# Connect with Me

## LinkedIn

```text
Add your LinkedIn profile here
```

## GitHub

```text
Add your GitHub profile here
```

---

# License

This project is for educational and learning purposes.

---

# Final Output

This project demonstrates how Generative AI can be integrated with FastAPI to create dynamic AI-powered backend applications capable of generating structured educational content in real-time.
