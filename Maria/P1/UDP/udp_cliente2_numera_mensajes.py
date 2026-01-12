import socket
import sys

# Valores por defecto
host = "localhost"
puerto = 9999

# Procesar argumentos de línea de comandos
#sys.argv es una lista de los argumentos de la línea de comandos
#sys.argv[1] es el nombre del script y los 2 otros argumentos el host y el puerto por eso si tiene más de 3 se excede
if len(sys.argv) == 3:
    server_ip = sys.argv[1]
    server_port = int(sys.argv[2])
else:
    server_ip = "localhost"
    server_port = 9999

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print(f"Escribe lo que quieras pero FIN AL FINAL")
numero = 1

while True:
    texto = input()
    if texto == "FIN":
        break
    
    mensaje = f"{numero}: {texto}"
    
    sock.sendto(mensaje.encode(), (server_ip, server_port))
    
    
    numero += 1

sock.close()