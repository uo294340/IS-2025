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

#lectura con ficheros (readline())
file = c.makefile("rwb") # read-write binary

# Algunas líneas de prueba (todas terminan en \r\n)
lineas = ["HOLA", "PYTHON", "REDES", "PRUEBA"]

for linea in lineas:
    # Enviar la línea + longitud del mensaje (añadimos el delimitador para que sepa donde acaba la longitud)
    longitud = f"{len(linea.encode('utf8'))}\n"
    file.write(longitud.encode("utf8"))
    file.write(linea.encode("utf8"))
    file.flush() # forzar envío
    
    print("Enviado:", linea.strip())

    # Recibir respuesta del servidor
    longitud_respuesta = file.readline().decode("utf8").strip()
    if not longitud_respuesta:  # servidor cerró
        break
    longitud_respuesta = int(longitud_respuesta)
    respuesta = file.read(longitud_respuesta).decode("utf8")
    print("Recibido:", respuesta)

# Cerrar conexión
file.close()
c.close()
print("Conexión cerrada")
