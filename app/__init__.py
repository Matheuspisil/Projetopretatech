from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect
from flask_migrate import Migrate 
from flask_login import LoginManager, current_user
import logging
from flask_wtf.csrf import CSRFProtect, generate_csrf
from werkzeug.security import generate_password_hash

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)

    # Configurações
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco_de_talentos.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'sua_chave_secreta'
    app.config['ADMIN_USERNAME'] = 'admin'
    app.config['ADMIN_PASSWORD'] = 'admin123'
 
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    csrf.init_app(app)
    
    logging.basicConfig(level=logging.INFO)

    with app.app_context():
        from .models import Talento, User  # Importar modelos dentro do contexto da aplicação
        db.create_all()
        inspector = inspect(db.engine)
        app.logger.info("Tabelas no banco de dados: %s", inspector.get_table_names())
        
        if not User.query.filter_by(username=app.config['ADMIN_USERNAME']).first():
            hashed_password = generate_password_hash(app.config['ADMIN_PASSWORD'], method='pbkdf2:sha256')
            new_user = User(username=app.config['ADMIN_USERNAME'], password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            app.logger.info("Superuser criado: %s", app.config['ADMIN_USERNAME'])

    # Importar e registrar blueprints dentro do contexto da aplicação
    from .routes import bp
    app.register_blueprint(bp)
    
    login_manager.login_view = "main.login"

    # Função de contexto para CSRF token
    @app.context_processor
    def inject_csrf_token():
        return dict(csrf_token=generate_csrf())

    # Função de contexto para o current_user
    @app.context_processor
    def inject_user():
        return dict(current_user=current_user)

    return app

@login_manager.user_loader
def load_user(user_id):
    from .models import User  # Importar modelo User dentro da função
    return User.query.get(int(user_id))
