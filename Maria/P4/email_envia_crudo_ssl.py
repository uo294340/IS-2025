import socket
import sys
import ssl         # Para el cifrado (STARTTLS)
import base64      # Para la autenticación (AUTH LOGIN)
import getpass     # Para pedir la contraseña de forma segura
import email.message # Para construir el mensaje (del Ej. 8)
import email.utils

# --- Función RecvReply (Modificada para recibir del socket seguro) ---
# Recibirá del socket (sc) y comprobará el código
def RecvReply(sc, codigo_esperado):
    try:
        respuesta = sc.recv(1024)
        print(f"S: {respuesta.decode('utf-8')}") # S: (Respuesta del Servidor)
        codigo_recibido = respuesta[:3]

        if codigo_recibido != codigo_esperado:
            print(f"Error: Se esperaba {codigo_esperado.decode('utf-8')}, se recibió {codigo_recibido.decode('utf-8')}")
            # sys.exit(1) # Comentado para que no aborte siempre
            
    except Exception as e:
        print(f"Error al recibir respuesta: {e}")
        sys.exit(1)

# --- 1. Definir variables ---
server = "smtp.gmail.com"
port = 587 # Puerto para STARTTLS
username = input("Usuario (tu email de Gmail completo): ")
password = getpass.getpass("Contraseña (¡la de Aplicación de 16 letras!): ")

toaddr = input("Email destinatario: ")
subject = "Prueba SMTP con SSL/TLS (Ejercicio 11)"
data = "Este es un mensaje enviado desde Gmail usando STARTTLS y AUTH LOGIN."

# --- 2. Construir el mensaje (método Ej. 8) ---
msg = email.message.EmailMessage()
msg['To'] = toaddr
msg['From'] = username # El remitente DEBE ser tu email de Gmail
msg['Subject'] = subject
msg['Date'] = email.utils.formatdate(localtime=True)
msg['Message-ID'] = email.utils.make_msgid()
msg.set_content(data)
message_bytes = msg.as_bytes()
# ¡¡NO AÑADIMOS EL PUNTO!! Lo haremos tras el comando DATA

try:
    # --- 3. Conexión TCP inicial (socket normal 's') ---
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server, port))
    RecvReply(s, b'220') # 220: Bienvenida del servidor

    # --- 4. Negociación TLS ---
    print("C: EHLO mi-pc-practicas\r\n")
    s.sendall(b'EHLO mi-pc-practicas\r\n')
    RecvReply(s, b'250') # 250: Servidor dice OK y lista sus capacidades

    print("C: STARTTLS\r\n")
    s.sendall(b'STARTTLS\r\n')
    RecvReply(s, b'220') # 220: Servidor dice "OK, empecemos a cifrar"

    # --- 5. "Envolver" el socket con SSL ---
    # A partir de aquí, todo se envía por el socket seguro 'sc'
    context = ssl.create_default_context()
    sc = context.wrap_socket(s, server_hostname=server)
    print("--- Canal seguro (SSL/TLS) establecido ---")

    # --- 6. Autenticación (usando el socket seguro 'sc') ---
    print("C: EHLO mi-pc-practicas (de nuevo sobre SSL)\r\n")
    sc.sendall(b'EHLO mi-pc-practicas\r\n')
    RecvReply(sc, b'250')

    print("C: AUTH LOGIN\r\n")
    sc.sendall(b'AUTH LOGIN\r\n')
    RecvReply(sc, b'334') # 334: Desafío (pide usuario en Base64)

    # Enviamos usuario en Base64
    user_b64 = base64.b64encode(username.encode("ascii"))
    print("C: [Enviando usuario en Base64]")
    sc.sendall(user_b64 + b'\r\n')
    RecvReply(sc, b'334') # 334: Desafío (pide contraseña en Base64)

    # Enviamos contraseña en Base64
    pass_b64 = base64.b64encode(password.encode("utf-8"))
    print("C: [Enviando password en Base64]")
    sc.sendall(pass_b64 + b'\r\n')
    RecvReply(sc, b'235') # 235: ¡Autenticación exitosa!
    print("--- ¡Autenticación exitosa! ---")

    # --- 7. Envío de correo (usando el socket seguro 'sc') ---
    mail_from_cmd = f"MAIL FROM:<{username}>\r\n".encode('utf-8')
    print(f"C: {mail_from_cmd.decode('utf-8')}")
    sc.sendall(mail_from_cmd)
    RecvReply(sc, b'250')

    rcpt_to_cmd = f"RCPT TO:<{toaddr}>\r\n".encode('utf-8')
    print(f"C: {rcpt_to_cmd.decode('utf-8')}")
    sc.sendall(rcpt_to_cmd)
    RecvReply(sc, b'250')

    print("C: DATA\r\n")
    sc.sendall(b'DATA\r\n')
    RecvReply(sc, b'354') # 354: OK, envía el mensaje

    # Enviamos el mensaje y el punto final
    print("C: [Enviando datos del mensaje...]")
    sc.sendall(message_bytes + b'\r\n.\r\n')
    RecvReply(sc, b'250') # 250: OK, mensaje encolado

    print("C: QUIT\r\n")
    sc.sendall(b'QUIT\r\n')
    RecvReply(sc, b'221') # 221: Adiós

    print("\n¡Correo enviado con éxito a través de Gmail!")

except Exception as e:
    print(f"Error durante la conexión SMTP: {e}")
finally:
    # --- 8. Cerrar los sockets ---
    if 'sc' in locals():
        sc.close() # Cierra el socket seguro
    if 's' in locals():
        s.close() # Cierra el socket original