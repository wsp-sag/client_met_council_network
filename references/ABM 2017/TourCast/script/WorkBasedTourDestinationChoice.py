####################################################################
# WorkBasedTourDestinationChoice.py
# should be renamed TourDestinationChoice_WorkBased.py 
#   this component uses size functions and logsums
####################################################################

from Globals import * # for numberOfZones

# Size Function defined in another file to reduce clutter here
import TourDestinationChoiceSizeFunction_WorkBased as sizeFunction

# the name of the corresponding class on the C# side:
# this allows for multiple scripts targeting the same component
modelComponentName="TourDestinationChoiceWorkBased"  

# this is merely informative and doesn't instigate any activity: 
# it indicates the logsum component that should be instantiated,
# and which should then be set as the TourModeChoiceLogsum property on TourDestinationChoiceWorkBased
logsumGeneratorName="TourModeChoiceLogsumWorkBased"

# TODO: I think this will be used by the Model component factory to hand the component the correct logit object
# in AA we hardwired this in the component
logitType="MultinomialLogit"

# introducing parameters, used for running same model component for, in this case:
#  modeling tours for particular purpose
#  university tours do not use segmented size function or location set but the other purposes do
# 
parameters= {
             "tourPurposeDescription": "Work-based Tours",
             "tourPurposeIds": [512],  # this is probably unneeded because incoming tours are only workbased
             "fullyJoint": False,
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

    # the first 4 data references lay out distributions for simulating values that 
    # haven't modeled at destination choice time; these are
    # simulating stop distributions and stop purposes
    # for work based tours, destination choice assumes that
    # arrival and departure are always in the midday period
    # arrival is always between 11am and 1 pm 

	# need to update all Distributions for TBI
    {"type" : "constantsgrid",
     "dataType":"double",
     "name" : "StopsOnHalfTourDistributionForTourPurposeWork",
     "columns" : ["HT2_zero", "HT2_one", "HT2_two", "HT2_three"],
     "rows" : ["HT1_zero", "HT1_one", "HT1_two", "HT1_three"],
     "values" : [[0.591, 0.145, 0.035, 0.021], #HT1_zero (values for HT2)
                 [0.054, 0.060, 0.010, 0.000], #HT1_one (values for HT2)
                 [0.032, 0.009, 0.011, 0.006], #HT1_two (values for HT2)
                 [0.023, 0.000, 0.003, 0.000]  #HT1_three (values for HT2)
                ]
    },
	
    {"type" : "constantsgrid",
     "dataType":"double",
     "name" : "StopsOnHalfTourDistributionForTourPurposeNonwork",
     "columns" : ["HT2_zero", "HT2_one", "HT2_two", "HT2_three"],
     "rows" : ["HT1_zero", "HT1_one", "HT1_two", "HT1_three"],
     "values" : [[0.8494, 0.0701, 0.0097, 0.0027], #HT1_zero (values for HT2)
                 [0.0523, 0.0103, 0.0000, 0.0000], #HT1_one (values for HT2)
                 [0.0043, 0.0012, 0.0000, 0.0000], #HT1_two (values for HT2)
                 [0.0000, 0.0000, 0.0000, 0.0000]  #HT1_three (values for HT2)
                ]
    },


    {"type" : "constantsgrid",
     "dataType":"double",
     "name" : "StopPurposeDistributionForTourPurposeWork",
     "columns" : ["Work", "Univer", "School", "Meal", "Shop", "PerBus", "Social", "Escort"],  # these names match up with names in workTourModeChoiceLogsum.py
     "rows" : ["HT1", "HT2"],
     "values" : [
                 [0.4968, 0.0000, 0.0000, 0.3011, 0.1140, 0.0881, 0.0000, 0.0000],  # HT1 dist
                 [0.4609, 0.0000, 0.0000, 0.2970, 0.1530, 0.0764, 0.0000, 0.0127]  # HT2 dist
                ] 
    },

    {"type" : "constantsgrid",
     "dataType":"double",
     "name" : "StopPurposeDistributionForTourPurposeNonwork",
     "columns" : ["Work", "Univer", "School", "Meal", "Shop", "PerBus", "Social", "Escort"],  # these names match up with names in workTourModeChoiceLogsum.py
     "rows" : ["HT1", "HT2"],
     "values" : [
                 [0.0000, 0.0000, 0.0000, 0.1580, 0.1241, 0.5246, 0.0814, 0.1119],  # HT1 dist
                 [0.0000, 0.0000, 0.0000, 0.2898, 0.2041, 0.3557, 0.0000, 0.1504]  # HT2 dist
                ] 
    },

    # usual data references follow:

    #OKWB
    {"type" : "dbffile",
     "name" : "HouseholdBaseData",  # this household data is needed only to feed to the logsum; note vars noCarsInHh and nCars, while household, will be supplied by NCarsFromAA
     "filename" : cube___HOUSEHOLDS_FILE___, # file paths MUST BE RAW strings (open quote preceded by 'r')
     "columns" : ["hhid", 
                  "hhzon", 
                  "hhinc5s", 
                  ],
        "deferredLoad" : True
     #"sort" :  ["hhzon", "hhinc5s","hhid"] # original household data is sorted this way
    },

	#new for tbi:
    {"type" : "dbffile",
     "name" : "HouseholdPassModels",  # this household data is needed only to feed to the logsum; 
     "filename" : cube___PASS_MODEL___, 
     "columns" : ["hhid", "hhzon", "mnPass", "transPass"],
     #"sort" :  ["hhzon", "hhinc5s","hhid"] # implicit sort by hhinc5 though column is not present; original household data is sorted this way
    },

	
    #OKWB
    {"type" : "dbffile",
     "name" : "Persons",  # this household data is needed only to feed to the logsum, and only for ptypeDAP
     "filename" : cube___PERSONS_FILE___, # file paths MUST BE RAW strings (open quote preceded by 'r')
     "columns" : ["personId", 
                  "hhid",
                  "HHZON",
                  "ptypeDAP",
                  "age"     #used for alternative eligibility requirements
                  ]
    },


    # output from Work-based subtour model
    {"type" : "dbffile",
     "name" : "WorkBasedTours",
     "filename" : cube___WORK_BASED_SUBTOURS___, # file paths MUST BE RAW strings (open quote preceded by 'r')
     "columns" : [  #OKWB
                    "personId", 
                    "persTourId",   
                    "tourPurp", 
                    "hhId",
                    "homeZoneId",
                    "origZoneId",
                    "parentMode",
                    "parTourId"  # when combined with personId gives full parent tour key
                  ],
        "deferredLoad" : True
          # "sort": ["hhzon", "hhinc5s", "hhid", "ptype2"] this is the sort as originally from PreDAPDataAssembly, and thus from output of DAP

    },
     
     
     # for derived value to pass to size function as segmentation value
    {"type" : "memory",
     "dataType" : "int",
     "name" : "DerivedValuesForSizeFn",
     "columns" : [
                  "tourPurpose",
				  "compoundSegment"  # actually for main code, not size fn
                  ]
    },
     
    #OKWB
    # from zone we need 
    {"type" : "dbffile",
     "name" : "Zones",
     "filename" : cube___ZONES_FILE___, # file paths MUST BE RAW strings (preceded by 'r')
     "columns" : ["zoneId",    # 0 for size fn (mapped by sizeFunctionDurableCoeffMap)
				  "nret_emp",   # 1 for size fn (mapped by sizeFunctionDurableCoeffMap)
                  "area",      # 2 unused for work-based, probably can remove
                  "ret_emp",   # 3 for size fn (mapped by sizeFunctionDurableCoeffMap)
                  "households",# 4 for size fn (mapped by sizeFunctionDurableCoeffMap)
                  "mix_dens",  # 5 for main model (no coeff mapping here)
                  #"tw_acc",     #14 for main model (no coeff mapping here)
                  ]      
    },

    {"type" : "dbffile",
     "isOutput": "true",
     "name" : "OutputWorkBasedTourDestinations",     
     "filename" : cube___WORK_BASED_TOUR_DESTINATION_CHOICE___, # file paths MUST BE RAW strings (preceded by 'r')
     # parameters could be generally of form source data reference : field
     # looks like time of day needs extra columns, 
     "parameters" : [
                  ["personId",  "personId"], # part 1 of pk: using first person in tour
                  ["persTourId",      "persTourId"],   # part 2 of pk: tourId starting from 5 for joint tours 
                  ["tourPurp",   "tourPurp"], 
                  ["hhId",       "hhId"],
                  ["homeZoneId", "homeZoneId"],  # note: not origin of work-based tour; carry so we can chunk hh/person info
                  ["origZoneId", "origZoneId"],
                  ["hhinc5s", "hhinc5s" ],        # needed by time of day for value of time
                  ["parentMode","parentMode"],
                  ["parTourId","parTourId"],
                  ["@alternativeChosen", "destZoneId"], 
                ]
    },

    # dbf output spec; used in tests for inspecting whether results are reasonable
    {"type" : "delimited",
     "isOutput": "true",
     "name" : "OutputDestinationChoiceStats",     
     "filename" : cube___WORK_BASED_TOUR_DESTINATION_CHOICE_SUMMARY___, # file paths MUST BE RAW strings (preceded by 'r')             
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
durableCoeffs=[ #OKWB
[ 0.77147550], # ls # logsum 
[-0.00069421], # SDist # sqr dist 
[ 0.00000092], # CDist # cube dist 
[placeholder], # Ln(dist + 1) segmented by tour purpose
[placeholder], # ln(dist + 1) segmented by tour type(work/non-work) combined with worker type (ftw/ptw/other)
[placeholder], # mixed use density segmented by tour purpose
[ 0.18948539], # intrFt # IntraZonal FT
[-1.37028216],# intrPt # IntraZonal PT
   # sizeFunction is handled separately
]

# there is no data that has only non-zone-related components
transientCoeffs=[[]]

# note: SizeFunction is handled separately

durableCoeffMap={} # the regular durableCoeffMap could work for location alternative set if we used a different utility to copy the values
# e.g. copy the same value to the same positions in a double[,] array
# and use maybe another notation to indicate a mapping from a matrix row to a column in the double[,] array
# in practice, the first option would be useful for mix_dens in this config
# more often we are setting a single value to non-zero in a particular double[,] column

# standard mapping doesn't work for matrix, need some new scheme; would have to be a diagonal mapping across alternatives
# I had something like this but this is nonsense: durableCoeffMap={"DistanceMatrixOD" : [[0,1,1] , [0, 2, 1]]} 

transientCoeffMap={}


segmentDefinitions = [
  # straight segmentation by tour purpose
 {'Name': 'Tour Purpose', 'DataRef': 'DerivedValuesForSizeFn','Offset': 0, 
  'DataRange': [ #OKWB
                purposeWork  + purposeWorkBased,    # work  
                purposeMeal  + purposeWorkBased,    # meal  
                purposeShop  + purposeWorkBased,    # shop  
                purposePersonalBusiness  + purposeWorkBased,    # perbus
                purposeSocialRecreation  + purposeWorkBased,    # socrec
                purposeEscort  + purposeWorkBased,    # escort
                ]
  },
  # compound segment calculated by workTour = 1, nonWorkTour = 2, ftw = 10, ptw = 20, other person type = 30
 {'Name': 'work/non-work tour by worker type', 'DataRef': 'DerivedValuesForSizeFn','Offset': 1, 
  'DataRange': [ 11, 12, 21, 22, 31, 32]
  }
]


segmentCoeffMap = [  #OKWB
{'Segment': 0, 'Vector': 'durable', 'Offset': 3,  'Coefficients':[[
	0.00000000, # work  
	-2.96178396, # meal  
	-2.8227187, # shop  
	-1.76043038, # perbus
	-2.17043832, # socrec
	-1.7074593, # escort
]]},# Ln(dist + 1) by tour purpose
{'Segment': 0, 'Vector': 'durable', 'Offset': 5,  'Coefficients':[[
	 0.00000000, # work  
	-0.00041681, # meal  
	-0.00019215, # shop  
	-0.00045984, # perbus
	-0.00024302, # socrec
	 0.00000000, # escort
]]},# mixed use density by tour purpose
{'Segment': 1, 'Vector': 'durable', 'Offset': 4,  'Coefficients':[[
	-1.67112083, # 11 ftw work tour
	0.00000000, # 12 ftw non-work tour
	-2.11004189, # 21 ptw work tour
	-0.35550362, # 22 ptw non-work tour
	0.00000000, # 31 other work tour
	0.00000000, # 32 other non-work tour
]]},# ln(dist + 1) segmented by tour type(work/non-work) combined with worker type (ftw/ptw/other)
]
