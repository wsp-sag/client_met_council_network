####################################################################
# UsualWorkplaceTourModeChoiceLogsumTest.py
# This file has some extra information so it can be copied as a future WorkTourModeChoiceLogsum.py
# to conver this:
# uncomment data marked (skip for workplace loc logsum) 
# use the commented-out altSpecificConsts
# will need to do some mapping of the newly enabled data

####################################################################
from Globals import * 

# the name of the corresponding class on the C# side:
# this allows for multiple scripts targeting the same component
modelComponentName="UsualWorkplaceLocationTourModeChoiceLogsum"  

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

    # households is unused for this logsum, but code is looking for zone from households ref
    # so the hhzon will be filled in code using the value from persons
    {"type" : "memory",
     "dataType" : "int",
     "name" : "HouseholdBaseData",                                     
     "columns" : ["hhzon"]
    },

    # because this is fed directly from the UsualLocation persons input row
    # the columns order and number of columns should match the columns from that configuration file exactly
    {"type" : "memory",
     "name" : "Persons",
     "columns" : ["personid",   # 0
                  "hhid",       # 1
                  "hhzon",      # 2
                  "ptype",      # 3 for location set segmentation (segmentation in coeff array, not segmentDefinitions); also for logsum
                  "hhinc5s",    # 4 for location set segmentation (normal) ; also for logsum
                  # following needed for logsum only:
                  "hhsize",     # 5 for deriving '2 person hh', 'hh size 3+'
                  "hworkers",   # 6 used alone and for deriving workers > cars
                  "hadults",    # 7 for deriving Adults > Cars, Workers <= Cars, Cars > 0              
                  "nCars",      # 8 for nCars and deriving workers > cars
                  "noCarsInHh", # 9
                  "wkGtCarGt0", # 10
                  "hh1Person",  # 11 could derive from hhsize if we wanted less data input
                  "age",        # 12 for deriving 'age < 30'
                  "female",      # 13 for deriving 'male'
				  "hchildren"	# 14 
                  ]
    },

    # conceived as a source of constants for vector values like dummy vars; 
    {"type" : "constants",
     "name" : "Constants",
     "columns" : ["One"],
     "values" : [1]  # values are single-dimension for this data reference type
    },

    # for now just put in columns enough to cover calculations needed
    # at some point we'll probably have to add half-tours as an input
    # these columns are NOT needed for the usual workplace logsum
    # but only would be used for an actual tour mode choice logsum
    {"type" : "memory",
     "name" : "Tours",
     "columns" : [
                  "arrival", "departure",  # values 
                  "nStopsHt1", "nStopsHt2",    # all the rest is half-tour related;
                  "nMealHt1", "nMealHt2", 
                  "nBusHt1",  "nBusHt2", 
                  "nSocHt1",  "nSocHt2", 
                  "nEscHt1",  "nEscHt2", # covers 'school escorting ht1 or 2'
                  "nWorkHt1",  "nWorkHt2", 
                  "nShopHt1",  "nShopHt2", # looks like shopping on ht1 is unused.
                  "nSchHt1",  "nSchHt2", 
                  "nUniHt1",  "nUniHt2" 
                  ]
    },

    # DerivedValues; for logsums this is just a specification of a column set 
    # a separate memory array of columns.length is generated for each alternative in the logsum code
    {"type" : "memory",
     "name" : "DerivedValues",
     "columns" : [
                  # these map to transients (and are set in the logsum code because we need to recalc for each zone; 
                  # the point of this is that we can at least keep the mapping to the coefficients in this file)
                  "RT Cost(I5)",                    #0 
                  "Gen Time",                       #1
                  "RT Distance",                    #2
                  "transfers",  					#3
                  "transitWaitLT10Mins",			#4
                  "transitWaitLT20Mins",			#5	  
                  "retail density dest",            #6
                  "pop density dest",               #7
                  "total employment density dest"   #8
                  ]
    },

    # DerivedDurableValues
    # the memory for this is allocated by the logsum code
    {"type" : "memory",
     "name" : "DerivedDurableValues",
     "columns" : [
                  # these map to durables and are set from the main code:
                  #TODO: I need to split this data reference into 2 
                  "wkGtCars", #0 was 7
                  "Adults > Cars, Workers <= Cars, Cars > 0", #1 was 8
                  "hhsize2",  #2 was 9
                  "hhsizeGt2",  #3 was 10
                  "isPtw",  #4 was 11
                  "isFtw",  #5 was 12
                  "isSen",  #6 was 13
                  "ageLt30", #7 was 14
                  "male"   , #8 was 15
                  "total employment density origin", #9 I don't think we need this, can use directly from calculated column in select
                  "arrAMPeak",  #10 not mapped to vectors here (only in full logsum) - is here for deciding which skims to use
                  "retPMPeak",  #11 not mapped to vectors here (only in full logsum) - is here for deciding which skims to use 
				  "ageGt35" # 12 age greater than 35
                  ]
    },

    {"type" : "dbffile",
     "name" : "Zones",
     "filename" : cube___ZONES_FILE___, 
     "columns" : [
                  "zoneId",    # 0
                  "mix_dens",  # 1
                  "ret_emp",   # 2
                  "population",# 3
                  "tot_emp",   # 4
                  "term_time", # 5
                  "park_cost", # 6
                  "area",      # 7
				  "district"   # 8
                  ]
    }
]

from MatrixRef4Hwy4Trans import matrixReferences

########################  model structure section  ##########################

# these values reflect the available TourMode values (School bus not used)
altIntrinsicValues = [1, 2, 3, 4, 5, 7, 6]

# updated from school for work tours
altNames = ["DA", "S2", "S3", "TW", "TD", "BK", "WK"]




logitType="NestedLogit"

# NestedLogit

# ASCII representation of nesting structure

#   [UI name, nestID, nest coeff, [alts], [nests]]
# where [alts] refers to alternatives by its order in any of the altIntrinsicValues/altNames/durableCoeffs/transientCoeffs lists
# and [nests] is a list of nestIDs
# updated from school for work tours
nestList = [
            ["Root", 0, 1.0, [], [1, 2, 3, 4]], # subnests are DA, HOV, Transit, Non-Motorized
            ["Drive Alone", 1, 0.8, [0], []],  # nest is just a single alt
            ["Shared Ride", 2, 0.8, [1, 2], []],  # nest with two alternatives SR2, SR3
            ["Transit", 3, 0.8, [3, 4], []],     # nest with two alternatives TW, TD
            ["Non-Motorized", 4, 0.8, [5, 6], []], # nest with two alternatives Wk, Bk
           ]

# These constants do not need to be adjusted based on the average values because we are simulating those inputs
altSpecificConsts = [  0.00000000, -4.42973660, -4.20811375, -0.41163926, -4.53615712, -2.15381615, -0.10651294] 

# Coefficients are divided into two types:
#   coefficients whose corresponding values don't change very often ('durable' values)
#   coefficients whose values are assumed to change for every iteration ('transient' values)

# In the case of logsums, the normal expectations for what is durable and what is transient are reversed
# because the logsum computations occur over all zones for a fixed person
# description of transient variables:
# some variables  are segmented by income, so those coefficients have placeholder values of 0
# Just for reference I've indicated the segmentation applied in parens e.g. (I2 means using 2 income segments (<$40k, >=$40k))
# updated from school for work tours (data from RegWrkLoc_LogsumCalcs.xlsx)
# for the 
transientCoeffs=[
 # DA,        # S2,        # S3,        # TW,        # TD,        # BK         # WK,   
[ placeholder]*7,  # 0 RT Cost(I5) calc for this is exactly as for school (segmented)
[ -0.00876907, -0.00876907, -0.00876907, -0.00876907, -0.00876907,  0.00000000,  0.00000000],  # 1 Gen Time
[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000, -0.14508584, -0.57247939],  # 2 RT distance - specific to the mode
[  0.00000000,  0.00000000,  0.00000000, -0.23503976, -0.23503976,  0.00000000,  0.00000000], # 3 Number of transfers 
[  0.00000000,  0.00000000,  0.00000000,  0.47023458,  0.69262819,  0.00000000,  0.00000000], # 4 WTHF10 # WT: OB Wait<10 mins; IB Wait < 10 mins
[  0.00000000,  0.00000000,  0.00000000,  0.39106252,  0.00000000,  0.00000000,  0.00000000], # 5 WTHF20 # WT: OB Wait-10-20 mins; IB Wait- 10-20 mins
[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00003746,  0.00000000,  0.00000000], # 6 ret_den # Retail Density at Destination
[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00008751,  0.00000000], # 7 dpopden # Population density at destination
[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000109], # 8 demp_den # Total Employment Density at Destination
]

transientCoeffMap={} #"DerivedValues": [[0,0,8]] }  # this is unused; just here to note that 
# there is a relationship between the DerivedValues data reference and the row order in the transient coeffs above
# in fact a MemoryDataReference based on the DerivedValues spec above is created for each alternative 
#(essentially for each column of coeffs in the transientCoeffs above)



# description of durable variables:
# updated from school for work tours (data from RegWrkLoc_LogsumCalcs.xlsx)
durableCoeffs=[
 # DA,        # S2,        # S3,        # TW,        # TD,        # BK         # WK,   
[ placeholder]*7, # 0 Income (SEGMENTED)  
[  0.00000000,  0.42441007,  0.52561135,  0.33049329,  0.33049329,  0.19347737,  0.19347737], # 1 children # Number of children
[  0.00000000,  0.94338708,  0.94338708,  0.82980017,  0.82980017,  0.67534206,  0.67534206], # 2 workers #   (Number of HH Workers) (from persons)
[  0.00000000, -0.67165688, -0.72398881, -1.21854892, -0.80531080, -1.21020354, -1.21020354], # 3 hhveh # HH number of vehicles (from persons)
[  1.00091281,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 4 agegr65 # Senior (from derived)
[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.55934559,  0.55934559], # 5 Male (from derived)
[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00001923], # 6 oemp_den # Total Employment Density at Origin (from zones)
[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00033711,  0.00039623], # 7 omxdens # Mixed density at origin
[  0.00000000,  0.00000000,  0.00000000, -0.52253064,  0.00000000, -1.05748321, -0.12732174], # 8 agegr35 # Age greater than 35
]
durableCoeffMap={ #[[input data offset, durable coeffs offset, number of consecutive fields]]
                 "Constants": [[0,0,1]] , # for hh income dummy
                 "Persons" : [
                              [14,1,1], # hchildren
                              [6,2,1],  # hworkers
                              [8,3,1]  # nCars
                              ], 
                 "DerivedDurableValues" : [
                                    [6,4,1], #isSen 
                                    [8,5,1], #male
									[12,8,1] #ageGt35
                                   ],
                 "Zones": [
							[4,6,1], #tot_emp
							[1,7,1] #mix_dens						
							]							
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
 {'Name': '5 Income Segments', 'DataRef': 'Persons','Offset': 4, 'DataRange': [0,1,2,3,4]}
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
		# INC1        # INC2       # INC3       # INC4       # INC5
		[ -0.00078364, -0.00058773, -0.00048977, -0.00044080, -0.00029386], # DA
		[ -0.00078364, -0.00058773, -0.00048977, -0.00044080, -0.00029386], # S2
		[ -0.00078364, -0.00058773, -0.00048977, -0.00044080, -0.00029386], # S3
		[ -0.00078364, -0.00058773, -0.00048977, -0.00044080, -0.00029386], # TW
		[ -0.00078364, -0.00058773, -0.00048977, -0.00044080, -0.00029386], # TD
		[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # BK
		[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000]  # WK
    ]
},

{'Segment': 0, 'Vector': 'durable', 'Offset': 0,  # income segment
  'Coefficients':
    [ 
		# INC1        # INC2       # INC3       # INC4       # INC5	
		[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000],	# DA
		[ -0.09573392, -0.09573392,  0.00000000,  0.36789922,  0.36789922],	# S2
		[ -0.09573392, -0.09573392,  0.00000000,  0.36789922,  0.36789922],	# S3
		[  0.77764779,  0.77764779,  0.00000000,  0.00000000,  0.00000000],	# TW
		[ -0.85022050, -0.85022050,  0.00000000,  0.08832096,  0.08832096],	# TD
		[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000],	# BK
		[  0.00000000,  0.00000000,  0.00000000, -1.19000659, -1.19000659]	# WK
    ]
}



]
