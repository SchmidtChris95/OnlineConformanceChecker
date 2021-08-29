WALK_INBOX = {
    "activity": "walk",
    "attribute": "inbox"
}
WALK_MACHINE = {
    "activity": "walk",
    "attribute": "machine"
}
WALK_TOOLBOX = {
    "activity": "walk",
    "attribute": "toolbox"
}
WALK_OUTBOX = {
    "activity": "walk",
    "attribute": "outbox"
}
WALK_UI = {
    "activity": "walk",
    "attribute": "ui"
}
WALK_REBOX = {
    "activity": "walk",
    "attribute": "rebox"
}
BEND = {
    "activity": "bend",
    "attribute": ""
}
GRASP_RIGHT = {
    "activity": "grasp",
    "attribute": "right"
}
GRASP_LEFT = {
    "activity": "grasp",
    "attribute": "left"
}
GRASP_BOTH = {
    "activity": "grasp",
    "attribute": "both"
}
LIFT_RIGHT = {
    "activity": "lift",
    "attribute": "right"
}
LIFT_LEFT = {
    "activity": "lift",
    "attribute": "left"
}
LIFT_BOTH = {
    "activity": "lift",
    "attribute": "both"
}
STRETCH_RIGHT = {
    "activity": "stretch",
    "attribute": "right"
}
STRETCH_LEFT = {
    "activity": "stretch",
    "attribute": "left"
}
STRETCH_BOTH = {
    "activity": "stretch",
    "attribute": "both"
}
PULL_RIGHT = {
    "activity": "pull",
    "attribute": "right"
}
PULL_LEFT = {
    "activity": "pull",
    "attribute": "left"
}
PULL_BOTH = {
    "activity": "pull",
    "attribute": "both"
}
RELEASE_RIGHT = {
    "activity": "release",
    "attribute": "right"
}
RELEASE_LEFT = {
    "activity": "release",
    "attribute": "left"
}
RELEASE_BOTH = {
    "activity": "release",
    "attribute": "both"
}
TAP_LONG = {
    "activity": "tap",
    "attribute": "long"
}
TAP_SHORT = {
    "activity": "tap",
    "attribute": "short"
}
ROTATE_BOTH = {
    "activity": "rotate",
    "attribute": "both"
}
ROTATE_RIGHT = {
    "activity": "rotate",
    "attribute": "right"
}
ROTATE_LEFT = {
    "activity": "rotate",
    "attribute": "left"
}



# erzeugt ein Custom Activity
def createCustomLowLevelActivity(activityText, attribute):
    lowLevelactivity = {
        "activity": activityText,
        "attribute": attribute
    }
    return lowLevelactivity

def lowLevelActivityToString(lowLevelActivity):

    activity = lowLevelActivity["activity"]
    attribute = lowLevelActivity["attribute"]
    
    if (attribute == ""):
        return activity
    else:
        return activity + "_" + attribute