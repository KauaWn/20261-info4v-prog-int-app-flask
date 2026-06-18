from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo

class LoginForm(FlaskForm):
    username = StringField('Usuário', validators=[DataRequired(message="Por favor, insira seu nome de usuário.")])
    email = StringField('Email', validators=[DataRequired(message="Por favor, insira seu email."), Email()])
    password = PasswordField('Senha', validators=[DataRequired(message="Por favor, insira sua senha.")])
    confirm_password = PasswordField('Confirmar senha', validators=[DataRequired(message="Por favor, insira sua senha."), EqualTo("password", message="As senhas não estão iguais.")])
    remember_me = BooleanField('Permanecer conectado')
    submit = SubmitField('Entrar')
