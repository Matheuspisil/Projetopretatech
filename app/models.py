from . import db
from flask_login import UserMixin

class Talento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    profissao = db.Column(db.String(100), nullable=False)
    objetivos = db.Column(db.Text, nullable=False)
    status_trabalho = db.Column(db.String(50), nullable=False)
    area = db.Column(db.String(100), nullable=False)
    cargo_pretendido = db.Column(db.String(100), nullable=False)
    cidade = db.Column(db.String(100), nullable=False)
    bairro = db.Column(db.String(100))
    email = db.Column(db.String(120), nullable=False, unique=True)
    telefone = db.Column(db.String(20), nullable=False)
    github = db.Column(db.String(100))
    linkedin = db.Column(db.String(100))

    def __repr__(self):
        return f"Talento('{self.nome}', '{self.cargo_pretendido}', '{self.cidade}')"

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
