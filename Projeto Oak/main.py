from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = "bd166146129be2560c92b30b928b0466"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///comunidade.db"

database = SQLAlchemy(app)

produto_cadastrado = {}

class Produto(database.Model):
    id =  database.Column(database.Integer, primary_key = True)
    nome =  database.Column(database.String(150), nullable = False)
    descricao =  database.Column(database.String(150), nullable = False)
    valor =  database.Column(database.Float, nullable = False)
    disponibilidade =  database.Column(database.String(20), nullable = False)

class Cadastro(FlaskForm):
    nome = StringField("Nome do produto", validators=[DataRequired()])
    descricao = StringField("Descrição do produto", validators=[DataRequired()])
    valor = DecimalField("Valor do produto", validators=[DataRequired()])
    disponibilidade = StringField("Possivel venda SIM ou NÃO", validators=[DataRequired()])
    botao = SubmitField("Cadastrar")


@app.route("/", methods=["GET", "POST"])
def homepage():
    form_cadastro = Cadastro()
    if form_cadastro.validate_on_submit():
        # Cria o produto com os dados do formulário
        novo_produto = Produto(
            nome = form_cadastro.nome.data,
            descricao = form_cadastro.descricao.data,
            valor = form_cadastro.valor.data,
            disponibilidade = form_cadastro.disponibilidade.data
        )
            
        database.session.add(novo_produto)
        database.session.commit()
        
        return redirect(url_for("exibir"))
        
    return render_template("homepage.html", form=form_cadastro)

@app.route("/exibir")
def exibir():
    # Busca todos os produtos
    produtos = Produto.query.all() 
    return render_template("pagina.html", produtos=produtos)


if __name__ == "__main__":
    with app.app_context():
        # Cria as tabelas no banco de dados
        database.create_all()
    app.run(debug=True)
