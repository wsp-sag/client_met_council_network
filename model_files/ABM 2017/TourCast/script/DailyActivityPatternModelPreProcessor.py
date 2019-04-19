####################################################################
# DailyActivityPatternModelPreProcessor.py
# A python script with DataReferences only
# the idea here is allow components to just select the data they need
# and then in an external component, merge data generated by the component with the proper base data sets 
# (e.g. persons, households...)
####################################################################

from Globals import *

instantiationType="DataAssemblyComponent"
#characteristics

# the name of the corresponding class on the C# side:
# this allows for multiple scripts targeting the same component
modelComponentName="PreDAPDataAssembly"  


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

    # only the columns needed for DAP
    # list columns in the same order as for output for convenience in the code
    {"type" : "dbffile",
     "name" : "Persons",
     "filename" : cube___PERSONS_FILE___, 
     "columns" : [
                  "personid",   # 0
                  "hhid",       # 1
                  "hhzon",      # 2
                  "ptypeDap",     # 3
                  "hhinc5s",    # 4 
                  "hhsize",     # 5 
                  "hchild1",    # 6
                  "hchild2",    # 7
                  "hchild3",    # 8
                  "hstud",      # 9
                  "hftw",       # 10
                  "hptw",       # 11
                  "hnwa",       # 12
                  "hsen",       # 13
                  "age",        # 14
                  "hchildren",  # 15
                  "hworkers",   # 16
                  "hchildlt16", # 17
                  "hh1Person",  # 19
                  "female",     # 20
                  "hpotworkad", # 21
                  "hnochildre", # 22
                  "hadults",    # 23
                  "ctype"       # 24                
                  ],
     "deferredLoad" : True, # new parameter, for input Dbf only; cannot combine 'sort' parameter with this
     #"sort" : ["hhzon", "hhinc5s", "hhid"]   # sort parameter is not available when using deferredLoad
     #"maxrecords":20000
    },

    {"type" : "dbffile",
     "name" : "UsualWorkplaceLocation",     
     "filename" : cube___WORKPLACE_LOCATIONS___,# file paths MUST BE RAW strings (preceded by 'r')
     # for dbf as input, supply columns instead of parameters
     # one problem with the way we're processing dbf files as input is that we don't have a select statement
     "columns" : ["personid", "hhzon",  "workZoneId", "noRegWkPlc", "logsum", "logRtToWk", "wlkTraccWk"],
     "deferredLoad" : True # new parameter, for input Dbf only; cannot combine 'sort' parameter with this
    },

    {"type" : "dbffile",
     "name" : "UsualSchoolLocation",     
     "filename" : cube___SCHOOL_LOCATIONS___,# file paths MUST BE RAW strings (preceded by 'r')
     # for dbf as input, supply columns instead of parameters
     # one problem with the way we're processing dbf files as input is that we don't have a select statement
     "columns" : ["personid", "homeZoneId", "schZoneId"],
     "deferredLoad" : True # new parameter, for input Dbf only; cannot combine 'sort' parameter with this
    },

    {"type" : "dbffile",
     "name" : "NCarsFromAA",     
     "filename" : cube___NUM_CARS_PER_HOUSEHOLD___,# file paths MUST BE RAW strings (preceded by 'r')
     # for dbf as input, supply columns instead of parameters
     # one problem with the way we're processing dbf files as input is that we don't have a select statement
     "columns" : ["hhid", "hhzon", "nCars", "noCarsInHh", "wkGtCarGt0"],
     "deferredLoad" : True # new parameter, for input Dbf only; cannot combine 'sort' parameter with this
    },    

    # dbf output spec
    {"type" : "dbffile",
     "isOutput": "true",
     "name" : "OutputPersons",     
     "filename" : cube___DAILY_ACTIVITY_PATTERN_PRE_PROCESSED_DATA___, 
     "parameters" : [
                    ["personId","personId"],  #these columns directly copied from Persons input
                    ["HHID","hhId"],
                    ["HHZON","hhZon"],
                    ["PTYPEDAP","ptypeDAP"],
                    ["HHINC5S","hhInc5s"],
                    ["HHSIZE","hhSize"],

                    ["HCHILD1","hChild1"],
                    ["HCHILD2","hChild2"],
                    ["HCHILD3","hChild3"],
                    ["HSTUD","hStud"],
                    ["HFTW","hFtw"],

                    ["HPTW","HPTW"],
                    ["HNWA","HNWA"],
                    ["HSEN","HSEN"],
                    ["AGE","AGE"],
                    ["HCHILDREN","HCHILDREN"],

                    ["HWORKERS","HWORKERS"],
                    ["HCHILDLT16","HCHILDLT16"],                    
                    ["HH1PERSON","HH1PERSON"],
                    ["FEMALE","FEMALE"],

                    ["HPOTWORKAD","HPOTWORKAD"],
                    ["HNOCHILDRE","HNOCHILDRE"],
                    ["HADULTS", "HADULTS"],
                    ["CTYPE","CTYPE"],
                    ["NCARS", "NCARS"],        

                    ["noCarsInHh", "noCarsInHh"],
                    ["wkGtCarGt0", "wkGtCarGt0"],
                    ["workZoneId","workZoneId"],# output added from usual workplace
                    ["noRegWkPlc","noRegWkPlc"],# output added from usual workplace
                    ["logsum", "logsum"],       # tour mode choice logsum for selected workplace zone
                    ["logRtToWk", "logRtToWk"], # if regular workplace, log (1+ RT distance) from home zone to work zone
                    ["wlkTraccWk", "wlkTraccWk"], # walk access to transit to workplace, both directions
                    ["schZoneId", "schZoneId"],  # output added from SchoolLocation
					["one adult + kid(s)", "adult1kids"] # calculating from other data in person input rather than add household input
                    ]
          # actually use the following to support both DAP and SchoolEscorting
          # "sort": ["hhzon", "hhinc5s", "hhid", "pTypeDAP" "age", "personId"]
    }
     
]
