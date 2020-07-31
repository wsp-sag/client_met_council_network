####################################################################
# FullyJointTourDestinationChoice.py
#   this component uses size functions and logsums
####################################################################

# Size Function defined in another file to reduce clutter here
from Globals import *

import TourDestinationChoiceSizeFunction_FullyJoint as sizeFunction

# the name of the corresponding class on the C# side:
# this allows for multiple scripts targeting the same component
modelComponentName="TourDestinationChoiceFullyJoint"  

# this is merely informative and doesn't instigate any activity: 
# it indicates the logsum component that should be instantiated,
# and which should then be set as the TourModeChoiceLogsum property on TourDestinationChoiceFullyJoint
logsumGeneratorName="TourModeChoiceLogsumFullyJoint"

# TODO: I think this will be used by the Model component factory to hand the component the correct logit object
# in AA we hardwired this in the component
logitType="MultinomialLogit"

# introducing parameters, used for running same model component for, in this case:
#  modeling tours for particular purpose
#  university tours do not use segmented size function or location set but the other purposes do
# 
parameters= {
             "tourPurposeDescription": "Fully Joint Tours",
             "tourPurposeIds": [256],
             "fullyJoint": True,
             "usesTransitAccessMatrix" : True,
             "locationSetIsSegmented":True,
             "sizeFunctionIsSegmented":True,
             }

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

    # the first 6 data references lay out distributions for simulating values that we
    # haven't modeled at destination choice time; these are 
    #    tour arrival/departure time (first 4 data references)
    #    number of stops for each half tour
    #    stop purpose distribution


	# for TBI I only have one Arrival-return distribution
	# for now fit this into the existing scheme
    # As far as I can determine we could eliminate this 2 step calculation
    # by generating an equivalent single distribution grid consisting of:
    # p(Short tour) * TimeOfDayArriveReturnDistributionShortTours 
	# + p(Medium tour) * TimeOfDayArriveReturnDistributionMediumTours
	# + p(Long tour) * TimeOfDayArriveReturnDistributionLongTours
	
    # to simulate the tours we'll do 2 monte carlos
    # first for the duration
    # then for the arrival/return pairs for purposes of selecting which time period matrices to use
    {"type" : "constants",
     "dataType":"double",
     "name" : "DistributionByTourDuration",
     "columns" : ["short", "medium", "long"],
     "values" : [
                 0.33, 0.34, 0.33  # probabilities that tours will have specified duration
                ]
    },


    # over all short duration tours, these are the distributions for arrival/departure pairs
    #  i.e. these add up to 1.0
	# for TBI, these were adjusted from the original overall distribution by
	# eliminating ineligible pairs for short tours and scaling up the remaining values to add to 1
    {"type" : "constantsgrid",
     "dataType":"double",
     "name" : "TimeOfDayArriveReturnDistributionShortTours",
     "columns" : ["returnAM", "returnMD", "returnPM", "returnNT"],
     "rows" : ["arriveAM", "arriveMD", "arrivePM", "arriveNT"],
     "values" : [
                 [0.015195240, 0.013132417,           0,           0], # arriveAM
                 [          0, 0.240155556, 0.054704817,           0], # arriveMD
                 [          0,           0, 0.189077948, 0.275673416], # arrivePM
                 [0.006169275,           0,           0, 0.205891332]  # arriveNT
                ]
    },
		

    # over all medium duration tours, these are the distributions for arrival/departure pairs
    #  i.e. these add up to 1.0
	# for TBI, these were adjusted from the original overall distribution by
	# eliminating ineligible pairs for medium-length tours and scaling up the remaining values to add to 1
    {"type" : "constantsgrid",
     "dataType":"double",
     "name" : "TimeOfDayArriveReturnDistributionMediumTours",
     "columns" : ["returnAM", "returnMD", "returnPM", "returnNT"],
     "rows" : ["arriveAM", "arriveMD", "arrivePM", "arriveNT"],
     "values" : [
                 [0.015289565, 0.013213937,           0,           0], # arriveAM
                 [          0, 0.241646339, 0.055044401,           0], # arriveMD
                 [          0,           0, 0.190251662, 0.277384678], # arrivePM
                 [          0,           0,           0, 0.207169417]  # arriveNT
                ]
    },

    # over all long duration tours, these are the distributions for arrival/departure pairs
    #  i.e. these add up to 1.0
	# for TBI, these were adjusted from the original overall distribution by
	# eliminating ineligible pairs for long-length tours and scaling up the remaining values to add to 1	
    {"type" : "constantsgrid",
     "dataType":"double",
     "name" : "TimeOfDayArriveReturnDistributionLongTours",
     "columns" : ["returnAM", "returnMD", "returnPM", "returnNT"],
     "rows" : ["arriveAM", "arriveMD", "arrivePM", "arriveNT"],
     "values" : [
                 [          0, 0.016500610, 0.001168037,           0], # arriveAM
                 [          0, 0.301750496, 0.068735473, 0.006769223], # arriveMD
                 [          0,           0,           0, 0.346377953], # arrivePM
                 [          0,           0,           0, 0.258698207]  # arriveNT
                ]
    },
	
    {"type" : "constantsgrid",
     "dataType":"double",
     "name" : "StopsOnHalfTourDistribution",
     "columns" : ["HT2_zero", "HT2_one", "HT2_two", "HT2_three"],
     "rows" : ["HT1_zero", "HT1_one", "HT1_two", "HT1_three"],
     "values" : [[0.669314817, 0.106100381, 0.015139682, 0.008424317], #HT1_zero (values for HT2)
                 [0.096002557, 0.034439981, 0.006221868, 0.003154476], #HT1_one (values for HT2)
                 [0.026869074, 0.006345165, 0.003552507, 0.004401554], #HT1_two (values for HT2)
                 [0.008593185, 0.00673988,  0.001175951, 0.003524605]  #HT1_three (values for HT2)
                ]
    },
	
    {"type" : "constantsgrid",
     "dataType":"double",
     "name" : "StopPurposeDistribution",
     "columns" : ["Work", "Univer", "School", "Meal", "Shop", "PerBus", "Social", "Escort"],  # these names match up with names in workTourModeChoiceLogsum.py
     "rows" : ["HT1", "HT2"],
     "values" : [
                 [0.00000, 0.00000, 0.00000,  0.130031994, 0.111828618, 0.027079136, 0.428889085, 0.302171167],  # HT1 dist
                 [0.00000, 0.00000, 0.00000,  0.150396649, 0.226209672, 0.030787346, 0.342045203, 0.250561129]  # HT2 dist
                ] 
    },
	
	
    # usual data references follow:

    {"type" : "dbffile",
     "name" : "HouseholdBaseData",  # this household data is needed for logsum and also for main loop 
     "filename" : cube___HOUSEHOLDS_FILE___, # file paths MUST BE RAW strings (open quote preceded by 'r')
     "columns" : ["hhid", 
                  "hhzon", 
                  "hhinc5s", 
				  "hworkers"
                  ],
        "deferredLoad" : True
     #"sort" :  ["hhzon", "hhinc5s","hhid"] # original household data is sorted this way
    },

    {"type" : "dbffile",
     "dataType" : "int",
     "name" : "HouseholdModeledData",
     "filename" : cube___MODELED_HOUSEHOLDS_FILE___, 
     "columns" : [
                "hhId",         # 00
                "homeZoneId",   # 01
                "nCars",        # 02
                ],
     "deferredLoad" : True 
},


	#new for tbi:
    {"type" : "dbffile",
     "name" : "HouseholdPassModels",  # this household data is needed only to feed to the logsum; 
     "filename" : cube___PASS_MODEL___, 
     "columns" : ["hhid", "hhzon", "mnPass", "transPass"],
     #"sort" :  ["hhzon", "hhinc5s","hhid"] # implicit sort by hhinc5 though column is not present; original household data is sorted this way
    },

    # output from Fully Joint Tour model
    {"type" : "dbffile",
     "name" : "FullyJointTours",
     "filename" : cube___FULLY_JOINT_TOURS___, # file paths MUST BE RAW strings (open quote preceded by 'r')
     "columns" : [
                    "person1Id", 
                    "tourId",   
                    "tourPurp", 
                    "hhId",
                    "homeZoneId",
                    "nAdults",    
                    "nChildren",
                    "xFtwInTour"
                  ],
        "deferredLoad" : True
          # "sort": ["hhzon", "hhinc5s", "hhid", "ptype2"] this is the sort as originally from PreDAPDataAssembly, and thus from output of DAP

    },
     
     
     # for derived value to pass to size function as segmentation value
    {"type" : "memory",
     "dataType" : "int",
     "name" : "DerivedValuesForSizeFn",
     "columns" : [
                  "compoundSegment"
                  ]
    },
     

    # for main model need
	# mix_dens (dest)
	# tw_acc
	# for size function need
	# ret_emp
	# NRET_emp
	# households
	# area
    {"type" : "dbffile",
     "name" : "Zones",
     "filename" : cube___ZONES_FILE___, # file paths MUST BE RAW strings (preceded by 'r')
     "columns" : ["zoneId",       # 0
                  "nret_emp",   # 7
                  "ret_emp",   # 2
                  "households",# 8
				  "area",
                  "mix_dens",   # 9  for main model
                  "tw_acc"    # 11
                  ]      
    },

    {"type" : "dbffile",
     "isOutput": "true",
     "name" : "OutputFullyJointTourDestinations",     
     "filename" : cube___FULLY_JOINT_TOUR_DESTINATION_CHOICE___, # file paths MUST BE RAW strings (preceded by 'r')
     # parameters could be generally of form source data reference : field
     # looks like time of day needs extra columns, 
     "parameters" : [
                  ["person1Id",  "person1Id"], # part 1 of pk: using first person in tour
                  ["@tourId",      "tourId"],   # part 2 of pk: tourId starting from 5 for joint tours 
                  ["@tourPurp",   "tourPurp"], 
                  ["hhId",       "hhId"],
                  ["homeZoneId", "homeZoneId"],
                  ["hhinc5s", "hhinc5s" ],        # needed by time of day for value of time
                 ["@alternativeChosen", "destZoneId"], 
                ]
    },

    # dbf output spec; used in tests for inspecting whether results are reasonable
    {"type" : "delimited",
     "isOutput": "true",
     "name" : "OutputDestinationChoiceStats",     
     "filename" : cube___FULLY_JOINT_TOUR_DESTINATION_CHOICE_SUMMARY___, # file paths MUST BE RAW strings (preceded by 'r')             
     "parameters" : [
                       [ "StatLine", "AggregateData"],
                    ]
    }


]

# Matrices are different enough to require their own structure:
from MatrixRef1Hwy1Trans import matrixReferences


# ######################  model structure section  ##########################

# this is meant to represent the alternative output as either:
#    a real world value (e.g. that can be used in downstream utility functions 
#    or an ID of the alternative; in this case the values are number of cars:
# Note: not used directly except for end points
altIntrinsicValues= [1, numberOfZones]#

# not used thus far:
# friendly descriptions of the alternatives, maybe for UI display somehow
altNames = [] # the set of zones; component doesn't use this 

# this should evolve into a specification (in general) a tree structure
logitType = "MultinomialLogit"

# NOTE: no Alternative-Specific Constants for this model (size function serves this purpose I guess)
#altSpecificConsts=None

# for this component we'll share one set of coefficients among all alternatives
# because location alternative set is used, zone-specific data must be in durable arrays, which map to location arrays 
durableCoeffs=[
[ 1.00000000], # ls # logsum 
[	0.02456668	], # dst # dist
[	0.00000112	], # CDist # cube dist
[	0.12785355	], # ldistI4shp # ln(dist+1)  Shopping tour, Income $75K-100K
[	0.38553883	], # ldistI5shp # ln(dist+1) Shopping tour, Income greater than $100K
[	-0.51685834	], # ldistmntch # ln(dist+1)  Child in party, Personal Business
[	-0.44565873	], # ldistshpch # ln(dist+1)  Child in party, Shopping
[	-0.51200359	], # ldisteatch # ln(dist+1)  Child in party, Meal
[	-0.35811461	], # ldistdscch # ln(dist+1)  Child in party, SocRec
[	-1.32732838	], # ldistmntLg # ln(dist+1)  PersBus tour, Party size 3 + 
[	-1.8202167	], # ldistmntSm # ln(dist+1)  PersBus tour, Party size 2
[	-1.86340555	], # ldistshpLg # ln(dist+1)  Shop tour, Party size 3+
[	-2.08842666	], # ldistshpSm # ln(dist+1)  Shop tour, Party size 2
[	-1.74976066	], # ldisteatLg # ln(dist+1)  Meal tour, Party size 3+
[	-1.55541916	], # ldisteatSm # ln(dist+1)  Meal tour, Party size 2
[	-1.22655386	], # ldistdscLg # ln(dist+1)  SocRec tour, Party size 3+
[	-1.64939053	], # ldistdscSm # ln(dist+1)  SocRec tour, Party size 2
[-0.00031688], # mxdens # Mixed Use Density 
[-0.97031993], # intr # intrazonal 
[ 0.45788473], # twacvehgw # Transit accessibility - Workers>Cars 
   # sizeFunction is handled separately
]

# for location set use we could have a set of names we can use to map to the 'columns' in the durableCoeffs
# something like
# locationSetColumns= ["modeLogsum","mix_dens","ret_empDensity","intrazonal",...]


# there is no data that has only non-zone-related components
transientCoeffs=[[]]

# note: SizeFunction is handled separately

# mlogsum value comes from code for now, and the matrix value is alternative-specific


durableCoeffMap={} # the regular durableCoeffMap could work for location alternative set if we used a different utility to copy the values
# e.g. copy the same value to the same positions in a double[,] array
# and use maybe another notation to indicate a mapping from a matrix row to a column in the double[,] array
# in practice, the first option would be useful for mix_dens in this config
# more often we are setting a single value to non-zero in a particular double[,] column

# standard mapping doesn't work for matrix, need some new scheme; would have to be a diagonal mapping across alternatives
# I had something like this but this is nonsense: durableCoeffMap={"DistanceMatrixOD" : [[0,1,1] , [0, 2, 1]]} 


transientCoeffMap={}

# could define some segmentations here but electing to skip it
segmentDefinitions = []

segmentCoeffMap = []

