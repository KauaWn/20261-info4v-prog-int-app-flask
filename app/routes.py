# from app import app
# from flask import render_template, redirect, flash
# from app.forms.login_form import LoginForm
# from app.controllers.AuthenticationControllers import AuthenticationController


# @app.route("/")
# def home():
#     usuario = {
#         "nome": "Kauã",
#         "produtos": ["Banana", "Abacaxi", "Melancia"]
#     }
#     esta_logado = True
#     return render_template("index.html", 
#                            pessoa = usuario, 
#                            usuario_logado = esta_logado)

# @app.route("/sobre")
# def sobre():
#     return "Página Sobre"

# @app.route("/index2")
# def index2():
#     return render_template('index2.html')


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     formulario = LoginForm()
#     if formulario.validate_on_submit():
#         if AuthenticationController.login(formulario):
#              flash("Login efetuado com sucesso!")
#              return redirect('/')
#         else:
#             flash("Erro nas credenciais.")
#             return redirect('/login')
#     return render_template('login.html', title='Login', form=formulario)


# from app import app
# from flask import render_template, redirect, flash, url_for
# from app.forms.login_form import LoginForm
# from app.controllers.AuthenticationControllers import AuthenticationController


# @app.route("/")
# def index():
#     # Inicializa automaticamente redirecionando para o login
#     return redirect(url_for('login'))


# @app.route("/home")
# def home():
#     usuario = {
#         "nome": "Kauã",
#         "produtos": ["Banana", "Abacaxi", "Melancia"]
#     }
#     esta_logado = True
#     return render_template("index.html", 
#                            pessoa=usuario, 
#                            usuario_logado=esta_logado)


# @app.route("/sobre")
# def sobre():
#     return "Página Sobre"


# @app.route("/index2")
# def index2():
#     return render_template('index2.html')


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     formulario = LoginForm()
#     if formulario.validate_on_submit():
#         if AuthenticationController.login(formulario):
#              flash("Login efetuado com sucesso!")
#              # Agora redireciona para a /home após o sucesso
#              return redirect(url_for('home'))
#         else:
#             flash("Erro nas credenciais.")
#             return redirect(url_for('login'))
            
#     return render_template('login.html', title='Login', form=formulario)

from app import app
from flask import render_template, redirect, flash, url_for, session # <-- Importe o 'session'
from app.forms.login_form import LoginForm
from app.controllers.AuthenticationControllers import AuthenticationController

@app.route("/")
def index():
    return redirect(url_for('login'))

@app.route("/home")
def home():
    # Recupera o nome salvo na sessão. Se não houver nenhum, usa 'Visitante' por padrão.
    nome_do_usuario = session.get('nome_usuario', 'Visitante')
    
    usuario = {
        "nome": nome_do_usuario, # <-- O nome agora é dinâmico!
        "produtos": ["Banana", "Abacaxi", "Melancia"]
    }
    
    # Verifica se a pessoa realmente passou pelo login checando se o nome está na sessão
    esta_logado = 'nome_usuario' in session 
    
    return render_template("index.html", 
                           pessoa=usuario, 
                           usuario_logado=esta_logado)

@app.route("/sobre")
def sobre():
    return "Página Sobre"

@app.route("/index2")
def index2():
    return render_template('index2.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    formulario = LoginForm()
    if formulario.validate_on_submit():
        if AuthenticationController.login(formulario):
             flash("Login efetuado com sucesso!")
             
             # Salva o nome preenchido no formulário dentro da sessão do Flask
             # ATENÇÃO: Substitua 'username' pelo nome exato do campo no seu LoginForm (ex: nome, email, login, etc)
             session['nome_usuario'] = formulario.username.data 
             
             return redirect(url_for('home'))
        else:
            flash("Erro nas credenciais.")
            return redirect(url_for('login'))
            
    return render_template('login.html', title='Login', form=formulario)


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    formulario = LoginForm()
    if formulario.validate_on_submit():
        if AuthenticationController.login(formulario):
             flash("Cadastro efetuado com sucesso!")
             
             # Salva o nome preenchido no formulário dentro da sessão do Flask
             # ATENÇÃO: Substitua 'username' pelo nome exato do campo no seu LoginForm (ex: nome, email, login, etc)
             session['nome_usuario'] = formulario.username.data 
             
             return redirect(url_for('home'))
        else:
            flash("Erro nas credenciais.")
            return redirect(url_for('cadastro'))
            
    return render_template('cadastro.html', title='Cadastro', form=formulario)