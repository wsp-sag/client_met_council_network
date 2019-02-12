####################################################################
# FullyJointTour.py
# other notes:
#   I am not adhering to the python convention of 70-odd columns per line
####################################################################

from Globals import *

# the name of the corresponding class on the C# side:
# this allows for multiple scripts targeting the same component
modelComponentName="PassModels"  
instantiationType="MultiModelComponent"


# this is a degenerate case of the multimodelcomponent;
# the main component does tour generation, this single submodel does participation:
subModels= {
            "MnPass": r"PassSubmodel_MnPass.py",
            "TransitPass": r"PassSubmodel_TransitPass.py",
}


dataReferences = [


    # this data will be fed to an instance of HouseholdDataUtility, along with the persons data ref following
    {"type" : "dbffile",
     "name" : "HouseholdBaseData",
     "filename" : cube___HOUSEHOLDS_FILE___, 
     # Column names are uppercase in this file
     "columns" : ["hhId", 
                  "hhInc5s", 
                  "hhZon", 
                  "hChild1", # transitpass
                  "hChild2", # for computed value kids older than 5 
                  "hChild3", # for computed value kids older than 5
                  "hStud", 
                  "hFtw", 
                  "hPtw", 
                  "hWorkers"
                  ], 
     "deferredLoad" : True 
    },


    # modeled data for person and household will be fed to a second instance of HouseholdDataUtility    

    {"type" : "dbffile",
     "dataType" : "int",
     "name" : "HouseholdModeledData",
     "filename" : cube___NUM_CARS_PER_HOUSEHOLD___, 
     "columns" : [
                "hhId",  # 00
                "hhzon",   # 01
                "nCars", # 02
                ],
     "deferredLoad" : True 
},

    # dbf output spec; used in tests for inspecting whether results are reasonable
    {"type" : "dbffile",
     "name" : "PersonWorkplaceData",     
     "filename" : cube___WORKPLACE_LOCATIONS___, # file paths MUST BE RAW strings (preceded by 'r')
     # parameters could be generally of form source data reference : field
     "columns" : [
                      "personId",
                      "hhId",
                      "hhzon",
                      "noRegWkPlc",
                      "workzoneId",
                      "wkPlcInCBD",
                      "wkPlcInSub"
                    ]
    },        
    
    {"type" : "dbffile",
     "name" : "Zones",
     "filename" : cube___ZONES_FILE___, # file paths MUST BE RAW strings (preceded by 'r')
     "columns" : [
                  "zoneId", 
                  "TEhwyacc10", 
                  "TETRacc15",  
                  "MEhwyacc10",# MnPass submodel only
                  "suburb3",
                  "suburb2",
                  "term_time",  # for stats output
                  ]  
    },



    
    {"type" : "computed",
     "name" : "computedValues",
	 # each parameter is of this form:
	 # ["columnNameForResult", "X op Y"]
	 # where X, Y each are one of the following:
	 #       constant e.g. 1.2
	 #       reference to column in another data reference
	 #         of form dataRefName:columnName 
	 #       reference to previous column in this datareference
	 #         using form :columnName
	 # op can be one of the 4 arithmetic operators + - * /
	 # or one of 7 logical operators == < <= > >= AND OR
	 # 
	 
     "parameters" :[
        ["hhChild23", "HouseholdBaseData:hChild1 + HouseholdBaseData:hChild2"], 
        ["hhCarsGt1", "HouseholdModeledData:nCars > 1"],		
        ["inc75to100", "HouseholdBaseData:hhinc5s == 3"], #transit pass
		["noCarsInHh", "HouseholdModeledData:nCars == 0"]
		]
    },
	

    # if we had an Id source we could reduce the compound key to simple key
    {"type" : "dbffile",
     "isOutput": "true",
     "name" : "OutputHouseholdPass",     
     "filename" : cube___PASS_MODEL___, # file paths MUST BE RAW strings (preceded by 'r')
     "parameters" : [
                  ["hhId",       "hhId"],
                  ["hhZon",       "hhZon"],
                  ["@household has MnPass", "mnPass"],
                  ["@household has TransitPass", "transPass"],
                  ] 
    }, 

	# this output is space and time-consuming so is disabled in the code unless a compile-time define named 'debug_validation' is set
    {"type" : "dbffile",
     "isOutput": "true",
     "name" : "OutputPassStats",     
     "filename" : cube___PASS_MODEL_SUMMARY___, # file paths MUST BE RAW strings (preceded by 'r')
     "parameters" : [
                  ["hhInc5s",  "hhInc5s"],         # 0
                  ["n No mnPass", "nNoMnPass"],
                  ["n mnPass", "nMnPass"],
                  ["n No Transit Pass", "nNoTrPass"],
                  ["n Transit Pass", "nTrPass"]
                  ]                                            
    },                                                         
                                                               
    ]                          
