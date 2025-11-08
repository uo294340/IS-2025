import socket
import sys
import email.message
import email.utils

# --- PASO 1: Definir la función RecvReply ---
# Esta función nos ayuda a leer la respuesta del servidor y
# comprobar si el código de 3 dígitos es el que esperamos.
def RecvReply(s, codigo_esperado=b'250'):
    try:
        # Recibimos hasta 1024 bytes
        respuesta = s.recv(1024)
        print(f"S: {respuesta.decode('utf-8')}") # S: (Respuesta del Servidor)

        # Extraemos los 3 primeros bytes (el código)
        codigo_recibido = respuesta[:3]

        # Verificamos si coincide con el código que esperábamos
        if codigo_recibido != codigo_esperado:
            print(f"Error: Se esperaba el código {codigo_esperado.decode('utf-8')}, pero se recibió {codigo_recibido.decode('utf-8')}")
            # sys.exit(1) # Terminamos el programa si hay error
    except Exception as e:
        print(f"Error al recibir respuesta: {e}")
        sys.exit(1)

# --- PASO 2: Definir variables ---
server = "relay.uniovi.es"
port = 25 # Puerto estándar SMTP
fromaddr = "uo294340@uniovi.es"
toaddr = "uo294340@uniovi.es"
subject = "Prueba SMTP 'en crudo' (Ejercicio 7)"
data = "Hola,\nEste es un mensaje de prueba enviado con un socket 'crudo'."

# --- PASO 3: Crear el mensaje con email.message (Modo Ej. 8) ---

# 1. Crear el objeto EmailMessage
msg = email.message.EmailMessage()

# 2. Añadir las cabeceras (como un diccionario)
msg['To'] = toaddr
msg['From'] = fromaddr
msg['Subject'] = subject
msg['Date'] = email.utils.formatdate(localtime=True) # Añade fecha
msg['Message-ID'] = email.utils.make_msgid()         # Añade ID único

# 3. Añadir el cuerpo del mensaje
msg.set_content(data) # Esto maneja tildes y acentos por nosotros

# 4. Convertir el mensaje a bytes
message_bytes = msg.as_bytes()

# 5. ¡IMPORTANTE! Añadir el punto final para el modo "crudo"
# La librería smtplib lo añade sola, pero nosotros no la usamos
message_bytes += b'\r\n.\r\n'

# --- PASO 4: Conexión TCP ---
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server, port))
    
    # El servidor nos da la bienvenida (código 220)
    RecvReply(s, codigo_esperado=b'220')

    # --- PASO 5: Enviar comandos SMTP ---
    
    # 1. HELO: Nos presentamos
    helo_cmd = b'HELO mi-pc-de-practicas\r\n'
    print(f"C: {helo_cmd.decode('utf-8')}") # C: (Comando del Cliente)
    s.sendall(helo_cmd)
    RecvReply(s, codigo_esperado=b'250') # Esperamos un "250 OK"

    # 2. MAIL FROM: Indicamos el remitente
    mail_from_cmd = f"MAIL FROM:<{fromaddr}>\r\n".encode('utf-8')
    print(f"C: {mail_from_cmd.decode('utf-8')}")
    s.sendall(mail_from_cmd)
    RecvReply(s, codigo_esperado=b'250')

    # 3. RCPT TO: Indicamos el destinatario
    rcpt_to_cmd = f"RCPT TO:<{toaddr}>\r\n".encode('utf-8')
    print(f"C: {rcpt_to_cmd.decode('utf-8')}")
    s.sendall(rcpt_to_cmd)
    RecvReply(s, codigo_esperado=b'250')

    # 4. DATA: Le decimos que vamos a enviar el mensaje
    data_cmd = b'DATA\r\n'
    print(f"C: {data_cmd.decode('utf-8')}")
    s.sendall(data_cmd)
    RecvReply(s, codigo_esperado=b'354') # Esperamos "354 Start mail input"

    # 5. Enviar el mensaje completo
    print("C: [Enviando datos del mensaje...]")
    s.sendall(message_bytes)
    RecvReply(s, codigo_esperado=b'250') # Esperamos "250 OK: Queued"

    # 6. QUIT: Cerramos la conexión
    quit_cmd = b'QUIT\r\n'
    print(f"C: {quit_cmd.decode('utf-8')}")
    s.sendall(quit_cmd)
    RecvReply(s, codigo_esperado=b'221') # Esperamos "221 Bye"

    print("\n¡Correo enviado con éxito!")

except Exception as e:
    print(f"Error durante la conexión SMTP: {e}")
finally:
    # --- PASO 6: Cerrar el socket ---
    s.close()