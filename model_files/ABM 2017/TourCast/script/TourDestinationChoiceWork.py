####################################################################
# TourDestinationChoiceWork.py
#   this component uses size functions and logsums
####################################################################

from Globals import * # for numberOfZones

# Size Function defined in another file to reduce clutter here
import TourDestinationChoiceSizeFunction_Work as sizeFunction

# the name of the corresponding class on the C# side:
# this allows for multiple scripts targeting the same component
modelComponentName="TourDestinationChoiceWork"  

# this is merely informative and doesn't instigate any activity: 
# it indicates the logsum component that should be instantiated,
# and which should then be set as the TourModeChoiceLogsum property on TourDestinationChoiceWork
logsumGeneratorName="WorkTourModeChoiceLogsum"

# TODO: I think this will be used by the Model component factory to hand the component the correct logit object
# in AA we hardwired this in the component
logitType="MultinomialLogit"

# introducing parameters, used for running same model component for, in this case:
#  modeling tours for particular purpose
#  university tours do not use segmented size function or location set but the other purposes do
# 
parameters= {
             "tourPurposeDescription": "Work Tours",
             "tourPurposeIds": [2],
             "fullyJoint": False,
             "usesTransitAccessMatrix" : False,
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

    {"type" : "constantsgrid",
     "dataType":"double",
     "name" : "TimeOfDayArriveReturnDistribution",
     "columns" : ["returnAM", "returnMD", "returnPM", "returnNT"],
     "rows" : ["arriveAM", "arriveMD", "arrivePM", "arriveNT"],
     "values" : [
                 [0.005967928, 0.222668224, 0.373816283, 0.014838114], # arriveAM
                 [0.000000000, 0.088023847, 0.130401534, 0.049080217], # arriveMD
                 [0.000000000, 0.000000000, 0.006364711, 0.033860118], # arrivePM
                 [0.012784761, 0.032946217, 0.011992501, 0.017255545]  # arriveNT
                ]
    },


    {"type" : "constantsgrid",
     "dataType":"double",
     "name" : "StopsOnHalfTourDistribution",
     "columns" : ["HT2_zero", "HT2_one", "HT2_two", "HT2_three"],
     "rows" : ["HT1_zero", "HT1_one", "HT1_two", "HT1_three"],
     "values" : [[0.515552110, 0.068152878, 0.022236449, 0.011167122], #HT1_zero (values for HT2)
                 [0.152888833, 0.055152791, 0.014643408, 0.007903740], #HT1_one (values for HT2)
                 [0.052474749, 0.024930627, 0.006032739, 0.002506776], #HT1_two (values for HT2)
                 [0.041849399, 0.015719148, 0.005948035, 0.002841196]  #HT1_three (values for HT2)
                ]
    },




    {"type" : "constantsgrid",
     "dataType":"double",
     "name" : "StopPurposeDistribution",
     "columns" : ["Work", "Univer", "School", "Meal", "Shop", "PerBus", "Social", "Escort"],  # these names match up with names in workTourModeChoiceLogsum.py
     "rows" : ["HT1", "HT2"],
     "values" : [
                 [0.204217018, 0.002474502, 0.003432743, 0.080743145, 0.055379011, 0.081080565, 0.260815266, 0.311857750],  # HT1 dist
                 [0.133296111, 0.006758117, 0.002056664, 0.087358121, 0.207137067, 0.093326380, 0.280459288, 0.189608252]  # HT2 dist
                ] 
    },


    {"type" : "constantsgrid",
     "dataType":"double",
     "name" : "IndividualToursDistribution",
     "columns" : ["zero","one", "two", "three", "four", "five", "six"],  # total tours including existing ones
     "rows" : ["oneWork", "twoTotalOneWork"],
     "values" : [
				  # TODO [TC-16]: must update these distributions for MetCouncil
                 [0, 0.81218, 0.15170, 0.02996, 0.00577, 0.00030, 0.00009],  # 1 work DAP (IDS 1,2) (note, slight adjustment so sum is 1.0)
                 [0, 0.00000, 0.74644, 0.19272, 0.04029, 0.01712, 0.00343],  # 2 mand DAP where one is work (IDs 3-9)
                ] 
    },

    {"type" : "constantsgrid",
     "dataType":"double",
     "name" : "SchoolEscortingDistribution",
     "columns" : ["noEscorting", "schoolEscorting"],
     "rows" : ["oneWork", "twoTotalOneWork"],
     "values" : [
				  # TODO [TC-16]: must update these distributions for MetCouncil
                 [0.8255, 0.1745],  # 1 work DAP (IDS 1,2)
                 [0.8984, 0.1016],  # 2 mand DAP where one is work (IDs 3-9)
                ] 
    },



    {"type" : "dbffile",
     "name" : "Households",  # this household data is needed only to feed to the logsum; note vars noCarsInHh and nCars, while household, will be supplied by NCarsFromAA
     "filename" : cube___HOUSEHOLDS_FILE___, # file paths MUST BE RAW strings (open quote preceded by 'r')
     "columns" : ["hhid", 
                  "hhzon", 
                  "hhinc5s", 
                  "hhsize", 
                  "hchildren", 
                  "hh1person", 
                  "hWorkers",
                  "nKidsGT2", 
                  #, "hstud" # not needed?
                  ],
     #"sort" :  ["hhzon", "hhinc5s","hhid"] # original household data is sorted this way
    },

	#new for tbi:
    {"type" : "dbffile",
     "name" : "HouseholdPassModels",  # this household data is needed only to feed to the logsum; 
     "filename" : cube___PASS_MODEL___, # file paths MUST BE RAW strings (open quote preceded by 'r')
     "columns" : ["hhid", "hhzon", "mnPass", "transPass"],
     #"sort" :  ["hhzon", "hhinc5s","hhid"] # implicit sort by hhinc5 though column is not present; original household data is sorted this way
    },
	
	
    {"type" : "dbffile",
     "name" : "FirstTours",
     "filename" : cube___DAILY_ACTIVITY_PATTERNS_FIRST_TOURS___, # file paths MUST BE RAW strings (open quote preceded by 'r')
     "columns" : [
                    "personId",    
                    "hhId",
                    "persTourId",   # pass-thru data for TOD
                    "tourPurp",     # used to id tours
                    "personType",   # pass-thru data for TOD
                    "cType1",       # pass-thru data for TOD, also = pchild1 for logsum
                    "cType2",       # pass-thru data for TOD
                    "cType3",       # pass-thru data for TOD
                    "cType4",       # pass-thru data for TOD
                    "cType5",       # pass-thru data for TOD, also = pchild5 for logsum
                    "age",          # pass-thru data for TOD, also logsum
                    "male",         # pass-thru data for TOD, also logsum
                    "destZoneId",   # common column, output of dest choice model (delete this here and put in output)
                    "workZoneId",   # pass-thru data for TOD, also logsum
                    "hhinc5s",      # pass-thru data for TOD,
                    "wkGtCarGt0",   # pass-thru data for TOD
                    "homeZoneId",   # # pass-thru data for TOD, also used here
                    "noStopTour",   # pass-thru data for TOD
                    "dapId",        # pass-thru data for TOD
                    "tourCount",    # pass-thru data for TOD
                    "hhC1tour",     # pass-thru data for TOD
                    "hhC2tour",     # pass-thru data for TOD
                    "hhC3tour",     # pass-thru data for TOD
                    "hhC4tour",     # pass-thru data for TOD
                    "hhC5tour",     # pass-thru data for TOD
                    "hhChildSAH",   # pass-thru data for TOD
                    "ctype",        # segmentation var here
                    "nCars",        # for logsum
                    "noCarsInHh",    # for here
                    "minNTours",    # for tour dest choice logsum TODO: we don't need these anymore; now simulating them in code based on distributions
                    "minNStops"     # for tour dest choice logsum TODO: we don't need these anymore; now simulating them in code based on distributions
                  ],
        "deferredLoad" : True
          # "sort": ["hhzon", "hhinc5s", "hhid", "ptype2"] this is the sort as originally from PreDAPDataAssembly, and thus from output of DAP

    },
     
    {"type" : "dbffile",
     "name" : "SecondTours",
     "filename" : cube___DAILY_ACTIVITY_PATTERNS_SECOND_TOURS___, # file paths MUST BE RAW strings (open quote preceded by 'r')
     "columns" : [
                    "personId",  
                    "hhId",
                    "persTourId",  
                    "tourPurp",    
                    "personType",
                    "cType1",
                    "cType2",
                    "cType3",
                    "cType4",
                    "cType5",
                    "age",
                    "male",
                    "destZoneId",
                    "workZoneId",
                    "hhinc5s",
                    "wkGtCarGt0",
                    "homeZoneId",
                    "noStopTour",
                    "dapId",
                    "tourCount",
                    "hhC1tour",
                    "hhC2tour",
                    "hhC3tour",
                    "hhC4tour",
                    "hhC5tour",
                    "hhChildSAH",
                    "ctype",        # segmentation var here
                    "nCars",        # for logsum
                    "noCarsInHh",    # for here
                    "minNTours",    # for tour dest choice logsum
                    "minNStops"     # for tour dest choice logsum
                  ],
        "deferredLoad" : True
          # "sort": ["hhzon", "hhinc5s", "hhid", "ptype2"] this is the sort as originally from PreDAPDataAssembly, and thus from output of DAP
     },
     
     # for derived value to pass to size function as segmentation value; also used for location set segmentation
    {"type" : "memory",
     "name" : "DerivedValuesForSizeFn",
     "columns" : [
                  "wrkrIncSeg",      # value = income + worker type; where inc < 75k = 0, >75k = 10; FT = 1, PT = 2, other = 3
				  "workerSeg"        # FT = 1, PT = 2, other = 3
                  ]
    },
     


    {"type" : "dbffile",
     "name" : "Zones",
     "filename" : cube___ZONES_FILE___, # file paths MUST BE RAW strings (preceded by 'r')
     "columns" : ["zoneId",    # 00
                  "households",# 01
                  "ret_emp",   # 02
				  "nret_emp",  # 03
                  "mix_dens",  # 04
				  "cbd",       # 05
				  "retempden", # 06
				  "popdens",   # 07
				  "totEmpDen", # 08
                  ] 
    },

    # dbf output spec; used in tests for inspecting whether results are reasonable
    {"type" : "dbffile",
     "isOutput": "true",
     "name" : "OutputFirstTours",     
     "filename" : cube___WORK_TOUR_DESTINATION_CHOICE_FIRST_TOURS___, # file paths MUST BE RAW strings (preceded by 'r')
     # parameters could be generally of form source data reference : field
     "parameters" : [
                 ["Persons", "personId"],
                 ["PersonTourId", "persTourId"],
                 ["homeZoneId", "homeZoneId"],
                 ["@alternativeChosen", "destZoneId"], # could be a pass-through depending on order of running dest
                 ["@distH2Work", "distH2Work"], # used in work-based subtour; one-way distance between home zone and work zone
                 ["avgerage logsum", "avgLogsum"],
                 ["logsum range", "logsumRng"],
                ]
    },
    # dbf output spec; used in tests for inspecting whether results are reasonable
    {"type" : "dbffile",
     "isOutput": "true",
     "name" : "OutputSecondTours",     
     "filename" : cube___WORK_TOUR_DESTINATION_CHOICE_SECOND_TOURS___, # file paths MUST BE RAW strings (preceded by 'r')
     # parameters could be generally of form source data reference : field
     "parameters" : [
                 ["Persons", "personId"],
                 ["PersonTourId", "persTourId"],
                 ["homeZoneId", "homeZoneId"],
                 ["@alternativeChosen", "destZoneId"], # could be a pass-through depending on order of running dest
                 ["@distH2Work", "distH2Work"], # used in work-based subtour; one-way distance between home zone and work zone
                  ["avgerage logsum", "avgLogsum"],
                 ["logsum range", "logsumRng"],
               ]
    },



    # dbf output spec; used in tests for inspecting whether results are reasonable
    {"type" : "delimited",
     "isOutput": "true",
     "name" : "OutputDestinationChoiceStats",     
     "filename" : cube___WORK_TOUR_DESTINATION_CHOICE_SUMMARY___, # file paths MUST BE RAW strings (preceded by 'r')             
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
[ placeholder], # ln(dist+1) compound segment by worker type/income
[ placeholder],  # square RT distance segmented by worker type
[ placeholder], # cube RT distance segmented by worker type
[-0.25882587], # cd # CBD (term ==5)   can preload
[ placeholder], # intrazonal segmented by worker type
[ placeholder], # usual workplace location, compound segment by worker type/income
[ 0.80],  # usual workplace location ln(dist + 1) (0 if zone is not the usual workplace)
[ placeholder], # usual workplace location and intrazonal, compound segment by worker type/income
   # sizeFunction is handled separately
]

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

# both segmentations require some manipulation of the inputs,so come from the DerivedValuesForSizeFn data reference
# 1) worker type/ income:
# 	only interested in 2 income segments, < 75, >=75;  income segment value = 0 for < 75k, 10 for >= 75 k
# 	worker type values: FT=1, PT=2, other=3, so value range is 1,2,3, 11, 12, 13
# 2) worker type segment, FT=1, PT=2, other =3; 
segmentDefinitions = [
 {'Name': ' Worker type/Income Segment', 'DataRef': 'DerivedValuesForSizeFn','Offset': 0, 'DataRange': [1,2,3, 11, 12, 13]},
 {'Name': ' Worker type segment', 'DataRef': 'DerivedValuesForSizeFn','Offset': 1, 'DataRange': [1,2,3]}, 
]

segmentCoeffMap = [
#																	 FT lo      PT lo         NW low       FT hi	     PT hi        NW hi
{'Segment': 0, 'Vector': 'durable', 'Offset': 1, 'Coefficients':[[ -1.00404101, -0.9666317, -2.14517907, -0.99345163, -1.11153175, -2.14517907]]},      # Ln(RT dist + 1)
{'Segment': 0, 'Vector': 'durable', 'Offset': 6, 'Coefficients':[[ 7.41129791, 6.14494071, 0, 7.15011429, 6.14494071, 0]]},      # location is uaual workplace

#                                                                      FT           PT        nonworker
{'Segment': 1, 'Vector': 'durable', 'Offset': 2, 'Coefficients':[[-0.00007288, -0.00025843, 0.00000000]]}, # Sq dist
{'Segment': 1, 'Vector': 'durable', 'Offset': 3, 'Coefficients':[[ 0.00000019,  0.00000050, 0.00000000]]}, # Cube dist
{'Segment': 1, 'Vector': 'durable', 'Offset': 5, 'Coefficients':[[ 2.15, 1.95, -1]]}, # intrazonal
{'Segment': 1, 'Vector': 'durable', 'Offset': 8, 'Coefficients':[[ -5.12519108, -4.43614871, 0.00000000]]}, # intrazonal and usual workplace
]