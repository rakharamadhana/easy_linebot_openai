# README

## English

### Description

This is a Flask application integrated with LINE Messaging API and OpenAI's GPT model to respond to user messages. The application can handle text messages, postback events, and member joins in a LINE group.

### Features

- Responds to text messages using OpenAI's GPT model.
- Handles postback events and prints the data for debugging.
- Welcomes new members to the LINE group.

### Prerequisites

- **Python 3.6+**
- **Flask**
- **LINE Messaging API credentials** (Channel Access Token and Channel Secret)
- **OpenAI API key**

### How to Deploy on Render.com

1. **Fork this repository**: 
   - Go to the GitHub repository page.
   - Click on the "Fork" button in the top-right corner.

2. **Create a new Web Service on Render**:
   - Go to [Render.com](https://render.com/).
   - Sign up or log in to your Render account.
   - Click on the "New" button and select "Web Service".

3. **Connect your GitHub repository**:
   - Choose "Connect to GitHub".
   - Select the forked repository from your GitHub account.

4. **Configure the Web Service**:
   - Set the **Name** for your service.
   - Select **Environment** as "Python".
   - Set the **Build Command** to `pip install -r requirements.txt`.
   - Set the **Start Command** to `python app.py`.

5. **Set Environment Variables**:
   - Click on "Advanced" and add the following environment variables:
     - `CHANNEL_ACCESS_TOKEN`: Your LINE channel access token.
     - `CHANNEL_SECRET`: Your LINE channel secret.
     - `OPENAI_API_KEY`: Your OpenAI API key.

6. **Deploy the Service**:
   - Click "Create Web Service" to start the deployment.
   - Render will automatically build and deploy your Flask application.

7. **Update LINE Messaging API Webhook URL**:
   - Go to the LINE Developers Console.
   - Set the webhook URL to your Render app URL, followed by `/callback` (e.g., `https://your-app-name.onrender.com/callback`).

### Usage

- Once deployed, the application will automatically respond to text messages sent to your LINE bot using OpenAI's GPT model.
- Postback events and new member joins will also be handled automatically.

---

## 繁體中文

### 說明

這是一個 Flask 應用程式，整合了 LINE Messaging API 和 OpenAI 的 GPT 模型，能夠回應使用者的訊息。該應用程式能夠處理文字訊息、postback 事件以及 LINE 群組中的新成員加入。

### 功能

- 使用 OpenAI 的 GPT 模型回應文字訊息。
- 處理 postback 事件並輸出資料以供除錯。
- 歡迎新成員加入 LINE 群組。

### 先決條件

- **Python 3.6+**
- **Flask**
- **LINE Messaging API 認證資訊**（頻道存取權杖和頻道密鑰）
- **OpenAI API 密鑰**

### 如何在 Render.com 部署

1. **分叉此儲存庫**：
   - 前往 GitHub 儲存庫頁面。
   - 點擊右上角的 "Fork" 按鈕。

2. **在 Render 上建立新的 Web 服務**：
   - 前往 [Render.com](https://render.com/)。
   - 註冊或登入您的 Render 帳戶。
   - 點擊 "New" 按鈕，選擇 "Web Service"。

3. **連接您的 GitHub 儲存庫**：
   - 選擇 "Connect to GitHub"。
   - 從您的 GitHub 帳戶中選擇分叉的儲存庫。

4. **配置 Web 服務**：
   - 為您的服務設定 **Name**（名稱）。
   - 選擇 **Environment**（環境）為 "Python"。
   - 設定 **Build Command**（建置命令）為 `pip install -r requirements.txt`。
   - 設定 **Start Command**（啟動命令）為 `python app.py`。

5. **設置環境變數**：
   - 點擊 "Advanced" 並新增以下環境變數：
     - `CHANNEL_ACCESS_TOKEN`: 您的 LINE 頻道存取權杖。
     - `CHANNEL_SECRET`: 您的 LINE 頻道密鑰。
     - `OPENAI_API_KEY`: 您的 OpenAI API 密鑰。

6. **部署服務**：
   - 點擊 "Create Web Service" 以開始部署。
   - Render 會自動建置並部署您的 Flask 應用程式。

7. **更新 LINE Messaging API Webhook URL**：
   - 前往 LINE 開發者控制台。
   - 將 webhook URL 設置為您的 Render 應用程式 URL，後面加上 `/callback`（例如，`https://your-app-name.onrender.com/callback`）。

### 使用方法

- 部署後，應用程式會自動回應發送到您 LINE 機器人的文字訊息，使用 OpenAI 的 GPT 模型。
- Postback 事件和新成員加入也會自動處理。
