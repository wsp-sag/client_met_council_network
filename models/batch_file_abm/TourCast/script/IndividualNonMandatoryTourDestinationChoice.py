####################################################################
# IndividualNonMandatoryTourDestinationChoice.py
#   this component uses size functions and logsums
####################################################################

from Globals import * # for numberOfZones, placeholder, purposeXxxx, incXxxx


# Size Function defined in another file to reduce clutter here
import TourDestinationChoiceSizeFunction_IndividualNonMandatory as sizeFunction

# the name of the corresponding class on the C# side:
# this allows for multiple scripts targeting the same component
modelComponentName="TourDestinationChoiceIndNonMnd"  

# this is merely informative and doesn't instigate any activity: 
# it indicates the logsum component that should be instantiated,
# and which should then be set as the TourModeChoiceLogsum property on TourDestinationChoiceIndNOnMnd
logsumGeneratorName="TourModeChoiceLogsumIndNonMnd"

# TODO: I think this will be used by the Model component factory to hand the component the correct logit object
# in AA we hardwired this in the component
logitType="MultinomialLogit"

# introducing parameters, used for running same model component for, in this case:
#  modeling tours for particular purpose
#  university tours do not use segmented size function or location set but the other purposes do
# 
parameters= {
             "tourPurposeDescription": "Individual Non Mandatory Tours",
             "tourPurposeIds": [purposeIndNonMnd + purposeMeal, 
								purposeIndNonMnd + purposeShop,
								purposeIndNonMnd + purposePersonalBusiness,
								purposeIndNonMnd + purposeSocialRecreation,
							   ],##INM outing purposes plus INM flag.  NO ESCORT (handled separately)
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
#Meal Tours
{"type" : "constantsgrid",
    "dataType":"double",
    "name" : "TimeOfDayArriveReturnDistributionMealTours",
    "columns" : ["returnAM", "returnMD", "returnPM", "returnNT"],
    "rows" : ["arriveAM", "arriveMD", "arrivePM", "arriveNT"],
    "values" : [
                [0.036354395, 0.018651547, 0.000000000, 0.000000000], # arriveAM
                [0.000000000, 0.303199213, 0.030252224, 0.000677902], # arriveMD
                [0.000000000, 0.000000000, 0.218900975, 0.172985393], # arrivePM
                [0.000388268, 0.000000000, 0.000000000, 0.218590083]  # arriveNT
            ]
},       
#Shopping Tours
{"type" : "constantsgrid",
    "dataType":"double",
    "name" : "TimeOfDayArriveReturnDistributionShoppingTours",
    "columns" : ["returnAM", "returnMD", "returnPM", "returnNT"],
    "rows" : ["arriveAM", "arriveMD", "arrivePM", "arriveNT"],
    "values" : [
                [0.020102740, 0.012546480, 0.003768354, 0.000072936], # arriveAM
                [0.000000000, 0.468908096, 0.064168740, 0.002603869], # arriveMD
                [0.000000000, 0.000000000, 0.192336410, 0.077775475], # arrivePM
                [0.000000000, 0.002009675, 0.000000000, 0.155707225]  # arriveNT
            ]
},

#Personal Business Tours
{"type" : "constantsgrid",
    "dataType":"double",
    "name" : "TimeOfDayArriveReturnDistributionPBTours",
    "columns" : ["returnAM", "returnMD", "returnPM", "returnNT"],
    "rows" : ["arriveAM", "arriveMD", "arrivePM", "arriveNT"],
    "values" : [
                [0.039448016, 0.066859450, 0.018088174, 0.000273164], # arriveAM
                [0.000000000, 0.592518259, 0.072859303, 0.002960925], # arriveMD
                [0.000000000, 0.000000000, 0.111627998, 0.051180694], # arrivePM
                [0.000393655, 0.001776168, 0.000000000, 0.042014194]  # arriveNT
            ]
},

 #Social/Recreation Tours
 {"type" : "constantsgrid",
  "dataType":"double",
  "name" : "TimeOfDayArriveReturnDistributionSRTours",
  "columns" : ["returnAM", "returnMD", "returnPM", "returnNT"],
  "rows" : ["arriveAM", "arriveMD", "arrivePM", "arriveNT"],
  "values" : [
              [0.040133707, 0.041438630, 0.003523396, 0.001064676], # arriveAM
              [0.000000000, 0.236263617, 0.072565828, 0.012321602], # arriveMD
              [0.000000000, 0.000000000, 0.109371151, 0.252085905], # arrivePM
              [0.017487506, 0.000624294, 0.000000000, 0.213119688]  # arriveNT
             ]
 },
  
##  Stops Distributions
    {"type" : "constantsgrid",
    "dataType":"double",
    "name" : "StopsOnHalfTourDistributionMeal",
    "columns" : ["HT2_zero", "HT2_one", "HT2_two", "HT2_three"],
    "rows" : ["HT1_zero", "HT1_one", "HT1_two", "HT1_three"],
    "values" : [
              [0.448366717, 0.170343413, 0.035409016, 0.015400174], #HT1_zero (values for HT2)
              [0.127704501, 0.082555954, 0.022505679, 0.018530167], #HT1_one (values for HT2)
              [0.021380671, 0.030131488, 0.003069053, 0.000793221], #HT1_two (values for HT2)
              [0.012291621, 0.004631532, 0.001946517, 0.004940276]  #HT1_three (values for HT2)
            ]
},

    {"type" : "constantsgrid",
    "dataType":"double",
    "name" : "StopsOnHalfTourDistributionShopping",
    "columns" : ["HT2_zero", "HT2_one", "HT2_two", "HT2_three"],
    "rows" : ["HT1_zero", "HT1_one", "HT1_two", "HT1_three"],
    "values" : [[0.407303857, 0.153757270, 0.046642796, 0.043240825], #HT1_zero (values for HT2)
                [0.105453924, 0.073093313, 0.021430101, 0.016926842], #HT1_one (values for HT2)
                [0.027995925, 0.032395228, 0.008538744, 0.014270112], #HT1_two (values for HT2)
                [0.026440592, 0.013564838, 0.006408639, 0.002536994]  #HT1_three (values for HT2)
            ]
},
{"type" : "constantsgrid",
    "dataType":"double",
    "name" : "StopsOnHalfTourDistributionPB",
    "columns" : ["HT2_zero", "HT2_one", "HT2_two", "HT2_three"],
    "rows" : ["HT1_zero", "HT1_one", "HT1_two", "HT1_three"],
    "values" : [[0.366411834, 0.075692490, 0.024015412, 0.026815991], #HT1_zero (values for HT2)
                [0.192907869, 0.054535991, 0.021875355, 0.009460830], #HT1_one (values for HT2)
                [0.079774410, 0.026606092, 0.009216078, 0.003503546], #HT1_two (values for HT2)
                [0.080542796, 0.018879982, 0.005247289, 0.004514035]  #HT1_three (values for HT2)
            ]
},


    {"type" : "constantsgrid",
    "dataType":"double",
    "name" : "StopsOnHalfTourDistributionSR",
    "columns" : ["HT2_zero", "HT2_one", "HT2_two", "HT2_three"],
    "rows" : ["HT1_zero", "HT1_one", "HT1_two", "HT1_three"],
    "values" : [[0.754563308, 0.102437068, 0.020568908, 0.004418757], #HT1_zero (values for HT2)
                [0.060839363, 0.021684991, 0.003554778, 0.001705429], #HT1_one (values for HT2)
                [0.011003719, 0.004784288, 0.007865789, 0.000081370], #HT1_two (values for HT2)
                [0.002135897, 0.001854180, 0.000449696, 0.002052459]  #HT1_three (values for HT2)
            ]
},


##Stop Purpose Distribution
    {"type" : "constantsgrid",
    "dataType":"double",
    "name" : "StopPurposeDistributionMeal",
    "columns" : ["Work", "Univer", "School", "Meal", "Shop", "PerBus", "Social", "Escort"],  
    "rows" : ["HT1", "HT2"],
    "values" : [
                [0.000000000, 0.000000000, 0.000000000, 0.029596806, 0.000000000, 0.000000000, 0.672669142, 0.297734052],  # HT1 dist
                [0.000000000, 0.000000000, 0.000000000, 0.072067711, 0.000000000, 0.000000000, 0.698833852, 0.229098437]  # HT2 dist
            ] 
},

    {"type" : "constantsgrid",
    "dataType":"double",
    "name" : "StopPurposeDistributionShopping",
    "columns" : ["Work", "Univer", "School", "Meal", "Shop", "PerBus", "Social", "Escort"],  
    "rows" : ["HT1", "HT2"],
    "values" : [
                [0.000000000, 0.000000000, 0.000000000, 0.116152086, 0.259230358, 0.000000000, 0.436161896, 0.188455660],  # HT1 dist
                [0.000000000, 0.000000000, 0.000000000, 0.132476490, 0.359037644, 0.000000000, 0.360286698, 0.148199168]  # HT2 dist
            ] 


			
},  
    {"type" : "constantsgrid",
    "dataType":"double",
    "name" : "StopPurposeDistributionPB",
    "columns" : ["Work", "Univer", "School", "Meal", "Shop", "PerBus", "Social", "Escort"],  
    "rows" : ["HT1", "HT2"],
    "values" : [
                [0.000000000, 0.000000000, 0.000000000, 0.085142186, 0.198602434, 0.217130930, 0.340502235, 0.158622215],  # HT1 dist
                [0.000000000, 0.000000000, 0.000000000, 0.119271074, 0.406089778, 0.125037760, 0.245313233, 0.104288155]  # HT2 dist
            ] 
},



    {"type" : "constantsgrid",
    "dataType":"double",
    "name" : "StopPurposeDistributionSR",
    "columns" : ["Work", "Univer", "School", "Meal", "Shop", "PerBus", "Social", "Escort"],  
    "rows" : ["HT1", "HT2"],
    "values" : [
                [0.000000000, 0.000000000, 0.000000000, 0.000000000, 0.000000000, 0.000000000, 0.583425170, 0.416574830],  # HT1 dist
                [0.000000000, 0.000000000, 0.000000000, 0.000000000, 0.000000000, 0.000000000, 0.531025004, 0.468974996]  # HT2 dist
            ] 



},
    {"type" : "dbffile",
     "name" : "Persons",  # this household data is needed only to feed to the logsum; note vars noCarsInHh and nCars, while household, will be supplied by NCarsFromAA
     "filename" : cube___PERSONS_FILE___, # file paths MUST BE RAW strings (open quote preceded by 'r')
     "columns" : ["personId", "hhid","HHZON", "age","ptypeDAP","gender"],
     "deferredLoad": True
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
                ],
     "deferredLoad": True
    },

    {"type" : "dbffile",
     "name" : "HouseholdBaseData",  # this household data is needed only to feed to the logsum; note vars noCarsInHh and nCars, while household, will be supplied by NCarsFromAA
     "filename" : cube___HOUSEHOLDS_FILE___, # file paths MUST BE RAW strings (open quote preceded by 'r')
     "columns" : ["hhid", "hhinc5s", "hhzon", "hh1Person","hftw","hptw","hhsize","hchildren", "hChild1"],
     "deferredLoad": True
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


    # output from IndNonMnd Generation model
    
    {"type" : "dbffile",
     "name" : "SchoolEscortTours",     
     "filename" : cube___SCHOOL_ESCORT_TOURS___, # file paths MUST BE RAW strings (preceded by 'r')
     "columns" : [
                     "personId",
                     "persTourId",
                     "homeZoneId"
                     # using '@' in data source name indicates this field is generated by the component, so requires some coordination with C# code
                    ],
     "deferredLoad": True
    },
    # if we had an Id source we could reduce the compound key to simple key
    {"type" : "dbffile",
     "name" : "FullyJointTours",     
     "filename" : cube___FULLY_JOINT_TOURS___, # file paths MUST BE RAW strings (preceded by 'r')
     "columns" : [
                  "person1Id", # part 1 of pk: using first person in tour
                  "tourId",   # part 2 of pk: tourId starting from 5 for joint tours 
                  "homeZoneId",
                 ],
     "deferredLoad": True 
    }, 
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

    # from zone we need 
    # for main model:  
        #   Mixed Use Density
        #   Restaurant Employment Density
        #   Transit Accessibility
    #  main model size fn:  
    #      x total emp, 
    #      x ret_emp, 
    #      x medical type1 employment, 
    #      x medical type 2 employment, 
    #      x restaurant employment, 
    #      x Entertainment employment, 
    #        education employment k12
    #      x households
    # for logsums none (all matrix values)
    {"type" : "dbffile",
     "name" : "Zones",
     "filename" : cube___ZONES_FILE___, # file paths MUST BE RAW strings (preceded by 'r')
     "columns" : ["zoneId",      # 0
                  "mix_dens",    # 1 MAIN MODEL
                  "tw_acc",      # 2 MAIN MODEL (all transit access)
                  "rural",       # 3
                  "cbd",         # 4
                  "nret_emp",    # 5
                  "ret_emp",     # 6
                  "households",  # 7
                  ]      
    },
     
    {"type" : "dbffile",
     "isOutput": "true",
     "name" : "OutputINMTourDestinations",     
     "filename" : cube___INDIVIDUAL_NON_MANDATORY_TOUR_DESTINATION_CHOICES___, # file paths MUST BE RAW strings (preceded by 'r')
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
                 ["avgerage logsum", "avgLogsum"],
                 ["logsum range", "logsumRng"],
                ]
    },
   
    # dbf output spec; used in tests for inspecting whether results are reasonable
    {"type" : "delimited",
     "isOutput": "true",
     "name" : "OutputDestinationChoiceStats",     
     "filename" : cube___INDIVIDUAL_NON_MANDATORY_TOUR_DESTINATION_CHOICE_SUMMARY___, # file paths MUST BE RAW strings (preceded by 'r')             
     "parameters" : [
                       [ "StatLine", "AggregateData"],
                    ]
    },
         # for derived value to pass to size function as segmentation value
    {"type" : "memory",
     "dataType" : "int",
     "name" : "DerivedValuesForSizeFn",
     "columns" : [
                  "compoundSegmentTourPurposeAndIncome",
                  "segmentTourPurposeMasked"  # mask for Meal/shop/perbus/socrec/other (0)
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
    [ 0.43819523], # ls # logsum 
    [-0.00067058], # SDist # sqr dist 
    [ 0.00000084], # CDist # cube dist 
    [ placeholder], # ln(dist+1) - segmented by tour purpose
    [-0.13039044], # ldistdscch # ln(dist+1) - SocRec, Child 
    [-0.12924579], # ldistmntnm # ln(dist+1) - PB - NM Day 
    [ 0.16867332], # ldisteatnm # ln(dist+1) - Meal - NM Day 
    [-0.09385039], # ldistdscnm # ln(dist+1) - SocRec - NM Day 
    [ 0.79188214], # rur # Rural (term == 1) 
    [-0.80101153], # cd # CBD (term ==5) 
    [ 0.06982581], # twac # Walk-Transit Available 
    [-0.07067069], # twacvehgw # Walk-Transit Available, workers > vehicles 
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

segmentDefinitions = [
## Meal <20, Meal 20-40 Meal 40-70, Meal 70-100, Meal >100, Shop <20, Shop 20-40, Shop 40-70, Shop 70-100, Shop >100, Personal Business <20, Personal Business 20-40, Personal Business 40-70, Personal Business 70-100, Personal Business >100, Social/Recreation <20, Social/Recreation 20-40, Social/Recreation 40-70, Social/Recreation 70-100, Social/Recreation 100+
#  friendly name     , input data ref, offset in input, range of values (order relates to coeff order in segmentCoeffMap)
 {'Name': 'TourPurpose Masked', 'DataRef': 'DerivedValuesForSizeFn','Offset': 1, 
  'DataRange': [purposeMeal, purposeShop, purposePersonalBusiness, purposeSocialRecreation]}
]

segmentCoeffMap = [
{'Segment': 0, 'Vector': 'durable', 'Offset': 3, 'Coefficients':[
  [    
	-2.20917167	, # ldisteat # ln(dist+1) - Meal 
	-2.27820566	, # ldistshp # ln(dist+1) - Shopping 
	-2.02053304	, # ldistmnt # ln(dist+1) - Personal Business 
	-2.07251312	, # ldistdsc # ln(dist+1) - SocRec 
  ]]
 }, # ln (1 + RT dist)
]