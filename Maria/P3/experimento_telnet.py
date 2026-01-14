import socket

s = socket.socket()
s.connect(("localhost", 23))
respuesta = s.recv(1024)

print("Respuesta en crudo:", respuesta)

# Pequeño bucle para ver hexadecimal
print("Hexadecimal:")
for byte in respuesta:
    print(hex(byte), end=" ")
print()
