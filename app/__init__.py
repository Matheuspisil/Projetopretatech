from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configurações
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco_de_talentos.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        # Importar modelos para garantir que eles são conhecidos pelo SQLAlchemy
        from .models import Talento
        db.create_all()  # Criar as tabelas no banco de dados

        # Usar inspect para listar tabelas no banco de dados
        inspector = inspect(db.engine)
        print("Tabelas no banco de dados:", inspector.get_table_names())

    # Importar e registrar blueprints
    from .routes import bp
    app.register_blueprint(bp)

    return app
