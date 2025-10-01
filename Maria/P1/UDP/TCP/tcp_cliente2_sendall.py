import sys
import socket

if len(sys.argv) > 3:
    print("Uso: python tcp_cliente1_simple.py [<ip-servidor> <puerto-servidor>]")
    sys.exit(1)
elif len(sys.argv) == 1:
    ip_servidor = "localhost"  # IP por defecto
    puerto_servidor = 9999      # Puerto por defecto
elif len(sys.argv) == 2:
    ip_servidor = sys.argv[1]
    puerto_servidor = 9999      # Puerto por defecto
else:
    ip_servidor = sys.argv[1]
    puerto_servidor = int(sys.argv[2])

# Creación del socket
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Repetir 5 veces un bucle en el que envíe el texto “ABCDE” (observa que son exactamente 5 bytes, tal como espera el servidor en cada envío)
cliente.connect((ip_servidor, puerto_servidor))
for i in range(5):
    cliente.sendall(b"ABCDE")
    datos = cliente.recv(1024)
    print("Recibido:", datos.decode("ascii"))

cliente.sendall(b"FINAL")
cliente.close()
print("Conexion cerrada")

