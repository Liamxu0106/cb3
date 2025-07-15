# app.py - Flask后端示例代码
import os, openai
from flask import Flask, request, jsonify
from flask_cors import CORS

openai.api_key = os.getenv("OPENAI_API_KEY")  # 从环境变量读取API密钥 [oai_citation:2‡community.render.com](https://community.render.com/t/unable-to-access-api-key/12752#:~:text=The%20only%20thing%20I%20can,your%20code%20with%20something%20like)

app = Flask(__name__)
CORS(app)  # 允许跨域请求，便于前端页面调用 [oai_citation:3‡rapidapi.com](https://rapidapi.com/guides/handle-cors-flask#:~:text=from%20flask%20import%20Flask)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_msg = data.get("message", "")  # 获取用户消息文本
    try:
        # 调用OpenAI的ChatGPT模型获取回答
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[ {"role": "user", "content": user_msg} ]
        )
        reply_text = response['choices'][0]['message']['content']
    except Exception as e:
        # 如API调用出错，返回错误提示
        reply_text = "（抱歉，AI暂时无法回答问题。）"
    return jsonify({ "reply": reply_text })
