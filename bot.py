from twilio.rest import Client
from flask import Flask, request
import requests
from g4f.client import Client as G4FClient
import logging
logging.basicConfig(level=logging.DEBUG)


# Twilio Credencials  (get from your account) 
account_sid = 'Sid'
auth_token = 'Token'
client = Client(account_sid, auth_token)

app = Flask(__name__)

def external_webhook_response(user_message):
    try:
        response = requests.post('https://ngrok', data={"Body": user_message}) #Endpoint using ngrok (configure the POST endpoint in TWILIO too)
        if response.status_code == 200:
            return response.text  
        else:
            return 'Houve um problema ao acessar o serviço do webhook.'
    except Exception as e:
        return f'Erro ao se conectar com o webhook externo: {str(e)}'


def gpt4free_response(user_message):
    try:
        gpt_client = G4FClient()  

        response = gpt_client.chat.completions.create(
            model="gpt-4o", #Chatgpt version
            messages=[{"role": "user", "content": user_message}]
        )
        
        return response.choices[0].message.content if response.choices else "Desculpe, não consegui entender sua solicitação."
    
    except Exception as e:
        return f'Erro ao se conectar com o serviço de IA: {str(e)}'

# Whatsapp route. remember to add /whatsapp in the end of your endpoint in twilio
@app.route('/whatsapp', methods=['POST'])
def whatsapp_reply():
    incoming_msg = request.values.get('Body', '').lower()  
    sender = request.values.get('From')  

    ai_response = gpt4free_response(incoming_msg)


    client.messages.create(
        body=ai_response,
        from_='whatsapp:+14155238886',  # Twilio's whatsapp number
        to=sender
    )

    return "OK", 200


if __name__ == '__main__':
    app.run(debug=True)
