from flask import Blueprint, render_template, request, redirect, url_for
from . import db
from .models import Talento

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
        contato = request.form["contato"]
        github = request.form["github"]
        linkedin = request.form["linkedin"]

        # Cria uma nova instância de Talento com os dados recebidos
        talento = Talento(nome=nome, area=area, cargo_pretendido=cargo_pretendido,
                          cidade=cidade, bairro=bairro, email=email,
                          contato=contato, github=github, linkedin=linkedin)

        # Adiciona o novo talento ao banco de dados
        db.session.add(talento)
        db.session.commit()

        # Redireciona para a página inicial após o cadastro
        return redirect(url_for("main.index"))

    # Renderiza o template 'cadastrar_talento.html' para exibir o formulário de cadastro
    return render_template("cadastrar_talento.html")

# Rota para visualizar todos os talentos cadastrados
@bp.route("/visualizar")
def visualizar_talentos():
    talentos = Talento.query.all()  # Obtém todos os talentos cadastrados no banco de dados

    if not talentos:
        message = "Nenhum talento cadastrado ainda."
        return render_template("visualizar_talentos.html", message=message)
    
    # Renderiza o template 'visualizar_talentos.html' e passa a lista de talentos como contexto
    return render_template("visualizar_talentos.html", talentos=talentos)

# Rota para exibir estatísticas ou dados analíticos
@bp.route("/estatisticas")
def estatisticas():
    # Implementação futura: incluir gráficos e dados analíticos
    return render_template("estatisticas.html")

#sugestão de rota
# Rota para adicionar uma nova formação 

@bp.route('/talento/<int:talento_id>/add_formacao', methods=['POST']) # rota para adicionar formação inicial
def add_formacao(talento_id):
    # obter os dados da formação do request.form 
    nova_formacao = Formacao(
        formacao=request.form['formacao'],
        inicio_formacao=request.form['inicio_formacao'],
        termino_formacao=request.form['termino_formacao'],
        talento_id=talento_id
    )
    db.session.add(nova_formacao)
    db.session.commit()
    return 'Formação adicionada com sucesso!', 201

@bp.route('/talento/<int:talento_id>/nova_formacao') # rota para mostrar a página com o formulário
def nova_formacao(talento_id):
    # Aqui você pode passar o talento_id para o template
    return render_template('add_formacao.html', talento_id=talento_id)

