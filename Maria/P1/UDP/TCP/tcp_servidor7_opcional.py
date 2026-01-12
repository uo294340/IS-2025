import socket
import time
import struct
import sys

# Configuración del puerto
PORT = 9999
if len(sys.argv) > 1:
    PORT = int(sys.argv[1])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", PORT))
s.listen(1)

print(f"Servidor OCHE (Binario >H) escuchando en puerto {PORT}")

while True:
    sd, origen = s.accept()
    # time.sleep(1) # Mantenemos el retardo para demostrar robustez
    print("Cliente conectado:", origen)
    
    # 'rwb' es crucial aquí para leer bytes crudos para struct
    file = sd.makefile("rwb") 

    while True:
        # 1. LEER CABECERA (2 bytes fijos)
        # >H son 2 bytes. Si no leemos 2, es que se cerró la conexión.
        cabecera = file.read(2)
        if not cabecera or len(cabecera) < 2: 
            break
            
        # Desempaquetamos: >H = Big Endian, Unsigned Short
        # unpack devuelve una tupla, por eso usamos [0]
        longitud = struct.unpack(">H", cabecera)[0]

        # 2. LEER MENSAJE (Exactamente 'longitud' bytes)
        mensaje_bytes = file.read(longitud)
        if len(mensaje_bytes) < longitud:
            break # Cliente cerró a medias

        mensaje = mensaje_bytes.decode("utf8")
        print("Recibido:", mensaje)
        
        # Procesar
        respuesta = mensaje[::-1]
        respuesta_bytes = respuesta.encode("utf8")

        # 3. ENVIAR RESPUESTA (Cabecera binaria + Datos)
        # Empaquetamos la longitud en 2 bytes
        cabecera_resp = struct.pack(">H", len(respuesta_bytes))
        
        file.write(cabecera_resp)
        file.write(respuesta_bytes)
        file.flush()
        print("Enviado:", respuesta)
        
    file.close()
    sd.close()
    print("Cliente desconectado:", origen)