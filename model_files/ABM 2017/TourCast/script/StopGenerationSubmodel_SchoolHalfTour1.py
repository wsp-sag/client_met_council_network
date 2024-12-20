####################################################################
# StopGenerationSubmodel_SchoolHalfTour1.py
# School-based Tour Half Tour 1 submodel for Stop Generation
####################################################################

from StopGenerationSubmodelCommon import *
from StopGenMemDataRefs import *

parameters = {
              # These are the parameters to generate the specific stop alternatives for this model
              "MaxStops" : 2,
              "StopPurposeDescriptions" : ['school stops', 'uni stops', 'meal stops', 'shop stops', 'pb stops', 'sr stops', 'esc stops'],
              "StopPurposeIds" : [1, 4, 8, 16, 32, 64, 128],
              #N/A
              "unavailableAlternativesA" : [],
              #N/A
              "unavailableAlternativesB" : [],
             }

#Alternatives determined by the combination of stop purposes and maximum number of stops
altIntrinsicValues = [   0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,  13,  14,  15,  16,  17,  18,  19,
  20,  21,  22,  23,  24,  25,  26,  27,  28,  29,  30,  31,  32,  33,  34,  35,]

# altNames is required for config file but not used here because of the complexity of the alternatives
altNames = []

nestList = [
["Root", 0, 1.00, [], [1, 2, 3]],
["0-stop alts", 1, 0.800, [0], []],
["1-stop alts", 2, 0.800, [   1,   2,   3,   4,   5,   6,   7,], []],
["2-stop alts", 3, 0.800, [   8,   9,  10,  11,  12,  13,  14,  15,  16,  17,  18,  19,  20,  21,  22,  23,  24,  25,  26,  27,
  28,  29,  30,  31,  32,  33,  34,  35,], []],
]
           
altSpecificConsts = [0, -13.37053, -13.37053, -14.33783, -17.7789, -15.61023, -10.87535, -13.14586, -29.80917, -30.15716, 
-29.14905, -31.89977, -29.79836, -26.41375, -29.9325, -29.80917, -26.51643, -34.56554, -32.39686, -25.40456, 
-29.9325, -33.94879, -35.53285, -31.09482, -26.88301, -28.29434, -32.31485, -36.80524, -28.62644, -34.34088, 
-35.22118, -26.74917, -32.1722, -30.4863, -26.54601, -30.16824]



durableCoeffs = [

]

transientCoeffs = [
# 0 CHD16 # Child Age 16+
[
  0.000000,  0.000000,  0.000000, -0.604048,  0.000000,  0.000000, -0.964217,  0.647758,  0.000000,  0.000000,
 -0.604048,  0.000000,  0.000000, -0.964217,  0.647758,  0.000000, -0.604048,  0.000000,  0.000000, -0.964217,
  0.647758,  0.000000, -0.604048, -0.604048, -1.568264,  0.043710,  0.000000,  0.000000, -0.964217,  0.647758,
  0.000000, -0.964217,  0.647758,  0.000000, -0.316459,  0.000000
],
# 1 MALE #  
[
  0.000000, -0.496869, -0.496869, -0.496869, -0.496869, -0.496869, -0.496869, -0.496869, -0.993738, -0.993738,
 -0.993738, -0.993738, -0.993738, -0.993738, -0.993738, -0.993738, -0.993738, -0.993738, -0.993738, -0.993738,
 -0.993738, -0.993738, -0.993738, -0.993738, -0.993738, -0.993738, -0.993738, -0.993738, -0.993738, -0.993738,
 -0.993738, -0.993738, -0.993738, -0.993738, -0.993738, -0.993738
],
# 2 DISTANCE # Distance - HT1+HT2
[
  0.000000,  0.000000,  0.000000,  0.000000, -0.002880,  0.015649,  0.000000,  0.000000,  0.000000,  0.000000,
  0.000000, -0.002880,  0.015649,  0.000000,  0.000000,  0.000000,  0.000000, -0.002880,  0.015649,  0.000000,
  0.000000,  0.000000, -0.002880,  0.015649,  0.000000,  0.000000,  0.000000,  0.012769, -0.002880, -0.002880,
  0.000000,  0.015649,  0.015649,  0.000000,  0.000000,  0.000000
],
# 3 IT_EMP/DAREA # Employment Density at Destination
[
  0.000000,  0.000000,  0.000037,  0.000000,  0.000000,  0.000000,  0.000000,  0.000000,  0.000000,  0.000037,
  0.000000,  0.000000,  0.000000,  0.000000,  0.000000,  0.000037,  0.000037,  0.000037,  0.000037,  0.000037,
  0.000037,  0.000000,  0.000000,  0.000000,  0.000000,  0.000000,  0.000000,  0.000000,  0.000000,  0.000000,
  0.000000,  0.000000,  0.000000,  0.000000,  0.000000,  0.000000
],
# 4 LOG(PERAVHT1+1) # ln(1 + Number of Available Periods)
[
  0.000000,  3.986219,  3.986219,  3.279591,  4.256234,  3.986219,  2.973941,  3.986219,  8.656583,  8.656583,
  7.949954,  8.926597,  8.656583,  7.644304,  8.656583,  8.656583,  7.949954,  8.926597,  8.656583,  7.644304,
  8.656583,  7.949954,  8.219969,  7.949954,  6.937676,  7.949954,  8.926597,  8.926597,  7.914319,  8.926597,
  8.656583,  7.644304,  8.656583,  7.644304,  7.644304,  8.656583
],
# 5 NOON_AM # Arrival Time 9AM and 12 pm
[  0, 0.7026, 0.4309, 0.7026, 0.7026, 0.7026, 0.7026, -0.07477, 1.40519, 1.13349, 
1.40519, 1.40519, 1.40519, 1.40519, 0.62782, 1.13349, 1.13349, 1.13349, 1.13349, 1.13349, 
0.35612, 1.40519, 1.40519, 1.40519, 1.40519, 0.62782, 1.40519, 1.40519, 1.40519, 0.62782, 
1.40519, 1.40519, 0.62782, 1.40519, 0.62782, 0.62782], 

###### 6 Arrival before 9 AM
[  0, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3, -0.6, -0.6, 
-0.6, -0.6, -0.6, -0.6, -0.6, -0.6, -0.6, -0.6, -0.6, -0.6, 
-0.6, -0.6, -0.6, -0.6, -0.6, -0.6, -0.6, -0.6, -0.6, -0.6, 
-0.6, -0.6, -0.6, -0.6, -0.6, -0.6], 


]

from StopGenerationSubmodelSchoolHalfTour1Maps import durableCoeffMap,transientCoeffMap
