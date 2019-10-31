####################################################################
# SchoolLocationConstrChoice.py
#
#	Available alternatives are pre-selected and saved into the zone db file
#
#	Alternatives are grouped by age ranges, that are roughly associated with school type (elementary, middle, high) 
#	The child age is used to determine the school type (2, 3, 4 & 5 respectively)
#
#	The zones file is configured to support up to 10 alternatives, if more are desired, the 
#	SCH#NUM# convention must be followed. If fewer zones are available, a 0 (zero) must be written in the zones file
#
#
####################################################################

from Globals import *

#characteristics

# the name of the corresponding class on the C# side:
# this allows for multiple scripts targeting the same component
modelComponentName="SchoolLocationConstrChoice"  
logitType="MultinomialLogit"


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

    # conceived as a source of constants for vector values like dummy vars; 
    {"type" : "constants",
     "name" : "Constants",
     "columns" : ["One"],
     "values" : [1]  # values are single-dimension for this data reference type
    },
	
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
        ["chldGrp1", "Children:age == 2"], 
        ["chldGrp2", "Children:age == 3"]
		]
    },	

	# The zones file contains all the school location alternatives
	# The first zone listed for each school type MUST be the nearest school
    {"type" : "dbffile",
     "name" : "Zones",     
     "filename" : cube___ZONES_FILE___,# file paths MUST BE RAW strings (preceded by 'r')
     # for dbf as input, supply columns instead of parameters
     # one problem with the way we're processing dbf files as input is that we don't have a select statement
     "columns" : ["zoneId", 
					"SCH1NUM1",
					"SCH1NUM2",
					"SCH1NUM3",
					"SCH1NUM4",
					"SCH1NUM5",
					"SCH1NUM6",
					"SCH1NUM7",
					"SCH1NUM8",
					"SCH1NUM9",
					"SCH1NUM10",
					"SCH2NUM1",
					"SCH2NUM2",
					"SCH2NUM3",
					"SCH2NUM4",
					"SCH2NUM5",
					"SCH2NUM6",
					"SCH2NUM7",
					"SCH2NUM8",
					"SCH2NUM9",
					"SCH2NUM10",
					"SCH3NUM1",
					"SCH3NUM2",
					"SCH3NUM3",
					"SCH3NUM4",
					"SCH3NUM5",
					"SCH3NUM6",
					"SCH3NUM7",
					"SCH3NUM8",
					"SCH3NUM9",
					"SCH3NUM10"
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
                    ["schZoneId", "schZoneId"],  # output added from SchoolLocation
                    ["schType", "schType"]  # output added from SchoolLocation (1 = elem, 2 = middle, 3 = high)
                    ]
    }
     
]

# if the number of potential alternatives changes, these arrays must also change
altIntrinsicValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

altNames = []

from itertools import chain

# When all 10 zones are available, this equals a 25% share to the nearest zone and equal share to the other 9
altSpecificConsts = list(chain(
		[0 ] * 1, 			# nearest zone
		[-1.09861 ] * 9  	# all other zones
))

transientCoeffs=[
# placeholder
[0]*10
]
transientCoeffMap={"Constants" : [[0,0,1]]}

durableCoeffs=[
[0]*10,  # child group 1 placeholder
[0]*10,  # child group 2 placeholder
]
durableCoeffMap={"computedValues" : [[0,0,2]]}
