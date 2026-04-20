from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)
OLLAMA_URL = 'http://localhost:11434/api/generate'
MODEL_NAME = 'medical-chatbot'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '').strip()
    if not user_message:
        return jsonify({'error': 'Empty message'}), 400
    try:
        response = requests.post(OLLAMA_URL, json={
            'model': MODEL_NAME,
            'prompt': user_message,
            'stream': False
        }, timeout=300)
        bot_reply = response.json().get('response', 'No response')
    except Exception as e:
        bot_reply = f'Error: {str(e)}'
    return jsonify({'response': bot_reply})

@app.route('/health')
def health():
    return jsonify({'status': 'ok', 'model': MODEL_NAME})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
