####################################################################
# StopGenerationSubmodel_WorkBasedHalfTour1.py
# WorkBased Tours Half Tour 1 submodel for Stop Generation
####################################################################

from StopGenerationSubmodelCommon import *
from StopGenMemDataRefs import *

parameters = {
              # These are the parameters to generate the specific stop alternatives for this model
              "MaxStops" : 1,
              "StopPurposeDescriptions" : ['work stops', 'pb stops', 'shop stops', 'meal stops',  'socrec stops', 'esc stops'],
              "StopPurposeIds" : [2, 32, 16, 8, 64, 128],
              #Exclusions (work tours)
              "unavailableAlternativesA" : [ ],
              #Exclusions (non-work tours)
              "unavailableAlternativesB" : [ 1],
             }

#Alternatives determined by the combination of stop purposes and maximum number of stops
altIntrinsicValues = [   0,   1,   2,   3,   4,   5,   6,]

# altNames is required for config file but not used here because of the complexity of the alternatives
altNames = []

nestList = [
["Root", 0, 1.0, [], [1, 2]],
["0-stop alts", 1, 1.0, [0], []],
["1-stop alts", 2, 1.0, [   1,   2,   3,   4,   5,  6,], []],
]
           
						# 0 stop     # 1 work     # 1 persbus  # 1 shop     # 1 eat      # 1 socrec   # 1 escort
#altSpecificConsts =  [  0.00000000, -5.75045095, -8.83970969, -4.45483197, -6.05192944, -4.24402918, -5.10541148]
#altSpecificConsts = [  0.00000000, -5.25045095, -8.83970969, -4.70483197, -6.05192944, -4.74402918, -5.10541148]
#altSpecificConsts = [  0.00000000, -5.00045095, -8.63970969, -4.65483197, -5.55192944, -4.84402918, -5.10541148]
#altSpecificConsts = [  0.00000000, -4.35045095, -8.23970969, -4.70483197, -5.40192944, -4.59402918, -5.10541148]
#altSpecificConsts = [  0.00000000, -3.75045095, -8.23970969, -4.60483197, -5.05192944, -4.44402918, -5.10541148]
#altSpecificConsts = [  0.00000000, -2.25045095, -8.23970969, -4.95483197, -5.30192944, -4.44402918, -5.10541148]
#altSpecificConsts = [  0.00000000, -2.75045095, -8.23970969, -5.05483197, -5.20192944, -4.44402918, -5.10541148]
#altSpecificConsts = [  0.00000000, -2.85045095, -8.23970969, -4.20483197, -5.30192944, -4.44402918, -5.10541148]
#altSpecificConsts = [  0.00000000, -2.85045095, -8.23970969, -4.45483197, -5.05192944, -4.44402918, -5.10541148]
altSpecificConsts = [  0.00000000, -2.85045095, -8.23970969, -4.95483197, -4.80192944, -4.44402918, -5.10541148]


durableCoeffs = [
 # 0 stop     # 1 work     # 1 persbus  # 1 shop     # 1 eat      # 1 socrec   # 1 escort
[  0.00000000, -2.54962048,  0.00000000, -2.54962048, -2.54962048,  0.00000000,  0.00000000], # 0 inc50 # HH Income < $50K 
[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.29932099,  0.00000000], # 1 inc100 # HH Income > $100K
]
transientCoeffs = [
###### 0 Tour Purpose
[ placeholder]*7,
[  0.00000000,  1.02052239,  1.02052239,  1.02052239,  1.02052239,  1.02052239,  1.02052239], # 1 ftwrkr # Full-Time Worker
[  0.00000000,  0.00000000,  0.37279556, -0.48361582,  0.00000000, -0.48361582,  0.00000000], # 2 male #  
[  0.00000000,  0.01849609,  0.01849609, -0.31388896,  0.01849609,  0.01849609,  0.01849609], # 3 distance # Round Trip Auto Travel Distance (mi)
[  0.00000000,  0.18181910,  0.06880806, -1.91554788, -0.15571950,  0.06880806,  0.06880806], # 4 (depper2-arrper2) # Duration of Tour Activity (in number of 30-min periods)
[  0.00000000,  0.12116415,  0.12116415,  0.12116415,  0.30760894,  0.12116415,  0.12116415], # 5 log(peravht1+1) # ln(1 + Number of Available Periods in HT1)
[  0.00000000,  0.00000000,  3.45530737,  0.00000000,  0.00000000,  0.23799928, -0.46671112], # 6 befoream # Arrival time before 9 AM
[  0.00000000, -0.76332263, -0.76332263, -0.76332263, -0.76332263, -0.76332263, -0.76332263], # 7 noon_am # Arrival time 9 AM to 12 PM
[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000, -0.65963023], # 8 aft_noon # Arrival time after 12 PM
]

from StopGenerationSubmodelWorkBasedHalfTour1Maps import durableCoeffMap,transientCoeffMap

segmentDefinitions = [{'Name': 'Tour Purpose', 'DataRef': 'Tour','Offset': 0, 'DataRange': [8, 16, 32, 64, 128]},
]
segmentCoeffMap = [{'Segment': 0, 'Vector': 'transient', 'Offset': 0,  # Tour Purpose
  'Coefficients': [
 # #  Meal      Shop      PerBus   SocRec    Esc # PURPOSE  
[  0.00000,  0.00000,  0.00000,  0.00000,  0.00000,],
[  0.00000,  0.00000,  0.00000,  0.00000,  0.00000,],
[  0.00000,  0.00000,  4.65647,  0.00000,  0.00000,],
[  0.00000,  -0.75,  2.08538,  0.00000,  0.00000,],
[  0.3,  1.32637,  1.29834,  0.00000,  0.00000,],
[  0.3,  -0.75,  0.00000,  0.64785,  0.00000,],
[  0.3,  -0.75,  0.00000,  0.00000,  0.00000,],
]
  },
]
