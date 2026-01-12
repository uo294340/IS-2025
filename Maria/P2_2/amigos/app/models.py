from app import db

class Amigo(db.Model):
    """
    Clase que define la tabla 'amigos' en la base de datos.
    """
    __tablename__ = 'amigos'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(60))
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)

    def __repr__(self):
        return f'<Amigo: {self.nombre}>'