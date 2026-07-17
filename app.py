#Importando os frameworks Necessários
from flask import Flask,request,jsonify
from flask_cors import CORS
from sklearn.linear_model import LinearRegression
import pandas as pd
from supabase import create_client
from dotenv import load_dotenv
import os

load_dotenv()

tabela = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY"),
)

#Habilitando a execução da API
app = Flask(__name__)
CORS(app)

#Realizando a leitura do dataset
df = pd.read_csv("dataset_carros_usados_2.csv")

#Separando dados de treinamento
X = df[["ano","quilometragem","motor","num_revisoes"]]
y = df["preco"]

#Treinando o modelo
modelo = LinearRegression()
modelo.fit(X,y)

#Criando os métodos e rotas
@app.route("/",methods=["GET"])
def inicio():
    return jsonify({
       
        "Resposta":"API online, Flask rodando forma correta"
       
        })
   
@app.route("/prever",methods=["POST"])
def prever():
    try:
        dados = request.get_json()
        carro = pd.DataFrame({
            "ano":[dados["ano"]],
            "quilometragem":[dados["quilometragem"]],
            "motor":[dados["motor"]],
            "num_revisoes":[dados["num_revisoes"]]
        })
        preco = modelo.predict(carro)[0]
        preco_formatado = round(float(preco),2)
        #-----BANCO DE DADOS-----
        registros = {
            "ano":dados["ano"],
            "quilometragem":dados["quilometragem"],
            "motor":dados["motor"],
            "num_revisoes":dados["num_revisoes"],
            "preco":preco_formatado
        }
        tabela.table("historico_previsoes").insert(registros).execute()
        
  
        
        return jsonify({"preco":round(float(preco),2)})
   
    except Exception as erro:
        return jsonify({
           
            "erro":f"Erro:{str(erro)}"
                       
                        })
       
#Iniciar a API
if __name__ == '__main__':
    app.run(port=8000,host="0.0.0.0",debug=True)