from flask import Blueprint, render_template, request, redirect, url_for, flash
from . import db
from .models import Talento, User
from .forms import TalentoForm
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

# Criação do Blueprint chamado 'main'
bp = Blueprint('main', __name__)

# Rota inicial que renderiza a página inicial do Banco de Talentos
@bp.route("/")
def index():
    title = "Banco de Talentos"
    return render_template("index.html", title=title)

# Rota para cadastrar um novo talento
@bp.route("/talentos", methods=["GET", "POST"])
def cadastrar_talento():
    if request.method == "POST":  # Verifica se o método da requisição é POST
        # Coleta os dados do formulário
        nome = request.form["nome"]
        area = request.form["area"]
        cargo_pretendido = request.form["cargo_pretendido"]
        cidade = request.form["cidade"]
        bairro = request.form["bairro"]
        email = request.form["email"]
        telefone = request.form["contato"]
        github = request.form["github"]
        linkedin = request.form["linkedin"]

        # Cria uma nova instância de Talento com os dados recebidos
        talento = Talento(nome=nome, area=area, cargo_pretendido=cargo_pretendido,
                          cidade=cidade, bairro=bairro, email=email,
                          telefone=telefone, github=github, linkedin=linkedin)
                                        
        # Adiciona o novo talento ao banco de dados
        db.session.add(talento)
        db.session.commit()

        # Redireciona para a página inicial após o cadastro
        return redirect(url_for("main.index"))

    # Renderiza o template 'cadastrar_talento.html' para exibir o formulário de cadastro
    return render_template("cadastrar_talento.html")

# Rota para visualizar todos os talentos cadastrados
@bp.route("/visualizar")
@login_required
def visualizar_talentos():
    talentos = Talento.query.all()  # Obtém todos os talentos cadastrados no banco de dados
    if not talentos:
        message = "Nenhum talento cadastrado ainda."
        return render_template("visualizar_talentos.html", message=message)
    
    # Renderiza o template 'visualizar_talentos.html' e passa a lista de talentos como contexto
    return render_template("visualizar_talentos.html", talentos=talentos)




# Rota para exibir estatísticas ou dados analíticos
@bp.route("/estatisticas")
@login_required
def estatisticas():
    # Implementação futura: incluir gráficos e dados analíticos
    return render_template("estatisticas.html")

@bp.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for("main.index"))
        else:
            flash("Usuário ou senha inválidos ")
    return render_template("login.html")

@bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))
        

# @bp.route("/index")
#     def voltar_pagina_inicial():
#     title = "Voltar para a pagina inicial"
#     return render_template("index.html", title=title)
   