from . import db

# Definição do modelo Talento
class Talento(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Chave primária do talento
    nome = db.Column(db.String(100), nullable=False)  # Nome do talento (obrigatório)
    cargo_pretendido = db.Column(db.String(100), nullable=False)  # Cargo pretendido pelo talento (obrigatório)
    cidade = db.Column(db.String(100), nullable=False)  # Cidade onde o talento mora (obrigatório)
    bairro = db.Column(db.String(100))  # Bairro onde o talento mora (opcional)
    empregado = db.Column(db.Boolean, nullable=False, default=False)  # Status de emprego do talento (obrigatório, padrão False)
    email = db.Column(db.String(120), nullable=False, unique=True)  # Email do talento (obrigatório e único)
    telefone = db.Column(db.String(20), nullable=False)  # Telefone para contato do talento (obrigatório)
    github = db.Column(db.String(100))  # Perfil do GitHub do talento (opcional)
    linkedin = db.Column(db.String(100))  # Perfil do LinkedIn do talento (opcional)
    objetivo = db.Column(db.String(200), nullable=False)  # Área onde o talento deseja atuar (obrigatório)
    resumo_profissional = db.Column(db.Text, nullable=False)  # Resumo profissional do talento (obrigatório)

    # Relacionamentos com outros modelos
    graduacoes = db.relationship('Graduacao', backref='talento', lazy=True)  # Relacionamento um-para-muitos com Graduacao
    cursos_livres = db.relationship('CursoLivre', backref='talento', lazy=True)  # Relacionamento um-para-muitos com CursoLivre
    idiomas = db.relationship('Idioma', backref='talento', lazy=True)  # Relacionamento um-para-muitos com Idioma
    experiencias_profissionais = db.relationship('ExperienciaProfissional', backref='talento', lazy=True)  # Relacionamento um-para-muitos com ExperienciaProfissional

    def __repr__(self):
        return f"Talento('{self.nome}', '{self.cargo_pretendido}', '{self.cidade}')"

# Definição do modelo Graduacao
class Graduacao(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Chave primária da graduação
    nome = db.Column(db.String(100), nullable=False)  # Nome da graduação (obrigatório)
    data_inicial = db.Column(db.String(20), nullable=False)  # Data de início da graduação (obrigatório)
    data_final = db.Column(db.String(20), nullable=True)  # Data de término da graduação (opcional)
    talento_id = db.Column(db.Integer, db.ForeignKey('talento.id'), nullable=False)  # Chave estrangeira referenciando Talento

# Definição do modelo CursoLivre
class CursoLivre(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Chave primária do curso livre
    nome = db.Column(db.String(100), nullable=False)  # Nome do curso livre (obrigatório)
    carga_horaria = db.Column(db.String(20), nullable=True)  # Carga horária do curso livre (opcional)
    data_inicial = db.Column(db.String(20), nullable=False)  # Data de início do curso livre (obrigatório)
    data_final = db.Column(db.String(20), nullable=True)  # Data de término do curso livre (opcional)
    talento_id = db.Column(db.Integer, db.ForeignKey('talento.id'), nullable=False)  # Chave estrangeira referenciando Talento

# Definição do modelo Idioma
class Idioma(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Chave primária do idioma
    nome = db.Column(db.String(100), nullable=False)  # Nome do idioma (obrigatório)
    nivel = db.Column(db.String(50), nullable=False)  # Nível de proficiência no idioma (obrigatório)
    talento_id = db.Column(db.Integer, db.ForeignKey('talento.id'), nullable=False)  # Chave estrangeira referenciando Talento

# Definição do modelo ExperienciaProfissional
class ExperienciaProfissional(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Chave primária da experiência profissional
    empresa = db.Column(db.String(100), nullable=False)  # Nome da empresa (obrigatório)
    data_entrada = db.Column(db.String(20), nullable=False)  # Data de entrada na empresa (obrigatório)
    data_saida = db.Column(db.String(20), nullable=True)  # Data de saída da empresa (opcional)
    resumo_atividades = db.Column(db.Text, nullable=False)  # Resumo das atividades realizadas (obrigatório)
    talento_id = db.Column(db.Integer, db.ForeignKey('talento.id'), nullable=False)  # Chave estrangeira referenciando Talento

#sugestao de classe alterando string para date
# Definição do modelo Formacao
class Formacao(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Chave primária da experiência profissional
    formacao = db.Column(db.String(100), nullable=False)  # Nome da Formação (obrigatório)
    inicio_formacao = db.Column(db.Date, nullable=False)  # Data de início da formação (obrigatório) # ao invés de string usar date para facilitar a manipulação de datas.
    termino_formacao = db.Column(db.Date, nullable=False)  # Data de conclusão da formação (opcional)
    talento_id = db.Column(db.Integer, db.ForeignKey('talento.id'), nullable=False)  # Chave estrangeira referenciando Talento



    # ver DateField