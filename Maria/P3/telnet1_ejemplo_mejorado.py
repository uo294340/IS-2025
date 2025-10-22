import getpass
import telnetlib

HOST = "localhost"
user = input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)
tn.set_debuglevel(1)

tn.read_until(b"login: ")
tn.write(user.encode('utf-8') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('utf-8') + b"\n")

tn.read_until(b"$")
tn.write(b"ls /home\n")
tn.write(b"exit\n")

print(tn.read_all().decode('utf-8'))