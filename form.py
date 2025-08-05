from collections.abc import Sequence
from typing import Any, Mapping
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from fakepintrest.models import Usuario

class FormLogin(FlaskForm):
    email = StringField("E-mail!", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired()])
    button = SubmitField("Fazer Login")
    
    

class FormCriarConta(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    username = StringField("Username", validators=[DataRequired()])
    senha = PasswordField("Senha", validators=[DataRequired(), Length(6, 20)])
    confirmar_senha = PasswordField("Confirmar senha", validators=[DataRequired(), EqualTo("senha")])
    button = SubmitField("Criar conta")
    
    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError("E-mail já cadastrado, faça login para continuar")
        
        
class FormFoto(FlaskForm):
    foto = FileField("Foto", validators=[DataRequired()])
    botao_envio = SubmitField("Enviar")
