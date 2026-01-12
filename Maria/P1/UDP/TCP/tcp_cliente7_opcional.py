import sys
import socket
import struct

# Parámetros
if len(sys.argv) > 3:
    print("Uso: python tcp_cliente7_opcional.py [<ip-servidor> <puerto>]")
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

# Conexión
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect((ip_servidor, puerto))
print(f"Conectado a {ip_servidor}:{puerto}")

file = c.makefile("rwb")

lineas = ["HOLA", "PYTHON", "REDES", "BINARIO"]

for linea in lineas:
    datos_bytes = linea.encode("utf8")
    
    # 1. ENVIAR (Cabecera binaria 2 bytes + Datos)
    cabecera = struct.pack(">H", len(datos_bytes))
    
    file.write(cabecera)
    file.write(datos_bytes)
    file.flush()
    print("Enviado:", linea)

    # 2. RECIBIR RESPUESTA
    # Leemos primero los 2 bytes de longitud
    cabecera_resp = file.read(2)
    if not cabecera_resp:
        break
        
    longitud_resp = struct.unpack(">H", cabecera_resp)[0]
    
    # Leemos el cuerpo del mensaje
    respuesta = file.read(longitud_resp).decode("utf8")
    print("Recibido:", respuesta)

file.close()
c.close()
print("Conexión cerrada")