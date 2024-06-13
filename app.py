from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)  # Serve para pegar as requisições no local do js

@app.route('/execute', methods=['POST'])
def execute_codigo():
    data = request.get_json()
    codigo = data.get('codigo')
    try:
        result = subprocess.run(
            ['python3', '-c', codigo],
            capture_output=True, text=True
        )
        output = result.stdout + result.stderr
    except Exception as e:
        output = f"Erro! {e}"
    return jsonify({'output': output})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
