####################################################################                                                                                                                                                                                           
# TourTimeOfDaySubmodel_Work.py
# Configuration script for Work Tour Time Of Day
####################################################################                                                                                                                                                                                           
from Globals import * 

instantiationType="TimeOfDayComponent"

modelComponentName="TourTimeOfDaySubmodelWork"

dataReferences = [

    # Tours will be passed in from main model component
    {"type" : "memory",
     "dataType" : "int",
     "name" : "Tour",
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
                  "tourCount", 
                  "hhc1tour", 
                  "hhc2tour", 
                  "hhc3tour", 
                  "hhc4tour",                   
                  "hhc5tour", 
                  "hhChildSah",
				  "adult1Kids"
                  ]
    },

    {"type" : "memory",
     #"dataType" : "int",
     "name" : "DerivedTour",
     "columns" : [
                  "ftw", 
                  "ptw", 
                  "stud", 
                  "sen", 
                  "hiInc", 
                  "loInc", 
                  "isWrkwStop",  # this tour has stops
                  "xChild_SAH",   # hhchildsah > 0 ? 1: 0
                  "adult1Kids",
				  "male",
				  "agelt35",
				  "multiTour"  # more than 1 mandatory tour
                  ]
     },

    # Special school tour type indicator flags, unused here
    {"type" : "constants",
     "dataType":"int",
     "name" : "TourTypeFlags",
     "columns" : ["dummyUnused"],
     "values" : [0]
    },

    # corresponding to the transientCoeffs array
    {"type" : "memory",
     "dataType" : "double",
     "name" : "AlternativeSpecificValues",
     "columns" : [
                  "highIncome", # high income working early or late
                  "ftwInPeak",
                  "ftw9HrDay",  # duration = 9 hours for FTW
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




]

# Times are shifted three hours earlier to account for the 3am model start time
# and multiplied by 2 to allow for integer indexes 0 - 47
# E.g. 3am -> 0, 4.5 -> (4.5 - 3) * 2 = 3, 
# 5pm = 17 -> (17 - 3) * 2 = 28, 24  -> 42, 2am -> (2 - 3 + 24) * 2 = 46
from itertools import chain

arrivalConsts = list(chain(
	[-0.408 ] * 4, # [3-5) AM 
	[0.120  ] * 2, #  [5-6) AM 
	[0.194  ] * 1, # 6:00 AM 
	[0.258  ] * 1, # 6.5 AM 
	[0.069  ] * 1, # 7:00 AM 
	[0.000  ] * 1, #  7.5 AM (BASE) 
	[-0.070 ] * 1, # 8:00 AM 
	[-0.482 ] * 1, # 8.5 AM 
	[-0.507 ] * 1, # 9:00 AM 
	[-1.002 ] * 1, # 9.5 AM 
	[-1.752 ] * 6, #  [10  AM-13 PM) 
	[-1.931 ] * 6, # [13-16) PM 
	[-2.005 ] * 6, # [16-19) PM 
	[-3.419 ] * 10, # [19-24) PM 
	[-6.539 ] * 6  # [24-3)  PM 
))

departureConsts = list(chain(
	[-3.375 ] * 6, # [3-6) AM 
	[-3.141 ] * 1, #  [6-6.5) AM 
	[-3.878 ] * 5, #  [6.5-9) AM 
	[-3.141 ] * 2, #  [9-10) AM 
	[-2.244 ] * 4, # [10-12) AM 
	[-1.739 ] * 4, # [12-14) PM 
	[-1.006 ] * 2, # [14-15) PM 
	[-0.417 ] * 1, # [15-15.5) PM 
	[-0.515 ] * 1, # [15.5-16) PM 
	[-0.148 ] * 1, # 16 PM 
	[0.023  ] * 1, # 16.5 PM 
	[0.000  ] * 1, # 17 PM (BASE) 
	[-0.423 ] * 1, # 17.5 PM 
	[-0.354 ] * 1, # 18 PM 
	[-0.330 ] * 1, # 18.5 PM 
	[-0.551 ] * 2, # [19-20) PM 
	[-0.412 ] * 2, # [20-21) PM 
	[-0.089 ] * 4, #  [21-23) PM 
	[-0.631 ] * 8 # [23 PM-3 AM) 
))

durationConsts = list(chain(
	[0.097  ] * 6, # [0-3) Hours 
	[0.758  ] * 6, #  [3-6) Hours 
	[0.162  ] * 2, # [6-7) Hours 
	[0.048  ] * 2, # [7-8) Hours 
	[0.132  ] * 1, # 8 Hours 
	[0.598  ] * 1, # 8.5 Hours 
	[0.000  ] * 1, #  9 Hours (BASE) 
	[-0.409 ] * 1, # 9.5 Hours 
	[-0.677 ] * 1, # 10 Hours 
	[-1.041 ] * 1, # 10.5 Hours 
	[-1.302 ] * 2, #  [11-12) Hours 
	[-1.799 ] * 2, #  [12-13) Hours 
	[-2.889 ] * 6, #  [13-16) Hours 
	[-5.655 ] * 16 #  [16-24)   Hours 
))

#for i in range(48):
#    print (i/2.0 + 3) % 24, departureConsts[i]

#for i in range(48):
#    print (i/2.0) % 24, durationConsts[i]

arrivalPivot = 7.5      # 7:30 am
durationPivot = 9.0     # 

# for alternative-specific calculations that will be done in the subclass
derivedValueCoeffs= [
					[-0.46263652  # (ERLYLTSHFT*INC100) # highIncome, arrival time <=5.5 or return time >= 22
					,0.48522322  # (PKPERTRAV*FTWRKR) # ftwInPeak, full time worker AND arrival time is 6.5 to 8.5 AND return time is 15.5 to 18
					,-0.66037006,  # (NINEHOURS*FTWRKR) # ftw9HrDay, duration = 9 hours for FTW
                  0, # childArrPeriod1
                  0, # childDepPeriod1					
                  0, # childArrPeriod2
                  0, # childDepPeriod2
                  0, # childArrPeriod3
                  0, # childDepPeriod3
                  0, # childArrPeriod4
                  0, # childDepPeriod4
                  0, # childArrPeriod5
                  0, # childDepPeriod5							
                  ]]
derivedValueCoeffMap={"AlternativeSpecificValues" : [[0,0,13]]}


# Shift variables treated like coefficient array with theshift types (arrEarly/arrLate/durE, durL, dep) treated like alternatives
# CoeffMap use to match variables used to compute aggregate coefficient

shiftCoeffs=[
	 # arrEarly   # arrLate   # durEarly  # durLate   # departure
	[-0.38666865,-0.26249220,-0.16854719,-0.28085010, 0.00000000], # FTWRKR
	[-0.42574087,-0.19564712, 0.04621678,-0.42401573, 0.00000000], # PTWRKR
	[-0.26681600,-0.32305059, 0.18185286,-0.30261394, 0.00000000], # ADTST
	[-1.00695530,-0.20480208, 0.22935675,-0.19018762, 0.00000000], # SENIOR
	[-0.22580820,-0.00872756, 0.00645817, 0.01236460, 0.00000000], # INC100
	[ 0.07669028, 0.01857791, 0.05153411,-0.10914252, 0.00000000], # INC50
	[-0.57632051, 0.15797039, 0.00000000, 0.00000000,-0.23910186], # HASSTOPS
	[-0.14918324,-0.11057814, 0.07930287,-0.00816046, 0.00000000], # HOMEKID
	[ 0.00927049, 0.01075440,-0.05097174,-0.03322472, 0.00000000], # SNGLPARENT
	[ 0.33743527, 0.05992947, 0.00154240, 0.12070043, 0.00000000], # MALE
	[ 0.01836640, 0.10061492,-0.15335578,-0.13376433, 0.00000000], # AGELT35
	[ 0.25269654, 0.12120764, 0.37662849,-1.35458078, 0.00000000], # ONETOUR  > 1 mandatory tours
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
    [0.000,	0.000,	0.000,	0.000,	0.000,	0.000,    0.000,	0.000,	0.000,	0.000], # not needed for work tour
]

tourCoeffMap={"TourTypeFlags" : [[0, 0, 1]]}

congestionShifts=[0.08746062, 0.01157071, 0.00000000, 0.26153337]# amEarly, amLate, pmEarly, pmLate

autoTotGenTimeCoeff = -0.0030

valueOfTime=[6.721, 8.961, 10.754, 11.948, 17.923]  # $0-25K, $25-50K, $50-75K, $75-100K, $100K+

##2.5 confirmed for TBI as well
outOfVehicleWeight = 2.5

