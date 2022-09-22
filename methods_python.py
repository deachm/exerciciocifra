from flask import Flask, request
import requests
import json
import random
from criptografar_decriptografar import cifra_cesar_criptografa

app = Flask(__name__)


@app.route("/getCifra", methods=["GET"])
def getcifra():
    chave = random.randint(1,47)
    requisicao = requests.get('https://dog-api.kinduff.com/api/facts')
    cifra = json.loads(requisicao.content)
    cifra_str = cifra['facts']
    print (cifra_str [0]) #apenas para verificar a frase recebida da API
    cifra_criptografa = cifra_cesar_criptografa(cifra_str[0],chave,1)
    return {
        'cifra criptografada': cifra_criptografa, 
        'chave para decriptografar': chave,
        }

@app.route("/resolveCifra", methods =["POST"])
def resolvecifra():
    parametros_teste = request.get_json()
    cifra_criptografa = parametros_teste['cifra criptografada']
    chave = parametros_teste['chave para decriptografar']
    cifra_resolvida = cifra_cesar_criptografa(cifra_criptografa,chave,2) #decriptografando
    return cifra_resolvida

    
if __name__=="__main__":
    app.run(debug=True)


