####################################################################
# TourDestinationChoiceUniversity.py
#   this component uses size functions and logsums
####################################################################

from Globals import * # for numberOfZones

# Size Function defined in another file to reduce clutter here
import TourDestinationChoiceSizeFunction_University as sizeFunction

# the name of the corresponding class on the C# side:
# this allows for multiple scripts targeting the same component
modelComponentName="TourDestinationChoiceUniversity"  

# this is merely informative and doesn't instigate any activity: 
# it indicates the logsum component that should be instantiated,
# and which should then be set as the TourModeChoiceLogsum property on TourDestinationChoiceUniversity
# for University we're using the same logsum used by school location;
logsumGeneratorName="SchoolLocationTourModeChoiceLogsum"

# TODO: I think this will be used by the Model component factory to hand the component the correct logit object
# in AA we hardwired this in the component
logitType="MultinomialLogit"

# introducing parameters, used for running same model component for, in this case:
#  modeling tours for particular purpose
#  university tours do not use segmented size function or location set but the other purposes do
# 
parameters= {
             "tourPurposeDescription": "University Tours",
             "tourPurposeIds": [4],
             "fullyJoint": False,
             "usesTransitAccessMatrix" : False,
             "locationSetIsSegmented":True,
             "sizeFunctionIsSegmented":False,
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
    # values are in a grid just for clarity
    {"type" : "constantsgrid",
     "dataType":"double",
     "name" : "TimeOfDayArriveReturnDistribution",
     "columns" : ["returnAM", "returnMD", "returnPM", "returnNT"],
     "rows" : ["arriveAM", "arriveMD", "arrivePM", "arriveNT"],
     "values" : [#dep am    dep md    dep pm  dep nt
                 [0.006205348, 0.277663974, 0.056535937, 0.000000000], # arriveAM
                 [0.000000000, 0.312807787, 0.127415794, 0.024634900], # arriveMD
                 [0.000000000, 0.000000000, 0.007278538, 0.155972082], # arrivePM
                 [0.017383367, 0.000000000, 0.000000000, 0.014102273]  # arriveNT
                ]
    },
		
    # after running monte carlo on the probabilities in 
    # the TimeOfDayArriveReturnDistribution constantsgrid input
    # we use the choice to index into this array for the simulated arrival time
    # values are in a grid just for clarity
    {"type" : "constantsgrid",
     "dataType":"double",
     "name" : "ArrivalTimes",
     "columns" : ["returnAM", "returnMD", "returnPM", "returnNT"],
     "rows" : ["arriveAM", "arriveMD", "arrivePM", "arriveNT"],
     "values" : [#dep am   md    pm  nt
                     [7.0, 7.5,  8, 8.5,], # arriveAM
                     [10,  11,   12, 13], # arriveMD
                     [17,  17.5, 18, 18.5], # arrivePM
                     [20,  21,   22, 23]  # arriveNT
                ]
    },

    # after running monte carlo on the probabilities in 
    # the TimeOfDayArriveReturnDistribution constantsgrid input
    # we use the choice to index into this array for the simulated departure time
    # values are in a grid just for clarity
    {"type" : "constantsgrid",
     "dataType":"double",
     "name" : "DepartureTimes",
     "columns" : ["returnAM", "returnMD", "returnPM", "returnNT"],
     "rows" : ["arriveAM", "arriveMD", "arrivePM", "arriveNT"],
     "values" : [#dep am   md    pm    nt
                     [8,   11,   18,   21,], # arriveAM
                     [7,   10,   17,   22], # arriveMD
                     [6.5, 12,   18.5, 19.5], # arrivePM
                     [7.5, 13,   17.5, 20.5]  # arriveNT
                ]
    },

    {"type" : "dbffile",
     "name" : "Households",  # this household data is needed only to feed to the logsum; note vars noCarsInHh and nCars, while household, will be supplied by NCarsFromAA
     "filename" : cube___HOUSEHOLDS_FILE___, # file paths MUST BE RAW strings (open quote preceded by 'r')
     "columns" : ["hhid", "hhzon", "hhinc5s", "nKidsGT2", "hWorkers", "hstud", "hhsize", "hChild1", "hChild2"],
     #"sort" :  ["hhzon", "hhinc5s","hhid"] # original household data is sorted this way
    },

	#new for tbi:
    {"type" : "dbffile",
     "name" : "HouseholdPassModels",  # this household data is needed only to feed to the logsum; 
     "filename" : cube___PASS_MODEL___, 
     "columns" : ["hhid", "hhzon", "mnPass", "transPass"],
     #"sort" :  ["hhzon", "hhinc5s","hhid"] # implicit sort by hhinc5 though column is not present; original household data is sorted this way
    },
	
    {"type" : "dbffile",
     "name" : "FirstTours",
     "filename" : cube___DAILY_ACTIVITY_PATTERNS_FIRST_TOURS___, # file paths MUST BE RAW strings (open quote preceded by 'r')
     "columns" : [
                    "personId",    
                    "hhId",
                    "persTourId",  # pass-thru data for TOD
                    "tourPurp",    # used to id tours
                    "personType", # pass-thru data for TOD  THIS IS PTYPE2
                    "cType1",     # pass-thru data for TOD, also = pchild1 for logsum
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
                    "ctype",         # segmentation var here
                    "nCars",        # for logsum
                    "noCarsInHh"    # for here
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
                    "ctype",         # segmentation var here
                    "nCars",        # for logsum
                    "noCarsInHh"    # for here
                  ],
        "deferredLoad" : True
          # "sort": ["hhzon", "hhinc5s", "hhid", "ptype2"] this is the sort as originally from PreDAPDataAssembly, and thus from output of DAP
     },

	 
	 

    # code uses this to feed simulated arr/dep pair to logsum
    {"type" : "memory",
     "dataType" : "double",
     "name" : "SimulatedTourArrDep",
     "columns" : [
                  "arrival",
                  "departure"
                  ]
    },


     
     # this is here to define a simulated half tour column set
     # the code uses this as a template for data to feed to the logsum 
    {"type" : "memory",
     "dataType" : "int",
     "name" : "HalfTour",
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

    # a trick of sorts, just to provide a mapping for segmentation
    {"type" : "memory",
     "dataType" : "int",
     "name" : "DerivedValueForHhSizeSegmentation",
     "columns" : [
                  "hhSizeLt3"
                  ]
    },




    {"type" : "dbffile",
     "name" : "Zones",
     "filename" : cube___ZONES_FILE___, # file paths MUST BE RAW strings (preceded by 'r')
     "columns" : [
        "zoneId", 
# new for size function
        "Enrolled", 
        "enrolled2", 
        "enrolled5", 
        "enrolled10", 
        "NRET_EMP",
# other columns deleted for now
        ] # 20
    },

    # dbf output spec; used in tests for inspecting whether results are reasonable
    {"type" : "dbffile",
     "isOutput": "true",
     "name" : "OutputFirstTours",     
     "filename" : cube___UNIVERSITY_TOUR_DESTINATION_CHOICE_FIRST_TOURS___, # file paths MUST BE RAW strings (preceded by 'r')
     # parameters could be generally of form source data reference : field
     "parameters" : [
                 ["Persons", "personId"],
                 ["PersonTourId", "persTourId"],
                 ["homeZoneId", "homeZoneId"],
                 ["@alternativeChosen", "destZoneId"] # could be a pass-through depending on order of running dest
                ]
    },
    # dbf output spec; used in tests for inspecting whether results are reasonable
    {"type" : "dbffile",
     "isOutput": "true",
     "name" : "OutputSecondTours",     
     "filename" : cube___UNIVERSITY_TOUR_DESTINATION_CHOICE_SECOND_TOURS___, # file paths MUST BE RAW strings (preceded by 'r')
     # parameters could be generally of form source data reference : field
     "parameters" : [
                 ["Persons", "personId"],
                 ["PersonTourId", "persTourId"],
                 ["homeZoneId", "homeZoneId"],
                 ["@alternativeChosen", "destZoneId"] # could be a pass-through depending on order of running dest
                ]
    },



    # dbf output spec; used in tests for inspecting whether results are reasonable
    {"type" : "delimited",
     "isOutput": "true",
     "name" : "OutputDestinationChoiceStats",     
     "filename" : cube___UNIVERSITY_TOUR_DESTINATION_CHOICE_SUMMARY___, # file paths MUST BE RAW strings (preceded by 'r')             
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
    [ placeholder], # ln(dist+1) Segmented by hh size
    [ 2.21656494], # usualwp # usual workplace location 
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

#TODO: note the next comment no longer applies because destination choice architecture now has separate components 
# e.g. TourDestinationChoiceWork, TourDestinationChoiceUniversity; this also implies that locationSetIsSegmented is unneeded

#small problem here:  TourDestinationChoice is marked as ISegmented because some submodels are segmented;
# however, University destination is not segmented.  I'm putting in a dummy segmentation here, 
# Segmentation code will not be called in the component because locationSetIsSegmented is false in the parameters section above
segmentDefinitions = [
#  friendly name     , input data ref, offset in input, range of values (order relates to coeff order in segmentCoeffMap)
 {'Name': 'Household Size Less than 2', 'DataRef': 'DerivedValueForHhSizeSegmentation','Offset': 0, 'DataRange': [0,1]},
]

segmentCoeffMap = [
{'Segment': 0, 'Vector': 'durable', 'Offset': 1, 
  'Coefficients':
    [ 
        # hhsize >2,  hhsize <= 2
        [-1.31642292, -0.41839200]
        #[ -1.82, -0.918]
    ]
}

]