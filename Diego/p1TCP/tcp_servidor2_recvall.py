# Creación del socket de escucha
import socket
import sys

def recvall(sock,length):
    datos=b""
    while len(datos)<length:
        more=sock.recv(length-len(datos))
        if not more:
            raise EOFError("Se cerro la conexion antes de recibir todos los datos")
    return datos
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
# Podríamos haber omitido los parámetros, pues por defecto `socket()` en python
# crea un socket de tipo TCP
if len(sys.argv)>2:
    print("Uso python tcp_servidor2_recvall.py ip puertos")
    sys.exit(1)
elif len(sys.argv)==1:
    puerto=9999
else:
    puerto=int(sys.argv[1])
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
        datos=recvall(sd,5)  # Observar que se lee del socket sd, no de s
        datos = datos.decode("ascii")  # Pasar los bytes a caracteres
                # En este ejemplo se asume que el texto recibido es ascii puro
        if datos=="":  # Si no se reciben datos, es que el cliente cerró el socket
            print("Conexión cerrada de forma inesperada por el cliente")
            sd.close()
            continuar = False
        elif datos=="FINAL":
            print("Recibido mensaje de finalización")
            sd.send(("Recibido mensaje FINAL, cerrando conexion").encode("ascii"))
            sd.close()
            continuar = False
        else:
            print("Recibido mensaje: %s" % datos)
            sd.send(("Recibido mensaje pero no FINAL").encode("ascii"))