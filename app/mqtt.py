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

generalMode = False
dataProducer = False
lowLevel_processTrace = process.active_process_lowLevelActivityTrace

har_topic = "/cs/har"
bpm_topic = "/cs/bpm"
occ_topic = "/cs/occ"

har_client = ""
bpm_client = ""
occ_client = ""
dp_client = ""

def connect_mqtt():
    client_id = f'python-mqtt-{random.randint(0, 1000)}'  # randomly generate MQTT client id
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    # Set Connecting Client ID
    client = mqtt_client.Client(client_id)
    #client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def disconnect (client):
    client.disconnect()
    print("Disconnected from MQTT Broker!")

def publish(client, topic, msg):
    result = client.publish(topic,msg)
    # result: [0, 1]
    status = result[0]
    if status == 0:
        #print(f"Send `{msg}` to topic `{topic}`")
        return
    else:
        print(f"Failed to send message to topic {topic}")


def subscribe(client: mqtt_client, socketio, topic):
    def on_message(client, userdata, msg):
        tnow=datetime.now()
        #print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        data = dict(
            topic=msg.topic,
            payload=msg.payload.decode(),
            timestamp=str(tnow)
        )
        # emit a mqtt_message events to the socket containing the message data
        socketio.emit('mqtt_message', data=data)

        if msg.topic == "/cs/har":    
            bpm.lowLevelActivity_received(msg,tnow)
        elif msg.topic == "/cs/bpm":
            occ.highLevelActivity_received(msg,tnow)
        elif msg.topic == "/cs/occ":
            True
            # TODO: Here occ_warn function start
            # print("Start occ_message_received Function")

        else:
            # TODO: Here unknown channel function
            print("unknown channel")
            
    client.subscribe(topic)
    client.on_message = on_message


def startDataProducer (dp_client, har_topic, bpm_topic, occ_topic):
    if (generalMode == True):
        x = 0
        while dataProducer:
            message = {
                "text": "This is a test" + str(x)
            }
            jsonData = json.dumps(message)
            publish(dp_client, har_topic, jsonData)
            publish(dp_client, bpm_topic, jsonData)
            publish(dp_client, occ_topic, jsonData)
            x+=1
            time.sleep(2)
    else:
        for lowLevelactivity in lowLevel_processTrace:
            if dataProducer:
                # textData = lowLevelActivities.activityToString(activity)
                # publish(dp_client, har_topic, textData)

                jsonData = json.dumps(lowLevelactivity)
                publish(dp_client, har_topic, jsonData)
                
                time.sleep(random.randint(1, 3))
            else:
                break


