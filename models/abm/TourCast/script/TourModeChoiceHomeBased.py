####################################################################
# TourModeChoiceHomeBased.py
# Config for MultiModel component for tour mode choice models
# NOTE: work-based model imports this file 
####################################################################
from Globals import * 


modelComponentName="TourModeChoice"
instantiationType="MultiModelComponent"

subModels={ # the key here is OutingPurpose; if a ';' in the dictionary key, handles both of these separately;
           # if joined by |, only handles the combination of these
           "School;University" : r"TourModeChoiceLogsum_SchoolLocation.py",
           "FullyJointNMT" :     r"TourModeChoiceLogsum_FullyJoint.py",
           "IndNonMnd" :         r"TourModeChoiceLogsum_IndividualNonMandatory.py",
           "IndNonMnd|Escort;SchoolEscort" : r"TourModeChoiceLogsum_IndividualNonMandatory_Escort.py",
           "Work" :              r"TourModeChoiceLogsum_Work.py",
           #"WorkBased" : r"WorkBasedTourModeChoiceLogsum.py"
           }


# NOTE: keep the same order for data references so that TourModeChoiceWorkBased can substitute filenames by index into the dataReferences array
dataReferences = [
    # this data will be fed to an instance of HouseholdDataUtility, along with the persons data ref following
    {"type" : "dbffile",
     "name" : "HouseholdBaseData",
     "filename" : cube___HOUSEHOLDS_FILE___, 
     # Column names are uppercase in this file
     "columns" : ["HHID",     # 0
                  "HHZON",    # 1
                  "HHINC5S",  # 2
                  "HHSIZE",   # 3
                  "HSTUD",    # 4
                  "hh1Person",# 5
                  "hchildren",# 6
                  "nKidsGT2", # 7
                  "hWorkers", # 8
				  "hChild1",  # 9
				  "hChild2",  # 9
                  ], 
     "deferredLoad" : True 
    },

    # this data will be fed to an instance of HouseholdDataUtility, along with the persons data ref following
    {"type" : "dbffile",
     "name" : "HouseholdModeledData",
     "filename" : cube___NUM_CARS_PER_HOUSEHOLD___, 
     # Column names are uppercase in this file
     "columns" : ["HHID",      # 0
                  "HHZON",     # 1
                  "nCars",     # 2
                  "noCarsInHh",# 3
                  ], 
     "deferredLoad" : True 
    },
	
    {"type" : "dbffile",
     "name" : "HouseholdPassData", 
     "filename" : cube___PASS_MODEL___, # file paths MUST BE RAW strings (open quote preceded by 'r')
     "columns" : ["hhid", "hhzon", "mnPass", "transPass"],
    },	

    {"type" : "dbffile",
     "name" : "PersonBaseData",
     "filename" : cube___PERSONS_FILE___, # Looks like a good place to start
     "columns" : ["personId", # 0
                  "hhId",     # 1
                  "hhzon",    # 2
                  "ptypeDAP",   # 3
                  "age",      # 4
                  "gender",   # 5
#                  "hhinc5s", # 

                  ],
     "deferredLoad" : True,
    },

    {"type" : "dbffile",
     "name" : "PersonModeledData",
     "filename" : cube___DAILY_ACTIVITY_PATTERNS___, # Looks like a good place to start
     "columns" : ["personId",   # 
                  "hhId",       # 
                  "homeZoneId",      # 
                  "DAPId",      # 


                  ],
     "deferredLoad" : True,
    },


    # maybe separate out individual tours from multiperson tours
    {"type" : "dbffile",
     "name" : "Tours",
     "filename" : cube___STOP_GENERATION_TOURS_HOME_BASED___, # Looks like a good place to start
     "columns" : [
                  #school:
                   "personId",
                   "persTourId",      
                   "hhId",             
                   "homeZoneId", # for chunking
                   "destZoneId",
                   "tourPurp",
                   "arrival", 
                   "departure",
                   "noStopTour",
                    # school tour stop-related info, not sure if I need this
                    "esPrsOutId",
                    #   [ "escort tour id outbound", "esTrOutId"],
                    "esPrsInId",
                    #   [ "escort tour id inbound", "esTrInId"],
                    "nEscOut", # for school escort standalone tour, number of children escorted on outbound trip
                    "nEscIn"  # for school escort standalone tour, number of children escorted on return trip
                  ],
     "deferredLoad" : True 
    },


    # from stop generation model
    {"type" : "dbffile",
     "name" : "Stops",     
     "filename" : cube___STOP_GENERATION_STOPS_HOME_BASED___, # file paths MUST BE RAW strings (preceded by 'r')
     "columns" : [
                "hhzon",
                "hhinc5s",
                "hhid",
                "personId",
                "tourId",
                "stopId" ,
                "halfTour",
                "purpose",
                "destZone",
                "time" 
                  ],
     "deferredLoad" : True 
     },

    # this covers tour data expected by some subclasses in their tour data; 
    # the main class will map this data to the tour data for the subclass
    {"type" : "memory",
     "dataType" : "int",
     "name" : "DerivedTour",
     "columns" : [
                  "nAdults",   # for fully joint tours
                  "nChildren", # for fully joint tours
                  "xFtwInTour",# for fully joint tours
                  "nTours",    # for work tour calc
                  "nWorkTours",# for work tour calc
                  ]
    },


     # these will be filled from Stops input and fed to submodels
    {"type" : "memory",
     "dataType" : "int",
     "name" : "HalfTour1",
     "columns" : [
                  "nMeal",
                  "nPerBus",
                  "nSocial",
                  "nEscort",
                  "nSchEsc",
                  "nWork",
                  "nShop",
                  "nSchool",
                  "nUniver"
                  ]
    },

     # these will be filled from Stops input and fed to submodels
    {"type" : "memory",
     "dataType" : "int",
     "name" : "HalfTour2",
     "columns" : [
                  "nMeal",
                  "nPerBus",
                  "nSocial",
                  "nEscort",
                  "nSchEsc",
                  "nWork",
                  "nShop",
                  "nSchool",
                  "nUniver"
                  ]
    },
    

# in case we need this:
    # equivalent of link table from personId to tours;
    # if we had an Id source to generate tour ids we could eliminate the now-confusing compound tour id which
    # for fully joint tours consists of the id of one person on the tour plus a persTourId in the range of FirstAssignedTourId to FirstAssignedTourId + 1
    # (where FirstAssignedTourId is an input parameter at the top of this configuration file)
    {"type" : "dbffile",
     "name" : "FullyJointPersonTourLinkTable",     
     "filename" : cube___FULLY_JOINT_TOUR_PERSON_LINK_TABLE___, # file paths MUST BE RAW strings (preceded by 'r')
     "columns" : [
                  "persTourId",
                  "tourId",   
                  "personId", 
                  "homeZoneId",
                  "ptypeDAP", 
                  "female", 
                  ],
     "deferredLoad" : True 
    }, 


    {"type" : "dbffile",
     "name" : "Zones",
     "filename" : cube___ZONES_FILE___, 
     "columns" : ["zoneId", "term_time", "park_cost", "mix_dens"]
    },

    {"type" : "dbffile",
     "isOutput": "true",
     "name" : "OutputModeChoice",     
     "filename" : cube___HOME_BASED_TOUR_MODE_CHOICE___, # file paths MUST BE RAW strings (preceded by 'r')
     "parameters" : [
                       [ "personId", "personId"],  # part 1 of tour pk, for individual tours would be same as person id
                       [ "persTourId", "persTourId"],
                       ["homeZoneId", "homeZoneId"], # for chunking
                       [ "@tourMode", "tourMode"] # numerical value of TourMode enum 
                    ]
     },

    {"type" : "dbffile",
     "isOutput": "true",
     "name" : "OutputModeChoiceForStats",     
     "filename" : cube___HOME_BASED_TOUR_MODE_CHOICE_SUMMARY___, # file paths MUST BE RAW strings (preceded by 'r')
     "parameters" : [
                       [ "ptypeDAP", "ptypeDAP"],  # part 1 of tour pk, for individual tours would be same as person id
                       [ "tourPurp", "tourPurp"],
                       [ "@tourMode", "tourMode"], # numerical value of TourMode enum 
                       [ "arrival", "arrival"],
                       [ "departure", "departure"],
                       ["origin zone", "origZoneId"],
                       ["destination zone", "destZoneId"]
                    ]
     },

]


from MatrixRef4Hwy4Trans import matrixReferences;