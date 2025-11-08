import dns.resolver

try:
    respuesta = dns.resolver.query('en.wikipedia.org')

    # Imprime la primera IP encontrada
    print(f"IP: {respuesta[0].address}")

    #Imprime la respuesta completa (legible)
    print("\n--- Respuesta completa (legible) ---")
    print(respuesta.response)

    #Imprime la respuesta en binario
    print("\n--- Respuesta completa (binario 'wire') ---")
    # .to_wire() devuelve bytes, que pueden no ser imprimibles,
    # así que mostramos solo los primeros 100 bytes
    print(respuesta.response.to_wire()[:100])

except Exception as e:
    print(f"Error en la consulta DNS: {e}")