####################################################################
# SchoolLocationAssignment.py
####################################################################

from Globals import *

instantiationType="DataAssemblyComponent"
#characteristics

# the name of the corresponding class on the C# side:
# this allows for multiple scripts targeting the same component
modelComponentName="SchoolLocationAssignment"  


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
     "name" : "Children",
     "filename" : cube___PERSONS_CHILDREN___, # file paths MUST BE RAW strings (open quote preceded by 'r')
     "columns" : ["personid", 
                  "hhid", 
                  "hhzon", 
                  "age",
                  ], #
     "deferredLoad" : True     
    },

    {"type" : "dbffile",
     "name" : "Zones",     
     "filename" : cube___ZONES_FILE___,# file paths MUST BE RAW strings (preceded by 'r')
     # for dbf as input, supply columns instead of parameters
     # one problem with the way we're processing dbf files as input is that we don't have a select statement
     "columns" : ["zoneId", 
                  "elSchZone",  
                  "hSchZone"
                ],
     "deferredLoad" : False 
    },

    # dbf output spec
    {"type" : "dbffile",
     "isOutput": "true",
     "name" : "OutputSchoolLocation",     
     "filename" : cube___SCHOOL_LOCATIONS___, 
     "parameters" : [
                    ["PERSONID","PERSONID"],  #these columns directly copied from Persons input
                    ["HHID","HHID"],
                    ["HHZON","HHZON"],
                    ["schZoneId", "schZoneId"]  # output added from SchoolLocation
                    ]
    }
     
]

