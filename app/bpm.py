import json
from . import lowLevelActivities as lla
from . import highLevelActivities as hla
from . import process
from . import mqtt


process_activity_set = process.active_process_set
rec_activities = []
possible_matches = []
maxLowLevelActivityThreshold = 5
maxPossibleActivityThreshold = -1

# erzeugt eine recognized_activity
def createRecActivity(activityText, attribute, timestamp):
    rec_activity = {
        "activity": activityText,
        "attribute": attribute,
        "timestamp": timestamp
    }
    return rec_activity
    
# ToString für eine Rec_activity
def rec_activityToString(rec_activity):
    activity = rec_activity["activity"]
    attribute = rec_activity["attribute"]
    timestamp = rec_activity["timestamp"]
 
    if (attribute == ""):
        return activity
    else:
        return activity + "_" + attribute + "_" + timestamp

# Initiiert das Mapping, nachdem ein Schritt erkannt wurde
def init_mapping():
    global possible_matches
    global rec_activities
    global maxPossibleActivityThreshold

    possible_matches = process_activity_set
    rec_activities = []
    maxPossibleActivityThreshold = -1
    return

# Mapping ausgeben
def send_mapping(bpm_activity):
    jsonData = json.dumps(bpm_activity)
    mqtt.publish(mqtt.bpm_client, mqtt.bpm_topic, jsonData)
    init_mapping()

# Unpassende Mappings aus der Liste der möglichen Entfernen
def eliminate_mismatches(rec_activity):
    global possible_matches

    rec_activityText = rec_activity["activity"]
    rec_attributeText = rec_activity["attribute"]

    matches = possible_matches.copy() #Damit rauslöschen nicht die for schleife behindert

    for possible_match in possible_matches: # Iteriere durch die Highlevel Aktivities
        found=False
        for lowLevelActivity in possible_match["lowlevelActivities"]: # Iteriere durch deren Lowlevel Activities
            if (lowLevelActivity["activity"] == rec_activityText) & (lowLevelActivity["attribute"] == rec_attributeText): # Dann bleibt die HighLevelActivity im possible_matches drin
                found = True
                break
        if found:
            continue
        else:
            matches.remove(possible_match) #Damit rauslöschen nicht die for schleife behindert
    return matches

# Low Level Aktivität von HAR Modul erhalten
def lowLevelActivity_received(msg,tnow):
    global possible_matches
    global rec_activities
    global maxPossibleActivityThreshold
    global maxLowLevelActivityThreshold

    jsonMessage=json.loads(msg.payload.decode()) #decode json data

    activity = jsonMessage["activity"]
    attribute = jsonMessage["attribute"]

    rec_activity = createRecActivity(activity, attribute, tnow)
    rec_activities.append(rec_activity)
    
    old_possible_matches = possible_matches.copy() # Speichern für später, falls kein Mapping mehr möglich sein sollte
    possible_matches = eliminate_mismatches(rec_activity)
    

    # wenn nur noch ein mögliches Mapping da ist, dann abwarten bis alle Aktivitäten davon erkannt wurden
    if len(possible_matches) == 1:
        maxPossibleActivityThreshold = len(possible_matches[0]["lowlevelActivities"])

    # wenn alle aktivitäten erkannt & nur ein mögliches Mapping:
    if (len(rec_activities) == maxPossibleActivityThreshold) & (len(possible_matches) == 1):
        #Erflogreiches Mapping! --> Initialisieren und Mapping ausgeben
        send_mapping(possible_matches[0])

    if len(possible_matches) == 0: #Wenn keine Mappings mehr möglich, dann nimm aus den letzten Möglichkeiten das wahrscheinlichste! (Reihenfolge checken) Wichtig: Letzte erkannte Tätigkeit muss drinbleiben!
        print("Entscheidung treffen: Keine möglichen Mappings mehr da.")
        last_rec_activity = rec_activities[len(rec_activities) - 1]

        for i in range (0,len(rec_activities) - 2 ): # Weil letzte erkannte Activity ja dazu geführt hat, dass keine Mappings mehr möglich sind.
            new_matches = old_possible_matches.copy()
            for old_possible_match in old_possible_matches:
                if (old_possible_match["lowlevelActivities"][i]["activity"] == rec_activities[i]["activity"]) & (old_possible_match["lowlevelActivities"][i]["attribute"] == rec_activities[i]["attribute"]):

                    continue
                else:
                    #Eliminate mismatch
                    new_matches.remove(old_possible_match)
                    if (len(new_matches)==1):
                        break
            if (len(new_matches)==1):
                possible_matches = new_matches
                break         

        # TODO [Future Work] Invariante, wenn nichts gefunden! --> also wenn die Reihenfolge der LLA mit keiner HLA übereinstimmt 
        # Kein eindeutiges Mapping möglich --> flexiblere  Algorithmen einsetzen
        
        
        # nur noch ein Mapping möglich! --> Mapping ausgeben 
        send_mapping(possible_matches[0])
        # schon erkannte Activity nochmal überprüfen
        rec_activities = [last_rec_activity]
        possible_matches = eliminate_mismatches(last_rec_activity)
        if len(possible_matches) == 1:
            maxPossibleActivityThreshold = len(possible_matches[0]["lowlevelActivities"])
        
    # Maximale Anzahl an erkannten LowLevelActivities erreicht, aber mehrere Mappings möglich --> jetzt muss ein Mapping passieren
    if len(rec_activities) == maxLowLevelActivityThreshold:
        print("Entscheidung treffen: Maximale Anzahl an erkannten Lowlevel Activities.")
        for x in rec_activities:
            print(lla.lowLevelActivityToString(x))
            # TODO [Future Work]: Kann wegen Annahme (vgl. S. 87 in Ausarbeitung) hier nicht vorkommen 

    return
