import socket
import sys

# Valores por defecto
host = "localhost"
puerto = 9999

# Procesar argumentos de línea de comandos
#sys.argv es una lista de los argumentos de la línea de comandos
#sys.argv[1] es el nombre del script y los 2 otros argumentos el host y el puerto por eso si tiene más de 3 se excede
if len(sys.argv) > 3:
    print("Uso: python udp_cliente1.py <host> <puerto>")
    sys.exit(1)
elif len(sys.argv) == 3:
    host = sys.argv[1]
    puerto = int(sys.argv[2])
elif len(sys.argv) == 2:
    host = sys.argv[1]

# Crear socket UDP
cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

n = 1
cliente.settimeout(2)
while True:
    mensaje = input("Introduce mensaje (FIN para terminar): ")
    if mensaje == "FIN":
        break
    mensaje_n = f"{n}: {mensaje}"
    cliente.sendto(mensaje_n.encode(), (host, puerto))
    try:
        #esperar respuesta del servidor
        respuesta, _ = cliente.recvfrom(1024)
        print(f"Respuesta del servidor: {respuesta.decode()}")
    except socket.timeout:
        print("No se recibió respuesta del servidor")
    n += 1

    

cliente.close()