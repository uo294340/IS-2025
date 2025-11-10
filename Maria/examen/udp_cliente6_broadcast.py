import socket
import sys

"""puerto = 12345
BROADCAST_IP = '192.168.0.255'  # ip: 192.168.0.28 mask= 255.255.255.0 bradcast_ip:192.168.0.255"""
BROADCAST_IP = sys.argv[1] if len(sys.argv) > 1 else '192.168.0.255'
puerto = int(sys.argv[2]) if len(sys.argv) > 2 else 12345


cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
cliente.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
cliente.settimeout(2)

# Enviar mensaje de búsqueda por broadcast
cliente.sendto(b"BUSCANDO HOLA", (BROADCAST_IP, puerto))
print(f"Enviado 'BUSCANDO HOLA' por broadcast a {BROADCAST_IP}:{puerto}")

servidores = []
try:
    while True:
        datos, direccion = cliente.recvfrom(1024)
        mensaje = datos.decode()
        if mensaje == "IMPLEMENTO HOLA":
            print(f"Servidor encontrado en {direccion[0]}")
            if direccion[0] not in servidores:
                servidores.append(direccion[0])
except socket.timeout:
    pass

if not servidores:
    print("No se encontraron servidores HOLA.")
    sys.exit(0)

# Probar con el primer servidor encontrado
servidor_ip = servidores[0]
print(f"Probando servicio HOLA con {servidor_ip}...")
cliente.settimeout(3)
cliente.sendto(b"HOLA", (servidor_ip, puerto))
try:
    datos, direccion = cliente.recvfrom(1024)
    print(f"Respuesta del servidor: {datos.decode()}")
except socket.timeout:
    print("No se recibió respuesta al mensaje HOLA.")

