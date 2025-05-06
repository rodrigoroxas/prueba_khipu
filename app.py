import os
import requests
from flask import Flask, request, jsonify, send_from_directory
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, static_folder='static')

API_KEY = os.getenv("KHIPU_API_KEY")
HEADERS = {
    "Content-Type": "application/json",
    "x-api-key": API_KEY
}

BASE_URL = "https://payment-api.khipu.com/v3"

@app.route('/bancos', methods=['GET'])
def listar_bancos():
    response = requests.get(f"{BASE_URL}/banks", headers=HEADERS)
    return jsonify(response.json()), response.status_code

@app.route('/crear-cobro', methods=['POST'])
def crear_cobro():
    data = request.json
    payload = {
        "amount": float(data.get("amount", 1000)),
        "currency": "CLP",
        "subject": "Cobro de prueba",
        "transaction_id": "demo-" + data.get("transaction_id", "001"),
        "payer_email": data.get("payer_email", "cliente@correo.com"),
        "bank_id": data.get("bank_id", ""),
        "return_url": "http://localhost:5000/ok",
        "cancel_url": "http://localhost:5000/cancelado",
        "body": "Este es un cobro de prueba para entrevista"
    }

    response = requests.post(f"{BASE_URL}/payments", headers=HEADERS, json=payload)
    return jsonify(response.json()), response.status_code

@app.route('/estado-cobro/<payment_id>', methods=['GET'])
def estado_cobro(payment_id):
    response = requests.get(f"{BASE_URL}/payments/{payment_id}", headers=HEADERS)
    return jsonify(response.json()), response.status_code

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/ok')
def ok():
    return "✅ Pago completado exitosamente."

@app.route('/cancelado')
def cancelado():
    return "❌ Pago cancelado por el usuario."

if __name__ == '__main__':
    app.run(debug=True)
