from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

#====== Python Libraries ==========
import tempfile, os
import datetime
import openai
import time
import traceback
#====== Python Libraries ==========

# 初始化 Flask 網頁應用程式
# Initialize a Flask web application
app = Flask(__name__)

# 定義一個靜態臨時路徑來存儲檔案
# Define a static temporary path for storing files
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')

# 使用環境變數初始化 Line Bot API 和 Webhook 處理器來確保安全性
# Initialize Line Bot API and Webhook Handler with environment variables for security
line_bot_api = LineBotApi(os.getenv('CHANNEL_ACCESS_TOKEN'))  # Line API 存取令牌
handler = WebhookHandler(os.getenv('CHANNEL_SECRET'))         # Line API 頻道密鑰

# 從環境變數設定 OpenAI API 密鑰
# Set OpenAI API key from environment variables
openai.api_key = os.getenv('OPENAI_API_KEY')

# 定義函數從 OpenAI 的 GPT 模型獲取回應
# Function to get a response from OpenAI's GPT model
def GPT_response(text):
    response = openai.ChatCompletion.create(
        model="ft:gpt-4o-mini-2024-07-18:ppln-taipei:ntust-restaurant:9ybxSIIJ",  # 確保此模型名稱正確
        # Ensure this model name is correct
        messages=[
            {"role": "system", "content": "You are a helpful assistant providing menu information for NTUST."},
            # 系統訊息：您是一個提供 NTUST 菜單資訊的助手
            {"role": "user", "content": text},  # 使用者訊息
        ],
        temperature=0.5,  # 控制回應的隨機性，在確定性和隨機性之間取得平衡
        # Controls randomness in responses, a balance between deterministic and random
        max_tokens=500   # 限制生成回應的長度
        # Limits the length of the generated response
    )
    # 從 OpenAI 的 API 回應中提取回應文本
    # Extract the response text from OpenAI's API response
    answer = response['choices'][0]['message']['content']
    return answer

# 定義一個處理 POST 請求的 /callback 路由
# Define a route for handling POST requests to /callback
@app.route("/callback", methods=['POST'])
def callback():
    # 獲取 X-Line-Signature 標頭的值
    # Get the X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    
    # 獲取請求正文作為文本
    # Get the request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)  # 紀錄請求正文以便除錯
    # Log the request body for debugging
    
    # 使用處理器處理 webhook 正文
    # Handle webhook body using the handler
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)  # 如果簽名無效，則終止並返回 400 錯誤
        # If signature is invalid, abort with 400 error
    return 'OK'

# 事件處理程序用於處理傳入的訊息
# Event handler for incoming messages
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text  # 從傳入的訊息中獲取文本
    # Get the text from the incoming message
    try:
        GPT_answer = GPT_response(msg)  # 使用 GPT 生成回應
        # Generate a response using GPT
        print(GPT_answer)  # 將回應輸出到控制台
        # Print the response to the console
        line_bot_api.reply_message(event.reply_token, TextSendMessage(GPT_answer))  # 使用生成的回應回覆使用者
        # Reply to the user with the generated response
    except:
        print(traceback.format_exc())  # 輸出錯誤堆疊以便除錯
        # Print the error stack trace for debugging
        line_bot_api.reply_message(event.reply_token, TextSendMessage('您使用的 OPENAI API 密鑰可能已超出限制。請確認後臺日誌中的錯誤訊息。'))
        # 回覆使用者 API 密鑰使用量可能已超出，請檢查後臺日誌中的錯誤訊息。

# 事件處理程序用於處理 postback 動作
# Event handler for postback actions
@handler.add(PostbackEvent)
def handle_message(event):
    print(event.postback.data)  # 輸出 postback 資料以便除錯
    # Print the postback data for debugging

# 事件處理程序用於處理新成員加入群組
# Event handler for new members joining the group
@handler.add(MemberJoinedEvent)
def welcome(event):
    uid = event.joined.members[0].user_id  # 獲取新成員的使用者 ID
    # Get user ID of the new member
    gid = event.source.group_id  # 獲取成員加入的群組 ID
    # Get group ID where the member joined
    profile = line_bot_api.get_group_member_profile(gid, uid)  # 獲取新成員的個人資料
    # Get profile of the new member
    name = profile.display_name  # 獲取新成員的顯示名稱
    # Get the display name of the new member
    message = TextSendMessage(text=f'{name}, 歡迎加入群組！')  # 創建歡迎訊息
    # Create a welcome message
    line_bot_api.reply_message(event.reply_token, message)  # 向群組發送歡迎訊息
    # Send the welcome message to the group

# 應用程式的主入口點
# Main entry point for the application
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))  # 設定 Flask 應用程式的運行端口
    # Set the port for the Flask app to run on
    app.run(host='0.0.0.0', port=port)  # 啟動 Flask 應用程式
    # Start the Flask app
