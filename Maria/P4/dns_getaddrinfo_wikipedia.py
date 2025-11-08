import socket
import sys

HOST = "en.wikipedia.org"
SERVICIO = "www" # alias para el puerto 80 (http)

print(f"Buscando información de conexión para {HOST} en servicio {SERVICIO}...\n")

try:
    # 1. Usar getaddrinfo()
    # Filtramos por AF_INET (IPv4) y SOCK_STREAM (TCP)
    # Cambia AF_INET a AF_INET6 para probar IPv6

    lista_resultados = socket.getaddrinfo(HOST, SERVICIO, socket.AF_INET, socket.SOCK_STREAM)

    print(f"getaddrinfo() encontró {len(lista_resultados)} formas de conectar por IPv4.")

    # Usamos solo el primer resultado para este ejemplo
    info_conexion = lista_resultados[0]

    # Desempaquetamos la tupla 
    familia, tipo_socket, proto, nombre_canonico, direccion_socket = info_conexion

    print(f"\n--- Usando el primer resultado ---")
    print(f"Familia de direcciones: {familia}")
    print(f"Tipo de socket: {tipo_socket}")
    print(f"Protocolo: {proto}")
    print(f"Dirección (IP, Puerto): {direccion_socket}")
    print("----------------------------------\n")

    # 2. Crear el socket y conectar
    print(f"Creando socket y conectando a {direccion_socket}...")
    s = socket.socket(familia, tipo_socket, proto)
    s.connect(direccion_socket)
    print("¡Conectado!")

    # 3. Enviar una cabecera HTTP
    # Lo enviamos como bytes (por eso la b"...")
    # Pedimos el directorio raíz "/"
    peticion = b"GET / HTTP/1.1\r\nHost: en.wikipedia.org\r\nConnection: close\r\n\r\n"

    s.sendall(peticion)

    # 4. Recibir la respuesta del servidor
    print("\n--- Respuesta del Servidor (primeros 500 bytes) ---")
    respuesta = s.recv(512) # Recibimos los primeros 512 bytes

    # Decodificamos de bytes a texto para imprimirlo
    print(respuesta.decode('utf-8', 'ignore'))
    print("...")

except socket.error as e:
    print(f"Error de socket: {e}")
    print("Asegúrate de tener conexión a internet.")
except Exception as e:
    print(f"Error inesperado: {e}")
finally:
    # Aseguramos que el socket se cierre
    if 's' in locals():
        s.close()
        print("\nSocket cerrado.")