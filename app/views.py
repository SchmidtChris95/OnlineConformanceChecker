from datetime import datetime
from flask import Flask, render_template, jsonify
import eventlet
from flask_socketio import SocketIO
from . import mqtt
from . import bpm
from . import app

# eventlet.monkey_patch()
socketio = SocketIO(app)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/bpmnViewer/")
def bpmnViewer():
    return render_template("bpmn_Viewer.html")

@app.route("/activityRecognition/")
def activityRecognition():
    return render_template("activity_recognition.html")

@app.route("/processStepMapping/")
def processStepMapping():
    return render_template("process_step_mapping.html")

@app.route("/onlineConformanceCheck/")
def onlineConformanceCheck():
    return render_template("conformance_check.html")

@app.route("/start_all", methods=["POST"])
def start_all():

    start_har()
    start_bpm()
    start_occ()
    
    response = {
            "source": "start_all"
        }
    return jsonify(response)

@app.route("/stop_all", methods=["POST"])
def stop_all():

    stop_har()
    stop_bpm()
    stop_occ()
    
    response = {
            "source": "stop_all"
        }
    return jsonify(response)

@app.route("/start_har", methods=["POST"])
def start_har():

    global socketio


    # Falls schon angelegt
    if mqtt.har_client != "":
        response = {
            "message": "HAR already started.",
            "source": "start_har"
        }
        return jsonify(response),500

    mqtt.har_client = mqtt.connect_mqtt()
    mqtt.subscribe(mqtt.har_client, socketio, mqtt.har_topic)
    mqtt.har_client.loop_start()

    # mqtt.publish(mqtt.har_client,"testMsg1")
    
    response = {
            "source": "start_har"
        }
    return jsonify(response)

@app.route("/stop_har", methods=["POST"])
def stop_har():
    # falls noch nicht angelegt
    if mqtt.har_client == "":
        response = {
            "message": "Not yet started.",
            "source": "stop_har"
        }
        return jsonify(response),500
    
    mqtt.disconnect(mqtt.har_client)
    mqtt.har_client = ""
    
    response = {
           "source": "stop_har"
        }
    return jsonify(response)

@app.route("/start_bpm", methods=["POST"])
def start_bpm():

    global socketio

    # Falls schon angelegt
    if mqtt.bpm_client != "":
        response = {
            "message": "BP mapping already started.",
            "source": "start_bpm"
        }
        return jsonify(response),500
    
    bpm.init_mapping()
    mqtt.bpm_client = mqtt.connect_mqtt()
    mqtt.subscribe(mqtt.bpm_client, socketio, mqtt.bpm_topic)
    mqtt.bpm_client.loop_start()
    
    response = {
            "source": "start_bpm"
        }
    return jsonify(response)

@app.route("/stop_bpm", methods=["POST"])
def stop_bpm():

    # falls noch nicht angelegt
    if mqtt.bpm_client == "":
        response = {
            "message": "Not yet started.",
            "source": "stop_bpm"
        }
        return jsonify(response),500
    
    mqtt.disconnect(mqtt.bpm_client)
    mqtt.bpm_client = ""
    
    response = {
           "source": "stop_bpm"
        }
    return jsonify(response)

@app.route("/start_occ", methods=["POST"])
def start_occ():

    global socketio

    # Falls schon angelegt
    if mqtt.occ_client != "":
        response = {
            "message": "OCC already started.",
            "source": "start_occ"
        }
        return jsonify(response),500
    
    mqtt.occ_client = mqtt.connect_mqtt()
    mqtt.subscribe(mqtt.occ_client, socketio, mqtt.occ_topic)
    mqtt.occ_client.loop_start()
    
    response = {
            "source": "start_occ"
        }
    return jsonify(response)

@app.route("/stop_occ", methods=["POST"])
def stop_occ():
    # falls noch nicht angelegt
    if mqtt.occ_client == "":
        response = {
            "message": "Not yet started.",
            "source": "stop_occ"
        }
        return jsonify(response),500
    
    mqtt.disconnect(mqtt.occ_client)
    mqtt.occ_client = ""
    
    response = {
           "source": "stop_occ"
        }
    return jsonify(response)

@app.route("/start_dp", methods=["POST"])
def start_dp():

    # falls schon gestartet
    if mqtt.dataProducer == True:
        response = {
            "message": "DataProducer already started.",
            "source": "start_dp"
        }
        return jsonify(response),500
    
    mqtt.dataProducer = True
    mqtt.dp_client = mqtt.connect_mqtt()
    mqtt.startDataProducer(mqtt.dp_client, mqtt.har_topic, mqtt.bpm_topic, mqtt.occ_topic)
    
    response = {
           "source": "start_dp"
        }
    return jsonify(response)

@app.route("/stop_dp", methods=["POST"])
def stop_dp():

    # falls noch nicht gestarted
    if mqtt.dataProducer == False:
        response = {
            "message": "DataProducer not yet started.",
            "source": "stop_dp"
        }
        return jsonify(response),500    

    mqtt.dataProducer = False
    mqtt.disconnect(mqtt.dp_client)
    mqtt.dp_client = ""

    
    response = {
           "source": "stop_dp"
        }
    return jsonify(response)