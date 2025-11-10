import paramiko
import sys
import os

IP_REMOTA = "156.35.163.18" 
USUARIO_REMOTO = "uo294340"    



client = paramiko.SSHClient()


client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # 1. Conectar usando la clave SSH (sin contraseña)
    # Buscará automáticamente tu clave en ~/.ssh/id_rsa
    client.connect(IP_REMOTA, username=USUARIO_REMOTO)
    
    print("Conectado!!")

    # 2. Ejecutar el comando 'ls'
    stdin, stdout, stderr = client.exec_command('ls')

    # 3. Mostrar el resultado
    for line in stdout:
        print(line.rstrip())

except paramiko.AuthenticationException:
    print("Error: Autenticación fallida.")
    print("Asegúrate de haber usado 'ssh-copy-id' correctamente.")
except Exception as e:
    print(f"Error: {e}")

finally:
    client.close()