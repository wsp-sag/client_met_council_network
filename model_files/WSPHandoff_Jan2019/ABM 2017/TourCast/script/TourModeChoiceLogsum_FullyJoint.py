####################################################################
# TourModeChoiceLogsumFullyJoint.py
# Config script used by Fully Joint tour destination choice 
# and by Fully Joint Tour Mode choice components
# To delineate the following:
#   Input/output data sources 
#   Set of alternatives
#   Logit type
#   Utility function coefficients
#   mapping inputs to coefficients
####################################################################

from Globals import * 

# the name of the corresponding class on the C# side:
# this allows for multiple scripts targeting the same component
modelComponentName="TourModeChoiceLogsumFullyJoint"  

parameters={
            "OutOfVehicleFactor": 2.0,
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
     "columns" : ["hhid", "hhinc5s", "hhzon"]
    },

    {"type" : "memory",
     "dataType" : "int",
     "name" : "HouseholdModeledData",                                     
     "columns" : ["nCars"]
    },

    {"type" : "memory",
     "dataType" : "int",
     "name" : "HouseholdPassData",                                     
     "columns" : ["mnPass", "transPass" ]
    },

	
	
    # conceived as a source of constants for vector values like dummy vars; 
    {"type" : "constants",
     "dataType" : "int",
     "name" : "Constants",
     "columns" : ["One"],
     "values" : [1]  # values are single-dimension for this data reference type
    },

    # these values come from Table1 in Tour_Mode_Choice_Documentation_01_31_12.docx
    {"type" : "constants",
     "dataType" : "double",
     "name" : "ValueOfTime",
     "columns" : ["incLt20k", "inc20_40k", "inc40_70k", "inc70_100k", "incGt100k" ],
     "values" : [
                    3.700,  # $3.70 
                    5.000,
                    6.300,
                    7.700,
                    9.000                 
                 ]  # values are single-dimension for this data reference type
    },



    {"type" : "memory",
     "dataType" : "double",
     "name" : "Tours",
     "columns" : [
                  "tourPurp",  
                  "nAdults",    # for tour dest choice logsum (partySize2, noAdults)
                  "nChildren",  # for tour dest choice logsum (partySize2, noChildren)
                  "xFtwInTour",# for tour dest choice logsum (party has at least one ftw) 
                  # the next two are simulated for us when running the destination choice model
                  # but will come directly from input data when running tour mode choice
                  "arrival",   # 
                  "departure"  # 
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




    # DerivedValues
    # this serves as a template for the logsum classes
    # a memory reference is generated for each location
    # reserve this reference for RT-related location values
    # the DataNames set is traversed to trigger calculations
    # in the ComputeLogsum method called for each O-D pair
    {"type" : "memory",
     "dataType" : "double",
     "name" : "DerivedValues",
     "columns" : ["RT Cost", "Gen Time", "RT Distance", "mix_dens destination"]
    },

    # DerivedDurableValues
    # the memory for this is allocated by the logsum code
    {"type" : "memory",
     "dataType" : "double",
     "name" : "DerivedDurableValues",
     "columns" : [
                  # these map to durables and are set from the main code:
                    "mix_dens", # 0  
                    "stops", # 1 
                    "shopTour", # 2 
                    "mealTour", # 3 
                    "incLt50k", # 4 
                    "nCars", # 5 
                    "partySize3Plus", # 6 
                    "childrenOnly", # 7 
                    "adultsOnly", # 8 
                  ]
    },




    {"type" : "dbffile",
     "name" : "Zones",
     "filename" : cube___ZONES_FILE___, 
     "columns" : ["zoneId", "mix_dens", "ret_emp", "population", "tot_emp", "term_time", "park_cost", "area", "district"]
    }
]

# Matrices are different enough to require their own structure:
from MatrixRef4Hwy4Trans import matrixReferences;

########################  model structure section  ##########################

# These values are TourMode enum values;  note that DriveAlone, DriveToTransit, and SchoolBus are not used here
altIntrinsicValues = [2,3,4,7,6]

altNames = ["SharedRide2", "SharedRide3", "WalkToTransit", "Bike", "Walk"]


logitType="NestedLogit"

# NestedLogit

# representation of Nest structure
#   [UI name, nestID, nest coeff, [alts], [nests]]
# where [alts] refers to alternatives by its order in any of the altIntrinsicValues/altNames/durableCoeffs/transientCoeffs lists
# and [nests] is a list of nestIDs

#FOR TBI is actually multinomial but since base class for logsums is nested it's easier to force a nest that degenerates to multinomial here (same nest coeff for all nests, might as well use 1)
nestList = [
            ["Root", 0, 1.0, [], [1,2,3,4,5]],
            ["SharedRide2", 1, 1.0, [0], []],
            ["SharedRide3", 1, 1.0, [1], []],
            ["WalkToTransit", 1, 1.0, [2], []],
            ["Bike", 1, 1.0, [3], []],
            ["Walk", 1, 1.0, [4], []],
           ]


                        # S2,        # S3,        # TW         # BK         # WK,       
#altSpecificConsts = [0, 0.199, -1.21, -2.79, -1.128]
#altSpecificConsts = [0, 0.361, -2.195, -2.746, -1.569]
#altSpecificConsts = [0, 0.49, -2.755, -2.588, -1.673]
#altSpecificConsts = [0, 0.553, -3.117, -2.448, -1.542]
#altSpecificConsts = [0, 0.446, -2.689, -2.568, -1.39]
#altSpecificConsts = [0, 0.412, -2.413, -2.581, -1.334]
#altSpecificConsts = [0, 0.401, -2.323, -2.589, -1.308]
#altSpecificConsts = [0, 0.397, -2.28, -2.578, -1.3]
altSpecificConsts = [0, 0.396, -2.21, -2.57, -1.294]

# Coefficients are divided into two types:
#   coefficients whose corresponding values don't change very often ('durable' values)
#   coefficients whose values are assumed to change for every iteration ('transient' values)

# In the case of logsums, the normal expectations for what is durable and what is transient are reversed
# because the logsum computations occur over all zones for a fixed person
# description of transient variables:
# some variables  are segmented by income, so those coefficients have placeholder values of 0
# Just for reference I've indicated the segmentation applied in parens e.g. (I5 means using 5 income segments)
transientCoeffs=[
    # S2,        # S3,        # TW         # BK         # WK,       
[ -0.00187748, -0.00187748, -0.00187748,  0.00000000,  0.00000000], # RT Cost
[ -0.03956349, -0.03956349, -0.03956349,  0.00000000,  0.00000000], # Gen Time
[  0.00000000,  0.00000000,  0.00000000, -0.28371673, -0.38989594], # RT Distance bike(weighted), walk (unweighted)
[  0.00000000,  0.00000000,  0.00027057,  0.00041567,  0.00041567], # dmxdens # Destination Mixed Use Density

]

# The location related values all have to be computed in the code
# so there are no mappings here
transientCoeffMap={} 


# description of durable variables:
durableCoeffs=[
    # S2,        # S3,        # TW         # BK         # WK,       
[  0.00000000,  0.00000000,  0.00079048,  0.00000000,  0.00000000], # omxdens # Origin Mixed Use Density
[  0.55982933,  0.55982933,  0.00000000,  0.00000000,  0.00000000], # hasstop # Presence of stops HT1 or HT2
[  0.29610782,  0.29610782,  0.00000000,  0.00000000,  0.00000000], # TPshp # Shop Tour
[  2.43701303,  2.43701303,  0.00000000,  0.00000000,  0.00000000], # TPeat # Meal Tour
[  0.00000000,  0.00000000,  3.83164703,  0.00000000,  1.24811195], # IncLe50 # Income <= $50K
[  0.00000000,  0.00000000,  0.00000000, -0.14154144, -0.14154144], # hhveh # Number of vehicles in HH
[  0.00000000,  0.00000000,  0.00000000,  1.16419776,  1.16419776], # PtSzG3 # Travel party size >= 3
[  0.00000000,  0.00000000,  0.00000000,  1.39050289,  1.39050289], # Chd_only # Children only travel party
[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.77753138], # NoKid # Adults only travel party
]


durableCoeffMap={
                 "DerivedDurableValues" : [[0,0,9]], #
                } 

# 
# SEGMENTATION maps to handle cases where the coefficient depends upon some segmentation of the input data,
# usually household income:
#

segmentDefinitions = [
]

segmentCoeffMap = [
]






