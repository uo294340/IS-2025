#!/bin/bash


BROADCAST_IP="172.18.255.255"

echo "Lanzando cliente buscando en $BROADCAST_IP..."

docker run -it --name cliente6 --network pruebas \
  -v $(pwd):/app python:3.7 \
  python /app/udp_cliente6_broadcast.py $BROADCAST_IP 12345