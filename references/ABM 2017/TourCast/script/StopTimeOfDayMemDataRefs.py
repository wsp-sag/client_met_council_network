####################################################################
# StopTimeOfDayMemDataRefs.py
# import this using
# from StopTimeOfDayMemDataRefs import *
####################################################################

# All data references for the Stop Time of Day subcomponents are memory references 
# data reference rows are fed to the subcomponents by the main component
# in general each subcomponent uses only a subset of the supplied data rows
dataReferences = [

    {"type" : "memory",
     "dataType" : "int",
     "name" : "Person",
     "columns" : [  "isChild",          # 0  
                    "isChild1",         # 1
                    "isChild2",         # 2
                    "isChild3",         # 3
                    "isNonWorkingAdult",# 4
                    "isSenior",         # 5,
                    "isPartTimeWorker", # 6,
                    "isFullTimeWorker", # 7
                    "isAdultStudent",   # 8
                 ],
    },
    {"type" : "memory",
     "dataType" : "int",
     "name" : "Day",
     "columns" : [  "hasEarlierTour",     # 0
                    "hasLaterTour",       # 1
                    "1+additionalStops",  # 2
                    "2additionalStops",   # 3 
                 ],
    },
    {"type" : "memory",
     "dataType" : "int",
     "name" : "Tour",
     "columns" : [  "tourPurpose",              # 0     For possible segmentation
                    "tourDuration0to1",         # 1
                    "tourDuration2to3",         # 2
                    "tourDuration16+",          # 3
                    "arrivalBefore6:00am",     	# 4 
                    "arrival6:30amTo9:00am",    # 5
                    "arrivalBefore9:00am",      # 6
                    "arrival9:00amTo12pm",      # 7
                    "arrival11:00amTo1:00pm",   # 8
                    "arrival12:00pmTo3:00pm",   # 9
                    "arrival3:00pmTo6:00pm",    # 10
                    "arrival6:30pmTo9:00pm",    # 11
                    "arrivalAfter6:00pm",       # 12
                    "arrivalAfter9:00pm",       # 13
                    "departureBefore9:00am",    # 14
                    "departure9:00amTo12pm",    # 15
                    "departure12:00pmTo3:00pm", # 16
                    "departure1:00pmTo3:00pm",  # 17
                    "departure3:30pmTo6:30pm",  # 18
                    "departure6:30pmTo9:00pm",  # 19
                    "departureAfter6:30pm",     # 20
                    "departureAfter9:00pm",     # 21
                    "isSchoolTour",             # 22
                    "isUniversityTour",         # 23
                    "isWorkTour",               # 24
                    "isSchoolOrUniTour",        # 25
                    "isNonMandTour",            # 26
                    "isSaSchoolEscortTour",     # 27
                    "transitMode",              # 28
                    "sharedRideMode",           # 29
                    "walkOrBikeMode",           # 30
                    "escortStopPeriodHalfTour1",
                    "escortStopPeriodHalfTour2",
                 ],
    },
    {"type" : "memory",
     "dataType" : "int",
     "name" : "Stop",
     "columns" : [  "stopPurpose",                          # 0 for segmentation
                    "fullyJointEscortStop",                 # 1
                    "workTourMealStop",                     # 2 for tourCoeffs
                    "workTourShopStop",                     # 3
                    "workTourPersonalBusinessStop",         # 4
                    "workTourSocialRecreation",             # 5
					"nonManTourMealStop",					# 6
					"nonManTourShopStop",					# 7
					"nonManTourPersonalBusinessStop", 		# 8
					"nonManTourSocialRecreation"			# 9
                ],
     },
    {"type" : "memory",
     "dataType" : "double",
     "name" : "StopLevelOfService",
     "columns" : [  "distance",                # 0
                    "detourDistance",   # 1
                  ],
     },

    {"type" : "memory",
     "dataType" : "double",
     "name" : "AlternativeSpecificValues",
     "columns" : [  "stopDuration",                         # 0
                    "distIfStopDuration0",                  # 1
                    "distIfStopDuration1",                  # 2
                    "distIfStopDuration0or1nonAutoMode",    # 3
                    "detourDistStopDuration2+",             # 4
                    "detourDistStopDuration4+",             # 5
                    "detourDistStopDuration8+",             # 6
                    "periodPartiallyUsed",                  # 7
                    "numAvailablePeriodsIfOtherTour",       # 8
                    "numAvailablePeriodsIf1+MoreStops",     # 9
                    "numAvailablePeriodsIf2moreStops",      # 10
                    "noSchoolEscorted",                     # 11
                 ],
     },

]