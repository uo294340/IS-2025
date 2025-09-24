import socket
import sys



if len(sys.argv) == 3:
	server_ip = sys.argv[1]
	server_port = int(sys.argv[2])
elif len(sys.argv) == 1:
	server_ip = "localhost"
	server_port = 9999
else:
	print("Error en los argumentos")
	sys.exit(1)

# Crear socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print(f"Escribe lo que quieras pero FIN AL FINAL")
while True:
	mensaje = input()
	if mensaje == "FIN":
		break
	sock.sendto(mensaje.encode(), (server_ip, server_port))

sock.close()
