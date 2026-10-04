import os
import google.generativeai as genai
from flask import Flask, request, jsonify


app = Flask(__name__)


GENAI_API_KEY = "YOUR_API_KEY_HERE"
genai.configure(api_key=GENAI_API_KEY)


generation_config = {
  "temperature": 0.7,
  "top_p": 0.9,
  "max_output_tokens": 150, 
}


system_instruction = """You are a strict technical interviewer at a top tech company. 
The candidate is a B.Tech CSE student. 
Your job is to test them on C++ Data Structures and Python.
Rules:
1. Always rate the candidate's previous answer out of 10.
2. Give a 1-sentence feedback.
3. Ask the next technical question.
4. Keep the total response under 3 sentences so it is easy to read out loud."""

model = genai.GenerativeModel(
  model_name="gemini-pro",
  generation_config=generation_config,
  system_instruction=system_instruction,
)


chat_session = model.start_chat(history=[])

@app.route('/')
def home():
    return "🚀 PrepPilot AI Backend is Live on Localhost!"

@app.route('/ask', methods=['POST'])
def ask_interviewer():
    data = request.get_json()
    user_answer = data.get("answer", "Hello, I am ready for my technical interview.")
    
    try:
        
        response = chat_session.send_message(user_answer)
        return jsonify({
            "status": "success", 
            "bot_reply": response.text
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    
    app.run(port=5000, debug=True)