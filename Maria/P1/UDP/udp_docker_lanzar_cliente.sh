#!/bin/bash
docker run -it --network pruebas --name cliente6 -v $(pwd):/app python:3.7    python /app/udp_cliente6_broadcast.py 172.18.255.255 12345