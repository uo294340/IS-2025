# coding: utf-8
from slixmpp import ClientXMPP
import ssl
import logging
import getpass
import os
import sys

class MiBot(ClientXMPP):
    def __init__(self, jid, clave):
        super().__init__(jid, clave)
        self.add_event_handler("session_start", self.callback_para_session_start)
        self.add_event_handler("message", self.callback_para_message)
        self.add_event_handler("chatstate_composing", self.callback_composing)
        self.add_event_handler("chatstate_paused", self.callback_paused)
        self.add_event_handler("chatstate_active", self.callback_active)
        self.add_event_handler("chatstate_inactive", self.callback_inactive)

    async def callback_para_session_start(self, evento):
        self.send_presence()
        await self.get_roster()

    def callback_para_message(self, evento):
        print(f"Recibido un mensaje de tipo {evento['type']} desde {evento['from']}")
        print(f"Que dice: {evento['body']}")
        
        if evento['type'] == 'chat':
            jid_destino = evento['from']
            body = evento['body']
            
            # Si el mensaje comienza por '=', evaluar la expresión
            if body.startswith('='):
                expresion = body[1:]  # Quitar el '='
                try:
                    resultado = eval(expresion)
                    cuerpo = str(resultado)
                except Exception as e:
                    cuerpo = f"Error al evaluar: {e}"
            else:
                # Comportamiento por defecto: eco con interrogantes
                cuerpo = f"¿{body}?"
            
            msg = self.Message()
            msg["to"] = jid_destino
            msg["type"] = "chat"
            msg["body"] = cuerpo
            msg.send()

    def callback_composing(self, evento):
        print(f"{evento['from'].bare} está escribiendo...")

    def callback_paused(self, evento):
        print(f"{evento['from'].bare} ha parado de escribir")

    def callback_active(self, evento):
        print(f"{evento['from'].bare} está activo")

    def callback_inactive(self, evento):
        print(f"{evento['from'].bare} está inactivo")


# Programa principal
if __name__ == "__main__":
    # Configurar logging para ver mensajes informativos
    logging.basicConfig(level=logging.INFO,
                        format='%(levelname)-8s %(message)s')
    
    # Pedir datos al usuario
    jid = input("Enter para que sea bot@ingserv002: ") or "bot@ingserv002"
    clave = getpass.getpass("Contraseña del bot: ")
    ip = input("Enter para que sea localhost: ") or "localhost"
    puerto = 5222
    
    # Instanciar el cliente
    cliente = MiBot(jid, clave)
    cliente.register_plugin("xep_0085")  # chatstates
    
    # Configurar SSL para que confíe en el certificado autofirmado
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    cliente.ssl_context = ssl_context
    
    # Conectar con el servidor
    cliente.connect((ip, puerto))
    
    # Iniciar el bucle de eventos (bloquea hasta Ctrl-C)
    cliente.process(forever=True)
