import socket
import sys
import random

if len(sys.argv)>1:
    puerto=int(sys.argv[1])
else:
    puerto=9999

servidor=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
servidor.bind(('',puerto))
print(f"Servidor UDP escuchando en el puerto {puerto}")

while True:
    datos,direccion=servidor.recvfrom(1024)
    
    # Decidimos si se pierde (0) o se procesa (1)
    num=random.randint(0,1)
    
    if(num==1):
        # CASO ÉXITO: Lo mostramos 
        print(f"Recibido {datos.decode()} de {direccion}")
    else:
        # CASO PÉRDIDA: Solo imprimimos para nosotros, pero NO respondemos al cliente
        print("Simulando paquete perdido")
        