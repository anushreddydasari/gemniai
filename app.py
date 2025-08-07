from flask import Flask, request, jsonify, render_template
from agent1 import generate_agent1_response
from agent2 import generate_ui_prompt, generate_ui_image
from agent3 import generate_code_prompt

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/agent1/generate', methods=['POST'])
def agent1_generate():
    input_data = request.form.get('input') or request.json.get('input')
    output = generate_agent1_response(input_data)
    return jsonify({"response": output})

@app.route('/api/agent2/generate', methods=['POST'])
def agent2_generate():
    app_info = request.form.get('app_info') or request.json.get('app_info')
    prompt = generate_ui_prompt(app_info)
    image_url = generate_ui_image(prompt)
    return jsonify({"prompt": prompt, "image_url": image_url})

@app.route('/api/agent3/generate', methods=['POST'])
def agent3_generate():
    app_info = request.form.get('app_info') or request.json.get('app_info')
    code = generate_code_prompt(app_info)
    return jsonify({"code": code})

if __name__ == '__main__':
    print("✅ AI Agent App is running! Use POST on /api/agent1/generate, /api/agent2/generate, /api/agent3/generate")
    app.run(debug=True)
