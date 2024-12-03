from flask import Flask, request, jsonify

app = Flask(__name__)

# 预定义的 ChatBot 响应
responses = {
    "hello": "Hi there! How can I assist you?",
    "how are you": "I'm just a bot, but I'm functioning as expected. How about you?",
    "bye": "Goodbye! Have a great day!",
}

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message', '').lower()
    response = responses.get(user_input, "Sorry, I didn't understand that.")
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
