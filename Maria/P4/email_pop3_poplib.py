import poplib
import getpass
import sys

server = "pop.gmail.com"

try:
    username = input("Usuario (tu email de Gmail, usa 'recent:' si es necesario): ")
    password = getpass.getpass("Contraseña (¡la de Aplicación de 16 letras!): ")
except EOFError:
    sys.exit("Entrada cancelada.")

try:
    print(f"\nConectando a {server}...")
    pop3_mail = poplib.POP3_SSL(server)
    pop3_mail.set_debuglevel(2)
    
    pop3_mail.user(username)
    pop3_mail.pass_(password)
    
    print("\nDescargando el primer mensaje...")
    
    # retr(1) devuelve una tupla: (respuesta, [líneas], tamaño)
    respuesta, lineas, tamaño = pop3_mail.retr(1)
    
    print(f"\nRespuesta del servidor: {respuesta}")
    print(f"Tamaño del mensaje: {tamaño} bytes")
    print(f"\nContenido del mensaje (lista de líneas):")
    print("-" * 80)
    print(lineas)
    print("-" * 80)
    
    pop3_mail.quit()
    print("\nConexión cerrada.")

except Exception as e:
    print(f"\n[ERROR] Ocurrió un error: {e}")
