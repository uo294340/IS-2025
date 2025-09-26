import socket

puerto = 12345
    # Crear socket UDP
servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # activar modo broadcast
servidor.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    # Asociar el socket al puerto y a todas las interfaces
servidor.bind(("0.0.0.0", puerto)) 
print(f"Servidor HOLA escuchando en puerto {puerto} (broadcast activado)")
    
while True:
    datos, direccion = servidor.recvfrom(1024)
    mensaje = datos.decode()
    print(f"Recibido '{mensaje}' de {direccion}")
    if mensaje == "BUSCANDO HOLA":
            # Responder que implementa HOLA
        servidor.sendto(b"IMPLEMENTO HOLA", direccion)
        print(f"Respondido IMPLEMENTO HOLA a {direccion}")
    elif mensaje == "HOLA":
            # Responder con HOLA: IP
        respuesta = f"HOLA: {direccion[0]}".encode()
        servidor.sendto(respuesta, direccion)
        print(f"Respondido {respuesta.decode()} a {direccion}")
	
