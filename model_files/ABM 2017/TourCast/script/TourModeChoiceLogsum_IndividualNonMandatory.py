####################################################################
####################################################################
# TourModeChoiceLogsum_IndividualNonMandatory.py
# Config script used by Tour Mode Choice and Tour Destination Choice for Individual Non-Mandatory tours
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
modelComponentName="TourModeChoiceLogsumIndNonMnd"  

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
     "datatype" : "int",
      "name" : "Persons",  # this household data is needed only to feed to the logsum; note vars noCarsInHh and nCars, while household, will be supplied by NCarsFromAA
     "columns" : [
                  "personId", 
                  "hhid",
                  "HHZON", 
                  "age",
                  "ptypeDAP",
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
     "columns" : [
                  "hhid", 
                  "hhinc5s", 
                  "hhzon", 
                  "hh1Person",
                  "hhsize",
                  "hchildren",
                  "hChild1",
				  "hChild2",
				  "hworkers"
                  ]
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
                    3.400,  # $3.40 
                    4.200,
                    4.700,
                    7.900,
                    10.000                                     
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
    # reserve this reference for RT-related location values
    # the DataNames set is traversed to trigger calculations
    # in the ComputeLogsum method called for each O-D pair
    {"type" : "memory",
     "dataType" : "double",
     "name" : "DerivedValues",
     "columns" : ["RT Cost(I5)","RT Distance","Gen Time", "tot_EmpDensity","mix_dens destination",
	 			  # Destination District constants - 
				  # to create a district constant, add the name followed by an "_" and the district number
				  # districts are defined in the zones file
					"district_1",	# 10 District 1 destination
					"district_6",	# 11 District 2 and 3 destination
					"district_2_3_7",	# 12 District 6 and 7 destination	
	 ]
    },

    # DerivedDurableValues
    # the memory for this is allocated by the logsum code
    {"type" : "memory",
     "dataType" : "int",
     "name" : "DerivedDurableValues",
     "columns" : [
                  # these map to durables and are set from the main code:
                 "noCarsInHh",	     # zeroveh # Zero-Car HH
                 "incLt50k",	     # incle50 # Inc <= $50K
                 "incGt75k",	     # ifin(hhinc,4,5) # Inc > $75K
                 "hh1Person",	 # 1per # 1 person HH
                 "hchild1",	 # hchild1 # HH number of children age 0-5
                 "hhsize2",	 # ifeq(hhsize,2) # 2 person HH
                 "isftw",	 # ftwrkr # full time 
                 "isChild2",	     # child2 # Child age 6-15
                 "male",	     # male #  
                 "ageGt35",	     # agegr35 # Age > 35
                 "ageGt55",	     # ageg55 # Age over 55
                 "isAdtStud",	 # adstud # Adult Student
                 "isSen",	     # senior #  
                 "nFjTours",	 # nfjnt # Number of Fully Joint Tours
                 "isShop",	      # TPshp # Shop Tour
                 "isPerBus",	      # TPmnt # PerBus Tour
                 "isMeal",	     # TPeat # Meal Tour
                 "isSocRec",	     # TPdsc # SocRec Tour
                 "xMealHT12",	         # hhteat # Presence of Meal Stops HT1+HT2
                 "xSRecHT12",	     # hhtdsc # Presence of SocRec stops HT1+HT2
                 "arr6Pmto12Am",	     # ifin(arrtim,18,24) # Arrival time after 6PM and before 12AM
                 "xEscStopHT12",	         # hhtchf # Presence of Chauffer Stops on HT1+HT2
                 "arr10AmTo4Pm",	         # ifin(arrtim,10,16) # Arrival Time After 10AM and Before 4PM
                 "xStopsHT12",	     # hasstop # Presence of stops on HT1 + HT2
				"autoGeWorker",#  Autos greater than / equal to workers AND autos > zero
				"autoGeDriver",#  Autos greater than / equal to drivers				 
                  ]
    },

    {"type" : "dbffile",
     "name" : "Zones",
     "filename" : cube___ZONES_FILE___,      
     "columns" : ["zoneId", "mix_dens", "totEmpDen",
                  "term_time", "park_cost", "ret_emp", "population", "tot_emp","area", "district"] # these columns are mapped by TourModeChoiceLogit
    }
]

# Matrices are different enough to require their own structure:
from MatrixRef4Hwy4Trans import matrixReferences;

########################  model structure section  ##########################

# These values are TourMode.cs enum values;  SchoolBus is not used here
altIntrinsicValues = [1,2,3,4,5,7,6]

 # DA,        # S2,        # S3,        # TW,        # TD,        # BK         # WK,       


altNames = ["Drive Alone", "Shared Ride2","Shared Ride3","Walk Transit", "Drive Transit", "Bike", "Walk"]
#altSpecificConsts = [0, 1.196, 1.901, 2.96, -3.126, -1.53, 1.54]
#altSpecificConsts = [0, -1.241, -0.64, -1.008, -5.951, -3.926, -1.044]
#altSpecificConsts = [0, -0.693, -0.007, -0.877, -5.253, -3.46, -0.153]
#altSpecificConsts = [0, -0.059, 0.655, -0.634, -4.777, -2.854, 0.537]
#altSpecificConsts = [0, 0.405, 1.11, -0.406, -4.618, -2.399, 0.869]
#altSpecificConsts = [0, 0.702, 1.408, -0.231, -4.441, -2.09, 1.038]
#altSpecificConsts = [0, 0.888, 1.592, -0.104, -4.405, -1.908, 1.131]
#altSpecificConsts = [0, 0.975, 1.675, -0.026, -4.336, -1.824, 1.172]
#altSpecificConsts = [0, 1.062, 1.761, 0.044, -4.395, -1.738, 1.212]
#altSpecificConsts = [0, 1.092, 1.793, 0.075, -3.461, -1.707, 1.227]
#					DA,  # S2,  # S3,  # TW,   # TD,   # BK   # WK,
altSpecificConsts = [0, 1.092, 1.793, 0.075, -3.061, -1.707, 1.227]

logitType="NestedLogit"

# NestedLogit

# representation of Nest structure
#   [UI name, nestID, nest coeff, [alts], [nests]]
# where [alts] refers to alternatives by its zero-based order in any of the altIntrinsicValues/altNames/durableCoeffs/transientCoeffs lists
# and [nests] is a list of nestIDs
# using this 
nestList = [
            ["Root", 0, 1.0, [], [1, 2, 3, 4]], # subnests are DA, Shared Ride, Transit, Non-Motorized
            ["Drive Alone", 1, 0.800, [0], []],  # nest is just a single alt
            ["Shared Ride", 2, 0.800, [1,2], []],  # SR2, SR3
            ["Transit", 3, 0.800, [3, 4], []],     # nest with subnests TW, TD
            ["Non-Motorized", 4, 0.800, [5, 6], []], # nest with subnests Bk, Wk
           ]


# Coefficients are divided into two types:
#   coefficients whose corresponding values don't change very often ('durable' values)
#   coefficients whose values are assumed to change for every iteration ('transient' values)

# In the case of logsums, the normal expectations for what is durable and what is transient are reversed
# because the logsum computations occur over all zones for a fixed person
# description of transient variables:
transientCoeffs=[##Note, must be in the same order as in the "DerivedValues" memory reference, as there is no map]
    # DA,        # S2,        # S3,        # TW,        # TD,        # BK         # WK, 
# O-D dependent  #using placeholder where segment mapping will occur
[  placeholder, placeholder, placeholder, placeholder, placeholder, placeholder, placeholder], # RT Cost(I5)
[ -0.00700000, -0.00700000, -0.00700000, -0.00700000, -0.00700000,  0.00000000,  0.00000000], # Gen Time
[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000, -0.27208158, -0.84485700], # RT distance (bike weighted, walk unweighted) # doc currently describes 'travel distance'; to disambiguate, is RT
# destination dependent (zonal data - in principle could preload)
[ -0.00001000,  0.00000000,  0.00000000,  0.00004000,  0.00000180,  0.00000000,  0.00000000], # Employment Density at Destination
[  0.00000000,  0.00000000,  0.00000000,  0.00069921,  0.00000000,  0.00056758,  0.00054258], # dmxdens # Mixed Density at Destination
[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # district 1 destination
[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # district 6 destination
[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # district 2, 3, 7 destination
]
#[  0.00000000,  0.00000000,  0.00000000,  0.75000000,  0.50000000,  0.00000000,  0.00000000], # district 1 destination
#[  0.00000000,  0.00000000,  0.00000000,  0.25000000,  0.10000000,  0.00000000,  0.00000000], # district 6 destination
#[  0.00000000,  0.00000000,  0.00000000, -0.25000000, -0.10000000,  0.00000000,  0.00000000], # district 2, 3, 7 destination

# The location related values all have to be computed in the code
# so there are no mappings here
transientCoeffMap={} 


# description of durable variables:
durableCoeffs=[
    # DA,        # S2,        # S3,        # TW,        # TD,        # BK         # WK, 
#hh
[  0.00000000,  2.09870884,  2.09870884,  0.00000000,  0.00000000,  3.03455379,  3.03455379], # 00 zeroveh # Zero-Car HH
[ -0.43760131,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 01 incle50 # Inc <= $50K
[  0.00000000,  0.22108612,  0.22108612,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 02 ifin(hhinc,4,5) # Inc > $75K
[  0.00000000, -1.18148769, -1.29479841,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 03 1per # 1 person HH
[  0.00000000,  0.68283862,  0.82660964,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 04 hchild1 # HH number of children age 0-5
[  0.00000000,  0.00000000, -0.49112738,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 05 ifeq(hhsize,2) # 2 person HH
                                                                                                
#person                                                                                         
[  0.51658168,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 06 ftwrkr # full time
[  0.00000000,  3.25116193,  3.25116193,  0.00000000,  0.00000000,  4.08538342,  0.00000000], # 07 child2 # Child age 6-15
[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.71495095,  0.00000000], # 08 male #  
[  0.33935106,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 09 agegr35 # Age > 35
[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000, -1.22356930,  0.00000000], # 10 ageg55 # Age over 55
[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.91974820,  0.00000000], # 11 adstud # Adult Student
[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000, -1.19892332], # 12 senior #  
[  0.00000000,  0.00000000,  0.00000000,  0.70682343,  0.00000000,  0.00000000,  0.00000000], # 13 nfjnt # Number of Fully Joint Tours
                                                                                                 
#tour                                                                                           
[  1.35215888,  0.00000000,  0.00000000, -0.08203708, -0.08203708,  0.00000000,  0.00000000], # 14 TPshp # Shop Tour
[  1.56052593,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 15 TPmnt # PerBus Tour
[  0.00000000,  0.00000000,  0.00000000, -1.98913392, -1.98913392,  0.00000000,  0.00000000], # 16 TPeat # Meal Tour
[  0.00000000, -0.99672635, -0.99672635, -2.94175279, -2.94175279,  0.00000000,  0.00000000], # 17 TPdsc # SocRec Tour
[  0.00000000,  1.05581701,  1.05581701,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 18 hhteat # Presence of Meal Stops HT1+HT2
[  0.00000000,  0.55461742,  0.55461742,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 19 hhtdsc # Presence of SocRec stops HT1+HT2
[  0.00000000,  0.60585174,  0.87576631,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 20 ifin(arrtim,18,24) # Arrival time after 6PM and before 12AM
[  0.00000000,  3.55437989,  3.55437989,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 21 hhtchf # Presence of Chauffer Stops on HT1+HT2
[  0.00000000,  0.00000000, -0.08726364,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 22 ifin(arrtim,10,16) # Arrival Time After 10AM and Before 4PM
[0.2, 0, -0.2, -0.63822804, -1.03822804, -0.40755125, -1.40755125], # 23 hasstop # Presence of stops on HT1 + HT2

# Added during calibration
[  1.50000000,  0.00000000,  0.00000000, -2.00000000,  0.00000000,  0.00000000,  0.00000000], # 24 Vehicles greater than / equal to workers AND autos > zero
[  1.50000000,  0.00000000,  0.00000000, -5.00000000,  0.00000000,  0.00000000,  0.00000000], # 25 Vehicles greater than / equal to  Drivers
[ placeholder ] * 7 # 26 Income Specific Constants
]


# durableCoeffMap={"table name": [[tableColIndex, matchingCoeffVectorStartIndex, numberOfConsecutiveColumnsToMatch],...]}
durableCoeffMap={
                 "DerivedDurableValues" : [[0,0,26]],
                 "Constants" : [[0,26,1]],
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
 {'Name': '5 Income Segments', 'DataRef': 'HouseholdBaseData','Offset': 1, 'DataRange': [incLt25k, inc25To50k, inc50To75k, inc75To100k, incGt100k]}
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
{'Segment': 0, 'Vector': 'transient', 'Offset': 0,  # RT Cost
  'Coefficients':
    [#    0-25k  25-50  50-75  75-100  >100k
        [ -0.00160928, -0.00130214, -0.00099380, -0.00088908, -0.00059630], # DA   
        [ -0.00160928, -0.00130214, -0.00099380, -0.00088908, -0.00059630], # S2
        [ -0.00160928, -0.00130214, -0.00099380, -0.00088908, -0.00059630], # S3
        [ -0.00160928, -0.00130214, -0.00099380, -0.00088908, -0.00059630], # TW
        [ -0.00160928, -0.00130214, -0.00099380, -0.00088908, -0.00059630], # TD
        [  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # BK
        [  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # WK
    ]
},

{'Segment': 0, 'Vector': 'durable', 'Offset': 26,  # Constant
  'Coefficients':
    [ # normally 1 row that applies to every alternative; it's possible that there may be alternative-specific-variables that are affected by segmentation
      # in that case there would be as many rows as alternatives; I suspect this would never apply to a case with a very large alternative set
        #coeff when segment value is 0, 1, 2, 3, 4 respectively
			# INC0        # INC1       # INC2       # INC3       # INC4
		[ 0, 	0, 	0, 	0, 	0], #  DriveAlone
		[ 0, 	0, 	0, 	0, 	0], #  SharedRide2
		[ 0, 	0, 	0, 	0, 	0], #  SharedRide3
		[ 4.5, 	.5, 	0, 	0, 	0], #  WalkToTransit
		[ 0, 	0, 	0, 	0, 	0], #  DriveToTransit
		[ 0.5, 	0, 	0, 	0, 	0], #  Bike
		[ 0, 	0, 	0, 	0, 	0], #  Walk

    ]
}
]






