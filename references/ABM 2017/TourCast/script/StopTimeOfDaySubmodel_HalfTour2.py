####################################################################                                                                                                                                                                                           
# StopTimeOfDaySubmodel_HalfTour2.py
# Configuration script for Stop Time Of Day Half Tour 2
# This is overloading the Tour TimeOfDayComponent, so many items will be blank for Stops
####################################################################                                                                                                                                                                                           

from Globals import *

instantiationType="TimeOfDayComponent"

modelComponentName="StopTimeOfDaySubmodel"

from StopTimeOfDayMemDataRefs import *

# Stops are almost exclusively driven by duration and available periods
from itertools import chain

arrivalConsts = []

departureConsts = []

# Duration is measured in # of periods from 0 - 47
durationConsts = list(chain(
                [ 0.0],    # 0
				[  1.333 ] * 1, # 1 
				[  0.631 ] * 1, # 2 
				[  0.643 ] * 1, # 3 
				[  0.668 ] * 1, # 4 
				[  0.635 ] * 1, # 5 
				[  0.737 ] * 2, # 6-7 
				[  0.833 ] * 3, # 8-10 
				[  0.355 ] * 5, # 11-15 
				[ -0.105 ] * 32, # 16+ 
                 ))

arrivalPivot = 0.0      # not used for stop tod
durationPivot = 0.0     # not used for stop tod


# Shift variables treated like coefficient array with shift types (arrEarly/arrLate/durE, durL, dep) treated like alternatives
# CoeffMap use to match variables used to compute aggregate coefficient
# For Stops, only duration shift is needed, but is also segmented
shiftCoeffs=[[
    #    duration
         placeholder,	# 0 for work tour, segmented by stop purpose
         placeholder,	# 1 for school/uni tour, segmented by stop purpose
         placeholder,	# 2 for non mandatory tour, segmented by stop purpose
         placeholder,	# 3 for standalone school escort tour, segmented by stop purpose
		 -0.11331224, # 4 SESC*ISFJNT # Escort Stop , Fully Joint Tour 
		 -0.08704394, # 5 IFIN(TOUR_DR,0,1) # Tour Duration = 0-1
		 -0.08704394, # 6 IFIN(TOUR_DR,2,3) # Tour Duration = 2-3
		 -0.08054773, # 7 IFIN(DEPPER2,14,20) # Tour Return 9am-12pm
		 -0.14139809, # 8 IFIN(DEPPER2,21,26) # Tour Return 12pm-3pm
		 -0.16638956, # 9 IFIN(DEPPER2,27,32) # Tour Return 3:30pm-6:30pm
		 -0.51541527, # 10 IFGT(DEPPER2,32) # Tour Return 6:30pm or later 
		  0.01118960, # 11 IFIN(REMODE,2,3) # Shared Ride (2 or 3+) Tour Mode
		  0.02417550, # 12 IFIN(PTYPE,2,3) # Children between 5 and 15 years & 16+ years	
]]

shiftCoeffMap={
     "Tour" : [[24, 0, 4],
               [1, 5, 2],
               [15, 7, 2],
			   [18, 9, 1],
			   [20, 10, 1],
               [29, 11, 1],
              ],
     "Stop" : [[1, 4, 1]],
	 "Person" : [[0, 12, 1]],
     }

tourCoeffs=[
		  # dur - 1,    dur - 2     dur - 4
		[  0.00000000, -0.51105371,   0.00000000], # IWK*SML # Meal Stop, Work Tour
		[  0.00000000, -1.32896634, 0.97039189], # IWK*SSH # Shopping Stop, Work Tour
		[0.05394597, -0.62504583,   0.00000000], # IWK*SMNT # PersBus Stop, Work Tour
		[  0.00000000, -0.25, -0.04631785], # IWK*SDSC # SocRec Stop, Work Tour
		[  0.00000000, -0.71348938,  0.00000000], # (ISC+IUN)*SML # Meal Stop, NonMan Tour
		[  0.00000000, -0.74659145,  0.00000000], # (ISC+IUN)*SSH # Shopping Stop, NonMan Tour
		[  0.00000000, -0.57918081,  0.00000000], # (ISC+IUN)*SMNT # PersBus Stop, NonMan Tour
		[  0.00000000, -0.32132446,  0.00000000], # (ISC+IUN)*SDSC # SocRec Stop, NonMan Tour
]

tourCoeffMap={
    "Stop" : [[2, 0, 8]]
    }

# for alternative-specific calculations that will be done in the subclass
derivedValueCoeffs= [[ 
				 -0.01733256, # 0 DIST_LOC*IFEQ(STPDUR,0) # Dur = 0: Distance - Stop Location to Subsequent Location (if HT=1), Prior Location to Stop Location (if HT=2)
				 -0.01803170, # 1 DIST_LOC*IFEQ(STPDUR,1) # Dur = 1: Distance - Stop Location to Subsequent Location (if HT=1), Prior Location to Stop Location (if HT=2)
				 -0.02744014, # 2 DIST_LOC*IFIN(STPDUR,0,1)*IFGT(REMODE,3) # Dur = 0 or 1: Distance - Stop Location to Subsequent Location (if HT=1), Prior Location to Stop Location (if HT=2), non-auto modes
				  0.00665098, # 3 (SR_DISTO+SR_DISTI)*IFGE(STPDUR,2) # Stop Duration = 2+; Detour Distance
				  0.00098319, # 4 (SR_DISTO+SR_DISTI)*IFGE(STPDUR,4) # Stop Duration = 4+; Detour Distance
				  0.00298107, # 5 (SR_DISTO+SR_DISTI)*IFGE(STPDUR,8) # Stop Duration = 8+; Detour Distance
				 -2.74319607, # 6 PPUSE2 # Period Partially Used by Later Tour  
				  0.00000000, # 7 # Number of Available Periods-Early given Presence of other Tour Earlier in Day
				  0.09617562, # 8 (IFEQ(STPNO,2)*IFEQ(STOP2,3)+IFEQ(STPNO,1)*IFGE(STOP2,2))*TIMAFT # Number of Available Periods-Late	1+ Additional Stops Later
				  0.00000000, # 9 # 2 Additional Stops Earlier   
				  placeholder, # 10 no school escorted children, segmented by stop purpose
                  ]]
derivedValueCoeffMap={
       "AlternativeSpecificValues" : [[1,0,11],
                                     ]}

segmentDefinitions = [
{'Name': 'Stop Purpose', 'DataRef': 'Stop', 'Offset':0, 'DataRange': [1,2,4,8,16,32,64,128]}, # school, work, uni, meal, shop, pb, sr, escort
]

segmentCoeffMap = [
{'Segment': 0, 'Vector': 'transient', 'Offset': 0, # shiftCoeffs:work tour
 'Coefficients': [ # school,      work,        uni,         meal,        shop,        pb,          sr,          escort 
                  [  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000, -0.08618718, -0.39286560]]},
{'Segment': 0, 'Vector': 'transient', 'Offset': 1, # shiftCoeffs:school/uni tour
 'Coefficients': [ # school,      work,        uni,         meal,        shop,        pb,          sr,          escort 
                  [  0.00000000,  0.00000000,  0.07924173,  0.15380240, -0.36113996,  0.00000000,  0.00000000, -0.71121249]]},
{'Segment': 0, 'Vector': 'transient', 'Offset': 2, # shiftCoeffs:non mandatory tour
 'Coefficients': [ # school,      work,        uni,         meal,        shop,        pb,          sr,          escort 
                  [  0.00000000,  0.00000000,  0.00000000, -0.12392468, -0.38188907, -0.45813852, -0.11105306, -0.43572361]]},
{'Segment': 0, 'Vector': 'transient', 'Offset': 3, # shiftCoeffs:standalone school escort tour
 'Coefficients': [ # school,      work,        uni,         meal,        shop,        pb,          sr,          escort 
                  [  0.00000000,  0.00000000,  0.00000000, -0.21374473, -0.41664053,  0.00000000, -0.09802466, -0.69854166]]},
{'Segment': 0, 'Vector': 'transient', 'Offset': 26, # derivedValueCoeffs:no school escorted children, offset is sum of widths of all coeff maps
 'Coefficients': [ # school,      work,         uni,         meal,        shop,        pb,          sr,          escort 
                  [  0.00000000,  10.00000000,  10.00000000,  0.00000000, -0.67872793,  0.00000000,  0.00000000,  0.00000000]]},

]

# Not used for Stop Time Of Day

congestionShifts=[]
autoTotGenTimeCoeff=0.0
valueOfTime=[]
outOfVehicleWeight=0.0
