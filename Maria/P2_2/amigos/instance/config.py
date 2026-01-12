# Definición de secretos a usar por la app
import os

# Leemos la URI de la variable de entorno, si no existe, usa sqlite (que fallará, pero es seguro)
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", "sqlite://")