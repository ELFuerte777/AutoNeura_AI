from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Cambia esto por tu URL pública de ngrok cuando expongas tu PC
PC_URL = "https://TU-NGROK-ID.ngrok.io/recibir_cuestionario"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/enviar_cuestionario', methods=['POST'])
def enviar_cuestionario():
    data = request.get_json()
    try:
        # Reenvía los datos a tu PC
        resp = requests.post(PC_URL, json=data, timeout=10)
        return jsonify({"ok": True, "respuesta_pc": resp.json()})
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)
