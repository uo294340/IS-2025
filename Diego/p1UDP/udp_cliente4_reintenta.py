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
numero = 1
while True:
	texto = input()
	if texto == "FIN":
		break
	mensaje = f"{numero}: {texto}"
	timeout=0.1
	recibido=False
	while not recibido and timeout<=2:
		sock.settimeout(timeout)
		sock.sendto(mensaje.encode(), (server_ip, server_port))

		try:
			datos,_= sock.recvfrom(1024)
			print((f"Recibido {datos}"))
			recibido=True
		except socket.timeout:
			print("No se recibió confirmación del servidor vuelve a escribir los datos ")
			timeout*=2
	#Una vez se sale del while comprobamos si el mensaje se ha recibido-> el timeout >2
	if not recibido:
		print("No se ha recibido confirmación del servidor, se descarta el mensaje")
		break
	numero += 1

sock.close()
