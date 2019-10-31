####################################################################                                                                                                                                                                                           
# TourTimeOfDaySubmodel_WorkBased.py
# Configuration script for Work Tour Time Of Day
# originally copied from work submodel
####################################################################                                                                                                                                                                                           
from Globals import * 

instantiationType="TimeOfDayComponent"

modelComponentName="TourTimeOfDaySubmodelWorkBased"

parameters={
			"OperatingCostCentsPerMile":autoOpCost
            }

dataReferences = [

    # this data will be fed to an instance of HouseholdDataUtility, along with the persons data ref following
    {"type" : "dbffile",
     "name" : "HouseholdBaseData",
     "filename" : cube___HOUSEHOLDS_FILE___, 
     "columns" : ["HHID", 
                  "HHINC5S", 
                  "HHZON"
                  ], 
     "deferredLoad" : True 
    },

    {"type" : "dbffile",
     "name" : "PersonBaseData",
     "filename" : cube___PERSONS_FILE___, 
     # Column names are uppercase in this file
     "columns" : [
                  "personId",
                  "HHID", 
                  "HHINC5S", 
                  "HHZON", 
                  "ptypeDAP", 
                  "gender",
                  "age"
                  ],

     "deferredLoad" : True 
    },

    {"type" : "dbffile",
     "dataType" : "int",
     "name" : "HouseholdModeledData",
     "filename" : cube___MODELED_HOUSEHOLDS_FILE___, 
     "columns" : [
                "hhId",         # 00
                "homeZoneId",   # 01
                "nC_SAH",       # 26
                ],
     "deferredLoad" : True 
},

   # submodel needs information from parent tours so will need to consolidate this info
   # from work tours in the TOD
   {"type" : "dbffile",
     "name" : "TODToursDAPFirst",     
     "filename" : cube___DAP_TOUR_TIME_OF_DAY_CHOICE_FIRST_TOURS___, 
     # parameters could be generally of form source data reference : field
     "columns" : [
                    "personId",
                    "hhId",
                    "persTourId",
                    "homeZoneId",
                    "tourPurp",
                    "arrival",
                    "departure"
                 ]
    },
   
    {"type" : "dbffile",
     "name" : "TODToursDAPSecond",     
     "filename" : cube___DAP_TOUR_TIME_OF_DAY_CHOICE_SECOND_TOURS___, 
     # parameters could be generally of form source data reference : field
     "columns" : [
                    "personId",
                    "hhId",
                    "persTourId",
                    "homeZoneId",
                    "tourPurp",
                    "arrival",
                    "departure"
                 ]
    },


    # Tours will be passed in from main model component
    {"type" : "memory",
     "dataType" : "int",
     "name" : "Tour",
     "columns" : [                  
                    "personId", 
                    "persTourId",   
                    "tourPurp", 
                    "hhId",
                    "origZoneId",
                    "homeZoneId",
                    "hhinc5s",
                    "destZoneId",
                    "parTourId"
                  ]
    },

    {"type" : "memory",
     #"dataType" : "int",
     "name" : "DerivedTour", # shift variables  #OKWB
     "columns" : [
                  "isFtw",            #Full Time
                  "hiInc",            #High Income ( > 100k, from looking at work submodel)
                  "loInc",            #Low Income (< 50K; from looking at work submodel)
                  "agegt35",	      #age > 35yrs old
                  "male",       	  #Gender
                  "mealPurp",         #Meal
                  "shopPurp",         #Shop
                  "perBusPurp",       #Personal Business
                  "socRecPurp",        #Social/Recreational
                  "workPurp"          #work
                  ]
     },


    # Special school tour type indicator flags, unused for work-based subtours
    {"type" : "constants",  #OKWB
     "dataType":"int",
     "name" : "TourTypeFlags",
     "columns" : ["dummyUnused"],
     "values" : [0]
    },


    # there are no alt-specific values for work-based  #OKWB
    # not sure if I need to specify any columns
    {"type" : "memory",  
     "dataType" : "double",
     "name" : "AlternativeSpecificValues",
     "columns" : [
                  "dummy"
                  ]
    },

]

# Times are shifted three hours earlier to account for the 3am model start time
# and multiplied by 2 to allow for integer indexes 0 - 47
# E.g. 3am -> 0, 4.5 -> (4.5 - 3) * 2 = 3, 
# 5pm = 17 -> (17 - 3) * 2 = 28, 24  -> 42, 2am -> (2 - 3 + 24) * 2 = 46
from itertools import chain

arrivalConsts = list(chain(
				[-2.153 ] * 6, #[3-6)
				[-1.915 ] * 6, #[6-9)
				[-1.152 ] * 4, #[9-11)
				[-0.464 ] * 1, #11
				[ 0.130 ] * 1, #11.5
				[ 0.000 ] * 1, #12 (BASE)
				[-0.469 ] * 1, #12.5
				[-0.815 ] * 2, #[13-14)
				[-1.237 ] * 6, #[14-17)
				[-0.676 ] * 6, #[17-20)
				[-0.713 ] * 14,# [20-3)
                ))

departureConsts = list(chain(
				[-0.737 ] * 7, # [3-6.5) 
				[-0.910 ] * 5, # [6.5-9) 
				[-1.102 ] * 4, # [9-11) 
				[-0.675 ] * 2, # [11-12) 
				[-0.115 ] * 1, # 12 
				[0.000  ] * 1, # 12.5 (BASE) 
				[-0.199 ] * 1, # 13 
				[-0.534 ] * 1, # 13.5 
				[-0.937 ] * 2, # [14-15) 
				[-1.622 ] * 1, # [15-15.5) 
				[-2.002 ] * 5, # [15.5-18) 
				[-2.991 ] * 1, # [18-18.5) 
				[-2.423 ] * 5, # [18.5-21) 

				[-3.974 ] * 12, # [21-3) 
                ))

durationConsts = list(chain(  #
				[0.000  ] * 2, # 0.5 (BASE) 
				[-0.321 ] * 1, #1
				[-1.034 ] * 1, #1.5
				[-3.008 ] * 4, #[2-4)
				[-6.762 ] * 8, #[4-8)
				[-7.789 ] * 32,# [8-24)
                ))

#for i in range(48):
#    print (i/2.0 + 3) % 24, departureConsts[i]

#for i in range(48):
#    print (i/2.0) % 24, durationConsts[i]

arrivalPivot = 3     # for Work-based, not really a pivot.  Starts at beginning of day so
                     #only applies to arrival 'late' 
durationPivot = 0.5     # from H-GAC ABM - Tour Time of Day choice Model final.docx #OKWB

# for alternative-specific calculations that will be done in the subclass
# no alternative-specific variables for work-based TTOD:
derivedValueCoeffs= [[ 
                  ]]
derivedValueCoeffMap={
                      }


# Shift variables treated like coefficient array with theshift types (arrEarly/arrLate/durE, durL, dep) treated like alternatives
# CoeffMap use to match variables used to compute aggregate coefficient

shiftCoeffs=[
	 # arrival  # duration
	[ 0.14124098, 0.36388654], # FTWRKR
	[-0.05337299,-0.07546148], # INC100
	[-0.17486463,-0.45482400], # INC50
	[-0.11309226,-0.03047240], # AGEGR35
	[-0.03683135,-0.00221291], # MALE	
	[ 0.14654566,-0.33324942], # MEAL
	[ 0.24668949,-1.39414136], # SHOP
	[ 0.12990899,-0.61535027], # PersBus
	[ 0.05935557,-0.63265055], # SocRec
	[ 0.10817567, 0.69830330], # WORK
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
shiftCoeffMap={"DerivedTour" : [[0, 0, 10]] } 


tourCoeffs=[
    # coeffs associated with tour/person attribute and a specific arrival or departure time
    # not needed for work-based #OKWB
    #  630,	  700,	730,	800,	830,    900        230,	     300,	330,	400
    [0.000,	0.000,	0.000,	0.000,	0.000,	0.000,    0.000,	0.000,	0.000,	0.000], 
]

tourCoeffMap={"TourTypeFlags" : [[0, 0, 1]]}  #OKWB

congestionShifts=[0, 0, 0, 0] # amEarly, amLate, pmEarly, pmLate; not specified for work-based

autoTotGenTimeCoeff = -0.00492496 #  genTime

# these come from the Tour Mode Choice word document table 1
valueOfTime=[12.13, 12.13, 12.13, 12.13, 12.13]  

# Consistent with estimation file
outOfVehicleWeight = 2.5 

