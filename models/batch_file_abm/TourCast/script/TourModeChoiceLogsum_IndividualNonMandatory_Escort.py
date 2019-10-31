####################################################################
# TourModeChoiceLogsum_IndividualNonMandatory_Escort.py
# used by TourDestinationChoice for IndividualNonMandatoryEscort
# and by TourModeChoice for both Individual non-mandatory Escort tours and for School Escort tours
# To delineate the following:
#   Input/ouputu data sources 
#   Set of alternatives
#   Logit type
#   Utility function coefficients
#   mapping inputs to coefficients
####################################################################

from Globals import * # for numberOfZones, placeholder, purposeXxxx, incXxxx

# the name of the corresponding class on the C# side:
# this allows for multiple scripts targeting the same component
modelComponentName="TourModeChoiceLogsumINMEscort"  

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
     "datatype" : "int",
      "name" : "Persons",  #gv removed ptype(2) not needed
     "columns" : [
                  "personId", 
                  "hhid",
                  "HHZON", 
                  "age",
                  "gender"
                  ]
    },
        
    {"type" : "memory",
     "dataType" : "int",
     "name" : "PersonsModeledData",
     "columns" : [
                "personId",
                "hhId",
                "homeZoneId",
                "DAPId",
                ]
    },

    {"type" : "memory",
     "dataType" : "int",
     "name" : "HouseholdBaseData",                                     
     "columns" : ["hhid", "hhinc5s", "hhzon", "hh1Person","hhsize","hchildren"]
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
                    3.000,  # $3.00 
                    4.100,
                    5.300,
                    6.400,
                    7.500                                     
                 ]  # values are single-dimension for this data reference type
    },
    {"type" : "memory",
     "dataType" : "double",
     "name" : "Tours",
     "columns" : [
                  "personId", 
                  "tourId",   
                  "tourPurp", 
                  "homeZoneId",
                  # the next two are simulated for us when running the destination choice model
                  # but will come directly from input data when running tour mode choice
                  "arrival",   # 24hr time since midnight (e.g. 0.5 = 12:30 am)
                  "departure", # 
                  "nEscOut",   # number of escorted children on outbound half tour
                  "nEscIn"     # number of escorted children on return half tour

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
    # reserve this reference for RT-related location values
    # the DataNames set is traversed to trigger calculations
    # in the ComputeLogsum method called for each O-D pair
    {"type" : "memory",
     "dataType" : "double",
     "name" : "DerivedValues",
     "columns" : ["RT Distance", "RT Cost(I5)","Gen Time", "mix dens OD" ]
    },

    # DerivedDurableValues
    # the memory for this is allocated by the logsum code
    {"type" : "memory",
     "dataType" : "int",
     "name" : "DerivedDurableValues",
     "columns" : [
                  # these map to durables and are set from the main code:
                    "nCars",  # Number of vehicles in HH
                    "hhsize2",  # 2 person HH
                    "nSchEsc",  # Number of children escorted to school
                    "ageLt35",  # Age <= 35 years
                    "schEscortTour",  # School escort tour
                    "xStopsHT12"  # Presence of stops HT1 or HT2
                  ]
    },

    {"type" : "dbffile",
     "name" : "Zones",
     "filename" : cube___ZONES_FILE___, 
     "columns" : ["zoneId", "mix_dens", "ret_emp", "population", "tot_emp", "term_time", "park_cost","area", "district"]
    }
]

# Matrices are different enough to require their own structure:
from MatrixRef4Hwy4Trans import matrixReferences;

########################  model structure section  ##########################

# These values are TourMode.cs enum values;  note that DriveAlone, DriveToTransit, and SchoolBus are not used here
altIntrinsicValues = [2,3,7,6]
#altNames = ["Shared Ride2","Shared Ride3","Bike", "Walk"]
altNames = ["S2","S3","BK", "WK"]
                        # S2,        # S3,        # BK         # WK,       
altSpecificConsts = [0, -0.928, -1.797, 0.919]

# for tbi is actually multinomial but we will use degenerate nest
logitType="NestedLogit"

# NestedLogit

# representation of Nest structure
#   [UI name, nestID, nest coeff, [alts], [nests]]
# where [alts] refers to alternatives by its order in any of the altIntrinsicValues/altNames/durableCoeffs/transientCoeffs lists
# and [nests] is a list of nestIDs
# using this 
# really is multinomial, but due to inheritance hieararchy at the moment, use a degenerate nest:
# this does NOT work with our framework, though in principle it should:
# nestList = [
#            ["Root", 0, 1.0, [0,1,2,3], []], # degenerate multinomial logit
#           ]
# instead use this:
nestList = [
            ["Root", 0, 1.0, [], [1, 2, 3, 4]], # a subnest for each alternative
            ["SR2", 1, 1.0, [0], []], # nest with subnests SR2
            ["SR3", 2, 1.0, [1], []], # nest with subnests SR3
            ["Bike", 3, 1.0, [2], []], # nest with subnests Bk
            ["Walk", 4, 1.0, [3], []], # nest with subnests Wk
           ]



# Coefficients are divided into two types:
#   coefficients whose corresponding values don't change very often ('durable' values)
#   coefficients whose values are assumed to change for every iteration ('transient' values)

# In the case of logsums, the normal expectations for what is durable and what is transient are reversed
# because the logsum computations occur over all zones for a fixed person
# description of transient variables:
transientCoeffs=[##Note, must be in the same order as in the "DerivedValues" memory reference, as there is no map

 # S2,        # S3,        # BK         # WK,       
[  0.00000000,  0.00000000, -0.26501387, -0.61916813], # bk_dist # Bike Distance (weighted), walk distance unweighted
[ -0.00088014, -0.00088014,  0.00000000,  0.00000000], # cost
[ -0.02000000, -0.02000000,  0.00000000,  0.00000000], # time
[  0.00000000,  0.00000000,  0.00033808,  0.00012335], # mxdens # Mixed Density at Origin + Mixed Density at Destination
]

# The location related values all have to be computed in the code
# so there are no mappings here
transientCoeffMap={} 


# description of durable variables:
durableCoeffs=[
[  0.75221786,  0.75221786,  0.00000000,  0.00000000], # hhveh # Number of vehicles in HH
#[  0.00000000,  0.24850467,  0.00000000,  0.00000000], # 2per # 2 person HH
[  0.00000000,  0,  0.00000000,  0.00000000], # 2per # 2 person HH
[  0.00000000,  0.71103619,  0.00000000,  0.00000000], # nSchEsc # Number of children escorted to school
[  0.00000000,  0.00000000,  1.58175972,  1.58175972], # agel35 # Age <= 35 years
[  0.00000000,  2.05075753,  0.00000000,  0.00000000], # pr_sch # School escort tour
[  0.00000000,  0.00000000, -2.15643076, -2.15643076], # hasstop # Presence of stops HT1 or HT2
]

durableCoeffMap={
                 "DerivedDurableValues" : [[0,0,6]],
                } 

#no segmentation here
#segmentDefinitions = [
#]

#segmentCoeffMap = [
#]






