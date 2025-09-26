import socket
import sys
import uuid

# Valores por defecto
host = "localhost"
puerto = 9999

# Procesar argumentos de línea de comandos
if len(sys.argv) > 3:
	print("Uso: python udp_cliente5_mejorado.py <host> <puerto>")
	sys.exit(1)
elif len(sys.argv) == 3:
	host = sys.argv[1]
	puerto = int(sys.argv[2])
elif len(sys.argv) == 2:
	host = sys.argv[1]

# Crear socket UDP
cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
	mensaje = input("Introduce mensaje (FIN para terminar): ")
	if mensaje == "FIN":
		break
	# Generar identificador único para el mensaje
	id_mensaje = str(uuid.uuid4())
	datagrama = f"{id_mensaje}|{mensaje}"

	t = 0.1
	while True:
		cliente.sendto(datagrama.encode(), (host, puerto))
		try:
			cliente.settimeout(t)
			respuesta, addr = cliente.recvfrom(1024)
			respuesta_dec = respuesta.decode()
			# Espera formato: OK|<id>
			if respuesta_dec.startswith("OK|"):
				id_ack = respuesta_dec.split('|', 1)[1]
				if id_ack == id_mensaje:
					print(f"Confirmación recibida para el mensaje: {mensaje}")
					break
				else:
					print(f"ACK recibido para otro mensaje: {id_ack}")
			else:
				print(f"Respuesta inesperada: {respuesta_dec}")
		except socket.timeout:
			t *= 2
			if t > 2:
				print("Puede que el servidor esté caído. Inténtelo más tarde")
				cliente.close()
				sys.exit(1)
			print("No se recibió respuesta del servidor, reintentando...")

cliente.close()

