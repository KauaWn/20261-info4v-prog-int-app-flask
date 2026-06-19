from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Usuário', validators=[DataRequired(message="Por favor, insira seu nome de usuário.")])
    password = PasswordField('Senha', validators=[DataRequired(message="Por favor, insira sua senha.")])
    remember_me = BooleanField('Permanecer conectado')
    submit = SubmitField('Entrar')

    # def validate_username(self, field):
    #     if field.data.lower() == 'admin':
    #         raise ValidationError('O nome "admin" está reservado. Escolha outro.')