####################################################################                                                                                                                                                                                           
# TourTimeOfDaySubmodelIndNonMand.py
# Configuration script for Work Tour Time Of Day
# originally copied from fully joint
####################################################################                                                                                                                                                                                           

from Globals import * 

instantiationType="TimeOfDayComponent"

modelComponentName="TourTimeOfDaySubmodelIndNonMand"

parameters = {
				"firstIndNonManTourId" : 50, # this should match the value in IndNonMnd.py
				"OperatingCostCentsPerMile":autoOpCost			  
             }


dataReferences = [


    {"type" : "dbffile",
     "name" : "HouseholdModeledData",
     "filename" : cube___MODELED_HOUSEHOLDS_FILE___, 
     "columns" : [
                  "hhid",       # 0
                  "homeZoneId",      # 1
                  "nC_SAH"      # 2
                  ],
     "deferredLoad" : True, # new parameter, for input Dbf only; cannot combine 'sort' parameter with this
     #"sort" : ["hhzon", "hhinc5s", "hhid"]   # sort parameter is not available when using deferredLoad
     #"maxrecords":20000
    },
    
    {"type" : "dbffile",
     "name" : "PersonBaseData",
     "filename" : cube___PERSONS_FILE___, 
     "columns" : [
                  "personid",   # 0
                  "hhid",       # 1
                  "hhzon",      # 2
                  "ptypeDAP",   # 3
                  "hhinc5s",    # 4 
                  "female",     # 20
				  "age"
                  ],
     "deferredLoad" : True, # new parameter, for input Dbf only; cannot combine 'sort' parameter with this
     #"sort" : ["hhzon", "hhinc5s", "hhid"]   # sort parameter is not available when using deferredLoad
     #"maxrecords":20000
    },
    


    # Tours will be passed in from main model component
    {"type" : "memory",
     "dataType" : "int",
     "name" : "Tour",
     "columns" : [                  
                    "personId", 
                    "tourId",   
                    "tourPurpose", 
                    "nInmTours",
                    "homeZoneId",
                    "destZoneId",
					"adult1Kids",
					"nTours"
                  ]
    },

    {"type" : "memory",
     #"dataType" : "int",
     "name" : "DerivedTour",
     "columns" : [
				  "hhIncLt2",		  # HH Income less than 50K
				  "hhIncEq4", 		  # HH Income > 100K
                  "xFtwOnTour",       # Full Time  (existence of ~ on tour)
                  "xPtwOnTour",       # Part Time  "
                  "xStudOnTour",      # University " 
                  "xSenOnTour",       # Senior     "
                  "xC2OnTour",        # Child 5-15 years old  "
                  "xC3OnTour",        # Child 16+ years old  "
				  "xMaleOnTour",	  # male "
				  "xAgeLt35",         # person age < 35
				  "adult1Kids", 	  # single parent
				  "multiTour",        # 2+ tours of any type
                  "xC123SAH",      # Child in hh with stay at home DAP 
                  "mealTour",      # Meal
                  "shopTour",      # Shop
                  "perBusTour",      # Personal Business
                  "socRecTour",      # Social/Recreational
                  "escortTour",      # escort
				  # not used in TBI, kept for backwards compatibility
                  "xNwaOnTour",       # Non-Worker "
                  "xOneTourInDay",    # only tour in day		
                  "xFemaleOnTour",     # female      "				  
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
    {"type" : "memory",
     "dataType" : "double",
     "name" : "AlternativeSpecificValues",
     "columns" : [
                    "mealLeaveAfter5", # Leave after 5PM: Meal (assuming leave == depart
                    "sRecLeaveAfter5", # Leave after 5PM: Social / Recreational (assuming leave == depart
                    "femaleTravel10PmTo3Am", # Female travel between 10pm and 3AM
                    "totalAvailTime",  # Total available time remaining
                    "totalAvailTimeIfToursRemaining", # Total available time remaining if there are more ind non-mand tours after this one
                    "arrPartUse", # Arrival period partially used
                    "depPartUse", # Departure period partially used
					"mealDurGe1h",# Meal tour, duration >= 1hr
                    "mealDur30",  # Meal tour, duration 0.5
                    "mealDur1h",  # Meal tour, duration 1
                    "mealDur90",  # Meal tour, duration 1.5
                    "mealDur2h",  # Meal tour, duration 2
                    "shopDur30",  # Shop tour, duration 0.5
                    "shopDur1h",  # Shop tour, duration 1
                    "shopDur90",  # Shop tour, duration 1.5
                    "shopDur2h",  # Shop tour, duration 2
                    "pBusDur30",  # pBus tour, duration 0.5
                    "pBusDur1h",  # pBus tour, duration 1
                    "pBusDur90",  # pBus tour, duration 1.5
                    "pBusDur2h",  # pBus tour, duration 2
                    "escortDur30",  # Escort tour, duration 0.5
                    "escortDur1h",  # Escort tour, duration 1
                    "escortDur90",  # Escort tour, duration 1.5
                    "escortDur2h",   # Escort tour, duration 2				
                  ]
    },

]

# Times are shifted three hours earlier to account for the 3am model start time
# and multiplied by 2 to allow for integer indexes 0 - 47
# E.g. 3am -> 0, 4.5 -> (4.5 - 3) * 2 = 3, 
# 5pm = 17 -> (17 - 3) * 2 = 28, 24  -> 42, 2am -> (2 - 3 + 24) * 2 = 46
from itertools import chain

arrivalConsts = list(chain(  #ok inm
				[-0.060 ] * 6, # [3-6) 
				[0.609  ] * 2, #  [6-7) 
				[1.176  ] * 2, #  [7-8) 
				[1.067  ] * 2, #  [8-9) 
				[0.894 ] * 2 , 	#	[9-10)
				[0.2 ] * 2 , 	#	[10-11)
				[0.633 ] * 2 , 	#	[11-12)
				[0.74 ] * 4 , 	#	[12-14)
				[0.928 ] * 4 , 	#	[14-16) 
				[1.274  ] * 2, #  [16-17) 
				[1.950  ] * 2, #  [17-18) 
				[2.349  ] * 2, #  [18-19) 
				[1.942  ] * 2, #  [19-20) 
				[1.389  ] * 4, #  [20-22) 
				[0.471  ] * 4, #  [22-24) 
				[-0.060 ] * 6  #  [24-3) 
                 ))

departureConsts = list(chain(  #ok inm
				[-3.229 ] * 6, # [3-6) 
				[-1.749 ] * 1, #  [6-6.5) 
				[-2.159 ] * 1, #  [6.5-7) 
				[-1.914 ] * 2, #  [7-8) 
				[-2.082 ] * 2, #  [8-9) 
				[-1.537 ] * 2, #  [9-10) 
				[-1.287 ] * 2, #  [10-11) 
				[-0.967 ] * 2, #  [11-12) 
				[-0.694 ] * 4, #  [12-14) 
				[-0.299 ] * 2, #  [14-15) 
				[0.000  ] * 2, #  [15-16) (BASE) 
				[0.118  ] * 2, #  [16-17) 
				[0.001  ] * 2, #  [17-18) 
				[-0.198 ] * 1, #  [18-18.5) 
				[-0.160 ] * 1, #  [18.5-19) 

				[0.112  ] * 2, #  [19-20) 
				[0.633  ] * 4, #  [20-22) 
				[0.181  ] * 4, # [22-24) 
				[-1.839 ] * 6  # [24-3) 
                             ))

durationConsts = list(chain(  #ok inm
				[0.040  ] * 2, # 0.5 
				[0.682  ] * 1, #  1 
				[0.929  ] * 1, #  1.5 
				[0.623  ] * 1, #  2 
				[0.000  ] * 1, #   2.5 (BASE) 
				[-0.128 ] * 1, # 3 
				[-0.137 ] * 1, # 3.5 
				[-0.149 ] * 2, #  [4-5) 
				[0.063  ] * 2, #  [5-6) 
				[-0.467 ] * 6, #  [6-9) 
				[1.194  ] * 6, #  [9-12) 
				[0.201  ] * 12, #  [12-18) 
				[0.817  ] * 12  #  [18-24) 
                            ))

#for i in range(48):
#    print (i/2.0 + 3) % 24, departureConsts[i]

#for i in range(48):
#    print (i/2.0) % 24, durationConsts[i]

arrivalPivot = 10.0      #ok inm # 10:00 am for non-mandatory tours
durationPivot = 2.5     #not used

# for alternative-specific calculations that will be done in the subclass
derivedValueCoeffs= [[ 
				  0.68963234  # (MEAL*IFGE(DEPMIDPT,17)) # Leave after 5PM: Meal (assuming leave == depart
				, 0.31299651  # (DSC*IFGE(DEPMIDPT,17)) # Leave after 5PM: Social / Recreational (assuming leave == depart
				, 0.44865122  # ((1-MALE)*IFGE(ARRMIDPT,22)) # Female travel between 10pm and 3AM
				, 0.54574488  # REM_TIME # Total available time remaining
				, 0.16222554  # (REM_TIME*TR_NMAN) # Total available time remaining if there are more ind non-mand tours after this one
				,-3.12553785  # PART_ARR # Arrival period partially used
				,-3.92430409  # PART_DEP # Departure period partially used
				, 1.36037521  # (MEAL*IFGE(DURTIME,1)) # Meal tour, duration >= 1hr
				, 0.74589519  # (MEAL*IFEQ(DURTIME,0.5))
				,-0.52490117  # (MEAL*IFEQ(DURTIME,1))
				,-0.67344301  # (MEAL*IFEQ(DURTIME,1.5))
				,-0.37506412  # (MEAL*IFEQ(DURTIME,2))
				, 1.26820564  # (SHOP*IFEQ(DURTIME,0.5))
				, 0.34756906  # (SHOP*IFEQ(DURTIME,1))
				,-0.68988589  # (SHOP*IFEQ(DURTIME,1.5))
				,-1.06665398  # (SHOP*IFEQ(DURTIME,2))
				, 0.75111407  # (MAINT*IFEQ(DURTIME,0.5)) # PersBus
				, 0.02136721  # (MAINT*IFEQ(DURTIME,1))
				,-0.51552938  # (MAINT*IFEQ(DURTIME,1.5))
				,-0.48633927  # (MAINT*IFEQ(DURTIME,2))
				,-0.50607416  # (ESC*IFEQ(DURTIME,0.5))
				,-2.47964129  # (ESC*IFEQ(DURTIME,1))
				,-2.46123285  # (ESC*IFEQ(DURTIME,1.5))
				,-1.60898052  #  (ESC*IFEQ(DURTIME,2))
                  ]]
derivedValueCoeffMap={"AlternativeSpecificValues" : [[0,0,24]]}


# Shift variables treated like coefficient array with theshift types (arrEarly/arrLate/durE, durL, dep) treated like alternatives
# CoeffMap use to match variables used to compute aggregate coefficient

shiftCoeffs=[  #ok inm
			 # arrEarly   # arrLate   # duration
			[-0.10854978,-0.03966976,-0.03916140], # INC50 # Income less than $50,000
			[ 0.02887780,-0.00337833,-0.03108428], # INC100 # Income greater than $100,000
			[ 0.30303479, 0.16848083, 0.06899286], # FTWRKR
			[ 0.12357019, 0.06268660, 0.05621528], # PTWRKR
			[ 0.31775031, 0.03597178, 0.21091994], # ADTST # Adult Student
			[ 0.02313143,-0.01690138,-0.01797771], # SENIOR
			[-0.06002824, 0.07986002, 0.07875673], # CHD515
			[ 0.16927107, 0.18552783, 0.15882073], # CHD16
			[ 0.04592438, 0.03557704,-0.01848469], # MALE
			[-0.03690265, 0.04295971, 0.09695765], # AGELT35
			[ 0.05061669, 0.02662820,-0.00475628], # SNGLPARENT # Single Parent
			[ 0.15628753, 0.09575412, 0.02492444], # ONETOUR # Two + tours (any type) in day
			[ 0.07629779, 0.06852372,-0.03607586], # HOMEKID # Child in hh with stay at home DAP
			[-0.72092279, -0.56800404, -0.31533556],  # MEAL
			[-1.07097533, -0.58500006, -0.88635504],  # Shop
			[-0.75637816, -0.69498152, -0.34430828],  # Personal Business
			[-0.38402266,-0.50998029, 0.00000000], # DSC # Social Recreational
			[-0.23171661, -0.47044794, -1.09076696],  # Escort
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
shiftCoeffMap={"DerivedTour" : [[0, 0, 18]]}


tourCoeffs=[
    #  630,	  700,	730,	800,	830,    900        230,	     300,	330,	400
    [0.000,	0.000,	0.000,	0.000,	0.000,	0.000,    0.000,	0.000,	0.000,	0.000], # not needed for Ind non mand
]

tourCoeffMap={"TourTypeFlags" : [[0, 0, 1]]}

congestionShifts=[0, 0, 0, 0] # amEarly, amLate, pmEarly, pmLate; not specified for inm tour

autoTotGenTimeCoeff = -0.01786614

# these come from the Tour Mode Choice word document 
valueOfTime=[3.28, 4.062, 5.312, 5.939, 8.859]  # $0-25K, $25-50K, $50-75K, $75-100K, $100K+

# 
outOfVehicleWeight = 2.0 

