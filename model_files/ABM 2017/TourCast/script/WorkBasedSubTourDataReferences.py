####################################################################
# WorkBasedSubTourDataReferences.py
#import this using
# from WorkBasedSubTourDataReferences import *
####################################################################

from Globals import * 

# All data references for the DAP subcomponents are memory references (except for the constants ref)
# data reference rows are fed to the subcomponents by the main DAP component
# in general each subcomponent uses only a subset of the supplied data rows
dataReferences = [

    {"type" : "constants",
     "name" : "Constants",
     "columns" : ["One"],
     "values" : [1]
    },

    {"type" : "dbffile",
     "name" : "Data",
     "filename" : cube___WORK_BASED_TOUR_PRE_PROCESSED_DATA___, # file paths MUST BE RAW strings (open quote preceded by 'r')
     "columns" : [
                   "persId",         # 0    PassThrough
                   "persTourId",     # 1    PassThrough
                   "hhId",           # 2    PassThrough
                   "homeZoneId",     # 3    PassThrough
                   "tourPurp",       # 4    
                   "destZoneId",     # 5    PassThrough (As OrigZoneId)
                   "hhinc5s",        # 6
                   "PTMode",         # 7    PassThrough
                   "ptype",          # 8    
                   "male",           # 9
                   "2MndTours",      # 10
                   "numWKTours",     # 11
                   "numScEscTrs",    # 12
                   "logdistHmWk",    # 13
                   "rehwyacc10",     # 14
                   "nehwyacc10",     # 15
                   "durationPT",     # 16
                   "30minLT12",      # 17
                   "30minGT12",      # 18
                   "tourArr",        # 19   PassThrough
                   "tourDep",        # 20   PassThrough
                  ],
     "deferredLoad" : True 
    },       
    
    {"type" : "dbffile",
     "name" : "OutputTours",
     "isOutput" : "true",
     "filename" : cube___WORK_BASED_SUBTOURS___, # file paths MUST BE RAW strings (open quote preceded by 'r')
     "parameters" : [
                    ["personId",    "personId"],   
                    ["persTourId",  "persTourId"],   
                    ["tourPurp",    "tourPurp"], 
                    ["hhId",        "hhId"],
                    ["homeZoneId",  "homeZoneId"],
                    ["origZoneId",  "origZoneId"],
                    ["parentMode",  "parentMode"],
                    ["parTourId",   "parTourId"],
                    ["ptArrive",    "ptArrive"],
                    ["ptDepart",    "ptDepart"],
                    
                    ]
     }
]
