from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Random Joke API!"

@app.route("/joke", methods=["GET"])
def get_joke():
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    joke = response.json()
    return jsonify({"setup": joke["setup"], "punchline": joke["punchline"]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
