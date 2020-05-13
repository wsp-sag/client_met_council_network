####################################################################
# StopGeneration.py
# Config for MultiModel component for stop generation models
####################################################################

from Globals import *

modelComponentName="StopGeneration"
instantiationType="MultiModelComponent"

subModels={
           "Work:HalfTour1" : 			r"StopGenerationSubmodel_WorkHalfTour1.py",
           "Work:HalfTour2" : 			r"StopGenerationSubmodel_WorkHalfTour2.py",
           "School:HalfTour1" : 		r"StopGenerationSubmodel_SchoolHalfTour1.py",
           "School:HalfTour2" : 		r"StopGenerationSubmodel_SchoolHalfTour2.py",
           "University:HalfTour1" : 	r"StopGenerationSubmodel_UniversityHalfTour1.py",
           "University:HalfTour2" : 	r"StopGenerationSubmodel_UniversityHalfTour2.py",
           "IndNonMnd:HalfTour1" : 		r"StopGenerationSubmodel_IndividualNonMandatoryHalfTour1.py",
           "IndNonMnd:HalfTour2" : 		r"StopGenerationSubmodel_IndividualNonMandatoryHalfTour2.py",
           "FullyJointNMT:HalfTour1" :  r"StopGenerationSubmodel_FullyJointHalfTour1.py",
           "FullyJointNMT:HalfTour2" :  r"StopGenerationSubmodel_FullyJointHalfTour2.py",
           "Escort" : 					r"StopGenerationSubmodel_Escort.py",
           }

parameters = {
              "amPeakStart" : 6.5,
              "amPeakEnd" : 8.5,
              "pmPeakStart" : 15.5,
              "pmPeakEnd" : 18.5,
              # Match order of submodels: work, school, university, INM, FJ
              "OutOfVehicleWeights" : [2.5, 2.0, 2.0, 2.5, 2.0],
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

    # For all three tour input data references, the first seven need to be specified in the same order at the beginning of the columns list:
    # "personId", "hhId", "persTourId", "tourPurp", "arrival", "departure", "homeZoneId"
    {"type" : "dbffile",
     "name" : "MandatoryAndSchoolEscortTours",
     "filename" : cube___SCHOOL_ESCORT_TOURS___,
     "columns" : ["personId", "hhId", "persTourId", "tourPurp", "arrival", "departure", "homeZoneId", "destZoneId",
                  "noStopTour", "esPrsOutId", "esTrOutId", "esPrsInId", "esTrInId", "nEscOut", "nEscIn"],
     "deferredLoad" : True 

    },
    {"type" : "dbffile",
     "name" : "FullyJointTours",     
     "filename" : cube___FULLY_JOINT_TOUR_TIME_OF_DAY___, 
     "columns" : [
                  "person1Id", # part 1 of pk: using first person in tour
                  "hhId",
                  "tourId",   # part 2 of pk: tourId starting from 5 for joint tours 
                  "tourPurp", 
                  "arrival",
                  "departure",         
                  "homeZoneId",
                  "destZoneId",
                 ],
     "deferredLoad" : True 

    }, 

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
     "name" : "IndividualNonMandatoryTours",     
     "filename" : cube___INDIVIDUAL_NON_MANDATORY_TOUR_TIME_OF_DAY_CHOICE___, 
     "columns" : [
                     "personId",
                     "hhId",
                     "tourId",  
                     "tourPurpose",
                     "arrival",
                     "departure",
                     "homeZoneId",
                     "destZoneId",
                  ],
     "deferredLoad" : True 
    },

    {"type" : "dbffile",
     "name" : "IndividualNonMandatoryEscortTours",     
     "filename" : cube___INDIVIDUAL_NON_MANDATORY_ESCORT_TOUR_TIME_OF_DAY_CHOICE___, 
     "columns" : [
                     "personId",
                     "hhId",
                     "tourId",  
                     "tourPurpose",
                     "arrival",
                     "departure",
                     "homeZoneId",
                     "destZoneId",
                  ],
     "deferredLoad" : True 
    },

    {"type" : "dbffile",
     "name" : "Zones",
     "filename" : cube___ZONES_FILE___, 
     "columns" : ["zoneId", "area", "term_time", "mix_dens", "tot_emp", "households"]
    },

    {"type" : "dbffile",
     "isOutput": "true",
     "name" : "OutputStops",     
     "filename" : cube___STOP_GENERATION_STOPS_HOME_BASED___, # file paths MUST BE RAW strings (preceded by 'r')
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
     },
   {"type" : "dbffile",
     "isOutput": "true",
     "name" : "OutputTours",     
     "filename" : cube___STOP_GENERATION_TOURS_HOME_BASED___, # file paths MUST BE RAW strings (preceded by 'r')
     "parameters" : [
                       [ "Person id", "personId"],
                       [ "household id", "hhId"],
                       [ "tour", "persTourId"],
                       [ "tour purpose", "tourPurp"], 
                       [ "arrival", "arrival"],
                       [ "departure", "departure"],
                       [ "homeZone", "homeZoneId"],
                       [ "destinationZone", "destZoneId"], 
                       [ "nonstop tour", "noStopTour"],
                       [ "escort person id outbound", "esPrsOutId"],
                       [ "escort tour id outbound", "esTrOutId"],
                       [ "escort person id inbound", "esPrsInId"],
                       [ "escort tour id inbound", "esTrInId"],
                       [ "children escorted on outbound first halftour", "nEscOut"],
                       [ "children escorted on second halftour", "nEscIn"]
                    ],
     },
]

from MatrixRef4Hwy2TransWk import matrixReferences