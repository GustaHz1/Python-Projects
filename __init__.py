from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)

# Configurações
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///comunidade.db"
app.config["SECRET_KEY"] = "bd166146129be2560c92b30b928b0466"
app.config["UPLOAD_FOLDER"] = "static/fotos_posts"

# Inicializando extensões
database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

# Configuração do login
login_manager.login_view = "homepage"

# Importando rotas
from fakepintrest import views
