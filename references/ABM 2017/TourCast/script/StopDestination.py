####################################################################
# StopDestination.py
#   this component uses size functions
####################################################################

from Globals import * # for numberOfZones
from MatrixKeyValues import *

# Size Function defined in another file to reduce clutter here
import StopDestinationSizeFunction as sizeFunction

# the name of the corresponding class on the C# side:
# this allows for multiple scripts targeting the same component
modelComponentName="StopDestination"  

dataReferences = [


    {"type" : "constants",
     "name" : "OutOfVehicleFactorByTourPurpose",
     "columns" : ["school","work","university", "escort","fullyJoint", "workbased", "indNonMnd"],
     "values" : [2.0, 2.5, 2.0, 2.5, 2.5, 2.5, 2.5]
    },

    {"type" : "constants",
     "name" : "GeneralizedTimeCoeffsByTourPurpose",
     "columns" : ["school","work","university", "escort","fullyJoint", "workbased", "indNonMnd"],
     "values" : [-0.0200, -0.0088, -0.0200, -0.0200, -0.0428, -0.0200, -0.0070]
    },
   

    {"type" : "dbffile",
     "name" : "Stops",     
     "filename" : cube___STOP_GENERATION_STOPS_HOME_BASED___, # file paths MUST BE RAW strings (preceded by 'r')
     "columns" : [
                        "hhzon",
                        "hhinc5s",
                        "hhid",
                        "personId",
                        "personType",
                        "tourId",
                        "tourPurpose",
                        "stopId" ,
                        "halfTour",
                        "purpose",
                        "destZone",  # empty on input
                        "time"       # empty on input
                    ],
     "deferredLoad": True,
     },

    {"type" : "dbffile",
     "name" : "StopsWorkBased",     
     "filename" : cube___WORK_BASED_STOPS___, # file paths MUST BE RAW strings (preceded by 'r')
     "columns" : [
                        "hhzon",
                        "hhinc5s",
                        "hhid",
                        "personId",         
                        "personType",
                        "tourId",
                        "tourPurpose",
                        "stopId" ,
                        "halfTour",
                        "purpose",
                        "destZone",  # empty on input
                        "time"       # empty on input
                    ],
     "deferredLoad": True,
     },

   {"type" : "dbffile",
     "name" : "Tours",     
     "filename" : cube___STOP_GENERATION_TOURS_HOME_BASED___, # file paths MUST BE RAW strings (preceded by 'r')
     "columns" : [
                        "personId",
                        "hhId",
                        "persTourId",
                        "tourPurp", 
                        "arrival",
                        "departure",
                        "homeZoneId",
                        "destZoneId",
                       # columns specific to this input below; keep other columns in same order as for ToursWorkBased
                        "noStopTour",
                        "esPrsOutId",
                        "esTrOutId",
                        "esPrsInId",
                        "esTrInId",
                    ],
     "deferredLoad": True,
     },

   {"type" : "dbffile",
     "name" : "ToursWorkBased",     
     "filename" : cube___WORK_BASED_TOUR_TIME_OF_DAY_CHOICE___, # file paths MUST BE RAW strings (preceded by 'r')
     "columns" : [
                       "personId",
                       "hhId",
                       "persTourId",
                       "tourPurp", 
                       "arrival",
                       "departure",
                       "homeZoneId",
                       "destZoneId", 
                       # columns specific to this input below; keep other columns in same order as for Tours
                       "origZoneId",
                       "parentMode",
                       "parArrive",
                       "parDepart",
                    ],
     "deferredLoad": True,
     },

   {"type" : "dbffile",
     "name" : "TourModeChoice",     
     "filename" : cube___HOME_BASED_TOUR_MODE_CHOICE___, # file paths MUST BE RAW strings (preceded by 'r')
     "columns" : [
                       "personId",  # part 1 of tour pk, for individual tours would be same as person id
                        "persTourId",
                        "homeZoneId", # for chunking
                        "tourMode" # numerical value of TourMode enum 
                    ],
     "deferredLoad": True,
     },

   {"type" : "dbffile",
     "name" : "TourModeChoiceWorkBased",     
     "filename" : cube___WORK_BASED_TOUR_MODE_CHOICE___,
     "columns" : [
                       "personId",  # part 1 of tour pk, for individual tours would be same as person id
                        "persTourId",
                        "homeZoneId", # for chunking
                        "tourMode" # numerical value of TourMode enum 
                    ],
     "deferredLoad": True,
     },
     
     # for segmentation to pass to location set
    {"type" : "memory",
     "dataType" : "int",
     "name" : "DerivedValues",
     "columns" : [
                  "stopPurpose",  # mask incoming stop purpose with Work | University | Meal | Shop |SocialRecreation | Escort                  
                  "tourModeByHalfTour",  # abs(mode) if HT1, -abs(mode) if HT2
                  ]
    },
     # for derived value to pass to size function as segmentation value
    {"type" : "memory",
     "dataType" : "int",
     "name" : "DerivedValuesForSizeFn",
     "columns" : [
                  "compoundSegment", #Compound: Work stop/worker type/inc lo-hi (for size function
				  "uniTourOrStop",  # for size function
                  ]
    },
     
    {"type" : "dbffile",
     "name" : "Zones",
     "filename" : cube___ZONES_FILE___, # file paths MUST BE RAW strings (preceded by 'r')
     "columns" : [
                    "zoneId",      #          					
                    "term_time",   # 
					"rural",
					"cbd",
					# these for size function:
					"ret_emp",
					"nret_emp",
					"population",
					"enrolled2"
                  ]
    },

    # stops will be combined output for home-based and work-based
    {"type" : "dbffile",
     "isOutput": "true",
     "name" : "OutputStops",     
     "filename" : cube___STOP_DESTINATION_CHOICE___, # file paths MUST BE RAW strings (preceded by 'r')
     "parameters" : [
                       [ "hh zone", "hhzon"],
                       [ "hh inc 5 segments", "hhinc5s"],
                       [ "hhid", "hhid"],
                       [ "Person id", "personId"],
                       [ "Person Type", "personType"],
                       [ "tour", "tourId"],
                       [ "tour purpose", "tourPurpose"],
                       [ "stop", "stopId" ],
                       [ "half tour number", "halfTour"],
                       [ "stop purpose", "purpose"],
                       [ "@destination zone", "destZoneId"],
                       [ "@distance", "distance"],
                       [ "stop time", "time" ],   #empty? 
                       [ "tour mode", "tourMode"],
                       [ "location utility", "locUtil" ],
                       [ "size function value", "sizeFun" ],
                    ]
     },

    # dbf output spec; used in tests for inspecting whether results are reasonable
    {"type" : "delimited",
     "isOutput": "true",
     "name" : "OutputDestinationChoiceStats",     
     "filename" : cube___STOP_DESTINATION_CHOICE_SUMMARY___, # file paths MUST BE RAW strings (preceded by 'r')             
     "parameters" : [
                       [ "StatLine", "AggregateData"],
                    ]
    }

]


# Matrices are different enough to require their own structure:
matrixReferences = [

    {"type" : "matrix",
     "name" : "NonMotorized",
     "filename" : cube___NM_MATRIX___, 
     "matrixNames" : ["WALKDIST"]
    },

    # note same matrix file used twice here: 
    {"name" : "DistanceMatrixOD",
     "filename" : cube___OD_DISTANCE_MATRIX___, #NOTE: NOT CORRECT DATA: need a matrix with log(1 + round trip distance)
     "matrixNames" : ["a3pdist"] # using drive alone no tolls; 
    },

    {"type" : "matrix",
     "name" : "AMPeak",
     "isHighwayTimeSpanMatrix" : "true",
     "startTime" : "6.5", #6:30 am
     "endTime" : "8",  # 8 for an endTime means that this matrix includes up to the instant before 8:30AM (8:29:59.999...)
     "filename" : cube___AM_PEAK_MATRIX___, 
     "matrixNames" : [#"dapdist", "daptoll", "a2pdist", "a2ptoll", "a3pdist", "a3ptoll", 
                      "daptime", "a2ptime", "a3ptime"]
    },

    {"type" : "matrix",
     "name" : "Midday",
     "isHighwayTimeSpanMatrix" : "true",
     "startTime" : "8.5", #8:30 am
     "endTime" : "15", # ends at instant before 15:30
     "filename" : cube___MIDDAY_MATRIX___, 
     "matrixNames" : [#"dapdist", "daptoll", "a2pdist", "a2ptoll", "a3pdist", "a3ptoll", 
                      "daptime", "a2ptime", "a3ptime"]
    },

    {"type" : "matrix",
     "name" : "PMPeak",
     "isHighwayTimeSpanMatrix" : "true",
     "startTime" : "15.5", 
     "endTime" : "18", # ends at instant before 18:30
     "filename" : cube___PM_PEAK_MATRIX___, 
     "matrixNames" : [#"dapdist", "daptoll", "a2pdist", "a2ptoll", "a3pdist", "a3ptoll", 
                      "daptime", "a2ptime", "a3ptime"]
    },

    {"type" : "matrix",
     "name" : "Overnight",
     "isHighwayTimeSpanMatrix" : "true",
     "startTime" : "18.5", #6:30 pm
     "endTime" : "6",  # wrap around midnight is OK; ends at instant before 6:30 AM
     "filename" : cube___OVERNIGHT_MATRIX___, 
     "matrixNames" : [#"dapdist", "daptoll", "a2pdist", "a2ptoll", "a3pdist", "a3ptoll", 
                      "daptime", "a2ptime", "a3ptime"]
    },

    {"type" : "matrix",
     "name" : "PeakWalkToTransit",
     "filename" : cube___PEAK_WALK_TO_TRANSIT_MATRIX___, 
     "matrixNames" : ["WLKACC", "TRNTIME", "WLKXFER", "WLKEGR", "IWAIT", "XWAIT"]
     #"matrixNames" : ["FARE", "TRNTIME", "WLKACC", "WLKXFER", "WLKEGR", "IWAIT", "XWAIT"]
    },

    {"type" : "matrix",
     "name" : "PeakDriveToTransit",
     "filename" : cube___PEAK_DRIVE_TO_TRANSIT_MATRIX___, 
     "matrixNames" : ["DRACC", "TRNTIME", "WLKXFER", "WLKEGR", "IWAIT", "XWAIT"]
     #"matrixNames" : ["FARE", "DRACC", "TRNTIME", "WLKACC", "WLKXFER", "WLKEGR", "IWAIT", "XWAIT"] # note there's a WLKACC core that's all zeros here
    },

    {"type" : "matrix",
     "name" : "OffPeakWalkToTransit",
     "filename" : cube___OFF_PEAK_WALK_TO_TRANSIT_MATRIX___, 
     "matrixNames" : ["WLKACC", "TRNTIME", "WLKXFER", "WLKEGR", "IWAIT", "XWAIT"]
     #"matrixNames" : ["FARE", "TRNTIME", "WLKACC", "WLKXFER", "WLKEGR", "IWAIT", "XWAIT"]
    },

    {"type" : "matrix",
     "name" : "OffPeakDriveToTransit",
     "filename" : cube___OFF_PEAK_DRIVE_TO_TRANSIT_MATRIX___, 
     "matrixNames" : ["DRACC", "TRNTIME", "WLKXFER", "WLKEGR", "IWAIT", "XWAIT"]
     #"matrixNames" : ["FARE", "DRACC", "TRNTIME", "WLKACC", "WLKXFER", "WLKEGR", "IWAIT", "XWAIT"]
    }
]



# ######################  model structure section  ##########################

# this is meant to represent the alternative output as either:
#    a real world value (e.g. that can be used in downstream utility functions 
#    or an ID of the alternative; in this case the values are zone ids
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
    [placeholder], # log(det),SEGMENTED BY Stop Purpose					#
    [placeholder], # log(det) SEGMENTED BY tour mode and half tour		#
    [placeholder], # log(det) IF work tour, SEGMENTED BY Stop Purpose	#
	[5.09730795], # (gtime(1)*(car+transit)) # GenAcc - motorized
	[-2.72601522], # (gtime(1)*(car+transit)*isfjnt) # GenAcc - motorized, Joint
	[-1.30331078], # (gtime(1)*(car+transit)*wrk) # GenAcc - motorized, work tour

	# can prefill:
	[ 0.98597394], # rur # Rural (term = 1) 
	[-0.75639980], # cd # CBD (term=5) 

	[ 0.73343810], # (twac(1)*transit) # TransitAvail - transit mode 

	[1.10535329], # (intr(1)*wk) # Intrazonal - walk
	[0.07303063], # (intr(1)*(wrk+sch+uni)) # Intrazonal - Mandatory Tour
	[0.32941452], # (intr(1)*(sshp)) # Intrazonal - shop stop

	# these should be reset when origin zone changes, 
	[0.84055505], # (bintr(1)*ht1*(wrk+sch+uni)) # Base zone - mandatory - HT1
	[0.43620852], # (bintr(1)*ht2*(wrk+sch+uni)) # Base zone - mandatory - HT2
	[0.1089871], # (bintr(1)*ht1*ifgt(tourpurp,4)) # Base zone - non-mandatory - HT1
	[0.64497239], # (bintr(1)*ht2*ifgt(tourpurp,4)) # Base zone - non-mandatory - HT2
	[ 1.00000000], # dummy for disqualifying location based on detour distance for bike and walk tours
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
# compound segment defined as follows: Mode * 1 for HT1; Mode * -1 for HT2;
{'Name': 'tourMode/halftour', 'DataRef': 'DerivedValues', 'Offset': 1,
 'DataRange': [
				1, # DriveAlone     HT1
                2, # SharedRide2    HT1
                3, # SharedRide3    HT1
                4, # WalkToTransit  HT1
                5, # DriveToTransit HT1
                6, # Walk           HT1
                7, # Bike           HT1
                8, # SchoolBus      HT1
			   -1, # DriveAlone     HT2
               -2, # SharedRide2    HT2
               -3, # SharedRide3    HT2
               -4, # WalkToTransit  HT2
               -5, # DriveToTransit HT2
               -6, # Walk           HT2
               -7, # Bike           HT2
               -8  # SchoolBus      HT2
                ]
 },

 {'Name': ' StopPurpose', 'DataRef': 'DerivedValues','Offset': 0, # 
  'DataRange': [
                1,  # School = 1,
                2,  # Work  = 2,
                4,  # University = 4,
                8,  # Meal = 8,
                16, # Shop = 16,
                32, # PersonalBusiness = 32,
                64, # SocialRecreation = 64,
                128 # Escort = 128,
                ]}
]
segmentCoeffMap = [
{'Segment': 0, 'Vector': 'durable', 'Offset': 1,  'Coefficients':[#lnDetourDist by mode and half tour
    [ 
		 0,          # DA HT1	
		-0.06994575, # (ldist(1)*sr2*ht1) # ln(detour dist + 1) - SR2 - HT1 
		 0.10318814, # (ldist(1)*sr3*ht1) # ln(detour dist + 1) - SR3 - HT1 
		-2.17222212, # (ldist(1)*transit*ht1) # ln(detour dist + 1) - WT - HT1 
		-2.17222212, # (ldist(1)*transit*ht1) # ln(detour dist + 1) - DT - HT1 
		-2.17816865, # (ldist(1)*wk) # ln(detour dist + 1) - Walk HT1
		-1.07784003, # (ldist(1)*bk) # ln(detour dist + 1) - Bike HT1
		 0,          # School Bus HT1	
		 0,		     # DA HT2	
		 0.11620085, # (ldist(1)*sr2*ht2) # ln(detour dist + 1) - SR2 - HT2 
		 0.29054043, # (ldist(1)*sr3*ht2) # ln(detour dist + 1) - SR3 - HT2 
		-0.28029281, # (ldist(1)*transit*ht2) # ln(detour dist + 1) - WT - HT2 
		-0.28029281, # (ldist(1)*transit*ht2) # ln(detour dist + 1) - DT - HT2 
		-2.17816865, # (ldist(1)*wk) # ln(detour dist + 1) - Walk HT2
		-1.07784003, # (ldist(1)*bk) # ln(detour dist + 1) - Bike HT2
		 0,           # School Bus HT2
    ]]},# log(det)  SEGMENTED BY tour mode/half tour
	
{'Segment': 1, 'Vector': 'durable', 'Offset': 0,  'Coefficients':[
   [
		 0.00000000, # School Stop 
		-1.36849629, # (ldist(1)*swrk) # ln(detour dist + 1) - Work Stop
		-0.19391765, # (ldist(1)*suni) # ln(detour dist + 1) - Uni Stop
		-2.09369235, # (ldist(1)*seat) # ln(detour dist + 1) - Meal Stop
		-2.31767046, # (ldist(1)*sshp) # ln(detour dist + 1) - Shop Stop
		-1.5189088, # (ldist(1)*smnt) # ln(detour dist + 1) - PersBus Stop
		-1.52463766, # (ldist(1)*sdsc) # ln(detour dist + 1) - SocRec Stop
		-1.35419912, # (ldist(1)*schf) # ln(detour dist + 1) - Escort Stop
    ]]},# log(det), SEGMENTED BY Stop Purpose

	{'Segment': 1, 'Vector': 'durable', 'Offset': 2,  'Coefficients':[
   [
		0, # School Stop
		0, # Work Stop
		0, # Uni Stop
		0.64759159, # (ldist(1)*seat*wrk) # ln(detour dist + 1) - Meal stop, work tour
		0.29437232, # (ldist(1)*sshp*wrk) # ln(detour dist + 1) - Shop stop, work tour
		-0.11738819, # (ldist(1)*smnt*wrk) # ln(detour dist + 1) - PersBus stop, work tour
		0.0113166, # (ldist(1)*sdsc*wrk) # ln(detour dist + 1) - SocRec stop, work tour
		-0.31003269, # (ldist(1)*schf*wrk) # ln(detour dist + 1) - Escort stop, work tour
		 
    ]]},# log(det), if work tour, SEGMENTED BY Stop Purpose

]

