import smtplib
import getpass
import email.message
import email.utils
import sys

# --- 1. Definir variables ---
SERVER = "smtp.gmail.com"
PORT = 587

try:
    # Pedimos los datos
    username = input("Usuario (tu email de Gmail completo): ")
    password = getpass.getpass("Contraseña (¡la de Aplicación de 16 letras!): ")
    toaddr = input("Email destinatario: ")
    
except EOFError:
    sys.exit("Entrada cancelada.")

# --- 2. Construir el mensaje (igual que antes) ---
msg = email.message.EmailMessage()
msg['To'] = toaddr
msg['From'] = username
msg['Subject'] = "Prueba con smtplib (Ejercicio 12)"
msg['Date'] = email.utils.formatdate(localtime=True)
msg['Message-ID'] = email.utils.make_msgid()
msg.set_content("Este mensaje se ha enviado usando la librería smtplib. ¡Mucho más fácil!")

# --- 3. Conectar y enviar con smtplib ---
try:
    # 3.1. Conectar al servidor
    # Creamos el objeto SMTP
    s = smtplib.SMTP(SERVER, PORT)

    # 3.2. Activar depuración (¡Muy útil!)
    # Esto nos mostrará el diálogo C:/S en la terminal
    s.set_debuglevel(1)

    # 3.3. Negociar canal seguro
    # .starttls() hace todo el trabajo del Ej. 11 (EHLO, STARTTLS, SSL wrap)
    s.starttls()

    # 3.4. Autenticarse
    # .login() hace todo el trabajo de AUTH LOGIN y Base64
    s.login(username, password)

    # 3.5. Enviar el mensaje
    # .send_message() es la forma moderna (maneja el .as_bytes() y el punto final)
    print("\nC: Enviando mensaje...")
    s.send_message(msg)
    print("S: [Mensaje enviado]")

    # 3.6. Cerrar conexión
    s.quit()
    
    print("\n¡Correo enviado con éxito!")

except smtplib.SMTPAuthenticationError:
    print("\n[ERROR] Autenticación fallida. Revisa el usuario o la contraseña de aplicación.")
except Exception as e:
    print(f"\n[ERROR] Ocurrió un error: {e}")