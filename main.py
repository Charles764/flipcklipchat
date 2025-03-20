from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os

app = Flask(__name__)
CORS(app)  # Allows frontend requests from different domains

# Load API key from Render environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

# Home route (for testing)
@app.route("/", methods=["GET"])
def home():
    return "Chatbot API is running!", 200

# Chatbot route
@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.json
        user_message = data.get("message", "")

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": user_message}]
        )

        reply = response["choices"][0]["message"]["content"]
        return jsonify({"reply": reply})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
