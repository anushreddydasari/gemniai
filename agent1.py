# agent1.py
import requests
import json

GEMINI_API_KEY = "AIzaSyCMO28d7v8lI8W9VIOL-ENdMmlw9okPoJw"
GEMINI_ENDPOINT = f"https://generativelanguage.googleapis.com/v1/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"
HEADERS = {"Content-Type": "application/json"}

def generate_app_info(app_name):
    prompt = f"""
You are a software architect. For the application idea: "{app_name}", generate the following:

1. Tech Stack (Frontend, Backend, Database, Hosting)
2. MVP (Minimum Viable Product - 4 to 6 points)
3. Features (4 to 6 main features)

Return the output in clear bullet format.
"""

    data = {
        "contents": [
            {
                "role": "user",
                "parts": [{"text": prompt}]
            }
        ]
    }

    response = requests.post(GEMINI_ENDPOINT, headers=HEADERS, data=json.dumps(data))

    if response.status_code != 200:
        return f"❌ Agent 1 Gemini error {response.status_code}: {response.text}"

    try:
        return response.json()["candidates"][0]["content"]["parts"][0]["text"]
    except (KeyError, IndexError):
        return "⚠️ Agent 1: Unexpected Gemini response structure."
