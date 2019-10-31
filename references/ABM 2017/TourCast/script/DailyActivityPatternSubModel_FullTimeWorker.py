####################################################################
# DailyActivityPatternSubModel_FullTimeWorker.py
# TBI version
# 
####################################################################

from Globals import *

# the name of the corresponding class on the C# side:
# this allows for multiple scripts targeting the same component
modelComponentName="DAPFullTimeWorker"  

from DAPMemoryDataReferences import *

# Matrices are different enough to require their own structure:
matrixReferences = [
# for now none
]


# ######################  model structure section  ##########################

# TBI: updated:
# DAP Ids for     ************************
altIntrinsicValues= [1, 2, 3, 4, 5, 6, 7, 10, 14, 15, 17]#  

# TBI: updated:
# friendly descriptions of the alternatives, maybe for UI display somehow
altNames = ["1Wk-S", "1Wk+S", "2 Wk -S", "2Wk + 1S", "2Wk + 2 St", "1 UNI + 1Wk -S", "1UNI + 1Wk +S", "1 UNI", "NMT", "SAH", "EXT"]

# TBI: OK:
# this should evolve into a specification (in general) a tree structure
logitType = "NestedLogit"

# TBI: nest coeffs updated
# nest structure
# note that our implementation requires that each nest contains either other nests or bare alternatives, not both
# so here e.g. there is a non mandatory travel nest with only one subnode, to prevent the root node from containing 3 nests + one alternative
#   [UI name, nestID, nest coeff, [alts], [nests]]
# where [alts] refers to alternatives by its order in any of the altIntrinsicValues/altNames/durableCoeffs/transientCoeffs lists
# and [nests] is a list of nestIDs
# any subnest must have nest coeff(aka theta) less than the level above
# nests have either all alternatives or all nests underneath, no mixture
nestList=[ # UI name, nestID,coeff, [alts], [nests]
          ["root",      0, 1.0, [],[1, 2, 3, 4]],  # has 4 nests ( 
          ["Work Only Patterns", 1, 0.871, [0,1,2,3,4],[]], # no subnests, alternatives: "1Wk-S", "1Wk+S", "2 Wk -S", "2Wk + 1S", "2Wk + 2 St"
          ["University Patterns", 2, 0.871, [5, 6, 7],[]], # no subnests, alternatives: "1 UNI + 1Wk -S", "1UNI + 1Wk +S", "1 UNI"
          ["Non-Mandatory Travel Only", 3, 0.871, [8],[]], # no subnests, only one alternative: "NMT"
          ["Other Patterns", 4, 0.871, [9, 10],[]] # no subnests, alternatives: "SAH", "EXT"
         ]
# the nestId is really superfluous here, as it corresponds to the nest's order in the array


# TBI: updated:
# 1 Uni tour is the base alternative, thus 0 constant
# 					1WrkNoStps   1WorkStps    2WrkNoStps   2Wrk1/0Stps  2Wrk1/1Stps 1UniWrkNoStps 1UniWrkStps  1 Uni        NMTravel     # SAH      ExternalOnly
#altSpecificConsts=[ 4.52754738,  4.98923058,  1.89542644,  1.79523755,  1.37120447, -0.82258832, -0.82258832,  0.00000000,  2.80713487,  2.68232161, 3.71730930]
#altSpecificConsts=[4.057,4.72,1.5,1.633,0.924,-0.349,-2.317,0,2.97,3.769,1.923]
#altSpecificConsts=[4.038,4.674,1.423,1.548,0.820,-0.403,-2.264,0,2.963,2.771,2.968]
#altSpecificConsts=[4.011,4.657,1.434,1.543,0.801,-0.467,-2.366,0,2.964,2.657,2.955]
#altSpecificConsts=[3.98,4.626,1.404,1.509,0.765,-0.444,-2.401,0,2.937,2.614,2.913]
#altSpecificConsts=[4.311,4.956,1.7,1.812,1.081,-0.181,-2.149,0,2.977,2.658,4.109]
# JPN Calibration begins here
#altSpecificConsts=[4.492,5.14,1.887,1.988,1.237,-0.247,-2.083,0,2.962,2.647,4.114]
#altSpecificConsts=[4.535,5.182,1.932,2.028,1.269,-0.229,-2.218,0,2.965,2.646,4.105]
altSpecificConsts=[4.514,5.161,1.907,1.999,1.266,-0.227,-2.253,0,2.935,2.612,4.076]




# person sorting from preprocessor is by zone, hnhinc5s, hhid, pTypeDAP, age, personId
# for each submodel household will be new almost every time, try first in durables though
# however, it's worth an experiment to try household information in transient and durable

durableCoeffs=[
#sort tier 1 zone attributes
[ 0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000, -0.07394197],# 00 DISTTOEXT        # zone 1
[ 0.00000000,  0.00000000, -0.45554666, -0.45554666, -0.45554666, -0.45554666, -0.45554666,  0.00000000,  0.00000000,  0.00000000,  0.00000000],# 01 TRANSITACC       # zone 2
[ 0.00000000,  0.00000000,  0.00008723,  0.00008723,  0.00008723,  0.00008723,  0.00008723,  0.00000000,  0.00000000,  0.00000000,  0.00000000],# 02 HMXDENS          # zone 3
[ 0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.04512053,  0.00000000,  0.00000000],# 03 EMPACC           # zone 4
#sort tier 2 (hhinc)                                                                                                                                                  
[-0.55406691, -0.55406691, -0.55406691, -0.55406691, -0.55406691, -0.55406691, -0.55406691,  0.00000000, -0.19325492,  0.00000000,  0.00000000],# 04 INCLE50          # derived  0
[ 0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.55578901,  0.55578901,  0.55578901,  0.00000000,  0.00000000,  0.61260862],# 05 INC100           # derived  1
#sort tier 3  household related                                                                                                                                       
[ 0.00000000,  0.14561852, -0.52422370, -0.37860518, -0.37860518, -0.52422370, -0.37860518,  0.00000000,  0.00000000,  0.00000000,  0.00000000],# 06 HCHILD1          # persons  6 
[ 0.00000000, -0.17696770,  0.00000000, -0.17696770, -0.17696770,  0.00000000, -0.17696770,  0.00000000,  0.00000000,  0.00000000, -0.64301365],# 07 WORKERS          # persons 16
[ 0.34155886,  0.34155886,  0.34155886,  0.34155886,  0.34155886,  0.34155886,  0.34155886,  0.00000000,  0.23333430,  0.00000000,  0.00000000],# 08 IFEQ(HHSIZE,1)   # persons 19
[ 0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000, -0.90946967,  0.00000000,  0.00000000],# 09 IFEQ(CHILDREN,0) # persons 22
[ 0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000, -0.35820617, -0.35820617, -0.35820617,  0.00000000, -0.14267106,  0.00000000],# 10 HHVEH            # persons 27
[ 0.00000000, -0.38539999,  0.00000000, -0.38539999, -0.38539999,  0.00000000, -0.38539999,  0.00000000, -1.59252062,  0.00000000,  0.00000000],# 11 ZEROVEH          # persons 28
[ 0.00000000,  0.34648697,  0.00000000,  0.34648697,  0.34648697,  1.33035443,  1.67684139,  1.33035443,  0.00000000,  0.88946156,  0.44191724],# 12 IFGE(CHILDREN,1) # derived  2

            ]

# durableCoeffMap={
#      {"Data reference name": [
#                                   [origin index in the data reference row, 
#                                    destination index in the durable Values array , 
#                                    number of consecutive values to copy from one to the other
#                                   ]
#                               ,...(optional additional ranges to copy in the same data reference)
#                              ]
#        ,... (additional data references as needed)     
#      }
durableCoeffMap={"Zones" : [
                            [1,0,4], # "ext_dist", "tw_acc", mix_dens, TEhwyacc10
                           ],
                 "DerivedResults": [
                                    [0,4,1], #inc <= 50k
                                    [1,5,1],  # inc > 100k
                                    [2,12,1],  # hchildren >= 1
                                    ] ,

                 "Persons": [
                             [6,6,1],# hchild1
                             [16,7,1],# hworkers
                             [19,8,1],# hh1person
                             [22,9,1],# hnochildre
                             [27,10,2],# nCars, noCarsInHh
                             ] 
                 }

			
transientCoeffs=[
# 1WrkNoStps   #1WorkStps   #2WrkNoStps #2Wrk1/0Stps #2Wrk1/1Stps #1UniWrk0Stps #1UniWrkStps # 1 Uni     # NMTravel    # SAH      # ExternalOnly
# person-related, not part of sort set
[-2.19576468, -1.96785696, -2.19576468, -1.96785696, -1.96785696, -2.19576468, -1.96785696,  0.00000000,  0.00000000,  0.00000000,  0.00000000],  # 00 IFEQ(WRKZON,HHZON)                                # derived  3
[-3.53447535, -2.98157474, -3.53447535, -2.98157474, -2.98157474, -3.53447535, -2.98157474,  0.00000000,  0.00000000,  0.00000000,  0.00000000],  # 01 IFEQ(WRKZON,0)                                    # persons 26
[ 0.36410263,  0.36410263,  0.36410263,  0.36410263,  0.36410263,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000],  # 02 WPLOGSUM                                          # persons 30
[ 0.00000000, -0.35293447,  0.00000000, -0.35293447, -0.35293447,  0.00000000, -0.35293447,  0.00000000,  0.00000000,  0.00000000,  0.00000000],  # 03 MALE                                              # derived  4
[ 0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000, -1.20086441, -1.20086441, -1.20086441,  0.37167541, -0.24315371,  0.00000000],  # 04 AGEGR35                                           # derived  5
[ 0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000, -3.35744754, -3.35744754, -3.35744754,  0.00000000, -0.36002505,  0.00000000],  # 05 IFGE(CHILDREN,1)MALE                              # derived  6
#submodel result-related                                                                                                                                                                                            
[ 0.16695995,  0.16695995,  0.16695995,  0.16695995,  0.16695995,  0.16695995,  0.16695995,  0.00000000,  0.00000000,  0.00000000,  0.00000000],  # 06 IFGE(NPTWMAND+NNWAMAND+NSENMAND,1)                # derived  7
[ 0.24034961,  0.24034961,  0.24034961,  0.24034961,  0.24034961,  0.24034961,  0.24034961,  0.00000000,  0.00000000,  0.00000000,  0.00000000],  # 07 IFGE(NCH2NM+NCH3NM,1)                             # derived  8
[ 0.82022113,  0.82022113,  0.82022113,  0.82022113,  0.82022113,  0.82022113,  0.82022113,  0.00000000,  0.00000000,  0.00000000,  0.00000000],  # 08 IFGE(NCH2MAND+NCH3MAND,1)                         # derived  9
[ 1.12379959,  1.12379959,  1.12379959,  1.12379959,  1.12379959,  1.12379959,  1.12379959,  0.00000000,  0.00000000,  0.00000000,  0.00000000],  # 09 SAH_PNSIFGE(NCH2SAH+NCH3SAH,1)                    # derived 10
[ 0.00000000, -0.59353689,  0.00000000, -0.59353689, -0.59353689,  0.00000000, -0.59353689,  0.00000000,  0.00000000,  0.00000000,  0.00000000],  # 10 NAL16SAH  Number of SAH CH2                       # derived 11
[ 0.00000000, -0.24106494,  0.00000000, -0.24106494, -0.24106494,  0.00000000, -0.24106494,  0.00000000,  0.00000000,  0.00000000,  0.00000000],  # 11 NAL16NM   number of NMT ch2                       # derived 12
[ 0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  2.13163723,  0.00000000,  0.00000000],  # 12 IFGE(NCH2NM,1)                                    # derived 13
[ 0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.74493049,  0.00000000,  0.00000000],  # 13 IFGE(NCH23MAND,1)                                 # derived 14
[ 0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000, -1.58581267,  0.00000000,  0.00000000],  # 14 IFGE(NCH2NM,1)MALE                                # derived 15
[ 0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000, -0.73686529,  0.00000000,  0.00000000],  # 15 IFGE(NCH23MAND,1)MALE                             # derived 16
[ 0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  1.16130044,  0.00000000],  # 16 IFGE(NCH2SAH+NCH3SAH,1)                           # derived 17
[ 0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  1.00926579,  0.00000000],  # 17 SAH_PNS  (existence of SAH for ptw, nwa or sen)   # derived 18
[ 0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  1.52407965],  # 18 EXT_PNS   (existence of EXT for ptw, nwa or sen)  # derived 19
[ 0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  4.76796528],  # 19 IFGE(NCH2EXT+NCH3EXT,1)                           # derived 20 
                                                                                                                                                     

]

transientCoeffMap={
                    
"Persons" :         [
                    [26, 1,1], # 49 noregwkplc
                    [30, 2,1]  # 53 logsum
                    ],

"DerivedResults" :  [
                     [3,0,1],
                     [4,3,17],
                    ]
} 





