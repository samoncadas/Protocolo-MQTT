import paho.mqtt.client as mqtt
from datetime import datetime
import ssl


BROKER   = "b9c04f87a5f64a61ac6c8666ed530332.s1.eu.hivemq.cloud"  # ← cambia esto
PORT     = 8883
USUARIO  = "samuel"                # ← cambia esto
PASSWORD = "Samu2225"               # ← cambia esto
TOPIC    = "celular/bateria"

def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("Conectado al broker")
        client.subscribe(TOPIC)
        print(f"Escuchando datos del celular en: {TOPIC}\n")
        print("-" * 45)
    else:
        print(f" Error de conexión, código: {rc}")

def on_message(client, userdata, msg):
    valor = msg.payload.decode()
    hora  = datetime.now().strftime("%H:%M:%S")
    topic = msg.topic.split("/")[-1]

    

    print(f"[{hora}]   {topic.upper()}: {valor}")

client = mqtt.Client(client_id="pc-receptor-01", callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
client.username_pw_set(USUARIO, PASSWORD)
client.tls_set(tls_version=ssl.PROTOCOL_TLS_CLIENT)

client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT)
client.loop_forever()