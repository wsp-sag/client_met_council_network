####################################################################
# StopGenerationSubmodel_WorkHalfTour1.py
# Work Tours Half Tour 1 submodel for Stop Generation
####################################################################

from StopGenerationSubmodelCommon import *
from StopGenMemDataRefs import *

parameters = {
              # These are the parameters to generate the specific stop alternatives for this model
              "MaxStops" : 3,
              "StopPurposeDescriptions" : ['work stops', 'uni stops', 'meal stops', 'shop stops', 'pb stops', 'sr stops', 'esc stops'],
              "StopPurposeIds" : [2, 4, 8, 16, 32, 64, 128],
              #Adults
              "unavailableAlternativesA" : [   16, 38, 44, 45, 46, 47, 48, 49, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86,],
              #Children
              "unavailableAlternativesB" : [   16, 38, 44, 45, 46, 47, 48, 49, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86,],
             }

#Alternatives determined by the combination of stop purposes and maximum number of stops
altIntrinsicValues = [   0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,  13,  14,  15,  16,  17,  18,  19,
  20,  21,  22,  23,  24,  25,  26,  27,  28,  29,  30,  31,  32,  33,  34,  35,  36,  37,  38,  39,
  40,  41,  42,  43,  44,  45,  46,  47,  48,  49,  50,  51,  52,  53,  54,  55,  56,  57,  58,  59,
  60,  61,  62,  63,  64,  65,  66,  67,  68,  69,  70,  71,  72,  73,  74,  75,  76,  77,  78,  79,
  80,  81,  82,  83,  84,  85,  86,  87,  88,  89,  90,  91,  92,  93,  94,  95,  96,  97,  98,  99,
 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119,
]

# altNames is required for config file but not used here because of the complexity of the alternatives
altNames = []

nestList = [
["Root", 0, 1.0, [], [1, 2, 3, 4]],
["0-stop alts", 1, 0.7, [0], []],
["1-stop alts", 2, 0.7, [   1,   2,   3,   4,   5,   6,   7,], []],
["2-stop alts", 3, 0.7, [   8,   9,  10,  11,  12,  13,  14,  15,  16,  17,  18,  19,  20,  21,  22,  23,  24,  25,  26,  27,
  28,  29,  30,  31,  32,  33,  34,  35,], []],
["3-stop alts", 4, 0.7, [  36,  37,  38,  39,  40,  41,  42,  43,  44,  45,  46,  47,  48,  49,  50,  51,  52,  53,  54,  55,
  56,  57,  58,  59,  60,  61,  62,  63,  64,  65,  66,  67,  68,  69,  70,  71,  72,  73,  74,  75,
  76,  77,  78,  79,  80,  81,  82,  83,  84,  85,  86,  87,  88,  89,  90,  91,  92,  93,  94,  95,
  96,  97,  98,  99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115,
 116, 117, 118, 119,],[]]
]
           
altSpecificConsts = [0, -5.20753, -9.83704, -5.41246, -6.15281, -5.69269, -4.82681, -5.43685, -11.74219, -16.59423, 
-11.05383, -12.60645, -12.79518, -11.40414, -12.88374, -21.22374, -16.79917, -17.53951, -17.07939, -16.21352, 
-16.82355, -13.77761, -12.99051, -11.9906, -11.86418, -12.78021, -13.87419, -12.24524, -12.33145, -13.61589, 
-13.24906, -11.97991, -12.80576, -12.33557, -12.11835, -12.91466, -12.04558, -17.43028, -11.88988, -13.4425, 
-13.63123, -12.24018, -13.71979, -22.28232, -16.74192, -18.29454, -18.48327, -17.09222, -18.57183, -13.72036, 
-12.62971, -12.27866, -11.62706, -13.41266, -14.62922, -13.34557, -12.90661, -15.06062, -14.65294, -13.20392, 
-14.89934, -13.21428, -13.68675, -14.66293, -26.91183, -22.48725, -23.2276, -22.76748, -21.90161, -22.51164, 
-19.4657, -18.6786, -17.67869, -17.55227, -18.4683, -19.56228, -17.93333, -18.01954, -19.30398, -18.93715, 
-17.668, -18.49385, -18.02366, -17.80644, -18.60274, -26.91183, -15.65705, -14.65714, -14.53071, -15.44674, 
-15.01328, -12.72013, -13.54578, -15.13621, -13.84836, -12.65445, -13.7863, -13.67432, -13.83833, -14.5594, 
-13.23166, -14.26801, -14.35422, -15.63866, -14.103, -12.63602, -14.13627, -14.1416, -14.40094, -15.39508, 
-13.89682, -13.83767, -14.66352, -13.79005, -13.69939, -14.58495, -13.89229, -13.92849, -13.89754, -15.71642] 


durableCoeffs = [
# HHVEH # HH number of vehicles
[
  0.00000, -0.04482, -0.04482, -0.04482, -0.04482, -0.04482, -0.04482, -0.04482, -0.04482, -0.04482,
 -0.04482, -0.04482, -0.04482, -0.04482, -0.04482, -0.04482, -0.04482, -0.04482, -0.04482, -0.04482,
 -0.04482, -0.04482, -0.04482, -0.04482, -0.04482, -0.04482, -0.04482, -0.04482, -0.04482, -0.04482,
 -0.04482, -0.04482, -0.04482, -0.04482, -0.04482, -0.04482, -0.04482, -0.04482, -0.04482, -0.04482,
 -0.04482, -0.04482, -0.04482, -0.04482, -0.04482, -0.04482, -0.04482, -0.04482, -0.04482, -0.04482,
 -0.04482, -0.04482, -0.04482, -0.04482, -0.04482, -0.04482, -0.04482, -0.04482, -0.04482, -0.04482,
 -0.04482, -0.04482, -0.04482, -0.04482, -0.04482, -0.04482, -0.04482, -0.04482, -0.04482, -0.04482,
 -0.04482, -0.04482, -0.04482, -0.04482, -0.04482, -0.04482, -0.04482, -0.04482, -0.04482, -0.04482,
 -0.04482, -0.04482, -0.04482, -0.04482, -0.04482, -0.04482, -0.04482, -0.04482, -0.04482, -0.04482,
 -0.04482, -0.04482, -0.04482, -0.04482, -0.04482, -0.04482, -0.04482, -0.04482, -0.04482, -0.04482,
 -0.04482, -0.04482, -0.04482, -0.04482, -0.04482, -0.04482, -0.04482, -0.04482, -0.04482, -0.04482,
 -0.04482, -0.04482, -0.04482, -0.04482, -0.04482, -0.04482, -0.04482, -0.04482, -0.04482, -0.04482
],
# INC100 # Income greater than $100K
[
  0.00000,  0.27539,  0.27539,  0.03436, -0.26823,  0.27539,  0.03822,  0.27539,  0.55077,  0.55077,
  0.30974,  0.00716,  0.55077,  0.31360,  0.55077,  0.55077,  0.30974,  0.00716,  0.55077,  0.31360,
  0.55077,  0.30974, -0.23387,  0.30974,  0.07257,  0.30974,  0.00716,  0.00716, -0.23001,  0.00716,
  0.55077,  0.31360,  0.55077,  0.31360,  0.31360,  0.55077,  0.82616,  0.82616,  0.58513,  0.28255,
  0.82616,  0.58899,  0.82616,  0.82616,  0.58513,  0.28255,  0.82616,  0.58899,  0.82616,  0.58513,
  0.04152,  0.58513,  0.34796,  0.58513,  0.28255,  0.28255,  0.04538,  0.28255,  0.82616,  0.58899,
  0.82616,  0.58899,  0.58899,  0.82616,  0.82616,  0.58513,  0.28255,  0.82616,  0.58899,  0.82616,
  0.58513,  0.04152,  0.58513,  0.34796,  0.58513,  0.28255,  0.28255,  0.04538,  0.28255,  0.82616,
  0.58899,  0.82616,  0.58899,  0.58899,  0.82616,  0.58513,  0.04152,  0.58513,  0.34796,  0.58513,
  0.04152,  0.04152, -0.19565,  0.04152,  0.58513,  0.34796,  0.58513,  0.34796,  0.34796,  0.58513,
  0.28255,  0.28255,  0.04538,  0.28255,  0.28255,  0.04538,  0.28255,  0.04538,  0.04538,  0.28255,
  0.82616,  0.58899,  0.82616,  0.58899,  0.58899,  0.82616,  0.58899,  0.58899,  0.58899,  0.82616
],

# Income LT $50K
[  0, -0.8, -0.8, -0.8, -0.8, -0.8, -0.8, -0.8, -1.6, -1.6, 
-1.6, -1.6, -1.6, -1.6, -1.6, -1.6, -1.6, -1.6, -1.6, -1.6, 
-1.6, -1.6, -1.6, -1.6, -1.6, -1.6, -1.6, -1.6, -1.6, -1.6, 
-1.6, -1.6, -1.6, -1.6, -1.6, -1.6, -2.4, -2.4, -2.4, -2.4, 
-2.4, -2.4, -2.4, -2.4, -2.4, -2.4, -2.4, -2.4, -2.4, -2.4, 
-2.4, -2.4, -2.4, -2.4, -2.4, -2.4, -2.4, -2.4, -2.4, -2.4, 
-2.4, -2.4, -2.4, -2.4, -2.4, -2.4, -2.4, -2.4, -2.4, -2.4, 
-2.4, -2.4, -2.4, -2.4, -2.4, -2.4, -2.4, -2.4, -2.4, -2.4, 
-2.4, -2.4, -2.4, -2.4, -2.4, -2.4, -2.4, -2.4, -2.4, -2.4, 
-2.4, -2.4, -2.4, -2.4, -2.4, -2.4, -2.4, -2.4, -2.4, -2.4, 
-2.4, -2.4, -2.4, -2.4, -2.4, -2.4, -2.4, -2.4, -2.4, -2.4, 
-2.4, -2.4, -2.4, -2.4, -2.4, -2.4, -2.4, -2.4, -2.4, -2.4], 


]
transientCoeffs = [
# PTWRKR # PartTimeWorker
[
  0.00000, -0.24380, -0.41057, -0.41057, -0.08841, -0.41057, -0.41057, -0.41057, -0.65436, -0.65436,
 -0.65436, -0.33221, -0.65436, -0.65436, -0.65436, -0.82113, -0.82113, -0.49898, -0.82113, -0.82113,
 -0.82113, -0.82113, -0.49898, -0.82113, -0.82113, -0.82113, -0.49898, -0.49898, -0.49898, -0.49898,
 -0.82113, -0.82113, -0.82113, -0.82113, -0.82113, -0.82113, -1.06493, -1.06493, -1.06493, -0.74278,
 -1.06493, -1.06493, -1.06493, -1.06493, -1.06493, -0.74278, -1.06493, -1.06493, -1.06493, -1.06493,
 -0.74278, -1.06493, -1.06493, -1.06493, -0.74278, -0.74278, -0.74278, -0.74278, -1.06493, -1.06493,
 -1.06493, -1.06493, -1.06493, -1.06493, -1.23170, -1.23170, -0.90954, -1.23170, -1.23170, -1.23170,
 -1.23170, -0.90954, -1.23170, -1.23170, -1.23170, -0.90954, -0.90954, -0.90954, -0.90954, -1.23170,
 -1.23170, -1.23170, -1.23170, -1.23170, -1.23170, -1.23170, -0.90954, -1.23170, -1.23170, -1.23170,
 -0.90954, -0.90954, -0.90954, -0.90954, -1.23170, -1.23170, -1.23170, -1.23170, -1.23170, -1.23170,
 -0.90954, -0.90954, -0.90954, -0.90954, -0.90954, -0.90954, -0.90954, -0.90954, -0.90954, -0.90954,
 -1.23170, -1.23170, -1.23170, -1.23170, -1.23170, -1.23170, -1.23170, -1.23170, -1.23170, -1.23170
],
# FTWRKR # FullTimeWorker
[
  0.00000,  0.84005, -0.01406, -0.01406,  0.19732, -0.01406, -0.01406, -0.01406,  0.82599,  0.82599,
  0.82599,  1.03737,  0.82599,  0.82599,  0.82599, -0.02813, -0.02813,  0.18326, -0.02813, -0.02813,
 -0.02813, -0.02813,  0.18326, -0.02813, -0.02813, -0.02813,  0.18326,  0.18326,  0.18326,  0.18326,
 -0.02813, -0.02813, -0.02813, -0.02813, -0.02813, -0.02813,  0.81192,  0.81192,  0.81192,  1.02331,
  0.81192,  0.81192,  0.81192,  0.81192,  0.81192,  1.02331,  0.81192,  0.81192,  0.81192,  0.81192,
  1.02331,  0.81192,  0.81192,  0.81192,  1.02331,  1.02331,  1.02331,  1.02331,  0.81192,  0.81192,
  0.81192,  0.81192,  0.81192,  0.81192, -0.04219, -0.04219,  0.16919, -0.04219, -0.04219, -0.04219,
 -0.04219,  0.16919, -0.04219, -0.04219, -0.04219,  0.16919,  0.16919,  0.16919,  0.16919, -0.04219,
 -0.04219, -0.04219, -0.04219, -0.04219, -0.04219, -0.04219,  0.16919, -0.04219, -0.04219, -0.04219,
  0.16919,  0.16919,  0.16919,  0.16919, -0.04219, -0.04219, -0.04219, -0.04219, -0.04219, -0.04219,
  0.16919,  0.16919,  0.16919,  0.16919,  0.16919,  0.16919,  0.16919,  0.16919,  0.16919,  0.16919,
 -0.04219, -0.04219, -0.04219, -0.04219, -0.04219, -0.04219, -0.04219, -0.04219, -0.04219, -0.04219
],
# MALE #  
[
  0.00000,  0.02862,  0.02862,  0.02862, -0.27898,  0.02862,  0.02862,  0.02862,  0.05724,  0.05724,
  0.05724, -0.25036,  0.05724,  0.05724,  0.05724,  0.05724,  0.05724, -0.25036,  0.05724,  0.05724,
  0.05724,  0.05724, -0.25036,  0.05724,  0.05724,  0.05724, -0.25036, -0.25036, -0.25036, -0.25036,
  0.05724,  0.05724,  0.05724,  0.05724,  0.05724,  0.05724,  0.08585,  0.08585,  0.08585, -0.22175,
  0.08585,  0.08585,  0.08585,  0.08585,  0.08585, -0.22175,  0.08585,  0.08585,  0.08585,  0.08585,
 -0.22175,  0.08585,  0.08585,  0.08585, -0.22175, -0.22175, -0.22175, -0.22175,  0.08585,  0.08585,
  0.08585,  0.08585,  0.08585,  0.08585,  0.08585,  0.08585, -0.22175,  0.08585,  0.08585,  0.08585,
  0.08585, -0.22175,  0.08585,  0.08585,  0.08585, -0.22175, -0.22175, -0.22175, -0.22175,  0.08585,
  0.08585,  0.08585,  0.08585,  0.08585,  0.08585,  0.08585, -0.22175,  0.08585,  0.08585,  0.08585,
 -0.22175, -0.22175, -0.22175, -0.22175,  0.08585,  0.08585,  0.08585,  0.08585,  0.08585,  0.08585,
 -0.22175, -0.22175, -0.22175, -0.22175, -0.22175, -0.22175, -0.22175, -0.22175, -0.22175, -0.22175,
  0.08585,  0.08585,  0.08585,  0.08585,  0.08585,  0.08585,  0.08585,  0.08585,  0.08585,  0.08585
],
# AGEGR35 # Age greater than 35
[
  0.00000,  0.09586,  0.09586,  0.09586,  0.09586,  0.09586,  0.09586,  0.09586,  0.09586,  0.09586,
  0.09586,  0.09586,  0.09586,  0.09586,  0.09586,  0.09586,  0.09586,  0.09586,  0.09586,  0.09586,
  0.09586,  0.09586,  0.09586,  0.09586,  0.09586,  0.09586,  0.09586,  0.09586,  0.09586,  0.09586,
  0.09586,  0.09586,  0.09586,  0.09586,  0.09586,  0.09586,  0.09586,  0.09586,  0.09586,  0.09586,
  0.09586,  0.09586,  0.09586,  0.09586,  0.09586,  0.09586,  0.09586,  0.09586,  0.09586,  0.09586,
  0.09586,  0.09586,  0.09586,  0.09586,  0.09586,  0.09586,  0.09586,  0.09586,  0.09586,  0.09586,
  0.09586,  0.09586,  0.09586,  0.09586,  0.09586,  0.09586,  0.09586,  0.09586,  0.09586,  0.09586,
  0.09586,  0.09586,  0.09586,  0.09586,  0.09586,  0.09586,  0.09586,  0.09586,  0.09586,  0.09586,
  0.09586,  0.09586,  0.09586,  0.09586,  0.09586,  0.09586,  0.09586,  0.09586,  0.09586,  0.09586,
  0.09586,  0.09586,  0.09586,  0.09586,  0.09586,  0.09586,  0.09586,  0.09586,  0.09586,  0.09586,
  0.09586,  0.09586,  0.09586,  0.09586,  0.09586,  0.09586,  0.09586,  0.09586,  0.09586,  0.09586,
  0.09586,  0.09586,  0.09586,  0.09586,  0.09586,  0.09586,  0.09586,  0.09586,  0.09586,  0.09586
],
# NFJNT # Number of fully joint tours
[
  0.00000,  0.00000,  0.00000,  0.37602,  0.48106,  0.00000,  0.03462,  0.36935,  0.00000,  0.00000,
  0.37602,  0.48106,  0.00000,  0.03462,  0.36935,  0.00000,  0.37602,  0.48106,  0.00000,  0.03462,
  0.36935,  0.37602,  0.85709,  0.37602,  0.41065,  0.74537,  0.48106,  0.48106,  0.51569,  0.85041,
  0.00000,  0.03462,  0.36935,  0.03462,  0.40397,  0.36935,  0.00000,  0.00000,  0.37602,  0.48106,
  0.00000,  0.03462,  0.36935,  0.00000,  0.37602,  0.48106,  0.00000,  0.03462,  0.36935,  0.37602,
  0.85709,  0.37602,  0.41065,  0.74537,  0.48106,  0.48106,  0.51569,  0.85041,  0.00000,  0.03462,
  0.36935,  0.03462,  0.40397,  0.36935,  0.00000,  0.37602,  0.48106,  0.00000,  0.03462,  0.36935,
  0.37602,  0.85709,  0.37602,  0.41065,  0.74537,  0.48106,  0.48106,  0.51569,  0.85041,  0.00000,
  0.03462,  0.36935,  0.03462,  0.40397,  0.36935,  0.37602,  0.85709,  0.37602,  0.41065,  0.74537,
  0.85709,  0.85709,  0.89171,  1.22644,  0.37602,  0.41065,  0.74537,  0.41065,  0.78000,  0.74537,
  0.48106,  0.48106,  0.51569,  0.85041,  0.48106,  0.51569,  0.85041,  0.51569,  0.88504,  0.85041,
  0.00000,  0.03462,  0.36935,  0.03462,  0.40397,  0.36935,  0.03462,  0.40397,  0.40397,  0.36935
],
# NMAN_TR # Number of non-mandatory tours
[
  0.00000,  0.38950,  0.38950,  0.43914,  0.38950,  0.38950,  0.50883,  0.38950,  0.46393,  0.46393,
  0.51357,  0.46393,  0.46393,  0.58326,  0.46393,  0.46393,  0.51357,  0.46393,  0.46393,  0.58326,
  0.46393,  0.51357,  0.51357,  0.51357,  0.63290,  0.51357,  0.46393,  0.46393,  0.58326,  0.46393,
  0.46393,  0.58326,  0.46393,  0.58326,  0.58326,  0.46393,  0.00000,  0.00000,  0.04964,  0.00000,
  0.00000,  0.11933,  0.00000,  0.00000,  0.04964,  0.00000,  0.00000,  0.11933,  0.00000,  0.04964,
  0.04964,  0.04964,  0.16897,  0.04964,  0.00000,  0.00000,  0.11933,  0.00000,  0.00000,  0.11933,
  0.00000,  0.11933,  0.11933,  0.00000,  0.00000,  0.04964,  0.00000,  0.00000,  0.11933,  0.00000,
  0.04964,  0.04964,  0.04964,  0.16897,  0.04964,  0.00000,  0.00000,  0.11933,  0.00000,  0.00000,
  0.11933,  0.00000,  0.11933,  0.11933,  0.00000,  0.04964,  0.04964,  0.04964,  0.16897,  0.04964,
  0.04964,  0.04964,  0.16897,  0.04964,  0.04964,  0.16897,  0.04964,  0.16897,  0.16897,  0.04964,
  0.00000,  0.00000,  0.11933,  0.00000,  0.00000,  0.11933,  0.00000,  0.11933,  0.11933,  0.00000,
  0.00000,  0.11933,  0.00000,  0.11933,  0.11933,  0.00000,  0.11933,  0.11933,  0.11933,  0.00000
],
# SCHESC_PR # School escorting on work tour
[
  0.00000, -1.31177, -1.31177, -1.31177, -1.31177, -1.31177, -1.31177, -1.31177, -1.78345, -1.78345,
 -1.78345, -1.78345, -1.78345, -1.78345, -1.78345, -1.78345, -1.78345, -1.78345, -1.78345, -1.78345,
 -1.78345, -1.78345, -1.78345, -1.78345, -1.78345, -1.78345, -1.78345, -1.78345, -1.78345, -1.78345,
 -1.78345, -1.78345, -1.78345, -1.78345, -1.78345, -1.78345, -1.78345, -1.78345, -1.78345, -1.78345,
 -1.78345, -1.78345, -1.78345, -1.78345, -1.78345, -1.78345, -1.78345, -1.78345, -1.78345, -1.78345,
 -1.78345, -1.78345, -1.78345, -1.78345, -1.78345, -1.78345, -1.78345, -1.78345, -1.78345, -1.78345,
 -1.78345, -1.78345, -1.78345, -1.78345, -1.78345, -1.78345, -1.78345, -1.78345, -1.78345, -1.78345,
 -1.78345, -1.78345, -1.78345, -1.78345, -1.78345, -1.78345, -1.78345, -1.78345, -1.78345, -1.78345,
 -1.78345, -1.78345, -1.78345, -1.78345, -1.78345, -1.78345, -1.78345, -1.78345, -1.78345, -1.78345,
 -1.78345, -1.78345, -1.78345, -1.78345, -1.78345, -1.78345, -1.78345, -1.78345, -1.78345, -1.78345,
 -1.78345, -1.78345, -1.78345, -1.78345, -1.78345, -1.78345, -1.78345, -1.78345, -1.78345, -1.78345,
 -1.78345, -1.78345, -1.78345, -1.78345, -1.78345, -1.78345, -1.78345, -1.78345, -1.78345, -1.78345
],
# DISTANCE # Distance - HT1+HT2
[
  0.00000,  0.00906,  0.00906,  0.01092,  0.01168,  0.00906,  0.00906,  0.00906,  0.00906,  0.00906,
  0.01092,  0.01168,  0.00906,  0.00906,  0.00906,  0.00906,  0.01092,  0.01168,  0.00906,  0.00906,
  0.00906,  0.01092,  0.01353,  0.01092,  0.01092,  0.01092,  0.01168,  0.01168,  0.01168,  0.01168,
  0.00906,  0.00906,  0.00906,  0.00906,  0.00906,  0.00906,  0.00906,  0.00906,  0.01092,  0.01168,
  0.00906,  0.00906,  0.00906,  0.00906,  0.01092,  0.01168,  0.00906,  0.00906,  0.00906,  0.01092,
  0.01353,  0.01092,  0.01092,  0.01092,  0.01168,  0.01168,  0.01168,  0.01168,  0.00906,  0.00906,
  0.00906,  0.00906,  0.00906,  0.00906,  0.00906,  0.01092,  0.01168,  0.00906,  0.00906,  0.00906,
  0.01092,  0.01353,  0.01092,  0.01092,  0.01092,  0.01168,  0.01168,  0.01168,  0.01168,  0.00906,
  0.00906,  0.00906,  0.00906,  0.00906,  0.00906,  0.01092,  0.01353,  0.01092,  0.01092,  0.01092,
  0.01353,  0.01353,  0.01353,  0.01353,  0.01092,  0.01092,  0.01092,  0.01092,  0.01092,  0.01092,
  0.01168,  0.01168,  0.01168,  0.01168,  0.01168,  0.01168,  0.01168,  0.01168,  0.01168,  0.01168,
  0.00906,  0.00906,  0.00906,  0.00906,  0.00906,  0.00906,  0.00906,  0.00906,  0.00906,  0.00906
],
# DMXDENS # Mixed density at destination
[
  0.00000,  0.00010,  0.00010,  0.00010,  0.00010,  0.00010,  0.00010,  0.00010,  0.00010,  0.00010,
  0.00010,  0.00010,  0.00010,  0.00010,  0.00010,  0.00010,  0.00010,  0.00010,  0.00010,  0.00010,
  0.00010,  0.00010,  0.00010,  0.00010,  0.00010,  0.00010,  0.00010,  0.00010,  0.00010,  0.00010,
  0.00010,  0.00010,  0.00010,  0.00010,  0.00010,  0.00010,  0.00010,  0.00010,  0.00010,  0.00010,
  0.00010,  0.00010,  0.00010,  0.00010,  0.00010,  0.00010,  0.00010,  0.00010,  0.00010,  0.00010,
  0.00010,  0.00010,  0.00010,  0.00010,  0.00010,  0.00010,  0.00010,  0.00010,  0.00010,  0.00010,
  0.00010,  0.00010,  0.00010,  0.00010,  0.00010,  0.00010,  0.00010,  0.00010,  0.00010,  0.00010,
  0.00010,  0.00010,  0.00010,  0.00010,  0.00010,  0.00010,  0.00010,  0.00010,  0.00010,  0.00010,
  0.00010,  0.00010,  0.00010,  0.00010,  0.00010,  0.00010,  0.00010,  0.00010,  0.00010,  0.00010,
  0.00010,  0.00010,  0.00010,  0.00010,  0.00010,  0.00010,  0.00010,  0.00010,  0.00010,  0.00010,
  0.00010,  0.00010,  0.00010,  0.00010,  0.00010,  0.00010,  0.00010,  0.00010,  0.00010,  0.00010,
  0.00010,  0.00010,  0.00010,  0.00010,  0.00010,  0.00010,  0.00010,  0.00010,  0.00010,  0.00010
],
# (DEPPER2-ARRPER2) # Duration of Tour Activity (in number of 30-min periods)
[
  0.00000,  0.00000,  0.00000,  0.00000,  0.00000,  0.00000,  0.00000,  0.00000, -0.04474, -0.04474,
 -0.04474, -0.04474, -0.04474, -0.04474, -0.04474, -0.04474, -0.04474, -0.04474, -0.04474, -0.04474,
 -0.04474, -0.04474, -0.04474, -0.04474, -0.04474, -0.04474, -0.04474, -0.04474, -0.04474, -0.04474,
 -0.04474, -0.04474, -0.04474, -0.04474, -0.04474, -0.04474, -0.04474, -0.04474, -0.04474, -0.04474,
 -0.04474, -0.04474, -0.04474, -0.04474, -0.04474, -0.04474, -0.04474, -0.04474, -0.04474, -0.04474,
 -0.04474, -0.04474, -0.04474, -0.04474, -0.04474, -0.04474, -0.04474, -0.04474, -0.04474, -0.04474,
 -0.04474, -0.04474, -0.04474, -0.04474, -0.04474, -0.04474, -0.04474, -0.04474, -0.04474, -0.04474,
 -0.04474, -0.04474, -0.04474, -0.04474, -0.04474, -0.04474, -0.04474, -0.04474, -0.04474, -0.04474,
 -0.04474, -0.04474, -0.04474, -0.04474, -0.04474, -0.04474, -0.04474, -0.04474, -0.04474, -0.04474,
 -0.04474, -0.04474, -0.04474, -0.04474, -0.04474, -0.04474, -0.04474, -0.04474, -0.04474, -0.04474,
 -0.04474, -0.04474, -0.04474, -0.04474, -0.04474, -0.04474, -0.04474, -0.04474, -0.04474, -0.04474,
 -0.04474, -0.04474, -0.04474, -0.04474, -0.04474, -0.04474, -0.04474, -0.04474, -0.04474, -0.04474
],
# LOG(1+PERAVHT1) # ln(1 + Number of Available Periods)
[
  0.00000,  1.50981,  1.50981,  1.50981,  1.50981,  1.50981,  1.50981,  1.50981,  3.56198,  3.56198,
  3.56198,  3.56198,  3.56198,  3.56198,  3.56198,  3.56198,  3.56198,  3.56198,  3.56198,  3.56198,
  3.56198,  3.56198,  3.56198,  3.56198,  3.56198,  3.56198,  3.56198,  3.56198,  3.56198,  3.56198,
  3.56198,  3.56198,  3.56198,  3.56198,  3.56198,  3.56198,  3.56198,  3.56198,  3.56198,  3.56198,
  3.56198,  3.56198,  3.56198,  3.56198,  3.56198,  3.56198,  3.56198,  3.56198,  3.56198,  3.56198,
  3.56198,  3.56198,  3.56198,  3.56198,  3.56198,  3.56198,  3.56198,  3.56198,  3.56198,  3.56198,
  3.56198,  3.56198,  3.56198,  3.56198,  3.56198,  3.56198,  3.56198,  3.56198,  3.56198,  3.56198,
  3.56198,  3.56198,  3.56198,  3.56198,  3.56198,  3.56198,  3.56198,  3.56198,  3.56198,  3.56198,
  3.56198,  3.56198,  3.56198,  3.56198,  3.56198,  3.56198,  3.56198,  3.56198,  3.56198,  3.56198,
  3.56198,  3.56198,  3.56198,  3.56198,  3.56198,  3.56198,  3.56198,  3.56198,  3.56198,  3.56198,
  3.56198,  3.56198,  3.56198,  3.56198,  3.56198,  3.56198,  3.56198,  3.56198,  3.56198,  3.56198,
  3.56198,  3.56198,  3.56198,  3.56198,  3.56198,  3.56198,  3.56198,  3.56198,  3.56198,  3.56198
],
# BEFOREAM # Arrival time before 9AM
[  0, -3.41883, -0.65581, -2.43797, -2.00477, -2.43184, -1.12975, -0.14805, -3.61883, -3.61883, 
-5.40099, -4.96779, -5.39486, -4.09277, -3.11107, -0.85581, -2.63797, -2.20477, -2.63184, -1.32975, 
-0.34805, -2.63797, -3.98692, -4.41399, -3.1119, -2.1302, -2.20477, -3.9808, -2.6787, -1.697, 
-2.63184, -3.10577, -2.12407, -1.32975, -0.82198, -0.34805, -3.81883, -3.81883, -5.60099, -5.16779, 
-5.59486, -4.29277, -3.31107, -3.81883, -5.60099, -5.16779, -5.59486, -4.29277, -3.31107, -5.60099, 
-6.94994, -7.37702, -6.07492, -5.09322, -5.16779, -6.94382, -5.64172, -4.66002, -5.59486, -6.06879, 
-5.08709, -4.29277, -3.785, -3.31107, -1.05581, -2.83797, -2.40477, -2.83184, -1.52975, -0.54805, 
-2.83797, -4.18692, -4.61399, -3.3119, -2.3302, -2.40477, -4.1808, -2.8787, -1.897, -2.83184, 
-3.30577, -2.32407, -1.52975, -1.02198, -0.54805, -2.83797, -4.18692, -4.61399, -3.3119, -2.3302, 
-4.18692, -5.96295, -4.66086, -3.67916, -4.61399, -5.08793, -4.10623, -3.3119, -2.80413, -2.3302, 
-2.40477, -4.1808, -2.8787, -1.897, -4.1808, -4.65473, -3.67303, -2.8787, -2.37093, -1.897, 
-2.83184, -3.30577, -2.32407, -3.30577, -2.798, -2.32407, -1.52975, -1.02198, -1.02198, -0.54805], 
# NOON_AM # Arrival time between 9AM and 12 PM
[  0, -0.31875, 0.75, -0.80098, -0.0718, 0.45801, 0.58315, 0.73146, 0.43125, 0.43125, 
-1.11973, -0.39055, 0.13926, 0.2644, 0.41271, 1.5, -0.05098, 0.6782, 1.20801, 1.33315, 
1.48146, -0.05098, -0.87277, -0.34297, -0.21783, -0.06952, 0.6782, 0.38621, 0.51135, 0.65966, 
1.20801, 1.04116, 1.18947, 1.33315, 1.31461, 1.48146, 1.18125, 1.18125, -0.36973, 0.35945, 
0.88926, 1.0144, 1.16271, 1.18125, -0.36973, 0.35945, 0.88926, 1.0144, 1.16271, -0.36973, 
-1.19152, -0.66172, -0.53658, -0.38827, 0.35945, 0.06746, 0.1926, 0.34091, 0.88926, 0.72241, 
0.87072, 1.0144, 0.99585, 1.16271, 2.25, 0.69902, 1.4282, 1.95801, 2.08315, 2.23146, 
0.69902, -0.12277, 0.40703, 0.53217, 0.68048, 1.4282, 1.13621, 1.26135, 1.40966, 1.95801, 
1.79116, 1.93947, 2.08315, 2.06461, 2.23146, 0.69902, -0.12277, 0.40703, 0.53217, 0.68048, 
-0.12277, -0.41476, -0.28962, -0.14131, 0.40703, 0.24018, 0.38849, 0.53217, 0.51363, 0.68048, 
1.4282, 1.13621, 1.26135, 1.40966, 1.13621, 0.96936, 1.11767, 1.26135, 1.24281, 1.40966, 
1.95801, 1.79116, 1.93947, 1.79116, 1.77262, 1.93947, 2.08315, 2.06461, 2.06461, 2.23146], 

# RET_PM1 # Arrival time after 4PM
[
  0.00000,  0.00000,  0.00000, -0.59617, -0.53066, -0.42517,  0.31837,  0.00000,  0.00000,  0.00000,
 -0.59617, -0.53066, -0.42517,  0.31837,  0.00000,  0.00000, -0.59617, -0.53066, -0.42517,  0.31837,
  0.00000, -0.59617, -1.12684, -1.02134, -0.27780, -0.59617, -0.53066, -0.95583, -0.21229, -0.53066,
 -0.42517, -0.10679, -0.42517,  0.31837,  0.31837,  0.00000,  0.00000,  0.00000, -0.59617, -0.53066,
 -0.42517,  0.31837,  0.00000,  0.00000, -0.59617, -0.53066, -0.42517,  0.31837,  0.00000, -0.59617,
 -1.12684, -1.02134, -0.27780, -0.59617, -0.53066, -0.95583, -0.21229, -0.53066, -0.42517, -0.10679,
 -0.42517,  0.31837,  0.31837,  0.00000,  0.00000, -0.59617, -0.53066, -0.42517,  0.31837,  0.00000,
 -0.59617, -1.12684, -1.02134, -0.27780, -0.59617, -0.53066, -0.95583, -0.21229, -0.53066, -0.42517,
 -0.10679, -0.42517,  0.31837,  0.31837,  0.00000, -0.59617, -1.12684, -1.02134, -0.27780, -0.59617,
 -1.12684, -1.55200, -0.80846, -1.12684, -1.02134, -0.70296, -1.02134, -0.27780, -0.27780, -0.59617,
 -0.53066, -0.95583, -0.21229, -0.53066, -0.95583, -0.63745, -0.95583, -0.21229, -0.21229, -0.53066,
 -0.42517, -0.10679, -0.42517, -0.10679, -0.10679, -0.42517,  0.31837,  0.31837,  0.31837,  0.00000
],
# Child3
[  0, -2, -2, -2, -2, -2, -2, -2, -4, -4, 
-4, -4, -4, -4, -4, -4, -4, -4, -4, -4, 
-4, -4, -4, -4, -4, -4, -4, -4, -4, -4, 
-4, -4, -4, -4, -4, -4, -6, -6, -6, -6, 
-6, -6, -6, -6, -6, -6, -6, -6, -6, -6, 
-6, -6, -6, -6, -6, -6, -6, -6, -6, -6, 
-6, -6, -6, -6, -6, -6, -6, -6, -6, -6, 
-6, -6, -6, -6, -6, -6, -6, -6, -6, -6, 
-6, -6, -6, -6, -6, -6, -6, -6, -6, -6, 
-6, -6, -6, -6, -6, -6, -6, -6, -6, -6, 
-6, -6, -6, -6, -6, -6, -6, -6, -6, -6, 
-6, -6, -6, -6, -6, -6, -6, -6, -6, -6], 


]

from StopGenerationSubmodelWorkHalfTour1Maps import durableCoeffMap,transientCoeffMap