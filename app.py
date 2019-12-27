import os
from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
import json
import main

app = Flask(__name__)
api = Api(app)
CORS(app)

@app.route("/")
def index():
    return "<h1>APICheckPWC</h1>"

class validarArquivo(Resource):
    def post(self):
        #print(request.json)
        print("@@@@@@@@@@@@@@@@@@@@@@@@")
        #print(dir(request.data))
        retorno = main.ExecutaCheck(request.data)
        print(retorno)
        print("@@@@@@@@@@@@@@@@@@@@@@@@")
        #print(request.data)
        return retorno

api.add_resource(validarArquivo, '/validar')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(threaded=True, port=port)
