import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "sucesso",
        "mensagem": "Hello World do Flask rodando na Azure com CI/CD!"
    })

@app.route("/api/info", methods=["GET"])
def info():
    return jsonify({
        "ambiente": "Nuvem (Azure App Service)",
        "tecnologia": "Flask (Python)"
    })

if __name__ == "__main__":
    # A Azure injeta a variável de ambiente PORT automaticamente
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
