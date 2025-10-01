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


while True:
	mensaje = input()+"\r\n"
	sock.send(mensaje.encode())
	mensaje,_=sock.recvfrom(1024)  # Esperar respuesta del servidor
	print(f"Respuesta del servidor: {mensaje}")
	if mensaje=="Conexión cerrada por el cliente":
		print(f"El servidor ha cerrado la conexión")
		break
sock.close()
	
mensaje="FINAL"	
sock.send(mensaje.encode())
mensaje=sock.recv(1024)  # Esperar respuesta del servidor
print(f"Respuesta del servidor: {mensaje}")

sock.close()
