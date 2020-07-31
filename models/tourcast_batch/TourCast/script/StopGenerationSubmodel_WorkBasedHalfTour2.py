####################################################################
# StopGenerationSubmodel_WorkBasedHalfTour2.py
# WorkBased Tours Half Tour 2 submodel for Stop Generation
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
#altSpecificConsts = [  0.00000000, -5.01014918, -6.07597118, -7.60878890, -8.63787780, -4.47023124, -4.72347185] 
#altSpecificConsts = [  0.00000000, -4.51014918, -6.07597118, -7.6087889, -8.8878778, -4.97023124, -4.72347185]
#altSpecificConsts = [  0.00000000, -4.26014918, -5.87597118, -7.3587889, -8.8378778, -4.97023124, -4.72347185]
#altSpecificConsts = [  0.00000000, -3.61014918, -5.87597118, -7.1087889, -8.6378778, -4.97023124, -4.72347185]
#altSpecificConsts = [  0.00000000, -3.01014918, -5.82597118, -6.8587889, -8.6378778, -4.97023124, -4.72347185]
#altSpecificConsts = [  0.00000000, -2.51014918, -5.82597118, -6.8587889, -8.6378778, -4.97023124, -4.72347185]
#altSpecificConsts = [  0.00000000, -2.26014918, -5.82597118, -6.9087889, -8.6378778, -4.97023124, -4.72347185]
#altSpecificConsts = [  0.00000000, -2.11014918, -5.82597118, -6.8587889, -8.6378778, -4.97023124, -4.72347185]
#altSpecificConsts = [  0.00000000, -2.11014918, -5.82597118, -6.8587889, -8.6378778, -4.97023124, -4.72347185]
altSpecificConsts = [  0.00000000, -2.11014918, -5.82597118, -6.8587889, -8.6378778, -4.97023124, -4.72347185]
                   


durableCoeffs = [
 # 0 stop     # 1 work     # 1 persbus  # 1 shop     # 1 eat      # 1 socrec   # 1 escort
[  0.00000000, -0.78688126,  0.00000000, -0.78688126, -0.78688126,  0.00000000,  0.00000000], # inc50 # HH Income < $50K 

]
transientCoeffs = [
###### 0 Tour Purpose
[ placeholder]*7,
 # 0 stop     # 1 work     # 1 persbus  # 1 shop     # 1 eat      # 1 socrec   # 1 escort
[  0.00000000, -0.19607758, -0.19607758, -0.19607758, -0.19607758, -0.19607758, -0.19607758], # 1 ftwrkr # Full-Time Worker
[  0.00000000,  0.00000000,  0.00000000,  0.48531253,  0.00000000,  0.48531253,  0.00000000], # 2 male #  
[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  1.88551495,  0.00000000,  0.00000000], # 3 nwork # Number of Work Tours
[  0.00000000,  0.00318460,  0.00318460,  0.03680325,  0.00318460,  0.00318460,  0.00318460], # 4 distance # Round Trip Auto Travel Distance (mi)
[  0.00000000,  0.03093804,  0.03093804,  0.03093804,  0.03093804,  0.03093804,  0.03093804], # 5 (depper2-arrper2) # Duration of Tour Activity (in number of 30-min periods)
[  0.00000000,  0.21672663,  0.21672663,  0.21672663,  1.49644398,  0.21672663,  0.21672663], # 6 log(peravht2+1) # ln(1 + Number of Available Periods in HT2)
[  0.00000000,  2.19565927,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  2.11173469], # 7 befoream # Departure time before 9 AM
[  0.00000000,  1.32085959,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 8 noon_am # Departure time 9 AM to 12 PM
]

from StopGenerationSubmodelWorkBasedHalfTour2Maps import durableCoeffMap,transientCoeffMap

segmentDefinitions = [{'Name': 'Tour Purpose', 'DataRef': 'Tour','Offset': 0, 'DataRange': [8, 16, 32, 64, 128]},
]
segmentCoeffMap = [{'Segment': 0, 'Vector': 'transient', 'Offset': 0,  # Tour Purpose
  'Coefficients': [
 # #  Meal      Shop      PerBus   SocRec    Esc # PURPOSE  
[  0.00000,  0.00000,  0.00000,  0.00000,  0.00000,],
[  0.00000,  0.00000,  0.00000,  0.00000,  0.00000,],
[  0.00000,  0.00000,  1.71206,  0.00000,  0.00000,],
[  0.00000,  3.68581,  3.32346,  0.00000,  0.00000,],
[  0.00000,  1.55822,  2.03493,  0.00000,  0.00000,],
[  0.00000,  0.00000,  0.00000,  0.00000,  0.00000,],
[  0.00000,  0.00000,  0.00000,  0.00000,  0.00000,],
]
  },
]

