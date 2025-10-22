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


tn.read_until(b"$ ")
tn.write(b"cd /home/uo293690/IS-2025/Diego/\n")
tn.write(b"ps -ef\n")
ps_output = tn.read_until(b"$ ").decode('utf-8')
print(ps_output)
if "udp_servidor3_con_ok" in ps_output:
    print("El servidor ya está en ejecución.")
else:
    tn.write(b"nohup python3 /home/uo293690/IS-2025/Diego/udp_servidor3_con_ok.py &\n")
  

time.sleep(1)  # Esperar un momento para que el servidor se inicie

tn.write(b"exit\n")
print(tn.read_all().decode('utf-8'))