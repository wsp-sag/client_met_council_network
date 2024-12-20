####################################################################                                                                                                                                                                                           
# TourTimeOfDayIndNonMand.py
# DON'T USE THIS FILE DIRECTLY: 
# IT IS IMPORTED by TourTimeOfDayIndNonMandEscort.py AND TourTimeOfDayIndNonMandNonEscort.py
# IT HAS PLACEHOLDERS FOR THE INPUT AND OUTPUT FILES
# Configuration script for Tour Time Of Day processing
# this specifies the common input files for the IndNonMand tour time of day, 
# which is split into 2 parts, non-escort and escort handled separately
# and has placeholder variables for input and output file names
####################################################################                                                                                                                                                                                           

from Globals import * 

instantiationType="MultiModelComponent" 

modelComponentName="TourTimeOfDayHomeBased"

subModels = {
             "IndNonMand": r"TourTimeOfDaySubmodel_IndividualNonMandatory.py"
            }

dataReferences = [

    {"type" : "dbffile",
     "name" : "Tours",
     "filename" : "placeholder(set by importing file)",
     "columns" : [
                    "personId", 
                    "tourId",   
					"hhId",
                    "tourPurpose", 
                    "nInmTours",
                    "homeZoneId",
                    "destZoneId",
					"adult1Kids",
					"nTours"                    
                  ],
     "deferredLoad": True
    },

# this input would be present for all but dap first tours; filename depends on prior steps
   {"type" : "dbffile",
     "name" : "InputPersonDaySchedules",     
     "filename" : "placeholder(set by importing file)",
     # parameters could be generally of form source data reference : field
     "columns" : [
                    "personId",
                    "homeZoneId",
                    "slotsArriv",
                    "slotsDeprt",
                    "slotsUsed"
                 ],
     "deferredLoad": True
    },

    {"type" : "dbffile",
     "name" : "Zones",
     "filename" : cube___ZONES_FILE___, 
     "columns" : ["zoneId",   # 0
                  "term_time",# 1
                  "park_cost" # 2
                  ]
    },


    # note that for TOD model we are taking the input tours and appending
    # the arrival and departure info, so are NOT ACTUALLY USING THE
    # COLUMN NAMES BELOW;  this is either a little bogus or desirable (or both)
    
   {"type" : "dbffile",
     "isOutput": "true",
     "name" : "OutputTours",     
     "filename" : "placeholder(set by importing file)",
     # parameters could be generally of form source data reference : field
     "parameters" : [
                       [ "personId", "personId"],
                       [ "tourId", "tourId"],
                       [ "hhId", "hhId"],
                       [ "tour", "tourPurpose"],
                       [ "homeZoneId", "homeZoneId"], 
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
     "filename" : "placeholder(set by importing file)",
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
    

# TODO: this data is not currently being written - would be different for each TOD run - maybe I'll update it later
# the responsibility would have to fall to the submodel to write this data
   {"type" : "dbffile",
     "isOutput": "true",
     "name" : "OutputTODStats",     
     "filename" : cube___INDIVIDUAL_NON_MANDATORY_TOUR_TIME_OF_DAY_SUMMARY___, # file paths MUST BE RAW strings (preceded by 'r')
     # parameters could be generally of form source data reference : field
     "parameters" : [
                       [ "arrival", "arrival"],
                       [ "departure", "departure"],
                       [ "countSch", "countSch"],
                       [ "countUni", "countUni"],
                       [ "countWork", "countWork"],
                    ]
    },

]

from MatrixRef4Hwy import matrixReferences
