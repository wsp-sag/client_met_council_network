####################################################################                                                                                                                                                                                           
# StopTimeOfDaySubmodel_HalfTour1.py
# Configuration script for Stop Time Of Day Half Tour 1
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
				[  0.819 ] * 1, # 1 
				[ -0.130 ] * 1, # 2 
				[ -0.287 ] * 1, # 3 
				[ -0.780 ] * 1, # 4 
				[ -0.986 ] * 1, # 5 
				[ -1.708 ] * 2, # 6-7 
				[ -2.521 ] * 3, # 8-10 
				[ -3.509 ] * 5, # 11-15 
				[ -7.152 ] * 32, # 16+ 
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
		 -0.05182547, # 5 IFIN(TOUR_DR,0,1) # Tour Duration = 0-1
		 -0.05182547, # 6 IFIN(TOUR_DR,2,3) # Tour Duration = 2-3
		 -0.19243732, # 7 IFGE(TOUR_DR,16) # Tour Duration = 16+
		 -0.31513667, # 8 IFLE(ARRPER2,8) # Tour Arrival before 6am
		  0.15024984, # 9 IFIN(ARRPER2,14,20) # Tour Arrival 9am-12pm
		  0.26232566, # 10 IFIN(ARRPER2,21,26) # Tour Arrival 12pm-3pm
		  0.30576718, # 11 IFIN(ARRPER2,27,32) # Tour Arrival 3pm-6pm
		  0.33632972, # 12 IFGT(ARRPER2,32) # Tour Arrival 6pm or later
		  0.01118960, # 13 IFIN(REMODE,2,3) # Shared Ride (2 or 3+) Tour Mode
		 -0.06995370, # 14 IFIN(PTYPE,5,6) # Full-time/Part-time Workers
		 -0.06995370, # 15 IFIN(PTYPE,5,6) # Full-time/Part-time Workers 
		 -0.08540121, # 16 IFEQ(PTYPE,7) # Non-working Adult
]]



shiftCoeffMap={
     "Tour" : [[24, 0, 4],
               [1, 5, 4],
               [7, 9, 1],
               [9, 10, 2],
               [12, 12, 1],
               [29, 13, 1],
              ],
     "Stop" : [[1, 4, 1],],
     "Person" : [[6, 14, 2], [4, 16, 1],],
     }

tourCoeffs=[
		  # dur - 1,    dur - 2     dur - 4		
		[  0.00000000, -0.14986766,   0.00000000], # IWK*SML # Meal Stop, Work Tour
		[  0.00000000, -0.83313532, 0.97039189], # IWK*SSH # Shopping Stop, Work Tour
		[  0.00000000, -0.12504583,   0.00000000], # IWK*SMNT # PersBus Stop, Work Tour
		[  0.00000000, 0.25, -0.04631785], # IWK*SDSC # SocRec Stop, Work Tour
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
				 -2.40693685, # 6 PPUSE1 # Period Partially Used by Earlier Tour  
				  0.08959176, # 7 TIMBEF*TOUR_BEF # Number of Available Periods-Early given Presence of other Tour Earlier in Day
				  0.14165928, # 8 (IFEQ(STPNO,-2)*IFEQ(STOP1,3)+IFEQ(STPNO,-1)*IFGE(STOP1,2))*TIMBEF # Number of Available Periods-Early	1+ Additional Stops Earlier
				  0.02153240, # 9 IFEQ(STPNO,-1)*IFGE(STOP1,2)*TIMBEF # Number of Available Periods-Early	2 Additional Stops Earlier
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
                  [  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000, -0.11137694, -0.39286560]]},
{'Segment': 0, 'Vector': 'transient', 'Offset': 1, # shiftCoeffs:school/uni tour
 'Coefficients': [ # school,      work,        uni,         meal,        shop,        pb,          sr,          escort 
                  [  0.10531919,  0.00000000,  0.35056631,  0.23161146,  0.00000000,  0.00000000,  0.00000000, -0.71121249]]},
{'Segment': 0, 'Vector': 'transient', 'Offset': 2, # shiftCoeffs:non mandatory tour
 'Coefficients': [ # school,      work,        uni,         meal,        shop,        pb,          sr,          escort 
                  [  0.00000000,  0.00000000,  0.00000000, -0.12392468, -0.38188907, -0.45813852, -0.11105306, -0.43572361]]},
{'Segment': 0, 'Vector': 'transient', 'Offset': 3, # shiftCoeffs:standalone school escort tour
 'Coefficients': [ # school,      work,        uni,         meal,        shop,        pb,          sr,          escort 
                  [  0.00000000,  0.00000000,  0.00000000, -0.21374473, -0.41664053,  0.00000000, -0.09802466, -0.69854166]]},
{'Segment': 0, 'Vector': 'transient', 'Offset': 30, # derivedValueCoeffs:no school escorted children, offset is sum of all coeff maps
 'Coefficients': [ # school,      work,        uni,         meal,        shop,        pb,          sr,          escort 
                  [  0.00000000,  10.00000000,  10.00000000,  0.52855662,  0.52855662,  0.52855662,  0.52855662,  0.00000000]]},

]

# Not used for Stop Time Of Day

congestionShifts=[]
autoTotGenTimeCoeff=0.0
valueOfTime=[]
outOfVehicleWeight=0.0
