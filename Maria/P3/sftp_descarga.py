import paramiko
import base64
import getpass
import os
from stat import S_ISDIR

HOST = 'localhost'
USER = 'uo294340'
HOST_KEY_STR = 'AAAAC3NzaC1lZDI1NTE5AAAAINWq1hnIayN4DLxzX7jai3iwztiq1oSPj05bg/nAf/JX'
CARPETA_REMOTA = '.'  # El home
CARPETA_LOCAL = 'descargas_sftp'

password = getpass.getpass("Contraseña: ")

if not os.path.exists(CARPETA_LOCAL):
    os.makedirs(CARPETA_LOCAL)

try:
    client = paramiko.SSHClient()
    key = paramiko.Ed25519Key(data=base64.b64decode(HOST_KEY_STR))
    client.get_host_keys().add(HOST, 'ssh-ed25519', key)
    
    client.connect(HOST, username=USER, password=password)
    sftp = client.open_sftp()
    
    print(f"Descargando ficheros de {CARPETA_REMOTA} a {CARPETA_LOCAL}...")
    
    # Obtenemos lista de nombres
    nombres = sftp.listdir(CARPETA_REMOTA)
    
    for nombre in nombres:
        # Construimos la ruta completa remota
        ruta_remota = nombre 
        # Obtenemos atributos para ver si es directorio
        atributos = sftp.stat(ruta_remota)
        
        if S_ISDIR(atributos.st_mode):
            print(f"[OMITIDO] {nombre} es un directorio")
        else:
            print(f"[DESCARGANDO] {nombre}...", end=" ")
            ruta_local = os.path.join(CARPETA_LOCAL, nombre)
            sftp.get(ruta_remota, ruta_local)
            print("OK")

    sftp.close()
    client.close()
    print("Proceso terminado.")

except Exception as e:
    print(f"Error: {e}")