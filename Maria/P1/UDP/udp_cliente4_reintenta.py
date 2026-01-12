import socket
import sys

# Valores por defecto
host = "localhost"
puerto = 9999

if len(sys.argv) > 3:
    print("Uso: python udp_cliente4.py <host> <puerto>")
    sys.exit(1)
elif len(sys.argv) == 3:
    host = sys.argv[1]
    puerto = int(sys.argv[2])
elif len(sys.argv) == 2:
    host = sys.argv[1]

cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

n = 1

while True:
    mensaje = input(f"Introduce mensaje {n} (FIN para terminar): ")
    if mensaje == "FIN":
        break
    
    mensaje_n = f"{n}: {mensaje}"
    
    
    t = 0.1             # Reiniciamos el timeout inicial para CADA mensaje nuevo
    confirmado = False  # Bandera para saber si lo logramos
    
    # Bucle: Mientras no excedamos los 2 segundos...
    while t <= 2.0:
        try:
            print(f"   -> Enviando (Timeout: {t}s)...")
            cliente.sendto(mensaje_n.encode(), (host, puerto))
            
            cliente.settimeout(t)
            respuesta, _ = cliente.recvfrom(1024)
            
            # Si llegamos aquí, es que NO hubo timeout
            print(f"  Respuesta del servidor: {respuesta.decode()}")
            confirmado = True
            break # Salimos del bucle de reintentos (¡Éxito!)
            
        except socket.timeout:
            print("  Timeout. No hubo respuesta. Preparando reintento...")
            t *= 2 # Duplicamos el tiempo para el siguiente intento
            
    # Si salimos del bucle y NO se confirmó, es que nos rendimos (t > 2)
    if not confirmado:
        print("ERROR: Puede que el servidor esté caído. Inténtelo más tarde.")
        cliente.close()
        sys.exit(1) # Cerramos el programa por completo
        
    n += 1 # Solo incrementamos si se confirmó el anterior

cliente.close()