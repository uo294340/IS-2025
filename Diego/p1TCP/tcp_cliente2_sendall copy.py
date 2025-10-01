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
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((server_ip, server_port))

numero=1
while numero<6:
	mensaje = "ABCDE"
	sock.sendall(mensaje.encode())
	mensaje=sock.recv(1024)  # Esperar respuesta del servidor
	print(f"Respuesta del servidor: {mensaje}")
	numero+=1
mensaje="FINAL"	
sock.sendall(mensaje.encode())
mensaje=sock.recv(1024)  # Esperar respuesta del servidor
print(f"Respuesta del servidor: {mensaje}")

sock.close()
