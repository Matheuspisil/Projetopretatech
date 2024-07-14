from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from .models import Talento, User
from .forms import TalentoForm

bp = Blueprint('main', __name__)

@bp.route("/")
def index():
    title = "Banco de Talentos"
    return render_template("index.html", title=title)

@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for("main.index"))
        else:
            flash("Credenciais inválidas, tente novamente.", "error")
    return render_template("login.html")

@bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Você foi deslogado com sucesso.", "success")
    return redirect(url_for("main.index"))

@bp.route("/talentos", methods=["GET", "POST"])
def cadastrar_talento():
    form = TalentoForm()

    # Definir opções dinâmicas para o campo 'cargo_pretendido'
    form.cargo_pretendido.choices = [
        ('Desenvolvedor(a) Backend', 'Desenvolvedor(a) Backend'),
        ('Desenvolvedor(a) Frontend', 'Desenvolvedor(a) Frontend'),
        ('Desenvolvedor(a) Full Stack', 'Desenvolvedor(a) Full Stack'),
        ('Engenheiro(a) de Software', 'Engenheiro(a) de Software'),
        ('Analista de Sistemas', 'Analista de Sistemas'),
        ('Desenvolvedor(a) Mobile', 'Desenvolvedor(a) Mobile'),
        ('Engenheiro(a) de Dados', 'Engenheiro(a) de Dados'),
        ('Cientista de Dados', 'Cientista de Dados'),
        ('DevOps', 'DevOps'),
        ('Administrador(a) de Sistemas', 'Administrador(a) de Sistemas'),
        ('Outro', 'Outro')
    ]

    if form.validate_on_submit():
        try:
            nome = form.nome.data
            idade = form.idade.data
            profissao = form.profissao.data
            objetivos = form.objetivos.data
            status_trabalho = form.status_trabalho.data
            area = form.area_formacao.data
            cargos = ','.join(form.cargo_pretendido.data)
            cidade = form.cidade.data
            bairro = form.bairro.data
            email = form.email.data
            telefone = form.telefone.data
            github = form.github.data
            linkedin = form.linkedin.data

            if Talento.query.filter_by(email=email).first():
                flash("Email já cadastrado.", "error")
                return redirect(url_for("main.cadastrar_talento"))

            talento = Talento(
                nome=nome,
                idade=idade,
                profissao=profissao,
                objetivos=objetivos,
                status_trabalho=status_trabalho,
                area=area,
                cargo_pretendido=cargos,
                cidade=cidade,
                bairro=bairro,
                email=email,
                telefone=telefone,
                github=github,
                linkedin=linkedin
            )

            db.session.add(talento)
            db.session.commit()

            flash("Talento cadastrado com sucesso!", "success")
            return redirect(url_for("main.index"))

        except Exception as e:
            db.session.rollback()
            flash(f"Ocorreu um erro: {str(e)}", "error")

    # Adiciona mensagens de erro do formulário
    for field, errors in form.errors.items():
        for error in errors:
            flash(f"Erro no campo {getattr(form, field).label.text}: {error}", "error")

    return render_template("cadastrar_talento.html", form=form)

@bp.route("/visualizar")
@login_required
def visualizar_talentos():
    talentos = Talento.query.all()
    if not talentos:
        message = "Nenhum talento cadastrado ainda."
        return render_template("visualizar_talentos.html", message=message)
    return render_template("visualizar_talentos.html", talentos=talentos)

@bp.route("/estatisticas")
@login_required
def estatisticas():
    total_cadastros = Talento.query.count()
    desempregados = Talento.query.filter_by(status_trabalho='desempregado').all()
    empregados = Talento.query.filter_by(status_trabalho='empregado').all()

    desempregados_info = [{"nome": t.nome, "cargo_pretendido": t.cargo_pretendido} for t in desempregados]
    empregados_info = [{"nome": t.nome, "profissao": t.profissao} for t in empregados]

    return render_template(
        "estatisticas.html",
        total_cadastros=total_cadastros,
        desempregados_info=desempregados_info,
        empregados_info=empregados_info
    )

@bp.route("/editar/<int:id>", methods=["GET", "POST"])
@login_required
def editar_talento(id):
    talento = Talento.query.get_or_404(id)
    form = TalentoForm(obj=talento)

    # Definir opções dinâmicas para o campo 'cargo_pretendido'
    form.cargo_pretendido.choices = [
        ('Desenvolvedor(a) Backend', 'Desenvolvedor(a) Backend'),
        ('Desenvolvedor(a) Frontend', 'Desenvolvedor(a) Frontend'),
        ('Desenvolvedor(a) Full Stack', 'Desenvolvedor(a) Full Stack'),
        ('Engenheiro(a) de Software', 'Engenheiro(a) de Software'),
        ('Analista de Sistemas', 'Analista de Sistemas'),
        ('Desenvolvedor(a) Mobile', 'Desenvolvedor(a) Mobile'),
        ('Engenheiro(a) de Dados', 'Engenheiro(a) de Dados'),
        ('Cientista de Dados', 'Cientista de Dados'),
        ('DevOps', 'DevOps'),
        ('Administrador(a) de Sistemas', 'Administrador(a) de Sistemas'),
        ('Outro', 'Outro')
    ]

    if request.method == "POST" and form.validate_on_submit():
        talento.nome = form.nome.data
        talento.idade = form.idade.data
        talento.profissao = form.profissao.data
        talento.objetivos = form.objetivos.data
        talento.status_trabalho = form.status_trabalho.data
        talento.area = form.area_formacao.data
        talento.cargo_pretendido = ','.join(form.cargo_pretendido.data)
        talento.cidade = form.cidade.data
        talento.bairro = form.bairro.data
        talento.email = form.email.data
        talento.telefone = form.telefone.data
        talento.github = form.github.data
        talento.linkedin = form.linkedin.data

        try:
            db.session.commit()
            flash("Talento atualizado com sucesso!", "success")
            return redirect(url_for("main.visualizar_talentos"))
        except Exception as e:
            db.session.rollback()
            flash(f"Ocorreu um erro: {str(e)}", "error")

    # Adiciona mensagens de erro do formulário
    for field, errors in form.errors.items():
        for error in errors:
            flash(f"Erro no campo {getattr(form, field).label.text}: {error}", "error")

    return render_template("editar_talento.html", form=form, talento=talento)

@bp.route("/excluir/<int:id>", methods=["POST"])
@login_required
def excluir_talento(id):
    talento = Talento.query.get_or_404(id)
    db.session.delete(talento)
    db.session.commit()
    flash("Talento excluído com sucesso!", "success")
    return redirect(url_for("main.visualizar_talentos"))
