from flask import Flask, jsonify, request
from dotenv import load_dotenv
from flask_cors import CORS
import os, requests, json
from openai_utils import get_response

load_dotenv()
app = Flask(__name__)
CORS(app)

api_key = os.environ['TOKEN']
print(api_key)

@app.route("/")
def index():
    return "Welcome to the chatbot API"


@app.route(f"/api/v1/{api_key}", methods=['POST'])
def message():
    data = request.get_json()
    user_message = data["message"]

    chatbot_response = get_response(user_message)

    return jsonify({"message": chatbot_response})


if __name__ == '__main__':
    app.run(debug=False)
