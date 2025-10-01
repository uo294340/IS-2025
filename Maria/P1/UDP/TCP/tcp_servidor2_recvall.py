import sys
import socket
# Creación del socket de escucha
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
# Podríamos haber omitido los parámetros, pues por defecto `socket()` en python
# crea un socket de tipo TCP

def recvall(socket, n):
    datos = b""  # acumulador en bytes
    while len(datos) < n:
        paquete = socket.recv(n - len(datos))
        if not paquete:  # si el cliente cerró la conexión
            return ""
        datos += paquete
    return datos.decode("ascii")


#El puerto en que debe escuchar lo recibirá por línea de comandos o usará un valor por defecto de 9999 si no se especifica
if len(sys.argv) > 2:
    print("Uso: python tcp_servidor1_simple.py <puerto>")
    sys.exit(1)
elif len(sys.argv) == 1:
    puerto = 9999;  # Puerto por defecto
else:
    puerto = int(sys.argv[1])


# Asignarle puerto
s.bind(("", puerto))

# Ponerlo en modo pasivo
s.listen(5)  # Máximo de clientes en la cola de espera al accept()

# Bucle principal de espera por clientes
while True:
    print("Esperando un cliente")
    sd, origen = s.accept()
    print("Nuevo cliente conectado desde %s, %d" % origen)
    continuar = True
    # Bucle de atención al cliente conectado
    while continuar:
        datos = recvall(sd, 5)  # Observar que se lee del socket sd, no de s
        
        if datos=="":  # Si no se reciben datos, es que el cliente cerró el socket
            print("Conexión cerrada de forma inesperada por el cliente")
            sd.close()
            continuar = False
        elif datos=="FINAL":
            print("Recibido mensaje de finalización")
            sd.close()
            continuar = False
        else:
            print("Recibido mensaje: %s" % datos)
            #mandar respuesta al cliente
            sd.send(b"Recibido")