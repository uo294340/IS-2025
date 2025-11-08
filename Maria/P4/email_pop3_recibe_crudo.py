import socket
import sys
import ssl
import getpass

# --- 1. Definir la función RecvReply ---
# Esta vez, comprobamos que la respuesta empiece por b'+OK'
def RecvReply(sc):
    try:
        respuesta = sc.recv(1024)
        print(f"S: {respuesta.decode('utf-8').strip()}") # .strip() quita saltos de línea

        if not respuesta.startswith(b'+OK'):
            print(f"Error: El servidor no respondió con +OK. Respondió: {respuesta.decode('utf-8')}")
            sys.exit(1)
            
        return respuesta # Devolvemos la respuesta por si la necesitamos
        
    except Exception as e:
        print(f"Error al recibir respuesta: {e}")
        sys.exit(1)

# --- 2. Definir variables ---
server = "pop.gmail.com"
port = 995 # Puerto de POP3 sobre SSL

try:
    # --- 3. Leer usuario y contraseña ---
    username = input("Usuario (tu email de Gmail completo): ")
    password = getpass.getpass("Contraseña (¡la de Aplicación de 16 letras!): ")
except EOFError:
    sys.exit("Entrada cancelada.")

try:
    # --- 4. Conectar y "envolver" con SSL ---
    print(f"Conectando a {server}:{port}...")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server, port))
    
    # POP3 de Gmail usa SSL directo, no STARTTLS.
    # "Envolvemos" el socket desde el principio.
    context = ssl.create_default_context()
    sc = context.wrap_socket(s, server_hostname=server)
    print("--- Canal seguro (SSL) establecido ---")

    # El servidor nos da la bienvenida
    RecvReply(sc) 

    # --- 5. Enviar comandos POP3 ---
    
    # 1. USER
    user_cmd = f"USER {username}\r\n".encode('utf-8')
    print(f"C: USER {username}")
    sc.sendall(user_cmd)
    RecvReply(sc) # Esperamos +OK

    # 2. PASS
    pass_cmd = f"PASS {password}\r\n".encode('utf-8')
    print("C: PASS [CONTRASENA OCULTA]")
    sc.sendall(pass_cmd)
    RecvReply(sc) # Esperamos +OK

    # 3. STAT (Estadísticas del buzón)
    print("C: STAT")
    sc.sendall(b'STAT\r\n')
    respuesta_stat = RecvReply(sc) # Ej: "+OK 2 3456" (2 mensajes, 3456 bytes)

    # 4. RETR (Retrieve - Descargar el primer mensaje)
    print("C: RETR 1")
    sc.sendall(b'RETR 1\r\n')
    
    # Leemos la primera línea de respuesta (debería ser +OK)
    respuesta_retr = sc.recv(1024).decode('utf-8')
    print(f"S: {respuesta_retr.strip()}")
    
    if not respuesta_retr.startswith('+OK'):
        print("Error al descargar el mensaje 1.")
        sys.exit(1)

    # --- 6. Bucle para recibir el mensaje completo ---
    # El mensaje termina con una línea que contiene solo un punto: \r\n.\r\n
    print("S: [Recibiendo mensaje 1...]")
    mensaje_completo_bytes = b''
    while True:
        linea = sc.recv(4096) # Leemos en trozos
        if linea.endswith(b'\r\n.\r\n'):
            # Si encontramos la marca final, la quitamos y salimos
            mensaje_completo_bytes += linea[:-5] # Quitamos el \r\n.\r\n
            break
        else:
            mensaje_completo_bytes += linea

    # Convertimos el mensaje (bytes) a texto para analizarlo
    mensaje_texto = mensaje_completo_bytes.decode('utf-8', 'ignore')

    # --- 7. Extraer cabeceras "From" y "Subject" (modo simple) ---
    print("\n--- Cabeceras del Mensaje 1 ---")
    from_line = ""
    subject_line = ""

    for linea in mensaje_texto.split('\n'):
        if linea.lower().startswith('from:'):
            from_line = linea.strip()
        if linea.lower().startswith('subject:'):
            subject_line = linea.strip()
        
        # Dejamos de buscar cuando encontramos una línea vacía (fin de cabeceras)
        if linea.strip() == "":
            break
            
    print(from_line)
    print(subject_line)
    print("---------------------------------")

    # 8. QUIT
    print("C: QUIT")
    sc.sendall(b'QUIT\r\n')
    RecvReply(sc) # Esperamos el +OK de despedida

except Exception as e:
    print(f"\n[ERROR] Ocurrió un error: {e}")
finally:
    if 'sc' in locals():
        sc.close()
    if 's' in locals():
        s.close()
    print("Conexión cerrada.")