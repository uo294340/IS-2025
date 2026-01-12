import socket
import sys

SERVER_IP = "localhost"
SERVER_PORT = 9999
if len(sys.argv) == 3:
    SERVER_IP = sys.argv[1]
    SERVER_PORT = int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# MEJORA 1: Usamos connect().
# Esto fija la dirección destino y FILTRA paquetes de otros orígenes.
s.connect((SERVER_IP, SERVER_PORT))

print(f"Cliente MEJORADO conectado a {SERVER_IP}:{SERVER_PORT}")

contador = 1

while True:
    texto = input(f"Mensaje {contador}: ")
    if texto == "FIN":
        break

    mensaje_con_numero = f"{contador}: {texto}"
    
    # Lógica de reintentos (igual que en Ej4)
    timeout_actual = 0.5
    s.settimeout(timeout_actual)
    confirmado = False
    
    while timeout_actual <= 2.0:
        try:
            # Al usar connect(), usamos send() en vez de sendto()
            s.send(mensaje_con_numero.encode("utf-8"))
            
            # Al usar connect(), usamos recv() en vez de recvfrom()
            # Ya no nos devuelve la dirección (sabemos que es del servidor)
            datos = s.recv(1024)
            respuesta = datos.decode("utf-8")
            
            # MEJORA 2: Verificamos que el ACK confirma ESTE mensaje
            ack_esperado = f"OK {contador}"
            
            if respuesta == ack_esperado:
                print(f"  Confirmado correctamente: {respuesta}")
                confirmado = True
                break
            else:
                print(f" Recibido ACK extraño: {respuesta} (Esperaba {ack_esperado})")
                
        except socket.timeout:
            print("  Timeout. Reintentando...")
            timeout_actual *= 2
            s.settimeout(timeout_actual)
        except ConnectionRefusedError:
            # connect() a veces permite detectar si el puerto está cerrado inmediatamente
            print("Error: Puerto no alcanzable (ICMP Port Unreachable).")
            break

    if not confirmado:
        print(" Servidor no responde.")
        break

    contador += 1

s.close()