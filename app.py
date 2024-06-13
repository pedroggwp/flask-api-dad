from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app) #Serve pra pegar as requisições no local do js

#Definindo uma "rota" para as requisições
@app.route('/execute', methods=['POST'])
def execute_codigo():
    # Pegando as informações do json
    data = request.get_json()
    codigo = data.get('codigo')
    try:
        # Rodando o codigo pego na requisiçãop
        result = subprocess.run(
            ['python3', '-c', codigo],
            # pegando a saida e indicando como string
            capture_output=True, text=True
        )
        # Se o retorno for um erro, juntando o retorno com o erro
        output = result.stdout + result.stderr
    except Exception as e:
        output = f"Erro! {e}"
    # Retornando a saida como objeto json
    return jsonify({'output': output})

# rodando o flask
if __name__ == '__main__':
    app.run()
