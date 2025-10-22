import socket

def mostrar_hex(respuesta):
    for byte in respuesta:
        print(hex(byte), end=' ')
    print()

s = socket.socket()
s.connect(("localhost", 23))
respuesta = s.recv(1024)
mostrar_hex(respuesta)
s.close()


