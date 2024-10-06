# WhatsApp AI Bot using Twilio, Flask, and GPT-4Free

This project implements a WhatsApp chatbot that uses Twilio for message handling, Flask for the server, and GPT-4Free to generate AI responses. The bot listens for messages sent to a WhatsApp sandbox and responds with intelligent replies based on the input message.

## Features

- Receive WhatsApp messages using Twilio’s API.
- Respond to messages using AI-based responses from GPT-4Free.
- Deployable using ngrok for local testing or any other hosting service.
  
## Prerequisites

Before running this project, ensure you have the following:

- Python 3.9 installed (minimum, might have to update to 3.12)
- A Twilio account with a configured WhatsApp sandbox
- Flask for handling the web server
- Ngrok for local testing or any other service to expose your local server
- GPT-4Free installed for AI responses

## Project Setup

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/MariaSan-tos/Whatsapp-BOT---GPT.git
    cd Whatsapp-BOT---GPT
    ```

2. **Create a Virtual Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install Dependencies**:
    Ensure that `pip` is up to date:
    ```bash
    pip install --upgrade pip
    ```
    Then install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure Twilio**:
    You will need your Twilio account SID, Auth Token, and the WhatsApp sandbox number. Replace these values in `bot.py`:

    ```python
    account_sid = 'YOUR_TWILIO_ACCOUNT_SID'
    auth_token = 'YOUR_TWILIO_AUTH_TOKEN'
    from_='whatsapp:+YOUR_TWILIO_WHATSAPP_SANDBOX_NUMBER'
    ```

5. **Run Flask App**:
    Start your Flask server:
    ```bash
    python bot.py
    ```

6. **Expose Localhost to Public (ngrok)**:
    Run ngrok to expose the Flask server:
    ```bash
    ngrok http 5000
    ```
    Copy the forwarding URL provided by ngrok (e.g., `https://xxxxxxxx.ngrok-free.app`).

7. **Configure Twilio Webhook**:
    In your Twilio console, set the **"When a message comes in"** webhook URL to:
    ```
    https://xxxxxxxx.ngrok-free.app/whatsapp
    ```
    Make sure the HTTP method is `POST`.

8. **Test the Bot**:
    Now, send a message to your Twilio WhatsApp sandbox number. The bot will respond with AI-generated replies based on your input.

## File Structure

```
.
├── bot.py                 # Main Flask application and Twilio logic
├── requirements.txt       # Dependencies for the project
└── README.md              # Project documentation
```

## Dependencies

The required dependencies are listed in the `requirements.txt` file. Key libraries include:

- `Flask`: For handling the web server.
- `Twilio`: For interacting with the WhatsApp API.
- `requests`: For making HTTP requests (used for interacting with GPT-4Free).
- `g4f`: Client for GPT-4Free (if implemented).

To install all dependencies, use:

```bash
pip install -r requirements.txt
```

## Environment Variables (Optional)

You can use environment variables to store sensitive data such as Twilio credentials. Create a `.env` file in the root of the project and add the following:

```bash
TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
```

Load these variables in your Python script using `python-dotenv`:
```python
from dotenv import load_dotenv
load_dotenv()

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
```

## Troubleshooting

- **502 Bad Gateway on ngrok**: Ensure your Flask server is running on port 5000 and the webhook URL in Twilio matches the ngrok forwarding address.
- **No Response from Bot**: Check the Twilio logs in the console for errors and ensure the Flask server logs show incoming messages.
- **Missing `curl_cffi` error**: Install the missing module with:
    ```bash
    pip install curl_cffi
    ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
