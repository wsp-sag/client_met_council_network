####################################################################                                                                                                                                                                                           
# FullyJointTourTimeOfDay.py
# Configuration script for Tour Time Of Day processing of 
# the first tours generated by the DAP model
# these are a mixture of school, university and work tours
####################################################################                                                                                                                                                                                           

from Globals import *

instantiationType="MultiModelComponent" 

modelComponentName="TourTimeOfDayHomeBased"

subModels = {
             "FullyJoint": r"FullyJointTourTimeOfDaySubmodel.py"
            }
			

parameters = {
				"OperatingCostCentsPerMile":autoOpCost			  
             }			

dataReferences = [

    {"type" : "dbffile",
     "name" : "Tours",
     "filename" : cube___FULLY_JOINT_TOUR_DESTINATION_CHOICE___,
     "columns" : [
                    "person1Id", 
                    "tourId",   
                    "tourPurp", 
                    "hhId",
                    "homeZoneId",
                    "hhinc5s",
                    "destZoneId"
                  ],
     "deferredLoad" : True 
    },


# this input would be present for all but dap first tours; filename depends on prior steps
   {"type" : "dbffile",
     "name" : "InputPersonDaySchedules",     
     "filename" : cube___FULLY_JOINT_TOUR_PRE_PROCESSED_DATA___, # file paths MUST BE RAW strings (preceded by 'r')
     # parameters could be generally of form source data reference : field
     "columns" : [
                    "personId",
                    "homeZoneId",
                    "slotsArriv",
                    "slotsDeprt",
                    "slotsUsed"
                  ],
     "deferredLoad" : True 
    },

    {"type" : "dbffile",
     "name" : "Zones",
     "filename" : cube___ZONES_FILE___, 
     "columns" : ["zoneId", "term_time", "park_cost"]
    },


    # note that for TOD model we are taking the input tours and appending
    # the arrival and departure info, so are NOT ACTUALLY USING THE
    # COLUMN NAMES BELOW;  this is either a little bogus or desirable (or both)
    
   {"type" : "dbffile",
     "isOutput": "true",
     "name" : "OutputTours",     
     "filename" : cube___FULLY_JOINT_TOUR_TIME_OF_DAY___, # file paths MUST BE RAW strings (preceded by 'r')
     # parameters could be generally of form source data reference : field
     "parameters" : [
                       [ "Id of first person in tour", "person1Id"],
                       [ "tourId", "tourId"],
                       [ "tour", "tourPurp"],
                       [ "hhId", "hhId"],
                       [ "homeZoneId", "homeZoneId"], 
                       [ "hhinc5s", "hhinc5s"], 
                       [ "destZoneId", "destZoneId"], 
                       [ "@arrival", "arrival"],
                       [ "@departure", "departure"],
                       [ "@duration", "duration"]
                       # using '@' in data source name indicates this field is generated by the component, so requires some coordination with C# code
                    ]
    },
    
    # OutputPersonDaySchedules (different file name for different TOD stages) will be full set of persons with entire schedule, up to date after each run
   {"type" : "dbffile",
     "isOutput": "true",
     "name" : "OutputPersonDaySchedules",     
     "filename" : cube___FULLY_JOINT_TOUR_PERSON_SCHEDULES___, # file paths MUST BE RAW strings (preceded by 'r')
     # parameters could be generally of form source data reference : field
     "parameters" : [
                       [ "Person id", "personId"],
                       [ "homeZoneId", "homeZoneId"],  # only for chunking
                       [ "@slotsArriv", "slotsArriv"],
                       [ "@slotsDeprt", "slotsDeprt"],
                       [ "@slotsUsed", "slotsUsed"]
                       # using '@' in data source name indicates this field is generated by the component, so requires some coordination with C# code
                    ]
    },
    

]

from MatrixRef4Hwy import matrixReferences
