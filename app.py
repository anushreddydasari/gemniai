# app.py
from flask import Flask, render_template, request
from agent1 import generate_app_info
from agent2 import generate_ui_prompt, generate_ui_image
from agent3 import generate_app_logic_code

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    app_idea = ""
    agent1_output = ""
    agent2_prompt = ""
    agent2_image_url = ""
    agent3_code = ""

    if request.method == "POST":
        app_idea = request.form["app_idea"]

        # Agent 1: Generate tech stack, MVP, and features
        agent1_output = generate_app_info(app_idea)

        # Agent 2: Generate UI image prompt and image
        agent2_prompt = generate_ui_prompt(app_idea)
        if not agent2_prompt.startswith("\u274c") and not agent2_prompt.startswith("\u26a0\ufe0f"):
            agent2_image_url = generate_ui_image(agent2_prompt)

        # Agent 3: Generate core logic code
        agent3_code = generate_app_logic_code(app_idea)

    return render_template("index.html",
                           app_idea=app_idea,
                           agent1_output=agent1_output,
                           agent2_prompt=agent2_prompt,
                           agent2_image_url=agent2_image_url,
                           agent3_code=agent3_code)

if __name__ == "__main__":
    app.run(debug=True)
