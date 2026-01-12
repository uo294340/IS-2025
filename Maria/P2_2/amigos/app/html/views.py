# Imports correctos desde Flask
from flask import render_template, request, redirect, url_for, abort
# Importamos el blueprint 'html' definido en __init__.py
from . import html
# Importamos la base de datos y el modelo desde los paquetes superiores
from .. import db
from ..models import Amigo



# Ruta principal: Listar amigos
@html.route('/amigos')
def tabla_amigos():
    # Consulta a la base de datos
    amigos = Amigo.query.all()
    return render_template('tabla_amigos.html', amigos=amigos)

# Ruta raíz del blueprint redirige a la tabla
@html.route('/')
def index():
    return redirect(url_for('html.tabla_amigos'))

@html.route("/delete_amigo/<int:id>")
def delete_amigo(id):
    amigo = Amigo.query.get_or_404(id)
    db.session.delete(amigo)
    db.session.commit()
    return redirect(url_for('html.tabla_amigos'))

@html.route("/edit_amigo/<int:id>")
def edit_amigo(id):
    amigo = Amigo.query.get_or_404(id)
    return render_template("edit_amigo.html", amigo=amigo)

@html.route("/new_amigo")
def new_amigo():
    return render_template("edit_amigo.html", amigo=None)

@html.route("/save_amigo", methods=["POST"])
def save_amigo():
    # Usamos request.form (de Flask)
    id = request.form.get("id")
    nombre = request.form.get("nombre")
    lat = request.form.get("lat", "0")
    lon = request.form.get("lon", "0")

    if not nombre:
        abort(422) # Nombre obligatorio

    if not id:
        # Crear nuevo
        amigo = Amigo(nombre=nombre, lat=lat, lon=lon)
        db.session.add(amigo)
    else:
        # Editar existente
        amigo = Amigo.query.get_or_404(int(id))
        amigo.nombre = nombre
        amigo.lat = lat
        amigo.lon = lon

    db.session.commit()
    return redirect(url_for("html.tabla_amigos"))