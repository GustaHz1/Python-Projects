from flask import url_for, render_template, Flask, redirect, request
import pandas as pd

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def homepage():
    if request.method == 'POST':
        turno = request.form['turno']
        data = request.form['data']
        transportadora = request.form['transportadora']
        segmento = request.form['segmento']
        fornecedor = request.form['fornecedor']
        placa = request.form['placa']
        portaria = request.form['portaria']
        chegada_doca = request.form['chegada_doca']
        saida = request.form['saida']
        volume = request.form['volume']
        tipo = request.form['tipo']
        veiculo = request.form['veiculo']
        responsavel = request.form['responsavel']
        motorista = request.form['motorista']
        origem = request.form['origem']
        
        dados = {'Turno': [turno],
                 'Data': [data],
                 'Transportadora': [transportadora],
                 'Segmento': [segmento],
                 'Fornecedor': [fornecedor],
                 'Placa': [placa],
                 'Portaria': [portaria],
                 'Chegada_doca': [chegada_doca],
                 'Saida': [saida],
                 'Volume': [volume],
                 'Tipo': [tipo],
                 'Veiculo': [veiculo],
                 'Responsavel': [responsavel],
                 'Motorista': [motorista],
                 'Origem': [origem]}
        
        df = pd.DataFrame(dados)
        df.to_excel('Fornecedores.xlsx', index=False)
    

    return render_template("homepage.html")

@app.route("/teste")
def teste():
    return render_template("teste.html")

if __name__ == "__main__":
    app.run(debug=True)
