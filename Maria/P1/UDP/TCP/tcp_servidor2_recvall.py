import socket
import sys
import time

PORT = 9999
if len(sys.argv) > 1:
    PORT = int(sys.argv[1])


def recvall(sock, n):
    """
    Lee exactamente n bytes del socket, o devuelve None si se cierra.
    """
    datos = b''
    while len(datos) < n:
        # Intentamos leer lo que nos falta (n - lo que ya tenemos)
        paquete = sock.recv(n - len(datos))
        if not paquete:
            return None
        datos += paquete
    return datos


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", PORT))
s.listen(5)

print(f"Servidor TCP (recvall) esperando en puerto {PORT}...")

while True:
    sd, origen = s.accept()
    print("Cliente aceptado. Pausa dramática de 1s...")
    import time
    time.sleep(1)
    print(f"--> Conexión de: {origen}")

    continuar = True
    while continuar:
        # Usamos recvall en lugar de recv
        datos_bytes = recvall(sd, 5)
        
        if not datos_bytes:
            print("Conexión cerrada por el cliente.")
            sd.close()
            break
            
        texto = datos_bytes.decode("utf-8")
        
        if texto == "FINAL":
            print("Recibido FINAL. Cerrando con este cliente.")
            sd.close()
            continuar = False
        else:
            print(f"Recibido bloque completo: {texto}")