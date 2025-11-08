import paramiko
import getpass
import sys
import os      # Para crear la carpeta local
import stat    # Para usar S_ISDIR y comprobar si es un directorio

# --- Configura tus datos de conexión ---
HOST_IP = '192.168.0.30'  # REEMPLAZA con la IP de tu Ubuntu
USUARIO = 'uo294340'
CARPETA_REMOTA = '.'  # '.' significa el directorio 'home'
CARPETA_LOCAL = 'mi_descarga_sftp' # Nombre de la carpeta donde guardaremos todo
# --------------------------------------

# 1. Crear la carpeta local si no existe
if not os.path.exists(CARPETA_LOCAL):
    os.makedirs(CARPETA_LOCAL)
    print(f"Carpeta local '{CARPETA_LOCAL}' creada.")

# Pedimos la contraseña
try:
    PASSWORD = getpass.getpass(f"Introduce la contraseña para {USUARIO}@{HOST_IP}: ")
except Exception as e:
    print(f"Error al leer la contraseña: {e}")
    sys.exit(1)

# 2. Conectar (igual que en el ejercicio 12)
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    print(f"Conectando a {HOST_IP} como {USUARIO}...")
    client.connect(HOST_IP, username=USUARIO, password=PASSWORD)
    print("¡Conexión SSH exitosa!")

    sftp = client.open_sftp()
    print(f"Abierto canal SFTP. Accediendo a carpeta remota: '{CARPETA_REMOTA}'")

    # 3. Cambiar al directorio remoto deseado
    sftp.chdir(CARPETA_REMOTA)

    # 4. Listar el contenido del directorio actual
    # sftp.listdir('.') lista el directorio actual de sftp
    items = sftp.listdir('.')

    print(f"Iniciando descarga de archivos a '{CARPETA_LOCAL}'...")

    # 5. Recorrer la lista y descargar SÓLO los ficheros
    for item in items:
        # Obtenemos los 'stats' del item para saber qué es
        info = sftp.stat(item)

        # Usamos la función S_ISDIR 
        if stat.S_ISDIR(info.st_mode):
            # Si es un directorio, lo omitimos
            print(f"-> Omitiendo directorio: {item}")
        else:
            # Si es un fichero, lo descargamos
            print(f"-> Descargando fichero:  {item}")
            
            # Construimos la ruta local completa
            ruta_local_fichero = os.path.join(CARPETA_LOCAL, item)
            
            # Usamos sftp.get(fichero_remoto, fichero_local)
            sftp.get(item, ruta_local_fichero)

    print("\n¡Descarga completada!")
    sftp.close()

except paramiko.AuthenticationException:
    print("Error: Autenticación fallida. Revisa la contraseña.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")

finally:
    client.close()
    print("Conexión SSH cerrada.")