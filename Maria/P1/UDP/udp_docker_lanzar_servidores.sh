#!/bin/bash
# Crear la red "pruebas" si no existe
docker network inspect pruebas >/dev/null 2>&1 || docker network create pruebas

# Lanzar 3 servidores
echo "Lanzando servidor1..."
docker run -d --name servidor1 --network pruebas -v $(pwd):/app python:3.7 python /app/udp_servidor6_broadcast.py

echo "Lanzando servidor2..."
docker run -d --name servidor2 --network pruebas -v $(pwd):/app python:3.7 python /app/udp_servidor6_broadcast.py

echo "Lanzando servidor3..."
docker run -d --name servidor3 --network pruebas -v $(pwd):/app python:3.7 python /app/udp_servidor6_broadcast.py