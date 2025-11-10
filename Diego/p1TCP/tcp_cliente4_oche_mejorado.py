import sys
import socket

def recibe_mensaje(sock):
    buffer = []
    while True:
        byte = sock.recv(1)
        if not byte:
            return b""
        buffer.append(byte)
        if len(buffer) >= 2 and buffer[-2:] == [b'\r', b'\n']:
            return b"".join(buffer)
        
# Parámetros: ip y puerto, o localhost:9999 por defecto
if len(sys.argv) > 3:
    print("Uso: python tcp_cliente3_oche.py [<ip-servidor> <puerto>]")
    sys.exit(1)
elif len(sys.argv) == 1:
    ip_servidor = "localhost"
    puerto = 9999
elif len(sys.argv) == 2:
    ip_servidor = sys.argv[1]
    puerto = 9999
else:
    ip_servidor = sys.argv[1]
    puerto = int(sys.argv[2])

# Crear socket cliente
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect((ip_servidor, puerto))
print(f"Conectado a {ip_servidor}:{puerto}")

# Algunas líneas de prueba (todas terminan en \r\n)
lineas = ["HOLA\r\n", "PYTHON\r\n", "REDES\r\n", "PRUEBA\r\n"]
for i in range(0, len(lineas), 3):  # Enviar todo 3 veces seguidas
    grupo = lineas[i:i+3] #cogemos las 3 lineas a la vez grupo = "hola", "python", "redes"
    #ahora se envian las 3 lineas primero
    for linea in grupo:
        # Enviar la línea
        c.sendall(linea.encode("utf8"))
        print("Enviado:", linea.strip())
        
    for _ in grupo:  #ahora se reciben las 3 respuestas
        # Recibir respuesta del servidor
        respuesta = recibe_mensaje(c).decode("utf8").strip()
        print(repr(respuesta))

# Cerrar conexión
c.close()
print("Conexión cerrada")
