from flask import Flask, request, jsonify, render_template
import responses

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')

    if user_message:
        bot_response = responses.get_response(user_message)
        return jsonify({'response': bot_response})
    return jsonify({'response': 'Please provide a message.'}), 400

if __name__ == '__main__':
    app.run(debug=True)
