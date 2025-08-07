import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Load Gemini API Key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("❌ GEMINI_API_KEY not set in environment.")

# Configure the API
genai.configure(api_key=GEMINI_API_KEY)

# Load Gemini model
model = genai.GenerativeModel('gemini-pro')

# ✅ Agent 3 - Generate code prompt from app info
def generate_code_prompt(app_info):
    return f"""Generate complete backend and frontend starter code for the following application idea:
    
{app_info}

Requirements:
- Use modern frameworks (React, Flask, Express, etc.)
- Organize code into modules
- Include comments
- Output code in markdown code blocks
"""

# ✅ Agent 3 - Get the generated code from Gemini
def generate_code_from_prompt(prompt):
    print("⏳ Generating code using Gemini...")
    response = model.generate_content(prompt)
    return response.text  # Gemini returns code in markdown format
