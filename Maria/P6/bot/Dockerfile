# Usamos una imagen base ligera de Python
FROM python:3.9-slim

# Evita que Python guarde archivos .pyc y fuerza el flush de logs a la consola de Docker
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Instalamos las dependencias indicadas en el enunciado
# (Podemos hacerlo en una línea para ahorrar capas)
RUN pip install --no-cache-dir wheel slixmpp==1.8.6

# Copiamos el código del bot al contenedor
COPY mibot.py .

# Comando que se ejecuta al arrancar el contenedor
CMD ["python3", "mibot.py"]