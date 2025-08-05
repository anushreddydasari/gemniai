import requests
import json

GEMINI_API_KEY = "AIzaSyCMO28d7v8lI8W9VIOL-ENdMmlw9okPoJw"
GEMINI_ENDPOINT = f"https://generativelanguage.googleapis.com/v1/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"
HEADERS = {"Content-Type": "application/json"}

def generate_app_logic_code(app_idea):
    prompt = f"""
You are a senior software engineer. Given the app idea "{app_idea}", write the core logic code in Python or JavaScript (whichever fits best) that includes:

- Basic functionality
- Comments
- Proper formatting

Only output code. Do NOT include explanation.
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
        return f"❌ Agent 3 Gemini error {response.status_code}: {response.text}"

    try:
        return response.json()["candidates"][0]["content"]["parts"][0]["text"]
    except (KeyError, IndexError):
        return "⚠️ Agent 3: Unexpected Gemini response structure."
