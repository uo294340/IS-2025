from flask import render_template
from app import db
from app.models import Amigo

def register_routes(app):

    # Ruta principal: Listar amigos
    @app.route('/amigos')
    def list_amigos():
        # Consulta a la base de datos (SELECT * FROM amigos)
        amigos = Amigo.query.all()

        # Renderizar el template pasando los datos
        return render_template('tabla_amigos.html', amigos=amigos)

    # Ruta raíz redirige a /amigos
    @app.route('/')
    def index():
        return list_amigos()