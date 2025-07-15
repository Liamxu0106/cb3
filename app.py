from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os

app = Flask(__name__)
CORS(app)  # 启用CORS，允许跨域访问

# 从环境变量读取你的OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json(silent=True)
    if not data or 'message' not in data:
        return jsonify({'error': 'No message provided.'}), 400

    user_input = data['message']

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",  # 可根据实际需求使用其他模型
            messages=[
                {"role": "system", "content": "You are a helpful assistant focused on climate change and sustainability."},
                {"role": "user", "content": user_input}
            ]
        )
        answer = response['choices'][0]['message']['content']
        return jsonify({'reply': answer})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)