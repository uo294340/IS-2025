import paramiko
import time
import getpass
import base64

password = getpass.getpass("Contraseña: ")

client = paramiko.SSHClient()



# 1. Definimos la clave que esperamos del servidor

clave_servidor_str = 'AAAAC3NzaC1lZDI1NTE5AAAAINWq1hnIayN4DLxzX7jai3iwztiq1oSPj05bg/nAf/JX'  # <--- ¡COMPLETA ESTO!

# 2. Convertimos a objeto Key
key = paramiko.Ed25519Key(data=base64.b64decode(clave_servidor_str))

# 3. La añadimos a las claves conocidas del cliente
client.get_host_keys().add('localhost', 'ssh-ed25519', key)


client.connect('localhost', username='uo294340', password=password)
print("Conectado de forma segura!")

stdin, stdout, stderr = client.exec_command('ls')
for line in stdout:
    print(line.rstrip())

client.close()