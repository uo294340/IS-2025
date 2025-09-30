import socket


servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
servidor.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
puerto = 12345
servidor.bind(("0.0.0.0", puerto)) 
print(f"Servidor HOLA activado en el puerto {puerto}")
    
while True:
    datos, direccion = servidor.recvfrom(1024)
    mensaje = datos.decode()
    print(f"DEBUG1 '{mensaje}' de {direccion}")
    if mensaje == "BUSCANDO HOLA":
            # Responder que implementa HOLA
        servidor.sendto(b"IMPLEMENTO HOLA", direccion)
        print(f"DEBUG2 MANDADO ""IMPLEMENTO HOLA"" a {direccion}")
    elif mensaje == "HOLA":
            # Responder con HOLA: IP
        respuesta = f"HOLA: {direccion[0]}"
        servidor.sendto(respuesta.encode(), direccion)
        print(f"DEBUG3 RESPUESTA MANDADA {respuesta} a {direccion}")
	
