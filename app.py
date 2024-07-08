from flask import Flask, render_template, redirect, url_for, request, jsonify
from main import *


app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template("index.html")


@app.route('/bot', methods=["POST", "GET"])
def bot():
    return render_template('bot.html')


chat_history = []


@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.json['message']
    chat_history.append(message)
    bot = chatbot(message)
    return jsonify({"bot":bot})


@app.route('/get_chat_history', methods=['GET'])
def get_chat_history():
    return jsonify(chat_history)


if __name__ == '__main__':
    app.run()

