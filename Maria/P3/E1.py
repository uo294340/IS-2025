import socket
 
s = socket.socket()
s.connect(("localhost", 23))
respuesta = s.recv(1024)
#print(respuesta)

def to_hex(data):
    hex_string = ""
    for byte in data:
        hex_string += hex(byte) + " "
    print(hex_string)
    
to_hex(respuesta)