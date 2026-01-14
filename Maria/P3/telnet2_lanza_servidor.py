import getpass
import telnetlib
import time

HOST = "localhost"
user = input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)


tn.read_until(b"login: ")
tn.write(user.encode('utf-8') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('utf-8') + b"\n")

tn.read_until(b"$")
# Cambiar al directorio donde está el servidor
tn.write(b"cd IS-2025/Maria/P3\n")
tn.read_until(b"$")
#procesos del usuario
tn.write(b"ps -ef | grep udp_servidor3_con_ok.py | grep -v grep\n")
ps_output = tn.read_until(b"$").decode('utf-8')




if "python3 udp_servidor3_con_ok.py" in ps_output:
    print("El servidor ya está en ejecución")
else:
    (print("Iniciando el servidor UDP..."))
    tn.write(b"nohup python3 udp_servidor3_con_ok.py &\n")
    print("Servidor iniciado")

time.sleep(1)  # Esperar un momento para que el servidor se inicie
tn.write(b"exit\n")

print(tn.read_all().decode('utf-8'))