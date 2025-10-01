# Creación del socket de escucha
import socket
import sys


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
# Podríamos haber omitido los parámetros, pues por defecto `socket()` en python
# crea un socket de tipo TCP
if len(sys.argv)>2:
    print("Uso python tcp_servidor1_simple.py ip puertos")
    sys.exit(1)
elif len(sys.argv)==1:
    puerto=9999
else:
    puerto=int(sys.argv[1])
# Asignarle puerto
s.bind(("", puerto))

# Ponerlo en modo pasivo
s.listen(5)  # Máximo de clientes en la cola de espera al accept()

while True:
    print("Esperando un cliente")
    sd, origen = s.accept()
    print("Nuevo cliente conectado desde %s, %d" % origen)
    continuar = True
    # Bucle de atención al cliente conectado
    while continuar:
        # Primero recibir el mensaje del cliente
        mensaje = sd.recv(80)  # Nunca enviará más de 80 bytes, aunque tal vez sí menos
        mensaje = str(mensaje, "utf8") # Convertir los bytes a caracteres

        # Segundo, quitarle el "fin de línea" que son sus 2 últimos caracteres
        linea = mensaje[:-2]  # slice desde el principio hasta el final -2

        # Tercero, darle la vuelta
        linea = linea[::-1]

        # Finalmente, enviarle la respuesta con un fin de línea añadido
        # Observa la transformación en bytes para enviarlo
        sd.sendall(bytes(linea+"\r\n", "utf8"))
        if not mensaje:  # Si no se reciben datos, es que el cliente cerró el socket
            continuar = False
            sd.send(("Conexión cerrada por el cliente").encode("ascii"))
            sd.close()
            print("Conexión cerrada por el cliente")