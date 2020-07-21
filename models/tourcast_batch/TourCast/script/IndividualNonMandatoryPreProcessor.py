####################################################################
# PreINMDataAssembly.py
####################################################################

from Globals import *

instantiationType="DataAssemblyComponent"
#characteristics

# the name of the corresponding class on the C# side:
# this allows for multiple scripts targeting the same component
modelComponentName="PreINMDataAssembly"  


dataReferences = [
    {"type" : "dbffile",
     "name" : "Persons",
     "filename" : cube___PERSONS_FILE___, 
     # Column names are uppercase in this file
     "columns" : [
                  "personId",
                  "HHID", 
                  "HHINC5S", 
                  "HHZON", 
                  "ptypeDAP", 
                  "gender",
                  "age"
                  ],
     "deferredLoad" : True 
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
                       "tourCount",
                       "slotsUsed",
                       "slotsArriv",
                       "slotsDeprt"
                       # using '@' in data source name indicates this field is generated or updated by the component, so requires some coordination with C# code
                    ],
     "deferredLoad" : True 
    },
    
    # this data will be fed to an instance of HouseholdDataUtility, along with the persons data ref following
    {"type" : "dbffile",
     "name" : "Households",
     "filename" : cube___HOUSEHOLDS_FILE___, 
     # Column names are uppercase in this file
     "columns" : ["HHID", 
                  "HHINC5S", 
                  "HHZON", 
                  "HCHILD3", 
                  "HSTUD", 
                  "HFTW", 
                  "HPTW", 
                  "HNWA", 
                  "HSEN", 
                  "HH1PERSON", 
                  "ADULT1KIDS",
                  "HCHILDREN", 
                  "HHSIZE"
                  ], 
     "deferredLoad" : True 
    },

   # modeled data for person and household will be fed to a second instance of HouseholdDataUtility    

    {"type" : "dbffile",
     "dataType" : "int",
     "name" : "HouseholdsModeledData",
     "filename" : cube___MODELED_HOUSEHOLDS_FILE___, 
     "columns" : [
                "hhId",
                "homeZoneId",
                "nCars",
                "nC1_NMT",
                "nC2_NMT",
                "nC3_NMT",
                "nNWA_NMT",
                "nSen_NMT",
                "nPTW_NMT",
                "nFTW_NMT",
                "nAdS_NMT",
                "nHH_NMT",
                "nC1_MND",
                "nC2_MND",
                "nC3_MND",
                "nNWA_MND",
                "nSen_MND",
                "nPTW_MND",
                "nFTW_MND",
                "nAdS_MND",
                "nHH_MND",
                "nCT1_Sch",
                "nCT2_Sch",
                "nCT3_Sch",
                "nCT4_Sch",
                "nCT5_Sch",
                "nC_SAH",
                "nCh_0Tours",
                "nAdt_0Tours"
                ],
     "deferredLoad" : True 
},
 {"type" : "dbffile",
     "name" : "SchoolEscortTours",     
     "filename" : cube___SCHOOL_ESCORT_TOURS___, # file paths MUST BE RAW strings (preceded by 'r')
     "columns" : [
                     "personId",
                     "hhId",
                     "persTourId",
                     "tourPurp",
                     "homeZoneId",
                     "noStopTour",
                     "tourCount",
                     "arrival",
                     "departure"
                     # using '@' in data source name indicates this field is generated by the component, so requires some coordination with C# code
                    ]
    },

    # equivalent of link table from personId to tours;
    # if we had an Id source we could reduc
    {"type" : "dbffile",
     "name" : "PersonTourLinkTable",     
     "filename" : cube___FULLY_JOINT_TOUR_PERSON_LINK_TABLE___, # file paths MUST BE RAW strings (preceded by 'r')
     "columns" : [
                 "personId",  # person involved in tour
                 "persTourId",  # partial pk to FullyJointTours
                 "tourId",        # partial pk to FullyJointTours
                 "homeZoneId",  # for chunking
                  ] 
    },
    
   {"type" : "dbffile",
     "name" : "FullyJointDaySchedules",     
     "filename" : cube___FULLY_JOINT_TOUR_PERSON_SCHEDULES___,
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
     "dataType" : "int",
     "name" : "PersonsModeledData",
     "filename" : cube___DAILY_ACTIVITY_PATTERNS___, # may substitute another downstream item later
     "columns" : [
                "personId",
                "hhId",
                "homeZoneId", # for grouping
                "DAPId",
                "tourCount"
                ],
     "deferredLoad" : True 
},


    {"type" : "dbffile",
     "name" : "Zones",
     "filename" : cube___ZONES_FILE___, # file paths MUST BE RAW strings (preceded by 'r')
     "columns" : ["zoneId", "mix_dens", "rehwyacc10", "nehwyacc10"] 
    },

    {"type" : "dbffile",
     "isOutput": "true",
     "name" : "INM_PersonsModeledData",     
     "filename" : cube___INDIVIDUAL_NON_MANDATORY_TOUR_PRE_PROCESSED_DATA___, # file paths MUST BE RAW strings (preceded by 'r')
     # parameters could be generally of form source data reference : field
     "parameters" : [
                       [ "Persons",  "personId"],  
                       [ "hhId",     "hhId"],  
                       [ "homeZone", "homeZnId"],  
                       [ "DAPId",    "DAPId"],  
					   #Household
                       [ "hhinc5s",  "hhinc5s"],  
					   [ "hhsize",   "hhsize"],
                       [ "hnochildren","hnochildren"],			   
					   #zone/network variables
                       [ "mix_dens",  "mix_dens"],  
                       [ "hwy_retEmp","hwy_retEmp"],  
                       [ "hwy_nRetEmp","hwy_nRetEmp"],  
					   # HH modeled variables
                       [ "hnocars",	  "hnocars"],							   
					   [ "nChildMand", "nChldMnd"],
                       [ "nWorkersMand","nWorkerMnd"],  
                       [ "nWorkersNonMand","nWorkerNMT"],  
                       [ "StudNonWorkingSenMND","StdNwSnMND"],
                       [ "StudNonWorkingSenNMT","StdNwSnNMT"],
					   # person type variables
					   [ "child2", "child2"],
                       [ "child3", "child3"],
                       [ "stud",   "stud"],
                       [ "ftw",    "ftw"],
                       [ "ptw",    "ptw"],
                       [ "nwa",    "nwa"],
                       [ "adultFemale",    "adultFemale"],	
						# person DAP variables
                       [ "xC123_MND","xC123_MND"],
                       [ "xAds_MND", "xAds_MND"],
					   [ "WorkTourWithStops","gt1WkStops"],
                       [ "twoMND", "twoMND"],
                       [ "schEsc", "schEsc"],                       
                       [ "FJTours", "ge1FJTour"],
                       [ "logMaxTime", "logMaxT"],
                       [ "logRemTimeDay", "logRemTDay"],
					   # variables to pass on to other models
					   [ "ptypeDAP", "ptypeDAP"],
					   [ "adult1Kids", "adult1Kids"]
                    ]
     }
]