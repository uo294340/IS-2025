import paramiko
import base64
import getpass

# Configuración
HOST = 'localhost'
USER = 'uo294340' # TU USUARIO

HOST_KEY_STR = 'AAAAC3NzaC1lZDI1NTE5AAAAINWq1hnIayN4DLxzX7jai3iwztiq1oSPj05bg/nAf/JX'

password = getpass.getpass("Contraseña: ")

try:
    # 1. Conexión SSH
    client = paramiko.SSHClient()
    key = paramiko.Ed25519Key(data=base64.b64decode(HOST_KEY_STR))
    client.get_host_keys().add(HOST, 'ssh-ed25519', key)
    
    client.connect(HOST, username=USER, password=password)
    
    # 2. Abrir canal SFTP
    sftp = client.open_sftp()
    
    print(f"--- Listado de /home/{USER} ---")
    
    # Listar directorio actual (por defecto es el home)
    archivos = sftp.listdir()
    for archivo in archivos:
        # Obtenemos detalles para mostrarlo bonito 
        attr = sftp.stat(archivo)
        print(f"{archivo:<20} | {attr.st_size:>8} bytes")

    sftp.close()
    client.close()

except Exception as e:
    print(f"Error: {e}")