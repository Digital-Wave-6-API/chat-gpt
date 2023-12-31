from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)

# Configuração da chave da API
openai.api_type = "azure"
openai.api_base = "https://interactai.openai.azure.com/"
openai.api_version = "2023-05-15"
openai.api_key = "66a6b8c8d3c449d4b53fa75d09b04366"

@app.route('/ask', methods=['POST'])
def ask_question():
    try:
        data = request.json
        user_message = data['user_message']

        response = openai.ChatCompletion.create(
            engine="modelgpt35t",
            messages=[
               
                {"role": "user", "content": user_message},
            ]
        )

        last_message = response['choices'][0]['message']['content']

        return jsonify({"response": last_message})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
