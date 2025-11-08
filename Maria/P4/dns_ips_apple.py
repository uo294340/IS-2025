import dns.resolver

dominio = 'apple.com'
print(f"Buscando TODAS las IPs (Registros A) para: {dominio}\n")

try:
    # Pedimos explícitamente los registros 'A' (IPv4)
    respuesta = dns.resolver.query(dominio, 'A')

    # Iteramos sobre la respuesta (como pedía la pista)
    # 'rdata' es cada registro individual
    for rdata in respuesta:
        print(f"IP encontrada: {rdata.address}")

except dns.resolver.NoAnswer:
    print(f"La consulta para {dominio} no tuvo respuesta.")
except dns.resolver.NXDOMAIN:
    print(f"El dominio {dominio} no existe.")
except Exception as e:
    print(f"Ocurrió un error: {e}")