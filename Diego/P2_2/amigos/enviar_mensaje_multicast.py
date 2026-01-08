import firebase_admin
from firebase_admin import credentials, messaging

# Cargar credenciales desde el archivo JSON obtenido de Firebase
json_secrets = "serviceAccount.json"
cred = credentials.Certificate(json_secrets)
firebase_admin.initialize_app(cred)

# Lista de tokens de dispositivos
fcm_tokens = [
    "fTLP8_N3T1uCy98_mHY2dY:APA91bEtraBJNMBc2aG0aOLo1pG3yiUQWGpxHeKljzeFQEomZ6CP31cvYx8pUWr7IZu2FXyyrQmOaD4_DZ2AzqqT8v0qA09Sf4gx_O_Ys41Z_U4bALOiKLA"
]

notification_title = "Posición actualizada"
notification_body = "Un amigo ha actualizado su posición"

try:
    notification_payload = messaging.Notification(
        title=notification_title,
        body=notification_body
    )
    
    # El mensaje es de tipo MulticastMessage
    message = messaging.MulticastMessage(
        notification=notification_payload,
        tokens=fcm_tokens
    )

    print(f"Enviando mensaje a {len(fcm_tokens)} dispositivo(s)...")
    # El envío usa send_each_for_multicast
    response = messaging.send_each_for_multicast(message)
    
    print(f"Mensajes enviados con éxito: {response.success_count}")
    print(f"Mensajes fallidos: {response.failure_count}")
    
    # Mostrar detalles de cada envío
    for idx, resp in enumerate(response.responses):
        if resp.success:
            print(f"  Token {idx}: Enviado correctamente")
        else:
            print(f"  Token {idx}: Error - {resp.exception}")

except Exception as e:
    print(f"Error al enviar el mensaje: {e}")
