####################################################################
# WorkBasedStopGeneration.py
# should be renamed StopGeneration_WorkBased.py
# Config for MultiModel component for work based stop generation models
####################################################################
from Globals import * 


modelComponentName="StopGenerationWorkBased"
instantiationType="MultiModelComponent"

subModels={
           "WorkBased:HalfTour1" : r"StopGenerationSubmodel_WorkBasedHalfTour1.py",
           "WorkBased:HalfTour2" : r"StopGenerationSubmodel_WorkBasedHalfTour2.py",
           }

parameters = {
              "amPeakStart" : 6.5,
              "amPeakEnd" : 8.5,
              "pmPeakStart" : 15.5,
              "pmPeakEnd" : 18.5,
              # Not actually needed because gen time is not used, but here to be consistent with other models
              "OutOfVehicleWeights" : [2.5],
             }

dataReferences = [
    # this data will be fed to an instance of HouseholdDataUtility, along with the persons data ref following
    {"type" : "dbffile",
     "name" : "HouseholdBaseData",
     "filename" : cube___HOUSEHOLDS_FILE___, 
     # Column names are uppercase in this file
     "columns" : ["HHID", 
                  "HHSIZE",
                  "HHINC5S", 
                  "HHZON", 
                  "HCHILD1", 
                  "HCHILD2",
                  "HCHILD3", 
                  "HSTUD", 
                  "HFTW", 
                  "HPTW", 
                  "HNWA", 
                  "HSEN", 
				  "HCHILDREN"
                  ], 
     "deferredLoad" : True 
    },

    {"type" : "dbffile",
     "name" : "PersonBaseData",
     "filename" : cube___DAILY_ACTIVITY_PATTERNS___, # Looks like a good place to start
     "columns" : ["personId",   # 0
                  "hhId",       # 1
                  "homeZoneId", # 2
                  "personType", # 3
                  "hhinc5s",    # 4 
                  "DAPId",      # 5 
                  "tourCount",  # 6
                  "age",        # 7
                  "female",		# 8
                  ],
     "deferredLoad" : True,
    },

    {"type" : "dbffile",
     "name" : "NCarsFromAA",     
     "filename" : cube___NUM_CARS_PER_HOUSEHOLD___,# 
     "columns" : ["hhid", "hhzon", "nCars", "noCarsInHh", "wkGtCarGt0"],
     "deferredLoad" : True 

    },    

    # The first seven columns need to be specified in the same order at the beginning of the columns list:
    # "personId", "hhId", "persTourId", "tourPurp", "arrival", "departure", "homeZoneId"
    {"type" : "dbffile",
     "name" : "WorkBasedTours",
     "filename" : cube___WORK_BASED_TOUR_TIME_OF_DAY_CHOICE___,
     "columns" : ["personId", "hhId", "persTourId", "tourPurp", "arrival", "departure", "homeZoneId", "destZoneId",
                  "origZoneId", "parentMode", "parArrive", "parDepart"],
     "deferredLoad" : True                   
    },

    {"type" : "dbffile",
     "name" : "Zones",
     "filename" : cube___ZONES_FILE___, 
     "columns" : ["zoneId",   # 0
                  "area",     # 1
                  "term_time",# 2
                  "mix_dens", # 3
                  "tot_emp",  # 4
                  "households"# 5
                  ]
    },

    {"type" : "dbffile",
     "isOutput": "true",
     "name" : "OutputStops",     
     "filename" : cube___WORK_BASED_STOPS___, # file paths MUST BE RAW strings (preceded by 'r')
     "parameters" : [
                       [ "hh zone", "hhzon"],
                       [ "hh inc 5 segments", "hhinc5s"],
                       [ "hhid", "hhid"],
                       [ "Person id", "personId"],         
                       [ "Person Type", "personType"],
                       [ "tour", "tourId"],
                       [ "tour purpose", "tourPurpose"],
                       [ "@stop", "stopId" ],
                       [ "@half tour number", "halfTour"],
                       [ "@stop purpose", "purpose"],
                       [ "@destination zone", "destZone"],
                       [ "@stop time", "time" ],
                       [ "numEscort", "numEscort" ],
                       [ "arrLt900", "arrLt900" ],
                       [ "periods available HT1", "availPrHt1" ],
                       [ "choiceId", "choiceId" ],
                    ]
     }
# not needed for work-based tours- we would just be spitting out the WorkBasedTours input
#    ,
#   {"type" : "dbffile",
#     "isOutput": "true",
#     "name" : "OutputTours",     
#     "filename" : @___WORK_BASED_TOURS___@, # file paths MUST BE RAW strings (preceded by 'r')
#     "parameters" : [
#                       [ "Person id", "personId"],
#                       [ "household id", "hhId"],
#                       [ "tour", "persTourId"],
#                       [ "tour purpose", "tourPurp"], 
#                       [ "arrival", "arrival"],
#                       [ "departure", "departure"],
#                       [ "homeZone", "homeZoneId"],
#                       [ "destinationZone", "destZoneId"], 
#                       [ "origin zone", "origZoneId"],
#                       [ "parent tour mode", "parentMode"],
#                       [ "parent arrive time", "parArrive"],
#                       [ "parent depart time", "parDepart"],
#                    ],
#     },
]

from MatrixRef4Hwy2TransWk import matrixReferences