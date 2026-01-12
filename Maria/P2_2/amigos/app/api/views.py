from flask import request, jsonify, abort
from .. import db
from ..models import Amigo
from . import api


def amigo_to_dict(amigo):
    """Convierte un objeto Amigo a un diccionario para JSON"""
    return {
        'id': amigo.id,
        'name': amigo.nombre,   # Mapeamos nombre -> name
        'lati': amigo.lat,      # Mapeamos lat -> lati
        'longi': amigo.lon      # Mapeamos lon -> longi
    }



@api.route("/amigo/<int:id>")
def get_amigo(id):
    """Retorna JSON con un amigo concreto"""
    amigo = Amigo.query.get_or_404(id)
    return jsonify(amigo_to_dict(amigo))

@api.route("/amigo/byName/<name>")
def get_amigo_by_name(name):
    """Busca amigo por nombre"""
    # Buscamos por 'nombre' en la BD, aunque la URL use 'name'
    amigo = Amigo.query.filter_by(nombre=name).first()
    if not amigo:
        abort(404, "No se encuentra ningún amigo con ese nombre")
    return jsonify(amigo_to_dict(amigo))

@api.route("/amigos")
def list_amigos():
    """(EJERCICIO RESUELTO) Retorna la lista completa de amigos"""
    amigos = Amigo.query.all()

    lista_json = [amigo_to_dict(a) for a in amigos]
    return jsonify(lista_json)



@api.route("/amigos", methods=["POST"])
def new_amigo():
    """Crea un nuevo amigo desde JSON"""
    if not request.json:
        abort(422, "No se ha enviado JSON")
        
    name = request.json.get("name")
    if not name:
        abort(422, "El JSON no incluye el campo 'name'")
        
    if Amigo.query.filter_by(nombre=name).first():
        abort(422, "Ya existe un amigo con ese nombre")
        
    lati = request.json.get("lati", 0)
    longi = request.json.get("longi", 0)
    
   
    amigo = Amigo(nombre=name, lat=lati, lon=longi)
    db.session.add(amigo)
    db.session.commit()
    
    return jsonify(amigo_to_dict(amigo))

@api.route("/amigo/<int:id>", methods=["PUT"])
def edit_amigo(id):
    """Edita un amigo existente"""
    amigo = Amigo.query.get_or_404(id)
    
    if not request.json:
        abort(422, "No se ha enviado JSON")
        
    name = request.json.get("name")
    lati = request.json.get("lati")
    longi = request.json.get("longi")
    
    if name:
        amigo.nombre = name
    if lati:
        amigo.lat = lati
    if longi:
        amigo.lon = longi
        
    db.session.commit()
    return jsonify(amigo_to_dict(amigo))

@api.route("/amigo/<int:id>", methods=["DELETE"])
def delete_amigo(id):
    """(EJERCICIO RESUELTO) Borra un amigo"""
    amigo = Amigo.query.get_or_404(id)
    db.session.delete(amigo)
    db.session.commit()
    # 204 No Content
    return ('', 204)