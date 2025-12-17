from flask import Flask, render_template, request, jsonify
from chatbot import ChatBot

app = Flask(__name__)
bot = ChatBot("data/responses.json")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_response():
    user_input = request.json.get("msg")
    response = bot.get_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
