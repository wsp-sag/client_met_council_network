####################################################################
# TemporaryPrePassDataAssembly.py
#  simulate data to feed to PassModel
# 
####################################################################

from Globals import *

modelComponentName="TemporaryPrePassDataAssembly"  
instantiationType="DataAssemblyComponent"


dataReferences = [

    {"type" : "dbffile",
     "name" : "HouseholdBaseData",
     "filename" : cube___HOUSEHOLDS_FILE___, 
     "columns" : ["HHID", 
                  "HHINC5s", 
                  "hhzon", 
                  ], 
     "deferredLoad" : True 
    },

    {"type" : "dbffile",
     "name" : "Persons",
     "filename" : cube___PERSONS_FILE___, 
     # Column names are uppercase in this file
     "columns" : ["personId", 
                  "hhId", 
                  "hhzon", 
				  "ptype"
                  ], 
     "deferredLoad" : True 
    },

    {"type" : "dbffile",
     "name" : "Zones",
     "filename" : cube___ZONES_FILE___, # file paths MUST BE RAW strings (preceded by 'r')
     "columns" : [
                  "zoneID",
				  "CBD",				  
                  "term_time"
                  ]  
	 # no deferred load
    },
	

    # modeled data for person and household will be fed to a second instance of HouseholdDataUtility    

    {"type" : "dbffile",     
     "name" : "HouseholdModeledData",
	 "isOutput" : "true",
     "filename" : cube___MODELED_HOUSEHOLDS_FILE___, 
     "parameters" : [
                ["hhId",  "hhId"],  # 00
                ["hhzon", "hhzon"],   # 01
                ["nCars", "nCars"] # 02
                ],
},

    # dbf output spec; used in tests for inspecting whether results are reasonable
    {"type" : "dbffile",
     "name" : "PersonWorkplaceData",     
	 "isOutput" : "true",
     "filename" : cube___WORKPLACE_LOCATIONS___, # file paths MUST BE RAW strings (preceded by 'r')
     "parameters" : [
                      ["personId",   "personId"],
                      ["hhId",       "hhId"],
                      ["hhzon",      "hhzon"],
                      ["noRegWkPlc", "noRegWkPlc"],
                      ["workzoneId", "workzoneId"],
                      ["wpInCBD",    "wpInCBD"],
                      ["wpInSubB",    "wpInSubB"]
                    ]
    }
                                                               
    ]                          
