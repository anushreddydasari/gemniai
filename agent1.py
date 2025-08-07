def generate_agent1_response(app_idea):
    if not app_idea:
        return "❗ No idea provided. Please enter an application idea."

    # Simple example of how the response could vary by keywords
    idea = app_idea.lower()
    
    if "restaurant" in idea:
        tech_stack = "React (Frontend), Node.js (Backend), MongoDB (Database)"
        mvp = "- Digital menu\n- Table QR scanner\n- Order placement"
        dev_plan = "- UI for menu browsing\n- Backend for order processing\n- MongoDB schema for orders & menu"
    elif "chat" in idea or "messaging" in idea:
        tech_stack = "Flutter (Cross-platform), Firebase (Backend & Auth)"
        mvp = "- One-on-one chat\n- Notifications\n- User login/signup"
        dev_plan = "- Flutter UI\n- Firebase setup for auth & Firestore\n- Push notifications config"
    else:
        tech_stack = "React (Frontend), Express.js (Backend), PostgreSQL (Database)"
        mvp = "- Basic CRUD\n- User auth\n- Responsive design"
        dev_plan = "- Frontend UI setup\n- REST API with Express\n- DB models with PostgreSQL"

    return f"""
🤖 Agent 1: App Idea Analysis for: **{app_idea}**

🔧 Tech Stack:
{tech_stack}

🎯 MVP Features:
{mvp}

🛠 Development Plan:
{dev_plan}
"""
import requests
import json 