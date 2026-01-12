from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  
from config import app_config

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    db.init_app(app)
    
    
    # Inicializar la herramienta de migraciones vinculando app y db
    Migrate(app, db)
    
    # Importar los modelos para que SQLAlchemy sepa que existen
    from app import models 
    # ---------------------------

    @app.route("/")
    def prueba():
        return "¡Hola Flask con MariaDB!"

    return app