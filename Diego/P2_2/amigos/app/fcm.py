import os
import firebase_admin
from firebase_admin import credentials, messaging

# Variable global para las credenciales
cred = None

try:
    # Obtener la ruta al archivo serviceAccount.json
    json_path = os.path.join(os.path.dirname(__file__), "serviceAccount.json")
    
    # Cargar credenciales
    cred = credentials.Certificate(json_path)
    firebase_admin.initialize_app(cred)
    print(f"Firebase Admin inicializado correctamente desde {json_path}")
    
except Exception as e:
    print(f"Error al inicializar Firebase Admin: {e}")
    print("Las notificaciones FCM no estarán disponibles")
    cred = None


def notificar_amigos(tokens, body):
    """
    Envía una notificación FCM a una lista de dispositivos.
    
    Args:
        tokens: Lista de tokens de dispositivo
        body: Cuerpo del mensaje de notificación
    """
    # Si no hay tokens o no hay credenciales, no hacer nada
    if not tokens or cred is None:
        if not tokens:
            print("No hay dispositivos a los que notificar")
        else:
            print("Firebase no está inicializado. No se pueden enviar notificaciones")
        return
    
    try:
        # Crear el payload de notificación
        notification_payload = messaging.Notification(
            title="Amigos",
            body=body
        )
        
        # Crear el mensaje multicast
        message = messaging.MulticastMessage(
            notification=notification_payload,
            tokens=tokens
        )
        
        # Enviar el mensaje
        print(f"Enviando notificación a {len(tokens)} dispositivo(s): {body}")
        response = messaging.send_each_for_multicast(message)
        
        print(f"✓ Mensajes enviados con éxito: {response.success_count}")
        if response.failure_count > 0:
            print(f"✗ Mensajes fallidos: {response.failure_count}")
            
    except Exception as e:
        print(f"Error al enviar notificación FCM: {e}")
