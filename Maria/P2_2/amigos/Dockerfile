FROM python:3.9-slim
# Usamos 3.9-slim que es más ligero y moderno que 3.7

RUN pip install flask gunicorn flask-sqlalchemy pymysql flask-migrate

# Creamos directorio de trabajo
RUN mkdir /amigos
COPY . /amigos
WORKDIR /amigos

# Exponemos el puerto interno
EXPOSE 5000

# Comando de arranque con Gunicorn (Servidor de Producción)
CMD ["gunicorn", "-b", "0.0.0.0:5000", "-w", "4", "lanzar:app"]
