import socket
import time

def recibe_mensaje(sock):
    buffer = []
    while True:
        byte = sock.recv(1)
        if not byte:
            return b""
        buffer.append(byte)
        if len(buffer) >= 2 and buffer[-2:] == [b'\r', b'\n']:
            return b"".join(buffer)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 9999))
s.listen(1)

print("Servidor escuchando en puerto 9999")

while True:
    sd, origen = s.accept()
    print("Cliente conectado:", origen)
    time.sleep(1)
    f= sd.makefile(encoding="utf8", newline="\r\n")

    while True:
        mensaje = f.readline()
        if not mensaje:  # cliente cerró
            break
        print("Recibido:", mensaje.strip())
        linea = mensaje.strip()   # quitar \r\n
        respuesta = linea[::-1]    # invertir
        sd.sendall((respuesta + "\r\n").encode("utf8"))

    sd.close()
    print("Cliente desconectado:", origen)