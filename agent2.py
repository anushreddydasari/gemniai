# agent2.py
import requests
import json

GEMINI_API_KEY = "AIzaSyCMO28d7v8lI8W9VIOL-ENdMmlw9okPoJw"
GEMINI_ENDPOINT = f"https://generativelanguage.googleapis.com/v1/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"
HEADERS = {"Content-Type": "application/json"}

def generate_ui_prompt(app_idea):
    prompt = f"""
You are a UI designer. Given the app idea "{app_idea}", generate a short prompt for an image generation model like DALL·E to create a UI mockup.

Only output the image prompt. Do NOT include explanations.
Example: "Modern mobile UI design for a food delivery app with product cards, clean layout, light colors"
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
        return f"❌ Agent 2 Gemini error {response.status_code}: {response.text}"

    try:
        return response.json()["candidates"][0]["content"]["parts"][0]["text"]
    except (KeyError, IndexError):
        return "⚠️ Agent 2: Unexpected Gemini response structure."


def generate_ui_image(prompt):
    # Since you're using only Gemini, simulate the image (replace with actual image API if needed)
    return f"https://dummyimage.com/1024x1024/cccccc/000000.png&text={prompt.replace(' ', '+')}"
