####################################################################
# MandatoryTourTimeOfDayChoiceModelPreProcessor.py
# A python script with DataReferences only
# The preprocessor assembles data as needed from multiple upstream components (and/or synthesized population/household data).
# This reduces code maintenance arising from 'conveyor-belt' dependencies between adjacent components,
# i.e. dependencies from merely propagating data through to a downstream component.
####################################################################

from Globals import *

instantiationType="DataAssemblyComponent"
#characteristics

# the name of the corresponding class on the C# side:
# this allows for multiple scripts targeting the same component
modelComponentName="PreTODDataAssembly"  


dataReferences = [

    {"type" : "dbffile",
     "name" : "FirstTours",
     "filename" : cube___DAILY_ACTIVITY_PATTERNS_FIRST_TOURS___, # file paths MUST BE RAW strings (open quote preceded by 'r')
     "columns" : [
                    "personId",    
                    "hhId",
                    "persTourId", 
                    "tourPurp",   
                    "personType", 
                    "hhinc5s",    
                    "cType1",     
                    "cType2",     
                    "cType3",     
                    "cType4",     
                    "cType5",     
                    "age",        
                    "male",       
                    "destZoneId", 
                    "workZoneId", 
                    "wkGtCarGt0", 
                    "homeZoneId", 
                    "noStopTour", 
                    "dapId",      
                    "tourCount",  
                    "hhC1tour",   
                    "hhC2tour",   
                    "hhC3tour",   
                    "hhC4tour",   
                    "hhC5tour",   
                    "hhChildSAH", 
                    "ctype",        
                    "nCars",        
                    "noCarsInHh",   
                    "minNTours",
                    "minNStops",
					"adult1kids",
					"hChild2",
					"hChild3"
                  ],
        "deferredLoad" : True
          # "sort": ["hhzon", "hhinc5s", "hhid", "ptype2"] this is the sort as originally from PreDAPDataAssembly, and thus from output of DAP

    },
     
    {"type" : "dbffile",
     "name" : "SecondTours",
     "filename" : cube___DAILY_ACTIVITY_PATTERNS_SECOND_TOURS___, # file paths MUST BE RAW strings (open quote preceded by 'r')
     "columns" : [
                    "personId",  
                    "hhId",
                    "persTourId",  
                    "tourPurp",    
                    "personType",
                    "hhinc5s",
                    "cType1",
                    "cType2",
                    "cType3",
                    "cType4",
                    "cType5",
                    "age",
                    "male",
                    "destZoneId",
                    "workZoneId",
                    "wkGtCarGt0",
                    "homeZoneId",
                    "noStopTour",
                    "dapId",
                    "tourCount",
                    "hhC1tour",
                    "hhC2tour",
                    "hhC3tour",
                    "hhC4tour",
                    "hhC5tour",
                    "hhChildSAH",
                    "ctype",        
                    "nCars",        
                    "noCarsInHh",   
                    "minNTours",
                    "minNStops",
					"adult1kids",
					"hChild2",
					"hChild3"
                  ],
        "deferredLoad" : True
     },
     
     # NOTE: for each TourDestination model, we need to have 2 inputs here, one for first tours and one for second tours
     # there's a naming convention, the name must end in 'FirstTourDestinations' or 'SecondTourDestinations'
     # the column sets must also be the same and in the same order (at least listed here in the same order)
    {"type" : "dbffile",
     "name" : "UniversityFirstTourDestinations",
     "filename" : cube___UNIVERSITY_TOUR_DESTINATION_CHOICE_FIRST_TOURS___, # file paths MUST BE RAW strings (open quote preceded by 'r')
     "columns" : [
                    "personId",    # part of tour primary key
                    "persTourId",  # part of tour primary key
                    "destZoneId",  # data to integrate with tour data
                    "homeZoneId"   # for chunking
                  ],
        "deferredLoad" : True
          # "sort": ["hhzon", "hhinc5s", "hhid", "ptype2"] this is the sort as originally from PreDAPDataAssembly, and thus from output of DAP

    },

    {"type" : "dbffile",
     "name" : "UniversitySecondTourDestinations",
     "filename" : cube___UNIVERSITY_TOUR_DESTINATION_CHOICE_SECOND_TOURS___, # file paths MUST BE RAW strings (open quote preceded by 'r')
     "columns" : [
                    "personId",    # part of tour primary key
                    "persTourId",  # part of tour primary key
                    "destZoneId",  # data to integrate with tour data
                    "homeZoneId"   # for chunking
                  ],
        "deferredLoad" : True
          # "sort": ["hhzon", "hhinc5s", "hhid", "ptype2"] this is the sort as originally from PreDAPDataAssembly, and thus from output of DAP

    },

     # NOTE: for each TourDestination model, we need to have 2 inputs here, one for first tours and one for second tours
     # there's a naming convention, the name must end in 'FirstTourDestinations' or 'SecondTourDestinations'
     # the column sets must also be the same and in the same order (at least listed here in the same order)
    {"type" : "dbffile",
     "name" : "WorkFirstTourDestinations",
     "filename" : cube___WORK_TOUR_DESTINATION_CHOICE_FIRST_TOURS___, # file paths MUST BE RAW strings (open quote preceded by 'r')
     "columns" : [
                    "personId",    # part of tour primary key
                    "persTourId",  # part of tour primary key
                    "destZoneId",  # data to integrate with tour data
                    "homeZoneId",  # for chunking
                    "distH2Work"   # for downstream work-based subtour
                  ],
        "deferredLoad" : True
          # "sort": ["hhzon", "hhinc5s", "hhid", "ptype2"] this is the sort as originally from PreDAPDataAssembly, and thus from output of DAP

    },

    {"type" : "dbffile",
     "name" : "WorkSecondTourDestinations",
     "filename" : cube___WORK_TOUR_DESTINATION_CHOICE_SECOND_TOURS___, # file paths MUST BE RAW strings (open quote preceded by 'r')
     "columns" : [
                    "personId",    # part of tour primary key
                    "persTourId",  # part of tour primary key
                    "destZoneId",  # data to integrate with tour data
                    "homeZoneId",  # for chunking
                    "distH2Work"   # for downstream work-based subtour
                  ],
        "deferredLoad" : True
          # "sort": ["hhzon", "hhinc5s", "hhid", "ptype2"] this is the sort as originally from PreDAPDataAssembly, and thus from output of DAP

    },

    # ------------------------  outputs ----------------------------------------------

    {"type" : "dbffile",
     "isOutput": "true",
     "name" : "OutputFirstTours",     
     "filename" : cube___FIRST_MANDATORY_TOUR_TIME_OF_DAY___, # file paths MUST BE RAW strings (preceded by 'r')
     # parameters could be generally of form source data reference : field
     "parameters" : [
                 ["Persons", "personId"],
                 ["hhId","hhId"],
                 ["PersonTourId", "persTourid"],
                 ["tourPurp", "tourPurp"], 
                 ["personType","personType"],
                 ["cType1","cType1"],
                 ["cType2", "cType2"],
                 ["cType3", "cType3"],
                 ["cType4", "cType4"],
                 ["cType5", "cType5"],
                 ["age", "age"],
                 ["male", "male"],
                 ["destZoneId", "destZoneId"], 
                 ["workZoneId", "workZoneId"],
                 ["hhinc5s", "hhinc5s"],
                 ["wkGtCarGt0", "wkGtCarGt0"],
                 ["homeZone", "homeZoneId"],
                 ["noStopTour", "noStopTour"],
                 ["dapId",  "dapId"],
                 ["tourCount", "tourCount"],
                 ["hhC1tour", "hhC1tour"],
                 ["hhC2tour", "hhC2tour"],
                 ["hhC3tour", "hhC3tour"],
                 ["hhC4tour", "hhC4tour"],
                 ["hhC5tour", "hhC5tour"],
                 ["hhChildSAH", "hhChildSAH"],
                 ["ctype",  "ctype"],  
                 ["nCars", "nCars"], 
                 ["noCarsInHh", "noCarsInHh"],
                 ["minNTours", "minNTours"],  
                 ["minNStops", "minNStops"],
				 ["adult1kids", "adult1kids"],
				 ["hChild2", "hChild2"],
				 ["hChild3", "hChild3"],					 
                 ["distH2Work",  "distH2Work"]			 
                ]
    },
    # dbf output spec; used in tests for inspecting whether results are reasonable
    {"type" : "dbffile",
     "isOutput": "true",
     "name" : "OutputSecondTours",     
     "filename" : cube___SECOND_MANDATORY_TOUR_TIME_OF_DAY___, # file paths MUST BE RAW strings (preceded by 'r')
     # parameters could be generally of form source data reference : field
     "parameters" : [
                 ["Persons", "personId"],
                 ["hhId","hhId"],
                 ["PersonTourId", "persntourid"],
                 ["tourPurp", "tourPurp"], 
                 ["personType","personType"],
                 ["cType1","cType1"],

                 ["cType2", "cType2"],
                 ["cType3", "cType3"],
                 ["cType4", "cType4"],
                 ["cType5", "cType5"],
                 ["age", "age"],

                 ["male", "male"],
                 ["destZoneId", "destZoneId"], 
                 ["workZoneId", "workZoneId"],
                 ["hhinc5s", "hhinc5s"],
                 ["wkGtCarGt0", "wkGtCarGt0"],

                 ["homeZone", "homeZoneId"],
                 ["noStopTour", "noStopTour"],
                 ["dapId",  "dapId"],
                 ["tourCount", "tourCount"],
                 ["hhC1tour", "hhC1tour"],

                 ["hhC2tour", "hhC2tour"],
                 ["hhC3tour", "hhC3tour"],
                 ["hhC4tour", "hhC4tour"],
                 ["hhC5tour", "hhC5tour"],
                 ["hhChildSAH", "hhChildSAH"],

                 ["ctype",  "ctype"],   
                 ["nCars", "nCars"], 
                 ["noCarsInHh", "noCarsInHh"],
                 ["minNTours", "minNTours"], 
                 ["minNStops", "minNStops"],
				 ["adult1kids", "adult1kids"],
				 ["hChild2", "hChild2"],
				 ["hChild3", "hChild3"],					 
                 ["distH2Work",  "distH2Work"]				 
                ]
    }

]


