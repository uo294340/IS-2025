import ftplib
import getpass

# Lista para guardar lo que nos mande el servidor
lista = []

# Callback: Función que se ejecuta por cada línea que recibimos
def acumular(linea):
    lista.append(linea)

HOST = "localhost"
USER = "uo294340" 
CARPETA = "ftp_test" 

clave = getpass.getpass("Contraseña FTP: ")

try:
    print(f"Conectando a {HOST}...")
    f = ftplib.FTP(HOST)
    
    print("Login...")
    f.login(USER, clave)
    
    print(f"Cambiando a carpeta {CARPETA}...")
    f.cwd(CARPETA)
    
    print("Listando contenidos...")
    # LIST: Comando FTP estándar. 'acumular' recibe las líneas
    resp = f.retrlines("LIST", acumular)
    
    print("--- Respuesta del Servidor ---")
    print(resp)
    print("--- Ficheros Encontrados ---")
    for l in lista:
        print(l)
        
    f.quit()

except Exception as e:
    print(f"Error: {e}")