import sys
import socket

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

for linea in lineas:
    # Enviar la línea
    c.sendall(linea.encode("utf8"))
    print("Enviado:", linea.strip())

    # Recibir respuesta del servidor
    respuesta = c.recv(80).decode("utf8").strip()
    print("Recibido:", respuesta)

# Cerrar conexión
c.close()
print("Conexión cerrada")
