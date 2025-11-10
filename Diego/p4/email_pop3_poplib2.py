import poplib
import getpass
import sys
import email.parser       # Para parsear los bytes
import email.header       # Para decodificar cabeceras (tildes, etc.)

# --- 1. La función mágica del Ejercicio 16 ---
# La he adaptado un poco para que sea más clara
def imprime_resumen_mensaje(msg_bytes):
    try:
        # 1. Parsear los bytes en un objeto EmailMessage
        # Usamos BytesParser para leerlo desde bytes
        parser = email.parser.BytesParser()
        msg = parser.parsebytes(msg_bytes)

        # 2. Extraer cabeceras (con valor por defecto)
        remite_raw = msg.get("From", "<desconocido>")
        asunto_raw = msg.get("Subject", "<sin asunto>")

        # 3. Decodificar cabeceras (¡Esta es la parte clave!)
        # Esto convierte "=?UTF-8?..." en texto legible
        remite = email.header.make_header(email.header.decode_header(remite_raw))
        asunto = email.header.make_header(email.header.decode_header(asunto_raw))

        # 4. Extraer el cuerpo
        cuerpo = ""
        if msg.is_multipart():
            # Si es multipart, buscamos la primera parte de texto
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    # get_payload(decode=True) lo decodifica (ej. de base64)
                    cuerpo = part.get_payload(decode=True).decode(part.get_content_charset(), 'ignore')
                    break
            if not cuerpo:
                cuerpo = "[Mensaje multipart sin parte de texto plano]"
        else:
            # Si es un mensaje simple, solo hay un payload
            cuerpo = msg.get_payload(decode=True).decode(msg.get_content_charset(), 'ignore')
        
        # 5. Imprimir resumen
        print(f"From: {remite}")
        print(f"Subject: {asunto}")
        print("-" * 30)
        print(cuerpo[:200] + "...") # Primeros 200 caracteres
        print("=" * 80)

    except Exception as e:
        print(f"Error al parsear el mensaje: {e}")
        print("=" * 80)

# --- Código principal (similar al Ej. 15) ---

server = "pop.gmail.com"
try:
    username = input("Usuario (tu email de Gmail, usa 'recent:' si es necesario): ")
    password = getpass.getpass("Contraseña (¡la de Aplicación de 16 letras!): ")
except EOFError:
    sys.exit("Entrada cancelada.")

try:
    print(f"\nConectando a {server}...")
    pop3_mail = poplib.POP3_SSL(server)
    # pop3_mail.set_debuglevel(1) # Descomenta para ver el diálogo
    pop3_mail.user(username)
    pop3_mail.pass_(password)
    
    num_mensajes, _ = pop3_mail.stat()
    print(f"Hay {num_mensajes} mensajes. Descargando todos...")

    # --- Bucle para descargar TODOS los mensajes ---
    for i in range(1, num_mensajes + 1):
        print(f"\nDescargando mensaje {i} de {num_mensajes}...")
        
        # .retr(i) devuelve (respuesta, [lineas], tamaño)
        # Unimos las líneas con b'\r\n' como pide el ejercicio
        lineas_bytes = pop3_mail.retr(i)[1]
        mensaje_completo_bytes = b'\r\n'.join(lineas_bytes)
        
        # Pasamos los bytes a nuestra función de parseo
        imprime_resumen_mensaje(mensaje_completo_bytes)

    pop3_mail.quit()
    print("\nConexión cerrada.")

except Exception as e:
    print(f"\n[ERROR] Ocurrió un error: {e}")