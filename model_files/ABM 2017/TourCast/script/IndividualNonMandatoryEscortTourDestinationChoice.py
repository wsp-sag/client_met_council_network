####################################################################
# IndividualNonMandatoryEscortTourDestinationChoice.py
#   this component uses size functions and logsums
####################################################################

from Globals import * # for numberOfZones, placeholder, purposeXxxx, incXxxx

# Size Function defined in another file to reduce clutter here
import TourDestinationChoiceSizeFunction_IndividualNonMandatoryEscort as sizeFunction

# the name of the corresponding class on the C# side:
# this allows for multiple scripts targeting the same component
modelComponentName="TourDestinationChoiceINMEscort"  

# this is merely informative and doesn't instigate any activity: 
# it indicates the logsum component that should be instantiated,
# and which should then be set as the TourModeChoiceLogsum property on TourDestinationChoiceINMEscort
logsumGeneratorName="TourModeChoiceLogsumINMEscort"

# TODO: I think this will be used by the Model component factory to hand the component the correct logit object
# in AA we hardwired this in the component
logitType="MultinomialLogit"

# introducing parameters, used for running same model component for, in this case:
#  modeling tours for particular purpose
#  university tours do not use segmented size function or location set but the other purposes do
# 
parameters= {
             "tourPurposeDescription": "Individual Non Mandatory Escort Tours",
             "tourPurposeIds": [purposeIndNonMnd + purposeEscort],##Escort outing purposes plus INM flag.  
             "fullyJoint": False,
             "usesTransitAccessMatrix" : True,  
             "locationSetIsSegmented":True,
             "sizeFunctionIsSegmented":True
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
##Time Of Day Distributions for all Individual Non Mandatory Types
 #Non-School Escort Tours
 {"type" : "constantsgrid",
  "dataType":"double",
  "name" : "TimeOfDayArriveReturnDistributionEscortTours",
  "columns" : ["returnAM", "returnMD", "returnPM", "returnNT"],
  "rows" : ["arriveAM", "arriveMD", "arrivePM", "arriveNT"],
  "values" : [
              [0.205340007, 0.023031843, 0.006294876, 0.001330859], # arriveAM
              [0.000000000, 0.228289037, 0.019243951, 0.002542078], # arriveMD
              [0.000000000, 0.000000000, 0.269061606, 0.080875012], # arrivePM
              [0.000000000, 0.000564723, 0.000000000, 0.163426008]  # arriveNT
             ]
 },




 
##  Stops Distributions
    {"type" : "constantsgrid",
    "dataType":"double",
    "name" : "StopsOnHalfTourDistributionEscort",
    "columns" : ["HT2_zero", "HT2_one", "HT2_two", "HT2_three"],
    "rows" : ["HT1_zero", "HT1_one", "HT1_two", "HT1_three"],
    "values" : [[0.796807867, 0.059459509, 0.011717271, 0.003205062], #HT1_zero (values for HT2)
                [0.075345519, 0.009171394, 0.001556624, 0.001147893], #HT1_one (values for HT2)
                [0.022919595, 0.000516438, 0.002062087, 0.000000000], #HT1_two (values for HT2)
                [0.013200558, 0.001824064, 0.001066119, 0.000000000]  #HT1_three (values for HT2)
            ]
},
##Stop Purpose Distribution
    {"type" : "constantsgrid",
    "dataType":"double",
    "name" : "StopPurposeDistributionEscort",
    "columns" : ["Work", "Univer", "School", "Meal", "Shop", "PerBus", "Social", "Escort"],  
    "rows" : ["HT1", "HT2"],
    "values" : [
                [0.000000000, 0.000000000, 0.000000000, 0.010398255, 0.060388971, 0.051553793, 0.067851926, 0.809807055],  # HT1 dist
                [0.000000000, 0.000000000, 0.000000000, 0.087974661, 0.119792747, 0.096750715, 0.235978871, 0.459503006]  # HT2 dist
            ] 
},
    {"type" : "dbffile",
     "name" : "Persons",  # this household data is needed only to feed to the logsum; note vars noCarsInHh and nCars, while household, will be supplied by NCarsFromAA
     "filename" : cube___PERSONS_FILE___, # file paths MUST BE RAW strings (open quote preceded by 'r')
     "columns" : ["personId", "hhid", "HHZON", "age", "gender"]  #gender appears to be unused
    },
        
    {"type" : "dbffile",
     "dataType" : "int",
     "name" : "PersonsModeledData",
     "filename" : cube___DAILY_ACTIVITY_PATTERNS___, # may substitute another downstream item later
     "columns" : [
                "personId",
                "hhId",
                "homeZoneId",
                "DAPId",
                ]
    },

    {"type" : "dbffile",
     "name" : "HouseholdBaseData",  # this household data is needed only to feed to the logsum; note vars noCarsInHh and nCars, while household, will be supplied by NCarsFromAA
     "filename" : cube___HOUSEHOLDS_FILE___, # file paths MUST BE RAW strings (open quote preceded by 'r')
     "columns" : ["hhid", "hhinc5s", "hhzon", "hh1Person","hftw","hptw","hhsize","hchildren", "hworkers"]
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


    {"type" : "dbffile",
     "name" : "SchoolEscortTours",     
     "filename" : cube___SCHOOL_ESCORT_TOURS___, # file paths MUST BE RAW strings (preceded by 'r')
     "columns" : [
                     "personId",
                     "persTourId",
                     "homeZoneId",
                     # using '@' in data source name indicates this field is generated by the component, so requires some coordination with C# code
                    ]
    },
    # if we had an Id source we could reduce the compound key to simple key
    {"type" : "dbffile",
     "name" : "FullyJointTours",     
     "filename" : cube___FULLY_JOINT_TOURS___, # file paths MUST BE RAW strings (preceded by 'r')
     "columns" : [
                  "person1Id", # part 1 of pk: using first person in tour
                  "tourId",   # part 2 of pk: tourId starting from 5 for joint tours 
                  "homeZoneId",
                 ] 
    }, 
    # output from IndNonMnd Generation model
    {"type" : "dbffile",
     "name" : "IndNonMndTours",
     "filename" : cube___INDIVIDUAL_NON_MANDATORY_TOURS___, # file paths MUST BE RAW strings (open quote preceded by 'r')
     "columns" : [
                    "personId", 
                    "tourId",   
                    "tourType", 
                    "homeZnId",
                    "nINMTours",
					"nTours",
					"adult1Kids"					
                  ],
        "deferredLoad" : True
    },

    {"type" : "dbffile",
     "name" : "Zones",
     "filename" : cube___ZONES_FILE___, # file paths MUST BE RAW strings (preceded by 'r')
     "columns" : ["zoneId",  # 0 
                  "mix_dens",# 1 MAIN MODEL
                  "rst_emp", # 2 MAIN MODEL
                  "tw_acc",  # 3 MAIN MODEL (all transit access)
                  "tot_emp",  # 4 for size fn
                  "ret_emp",  # 5 for size fn
                  "med1_emp", # 6 for size fn
                  "med2_emp", # 7 for size fn
                  "ent_emp",  # 8 for size fn
                  "k12_emp",  # 9 for size fn
                  "households",  # 10 for size fn
                  "area",        # 11 for restaurant employment density main model
                  "cbd",
                  "nret_emp"
                  ]      
    },
     
    {"type" : "dbffile",
     "isOutput": "true",
     "name" : "OutputINMEscortTourDestinations",     
     "filename" : cube___INDIVIDUAL_NON_MANDATORY_ESCORT_TOUR_DESTINATION_CHOICES___, # file paths MUST BE RAW strings (preceded by 'r')
     # parameters could be generally of form source data reference : field
     "parameters" : [
                 ["PersonId", "personId"],  # first person assigned to this tour, part 1 of PK
                 ["tourId", "tourId"],   # part 2 of PK; joint tourIds are in range 5-6
                 ["hhId", "hhId"],
                 ["homeZoneId", "homeZoneId"],
                 ["@alternativeChosen", "destZoneId"], 
                 ["nINMTours","nINMTours"],
				 ["nTours",  "nTours"],
				 ["adult1Kids", "adult1Kids"], 						 
                 ["tourPurpose","tourPurpose"],
                ]
    },
   
    # dbf output spec; used in tests for inspecting whether results are reasonable
    {"type" : "delimited",
     "isOutput": "true",
     "name" : "OutputDestinationChoiceStats",     
     "filename" : cube___INDIVIDUAL_NON_MANDATORY_ESCORT_TOUR_DESTINATION_CHOICE_SUMMARY___, # file paths MUST BE RAW strings (preceded by 'r')             
     "parameters" : [
                       [ "StatLine", "AggregateData"],
                    ]
    },
         # for derived value to pass to size function as segmentation value
    {"type" : "memory",
     "dataType" : "int",
     "name" : "DerivedValuesForSizeFn",
     "columns" : [
                  "incomeSegment",   # size function
                  "hhSizeSegment",   # location set
                  "workerVehicleSegment" # location set
                  ]
    },
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
durableCoeffs=[ ##

[ 0.55566750], # ls # logsum 
[-0.00108354], # SDist # sqr dist 
[ 0.00000418], # CDist # cube dist 

[placeholder], # lDistHHLg # ln(dist+1) segmented by hhSize

[-0.27686860], # ldistu18 # ln(dist+1) - age < 18 
[-0.83111911], # intr # Intrazonal 

# destination only (preload)
[-1.19028108], # cd # CBD (term ==5) 
[-0.00012714], # HHDens # HH density 
[placeholder], # twacvehgw # Walk-Transit Available, segmented workers vs vehicles 

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

segmentDefinitions = [
# data range Is only income segment, as they all share a tour purpose (Escort) and are segmented only by income
#  friendly name     , input data ref, offset in input, range of values (order relates to coeff order in segmentCoeffMap)
 {'Name': 'hhsize 2 segments: <=2, more', 'DataRef': 'DerivedValuesForSizeFn','Offset': 1, 'DataRange': [0,1]},
 {'Name': 'workers vs vehicles', 'DataRef': 'DerivedValuesForSizeFn','Offset': 2, 'DataRange': [0,1]} # 1 = workers > vehicles
]

segmentCoeffMap = [
{'Segment': 0, 'Vector': 'durable', 'Offset': 3, 'Coefficients':[[-2.90093362, -2.51919943]]}, # ln(RT dist + 1) seg hhsize
{'Segment': 1, 'Vector': 'durable', 'Offset': 8, 'Coefficients':[[ 0.00000000,  0.14755730]]}, # tw_acc (workers > vehicles)
]