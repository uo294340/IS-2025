import socket
import time


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 9999))
s.listen(1)

print("Servidor escuchando en puerto 9999")

while True:
    sd, origen = s.accept()
    time.sleep(1)
    print("Cliente conectado:", origen)
    
    file = sd.makefile("rwb") # read-write binary

    while True:
        #leemos la longitud del mensaje
        longitud = file.readline().decode("utf8").strip()
        if not longitud:  # cliente cerró
            break
        try:
            longitud = int(longitud)
        except ValueError:
            print("Error: Longitud inválida recibida. Cerrando conexión.")
            break
        mensaje = file.read(longitud).decode("utf8")
        if not mensaje:  # cliente cerró
            break
        print("Recibido:", mensaje)
        respuesta = mensaje[::-1]    # invertir
        longitud_respuesta = f"{len(respuesta.encode('utf8'))}\n"
        file.write(longitud_respuesta.encode("utf8"))
        file.write(respuesta.encode("utf8"))
        file.flush() # forzar envío
        print("Enviado:", respuesta)
        
    file.close()
    sd.close()
    print("Cliente desconectado:", origen)