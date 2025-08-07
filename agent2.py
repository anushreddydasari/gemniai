import os
from dotenv import load_dotenv
import google.generativeai as genai

# ✅ Load environment variables from .env
load_dotenv()

# ✅ Get the Gemini API key from the environment
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("❌ GEMINI_API_KEY not set in environment.")

# ✅ Configure the Gemini API
genai.configure(api_key=GEMINI_API_KEY)

# ✅ Use Gemini model
model = genai.GenerativeModel('gemini-pro')

# ✅ Agent 2 - UI prompt generator
def generate_ui_prompt(app_info):
    return f"""Generate a beautiful and modern UI design idea for this app:
    
{app_info}

The design should include:
- Header / Navbar
- Main content area
- User interaction section (buttons, inputs, etc.)
- Responsive layout
- Suggested colors and themes"""

# ✅ Agent 2 - Generate UI image
def generate_ui_image(prompt):
    print("⏳ Generating UI image using Gemini...")
    response = model.generate_content(prompt)
    return response.text  # This is usually a design description, not an actual image
