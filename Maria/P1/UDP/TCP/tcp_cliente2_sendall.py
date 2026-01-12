import socket
import sys

IP = "localhost"
PORT = 9999
if len(sys.argv) > 2:
    IP = sys.argv[1]
    PORT = int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#TCP usa SOCK_STREAM
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(f"Conectando a {IP}:{PORT}...")
s.connect((IP, PORT))

# Enviamos 5 mensajes de 5 bytes
for i in range(4):
    #ensaje = "ABCDE"
    #pint(f"Enviando: {mensaje}")
    # Usamos sendall para garantizar el envío completo
    #.sendall(mensaje.encode("utf-8"))
    mensaje = "ABCD"  # <--- CAMBIO: Solo 4 bytes
    s.sendall(mensaje.encode("utf-8"))

# Enviamos FINAL
s.sendall("FINAL".encode("utf-8"))

s.close()
print("Desconectado.")