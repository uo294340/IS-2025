import socket
import sys
import random

if len(sys.argv)>2:
    print("Uso python udp_servidor1.py puertos")
    sys.exit(1)
elif len(sys.argv)==1:
    puerto=9999
else:
    puerto=int(sys.argv[1])

#socket udp

servidor=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
servidor.bind(('localhost',puerto))
print(f"Servidor UDP escuchando en el puerto {puerto}")

while True:
    num=random.randint(0,1)
    print(num)
    datos,direccion=servidor.recvfrom(1024)
    if(num==1):
        print(f"Recibido {datos.decode()} de {direccion}")
        servidor.sendto(b"OK",direccion)
    else:
     print("Simulando paquete perdido")