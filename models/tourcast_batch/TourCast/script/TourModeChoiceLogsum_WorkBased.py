####################################################################
# TourModeChoiceLogsum_WorkBased.py
# Config script for school logsum variant of TourModeChoice
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
modelComponentName="TourModeChoiceLogsumWorkBased"  

parameters={
            "OutOfVehicleFactor": 2.5,
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

    # hh modeled not needed for work-based
    #{"type" : "memory",
    # "dataType" : "int",
    # "name" : "HouseholdModeledData",                                     
    # "columns" : ["nCars"]
    #},

    {"type" : "memory",
     "dataType" : "int",
     "name" : "HouseholdPassData",                                     
     "columns" : ["mnPass", "transPass" ]
    },

	

    # NOTE: the logsum was initially developed for usual workplace where we were iterating over persons
    # here we will be iterating over tours;  the person data here will come from the tours and households;
    {"type" : "memory",
     "dataType" : "int",
     "name" : "Persons",
     "columns" : [

                  "age",  # for DA eligibility when applicable
                  "ptypeDAP" # for isSen
                 ]
    },

    # conceived as a source of constants for vector values like dummy vars; 
    {"type" : "constants",
     "dataType" : "int",
     "name" : "Constants",
     "columns" : ["One"],
     "values" : [1] 
    },

    # these values come from Table1 in Tour_Mode_Choice_Documentation_01_31_12.docx
    {"type" : "constants",
     "dataType" : "double",
     "name" : "ValueOfTime",
     "columns" : ["incLt20k", "inc20_40k", "inc40_70k", "inc70_100k", "incGt100k" ],
     "values" : [
                    5.6,  
                    6.3,
                    7.0,
                    7.7,
                    8.4                 
                 ]  
    },


    {"type" : "memory",
     "dataType" : "double",
     "name" : "Tours",
     "columns" : [   
                  "tourPurp",  
                  "parentMode",
                  "origZoneId", 
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
     "columns" : [  
                  "RT Cost", 
                  "Gen Time", 
                  "RT Distance",
                  "mix_dens destination",  
                  ]
    },

    # DerivedDurableValues
    # this is self-contained in the logsum
    {"type" : "memory",
     "dataType" : "int",
     "name" : "DerivedDurableValues",
     "columns" : [  
					"ageGt35",# agegr35 # Age >= 35
					"isPerBusTour",# TPmnt # PerBus Tour
					"isWorkTour",# TPwrk # Work Tour
					"isMealTour",# TPeat # Meal Tour
					"xStopsHt12"# hasstop # Presence of stops HT1 or HT2
                  ]

    },

     #(could eliminate ret_emp column)
    {"type" : "dbffile",
     "name" : "Zones",
     "filename" : cube___ZONES_FILE___, 
     "columns" : ["zoneId", "mix_dens", "ret_emp", "population", "tot_emp", "term_time", "park_cost", "area", "district"]
    }
]

# Matrices are different enough to require their own structure:
from MatrixRef4Hwy4Trans import matrixReferences;

########################  model structure section  ##########################

# These values are TourMode enum values;  note that DriveToTransit, Bike, and SchoolBus are not used here
altIntrinsicValues = [1,2,3,4,7,6] 

altNames = ["DriveAlone", "SharedRide2", "SharedRide3", "WalkToTransit", "Walk", "Bike"] 

logitType="NestedLogit"

# NestedLogit

# representation of Nest structure
#   [UI name, nestID, nest coeff, [alt indices], [nest indices]]
# where [alts] refers to alternatives by its order in any of the altIntrinsicValues/altNames/durableCoeffs/transientCoeffs lists
# and [nests] is a list of nestIDs
# using this 
nestList = [  
            ["Root", 0, 1.0, [], [1, 2, 3]],
            ["Auto", 1, 0.8, [0, 1, 2], []],
            ["Transit", 2, 0.8, [3], []],
            ["Non-Motorized", 3, 0.8, [4, 5], []]
           ]


		   				# DA,        # S2,        # S3,        # TW         # BK         # WK,       
#altSpecificConsts = [  0.00000000, -2.79342967, -2.73545303, -1.87923189, -5.00000000,  1.30221141] # constants
#altSpecificConsts = [  0.00000000, -2.693, -2.638, -1.75923189, -4.88, 1.93] # constants
#altSpecificConsts = [  0.00000000, -2.786, -2.713, -1.81423189, -4.935, 1.686] # constants
#altSpecificConsts = [  0.00000000, -2.698, -2.629, -1.77923189, -4.835, 2.182] # constants
#altSpecificConsts = [  0.00000000, -2.683, -2.607, -1.84823189, -4.804, 2.36] # constants
#altSpecificConsts = [  0.00000000, -2.683, -2.607, -1.84823189, -4.78, 2.44] # constants
#altSpecificConsts = [  0.00000000, -2.685, -2.603, -1.84023189, -4.772, 2.55] # constants
#altSpecificConsts = [  0.00000000, -2.669, -2.596, -1.95223189, -4.884, 2.118] # constants
#altSpecificConsts = [  0.00000000, -2.671, -2.598, -2.03723189, -4.969, 1.79] # constants
#altSpecificConsts = [  0.00000000, -2.681, -2.599, -2.16223189, -5.094, 0.928] # constants
#altSpecificConsts = [  0.00000000, -2.695, -2.644, -2.36123189, -5.293, 0.285] # constants
#altSpecificConsts = [  0.00000000, -2.705, -2.632, -2.307, -5.725, 0.638] # constants
#altSpecificConsts = [  0.00000000, -2.658, -2.608, -2.411, -5.96, 0.473] # constants
#altSpecificConsts = [  0.00000000, -2.787, -2.653, -2.59, -5.97, 0.389] # constants
#altSpecificConsts = [  0.00000000, -2.436, -2.465, -2.646, -6.767, -0.402] # constants
#altSpecificConsts = [  0.00000000, -2.89, -2.729, -3.001, -7.177, -1.115] # constants
#altSpecificConsts = [  0.00000000, -2.551, -2.596, -2.923, -7.337, -1.472] # constants
#altSpecificConsts = [  0.00000000, -2.814, -2.655, -3.208, -7.524, -1.838] # constants
#altSpecificConsts = [  0.00000000, -2.613, -2.65, -3.202, -7.587, -2.044] # constants
#altSpecificConsts = [  0.00000000, -2.772, -2.625, -3.224, -7.603, -1.955] # constants
#altSpecificConsts = [  0.00000000, -2.659, -2.673, -3.204, -7.605, -1.884] # constants
#altSpecificConsts = [  0.00000000, -2.7155, -2.649, -3.214, -7.604, -1.9195] # constants
#altSpecificConsts = [  0.00000000, -2.666, -2.63, -3.349, -7.739, -2.54] # constants
#altSpecificConsts = [  0.00000000, -2.797, -2.694, -3.214, -7.604, -3.025] # constants
#altSpecificConsts = [  0.00000000, -2.289, -2.462, -3.214, -7.604, -4.378] # constants
#altSpecificConsts = [  0.00000000, -2.289, -2.462, -3.214, -7.604, -4.778] # constants
altSpecificConsts = [  0.00000000, -3.055, -2.726, -3.214, -7.604, -5.234] # constants



# Coefficients are divided into two types:
#   coefficients whose corresponding values don't change very often ('durable' values)
#   coefficients whose values are assumed to change for every iteration ('transient' values)

# In the case of logsums, the normal expectations for what is durable and what is transient are reversed
# because the logsum computations occur over all zones for a fixed person
# description of transient variables:
# some variables  are segmented by income, so those coefficients have placeholder values of 0
# Just for reference I've indicated the segmentation applied in parens e.g. (I5 means using 5 income segments)
transientCoeffs=[
 # DA,        # S2,        # S3,        # TW         # BK         # WK,       
[ -0.00098890, -0.00098890, -0.00098890, -0.00098890,  0.00000000,  0.00000000], # cost
[ -0.02000000, -0.02000000, -0.02000000, -0.02000000,  0.00000000,  0.00000000], # Gen Time
[  0.00000000,  0.00000000,  0.00000000,  0.00000000, -0.38000000, -1.78696323], # RT Distance # Walk(unweighted), Bike (weighted)
[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00068890,  0.0048890], # mx dens dest # Destination Mixed Use Density
]
#[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00068890,  0.00068890], # mx dens dest # Destination Mixed Use Density
#[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00048890,  0.00048890], # mx dens dest # Destination Mixed Use Density

# The location related values all have to be computed in the code
# so there are no mappings here
transientCoeffMap={} 


# description of durable variables:
durableCoeffs=[  
 # DA,        # S2,        # S3,        # TW         # BK         # WK,       
#person
[0.00000000,  0.00000000,  0.00000000, -0.50571478, -0.50571478, -0.50571478], # agegr35 # Age >= 35
#tour
[0.71106711,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # TPmnt # PerBus Tour
[2.10624230,  2.87376489,  2.87376489,  0.00000000,  0.00000000,  0.00000000], # TPwrk # Work Tour
[0.00000000,  1.45276350,  1.94480894,  0.00000000,  0.00000000,  0.00000000], # TPeat # Meal Tour
[0.00000000,  0.00000000,  0.00000000, -2.86074313, -2.86074313, -2.86074313], # hasstop # Presence of stops HT1 or HT2
[placeholder, placeholder, placeholder, placeholder, placeholder, placeholder], # parent tour segmentation

]


durableCoeffMap={
                 "DerivedDurableValues" : [[0,0, 5]], # all in 
				 "Constants" : [[0,5,1]], # dummy for parent tour segment
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
 {'Name': 'Parent Tour Mode', 'DataRef': 'Tours','Offset': 1, 'DataRange': [modeDA,modeSR2,modeSR3,modeTW,modeTD,modeBK, modeWK]}  # school bus not a valid work tour mode
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
{'Segment': 0, 'Vector': 'durable', 'Offset': 5,  # Parent tour mode
  'Coefficients':
    [
# 	one row for each alternative	
 #  parent tour DA,        # S2,        # S3,        # TW        # TD         # BK         # WK,       
			[0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # DA segmented by parent tour mode
			[0.00000000,  0.76594057,  0.76594057,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # S2
			[0.00000000,  0.00000000,  0.99713816,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # S3
			[0.00000000,  0.00000000,  0.00000000,  5.42439248,  5.42439248,  5.42439248,  5.42439248], # TW 
			[0.00000000,  0.48315843,  0.48315843,  4.69216246,  4.69216246,  10.99216246, 4.69216246], #Bk
			[0.00000000,  0.48315843,  0.48315843,  4.69216246,  4.69216246,  4.69216246,  4.69216246], #Wk
    ]
},
]





