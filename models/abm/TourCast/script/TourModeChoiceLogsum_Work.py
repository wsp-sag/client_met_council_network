####################################################################
# WorkTourModeChoiceLogsum.py
# This file, originally from UsualWorkplaceTourModeChoiceLogsumTest.py, 
#  has commented-out that we need to enable:
# STILL TODO:  uncomment data marked (skip for workplace loc logsum) 
# DONE: use the commented-out altSpecificConsts
# STILL TODO: will need to do some mapping of the newly enabled data

####################################################################

from Globals import * 

# the name of the corresponding class on the C# side:
# this allows for multiple scripts targeting the same component
modelComponentName="WorkTourModeChoiceLogsum"  

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

    # some hh-related data is in the tour file, some in the 
    {"type" : "memory",
     "dataType" : "int",
     "name" : "HouseholdBaseData",                                     
     #              0       1          2          3        4            5         6         
     "columns" : ["hhzon", "hhid", "hhinc5s", "hhsize", "hh1person", "hWorkers", "hChildren", "hChild1", "hChild2"],
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

    # NOTE: the logsum was initially developed for usual workplace where we were iterating over persons
    # here we will be iterating over tours;  the person data here will come from the tours and households;
    {"type" : "memory",
     "dataType" : "int",
     "name" : "Persons",
     "columns" : ["personid",   # 0 
                  "hhid",       # 1
                  "ptypeDAP", # 2 for location set segmentation (segmentation in coeff array, not segmentDefinitions); also for logsum
                  "age",        # 3 for deriving 'age < 30'
                  "gender",       # 4 
                  ]
    },

    # don't quite know what tours and half tours will fully look like
    # for now let tour destination choice fill these 3 memory arrays (allocate and set memory values)
    {"type" : "memory",
     "name" : "Tours",
     "columns" : [
                  "arrival",
                  "departure", 
                  "nTours",
                  "nWorkTours",
                  "nEscIn",     # number of escorted children on return half tour
                  "nEscOut"     # number of escorted children on outbound half tour

                  ]
    },

    {"type" : "memory",
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

    # conceived as a source of constants for vector values like dummy vars; 
    {"type" : "constants",
     "name" : "Constants",
     "columns" : ["One"],
     "values" : [1]  # values are single-dimension for this data reference type
    },

    # DerivedValues; for logsums this is just a specification of a column set, 
	# this must exactly match the order of the rows in the transientCoeffs array
    # a separate memory array of columns.length is generated for each alternative in code
	# the names trigger methods in the code to calculate each quantity
    {"type" : "memory",
     "name" : "DerivedValues",
     "columns" : [
                  # these map to transients (and are set in the logsum code because we need to recalc for each zone; 				  
                  # the point of this is that we can at least set the mappings to the coefficients in this file)
                  "RT Cost(I5)",                  # 1
                  "Gen Time",                     # 2
				  "transfers",                    # 3
                  "transitWaitLT10Mins",          # 4
                  "transitWaitLT20Mins",          # 5
				  "RT Distance",                  # 6
                  "retail density dest",          # 7
                  "pop density dest",             # 8
                  "total employment density dest", # 9
				  # Destination District constants - 
				  # to create a district constant, add the name followed by an "_" and the district number
				  # districts are defined in the zones file
					"district_1",	# 10 District 1 destination
					"district_2_3_7",	# 11 District 2,3,7 destination
					"district_6",	# 12 District 6 destination				  
                  ]
    },

    # DerivedDurableValues
    {"type" : "memory",
     "name" : "DerivedDurableValues",
     "columns" : [
			"hworkers",# 00 workers #  	 
			"hchildren",# 01 children # Number of children	 
			"nCars",# 02 hhveh # HH number of vehicles	  
			"incLt50k",# 03 incle50 # Income < $50K	 
			"incGt75k",# 04 incge75 # Income > $75K	 
			"ageGt35",# 05 agegr35 # Age > 35 years	 
			"ageGt65",# 06 agegr65 # Age > 65 years	 
			"male",# 07 male #  	 
			"nMndStopsHt12",# 08 ht12man # Number of mandatory stops	 
			"nNMStopsHt12",# 09 ht12nonman # Number of non-mandatory stops	 
			"arrivalAM",# 10 arv_am # Arrival Time between 7 am & 9 am	 
			"returnPM",# 11 ret_pm # Return Time between 4 pm & 6 pm	 
			"mixDensOrigin",# 12 omxdens # Mixed density at origin                  
			"totEmpDensOrigin",# 13 oemp_den # Total Employment Density at Origin                  
			"autoGeWorker",# 14 Autos greater than / equal to workers AND autos > zero
			"autoGeDriver",# 15 Autos greater than / equal to drivers
			]                
    },

    {"type" : "dbffile",
     "name" : "Zones",
     "filename" : cube___ZONES_FILE___, 
     "columns" : ["zoneId", "mix_dens", "ret_emp", "population", "tot_emp", "term_time", "park_cost","area", "totEmpDen", "district"]
    }
]

from MatrixRef4Hwy4Trans import matrixReferences


########################  model structure section  ##########################

# Values are those of C# TourMode enum 
altIntrinsicValues = [1, 2, 3, 4, 5, 7, 6]

# updated from school for work tours
altNames = ["DA", "S2", "S3", "TW", "TD", "BK", "WK"]

logitType="NestedLogit"

# NestedLogit

# ASCII representation of nesting structure

#   [UI name, nestID, nest coeff, [alts], [nests]]
# where [alts] refers to alternatives by its order in any of the altIntrinsicValues/altNames/durableCoeffs/transientCoeffs lists
# and [nests] is a list of nestIDs
# updated for TBI
nestList = [
            ["Root", 0, 1.0, [], [1, 2, 3, 4]],    # subnests are DA, Shared Ride, Transit, Non-Motorized
            ["Drive Alone", 1, 0.8, [0], []],     # nest alt  is DA
            ["Shared Ride", 2, 0.8, [1, 2], []],  # nest alts are SR2, SR3			
            ["Transit", 3, 0.8, [3, 4], []],      # nest alts TW, TD
            ["Non-Motorized", 4, 0.8, [5, 6], []] # nest alts BK, WK
           ]

#TBI
#altSpecificConsts = [0, -2.888, -2.592, 0.822, -2.729, 0.252, 2.562]
#altSpecificConsts = [0, -4.188, -3.902, -1.13, -5.452, -1.07, 1.137]
#altSpecificConsts = [0, -3.941, -3.658, -0.821, -4.572, -0.74, 1.527]
#altSpecificConsts = [0, -3.729, -3.447, -0.579, -4.158, -0.502, 1.803]
#altSpecificConsts = [0, -3.553, -3.27, -0.39, -3.928, -0.326, 2]
#altSpecificConsts = [0, -3.265, -2.981, -0.096, -3.618, -0.068, 2.284]
#altSpecificConsts = [0, -3.087, -2.804, 0.052, -3.5, 0.062, 2.414]
#altSpecificConsts = [0, -2.989, -2.701, 0.131, -3.425, 0.13, 2.477]
#altSpecificConsts = [0, -2.932, -2.645, 0.177, -3.387, 0.164, 2.509] #n+9
#altSpecificConsts = [0, -3.901, -2.615, 0.198, -3.358, 0.185, 2.526]
#altSpecificConsts = [0, -2.932, -2.645, 0.157, -3.487, 0.164, 2.509] #m+9 chnaged time constant
#altSpecificConsts = [0, -2.932, -2.645, 0.098, -3.087, 0.164, 2.509] #m+10 adjust constants for less WT more DT
#altSpecificConsts = [0, -2.932, -2.645, 0.048, -2.787, 0.164, 2.509] #m+11 adjust constants for less WT more DT
#altSpecificConsts = [0, -2.932, -2.645, 0.000, -2.787, 0.164, 2.509] #m+12 adjust constants for less WT more DT
#altSpecificConsts = [0, -2.932, -2.645, -0.075, -2.807, 0.164, 2.509] #m+12 adjust constants for less WT more DT
#                   DA,     S2,     S3,     TW,     TD,    BK,    WK
#altSpecificConsts = [0, -2.932, -2.645, -0.475, -2.407, 0.164, 2.509] #m+14 adjust constants for less WT more DT
#altSpecificConsts = [0, -2.932, -2.645, -0.275, -2.407, 0.164, 2.509] #m+15
#altSpecificConsts = [0, -2.932, -2.645, -0.225, -2.407, 0.164, 2.509] #m+16
#altSpecificConsts = [0, -2.932, -2.645, -0.200, -2.507, 0.164, 2.509] #m+17
#altSpecificConsts = [0, -2.932, -2.645, -0.225, -2.407, 0.164, 2.509] #m+16
#altSpecificConsts = [0, -2.932, -2.645, -0.225, -2.007, 0.164, 2.509] #m+19
#altSpecificConsts = [0, -2.932, -2.645, -0.250, -2.407, 0.164, 2.509] #l+1
#altSpecificConsts = [0, -2.932, -2.645, -0.250, -2.557, 0.164, 2.509] #l+2
#altSpecificConsts = [0, -2.932, -2.645, -0.250, -2.657, 0.164, 2.509] #l+3
#altSpecificConsts = [0, -2.932, -2.645, -0.300, -2.957, 0.164, 2.509] #l+4
#altSpecificConsts = [0, -2.932, -2.645, -0.400, -3.257, 0.164, 2.509] #l+5
altSpecificConsts = [0, -2.932, -2.645, -0.300, -2.557, 0.164, 2.509] #l+6



# Coefficients are divided into two types:
#   coefficients whose corresponding values don't change very often ('durable' values)
#   coefficients whose values are assumed to change for every iteration ('transient' values)

# In the case of logsums, the normal expectations for what is durable and what is transient are reversed
# because the logsum computations occur over all zones for a fixed person
# for logsums, transientCoeffs should contain all skim-related variables, plus all destination-only related variables 
transientCoeffs=[
   # DA,        # S2,        # S3,        # TW,        # TD,        # BK         # WK,       
# skim   
[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # travel cost [ income segmented]
[ -0.00876907, -0.00876907, -0.00876907, -0.00776907, -0.00776907,  0.00000000,  0.00000000], # time
[  0.00000000,  0.00000000,  0.00000000, -0.23503976, -0.23503976,  0.00000000,  0.00000000], # xfers_tr  from skim
[  0.00000000,  0.00000000,  0.00000000,  0.47023458,  0.69262819,  0.00000000,  0.00000000], # WTHF10 # WT: OB Wait<10 mins; IB Wait < 10 mins
[  0.00000000,  0.00000000,  0.00000000,  0.39106252,  0.00000000,  0.00000000,  0.00000000], # WTHF20 # WT: OB Wait-10-20 mins; IB Wait- 10-20 mins
[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000, -0.14508584, -0.57247939], # RT distance (bike weighted, walk unweighted
# destination-related (non-skim); these can be loaded outside loop one time.
[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00003746,  0.00000000,  0.00000000], # ret_den # Retail Density at Destination
[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00008751,  0.00000000], # dpopden # Population density at destination
[ -0.00001200, -0.00000550, -0.00000550,  0.00000000,  0.00000000,  0.00000000,  0.00000109], # demp_den # Total Employment Density at Destination
[  0.00000000,  0.00000000,  0.00000000,  1.80000000,  1.50000000,  0.00000000,  0.00000000], # district 1 destination - Minneapolis core
[  0.00000000,  0.00000000,  0.00000000, -1.40000000, -0.50000000,  0.00000000,  0.00000000], # district 2, 3, 7 destination - west of Minneapolis core
[  0.00000000,  0.00000000,  0.00000000, -0.30000000,  0.10000000,  0.00000000,  0.00000000], # district 6 destination - St. Paul
]

# we need a map from the inputs to the locations in the lists
# It's easier to devise a notation if the order of data columns matches up with a range of the coefficients
# durableCoeffMap={"table name": [[tableColIndex, matchingCoeffVectorStartIndex, numberOfConsecutiveColumnsToMatch],...]}
# The skim related values all have to be computed in the code
transientCoeffMap={} #"DerivedValues": [[0,0,7]] }  # this is unused; just here to note that 
# there is a relationship between the DerivedValues data reference and the row order in the transient coeffs above
# in fact a MemoryDataReference based on the DerivedValues spec above is created for each alternative
#(essentially for each column of coeffs in the transientCoeffs above)

# for logsums, durables are all non- O-D variables;
durableCoeffs=[
   # DA,        # S2,        # S3,        # TW,        # TD,        # BK         # WK,    
# hh
[  0.00000000,  0.94338708,  0.94338708,  0.82980017,  0.82980017,  0.67534206,  0.67534206], # 00 workers #  
[  0.00000000,  0.42441007,  0.52561135,  0.33049329,  0.33049329,  0.19347737,  0.19347737], # 01 children # Number of children
[0, -0.67165688, -0.72398881, -1.21854892, -0.8053108, -1.21020354, -1.21020354], # 02 hhveh # HH number of vehicles
[  0.00000000, -0.09573392, -0.09573392,  0.77764779, -0.85022050,  0.00000000,  0.00000000], # 03 incle50 # Income < $50K
[  0.00000000,  0.36789922,  0.36789922,  0.00000000,  0.08832096,  0.00000000, -1.19000659], # 04 incge75 # Income > $75K
                                                                                                
# person
[  0.00000000,  0.00000000,  0.00000000, -0.52253064,  0.00000000, -1.05748321, -0.12732174], # 05 agegr35 # Age > 35 years
[  1.00091281,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 06 agegr65 # Age > 65 years
[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.55934559,  0.55934559], # 07 male #  

# tour
[  1.14886837,  1.34100033,  1.34100033,  0.93855706,  0.93855706,  0.00000000, -0.50000000], # 08 ht12man # Number of mandatory stops
[  0.40437388,  1.50090835,  1.50090835,  0.73327475,  0.73327475,  0.00000000, -0.50000000], # 09 ht12nonman # Number of non-mandatory stops
[  0.00000000,  0.49381757,  0.38824448,  0.70921703,  0.75396574,  0.00000000,  0.00000000], # 10 arv_am # Arrival Time between 7 am & 9 am
[  0.00000000,  0.00000000,  0.00000000,  0.61074953,  0.40604769,  0.00000000,  0.00000000], # 11 ret_pm # Return Time between 4 pm & 6 pm
[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00033711,  0.00039623], # 12 omxdens # Mixed density at origin
[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00001923], # 13 oemp_den # Total Employment Density at Origin

# Added during calibration
[  1.50000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 14 Vehicles greater than / equal to workers AND autos > zero
[  1.50000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 15 Vehicles greater than / equal to  Drivers
[ placeholder ] * 7 # 16 Income Specific Constant 
	
]
durableCoeffMap={ #[[input data offset, durable coeffs offset, number of consecutive fields]]
                 "HouseholdBaseData": [   # most hh data goes toward calculating derived values
                                [5,0,2],  # numWorkers, hchildren
                               ],
                 "HouseholdModeledData" : [
                              [0,2,1],  # nCars
                                          ],
                 "DerivedDurableValues" : [
                                    [3,3,9],   # incle50 # Income < $50K
                                    [14,14,2],   # vehicles per worker
                                   ],
                 "Zones" : [
                              [1,12,1],  # mix_dens
                              [8,13,1],  # totEmpDen
                                          ],
				 "Constants" : [[0,16,1]] # income segmentation
                 } 


# 
# SEGMENTATION maps handle cases where the coefficient depends upon some segmentation of the input data,
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
# updated from school for work tours 
 {'Name': '5 Income Segments', 'DataRef': 'HouseholdBaseData','Offset': 2, 'DataRange': [0,1,2,3,4]}
]

# segmentCoeffMap is another list of sets of key:value pairs.  The length of the list = the number of coefficients 
# that are affected by segmentation within the durable and transient vectors of the alternative(s)
# Each set defines:
#  Segment: index into the segmentDefinitions list (should probably just convert this to use the name)
#  Vector:  possible values: durable/transient:  which coefficient vector in the alternative(s) this set of coefficients applies to
#  Offset:  offset into the relevant Coefficient Vector 
#  Coefficients: an list of lists; first index is which alternative (i.e. alternatives are rows)
#           for each alternative row there are as many values as elements in the corresponding segmentDefinitions' DataRange value
#           so e.g for 'DataRange' :[5,10,15,20], each row below will have 4 elements; 
#           for a data value of 5, the coefficients would come from the first column of data
#           these coefficients will be substituted into the coefficients array for each alternative at the offset specified below


segmentCoeffMap = [
# data from RegWrkLoc_LogsumCalcs.xlsx)
{'Segment': 0, 'Vector': 'transient', 'Offset': 0,  # Total Cost
  'Coefficients':
    [ # normally 1 row that applies to every alternative; it's possible that there may be alternative-specific-variables that are affected by segmentation
      # in that case there would be as many rows as alternatives; I suspect this would never apply to a case with a very large alternative set
        #coeff when segment value is 0, 1, 2, 3, 4 respectively
			# INC0        # INC1       # INC2       # INC3       # INC4
		[ -0.00078364, -0.00058773, -0.00048977, -0.00044080, -0.00029386], # DA
		[ -0.00078364, -0.00058773, -0.00048977, -0.00044080, -0.00029386], # S2
		[ -0.00078364, -0.00058773, -0.00048977, -0.00044080, -0.00029386], # S3
		[ -0.00078364, -0.00058773, -0.00048977, -0.00044080, -0.00029386], # TW
		[ -0.00078364, -0.00058773, -0.00048977, -0.00044080, -0.00029386], # TD
		[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # BK
		[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000],  # WK
    ]
},

{'Segment': 0, 'Vector': 'durable', 'Offset': 16,  # Constant
  'Coefficients':
    [ # normally 1 row that applies to every alternative; it's possible that there may be alternative-specific-variables that are affected by segmentation
      # in that case there would be as many rows as alternatives; I suspect this would never apply to a case with a very large alternative set
        #coeff when segment value is 0, 1, 2, 3, 4 respectively
			# INC0        # INC1       # INC2       # INC3       # INC4
		[ 0, 	0, 	0, 	0, 	0], #  DriveAlone
		[ 0, 	0, 	0, 	0, 	0], #  SharedRide2
		[ 0, 	0, 	0, 	0, 	0], #  SharedRide3
		[ 0.8, 	0, 	0, 	0, 	0], #  WalkToTransit
		[ 0, 	0, 	0, 	0, 	0], #  DriveToTransit
		[ 0.8, 	0, 	0, 	0, 	0], #  Bike
		[ 1.25, 	0, 	0, 	0, 	0], #  Walk

    ]
}

]
