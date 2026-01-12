import socket
import sys
import random

IP = "0.0.0.0"
PORT = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((IP, PORT))

print(f"Servidor MEJORADO escuchando en {PORT}...")

while True:
    try:
        datos, direccion = s.recvfrom(1024)
        mensaje = datos.decode("utf-8")
        
        # Simulamos pérdida (50%)
        if random.randint(0, 1) == 0:
            print(f"Simulando pérdida: {mensaje}")
            continue

        print(f"Recibido: {mensaje}")
        
        # Extraemos el ID del mensaje. 
        # El formato es "NUMERO: TEXTO". Hacemos split por el primer ":"
        partes = mensaje.split(":", 1) 
        if len(partes) > 0:
            msg_id = partes[0]
            
            # Respondemos especificando QUÉ mensaje confirmamos
            respuesta = f"OK {msg_id}"
            s.sendto(respuesta.encode("utf-8"), direccion)
            
    except Exception as e:
        print(f"Error en servidor: {e}")