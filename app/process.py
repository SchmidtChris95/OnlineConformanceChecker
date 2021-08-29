from . import highLevelActivities as hla
from . import lowLevelActivities as lla

# NOTE: Modify "active_process_set" and "active_process_lowLevelActivityTrace" to change example process!

# Geschäftsprozesse
BP_0_right = {
    "id":"BP_0_right",
    "processName": "Bending process (right handed)",
    "highlevelActivities": [hla.ID_0,hla.ID_1,hla.ID_2,hla.ID_3,hla.ID_4,hla.ID_5,hla.ID_6_right,hla.ID_7,hla.ID_8_right,hla.ID_9]
}
BP_0_left = {
    "id":"BP_0_left",
    "processName": "Bending process (left handed)",
    "highlevelActivities": [hla.ID_0,hla.ID_1,hla.ID_2,hla.ID_3,hla.ID_4,hla.ID_5,hla.ID_6_left,hla.ID_7,hla.ID_8_left,hla.ID_9]
}
BP_1 = {
    "id":"BP_1",
    "processName": "Quality process",
    "highlevelActivities": [hla.ID_10,hla.ID_11,hla.ID_12,hla.ID_13,hla.ID_14,hla.ID_15,hla.ID_16,hla.ID_17,hla.ID_18,hla.ID_19]
}
BP_2_right = {
    "id":"BP_2_right",
    "processName": "Punching process (right handed)",
    "highlevelActivities": [hla.ID_20,hla.ID_21,hla.ID_22,hla.ID_23,hla.ID_24,hla.ID_25_right,hla.ID_26,hla.ID_27]
}
BP_2_left = {
    "id":"BP_2_left",
    "processName": "Punching process (left handed)",
    "highlevelActivities": [hla.ID_20,hla.ID_21,hla.ID_22,hla.ID_23,hla.ID_24,hla.ID_25_left,hla.ID_26,hla.ID_27]
}
 
# Alle LowLevel Traces
BP_0_right_lowLevelActivityTrace = [ #BP0_right
    lla.WALK_INBOX,lla.BEND,lla.GRASP_BOTH,lla.WALK_MACHINE,                #ID0
    lla.LIFT_BOTH,lla.STRETCH_BOTH,lla.RELEASE_BOTH,                        #ID1
    lla.GRASP_BOTH,lla.STRETCH_BOTH,lla.PULL_BOTH,                          #ID2
    lla.WALK_TOOLBOX,lla.LIFT_BOTH,lla.GRASP_BOTH,                          #ID3
    lla.WALK_MACHINE,lla.ROTATE_BOTH,lla.RELEASE_BOTH,                      #ID4
    lla.WALK_UI,lla.TAP_LONG,lla.WALK_MACHINE,                              #ID5
    lla.LIFT_RIGHT,lla.GRASP_RIGHT,lla.PULL_RIGHT,lla.RELEASE_RIGHT,        #ID6
    lla.WALK_UI,lla.TAP_SHORT,lla.WALK_MACHINE,                             #ID7
    lla.GRASP_RIGHT,lla.LIFT_RIGHT,lla.RELEASE_RIGHT,lla.STRETCH_BOTH,      #ID8
    lla.GRASP_BOTH, lla.PULL_BOTH,lla.WALK_OUTBOX,lla.RELEASE_BOTH          #ID9
]

BP_0_left_lowLevelActivityTrace = [ #BP0_left
    lla.WALK_INBOX,lla.BEND,lla.GRASP_BOTH,lla.WALK_MACHINE,        #ID0
    lla.LIFT_BOTH,lla.STRETCH_BOTH,lla.RELEASE_BOTH,                #ID1
    lla.GRASP_BOTH,lla.STRETCH_BOTH,lla.PULL_BOTH,                  #ID2
    lla.WALK_TOOLBOX,lla.LIFT_BOTH,lla.GRASP_BOTH,                  #ID3
    lla.WALK_MACHINE,lla.ROTATE_BOTH,lla.RELEASE_BOTH,              #ID4
    lla.WALK_UI,lla.TAP_LONG,lla.WALK_MACHINE,                      #ID5
    lla.LIFT_LEFT,lla.GRASP_LEFT,lla.PULL_LEFT,lla.RELEASE_LEFT,    #ID6
    lla.WALK_UI,lla.TAP_SHORT,lla.WALK_MACHINE,                     #ID7
    lla.GRASP_LEFT,lla.LIFT_LEFT,lla.RELEASE_LEFT,lla.STRETCH_BOTH, #ID8
    lla.GRASP_BOTH, lla.PULL_BOTH,lla.WALK_OUTBOX,lla.RELEASE_BOTH  #ID9
]

BP_0_right_alternative_wrong1_lowLevelActivityTrace = [ #BP0_right_alternative_wrong1 
    lla.LIFT_BOTH,lla.STRETCH_BOTH,lla.RELEASE_BOTH,                    #ID1    # not conform (not a start activity)
    lla.WALK_INBOX,lla.BEND,lla.GRASP_BOTH,lla.WALK_MACHINE,            #ID0    # not conform (wrong order)
    lla.GRASP_BOTH,lla.STRETCH_BOTH,lla.PULL_BOTH,                      #ID2    # not conform (wrong order)
    lla.WALK_TOOLBOX,lla.LIFT_BOTH,lla.GRASP_BOTH,                      #ID3
    lla.WALK_MACHINE,lla.ROTATE_BOTH,lla.RELEASE_BOTH,                  #ID4
    lla.WALK_UI,lla.TAP_LONG,lla.WALK_MACHINE,                          #ID5
    lla.LIFT_RIGHT,lla.GRASP_RIGHT,lla.PULL_RIGHT,lla.RELEASE_RIGHT,    #ID6
    lla.WALK_UI,lla.TAP_SHORT,lla.WALK_MACHINE,                         #ID7
    lla.GRASP_RIGHT,lla.LIFT_RIGHT,lla.RELEASE_RIGHT,lla.STRETCH_BOTH,  #ID8
    lla.GRASP_BOTH, lla.PULL_BOTH,lla.WALK_OUTBOX,lla.RELEASE_BOTH      #ID9
]

BP_0_right_alternative_wrong2_lowLevelActivityTrace = [ #BP0_right_alternative_wrong2
    lla.WALK_INBOX,lla.BEND,lla.GRASP_BOTH,lla.WALK_MACHINE,            #ID0
    lla.LIFT_BOTH,lla.STRETCH_BOTH,lla.RELEASE_BOTH,                    #ID1
    lla.GRASP_BOTH,lla.STRETCH_BOTH,lla.PULL_BOTH,                      #ID2
    lla.WALK_MACHINE,lla.ROTATE_BOTH,lla.RELEASE_BOTH,                  #ID4    # not conform (wrong order)
    lla.WALK_TOOLBOX,lla.LIFT_BOTH,lla.GRASP_BOTH,                      #ID3    # not conform (wrong order)
    lla.WALK_UI,lla.TAP_LONG,lla.WALK_MACHINE,                          #ID5    # not conform (wrong order)
    lla.LIFT_RIGHT,lla.GRASP_RIGHT,lla.PULL_RIGHT,lla.RELEASE_RIGHT,    #ID6
    lla.WALK_UI,lla.TAP_SHORT,lla.WALK_MACHINE,                         #ID7
    lla.GRASP_RIGHT,lla.LIFT_RIGHT,lla.RELEASE_RIGHT,lla.STRETCH_BOTH,  #ID8
    lla.GRASP_BOTH, lla.PULL_BOTH,lla.WALK_OUTBOX,lla.RELEASE_BOTH      #ID9
]

BP_0_right_alternative_wrong3_lowLevelActivityTrace = [ #BP0_right_alternative_wrong3
    lla.WALK_INBOX,lla.BEND,lla.GRASP_BOTH,lla.WALK_MACHINE,            #ID0
    lla.LIFT_BOTH,lla.STRETCH_BOTH,lla.RELEASE_BOTH,                    #ID1
    lla.GRASP_BOTH, lla.PULL_BOTH,lla.WALK_OUTBOX,lla.RELEASE_BOTH,     #ID9    # not conform (wrong order)
    lla.GRASP_BOTH,lla.STRETCH_BOTH,lla.PULL_BOTH,                      #ID2    # not conform (wrong order)
    lla.WALK_TOOLBOX,lla.LIFT_BOTH,lla.GRASP_BOTH,                      #ID3
    lla.WALK_MACHINE,lla.ROTATE_BOTH,lla.RELEASE_BOTH,                  #ID4
    lla.WALK_UI,lla.TAP_LONG,lla.WALK_MACHINE,                          #ID5
    lla.LIFT_RIGHT,lla.GRASP_RIGHT,lla.PULL_RIGHT,lla.RELEASE_RIGHT,    #ID6
    lla.WALK_UI,lla.TAP_SHORT,lla.WALK_MACHINE,                         #ID7
    lla.GRASP_RIGHT,lla.LIFT_RIGHT,lla.RELEASE_RIGHT,lla.STRETCH_BOTH   #ID8    # not conform (end missing) # TODO
]

BP_1_lowLevelActivityTrace = [ #BP1
    lla.WALK_INBOX,lla.BEND,lla.GRASP_BOTH,lla.WALK_MACHINE,        #ID10
    lla.LIFT_BOTH,lla.STRETCH_BOTH,lla.RELEASE_BOTH,                #ID11
    lla.LIFT_RIGHT,lla.GRASP_RIGHT,                                 #ID12
    lla.BEND,lla.TAP_SHORT,lla.LIFT_RIGHT,lla.RELEASE_RIGHT,        #ID13
    lla.STRETCH_BOTH,lla.GRASP_BOTH,lla.PULL_BOTH,lla.RELEASE_BOTH, #ID14
    lla.TAP_LONG,lla.GRASP_BOTH,lla.STRETCH_BOTH,lla.RELEASE_BOTH,  #ID15
    lla.STRETCH_RIGHT,lla.GRASP_RIGHT,lla.TAP_SHORT,                #ID16
    lla.GRASP_BOTH,lla.PULL_BOTH,lla.WALK_OUTBOX,lla.RELEASE_BOTH,  #ID17
    lla.WALK_MACHINE,lla.LIFT_RIGHT,lla.TAP_SHORT                   #ID19
]

BP_1_alternative_lowLevelActivityTrace = [ #BP1_alternative
    lla.WALK_INBOX,lla.BEND,lla.GRASP_BOTH,lla.WALK_MACHINE,        #ID10
    lla.LIFT_BOTH,lla.STRETCH_BOTH,lla.RELEASE_BOTH,                #ID11
    lla.LIFT_RIGHT,lla.GRASP_RIGHT,                                 #ID12
    lla.BEND,lla.TAP_SHORT,lla.LIFT_RIGHT,lla.RELEASE_RIGHT,        #ID13
    lla.STRETCH_BOTH,lla.GRASP_BOTH,lla.PULL_BOTH,lla.RELEASE_BOTH, #ID14
    lla.TAP_LONG,lla.GRASP_BOTH,lla.STRETCH_BOTH,lla.RELEASE_BOTH,  #ID15
    lla.GRASP_BOTH,lla.PULL_BOTH,lla.WALK_REBOX,lla.RELEASE_BOTH,   #ID18
    lla.WALK_MACHINE,lla.LIFT_RIGHT,lla.TAP_SHORT                   #ID19
]

BP_2_right_lowLevelActivityTrace = [
    lla.WALK_TOOLBOX,lla.LIFT_BOTH,lla.GRASP_BOTH,lla.WALK_MACHINE,                     #ID20
    lla.STRETCH_BOTH,lla.ROTATE_BOTH,lla.RELEASE_BOTH,                                  #ID21
    lla.WALK_UI,lla.TAP_LONG,                                                           #ID22
    lla.LIFT_RIGHT,lla.GRASP_RIGHT,lla.PULL_RIGHT,lla.LIFT_RIGHT,lla.RELEASE_RIGHT,     #ID23
    lla.WALK_MACHINE,lla.STRETCH_BOTH,lla.GRASP_BOTH,lla.WALK_OUTBOX,lla.RELEASE_BOTH,  #ID24
    lla.WALK_MACHINE,lla.LIFT_BOTH,lla.STRETCH_BOTH,lla.ROTATE_BOTH,lla.PULL_BOTH,      #ID26
    lla.WALK_TOOLBOX,lla.LIFT_BOTH,lla.RELEASE_BOTH                                     #ID27
]

BP_2_left_lowLevelActivityTrace = [
    lla.WALK_TOOLBOX,lla.LIFT_BOTH,lla.GRASP_BOTH,lla.WALK_MACHINE,                     #ID20
    lla.STRETCH_BOTH,lla.ROTATE_BOTH,lla.RELEASE_BOTH,                                  #ID21
    lla.WALK_UI,lla.TAP_LONG,                                                           #ID22
    lla.LIFT_RIGHT,lla.GRASP_RIGHT,lla.PULL_RIGHT,lla.LIFT_RIGHT,lla.RELEASE_RIGHT,     #ID23
    lla.WALK_MACHINE,lla.STRETCH_BOTH,lla.GRASP_BOTH,lla.WALK_OUTBOX,lla.RELEASE_BOTH,  #ID24
    lla.WALK_MACHINE,lla.LIFT_LEFT,lla.STRETCH_LEFT,lla.ROTATE_LEFT,                    #ID25
    lla.WALK_UI,lla.TAP_LONG,                                                           #ID22
    lla.LIFT_RIGHT,lla.GRASP_RIGHT,lla.PULL_RIGHT,lla.LIFT_RIGHT,lla.RELEASE_RIGHT,     #ID23
    lla.WALK_MACHINE,lla.STRETCH_BOTH,lla.GRASP_BOTH,lla.WALK_OUTBOX,lla.RELEASE_BOTH,  #ID24
    lla.WALK_MACHINE,lla.LIFT_BOTH,lla.STRETCH_BOTH,lla.ROTATE_BOTH,lla.PULL_BOTH,      #ID26
    lla.WALK_TOOLBOX,lla.LIFT_BOTH,lla.RELEASE_BOTH                                     #ID27
]

BP_2_right_alternative_lowLevelActivityTrace = [
    lla.WALK_TOOLBOX,lla.LIFT_BOTH,lla.GRASP_BOTH,lla.WALK_MACHINE,                      #ID20
    lla.STRETCH_BOTH,lla.ROTATE_BOTH,lla.RELEASE_BOTH,                                   #ID21
    lla.WALK_UI,lla.TAP_LONG,                                                            #ID22
    lla.LIFT_RIGHT,lla.GRASP_RIGHT,lla.PULL_RIGHT,lla.LIFT_RIGHT,lla.RELEASE_RIGHT,      #ID23
    lla.WALK_MACHINE,lla.STRETCH_BOTH,lla.GRASP_BOTH,lla.WALK_OUTBOX,lla.RELEASE_BOTH,   #ID24
    lla.WALK_MACHINE,lla.LIFT_RIGHT,lla.STRETCH_RIGHT,lla.ROTATE_RIGHT,                  #ID25
    lla.WALK_UI,lla.TAP_LONG,                                                            #ID22
    lla.LIFT_RIGHT,lla.GRASP_RIGHT,lla.PULL_RIGHT,lla.LIFT_RIGHT,lla.RELEASE_RIGHT,      #ID23
    lla.WALK_MACHINE,lla.STRETCH_BOTH,lla.GRASP_BOTH,lla.WALK_OUTBOX,lla.RELEASE_BOTH,   #ID24
    lla.WALK_MACHINE,lla.LIFT_BOTH,lla.STRETCH_BOTH,lla.ROTATE_BOTH,lla.PULL_BOTH,       #ID26
    lla.WALK_TOOLBOX,lla.LIFT_BOTH,lla.RELEASE_BOTH                                      #ID27
]

BP_2_right_alternative2_lowLevelActivityTrace = [
    lla.WALK_TOOLBOX,lla.LIFT_BOTH,lla.GRASP_BOTH,lla.WALK_MACHINE,                      #ID20
    lla.STRETCH_BOTH,lla.ROTATE_BOTH,lla.RELEASE_BOTH,                                   #ID21
    lla.WALK_UI,lla.TAP_LONG,                                                            #ID22
    lla.LIFT_RIGHT,lla.GRASP_RIGHT,lla.PULL_RIGHT,lla.LIFT_RIGHT,lla.RELEASE_RIGHT,      #ID23
    lla.WALK_MACHINE,lla.STRETCH_BOTH,lla.GRASP_BOTH,lla.WALK_OUTBOX,lla.RELEASE_BOTH,   #ID24
    lla.WALK_MACHINE,lla.LIFT_RIGHT,lla.STRETCH_RIGHT,lla.ROTATE_RIGHT,                  #ID25
    lla.WALK_UI,lla.TAP_LONG,                                                            #ID22
    lla.LIFT_RIGHT,lla.GRASP_RIGHT,lla.PULL_RIGHT,lla.LIFT_RIGHT,lla.RELEASE_RIGHT,      #ID23
    lla.WALK_MACHINE,lla.STRETCH_BOTH,lla.GRASP_BOTH,lla.WALK_OUTBOX,lla.RELEASE_BOTH,   #ID24
    lla.WALK_MACHINE,lla.LIFT_RIGHT,lla.STRETCH_RIGHT,lla.ROTATE_RIGHT,                  #ID25
    lla.WALK_UI,lla.TAP_LONG,                                                            #ID22
    lla.LIFT_RIGHT,lla.GRASP_RIGHT,lla.PULL_RIGHT,lla.LIFT_RIGHT,lla.RELEASE_RIGHT,      #ID23
    lla.WALK_MACHINE,lla.STRETCH_BOTH,lla.GRASP_BOTH,lla.WALK_OUTBOX,lla.RELEASE_BOTH,   #ID24
    lla.WALK_MACHINE,lla.LIFT_BOTH,lla.STRETCH_BOTH,lla.ROTATE_BOTH,lla.PULL_BOTH,       #ID26
    lla.WALK_TOOLBOX,lla.LIFT_BOTH,lla.RELEASE_BOTH                                      #ID27
]

BP_2_right_alternative_wrong1_lowLevelActivityTrace = [
    lla.WALK_TOOLBOX,lla.LIFT_BOTH,lla.GRASP_BOTH,lla.WALK_MACHINE,                      #ID20
    lla.STRETCH_BOTH,lla.ROTATE_BOTH,lla.RELEASE_BOTH,                                   #ID21
    lla.WALK_UI,lla.TAP_LONG,                                                            #ID22
    lla.LIFT_RIGHT,lla.GRASP_RIGHT,lla.PULL_RIGHT,lla.LIFT_RIGHT,lla.RELEASE_RIGHT,      #ID23
    lla.WALK_MACHINE,lla.STRETCH_BOTH,lla.GRASP_BOTH,lla.WALK_OUTBOX,lla.RELEASE_BOTH,   #ID24
    lla.WALK_MACHINE,lla.LIFT_RIGHT,lla.STRETCH_RIGHT,lla.ROTATE_RIGHT,                  #ID25
    lla.WALK_UI,lla.TAP_LONG,                                                            #ID22
    lla.LIFT_RIGHT,lla.GRASP_RIGHT,lla.PULL_RIGHT,lla.LIFT_RIGHT,lla.RELEASE_RIGHT,      #ID23
    lla.WALK_MACHINE,lla.STRETCH_BOTH,lla.GRASP_BOTH,lla.WALK_OUTBOX,lla.RELEASE_BOTH,   #ID24
    lla.WALK_MACHINE,lla.LIFT_RIGHT,lla.STRETCH_RIGHT,lla.ROTATE_RIGHT,                  #ID25
    lla.WALK_UI,lla.TAP_LONG,                                                            #ID22
    lla.LIFT_RIGHT,lla.GRASP_RIGHT,lla.PULL_RIGHT,lla.LIFT_RIGHT,lla.RELEASE_RIGHT,      #ID23
    lla.WALK_MACHINE,lla.STRETCH_BOTH,lla.GRASP_BOTH,lla.WALK_OUTBOX,lla.RELEASE_BOTH,   #ID24
    lla.WALK_MACHINE,lla.LIFT_RIGHT,lla.STRETCH_RIGHT,lla.ROTATE_RIGHT,                  #ID25      Not conform (max Occurance exceeded)
    lla.WALK_UI,lla.TAP_LONG,                                                            #ID22      Not conform (max Occurance exceeded)
    lla.LIFT_RIGHT,lla.GRASP_RIGHT,lla.PULL_RIGHT,lla.LIFT_RIGHT,lla.RELEASE_RIGHT,      #ID23      Not conform (max Occurance exceeded)
    lla.WALK_MACHINE,lla.STRETCH_BOTH,lla.GRASP_BOTH,lla.WALK_OUTBOX,lla.RELEASE_BOTH,   #ID24      Not conform (max Occurance exceeded)
    lla.WALK_MACHINE,lla.LIFT_BOTH,lla.STRETCH_BOTH,lla.ROTATE_BOTH,lla.PULL_BOTH,       #ID26
    lla.WALK_TOOLBOX,lla.LIFT_BOTH,lla.RELEASE_BOTH                                      #ID27
]

BP_2_right_alternative_wrong2_lowLevelActivityTrace = [
    lla.STRETCH_BOTH,lla.ROTATE_BOTH,lla.RELEASE_BOTH,                                   #ID21      Not conform (not a start activity)
    lla.WALK_TOOLBOX,lla.LIFT_BOTH,lla.GRASP_BOTH,lla.WALK_MACHINE,                      #ID20      Not conform (order)
    lla.STRETCH_BOTH,lla.ROTATE_BOTH,lla.RELEASE_BOTH,                                   #ID21      Not conform (max Occurance exceeded)
    lla.WALK_UI,lla.TAP_LONG,                                                            #ID22
    lla.LIFT_RIGHT,lla.GRASP_RIGHT,lla.PULL_RIGHT,lla.LIFT_RIGHT,lla.RELEASE_RIGHT,      #ID23
    lla.WALK_MACHINE,lla.STRETCH_BOTH,lla.GRASP_BOTH,lla.WALK_OUTBOX,lla.RELEASE_BOTH,   #ID24
    lla.WALK_MACHINE,lla.LIFT_RIGHT,lla.STRETCH_RIGHT,lla.ROTATE_RIGHT,                  #ID25
    lla.LIFT_RIGHT,lla.GRASP_RIGHT,lla.PULL_RIGHT,lla.LIFT_RIGHT,lla.RELEASE_RIGHT,      #ID23      Not conform (order)
    lla.WALK_UI,lla.TAP_LONG,                                                            #ID22      Not conform (order)
    lla.WALK_MACHINE,lla.STRETCH_BOTH,lla.GRASP_BOTH,lla.WALK_OUTBOX,lla.RELEASE_BOTH,   #ID24      Not conform (order)
    lla.WALK_MACHINE,lla.LIFT_RIGHT,lla.STRETCH_RIGHT,lla.ROTATE_RIGHT,                  #ID25
    lla.WALK_UI,lla.TAP_LONG,                                                            #ID22
    lla.LIFT_RIGHT,lla.GRASP_RIGHT,lla.PULL_RIGHT,lla.LIFT_RIGHT,lla.RELEASE_RIGHT,      #ID23
    lla.WALK_MACHINE,lla.STRETCH_BOTH,lla.GRASP_BOTH,lla.WALK_OUTBOX,lla.RELEASE_BOTH,   #ID24
    lla.WALK_MACHINE,lla.LIFT_RIGHT,lla.STRETCH_RIGHT,lla.ROTATE_RIGHT,                  #ID25      Not conform (max Occurance exceeded)
    lla.WALK_UI,lla.TAP_LONG,                                                            #ID22      Not conform (max Occurance exceeded)
    lla.LIFT_RIGHT,lla.GRASP_RIGHT,lla.PULL_RIGHT,lla.LIFT_RIGHT,lla.RELEASE_RIGHT,      #ID23      Not conform (max Occurance exceeded)
    lla.WALK_MACHINE,lla.STRETCH_BOTH,lla.GRASP_BOTH,lla.WALK_OUTBOX,lla.RELEASE_BOTH,   #ID24      Not conform (max Occurance exceeded)
    lla.WALK_MACHINE,lla.LIFT_BOTH,lla.STRETCH_BOTH,lla.ROTATE_BOTH,lla.PULL_BOTH,       #ID26
    lla.WALK_TOOLBOX,lla.LIFT_BOTH,lla.RELEASE_BOTH                                      #ID27
]

#######################################################
# Alle möglichen HLA aus dem aktiven Geschäftsprozess #
#######################################################

# active_process_set = BP_0_right["highlevelActivities"] 
# active_process_set = BP_0_left["highlevelActivities"] 
# active_process_set = BP_1["highlevelActivities"] 
active_process_set = BP_2_right["highlevelActivities"] 
# active_process_set = BP_2_left["highlevelActivities"] 

###########################################
# LowLevelActitity Trace für Dataproducer #
###########################################

# active_process_lowLevelActivityTrace = BP_0_right_lowLevelActivityTrace
# active_process_lowLevelActivityTrace = BP_0_left_lowLevelActivityTrace
# active_process_lowLevelActivityTrace = BP_0_right_alternative_wrong1_lowLevelActivityTrace
# active_process_lowLevelActivityTrace = BP_0_right_alternative_wrong2_lowLevelActivityTrace
# active_process_lowLevelActivityTrace = BP_0_right_alternative_wrong3_lowLevelActivityTrace
# active_process_lowLevelActivityTrace = BP_1_lowLevelActivityTrace
# active_process_lowLevelActivityTrace = BP_1_alternative_lowLevelActivityTrace
# active_process_lowLevelActivityTrace = BP_2_right_lowLevelActivityTrace
# active_process_lowLevelActivityTrace = BP_2_left_lowLevelActivityTrace
# active_process_lowLevelActivityTrace = BP_2_right_alternative_lowLevelActivityTrace 
# active_process_lowLevelActivityTrace = BP_2_right_alternative2_lowLevelActivityTrace 
# active_process_lowLevelActivityTrace = BP_2_right_alternative_wrong1_lowLevelActivityTrace
active_process_lowLevelActivityTrace = BP_2_right_alternative_wrong2_lowLevelActivityTrace 
