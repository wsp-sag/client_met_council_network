####################################################################
# DailyActivityPatternSubModel_PartTimeWorker.py
# other notes:
#   I am not adhering to the python convention of 70-odd columns per line
####################################################################

from Globals import *

# the name of the corresponding class on the C# side:
# this allows for multiple scripts targeting the same component
modelComponentName="DAPPartTimeWorker"  

from DAPMemoryDataReferences import *

# Matrices are different enough to require their own structure:
matrixReferences = [
# for now none
]


# ######################  model structure section  ##########################

logitType = "MultinomialLogit"


# friendly descriptions of the alternatives, maybe for UI display somehow
altNames = ["1WrkNoStps", "1WorkStps", "2WrkNoStps", "2Wrk1/0Stps", "2Wrk1/1Stps", "1UniWrkNoStps", "1UniWrkStps", "1 Uni", "NMTravel", "SAH", "ExternalOnly"]

# DAP Ids for     ************************
altIntrinsicValues= [1, 2, 3, 4, 5, 6, 7, 10, 14, 15, 17]

# non-mandatory travel is the base alternative, thus 0 constant
#                  # 1WrkNoStps  # 1WorkStps  #2WrkNoStps  #2Wrk1/0Stps #2Wrk1/1Stps #1UniWrkNoStps #1UniWrkStps #1 Uni      # NMTravel  # SAH       #ExternalOnly
#altSpecificConsts=[ 0.27780119, -0.14925920, -3.00791349, -3.69473407, -4.42310910, -0.28539492, -0.28539492, -0.28539492,  0.00000000, -0.52026195, -0.19878658]
#altSpecificConsts=[0.377,0.11,-3.104,-3.642,-4.099,-2.202,-4.402,0,0.357,-0.178,0.16]
#altSpecificConsts=[0.549,0.317,-2.947,-3.451,-3.948,-2.231,-4.513,0,0.582,0.062,0.479]
#altSpecificConsts=[0.570,0.340,-2.911,-3.425,-3.943,-2.239,-4.506,0,0.607,0.094,0.524]
#altSpecificConsts=[0.57,0.34,-2.918,-3.423,-3.943,-1.003,-1.003,-1.003,0,0.094,0.527]
#altSpecificConsts=[0.57,0.34,-2.925,-3.421,-3.943,-0.148,-0.148,-0.148,0,0.094,0.53]
#altSpecificConsts=[0.044,-0.217,-3.434,-3.991,-4.469,-0.746,-0.746,-0.746,0,-0.405,-0.087]
#altSpecificConsts=[0.522,0.299,-2.979,-3.461,-3.978,-1.356,-1.356,1.124,0,0.029,0.502]
#altSpecificConsts=[0.085,-0.134,-3.409,-3.898,-4.364,-3.158,-3.158,-0.558,0,-0.527,0.187]
# JPN calibration begins here
#altSpecificConsts=[0.257,0.038,-3.216,-3.693,-4.201,-3.058,-3.058,-0.536,0,-0.446,0.303]
#altSpecificConsts=[0.185,-0.032,-3.28,-3.801,-4.284,-3.177,-3.177,-0.6,0,-0.524,0.2]
altSpecificConsts=[0.176,-0.039,-3.308,-3.777,-4.296,-3.078,-3.078,-0.543,0,-0.536,0.189]




# person sorting from preprocessor is by zone, hnhinc5s, hhid, pTypeDAP, age, personId
# for each submodel household will be new almost every time, try first in durables though
durableCoeffs=[

# 1WrkNoStps  #1WorkStps   #2WrkNoStps  #2Wrk1/0Stps #2Wrk1/1Stps #1UniWrkNoStps #1UniWrkStps # 1 Uni     # NMTravel   # SAH       #ExternalOnly
#sort tier 1 zone attributes
[ 0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000, -0.10667755],  # 00 (DISTTOEXT)        # zones 1
[ 0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.29012319,  0.00000000,  0.00000000],  # 01 (TRANSITACC)       # zones 2
#sort tier 2 (hhinc)                                                                                                                                                   
[ 0.23049535,  0.23049535,  0.23049535,  0.23049535,  0.23049535,  0.23049535,  0.23049535,  0.40416366, -0.17512471,  0.00000000, -0.30204407],  # 02 (INCLE50)          # derived 0
[ 0.18557296,  0.18557296,  0.18557296,  0.18557296,  0.18557296, -0.17477039, -0.17477039, -0.36034335,  0.00000000,  0.00000000,  0.60992107],  # 03 (INC100)           # derived 1
#sort tier 3  household related                                                                                                                                        
[ 0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.74317228,  0.74317228,  0.74317228,  0.00000000,  0.48838447,  0.00000000],  # 04 (IFGE(CHILDREN,1)) # derived 2
[ 0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000, -0.06024356],  # 05 (HHSIZE)           # persons 05
[-0.41670353, -0.41670353, -0.41670353, -0.41670353, -0.41670353, -0.41670353, -0.41670353, -0.41670353,  0.00000000,  0.00000000,  0.00000000],  # 06 (HCHILD1)          # persons 06
[-0.45170326, -0.45170326, -0.45170326, -0.45170326, -0.45170326, -0.45170326, -0.45170326, -0.45170326,  0.00000000,  0.00000000,  0.00000000],  # 07 (HSTUD)            # persons 09
[-0.20123733, -0.20123733, -0.20123733, -0.20123733, -0.20123733, -0.20123733, -0.20123733,  0.00000000,  0.00000000,  0.00000000,  0.00000000],  # 08 (HFTW)             # persons 10
[ 0.33517266,  0.33517266,  0.54925223,  0.54925223,  0.54925223,  0.33517266,  0.33517266,  0.00000000,  0.27793668,  0.00000000,  0.00000000],  # 09 (CHILDREN)         # persons 15
[ 0.15925375,  0.15925375,  0.15925375,  0.15925375,  0.15925375,  0.15925375,  0.15925375,  0.00000000,  0.00000000,  0.00000000,  0.54692842],  # 10 (WORKERS)          # persons 16
[-0.38261133, -0.38261133, -0.38261133, -0.38261133, -0.38261133, -0.38261133, -0.38261133,  0.00000000,  0.00000000,  0.00000000,  0.00000000],  # 11 (IFEQ(HHSIZE,1))   # persons 19
[ 0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000, -0.16314870, -0.16314870, -0.16314870,  0.00000000,  0.00000000,  0.00000000],  # 12 (HHVEH)            # persons 27
[ 0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.37167721,  0.54779077,  0.00000000],  # 13 (ZEROVEH)          # persons 28
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
                            [1,0,2], # ext_dist, tw_acc
                           ],
                "DerivedResults" :  [
                    [0,2,3],
                    ],
                "Persons" : [
                   [ 5, 5,2], # hhsize, hchild1
                   [ 9, 7,2], # hstud, hftw
                   [15, 9,2], # children, workers
                   [19,11,1], # hh1person
                   [27,12,2], # hhveh, zeroveh
                    ]
                 }

transientCoeffs=[
# person-related
# person-level
[-2.29398149, -2.29398149, -2.29398149, -2.29398149, -2.29398149, -2.29398149, -2.29398149,  0.00000000,  0.00000000,  0.00000000,  0.00000000],  # (IFEQ(WRKZON,0))          # persons 26
[ 0.13731729,  0.13731729,  0.13731729,  0.13731729,  0.13731729,  0.13731729,  0.13731729,  0.00000000,  0.00000000,  0.00000000,  0.00000000],  # (WPLOGSUM)                # persons 30
[ 0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.53104744,  0.53104744,  0.53104744,  0.00000000,  0.00000000,  0.00000000],  # (IFGE(CHILDREN,1)MALE)    # derived  3
[-0.53052556, -0.83091936, -0.53052556, -0.83091936, -0.83091936, -0.53052556, -0.83091936,  0.00000000,  0.00000000,  0.00000000,  0.00000000],  # (IFEQ(WRKZON,HHZON))      # derived  4
[-0.56772982, -0.05737845, -0.56772982, -0.05737845, -0.05737845, -4.64479686, -4.13444549, -4.07706704,  0.00000000, -0.65281941,  0.00000000],  # (AGEGR35)                 # derived  5
[ 0.10041488, -0.27425989,  0.57711871,  0.20244394,  0.20244394,  0.10041488, -0.27425989,  0.00000000,  0.00000000,  0.00000000, -0.54980558],  # (MALE)                    # derived  6
#submodel result-related                                                                                                                                                                                              
[ 0.61833043,  0.61833043,  0.61833043,  0.61833043,  0.61833043,  0.61833043,  0.61833043,  0.00000000,  0.00000000,  0.00000000,  0.00000000],  # (IFGE(NNWANM+NSENNM,1))   # derived  7
[-0.92418074, -0.92418074, -0.92418074, -0.92418074, -0.92418074, -0.92418074, -0.92418074, -0.92418074,  0.00000000,  0.00000000,  0.00000000],  # (IFGE(NSENNM,1))          # derived  8
[ 0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  1.20129525,  0.00000000,  0.00000000],  # (IFGE(NCH2NM,1))          # derived  9
[ 0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.64068109,  0.00000000,  0.00000000],  # (IFGE(NCH3NM,1))          # derived 10 
[ 0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.57213662,  0.00000000,  0.00000000],  # (NM_PNS)                  # derived 11
[ 0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  2.56341377,  0.00000000],  # (IFGE(NAL16SAH,1))        # derived 12
[ 0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  1.98730919,  0.00000000],  # (IFGE(NCH3SAH,1))         # derived 13 
[ 0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  1.07575078,  0.00000000],  # (SAH_PNS)                 # derived 14 
[ 0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.82985295],  # (IFGE(NCH2EXT+NCH3EXT,1)) # derived 15 
[ 0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  2.49035109],  # (EXT_PNS)                 # derived 16 
    ]

transientCoeffMap={
                    
"Persons" :         [
                   [26,0,1],  # noregwkplc
                   [30,1,1], # logsum


                    ],

"DerivedResults" :  [
                    [3,2,14],
                    ]
}
                   
# no segment maps
