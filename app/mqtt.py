from paho.mqtt import client as mqtt_client
from datetime import datetime
import random
import time
import json
from . import lowLevelActivities
from . import process
from . import bpm
from . import occ

broker = "broker.hivemq.com"
port = 1883

har_topic = "/cs/har"
bpm_topic = "/cs/bpm"
occ_topic = "/cs/occ"

har_client = ""
bpm_client = ""
occ_client = ""
dp_client = ""

# Verbindung zum Broker herstellen
def connect_mqtt():
    client_id = f'python-mqtt-{random.randint(0, 1000)}'  # generiere eine zufällige Client ID
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    # Setze Connecting Client ID
    client = mqtt_client.Client(client_id)
    #client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

# Verbindung schließen
def disconnect (client):
    client.disconnect()
    print("Disconnected from MQTT Broker!")

# Message in ein bestimmtes Topic publishen
def publish(client, topic, msg):
    result = client.publish(topic,msg)
    # result: [0, 1]
    status = result[0]
    if status == 0:
        #print(f"Send `{msg}` to topic `{topic}`")
        return
    else:
        print(f"Failed to send message to topic {topic}")

# Ein bestimmtes Topic subscriben
def subscribe(client: mqtt_client, socketio, topic):
    def on_message(client, userdata, msg):
        tnow=datetime.now()
        #print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        data = dict(
            topic=msg.topic,
            payload=msg.payload.decode(),
            timestamp=str(tnow)
        )
        # Nachricht an den Socket senden, damit sie im UI ausgegeben werden kann.
        socketio.emit('mqtt_message', data=data)

        if msg.topic == "/cs/har":    
            bpm.lowLevelActivity_received(msg,tnow)
        elif msg.topic == "/cs/bpm":
            occ.highLevelActivity_received(msg,tnow)
        elif msg.topic == "/cs/occ":
            True
            # TODO [Future Work]: Starte Funktion zum Warnen des Mitarbeiters..

        else:
            print("unknown channel")
            
    client.subscribe(topic)
    client.on_message = on_message


