####################################################################                                                                                                                                                                                           
# FullyJointTourTimeOfDaySubmodel.py
# Configuration script for Work Tour Time Of Day
# originally copied from work submodel
####################################################################                                                                                                                                                                                           

from Globals import *

instantiationType="TimeOfDayComponent"

modelComponentName="TourTimeOfDaySubmodelFullyJoint"

dataReferences = [




    # I think submodel will manage this data; retrieve a list any time zone changes
    {"type" : "dbffile",
     "name" : "FullyJointTourLinkTable",     
     "filename" : cube___FULLY_JOINT_TOUR_PERSON_LINK_TABLE___, # file paths MUST BE RAW strings (preceded by 'r')
     "columns" : [
                   "persTourId", # partial pk to FullyJointTours
                   "tourId",    # partial pk to FullyJointTours
                   "personId",    # person involved in tour
                   "homeZoneId", # for chunking
                   "ptypeDAP",     # for tod
                   "female",      # for tod
                   "xC123_SAH"     # for tod
                   ]
    }, 

    # Tours will be passed in from main model component
    {"type" : "memory",
     "dataType" : "int",
     "name" : "Tour",
     "columns" : [                  
                    "person1Id", 
                    "tourId",   
                    "tourPurp", 
                    "hhId",
                    "homeZoneId",
                    "hhinc5s",
                    "destZoneId"
                  ]
    },

    {"type" : "memory",
     #"dataType" : "int",
     "name" : "DerivedTour",
     "columns" : [
                  "xFtwOnTour",       # Full Time  (existence of ~ on tour)
                  "xPtwOnTour",       # Part Time  "
                  "xNwaOnTour",       # Non-Worker "	
				  "onlyFemaleOnTour", 
				  "onlyMaleOnTour",
                  "xC123SAH",# Child in hh with stay at home DAP 				  
                  "noAdultsOnTour",    # No adults in group 	
                  "groupSize3",# Group size = 3  
                  "mealTour",# Meal
                  "shopTour",# Shop
                  "perBusTour",# Personal Business
                  "socRecTour",# Social/Recreational			
				  # the rest are not used by TBI, but kept for backwards compatibility
                  "xStudOnTour",      # University " 
                  "xSenOnTour",       # Senior     "
                  "xFemaleOnTour",     # female      "
                  "xC1OnTour",     # Child 0-5 years old   "
                  "xC2OnTour",# Child 5-15 years old  "
                  "noChildrenOnTour",    # No children in group 
                  "groupSizeGt4",# Group size >= 4
                  ]
     },

    # Special school tour type indicator flags, unused here
    {"type" : "constants",
     "dataType":"int",
     "name" : "TourTypeFlags",
     "columns" : ["dummyUnused"],
     "values" : [0]
    },


    # tour variables needed for this:  tour purpose; Entourage vars needed: arrPartUse, depPartUse
	# NOTE: this must be the same size as the durable coefficients
    {"type" : "memory",
     "dataType" : "double",
     "name" : "AlternativeSpecificValues",
     "columns" : [
                    "sRecDuration3HrPlus", # 0 Greater than 3 hour duration: Social / Recreational
					"shopDuration3HrPlus", # 1 Greater than 3 hour duration: Shop
                    "mealLeaveAfter5", # 2 Leave after 5PM: Meal (assuming leave == depart					
                    "sRecLeaveAfter5", # 3 Leave after 5PM: Social / Recreational (assuming leave == depart
                    "arrPartUse", # 4 Arrival period partially used
                    "depPartUse", # 5 Departure period partially used
                    "mealDur30",  # 6 Meal tour, duration 0.5
                    "mealDur1h",  # 7 Meal tour, duration 1
                    "mealDur90",  # 8 Meal tour, duration 1.5
                    "mealDur2h",  # 9 Meal tour, duration 2
                    "shopDur30",  # 10 Shop tour, duration 0.5
                    "shopDur1h",  # 11 Shop tour, duration 1
                    "shopDur90",  # 12 Shop tour, duration 1.5
                    "shopDur2h",  # 13 Shop tour, duration 2
                    "pBusDur30",  # 14 PersBus tour, duration 0.5
                    "pBusDur1h",  # 15 PersBus tour, duration 1
                    "pBusDur90",  # 16 PersBus tour, duration 1.5
                    "pBusDur2h"  # 17 PersBus tour, duration 2					
                  ]
    },

]

# Times are shifted three hours earlier to account for the 3am model start time
# and multiplied by 2 to allow for integer indexes 0 - 47
# E.g. 3am -> 0, 4.5 -> (4.5 - 3) * 2 = 3, 
# 5pm = 17 -> (17 - 3) * 2 = 28, 24  -> 42, 2am -> (2 - 3 + 24) * 2 = 46
from itertools import chain

arrivalConsts = list(chain(
				[0.352  ] * 6, # [3-6) 
				[-0.674 ] * 2, #  [6-7) 
				[0.973  ] * 2, #  [7-8) 
				[0.935  ] * 2, #  [8-9) 
				[	2.004	] * 2, #  [9-10)
				[	3	] * 2, #  [10-11)
				[	2.74	] * 2, #  [11-12)
				[	2.809	] * 2, #  [12-13)
				[	3.309	] * 2, #  [13-14)
				[	2.817	] * 2, #  [14-15)
				[	0.817	] * 2, #  [15-16)
				[	1.325	] * 2, #  [16-17)
				[1.706  ] * 2, #  [17-18) 
				[2.242  ] * 2, #  [18-19) 
				[1.560  ] * 2, #  [19-20) 
				[0.684  ] * 4, #  [20-22) 
				[-2.187 ] * 4, #  [22-24) 
				[-2.187 ] * 6, #  [24-3) 
                 ))

departureConsts = list(chain(
				[-1.003 ] * 6, # [3-6) 
				[-0.249 ] * 1, #  [6-6.5) 
				[-0.308 ] * 1, #  [6.5-7) 
				[-0.873 ] * 2, #  [7-8) 
				[-0.585 ] * 2, #  [8-9) 
				[-0.568 ] * 2, #  [9-10) 
				[-0.761 ] * 2, #  [10-11) 
				[-0.587 ] * 2, #  [11-12) 
				[-0.619 ] * 4, #  [12-14) 
				[-0.074 ] * 2, #  [14-15) 
				[0.000  ] * 2, #  [15-16) (BASE) 
				[-0.140 ] * 2, #  [16-17) 
				[-0.595 ] * 2, #  [17-18) 
				[-0.730 ] * 1, #  [18-18.5) 
				[-0.591 ] * 1, #  [18.5-19) 

				[-0.316 ] * 2, #  [19-20) 
				[0.145  ] * 4, #  [20-22) 
				[-0.741 ] * 10, #  [22-3) 
                             ))

durationConsts = list(chain(
				[-0.255 ] * 2, # 0.5 
				[0.694  ] * 1, #  1 
				[0.426  ] * 1, #  1.5 
				[0.235  ] * 1, #  2 
				[0.000  ] * 1, #   2.5 (BASE) 
				[-0.795 ] * 2, #   [3-4) 
				[-0.870 ] * 2, #  [4-5) 
				[-4.087 ] * 2, #  [5-6) 
				[-3.636 ] * 6, #  [6-9) 
				[-5.231 ] * 6, #  [9-12) 
				[-5.231 ] * 12, #  [12-18) 
				[-5.231 ] * 12, #  [18-24) 
                            ))

#for i in range(48):
#    print (i/2.0 + 3) % 24, departureConsts[i]

#for i in range(48):
#    print (i/2.0) % 24, durationConsts[i]

arrivalPivot = 10.0      # 10:00 am for non-mandatory tours
durationPivot = 2.5     # Not used

# for alternative-specific calculations that will be done in the subclass
derivedValueCoeffs= [[ 
                     -0.20551767  # (DSC*IFGE(DURTIME,3)) # Social Recreational
					,0.29161054  # (SHOP*IFGE(DURTIME,3))
					,0.51570447  # (MEAL*IFGE(DEPMIDPT,17))
					,0.46917359  # (DSC*IFGE(DEPMIDPT,17))
					,-2.02513730  # PART_ARR
					,-3.00000000 #  PART_DEP
					,1.03245229  # (MEAL*IFEQ(DURTIME,0.5))
					,0.21514471  # (MEAL*IFEQ(DURTIME,1))
					,0.62495927  # (MEAL*IFEQ(DURTIME,1.5))
					,-0.44976307  # (MEAL*IFEQ(DURTIME,2))
					,1.35340683  # (SHOP*IFEQ(DURTIME,0.5))
					,0.20792975  # (SHOP*IFEQ(DURTIME,1))
					,0.06239222  # (SHOP*IFEQ(DURTIME,1.5))
					,-0.91326068  # (SHOP*IFEQ(DURTIME,2))
					,0.53641640  # (MAINT*IFEQ(DURTIME,0.5)) # Personal Business
					,-0.30359098  # (MAINT*IFEQ(DURTIME,1)) # Personal Business
					,-0.31352672  # (MAINT*IFEQ(DURTIME,1.5)) # Personal Business
					,-1.22921528  # (MAINT*IFEQ(DURTIME,2)) # Personal Business
                  ]]
derivedValueCoeffMap={"AlternativeSpecificValues" : [[0,0,18]]}


# Shift variables treated like coefficient array with theshift types (arrEarly/arrLate/durE, durL, dep) treated like alternatives
# CoeffMap use to match variables used to compute aggregate coefficient

shiftCoeffs=[
		 # arrEarly   # arrLate   # duration
		[ 0.19942553, 0.07402182,-0.01936693], # NFULT (existence of ~ on tour)
		[-0.18534829,-0.01363085, 0.10206717], # NPART "
		[ 0.07637143,-0.04964172,-0.05148783], # WRK_NON "
		[-0.41598235, 0.04845701, 0.10797408], # ONLY_FEM "
		[ 0.39920462, 0.13131742, 0.14028021], # ONLY_MALE "
		[ 0.24685437, 0.12838725, 0.00517935], # HOMEKID Child in hh with stay at home DAP 
		[-1.12117545,-0.08641826,-0.12353202], # ONLYCHILD No adults in group 
		[-0.23557564, 0.06092799, 0.16227931], # 3PPL Group size = 3  
		[-1.87811148,-0.27905013,-0.61935513], # MEAL
		[-1.80482610,-0.31776415,-1.16289516], # SHOP
		[-0.95398231,-0.38018757,-0.64780178], # MAINT Personal Business
		[-0.60568850,-0.30376648,-0.01241664]  # DSC Social/Recreational
]                                       

# CoeffMap={
#      {"Data reference name": [
#                                   [origin index in the data reference row, 
#                                    destination index in the Values array , 
#                                    number of consecutive values to copy from one to the other
#                                   ]
#                               ,...(optional additional ranges to copy in the same data reference)
#                              ]
#        ,... (additional data references as needed)     
#      }
shiftCoeffMap={"DerivedTour" : [[0, 0, 12]] }


tourCoeffs=[
    #  630,	  700,	730,	800,	830,    900        230,	     300,	330,	400
    [0.000,	0.000,	0.000,	0.000,	0.000,	0.000,    0.000,	0.000,	0.000,	0.000], # not needed for fully joint tour
]

tourCoeffMap={"TourTypeFlags" : [[0, 0, 1]]}

congestionShifts=[0, 0, 0, 0] # amEarly, amLate, pmEarly, pmLate; not specified for fully joint tour

autoTotGenTimeCoeff = -0.02127287

# these come from the Tour Mode Choice word document 
valueOfTime=[12.638, 12.638, 12.638, 12.638, 12.638]  # $0-25K, $25-50K, $50-75K, $75-100K, $100K+

# Set according to the ALogit file parameters
outOfVehicleWeight = 2.5 

