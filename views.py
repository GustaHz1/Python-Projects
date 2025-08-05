from flask import render_template, url_for, redirect
from fakepintrest import app, database, bcrypt
from fakepintrest.models import Usuario, Foto
from flask_login import login_required, login_user, logout_user, current_user
from fakepintrest.form import FormCriarConta, FormLogin, FormFoto
import os
from werkzeug.utils import secure_filename

# Rota da homepage
# Se a página for receber ou enviar informações declaramos seus metodos
@app.route("/", methods=["GET", "POST"])
def homepage():
    # Validando o login de perfil
    form_login = FormLogin()
    if form_login.validate_on_submit():
        usuario = Usuario.query.filter_by(email = form_login.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, form_login.senha.data):
            login_user(usuario)
            return redirect(url_for("perfil", id_usuario = usuario.id))
    return render_template("homepage.html", form=form_login)

# Rota para criar conta
# Se a página for receber ou enviar informações declaramos seus metodos
@app.route("/criarconta", methods=["GET", "POST"])
def criarconta():
    form_criar_conta = FormCriarConta()
    if form_criar_conta.validate_on_submit():
        # Criptografando a senha do usuário
        senha_criptografada = bcrypt.generate_password_hash(form_criar_conta.senha.data).decode('utf-8')
        
        # Criando um novo usuário com a senha criptografada
        usuario = Usuario(
            username=form_criar_conta.username.data,
            senha=senha_criptografada,
            email=form_criar_conta.email.data
        )
        
        # Adicionando o usuário ao banco de dados
        database.session.add(usuario)
        database.session.commit()
        login_user(usuario, remember = True)
        
        # Redirecionar para o perfil após a criação da conta
        return redirect(url_for("perfil", id_usuario = usuario.id))
    
    return render_template("criarconta.html", form=form_criar_conta)

# Rota de perfil
# Se a página for receber ou enviar informações declaramos seus metodos
@app.route("/perfil/<id_usuario>", methods = ["GET", "POST"])
@login_required
def perfil(id_usuario):
    #Validando se o usuario está visitando seu perfil ou de outro usuario 
    if int(id_usuario) == int(current_user.id):
        form_foto = FormFoto()
        if form_foto.validate_on_submit():
            # Buscando a foto enviada pelo formulario
            arquivo = form_foto.foto.data
            nome_seguro = secure_filename(arquivo.filename)
            # Salvando o arquivo na pasta static/fotos_posts
            # OS está fazendo a busca do arquivo do nosso projeto
            caminho = os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config["UPLOAD_FOLDER"],nome_seguro)
            arquivo.save(caminho)
            # Registrando no banco de dados
            # Criando a imagem buscando os campos da tabela fotos 
            foto = Foto(imagem =nome_seguro, id_usuario =current_user.id)
            database.session.add(foto)
            database.session.commit()
        
        return render_template("perfil.html", usuario=current_user, form=form_foto)
    else:
        usuario = Usuario.query.get(int(id_usuario))
        return render_template("perfil.html", usuario=usuario, form = None)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("homepage"))

@app.route("/feed")
@login_required
def feed():
    fotos = Foto.query.order_by(Foto.data).all()
    return render_template("feed.html", fotos = fotos)
    
