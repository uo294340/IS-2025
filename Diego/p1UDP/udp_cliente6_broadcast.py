import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
puerto = 12345
broadcast_ip="192.168.1.255"
sock.settimeout(5)
sock.sendto(b"BUSCANDO HOLA", (broadcast_ip, puerto))
print("Enviado: BUSCANDO HOLA")

servidores = []
try:
    while True:
        datos, direccion = sock.recvfrom(1024)
        mensaje = datos.decode()
        if mensaje == "IMPLEMENTO HOLA":
            print(f"Servidor encontrado en {direccion[0]}")
            print(f"Respuesta recibida: {mensaje}")
            if direccion[0] not in servidores:
                servidores.append(direccion[0])
except socket.timeout:
    print("No se ha recibido ninguno mas")
    pass

if not servidores:
    print("No se encontraron servidores HOLA.")
    sys.exit(0)

server_ip = servidores[0]
sock.settimeout(3)
sock.sendto(b"HOLA", (server_ip, puerto))
try:
    datos, direccion = sock.recvfrom(1024)
    print(f"Respuesta del servidor: {datos.decode()}")
except socket.timeout:
    print("No se recibió respuesta al mensaje HOLA.")

sock.close()