####################################################################
# TourModeChoiceLogsum_SchoolLocation.py
# Config script for school logsum variant of TourModeChoice
# used in these components:
#   Usual School Location
#   TourDestinationChoiceUniversity
#   TourModeChoice for school and university tours
# To delineate the following:
#   Input/ouputu data sources 
#   Set of alternatives
#   Logit type
#   Utility function coefficients
#   mapping inputs to coefficients
####################################################################

from Globals import * 

# the name of the corresponding class on the C# side:
# this allows for multiple scripts targeting the same component
modelComponentName="SchoolLocationTourModeChoiceLogsum"  

parameters={
			"OperatingCostCentsPerMile":autoOpCost
            }

# dataReferences is a list
# each list element is a set of key:value pairs; each set has 2 required keys:  name and type
# the value corresponding to the "type" key indicates to C# how to instantiate the data reference
# the set of names is fixed for each C#-side model component
# each type constrains the set of keys to supply in the remainder of that dictionary
dataReferences = [
    # input spec
    # Rather than looping over households and tours, pass in arrays containing relevant data
    # in "memory" data references

    {"type" : "memory",
     "dataType" : "int",
     "name" : "HouseholdBaseData",                                     
     "columns" : ["hhzon", "hhinc5s", "nKidsGT2", "hWorkers", "hstud", "hchildren", "hhsize", "hChild1", "hChild2"]
    },

    {"type" : "memory",
     "dataType" : "int",
     "name" : "HouseholdModeledData",                                     
     "columns" : ["nCars", "noCarsInHh" ]
    },

    {"type" : "memory",
     "dataType" : "int",
     "name" : "HouseholdPassData",                                     
     "columns" : ["mnPass", "transPass" ]
    },

    {"type" : "memory",
     "dataType" : "int",
     "name" : "Persons",
     "columns" : ["ptype2", "gender", "age"]
    },

    # conceived as a source of constants for vector values like dummy vars; 
    {"type" : "constants",
     "name" : "Constants",
     "columns" : ["One"],
     "values" : [1]  # values are single-dimension for this data reference type
    },

    {"type" : "memory",
     "name" : "Tours",
     "columns" : [
                  # new
                  "tourPurp",  
                  # the next two are simulated for us when running the destination choice model
                  # but will come directly from input data when running tour mode choice
                  "arrival",   # 24hr time since midnight (e.g. 0.5 = 12:30 am)
                  "departure",  # 
                  "nEscOut",     # number of escorted children on outbound half tour
                  "nEscIn"     # number of escorted children on return half tour
                  ]                  
    },

    # DerivedValues; column order must match order of transient coeff rows 
    {"type" : "memory",
     "name" : "DerivedValues",
     "columns" : ["RT Distance", "pop_density_dest", "RT Cost", "Gen Time", "waitLt10", "wait10to20", "wait20to30"]
    },


    # DerivedDurableValues
    # these need to be filled by the logsum code only from the other inputs
    # In actual TourModeChoice the inputs are 
    {"type" : "memory",
     "dataType" : "int",
     "name" : "DerivedDurableValues",
     "columns" : [
                    "universityTour", # derive from tour purpose
                    "incLt50k",       # 
                    "agecat5" ,       # age 18-24
                    "ageLT16" ,      # child less than 16
                    "male",
                    "stopsExist",     # use for tbi
                    "nMealht12",      # n meal stops on both ht
                 ]
    },


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



    {"type" : "dbffile",
     "name" : "Zones",
     "filename" : cube___ZONES_FILE___, 
     "columns" : ["zoneId", "mix_dens", "ret_emp", "population", "tot_emp", "term_time", "park_cost","area", "district"]
    }
]

from MatrixRef4Hwy4Trans import matrixReferences

########################  model structure section  ##########################

# values are those of C# TourMode enum:
altIntrinsicValues = [1, 2, 3, 4, 5, 8, 7, 6]

altNames = ["DA", "S2", "S3", "TW", "TD", "SB", "WK", "BK"]

logitType="NestedLogit"

# NestedLogit

# ASCII representation of nesting structure

#   [UI name, nestID, nest coeff, [alts], [nests]]
# where [alts] refers to alternatives by its order in any of the altIntrinsicValues/altNames/durableCoeffs/transientCoeffs lists
# and [nests] is a list of nestIDs
# 
nestList = [
            ["Root", 0, 1.0, [], [1, 2, 3, 4]], 
            ["Auto", 1, 0.4, [0, 1, 2], []],
            ["Transit", 2, 0.4, [3, 4], []],
            ["School Bus", 3, 0.4, [5], []],
            ["Non-Motorized", 4, 0.4, [6, 7], []]
           ]

 # DA,        # S2,        # S3,        # TW,        # TD,        # SB,        # BK         # WK,       
[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000] # 

# Coefficients are divided into two types:
#   coefficients whose corresponding values don't change very often ('durable' values)
#   coefficients whose values are assumed to change for every iteration ('transient' values)

# In the case of logsums, the normal expectations for what is durable and what is transient are reversed
# because the logsum computations occur over all zones for a fixed person
# description of transient variables:
# some variables  are segmented by income, so those coefficients have placeholder values of 0
# Just for reference I've indicated the segmentation applied in parens e.g. (I2 means using 2 income segments (<$40k, >=$40k))
transientCoeffs=[
 
   # DA,        # S2,        # S3,        # TW,        # TD,        # SB,        # BK         # WK,       
[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000, -0.80439384, -1.03622748], # 00 RT distance bike, walk
# these segmented by school/university                                                                       
[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 01 Population density at destination 
[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 02 Travel cost in cents 
[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 03 Generalized Time
[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 04 IB+OB Wait time 0-10 minutes
[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 05 IB+OB Wait time 10-20 minutes
[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 06 IB+OB Wait time 20-30 minutes
]
# special case for the logsums ; the DerivedValues reference is used by the TourModeChoiceLogit to map the calculations to the correct positions in the transient vector
# this map is not used:
transientCoeffMap={                 
                   #"DerivedValues" : [[0,0,7]], 
                   }  


# tour sort for destination choice (university only for TBI):
#  "hhzon", "hhinc5s", "hhid", "ptype2"; 
# for Tour Mode Choice, home-based tours, sort is dictated by Household base sort, which is by zone, hhinc, hh;

durableCoeffs=[
   # DA,        # S2,        # S3,        # TW,        # TD,        # SB,        # BK         # WK,       
# tour purpose-related: no sort relevance
[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 00 ASC [segmented school/uni]
[  0.00000000, -0.26765424, -0.26765424,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 01 incl50 # Income < $50K
# the rest of these are all segmented by school vs uni tour                                                   
[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 02 HH vehicles
[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 03 HH number of children
[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 04 HH size
# person-related (no sort relevance):                                                                         
[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 05 Age between 18 and 24 years
[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 06 Child age less than 16 years
[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 07 male
# tour related:                                                                                              
[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 08 Presence of stops HT1 or HT2
[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 09 Number of meal stops HT1+HT2
#added during calibration
[ placeholder ] * 8 # 10 Income Specific Constant 
]




# we need a map from the inputs to the locations in the lists
# It's easier to devise a notation if the order of data columns matches up with a range of the coefficients
# durableCoeffMap={"table name": [[tableColIndex, matchingCoeffVectorStartIndex, numberOfConsecutiveColumnsToMatch],...]}
# The skim related values all have to be computed in the code

durableCoeffMap={
                 "Constants" : [[0,0,1], #ASC
								[0,10,1]], #income segment
                 "HouseholdModeledData" : [[0,2,1]], #"nCars"
                 "HouseholdBaseData" : [[5,3, 2]], # hchildren, hhsize
                 "DerivedDurableValues": [[1,1,1], #income < 50 k
                                          [2, 5, 5]],  # 05 Age between 18 and 24 years
                                                      # 06 Child age less than 16 years
                                                      # 07 male                                                        
                                                      # 08 Presence of stops HT1 or HT2
                                                      # 09 Number of meal stops HT1+HT2											  
                 } 

# 
# SEGMENTATION maps to handle cases where the coefficient depends upon some segmentation of the input data,
# usually household income:
#

# segmentDefinitions is list, each element of which defines (via key:value pairs):
#  Name: a friendly name not used elsewhere except maybe in comments in this file
#  DataRef:  Which input DataReference contains the segmentation info
#  Offset:   which column in the input has this segmentation info
#  DataRange: an array of discrete values representing the segmentation range; 
# there are 2 subtleties here:
#    at the top level, the array index within the segmentDefinitions array is used in the segmentCoeffMap
#    the DataRange array order corresponds to the order of the coefficients in each row of the 'coefficients' value in segmentCoeffMap
segmentDefinitions = [
#  friendly name     , input data ref, offset in input, range of values (order relates to coeff order in segmentCoeffMap)
 {'Name': 'School/University tour', 'DataRef': 'DerivedDurableValues','Offset': 0, 'DataRange': [0,1]}, # 0-school, 1-uni
 {'Name': '5 Income Segments', 'DataRef': 'HouseholdBaseData','Offset': 1, 'DataRange': [0,1,2,3,4]}
]

# segmentCoeffMap is another list of sets of key:value pairs.  The length of the list = the number of coefficients 
# that are affected by segmentation within the durable and transient vectors of the alternative(s)
# Each set defines:
#  Segment: index into the segmentDefinitions list
#  Vector:  possible values: durable/transient:  which coefficient vector in the alternative(s) this set of coefficients applies to
#  Offset:  offset into the relevant Coefficient vector 
#  Coefficients: an list of lists; first index is which alternative
#           for each alternative, the array represents coefficient value 
#               corresponding by index with each possible value of the segment in the segmentDefinitions.DataRange
#               e.g. if the '5 Income Segments' input value = 2, then the coefficient for hchild3 (the last segmentCoeffMap array 
#               below) is at offset 2 of the Coefficients, or 0.515
#               another example, if the '2 Income Segments' input (at offset 11 of the households data) = 0,



segmentCoeffMap = [
# segmentDefinitions offset, which coeffVector, offset in coeffVector, 

{'Segment': 0, 'Vector': 'durable', 'Offset': 0, # TP # Constants 
  'Coefficients':
    [      # School     # University
	[0, 0],	#	DA
	[-2.952, -0.943],	#	S2
	[0.477, -1.177],	#	S3
	[-0.478, 3.156],	#	TW
	[-4.093, 2.592],	#	TD
	[-2.989, 0],	#	SB
	[-1.53, 7.984],	#	BK
	[-0.176, 11.494],	#	WK
]
},


{'Segment': 0, 'Vector': 'durable', 'Offset': 2, # hhveh # HH vehicles
  'Coefficients':
    [      # School     # University        
        [  1.94893474,  2.07030352], # DA
        [  1.65300040,  1.36347891], # S2
        [  0.96133311,  1.36347891], # S3
        [  0.00000000,  0.00000000], # TW
        [  0.00000000,  0.00000000], # TD
        [  0.00000000,  0.00000000], # SB
        [  0.00000000,  0.00000000], # BK
        [  0.00000000,  0.00000000]  # WK
    ]
},

{'Segment': 0, 'Vector': 'durable', 'Offset': 3, # Chldrn # HH number of children
  'Coefficients':
    [      # School     # University
        [ -0.52961997,  0.00000000], # DA
        [  0.00000000,  0.00000000], # S2
        [  0.00000000,  0.00000000], # S3
        [  0.00000000,  0.00000000], # TW
        [  0.00000000,  0.00000000], # TD
        [  0.00000000,  0.00000000], # SB
        [  0.00000000,  0.00000000], # BK
        [  0.00000000,  0.00000000]  # WK
    ]
},

{'Segment': 0, 'Vector': 'durable', 'Offset': 4, # hhsize # HH size
  'Coefficients':
    [      # School     # University
        [  0.00000000,  0.00000000], # DA
        [  0.00000000,  0.00000000], # S2
        [  0.00000000,  0.00000000], # S3
        [  0.00000000,  0.00000000], # TW
        [  0.00000000,  0.00000000], # TD
        [  0.80138409,  0.00000000], # SB
        [  0.00000000,  0.00000000], # BK
        [  0.00000000,  0.00000000]  # WK
    ]
},

{'Segment': 0, 'Vector': 'durable', 'Offset': 5, # a18t24 # Age between 18 and 24 years
  'Coefficients':
    [      # School     # University
        [  0.00000000,  0.00000000], # DA
        [  0.00000000,  0.00000000], # S2
        [  0.00000000,  0.00000000], # S3
        [  5.12565338,  0.00000000], # TW
        [  5.12565338,  0.00000000], # TD
        [  0.00000000,  0.00000000], # SB
        [  0.00000000,  0.00000000], # BK
        [  0.00000000,  0.00000000]  # WK

    ]
},

{'Segment': 0, 'Vector': 'durable', 'Offset': 6, # agel15 # Child age less than 16 years
  'Coefficients':
    [      # School     # University
        [  0.00000000,  0.00000000], # DA
        [  0.00000000,  0.00000000], # S2
        [  0.00000000,  0.00000000], # S3
        [  0.00000000,  0.00000000], # TW
        [  0.00000000,  0.00000000], # TD
        [  3.62684176,  0.00000000], # SB
        [  0.00000000,  0.00000000], # BK
        [  0.00000000,  0.00000000]  # WK
    ]
},

{'Segment': 0, 'Vector': 'durable', 'Offset': 7, # male #  
  'Coefficients':
    [      # School     # University
        [  0.00000000,  0.00000000], # DA
        [  0.00000000,  0.00000000], # S2
        [  0.00000000,  0.00000000], # S3
        [  0.00000000,  0.00000000], # TW
        [  0.00000000,  0.00000000], # TD
        [  0.00000000,  0.00000000], # SB
        [  2.69119033,  0.97005611], # BK
        [  2.69119033,  0.00000000]  # WK
    ]
},

{'Segment': 0, 'Vector': 'durable', 'Offset': 8,  # stops # Presence of stops HT1 or HT2
  'Coefficients':
    [      # School     # University        
        [  0.74646704,  0.00000000], # DA
        [  0.74646704,  0.00000000], # S2
        [  0.74646704,  0.00000000], # S3
        [  1.00000000,  0.00000000], # TW
        [  0.00000000,  0.00000000], # TD
        [  0.00000000,  0.00000000], # SB
        [ -2.00000000,  0.00000000], # BK
        [ -3.00000000,  0.00000000]  # WK
    ]
},

{'Segment': 0, 'Vector': 'durable', 'Offset': 9, # hasEat # Number of meal stops HT1+HT2
  'Coefficients':
    [      # School     # University
        [  0.00000000,  0.00000000], # DA
        [  0.00000000,  0.00000000], # S2
        [  0.00000000,  2.18042903], # S3
        [  0.00000000,  0.00000000], # TW
        [  0.00000000,  0.00000000], # TD
        [  0.00000000,  0.00000000], # SB
        [  0.00000000,  0.00000000], # BK
        [  0.00000000,  0.00000000]  # WK
    ]
},


############# segmentation for transients  #################
{'Segment': 0, 'Vector': 'transient', 'Offset': 1, # dpopdn # Population density at destination
  'Coefficients':
    [      # School     # University
        [  0.00000000,  0.00000000], # DA
        [  0.00000000,  0.00000000], # S2
        [  0.00000000,  0.00000000], # S3
        [  0.00000000,  0.00000000], # TW
        [  0.00000000,  0.00000000], # TD
        [  0.00000000,  0.00000000], # SB
        [  0.00018902,  0.00000000], # BK
        [  0.00018902,  0.00000000]  # WK
    ]
},


{'Segment': 0, 'Vector': 'transient', 'Offset': 2,  #  Travel cost in cents 
  'Coefficients':
    [      # School     # University
        [ -0.00280000, -0.00280000], # DA
        [ -0.00280000, -0.00280000], # S2
        [ -0.00280000, -0.00280000], # S3
        [ -0.00280000, -0.00280000], # TW
        [ -0.00280000, -0.00280000], # TD
        [  0.00000000,  0.00000000], # SB
        [  0.00000000,  0.00000000], # BK
        [  0.00000000,  0.00000000]  # WK
    ]
},

{'Segment': 0, 'Vector': 'transient', 'Offset': 3,  # ttime # Generalized Time
  'Coefficients':
    [      # School     # University
        [ -0.02000000, -0.02000000], # DA
        [ -0.02000000, -0.02000000], # S2
        [ -0.02000000, -0.02000000], # S3
        [ -0.02000000, -0.02000000], # TW
        [ -0.02000000, -0.02000000], # TD
        [  0.00000000,  0.00000000], # SB
        [  0.00000000,  0.00000000], # BK
        [  0.00000000,  0.00000000]  # WK
    ]
},

{'Segment': 0, 'Vector': 'transient', 'Offset': 4, # TWfq10 # IB+OB Wait time 0-10 minutes
  'Coefficients':
    [      # School     # University
        [  0.00000000,  0.00000000], # DA
        [  0.00000000,  0.00000000], # S2
        [  0.00000000,  0.00000000], # S3
        [  2.55057743,  6.47577585], # TW
        [  0.00000000,  0.00000000], # TD
        [  0.00000000,  0.00000000], # SB
        [  0.00000000,  0.00000000], # BK
        [  0.00000000,  0.00000000]  # WK
    ]
},

{'Segment': 0, 'Vector': 'transient', 'Offset': 5, # TWfq20 # IB+OB Wait time 10-20 minutes
  'Coefficients':
    [      # School     # University
        [  0.00000000,  0.00000000], # DA
        [  0.00000000,  0.00000000], # S2
        [  0.00000000,  0.00000000], # S3
        [  2.55057743,  3.68465617], # TW
        [  0.00000000,  0.00000000], # TD
        [  0.00000000,  0.00000000], # SB
        [  0.00000000,  0.00000000], # BK
        [  0.00000000,  0.00000000]  # WK
    ]
},

{'Segment': 0, 'Vector': 'transient', 'Offset': 6, # TWfq30 # IB+OB Wait time 20-30 minutes
  'Coefficients':
    [      # School     # University
        [  0.00000000,  0.00000000], # DA
        [  0.00000000,  0.00000000], # S2
        [  0.00000000,  0.00000000], # S3
        [  0.00000000,  3.68465617], # TW
        [  0.00000000,  0.00000000], # TD
        [  0.00000000,  0.00000000], # SB
        [  0.00000000,  0.00000000], # BK
        [  0.00000000,  0.00000000]  # WK
    ]
},


{'Segment': 1, 'Vector': 'durable', 'Offset': 10,  # Constant
  'Coefficients':
    [ # normally 1 row that applies to every alternative; it's possible that there may be alternative-specific-variables that are affected by segmentation
      # in that case there would be as many rows as alternatives; I suspect this would never apply to a case with a very large alternative set
        #coeff when segment value is 0, 1, 2, 3, 4 respectively
			# INC0        # INC1       # INC2       # INC3       # INC4
		[ 0, 	0, 	0, 	0, 	0], #  DriveAlone	
		[ 0, 	0, 	0, 	0, 	0], #  SharedRide2	
		[ 0, 	0, 	0, 	0, 	0], #  SharedRide3	
		[ 2, 	0, 	0, 	0, 	0], #  WalkToTransit	
		[ 0, 	0, 	0, 	0, 	0], #  DriveToTransit	
		[ 2, 	0, 	0, 	0, 	0], #  School Bus	
		[ 0, 	0, 	0, 	0, 	0], #  Bike	
		[ 0, 	0, 	0, 	0, 	0], #  Walk	

    ]
}

]
