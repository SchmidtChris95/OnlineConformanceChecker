import time
import json
import random
from datetime import datetime
from . import process
from . import mqtt

testMode = False
dataProducer = False
# Zu simulierende Prozessdurchführung:
lowLevel_processTrace = process.active_process_lowLevelActivityTrace


def startDataProducer (dp_client, har_topic, bpm_topic, occ_topic):
    # Produziert nur irgendwelche Daten
    if (testMode == True):
        x = 0
        while dataProducer:
            message = {
                "text": "This is a test" + str(x)
            }
            jsonData = json.dumps(message)
            mqtt.publish(dp_client, har_topic, jsonData)
            mqtt.publish(dp_client, bpm_topic, jsonData)
            mqtt.publish(dp_client, occ_topic, jsonData)
            x+=1
            time.sleep(2)
    # Produziert konkrete Low-Level-Aktivitäten
    else:
        for lowLevelactivity in lowLevel_processTrace:
            if dataProducer:
                # textData = lowLevelActivities.activityToString(activity)
                # publish(dp_client, har_topic, textData)

                jsonData = json.dumps(lowLevelactivity)
                mqtt.publish(dp_client, har_topic, jsonData)
                
                time.sleep(random.randint(1, 3))
            else:
                break