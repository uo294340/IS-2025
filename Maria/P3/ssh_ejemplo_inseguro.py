import paramiko
import time
import getpass

password = getpass.getpass("Introduce tu contraseña de Ubuntu: ")

client = paramiko.SSHClient()

# Política de aceptar todo (INSEGURO)
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    client.connect('localhost', username='uo294340', password=password)
    print("Conectado!!")
    
    stdin, stdout, stderr = client.exec_command('ls -l')
    
    print("--- Salida del comando remoto ---")
    for line in stdout:
        print(line.rstrip())
        
except Exception as e:
    print(f"Error: {e}")
finally:
    client.close()