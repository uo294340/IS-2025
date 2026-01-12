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

    while True:
        mensaje = sd.recv(80)
        if not mensaje:  # cliente cerró
            break

        mensaje = mensaje.decode("utf8")
        linea = mensaje[:-2]   # quitar \r\n
        linea = linea[::-1]    # invertir
        sd.sendall((linea + "\r\n").encode("utf8"))

    sd.close()
    print("Cliente desconectado:", origen)