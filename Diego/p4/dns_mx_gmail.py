import dns.resolver

dominio = 'gmail.com'
print(f"Buscando servidores de correo (MX) para: {dominio}\n")

try:
    # 1. Hacemos la consulta para obtener los registros MX
    registros_mx = dns.resolver.query(dominio, 'MX')

    # 2. Creamos una lista para guardar los resultados
    resultados = []
    for r in registros_mx:
        # 3. Para cada registro MX, consultamos su IP (registro A)
        nombre_servidor = r.exchange.to_text()
        try:
            respuesta_ip = dns.resolver.query(nombre_servidor, 'A')
            ip = respuesta_ip[0].address
            
            # Guardamos la prioridad, nombre e IP
            resultados.append((r.preference, nombre_servidor, ip))
            
        except Exception as e:
            print(f"No se pudo resolver la IP para {nombre_servidor}: {e}")

    # 4. Ordenamos la lista final basándonos en la prioridad (el primer item de la tupla)
    resultados.sort()

    # 5. Imprimimos los resultados ordenados
    print("Prioridad  Servidor de Correo (MX)            IP")
    print("-" * 60)
    for res in resultados:
        # El :<10 significa "alineado a la izquierda, 10 caracteres de ancho"
        print(f"{res[0]:<10} {res[1]:<30} {res[2]}")

except Exception as e:
    print(f"Ocurrió un error al consultar MX para {dominio}: {e}")