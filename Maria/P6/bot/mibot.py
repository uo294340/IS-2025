import logging
import ssl
import asyncio
from slixmpp import ClientXMPP
import os
import sys

# Configuración de logs (útil para ver qué pasa)
logging.basicConfig(level=logging.INFO, format='%(levelname)-8s %(message)s')

class MiBot(ClientXMPP):
    def __init__(self, jid, password):
        super().__init__(jid, password)

        # Ejercicio 8: Registrar extensión chatstates (XEP-0085)
        self.register_plugin('xep_0085') 

        # Registrar eventos principales
        self.add_event_handler("session_start", self.start)
        self.add_event_handler("message", self.message)
        
        # Ejercicio 8: Registrar eventos de estado de chat
        self.add_event_handler("chatstate_composing", self.on_composing)
        self.add_event_handler("chatstate_paused", self.on_paused)
        self.add_event_handler("chatstate_active", self.on_active)
        self.add_event_handler("chatstate_inactive", self.on_inactive)

    async def start(self, event):
        """Callback para cuando la sesión se inicia (Ejercicio 6)"""
        self.send_presence()
        await self.get_roster()
        print(f"Bot conectado como: {self.boundjid.bare}")

    async def message(self, msg):
        """Callback para procesar mensajes recibidos (Ejercicios 7 y 9)"""
        if msg['type'] in ('chat', 'normal'):
            sender = msg['from']
            body = msg['body']
            
            # Ignorar mensajes vacíos (pueden ser solo notificaciones de estado)
            if not body:
                return

            print(f"Recibido de {sender.bare}: {body}")

            # Variable para la respuesta
            respuesta_texto = ""

            # Ejercicio 9: El bot calculador
            if body.startswith('='):
                expr = body[1:] # Quitar el '='
                try:
                    # ADVERTENCIA: eval() es peligroso en producción
                    resultado = str(eval(expr))
                    respuesta_texto = f"Resultado: {resultado}"
                except Exception as e:
                    respuesta_texto = f"Error de cálculo: {e}"
            else:
                # Ejercicio 7: Eco con interrogantes
                respuesta_texto = f"¿{body}?"

            # Construcción y envío de la respuesta manual
            reply = self.Message()
            reply['to'] = sender
            reply['type'] = 'chat'
            reply['body'] = respuesta_texto
            
            # Necesario para que Pidgin nos siga enviando estados (nota final del texto)
            reply['chat_state'] = 'active' 
            
            reply.send()
            print(f"Respuesta enviada: {respuesta_texto}")

    # --- Callbacks para Estados de Chat (Ejercicio 8) ---
    async def on_composing(self, msg):
        print(f"{msg['from'].bare} está escribiendo...")

    async def on_paused(self, msg):
        print(f"{msg['from'].bare} ha parado de escribir.")
    
    async def on_active(self, msg):
        print(f"{msg['from'].bare} está activo.")

    async def on_inactive(self, msg):
        print(f"{msg['from'].bare} está inactivo.")

if __name__ == '__main__':
    # Datos de conexión
    # Puedes cambiarlos o pedirlos con input() / getpass()
    jid = os.environ.get("BOT_JID", "bot@ingserv2e")
    password = os.environ.get("BOT_PASSWORD")
    server_address = os.environ.get("SERVER_ADDRESS", "prosody")
    
    if not password:
        print("Error: La variable de entorno BOT_PASSWORD es obligatoria.")
        sys.exit(1)
        
    # Instanciar el bot
    bot = MiBot(jid, password)

    # Configuración SSL para aceptar certificados autofirmados (Entorno de pruebas)
    bot.ssl_version = ssl.PROTOCOL_TLS
    bot.ssl_context = ssl.create_default_context()
    bot.ssl_context.check_hostname = False
    bot.ssl_context.verify_mode = ssl.CERT_NONE

    # Conectar y ejecutar
    print(f"Conectando a {server_address}...")
    bot.connect((server_address, 5222))
    bot.process(forever=True)