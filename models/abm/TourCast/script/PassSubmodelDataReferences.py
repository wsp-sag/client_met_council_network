####################################################################
# PassSubmodelDataReferences.py
# i.e. Common information for PARTICIPATION submodels of the Fully Joint Tour Submodels
####################################################################


dataReferences = [
    {"type" : "constants",
     "name" : "Constants",
     "columns" : ["One"],
     "values" : [1]
    },

    # this data will be fed to an instance of HouseholdDataUtility, along with the persons data ref following
    {"type" : "memory",
     "name" : "HouseholdBaseData",
     "dataType" : "int",
     # Column names are uppercase in this file
     "columns" : ["hhId", 
                  "hhInc5s", 
                  "hhZon", 
                  "hChild1", # transitpass
                  "hChild2", # for computed value kids older than 5 
                  "hChild3", # for computed value kids older than 5
                  "hStud", 
                  "hftw", 
                  "hPtw", 
                  "hWorkers"
                  ]
    },

    {"type" : "memory",
     "dataType" : "int",
     "name" : "PersonWorkplaceData",
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


    {"type" : "memory",
     "dataType" : "int",
     "name" : "HouseholdModeledData",
     "columns" : [
                "hhId",         # 00
                "hhzon",   # 01
                "nCars",        # 02
                ]
},

    {"type" : "memory",
     "dataType" : "int",
     "name" : "ComputedValues",
     "columns" : [
		"hhChild23", 
		"hhCarsGt1", 
		"inc75to100",
		"noCarsInHh"
                 ]                          
    },
	
    {"type" : "memory",
     "dataType" : "int",
     "name" : "DerivedValues",
     "columns" : [
		"nWkPlcInCBD", 
		"xWkPlcInSub" 
                 ]                          
    },

    {"type" : "memory",
     "dataType" : "double",
     "name" : "Zones",
     "columns" : [
                  "zoneId", 
                  "TEhwyacc10", 
                  "TETRacc15",  
                  "MEhwyacc10", # MnPass submodel only
                  "suburb3",
                  "suburb2",
                  "term_time",  # for stats output
                 ]                          
    }
    
]

# Matrices are different enough to require their own structure:
matrixReferences = [ ]
# for now none 




 
