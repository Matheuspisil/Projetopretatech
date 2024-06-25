from . import db

# Definição do modelo Talento
class Talento(db.Model):
    
    id = db.Column(db.Integer, primary_key=True) # id no Banco de dados da tabela talento
    nome = db.Column(db.String(100), nullable=False)  # Nome do talento (obrigatório)
    area = db.Column(db.String(100), nullable=False)
    cargo_pretendido = db.Column(db.String(100), nullable=False)  # Cargo pretendido pelo talento (obrigatório)
    cidade = db.Column(db.String(100), nullable=False)  # Cidade onde o talento mora (obrigatório)
    bairro = db.Column(db.String(100))  # Bairro onde o talento mora (opcional)
    email = db.Column(db.String(120), nullable=False, unique=True)  # Email do talento (obrigatório e único)
    telefone = db.Column(db.String(20), nullable=False)  # Telefone para contato do talento (obrigatório)
    github = db.Column(db.String(100))  # Perfil do GitHub do talento (opcional)
    linkedin = db.Column(db.String(100))  # Perfil do LinkedIn do talento (opcional)

    def __repr__(self):
        return f"Talento('{self.nome}', '{self.cargo_pretendido}', '{self.cidade}')"


