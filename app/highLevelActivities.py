from . import lowLevelActivities as lla

ID_0 = {
    "id":0,
    "name": "Take material out of input box",
    "lowlevelActivities": [lla.WALK_INBOX,lla.BEND,lla.GRASP_BOTH,lla.WALK_MACHINE],
    "pred": [],
    "succ": [1],
    "maxOccurrence": 1,
    "maxProcessingTime": 10 
}
ID_1 = {
    "id":1,
    "name": "Place material in bending machine",
    "lowlevelActivities": [lla.LIFT_BOTH,lla.STRETCH_BOTH,lla.RELEASE_BOTH,],
    "pred": [0],
    "succ": [2],
    "maxOccurrence" : 1,
    "maxProcessingTime": 10
}
ID_2 = {
    "id":2,
    "name": "Align material in the bending machine",
    "lowlevelActivities": [lla.GRASP_BOTH,lla.STRETCH_BOTH,lla.PULL_BOTH],
    "pred": [1],
    "succ": [3],
    "maxOccurrence" : 1,
    "maxProcessingTime": 10
}
ID_3 = {
    "id":3,
    "name": "Take bending tool",
    "lowlevelActivities": [lla.WALK_TOOLBOX,lla.LIFT_BOTH,lla.GRASP_BOTH],
    "pred": [2],
    "succ": [4],
    "maxOccurrence" : 1,
    "maxProcessingTime": 10
}
ID_4 = {
    "id":4,
    "name": "Place bending tool in machine",
    "lowlevelActivities": [lla.WALK_MACHINE,lla.ROTATE_BOTH,lla.RELEASE_BOTH,],
    "pred": [3],
    "succ": [5],
    "maxOccurrence" : 1,
    "maxProcessingTime": 10
}
ID_5 = {
    "id":5,
    "name": "Choose bending profile on machine UI and insert parameter",
    "lowlevelActivities": [lla.WALK_UI,lla.TAP_LONG,lla.WALK_MACHINE,],
    "pred": [4],
    "succ": [6],
    "maxOccurrence" : 1,
    "maxProcessingTime": 10
}
ID_6_right = {
    "id":6,
    "name": "Close the machine lid",
    "lowlevelActivities": [lla.LIFT_RIGHT,lla.GRASP_RIGHT,lla.PULL_RIGHT,lla.RELEASE_RIGHT],
    "pred": [5],
    "succ": [7],
    "maxOccurrence" : 1,
    "maxProcessingTime": 10
}
ID_6_left = {
    "id":6,
    "name": "Close the machine lid",
    "lowlevelActivities": [lla.LIFT_LEFT,lla.GRASP_LEFT,lla.PULL_LEFT,lla.RELEASE_LEFT],
    "pred": [5],
    "succ": [7],
    "maxOccurrence" : 1,
    "maxProcessingTime": 10
}
ID_7 = {
    "id":7,
    "name": "Press start button",
    "lowlevelActivities": [lla.WALK_UI,lla.TAP_SHORT,lla.WALK_MACHINE],
    "pred": [6],
    "succ": [8],
    "maxOccurrence" : 1,
    "maxProcessingTime": 10
}
ID_8_right = {
    "id":8,
    "name": "Open the machine lid again",
    "lowlevelActivities": [lla.GRASP_RIGHT,lla.LIFT_RIGHT,lla.RELEASE_RIGHT, lla.STRETCH_BOTH],
    "pred": [7],
    "succ": [9],
    "maxOccurrence" : 1,
    "maxProcessingTime": 10
}
ID_8_left = {
    "id":8,
    "name": "Open the machine lid again",
    "lowlevelActivities": [lla.GRASP_LEFT,lla.LIFT_LEFT,lla.RELEASE_LEFT, lla.STRETCH_BOTH],
    "pred": [7],
    "succ": [9],
    "maxOccurrence" : 1,
    "maxProcessingTime": 10
}
ID_9 = {
    "id":9,
    "name": "Pull out bended material and place it in the output box",
    "lowlevelActivities": [lla.GRASP_BOTH, lla.PULL_BOTH,lla.WALK_OUTBOX,lla.RELEASE_BOTH],
    "pred": [8],
    "succ": [],
    "maxOccurrence" : 1,
    "maxProcessingTime": 10
}
# -----------------------------
ID_10 = {
    "id":10,
    "name": "Take material out of input box",
    "lowlevelActivities": [lla.WALK_INBOX,lla.BEND,lla.GRASP_BOTH,lla.WALK_MACHINE],
    "pred": [],
    "succ": [11],
    "maxOccurrence" : 1,
    "maxProcessingTime": 10
}
ID_11 = {
    "id":11,
    "name": "Place material on screening table",
    "lowlevelActivities": [lla.LIFT_BOTH,lla.STRETCH_BOTH,lla.RELEASE_BOTH],
    "pred": [10],
    "succ": [12],
    "maxOccurrence" : 1,
    "maxProcessingTime": 10
}
ID_12 = {
    "id":12,
    "name": "Take QR code scanner",
    "lowlevelActivities": [lla.LIFT_RIGHT, lla.GRASP_RIGHT],
    "pred": [11],
    "succ": [13],
    "maxOccurrence" : 1,
    "maxProcessingTime": 10
}
ID_13 = {
    "id":13,
    "name": "Scan material code and put scanner away",
    "lowlevelActivities": [lla.BEND,lla.TAP_SHORT,lla.LIFT_RIGHT,lla.RELEASE_RIGHT],
    "pred": [12],
    "succ": [14],
    "maxOccurrence" : 1,
    "maxProcessingTime": 10
}
ID_14 = {
    "id":14,
    "name": "Adjust measuring device",
    "lowlevelActivities": [lla.STRETCH_BOTH,lla.GRASP_BOTH,lla.PULL_BOTH,lla.RELEASE_BOTH],
    "pred": [13],
    "succ": [15],
    "maxOccurrence" : 1,
    "maxProcessingTime": 10
}
ID_15 = {
    "id":15,
    "name": "Measure bending angle",
    "lowlevelActivities": [lla.TAP_LONG,lla.GRASP_BOTH,lla.STRETCH_BOTH,lla.RELEASE_BOTH],
    "pred": [14],
    "succ": [16,18],
    "maxOccurrence" : 1,
    "maxProcessingTime": 10
}
ID_16 = {
    "id":16,
    "name": "Attach seal of quality",
    "lowlevelActivities": [lla.STRETCH_RIGHT,lla.GRASP_RIGHT,lla.TAP_SHORT],
    "pred": [15],
    "succ": [17],
    "maxOccurrence" : 1,
    "maxProcessingTime": 10
}
ID_17 = {
    "id":17,
    "name": "Place material in the output box",
    "lowlevelActivities": [lla.GRASP_BOTH,lla.PULL_BOTH,lla.WALK_OUTBOX,lla.RELEASE_BOTH],
    "pred": [16],
    "succ": [19],
    "maxOccurrence" : 1,
    "maxProcessingTime": 10
}
ID_18 = {
    "id":18,
    "name": "Place material in the rework box",
    "lowlevelActivities": [lla.GRASP_BOTH,lla.PULL_BOTH,lla.WALK_REBOX,lla.RELEASE_BOTH],
    "pred": [15],
    "succ": [19],
    "maxOccurrence" : 1,
    "maxProcessingTime": 10
}
ID_19 = {
    "id":19,
    "name": "Update material status in system",
    "lowlevelActivities": [lla.WALK_MACHINE,lla.LIFT_RIGHT,lla.TAP_SHORT],
    "pred": [17,18],
    "succ": [],
    "maxOccurrence" : 1,
    "maxProcessingTime": 10
}
# -----------------------------
ID_20 = {
    "id":20,
    "name": "Take cutting die from toolbox",
    "lowlevelActivities": [lla.WALK_TOOLBOX,lla.LIFT_BOTH,lla.GRASP_BOTH,lla.WALK_MACHINE],
    "pred": [],
    "succ": [21],
    "maxOccurrence" : 1,
    "maxProcessingTime": 10
}
ID_21 = {
    "id":21,
    "name": "Put cutting die into the machine",
    "lowlevelActivities": [lla.STRETCH_BOTH,lla.ROTATE_BOTH,lla.RELEASE_BOTH],
    "pred": [20],
    "succ": [22],
    "maxOccurrence" : 1,
    "maxProcessingTime": 10
}
ID_22 = {
    "id":22,
    "name": "Adjust punching machine",
    "lowlevelActivities": [lla.WALK_UI,lla.TAP_LONG],
    "pred": [21,25],
    "succ": [23],
    "maxOccurrence" : 3,
    "maxProcessingTime": 10
}
ID_23 = {
    "id":23,
    "name": "Punch material",
    "lowlevelActivities": [lla.LIFT_RIGHT,lla.GRASP_RIGHT,lla.PULL_RIGHT,lla.LIFT_RIGHT,lla.RELEASE_RIGHT],
    "pred": [22],
    "succ": [24],
    "maxOccurrence" : 3,
    "maxProcessingTime": 15
}
ID_24 = {
    "id":24,
    "name": "Place punched part in output box",
    "lowlevelActivities": [lla.WALK_MACHINE,lla.STRETCH_BOTH,lla.GRASP_BOTH,lla.WALK_OUTBOX,lla.RELEASE_BOTH],
    "pred": [23],
    "succ": [25,26],
    "maxOccurrence" : 3,
    "maxProcessingTime": 10
}
ID_25_right = {
    "id":25,
    "name": "Remove metal shavings from cutting die",
    "lowlevelActivities": [lla.WALK_MACHINE,lla.LIFT_RIGHT,lla.STRETCH_RIGHT,lla.ROTATE_RIGHT],
    "pred": [24],
    "succ": [22],
    "maxOccurrence" : 2,
    "maxProcessingTime": 10
}
ID_25_left = {
    "id":25,
    "name": "Remove metal shavings from cutting die",
    "lowlevelActivities": [lla.WALK_MACHINE,lla.LIFT_LEFT,lla.STRETCH_LEFT,lla.ROTATE_LEFT],
    "pred": [24],
    "succ": [22],
    "maxOccurrence" : 2,
    "maxProcessingTime": 10
}
ID_26 = {
    "id":26,
    "name": "Remove cutting die",
    "lowlevelActivities": [lla.WALK_MACHINE,lla.LIFT_BOTH,lla.STRETCH_BOTH,lla.ROTATE_BOTH,lla.PULL_BOTH],
    "pred": [24],
    "succ": [27],
    "maxOccurrence" : 1,
    "maxProcessingTime": 15
}
ID_27 = {
    "id":27,
    "name": "Put cutting die back in toolbox",
    "lowlevelActivities": [lla.WALK_TOOLBOX,lla.LIFT_BOTH,lla.RELEASE_BOTH],
    "pred": [26],
    "succ": [],
    "maxOccurrence" : 1,
    "maxProcessingTime": 10
}

# erzeugt ein Custom Activity
def createCustomHighLevelActivity(id, name, lowlevelActivities, pred, succ, maxOccurrence, maxProcessingTime):
    highLevelactivity = {
        "id": id,
        "name": name,
        "lowlevelActivities": lowlevelActivities,
        "pred": pred,
        "succ": succ,
        "maxOccurrence" : maxOccurrence,
        "maxProcessingTime" : maxProcessingTime
    }
    return highLevelactivity
