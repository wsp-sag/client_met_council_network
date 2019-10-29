####################################################################
# DailyActivityPatternSubModel_Child2.py
# other notes:
#  differences for TBI:
# not nested model
# not segmented by income
####################################################################

from Globals import *

# the name of the corresponding class on the C# side:
# this allows for multiple scripts targeting the same component
modelComponentName="DAPChild2"  

from DAPMemoryDataReferences import *

# Matrices are different enough to require their own structure:
matrixReferences = [
# for now none
]


# ######################  model structure section  ##########################

# DAP Ids for     1sch,2sch,NMT,SAH,Ext
altIntrinsicValues= [12,13,14,15,17]#  

# friendly descriptions of the alternatives
altNames = ["1 School Tour","2 School Tours", "Non-mandatory Travel", "Stay at Home", "External Travel Only"] 

# this should evolve into a specification (in general) a tree structure
logitType = "MultinomialLogit"


# Ext travel is base alternative:
#                   # 1School   # 2School     # NMTravel    # SAH       # ExternalOnly
#altSpecificConsts=[ 2.22199741, -0.89934318, -0.32265922, -0.08586733,  0.00000000] 
#altSpecificConsts=[2.081, -1.041, -0.42, -0.86, 0]
#altSpecificConsts=[2.085,-1.046,-0.423,-0.901, 0]
#altSpecificConsts=[2.086,-1.047,-0.423,-0.904,0]
# JPN calibration starts here
#altSpecificConsts=[2.115,-1.008,-0.395,-0.863,0]
altSpecificConsts=[2.144,-0.969,-0.367,-0.822,0]



# person sorting will be by zone/income/household/personType
# for now, consider household attributes to be durable
# i.e. refresh durables per household,
# otherwise only have 2 durables, transitAccess and distToExt


durableCoeffs=[
# 1School	    # 2School   # NMTravel   # SAH       # ExternalOnly
# sort tier 1 zone attributes
[ 0.00000000,  0.00000000,  0.00000000,  0.00000000, -0.09995889],  # 00 (DISTTOEXT)   zones 1
[ 0.00000000,  0.00000000,  0.00000000, -0.37281293,  0.00000000],  # 01 (TRANSITACC)  zones 2
# sort tier 2 (hhinc)                                                                                  
[ 0.48459460,  0.48459460,  0.00000000,  0.92228401,  0.00000000],  # 02 (INCLE50)     derived values 0
[ 0.12767565,  0.12767565,  0.00000000,  0.00000000,  0.00000000],  # 03 (INC100)      derived values 1
# sort tier 3  household related                                                                        
[ 0.00000000,  0.00000000,  0.00000000, -0.23447797, -0.26375722],  # 04 ((HCHILD2+HCHILD3)) derived values 2
[-0.50404498, -0.50404498,  0.00000000,  0.00000000,  0.00000000],  # 05 (HHSIZE)      persons 5
[ 0.00000000,  0.00000000,  0.00000000, -0.16473970, -1.18097148],  # 06 (HCHILD1)     persons 6
[-0.20022292, -0.20022292,  0.00000000,  0.00000000,  0.00000000],  # 07 (HNWA)        persons 12
[ 0.12557361,  0.12557361,  0.00000000,  0.00000000,  0.00000000],  # 08 ((HCHILD2+HCHILD3+HCHILD1)) persons 15 (hchildren)
[ 0.00000000,  0.00000000,  0.00000000, -0.13092722,  0.00000000],  # 09 (WORKERS)     persons 16
[ 0.23704994,  0.23704994,  0.00000000,  0.00000000,  0.00000000],  # 10 (HHVEH)       persons 27
[ 0.00000000,  0.00000000,  0.00000000,  2.87939629,  0.00000000],  # 11 (ZEROVEH)     persons 28
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
durableCoeffMap={
"Zones" : [[1, 0,2] #distToExt, transitAcc
          ],
"DerivedResults" : [[0, 2,3] #incLt50, inc > 100, hChild23
                    ],
"Persons" : [[5,5,2],#  hhsize
             [12,7,1], # hnwa
             [15,8,2], # hchildren, workers
             [27,10,2], # hhVeh, zeroVeh
             ],
                 }




# transients here will be person-related attributes
transientCoeffs=[
# 1School	    # 2School   # NMTravel   # SAH       # ExternalOnly
# person-related, not part of sort set
[ 0.00000000,  0.00000000,  0.00000000,  0.21601878,  0.00000000],  # (IFEQ(AGE3,3))
]


transientCoeffMap={
"DerivedResults" : [[3, 0,1] #age cat= 3
                    ],
} 
                   
# no segmentation here
