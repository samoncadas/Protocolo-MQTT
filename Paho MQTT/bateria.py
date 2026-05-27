import ssl
import time
import json
import subprocess
import paho.mqtt.publish as publish

BROKER = "b9c04f87a5f64a61ac6c8666ed530332.s1.eu.hivemq.cloud"
PORT = 8883
TOPIC = "celular/bateria"

USUARIO = "samuel"
PASSWORD = "Samu2225"

while True:
    salida = subprocess.check_output(
        ["termux-battery-status"]
    ).decode("utf-8")

    datos = json.loads(salida)

    bateria = datos["percentage"]

    publish.single(
        TOPIC,
        f"{bateria}%",
        hostname=BROKER,
        port=PORT,
        auth={
            "username": USUARIO,
            "password": PASSWORD
        },
        tls={
            "tls_version": ssl.PROTOCOL_TLS_CLIENT
        }
    )

    print("Batería enviada:", bateria)

    time.sleep(5)