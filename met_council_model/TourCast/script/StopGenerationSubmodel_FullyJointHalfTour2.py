####################################################################
# StopGenerationSubmodel_FullyJointHalfTour2.py
# FullyJoint Tours Half Tour 2 submodel for Stop Generation
####################################################################

from StopGenerationSubmodelCommon import *
from StopGenMemDataRefs import *

parameters = {
              # These are the parameters to generate the specific stop alternatives for this model
              "MaxStops" : 2,
              "StopPurposeDescriptions" : ['meal stops', 'shop stops', 'pb stops', 'sr stops', 'esc stops'],
              "StopPurposeIds" : [8, 16, 32, 64, 128],
              #N/A
              "unavailableAlternativesA" : [],
              #N/A
              "unavailableAlternativesB" : [],
             }

#Alternatives determined by the combination of stop purposes and maximum number of stops
altIntrinsicValues = [   0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,  13,  14,  15,  16,  17,  18,  19, 20]

# altNames is required for config file but not used here because of the complexity of the alternatives
altNames = []

nestList = [
["Root", 0, 1.0, [], [1, 2, 3]],
["0-stop alts", 1, 0.8, [0], []],
["1-stop alts", 2, 0.8, [   1,   2,   3,   4,   5,], []],
["2-stop alts", 3, 0.8, [   6,   7,   8,   9,  10,  11,  12,  13,  14,  15,  16,  17,  18,  19,  20,], []]
]
           
altSpecificConsts = [0, -4.10263, -4.30663, -8.96333, -4.10263, -4.10263, -4.50263, -4.70663, -11.85123, -4.50263, 
-4.50263, -4.70663, -9.86021, -6.02149, -4.70663, -9.36333, -11.50065, -9.36333, -4.50263, -4.50263, 
-4.50263] 



durableCoeffs = [
# INC100 # Income greater than $100K
[0, -0.2, -0.2, -0.2, -0.2, -0.2, -0.4, -0.4, -0.4, -0.4, 
-0.4, -0.4, -0.4, -0.4, -0.4, -0.4, -0.4, -0.4, -0.4, -0.4, 
-0.4], 

]
transientCoeffs = [
###### 0 Tour Purpose
[ placeholder]*21,
# 1 FJSIZE # Fully Joint Tour Size
[
  0.000000, -0.038482, -0.038482, -0.038482, -0.038482, -0.038482, -0.038482, -0.038482, -0.038482, -0.038482,
 -0.038482, -0.038482, -0.038482, -0.038482, -0.038482, -0.038482, -0.038482, -0.038482, -0.038482, -0.038482,
 -0.038482
],
# 2 ONLYCHILD # Children only in Group
[
  0.000000, -0.884046, -0.287245, -0.287245, -0.287245, -0.287245, -0.884046, -0.884046, -0.884046, -0.884046,
 -0.884046, -0.287245, -0.287245, -0.287245, -0.287245, -0.287245, -0.287245, -0.287245, -0.287245, -0.287245,
 -0.287245
],
# 3 (1-ONLYCHILD) # At least 1 adult in group
[
  0.000000,  0.000000, -0.553369,  0.733883,  0.000000,  0.000000,  0.000000, -0.553369,  0.733883,  0.000000,
  0.000000, -0.553369,  0.180514, -0.553369, -0.553369,  0.733883,  0.733883,  0.733883,  0.000000,  0.000000,
  0.000000
],
# 4 ONLY_MALE # Males only in Group
[
  0.000000, -0.386201, -1.850157, -0.386201, -0.386201,  0.257512, -0.386201, -1.850157, -0.386201, -0.386201,
  0.257512, -1.850157, -1.850157, -1.850157, -1.206444, -0.386201, -0.386201,  0.257512, -0.386201,  0.257512,
  0.257512
],
# 5 IFGE(NSEN,1) # 1+ Senior in Group 
[ placeholder]*21,
# 6 WRK_JNT # 1+ Worker in Group
[
  0.000000, -0.454704, -0.454704, -0.454704, -0.454704, -0.454704, -0.454704, -0.454704, -0.454704, -0.454704,
 -0.454704, -0.454704, -0.454704, -0.454704, -0.454704, -0.454704, -0.454704, -0.454704, -0.454704, -0.454704,
 -0.454704
],
# 7 IFGE(MAND_TOUR,1) # Presence of Mandatory Tours 
[ placeholder]*21,
# 8 DISTANCE # Round Trip Auto Travel Distance (mi) 
[ placeholder]*21,
# 9 MXDENS # Mixed Density at Destination
[
  0.000000,  0.000059,  0.000071,  0.000059,  0.000059,  0.000059,  0.000059,  0.000071,  0.000059,  0.000059,
  0.000059,  0.000071,  0.000071,  0.000071,  0.000071,  0.000059,  0.000059,  0.000059,  0.000059,  0.000059,
  0.000059
],
# 10 ITOTEMP/OAREA # Employment Density at Destination
[
  0.000000, -0.000060,  0.000011,  0.000011,  0.000011,  0.000011, -0.000060, -0.000060, -0.000060, -0.000060,
 -0.000060,  0.000011,  0.000011,  0.000011,  0.000011,  0.000011,  0.000011,  0.000011,  0.000011,  0.000011,
  0.000011
],
# 11 (DEPPER2-ARRPER2) # Duration of Tour Activity (in number of 30-min periods) 
[ placeholder]*21,
# 12 LOG(1+PERAVHT2) # Natural Log of (1 + Number of Available Periods) 
[ placeholder]*21,
# 13 BEFOREAM1 # Departure Time Before 10AM 
[ placeholder]*21,
# 14 RET_PM1 # Departure Time after 4:00 pm
[0, -0.1, -1.14457, -1.97972, -0.42191, -0.1, -0.2, -1.24457, -2.07972, -0.52191, 
-0.2, -1.24457, -3.1243, -1.56648, -1.24457, -2.07972, -2.40164, -2.07972, -0.52191, -0.52191, 
-0.2], 





# 15 STOP1_TOT # Number of Stops on HT1 
[ placeholder]*21,

# 16 Departure after 6PM
[0, -1, -1, -1, -1, -1, -2, -2, -2, -2, 
-2, -2, -2, -2, -2, -2, -2, -2, -2, -2, 
-2], 

]

from StopGenerationSubmodelFullyJointHalfTour2Maps import durableCoeffMap,transientCoeffMap

segmentDefinitions = [{'Name': 'Tour Purpose', 'DataRef': 'Tour','Offset': 0, 'DataRange': [8, 16, 32, 64, 128]}
]
segmentCoeffMap = [{'Segment': 0, 'Vector': 'transient', 'Offset': 0, 
  'Coefficients': # TOURPURP # Purpose 
#  Meal      Shop      PerBus   SocRec     SchEsc
[
[  0.00000,  0.00000,  0.00000,  0.00000,  0.00000,],
[  0.00000,  2.39373,  0.18580,  0.00000,  0.00000,],
[  0.00000,  2.85443,  1.22276,  0.00000,  0.00000,],
[  0.00000,  2.85443,  0.18580,  0.00000,  0.00000,],
[  0.00000,  1.50456, -1.22287,  0.00000,  0.00000,],
[  0.00000,  0.16579,  0.18580,  0.00000,  0.00000,],
[  0.00000,  2.39373,  0.18580,  0.00000,  0.00000,],
[  0.00000,  2.39373,  1.22276,  0.00000,  0.00000,],
[  0.00000,  2.39373,  0.18580,  0.00000,  0.00000,],
[  0.00000,  1.04386, -1.22287,  0.00000,  0.00000,],
[  0.00000, -0.29491,  0.18580,  0.00000,  0.00000,],
[  0.00000,  2.85443,  1.22276,  0.00000,  0.00000,],
[  0.00000,  2.85443,  1.22276,  0.00000,  0.00000,],
[  0.00000,  1.50456, -0.18591,  0.00000,  0.00000,],
[  0.00000,  0.16579,  1.22276,  0.00000,  0.00000,],
[  0.00000,  2.85443,  0.18580,  0.00000,  0.00000,],
[  0.00000,  1.50456, -1.22287,  0.00000,  0.00000,],
[  0.00000,  0.16579,  0.18580,  0.00000,  0.00000,],
[  0.00000,  1.50456, -1.22287,  0.00000,  0.00000,],
[  0.00000, -1.18408, -1.22287,  0.00000,  0.00000,],
[  0.00000,  0.16579,  0.18580,  0.00000,  0.00000,],
]
  },
{'Segment': 0, 'Vector': 'transient', 'Offset': 5, 
  'Coefficients':
 # IFGE(NSEN,1) # 1+ Senior in Group 
#  Meal      Shop      PerBus   SocRec     SchEsc
[
[  0.00000,  0.00000,  0.00000,  0.00000,  0.00000,],
[ -1.47875, -0.19170, -0.35029, -1.47875, -1.47875,],
[ -1.47875, -0.19170, -0.35029, -1.47875, -1.47875,],
[ -1.47875, -0.19170, -0.35029, -1.47875, -1.47875,],
[ -1.47875, -0.19170, -0.35029, -1.47875, -1.47875,],
[ -1.47875, -0.19170, -0.35029, -1.47875, -1.47875,],
[ -1.47875, -0.19170, -0.35029, -1.47875, -1.47875,],
[ -1.47875, -0.19170, -0.35029, -1.47875, -1.47875,],
[ -1.47875, -0.19170, -0.35029, -1.47875, -1.47875,],
[ -1.47875, -0.19170, -0.35029, -1.47875, -1.47875,],
[ -1.47875, -0.19170, -0.35029, -1.47875, -1.47875,],
[ -1.47875, -0.19170, -0.35029, -1.47875, -1.47875,],
[ -1.47875, -0.19170, -0.35029, -1.47875, -1.47875,],
[ -1.47875, -0.19170, -0.35029, -1.47875, -1.47875,],
[ -1.47875, -0.19170, -0.35029, -1.47875, -1.47875,],
[ -1.47875, -0.19170, -0.35029, -1.47875, -1.47875,],
[ -1.47875, -0.19170, -0.35029, -1.47875, -1.47875,],
[ -1.47875, -0.19170, -0.35029, -1.47875, -1.47875,],
[ -1.47875, -0.19170, -0.35029, -1.47875, -1.47875,],
[ -1.47875, -0.19170, -0.35029, -1.47875, -1.47875,],
[ -1.47875, -0.19170, -0.35029, -1.47875, -1.47875,],
] 
  },
{'Segment': 0, 'Vector': 'transient', 'Offset': 7, 
  'Coefficients':
# IFGE(MAND_TOUR,1) # Presence of Mandatory Tours 
#  Meal      Shop      PerBus   SocRec     SchEsc
[
[  0.00000,  0.00000,  0.00000,  0.00000,  0.00000,],
[ -0.39554,  0.08371, -0.39554, -0.39554, -0.39554,],
[ -0.39554,  0.08371, -0.39554, -0.39554, -0.39554,],
[ -0.39554,  0.08371, -0.39554, -0.39554, -0.39554,],
[ -0.39554,  0.08371, -0.39554, -0.39554, -0.39554,],
[ -0.39554,  0.08371, -0.39554, -0.39554, -0.39554,],
[ -0.39554,  0.08371, -0.39554, -0.39554, -0.39554,],
[ -0.39554,  0.08371, -0.39554, -0.39554, -0.39554,],
[ -0.39554,  0.08371, -0.39554, -0.39554, -0.39554,],
[ -0.39554,  0.08371, -0.39554, -0.39554, -0.39554,],
[ -0.39554,  0.08371, -0.39554, -0.39554, -0.39554,],
[ -0.39554,  0.08371, -0.39554, -0.39554, -0.39554,],
[ -0.39554,  0.08371, -0.39554, -0.39554, -0.39554,],
[ -0.39554,  0.08371, -0.39554, -0.39554, -0.39554,],
[ -0.39554,  0.08371, -0.39554, -0.39554, -0.39554,],
[ -0.39554,  0.08371, -0.39554, -0.39554, -0.39554,],
[ -0.39554,  0.08371, -0.39554, -0.39554, -0.39554,],
[ -0.39554,  0.08371, -0.39554, -0.39554, -0.39554,],
[ -0.39554,  0.08371, -0.39554, -0.39554, -0.39554,],
[ -0.39554,  0.08371, -0.39554, -0.39554, -0.39554,],
[ -0.39554,  0.08371, -0.39554, -0.39554, -0.39554,],
]  
    },
{'Segment': 0, 'Vector': 'transient', 'Offset': 8, 
  'Coefficients':
 # DISTANCE # Round Trip Auto Travel Distance (mi) 
#  Meal      Shop      PerBus   SocRec     SchEsc
[
[  0.00000,  0.00000,  0.00000,  0.00000,  0.00000,],
[  0.07054,  0.05477, -0.00300, -0.00300, -0.00300,],
[  0.07054,  0.05477, -0.00300, -0.00300, -0.00300,],
[  0.07054,  0.05477, -0.00300, -0.00300, -0.00300,],
[  0.06585,  0.05008, -0.00769, -0.00769, -0.00769,],
[  0.07209,  0.05632, -0.00145, -0.00145, -0.00145,],
[  0.07054,  0.05477, -0.00300, -0.00300, -0.00300,],
[  0.07054,  0.05477, -0.00300, -0.00300, -0.00300,],
[  0.07054,  0.05477, -0.00300, -0.00300, -0.00300,],
[  0.06585,  0.05008, -0.00769, -0.00769, -0.00769,],
[  0.07209,  0.05632, -0.00145, -0.00145, -0.00145,],
[  0.07054,  0.05477, -0.00300, -0.00300, -0.00300,],
[  0.07054,  0.05477, -0.00300, -0.00300, -0.00300,],
[  0.06585,  0.05008, -0.00769, -0.00769, -0.00769,],
[  0.07209,  0.05632, -0.00145, -0.00145, -0.00145,],
[  0.07054,  0.05477, -0.00300, -0.00300, -0.00300,],
[  0.06585,  0.05008, -0.00769, -0.00769, -0.00769,],
[  0.07209,  0.05632, -0.00145, -0.00145, -0.00145,],
[  0.06585,  0.05008, -0.00769, -0.00769, -0.00769,],
[  0.06740,  0.05163, -0.00614, -0.00614, -0.00614,],
[  0.07209,  0.05632, -0.00145, -0.00145, -0.00145,],
] 
    },
{'Segment': 0, 'Vector': 'transient', 'Offset': 11, 
  'Coefficients':
# (DEPPER2-ARRPER2) # Duration of Tour Activity (in number of 30-min periods) 
#  Meal      Shop      PerBus   SocRec     SchEsc
[
[  0.00000,  0.00000,  0.00000,  0.00000,  0.00000,],
[ -0.85985, -0.32319, -0.32319, -0.00686, -0.32319,],
[ -0.85985, -0.32319, -0.32319, -0.00686, -0.32319,],
[ -0.85985, -0.32319, -0.32319, -0.00686, -0.32319,],
[ -0.85985, -0.32319, -0.32319, -0.00686, -0.32319,],
[ -0.85985, -0.32319, -0.32319, -0.00686, -0.32319,],
[ -0.85985, -0.32319, -0.32319, -0.00686, -0.32319,],
[ -0.85985, -0.32319, -0.32319, -0.00686, -0.32319,],
[ -0.85985, -0.32319, -0.32319, -0.00686, -0.32319,],
[ -0.85985, -0.32319, -0.32319, -0.00686, -0.32319,],
[ -0.85985, -0.32319, -0.32319, -0.00686, -0.32319,],
[ -0.85985, -0.32319, -0.32319, -0.00686, -0.32319,],
[ -0.85985, -0.32319, -0.32319, -0.00686, -0.32319,],
[ -0.85985, -0.32319, -0.32319, -0.00686, -0.32319,],
[ -0.85985, -0.32319, -0.32319, -0.00686, -0.32319,],
[ -0.85985, -0.32319, -0.32319, -0.00686, -0.32319,],
[ -0.85985, -0.32319, -0.32319, -0.00686, -0.32319,],
[ -0.85985, -0.32319, -0.32319, -0.00686, -0.32319,],
[ -0.85985, -0.32319, -0.32319, -0.00686, -0.32319,],
[ -0.85985, -0.32319, -0.32319, -0.00686, -0.32319,],
[ -0.85985, -0.32319, -0.32319, -0.00686, -0.32319,],
]  
    },
{'Segment': 0, 'Vector': 'transient', 'Offset': 12, 
  'Coefficients':
# LOG(1+PERAVHT2) # Natural Log of (1 + Number of Available Periods) 
#  Meal      Shop      PerBus   SocRec     SchEsc
[
[  0.00000,  0.00000,  0.00000,  0.00000,  0.00000,],
[  0.64233,  0.00000,  1.06653,  0.00000,  0.00000,],
[  0.81873,  0.17640,  1.24293,  0.17640,  0.17640,],
[  1.46481,  0.82248,  1.88901,  0.82248,  0.82248,],
[  1.05004,  0.40772,  1.47424,  0.40772,  0.40772,],
[  0.64233,  0.00000,  1.06653,  0.00000,  0.00000,],
[  0.64233,  0.00000,  1.06653,  0.00000,  0.00000,],
[  0.81873,  0.17640,  1.24293,  0.17640,  0.17640,],
[  1.46481,  0.82248,  1.88901,  0.82248,  0.82248,],
[  1.05004,  0.40772,  1.47424,  0.40772,  0.40772,],
[  0.64233,  0.00000,  1.06653,  0.00000,  0.00000,],
[  0.81873,  0.17640,  1.24293,  0.17640,  0.17640,],
[  1.64121,  0.99888,  2.06541,  0.99888,  0.99888,],
[  1.22644,  0.58412,  1.65064,  0.58412,  0.58412,],
[  0.81873,  0.17640,  1.24293,  0.17640,  0.17640,],
[  1.46481,  0.82248,  1.88901,  0.82248,  0.82248,],
[  1.87252,  1.23020,  2.29672,  1.23020,  1.23020,],
[  1.46481,  0.82248,  1.88901,  0.82248,  0.82248,],
[  1.05004,  0.40772,  1.47424,  0.40772,  0.40772,],
[  1.05004,  0.40772,  1.47424,  0.40772,  0.40772,],
[  0.64233,  0.00000,  1.06653,  0.00000,  0.00000,],
]
  
    },
{'Segment': 0, 'Vector': 'transient', 'Offset': 13, 
  'Coefficients':
# BEFOREAM1 # Departure Time Before 10AM 
#  Meal      Shop      PerBus   SocRec     SchEsc
[
[  0.00000,  0.00000,  0.00000,  0.00000,  0.00000,],
[ -1.48614, -1.03965,  1.49950, -1.48614, -1.48614,],
[ -1.06623, -0.61974,  1.91941, -1.06623, -1.06623,],
[ -1.48614, -1.03965,  1.49950, -1.48614, -1.48614,],
[ -0.09382,  0.35267,  2.89182, -0.09382, -0.09382,],
[ -1.48614, -1.03965,  1.49950, -1.48614, -1.48614,],
[ -1.48614, -1.03965,  1.49950, -1.48614, -1.48614,],
[ -1.06623, -0.61974,  1.91941, -1.06623, -1.06623,],
[ -1.48614, -1.03965,  1.49950, -1.48614, -1.48614,],
[ -0.09382,  0.35267,  2.89182, -0.09382, -0.09382,],
[ -1.48614, -1.03965,  1.49950, -1.48614, -1.48614,],
[ -1.06623, -0.61974,  1.91941, -1.06623, -1.06623,],
[ -1.06623, -0.61974,  1.91941, -1.06623, -1.06623,],
[  0.32609,  0.77258,  3.31173,  0.32609,  0.32609,],
[ -1.06623, -0.61974,  1.91941, -1.06623, -1.06623,],
[ -1.48614, -1.03965,  1.49950, -1.48614, -1.48614,],
[ -0.09382,  0.35267,  2.89182, -0.09382, -0.09382,],
[ -1.48614, -1.03965,  1.49950, -1.48614, -1.48614,],
[ -0.09382,  0.35267,  2.89182, -0.09382, -0.09382,],
[ -0.09382,  0.35267,  2.89182, -0.09382, -0.09382,],
[ -1.48614, -1.03965,  1.49950, -1.48614, -1.48614,],
]  
    },
{'Segment': 0, 'Vector': 'transient', 'Offset': 15, 
  'Coefficients':
  # STOP1_TOT # Number of Stops on HT1 
#  Meal      Shop      PerBus   SocRec     SchEsc
[
[  0.00000,  0.00000,  0.00000,  0.00000,  0.00000,],
[ -0.35754, -0.35754,  0.22177,  1.72058, -0.35754,],
[ -0.24434, -0.24434,  0.33496,  1.83377, -0.24434,],
[ -0.81489, -0.81489, -0.23559,  1.26323, -0.81489,],
[  0.00000,  0.00000,  0.57930,  2.07812,  0.00000,],
[  0.00000,  0.00000,  0.57930,  2.07812,  0.00000,],
[ -0.35754, -0.35754,  0.22177,  1.72058, -0.35754,],
[ -0.60188, -0.60188, -0.02258,  1.47624, -0.60188,],
[ -1.17243, -1.17243, -0.59312,  0.90569, -1.17243,],
[ -0.35754, -0.35754,  0.22177,  1.72058, -0.35754,],
[ -0.35754, -0.35754,  0.22177,  1.72058, -0.35754,],
[ -0.24434, -0.24434,  0.33496,  1.83377, -0.24434,],
[ -1.05923, -1.05923, -0.47993,  1.01888, -1.05923,],
[ -0.24434, -0.24434,  0.33496,  1.83377, -0.24434,],
[ -0.24434, -0.24434,  0.33496,  1.83377, -0.24434,],
[ -0.81489, -0.81489, -0.23559,  1.26323, -0.81489,],
[ -0.81489, -0.81489, -0.23559,  1.26323, -0.81489,],
[ -0.81489, -0.81489, -0.23559,  1.26323, -0.81489,],
[  0.00000,  0.00000,  0.57930,  2.07812,  0.00000,],
[  0.00000,  0.00000,  0.57930,  2.07812,  0.00000,],
[  0.00000,  0.00000,  0.57930,  2.07812,  0.00000,],
]
}
]
