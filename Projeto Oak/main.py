from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config["SECRET_KEY"] = "bd166146129be2560c92b30b928b0466"

produto_cadastrado = {}

class Cadastro(FlaskForm):
    nome = StringField("Nome do produto", validators=[DataRequired()])
    descricao = StringField("Descrição do produto", validators=[DataRequired()])
    valor = DecimalField("Valor do produto", validators=[DataRequired()])
    disponibilidade = StringField("Possivel venda SIM ou NÃO", validators=[DataRequired()])
    botao = SubmitField("Cadastrar")


@app.route("/", methods=["GET", "POST"])
def homepage():
    global produto_cadastrado
    form = Cadastro()
    if form.validate_on_submit():
        produto_cadastrado = {
            "nome": form.nome.data,
            "descricao": form.descricao.data,
            "valor": form.valor.data,
            "disponibilidade": form.disponibilidade.data
        }
        return redirect(url_for("exibir"))
    return render_template("homepage.html", form=form)

@app.route("/exibir")
def exibir():
    return render_template("pagina.html", produto=produto_cadastrado)


if __name__ == "__main__":
    app.run(debug=True)
