####################################################################                                                                                                                                                                                           
# TourTimeOfDaySubmodel_SchoolUniversity.py
# Configuration script for testing School Tour Time Of Day
####################################################################                                                                                                                                                                                           

from Globals import * 

instantiationType="TimeOfDayComponent"

modelComponentName="TourTimeOfDaySubmodelSchoolUniversity"

dataReferences = [

    #  this will be populated automatically using extension map method anc copy method
    {"type" : "memory",
     "dataType" : "int",
     "name" : "Tour",
     "columns" : ["personid",       # 0
                  "perstourid",    # 1
                  "hhinc5s",         # 2
                  "ctype1",         # 3 used directly and for deriving values
                  "ctype2",         # 4 for deriving values, so need to map column id  
                  "ctype3",         # 5 for deriving values, so need to map column id 
                  "ctype4",         # 6 for deriving values, so need to map column id 
                  "ctype5",         # 7 used directly and for deriving values
                  "destZoneId",     # for deriving values,
                  "homeZoneId",     # for deriving values,
                  "tourCount",      # for deriving values,
                  "hhc1tour",       # for deriving values, so need to map column id 
                  "hhc2tour",       # for deriving values, so need to map column id 
                  "hhc3tour",       # for deriving values, so need to map column id 
                  "hhc4tour",       # for deriving values, so need to map column id 
                  "hhc5tour",       # for deriving values, so need to map column id 
                  "hhChildSah",     # for deriving values, so need to map column id 
                  "tourPurp",       # for deriving values, so need to map column id
                  "personType",     # for deriving values, so need to map column id
                  "male",            # for deriving values, so need to map column id
				  "age",
				  "hchild2",
				  "hchild3"
                  ]
    },

    # these derived values will be calculated in the specific submodel Run method
    {"type" : "memory",
     "name" : "DerivedTour",
     "columns" : [
                  "unipurpose",     # derived from tourPurp
                  "schoolpurpose",  # derived from tourPurp
                  "isftw",          # derived from personType
                  "isptw",          # derived from personType
                  "isas",           # derived adult student from personType
                  "xC123_SAH",       # derived from hhChildSah
				  "male",			# derived from tour
				  "agelt35",
				  "multiTour",  # more than 1 mandatory tour
				  "child2"
                  ]
    },

    # corresponding to the transientCoeffs array
    {"type" : "memory",
     "dataType" : "double",
     "name" : "AlternativeSpecificValues",
     "columns" : [
                  "arrPartUse", 
                  "depPartUse",
                  "siblingArrPeriod1+1",
                  "siblingDepPeriod1+1",
                  "siblingArrPeriod2+2",
                  "siblingDepPeriod2+2",         
                  "siblingArrPeriod3+3",
                  "siblingDepPeriod3+3",
                  "siblingArrPeriod4+4",
                  "siblingDepPeriod4+4",         
                  "siblingArrPeriod5+5",
                  "siblingDepPeriod5+5",
                  "childArrPeriod1",
                  "childDepPeriod1",
                  "childArrPeriod2",
                  "childDepPeriod2",         
                  "childArrPeriod3",
                  "childDepPeriod3",
                  "childArrPeriod4",
                  "childDepPeriod4",         
                  "childArrPeriod5",
                  "childDepPeriod5"     				  
                  ]
    },

    # Special school tour type indicator flags
    {"type" : "memory",
     "dataType" : "int",
     "name" : "TourTypeFlags",
     "columns" : ["chld2gtOneChld2", "chld2geOneChld3"]
    }
]

# Times are shifted three hours earlier to account for the 3am model start time
# and multiplied by 2 to allow for integer indexes 0 - 47
# E.g. 3am -> 0, 4.5 -> (4.5 - 3) * 2 = 3, 
# 5pm = 17 -> (17 - 3) * 2 = 28, 24  -> 42, 2am -> (2 - 3 + 24) * 2 = 46
from itertools import chain

arrivalConsts = list(chain(
	[-4.107 ] * 6, # [3-6) 
	[-1.354 ] * 1, # 6 
	[-0.538 ] * 1, # 6.5 
	[	1.09	] * 1, # 7
	[	0	] * 1, #  7.5 (BASE)
	[	-0.556	] * 1, # 8
	[	-0.071	] * 1, # 8.5
	[	0.719	] * 1, # 9
	[	0.789	] * 5, #  [9.5-12)
	[	1.303	] * 12, # [12-18)
	[	2.855	] * 18 # [18-3)
))

departureConsts = list(chain(
	[-2.118 ] * 7, # [3-6.5) 
	[-2.615 ] * 5, # [6.5-9) 
	[-2.118 ] * 6, # [9-12) 
	[-1.569 ] * 4, # [12-14) 
	[-0.301 ] * 2, # [14-15) 
	[0.000  ] * 1, # 15 (BASE) 
	[-0.196 ] * 1, # 15.5 
	[-0.359 ] * 1, # 16 
	[-0.585 ] * 3, # [16.5-18) 
	[-1.273 ] * 1, # [18-18.5) 
	[-1.031 ] * 5, # [18.5-21) 
	[-1.772 ] * 6, # [21-24) 
	[-4.264 ] * 6 #  [24-3) 
))

durationConsts = list(chain(
	[1.988  ] * 6, # [0-3) 
	[1.719  ] * 6, #  [3-6) 
	[1.977  ] * 2, # [6-7) 
	[2.384  ] * 1, # 7 
	[1.439  ] * 1, # 7.5 
	[0.000  ] * 1, #  8 (BASE) 
	[-0.043 ] * 1, # 8.5 
	[-0.197 ] * 1, # 9 
	[-0.398 ] * 1, # 9.5 
	[-1.041 ] * 2, # [10-11) 
	[-2.921 ] * 2, #  [11-12) 
	[-5.231 ] * 8, #  [12-16) 
	[-5.231 ] * 16 #  [16-24) 
))

#for i in range(48):
#    print (i/2.0 + 3) % 24, departureConsts[i]

#for i in range(48):
#    print (i/2.0) % 24, durationConsts[i]

arrivalPivot = 7.5      # 7:30 am
durationPivot = 8.0     # Not actually used for School tour, implicitly used in durationConsts

# for alternative-specific calculations that will be done in the subclass
derivedValueCoeffs= [
					[-3.00000000  # PART_ARR
					 ,-3.00000000,  # PART_DEP
                  0,  # siblingArrPeriod1+1, same arrival period (ctype1 + ctype1)
                  0,  # siblingDepPeriod1+1, same depature period (ctype1 + ctype1)                  
                  0, #1.000,  # siblingArrPeriod2+2, same arrival period (ctype2 + ctype2)
                  0, #1.000,  # siblingDepPeriod2+2, same depature period (ctype2 + ctype2)                  
                  0, #1.000,  # siblingArrPeriod3+3, same arrival period (ctype3 + ctype3)
                  0, #1.000,  # siblingDepPeriod3+3 same depature period (ctype3 + ctype3)                  
                  0, #1.000,  # siblingArrPeriod4+4, same arrival period (ctype4 + ctype4)
                  0, #1.000,  # siblingDepPeriod4+4, same depature period (ctype4 + ctype4)                  
                  0, #0.500,  # siblingArrPeriod5+5, same arrival period (ctype5 + ctype5)
                  0, #0.500   # siblingDepPeriod5+5, same depature period (ctype5 + ctype5)
                  # This next set applies to University Tours ONLY.
                  0,  # childArrPeriod1
                  0,  # childDepPeriod1
                  0, #1.000,  # childArrPeriod2
                  0, #1.000,  # childDepPeriod2
                  0, #1.000,  # childArrPeriod3
                  0, #1.000,  # childDepPeriod3
                  0, #1.000,  # childArrPeriod4
                  0, #1.000,  # childDepPeriod4
                  0, #0.500,  # childArrPeriod5
                  0, #0.500   # childDepPeriod5  					 
                  ]]
derivedValueCoeffMap={"AlternativeSpecificValues" : [[0,0,22]]}

# Shift variables treated like coefficient array with the three shift types (Early/Late/Duration) treated like alternatives
# CoeffMap use to match variables used to compute aggregate coefficient


shiftCoeffs=[
	 # arrEarly   # arrLate   # duration
	[ 0.27352593,-0.13658933, 0.14831242], # UNIV
	[ 0.80362631, 0.03284681, 0.48611696], # SCHOOL
	[-0.07944400, 0.09124669, 0.00485341], # FTWRKR
	[ 0.04889844,-0.01191321,-0.15339911], # PTWRKR
	[-0.21114822, 0.02755811,-0.08882105], # ADTST
	[ 0.05852650,-0.05905647,-0.23333787], # HOMEKID
	[-0.08706591, 0.03923777, 0.04830292], # MALE
	[ 0.12374848,-0.18875979,-0.19259391], # AGELT35
	[ 0.00211008, 0.15699143,-0.15548866], # ONETOUR  > 1 mandatory tours
	[-0.26021994,-0.11427494, 0.03248995]  # CHD515
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
shiftCoeffMap={"DerivedTour" : [[0, 0, 10]]}

tourCoeffs=[
  # arr630  # arr700 # arr730 # arr800 # arr830 # arr900 # dep230 # dep300 # dep330 # dep400 # dep430 # dep500 # dep530
  [ 0.42002, 0.53810, 0.77571, 0.32907, 0.49335, 1.23466, 0.60305, 0.96919, 1.20709, 0.75847, 0.15662, 0.15662, 0.15662], # child in 6-15 years with other children in 6-15 years
  [ 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 1.23841, 2.06271, 0.99682, 0.99682, 0.00000, 0.00000, 0.00000]  # child in 6-15 years with other children in 16+ years and no other children 5-15 years
]

tourCoeffMap={"TourTypeFlags" : [[0, 0, 2]]}

congestionShifts=[1.69972141, 2.39904130, 0.00000000, 0.00000000 ]  # amEarly, amLate, pmEarly, pmLate

autoTotGenTimeCoeff = -0.0030

valueOfTime=[4.286, 4.286, 4.286, 4.286, 4.286]  # $0-25K, $25-50K, $50-75K, $75-100K, $100K+

outOfVehicleWeight = 2.0

