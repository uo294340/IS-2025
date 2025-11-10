import dns.resolver

dominio = "apple.com"

respuestas = dns.resolver.resolve(dominio, "A")
print(f"Direcciones IP asociadas a {dominio}:")
for respuesta in respuestas:
	print(" -", respuesta.to_text())
