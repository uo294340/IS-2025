import socket
import sys
import ssl
import getpass
import re # Importamos re para parsear la respuesta de STAT

# --- Función RecvReply (Igual que antes) ---
def RecvReply(sc, check_ok=True):
    try:
        respuesta = sc.recv(4096)
        # Mostramos solo los primeros 100 bytes para no llenar la consola
        print(f"S: {respuesta.decode('utf-8', 'ignore').strip()[:100]}...")

        if check_ok and not respuesta.startswith(b'+OK'):
            print(f"Error: El servidor no respondió con +OK. Respondió: {respuesta.decode('utf-8')}")
            sys.exit(1)
            
        return respuesta # Devolvemos la respuesta
        
    except Exception as e:
        print(f"Error al recibir respuesta: {e}")
        sys.exit(1)

# --- Función para parsear cabeceras ---
def parse_headers(header_bytes):
    from_line = "<From desconocido>"
    subject_line = "<Sin Asunto>"
    try:
        header_text = header_bytes.decode('utf-8', 'ignore')
        for linea in header_text.split('\n'):
            if linea.lower().startswith('from:'):
                from_line = linea.strip()
            if linea.lower().startswith('subject:'):
                subject_line = linea.strip()
    except Exception:
        pass # Ignorar errores de decodificación por ahora
    return from_line, subject_line

# --- 1. Definir variables y pedir credenciales ---
server = "pop.gmail.com"
port = 995
try:
    username = input("Usuario (tu email de Gmail, usa 'recent:' si es necesario): ")
    password = getpass.getpass("Contraseña (¡la de Aplicación de 16 letras!): ")
except EOFError:
    sys.exit("Entrada cancelada.")

try:
    # --- 2. Conectar y "envolver" con SSL ---
    print(f"Conectando a {server}:{port}...")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server, port))
    context = ssl.create_default_context()
    sc = context.wrap_socket(s, server_hostname=server)
    print("--- Canal seguro (SSL) establecido ---")
    RecvReply(sc) # Bienvenida

    # --- 3. Autenticación (USER/PASS) ---
    print(f"C: USER {username}")
    sc.sendall(f"USER {username}\r\n".encode('utf-8'))
    RecvReply(sc)

    print("C: PASS [CONTRASENA OCULTA]")
    sc.sendall(f"PASS {password}\r\n".encode('utf-8'))
    RecvReply(sc)

    # --- 4. STAT (Para saber cuántos mensajes hay) ---
    print("C: STAT")
    sc.sendall(b'STAT\r\n')
    respuesta_stat = RecvReply(sc).decode('utf-8') # Ej: "+OK 3 5000"
    
    try:
        num_mensajes = int(respuesta_stat.split(' ')[1])
        print(f"Buzón tiene {num_mensajes} mensajes.")
    except Exception:
        print("Error, no se pudo leer el número de mensajes desde STAT.")
        num_mensajes = 0

    if num_mensajes == 0:
        print("No hay mensajes nuevos que mostrar.")
    
    # --- 5. Bucle para leer TODOS los mensajes (usando TOP) ---
    for i in range(1, num_mensajes + 1):
        print(f"\n--- Leyendo cabeceras del mensaje {i} ---")
        cmd = f"TOP {i} 0\r\n".encode('utf-8')
        print(f"C: TOP {i} 0")
        sc.sendall(cmd)
        
        # Leemos la respuesta completa del TOP
        cabeceras_bytes = b''
        while True:
            linea = sc.recv(4096)
            if linea.endswith(b'\r\n.\r\n'):
                cabeceras_bytes += linea[:-5] # Quitamos el \r\n.\r\n
                break
            else:
                cabeceras_bytes += linea
        
        # Parseamos e imprimimos
        from_val, subject_val = parse_headers(cabeceras_bytes)
        print(from_val)
        print(subject_val)

    # 6. QUIT
    print("\nC: QUIT")
    sc.sendall(b'QUIT\r\n')
    RecvReply(sc)

except Exception as e:
    print(f"\n[ERROR] Ocurrió un error: {e}")
finally:
    if 'sc' in locals():
        sc.close()
    if 's' in locals():
        s.close()
    print("Conexión cerrada.")