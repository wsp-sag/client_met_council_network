####################################################################
# StopGenerationSubmodel_Escort.py
# Non School Escort Tours
####################################################################

from Globals import *

# the name of the corresponding class on the C# side:
# this allows for multiple scripts targeting the same component
modelComponentName="StopGenerationEscortSubmodel"

logitType="NestedLogit"

from StopGenMemDataRefs import *

altIntrinsicValues = [0, 1, 2, 3, 4, 5]

altNames = ["0 stops", "1 ht1", "1 ht2", "2 ht1", "1 ht1 & 1 ht2", "2 ht2"]

nestList = [
["Root", 0, 1, [], [1, 2]],
["0-stop alts", 1, 1, [0], []],
["1+-stop alts", 2, 1, [1, 2, 3, 4, 5], []]
]

                        # 0 stops    # 1 ht1      # 1 ht2      # 2 ht1      # 1 ht1&1 ht2 # 2 ht2 
altSpecificConsts = [ 0, -6.38852402, -6.45234328, -7.78380765, -6.82182309, -7.84177604 ] 

durableCoeffs = [
 # 0 stops    # 1 ht1      # 1 ht2      # 2 ht1      # 1 ht1&1 ht2 # 2 ht2 
[  0.00000000, -0.11014926, -0.11014926, -0.11014926, -0.11014926, -0.11014926], # children # Number of children in HH
]

transientCoeffs = [
 # 0 stops    # 1 ht1      # 1 ht2      # 2 ht1      # 1 ht1&1 ht2 # 2 ht2 
[  0.00000000,  2.02174592,  2.02174592,  2.02174592,  2.02174592,  2.02174592], # 0 chd515 # Child Age 5-15 
[  0.00000000,  1.71213213,  1.71213213,  1.71213213,  1.71213213,  1.71213213], # 1 chd16p # Child Age 16+
[  0.00000000, -0.38214793, -0.38214793, -0.38214793, -0.38214793, -0.38214793], # 2 male #  
[  0.00000000,  1.77873782,  1.77873782,  1.77873782,  1.77873782,  1.77873782], # 3 ageg35 # Age greater than 35
[  0.00000000,  0.78449260,  0.78449260,  1.56898519,  1.56898519,  1.56898519], # 4 ifge(nwork,1) # 1+ Work Tours in Day
[  0.00000000, -0.52807860, -0.52807860, -0.52807860, -0.52807860, -0.52807860], # 5 ifge(nfjnt,1) # 1+ Fully Joint Tours in Day
[  0.00000000,  0.00028017,  0.00028017,  0.00028017,  0.00028017,  0.00028017], # 6 dmxdens # Mixed density at destination
[  0.00000000,  0.10902005,  0.10902005,  0.10902005,  0.10902005,  0.10902005], # 7 (depper2-arrper2) # Duration of Tour Activity (in number of 30-min periods)
[  0.00000000,  0.35633311,  0.35633311,  0.35633311,  0.35633311,  0.35633311], # 8 log(1+peravht1) # ln(1 + Number of Available Periods in HT1)
[  0.00000000,  0.43095078,  0.43095078,  0.43095078,  0.43095078,  0.43095078], # 9 log(1+peravht2) # ln(1 + Number of Available Periods in HT2)
]

durableCoeffMap = {
		"Household" : [[5,0,1]]
    }

transientCoeffMap = {
        "Person" : [
                    [0, 0, 2],
                    [4, 2, 2]
                ],
        "Day" : [
                 [12, 4, 2],
                ],
        "TourLevelOfService" : [
                                [1, 6, 1],
                            ],
        "Tour" : [
                  [1, 7, 3]
                ],
    }
