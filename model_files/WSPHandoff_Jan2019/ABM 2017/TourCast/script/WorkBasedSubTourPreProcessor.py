####################################################################
# PreWorkBasedSubTourDataReferences.py
# A python script with
#   DataReferences, MatrixReferences
#   list of modelComponents that are submodels
#   I am not adhering to the python convention of 70-odd columns per line
####################################################################

from Globals import * 

instantiationType="DataAssemblyComponent"
#characteristics

# the name of the corresponding class on the C# side:
# this allows for multiple scripts targeting the same component
modelComponentName="PreWorkBasedSubTourDataAssembly"  

# dataReferences is an array
# each array element is a dictionary (set of key:value pairs); each dictionary has 2 required keys:  name and type
# the value corresponding to the "type" key indicates to C# how to instantiate the data reference
# the set of names is fixed for each C#-side model component
# each type constrains the set of keys to supply in the remainder of that dictionary
# e.g. a type of "db" currently (this spec is in flux) requires the connectionString and queryString
# to demonstrate that this structure can be read I've included an Excel data reference type
# and as an experiment in output, I also have a console data reference type so the component can display alternative choices
# until we have a real output spec
dataReferences = [

    {"type" : "dbffile",
     "name" : "PersonsBase",
     "filename" : cube___PERSONS_FILE___, # file paths MUST BE RAW strings (open quote preceded by 'r')
     "columns" : ["personid",   # 0
                  "hhid",       # 1
                  "hhzon",      # 2
                  "hhinc5s",    # 3
                  "ptype",      # 4
                  "female"		# 5
                ],
     "deferredLoad" : True,
     # "sort": ["hhzon", "hhinc5s", "hhid", "ptype2"], sort is done by PreDAP ##TODO: Fix this?
    },

    # dbf output spec; used in tests for inspecting whether results are reasonable
    {"type" : "dbffile",
     "name" : "PersonModeledDataOutput",     
     "filename" : cube___FULLY_JOINT_TOUR_PRE_PROCESSED_DATA___, # file paths MUST BE RAW strings (preceded by 'r')
     # parameters could be generally of form source data reference : field
     "columns" : [
                       "personId",
                       "hhId",
                       "homeZoneId",
                       "DAPId",
                       "slotsUsed",
                       "slotsArriv",
                       "slotsDeprt"
                       # using '@' in data source name indicates this field is generated or updated by the component, so requires some coordination with C# code
                    ],
     "deferredLoad" : True,
    },

    {"type" : "dbffile",
     "name" : "Zones",
     "filename" : cube___ZONES_FILE___, # file paths MUST BE RAW strings (preceded by 'r')
     "columns" : ["zoneId",  # 0
                  "area",    # 1
				  "rehwyacc10", 
				  "nehwyacc10"
                  ] 
    },

    
    {"type" : "dbffile",
     "name" : "DAPFirstTours",     
     "filename" : cube___DAP_TOUR_TIME_OF_DAY_CHOICE_FIRST_TOURS___, # file paths MUST BE RAW strings (preceded by 'r')
     # parameters could be generally of form source data reference : field
     "columns" : [
                       "personId",
                       "hhId",
                       "persTourId",
                       "tourPurp",
                       "homeZoneId",
                       "destZoneId",
                       "arrival",
                       "departure",
                    ],
     "deferredLoad" : True,
    },

    {"type" : "dbffile",
     "name" : "DAPSecondTours",     
     "filename" : cube___DAP_TOUR_TIME_OF_DAY_CHOICE_SECOND_TOURS___, # file paths MUST BE RAW strings (preceded by 'r')
     # parameters could be generally of form source data reference : field
     "columns" : [
                       "personId",
                       "hhId",
                       "persTourId",
                       "tourPurp",
                       "homeZoneId",
                       "destZoneId",
                       "arrival",
                       "departure",
                    ],
     "deferredLoad" : True,
    },

    {"type" : "dbffile",
    "name" : "TourMode",     
    "filename" : cube___HOME_BASED_TOUR_MODE_CHOICE___, # file paths MUST BE RAW strings (preceded by 'r')
    # parameters could be generally of form source data reference : field
    "columns" : [
                      "personId",
                      "homeZoneId",
                      "persTourId",
                      "tourMode",
                   ],
     "deferredLoad" : True,
   },

   {"type" : "dbffile",
    "name" : "Stops",     
    "filename" : cube___STOP_GENERATION_STOPS_HOME_BASED___, # file paths MUST BE RAW strings (preceded by 'r')
    # parameters could be generally of form source data reference : field
    "columns" : [
                      "personId",
                      "tourId",
                      "hhzon",
                      "purpose",
                      "halfTour",
                   ],
     "deferredLoad" : True,
   },

   {"type" : "dbffile",
     "name" : "Distances1",     
     "filename" : cube___WORK_TOUR_DESTINATION_CHOICE_FIRST_TOURS___, # file paths MUST BE RAW strings (preceded by 'r')
     "columns" : [
                       "personId",
                       "homeZoneId",
                       "persTourId",
                       "distH2Work",
                    ],
     "deferredLoad" : True,
    },

    {"type" : "dbffile",
     "name" : "Distances2",     
     "filename" : cube___WORK_TOUR_DESTINATION_CHOICE_SECOND_TOURS___, # file paths MUST BE RAW strings (preceded by 'r')
     "columns" : [
                       "personId",
                       "homeZoneId",
                       "persTourId",
                       "distH2Work",
                    ],
     "deferredLoad" : True,
    },

    {"type" : "dbffile",
     "name" : "FJTours",     
     "filename" : cube___FULLY_JOINT_TOURS___, # file paths MUST BE RAW strings (preceded by 'r')
     # parameters could be generally of form source data reference : field
     "columns" : [
                       "person1Id",
                       "homeZoneId",
                       "TourGenEnum",
                    ],
     "deferredLoad" : True,
    },
    
    {"type" : "dbffile",
     "name" : "inmTours",
     "filename" : cube___INDIVIDUAL_NON_MANDATORY_TOURS___, # file paths MUST BE RAW strings (preceded by 'r')
     # parameters could be generally of form source data reference : field
     "columns" : [
                       "personId",
                       "homeZnId",
                       "TourGenEnum",
                    ],
     "deferredLoad" : True,
    },

    {"type" : "dbffile",
     "name" : "SchoolEscortTours",     
     "filename" : cube___SCHOOL_ESCORT_TOURS___, # file paths MUST BE RAW strings (preceded by 'r')
     # parameters could be generally of form source data reference : field
     "columns" : [
                       "personId",
                       "persTourId",
                       "homeZoneId",
					   "nEscOut",
					   "nEscIn"
                    ],
     "deferredLoad" : True,
    },


    {"type" : "dbffile",
     "name" : "OutputTours",
     "isOutput" : "true",
     "filename" : cube___WORK_BASED_TOUR_PRE_PROCESSED_DATA___, # file paths MUST BE RAW strings (open quote preceded by 'r')
     "parameters" : [
                  ["persId",      "persId"],         # 0
                  ["persTourId",  "persTourId"],     # 1
                  ["hhId",        "hhId"],           # 2
                  ["homeZoneId",  "homeZoneId"],     # 3
                  ["tourPurp",    "tourPurp"],       # 4
                  ["destZoneId",  "destZoneId"],     # 5
                  ["hhinc5s",     "hhinc5s"],        # 6
                  ["PTMode",      "PTMode"],         # 7
                  ["ptype",       "ptype"],          # 8
                  ["male",        "male"],           # 9
                  ["2MndTours",   "2MndTours"],      # 10
                  ["numWKTours",  "numWKTours"],     # 11
                  ["numScEscTrs", "numScEscTrs"],     # 12
                  ["logdistHmWk", "logdistHmWk"],    # 13
                  ["rehwyacc10",  "rehwyacc10"],     # 14
                  ["nehwyacc10",  "nehwyacc10"],     # 15
                  ["durationPT",  "durationPT"],     # 16
                  ["30minLT12",   "30minLT12"],      # 17
                  ["30minGT12",   "30minGT12"],      # 18
                  ["tourArr",     "tourArr"],        # 19 
                  ["tourDep",     "tourDep"],        # 20
                 ]                                     
    }                                                  
                                                       
]
