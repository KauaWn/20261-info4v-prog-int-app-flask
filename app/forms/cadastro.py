from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

class cadastroForm(FlaskForm):
    username = StringField('Usuário', validators=[DataRequired(message="Por favor, insira seu nome de usuário.")])
    email = StringField('Email', validators=[DataRequired(message="Por favor, insira seu email."), Email()])
    password = PasswordField('Senha', validators=[DataRequired(message="Por favor, insira sua senha.")])
    confirm_password = PasswordField('Confirmar senha', validators=[DataRequired(message="Por favor, insira sua senha."), EqualTo("password", message="As senhas não estão iguais.")])
    remember_me = BooleanField('Permanecer conectado')
    submit = SubmitField('Cadastrar')

    def validate_username(self, field):
        if field.data.lower() == 'admin':
            raise ValidationError('O nome "admin" está reservado. Escolha outro.')
        
    def validate_password(self, field):
        if field.data.lower() == '123456':
            raise ValidationError('A senha é muito fraca.')
