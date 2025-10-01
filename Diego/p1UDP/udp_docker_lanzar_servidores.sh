#!/bin/bash
# Script para lanzar 3 servidores UDP en la red "pruebas"

# Crear la red si no existe
docker network inspect pruebas >/dev/null 2>&1 || docker network create pruebas

# Lanzar los servidores
docker run -d --name servidor1 --network pruebas  -v $(pwd):/app python:3.7 python /app
/udp_servidor6_broadcast.py

docker run -d --name servidor2 --network pruebas  -v $(pwd):/app python:3.7 python /app
/udp_servidor6_broadcast.py

docker run -d --name servidor3 --network pruebas  -v $(pwd):/app python:3.7 python /app
/udp_servidor6_broadcast.py


