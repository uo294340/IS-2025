import socket
import sys
import random

if len(sys.argv) > 2:
	print("Uso: python udp_servidor5_mejorado.py <puerto>")
	sys.exit(1)
elif len(sys.argv) == 1:
	puerto = 9999  # Puerto por defecto
else:
	puerto = int(sys.argv[1])

servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
servidor.bind(('localhost', puerto))
print(f"Servidor UDP escuchando en el puerto {puerto}")

# Lista de identificadores ya procesados
ids_recibidos = set()

while True:
	datos, direccion = servidor.recvfrom(1024)
	try:
		recibido = datos.decode()
		# Espera formato: <id>|<mensaje>
		id_mensaje, mensaje = recibido.split('|', 1)
	except Exception:
		print(f"Formato incorrecto de datagrama: {datos}")
		continue

	# Simular pérdida de paquetes con una probabilidad del 50%
	if random.random() < 0.5:
		print(f"Simulando pérdida de paquete de {direccion}")
		continue

	if id_mensaje not in ids_recibidos:
		print(f"Mensaje nuevo recibido: {mensaje} de {direccion} (id={id_mensaje})")
		# Aquí iría la acción asociada al mensaje
		ids_recibidos.add(id_mensaje)
	else:
		print(f"Duplicado recibido: {mensaje} de {direccion} (id={id_mensaje})")

	# Enviar ACK con el identificador
	ack = f"OK|{id_mensaje}"
	servidor.sendto(ack.encode(), direccion)
