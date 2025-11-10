import paramiko
import getpass  # Para pedir la contraseña de forma segura
import sys

# --- Configura tus datos de conexión ---
HOST_IP = '192.168.1.252'  # REEMPLAZA con la IP de tu Ubuntu
USUARIO = 'uo293690'
# --------------------------------------

# Pedimos la contraseña de forma segura en lugar de escribirla en el código
try:
    PASSWORD = getpass.getpass(f"Introduce la contraseña para {USUARIO}@{HOST_IP}: ")
except Exception as e:
    print(f"Error al leer la contraseña: {e}")
    sys.exit(1)

# 1. Crear el objeto SSHClient
client = paramiko.SSHClient()

# 2. Fijar la política para claves de host desconocidas
# Usamos AutoAddPolicy para que acepte automáticamente la clave del servidor.
# Esto es cómodo para ejercicios, pero inseguro en producción (como se vio en el Ej. 8)
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # 3. Conectar al servidor SSH
    print(f"Conectando a {HOST_IP} como {USUARIO}...")
    client.connect(HOST_IP, username=USUARIO, password=PASSWORD)
    print("¡Conexión SSH exitosa!")

    # 4. Abrir un canal SFTP sobre la conexión SSH
    sftp = client.open_sftp()
    print("Canal SFTP abierto.")

    # 5. Usar los métodos de SFTP
    # listdir() sin argumentos lista el contenido del directorio 'home' por defecto
    lista_archivos = sftp.listdir()

    print(f"\n--- Contenido de /home/{USUARIO} ---")
    for nombre_fichero in lista_archivos:
        print(nombre_fichero)
    print("-----------------------------------")

    # Cerramos el canal sftp
    sftp.close()

except paramiko.AuthenticationException:
    print("Error: Autenticación fallida. Revisa la contraseña.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")

finally:
    # 6. Cerrar siempre la conexión SSH principal
    client.close()
    print("Conexión SSH cerrada.")