import json
from datetime import date, datetime
from . import lowLevelActivities as lla
from . import highLevelActivities as hla
from . import process
from . import mqtt

rec_steps = []

# Schon erkannte Steps zurücksetzen
def init_checking():
    global rec_steps
    rec_steps = []

def highLevelActivity_received(msg,tnow):
    
    # Extract the process step infos
    jsonMessage=json.loads(msg.payload.decode()) #decode json data
    id = jsonMessage["id"]
    name = jsonMessage["name"]
    lowlevelActivities = jsonMessage["lowlevelActivities"]
    pred = jsonMessage["pred"]
    succ = jsonMessage["succ"]
    maxOccurrence = jsonMessage["maxOccurrence"]
    maxProcessingTime = jsonMessage["maxProcessingTime"]

    # Create recognized process step object
    rec_step = createRecStep(id, name, lowlevelActivities,pred,succ,maxOccurrence,maxProcessingTime,tnow)
    rec_steps.append(rec_step)


    # Check the conformance rule
    rule1(rec_step)
    rule2(rec_step)
    rule3(rec_step)

    return

# Triggered, when violation is detected
def violation_Detected(text, type, rec_step):
    violation = createViolation(text, type, rec_step["id"])
    jsonData = json.dumps(violation)
    mqtt.publish(mqtt.occ_client, mqtt.occ_topic, jsonData)
    return

def rule1(rec_step): # Checkt Reihenfolge
   
    # Checken ob start activity
    if (len(rec_steps) == 1): 
        if (len(rec_step["pred"])) != 0 : # not a start activity
            violation_Detected("Order violation: " + str(rec_step["id"]) + " is not a start activity.", "start", rec_step)
            return
    else: 
        # Reihenfolge checken
        actual_pred = rec_steps[len(rec_steps)-2]     # Tatsächlicher Vorgänger
        permitted_preds = rec_step["pred"]            # Erlaubte Vorgänger
        permitted_succs = actual_pred["succ"]         # Mögliche Nachfolger von tatsächlichem Vorgänger

        # Checken, ob tatsächlicher Vorgänger auch in den erlaubten Vorgängern ist.
        if actual_pred["id"] not in permitted_preds:
            violation_Detected("Order violation: Activity " + str(actual_pred["id"]) + " is not a permitted predecessor for " + str(rec_step["id"]) + ".", "order", rec_step)
            return
        else: # Wenn Prozess richtig, dann ist das hier nicht nötig.
            if rec_step["id"] not in permitted_succs:
                violation_Detected("Order violation: Activity " + str(rec_step["id"]) + " is not a permitted successor for " + str(actual_pred["id"]) + ".", "order", rec_step)
            return

def rule2(rec_step): # Checkt Zwischenzeit zwischen zwei HLA --> ungefähr gleich Bearbeitungsdauer einer HLA

    # Checken ob start activity, wenn ja, keine Violation mögl.
    if (len(rec_steps) == 1): 
        return
    else:
        maxProcessingTime = rec_step["maxProcessingTime"]
        pred = rec_steps[len(rec_steps)-2]  # Vorgänger
        start = pred["timestamp"]
        end = rec_step["timestamp"]
        timedelta = (end-start).total_seconds()
        if (timedelta > maxProcessingTime):
            violation_Detected("Max Processing Time exceeded: Activity " + str(rec_step["id"]) + " took " + str(timedelta) + " seconds and is allowed " + str(maxProcessingTime) +".", "processingtime", rec_step)
        return

def rule3(rec_step): # Checkt wie oft die Aktivität vorkommen darf

    maxOccurrence = rec_step["maxOccurrence"]
    counter = 0
    id = rec_step["id"]
    for item in rec_steps:
        if item["id"] == id:
            counter+=1
    if (counter > maxOccurrence):
        violation_Detected("Max Occurrence exceeded: Activity " + str(rec_step["id"]) + " was executed " + str(counter) + " times but is only allowed to happen " + str(maxOccurrence) + " times.", "occurence", rec_step)
    return

# erzeugt einen recognized_Step
def createRecStep(stepId, name, lowlevelActivities, pred, succ, maxOccurrence, maxProcessingTime, timestamp):
    rec_step = {
        "id": stepId,
        "name": name,
        "lowlevelActivities": lowlevelActivities,
        "pred": pred,
        "succ": succ,
        "maxOccurrence": maxOccurrence,
        "maxProcessingTime": maxProcessingTime,
        "timestamp": timestamp
    }
    return rec_step

# erzeugt ein Violation Object
def createViolation(text, type, rec_step_id):
    violation = {
        "text": text,
        "type": type,
        "step": rec_step_id
    }
    return violation 