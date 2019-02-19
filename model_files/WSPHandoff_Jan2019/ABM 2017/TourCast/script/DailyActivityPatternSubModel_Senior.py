####################################################################
# DailyActivityPatternSubModel_Senior.py


# other notes:
#   I am not adhering to the python convention of 70-odd columns per line
####################################################################

from Globals import *

# the name of the corresponding class on the C# side:
# this allows for multiple scripts targeting the same component
modelComponentName="DAPSenior"  

from DAPMemoryDataReferences import *

# Matrices are different enough to require their own structure:
matrixReferences = [
# for now none
]


# ######################  model structure section  ##########################

# DAP Ids for     ************************
altIntrinsicValues= [1, 2, 10, 14, 15, 17]


# not used thus far:
# friendly descriptions of the alternatives, maybe for UI display somehow
altNames = ["1Wk-S", "1Wk+S", "2 Wk -S", "2Wk + 1S", "2Wk + 2 St", "1 UNI", "NMT", "SAH", "OOA", "ETO"]

# this should evolve into a specification (in general) a tree structure
logitType = "NestedLogit"

# nest structure ##RETURN
#   [UI name, nestID, nest coeff, [alts], [nests]]
# where [alts] refers to alternatives by its order in any of the altIntrinsicValues/altNames/durableCoeffs/transientCoeffs lists
# and [nests] is a list of nestIDs
# any subnest must have nest coeff(aka theta) less than the level above
# nests have either all alternatives or all nests underneath, no mixture
nestList=[ # UI name, nestID,coeff, [alts], [nests]
          ["root",      0, 1.0, [],[1, 2]],  # has 2 nests underneath, no alts(NMT, offset 2)
          ["Travel Patterns", 1, 0.5407, [0,1,2,3,4,5,6],[]], # no subnests, alternatives: "1Wk-S", "1Wk+S", "2 Wk -S", "2Wk + 1S", "2Wk + 2 St", "1 UNI", "NMT"
          ["Other Patterns", 2, 0.5407, [7,8,9],[]], # no subnests, only one alternative: "SAH", "OOA", "ETO"
         ]
# the nestId is really superfluous here, as it corresponds to the nest's order in the array



# non-mandatory travel is the base alternative, thus 0 constant
#                   Wrk NoStps  # Work Stps   # 1 Uni     # NMTravel    # SAH       # ExternalOnly
#altSpecificConsts=[-2.97343557, -2.28172834, -4.97191460,  0.00000000,  0.15296493,  1.24967181]
#altSpecificConsts=[-2.88,-2.223,-4.717,0,2.142,0.278]
#altSpecificConsts=[-2.820,-2.169,-4.605,0,1.394,1.504]
#altSpecificConsts=[-2.851,-2.213,-4.648,0,1.256,1.499]
#altSpecificConsts=[-2.86,-2.222,-4.637,0,1.23,1.484]
# JPN calib begins here
#altSpecificConsts=[-2.744,-2.073,-4.834,0,1.196,0.93]
#altSpecificConsts=[-2.628,-1.924,-5.031,0,1.162,0.376]
altSpecificConsts=[-2.884,-2.208,-4.746,0,1.198,1.366]




# person sorting from preprocessor is by zone, hnhinc5s, hhid, pTypeDAP, age, personId
# for each submodel household will be new almost every time, try first in durables though

durableCoeffs=[
# Wrk NoStps  # Work Stps    # 1 Uni     # NMTravel    # SAH      # ExternalOnly
# sort tier 1 zone attributes
[ 0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000, -0.11116138],  # 01 (DISTTOEXT)        # zones 1
[-0.79220753, -0.79220753,  0.00000000, -0.52877873, -0.80188141,  0.00000000],  # 00 (TRANSITACC)       # zones 2
# sort tier 2 (hhinc)                                                                                  
[-0.66708642, -0.66708642,  0.00000000, -0.37134700,  0.00000000, -0.39521602],  # 02 (INCLE50)          # derived 0
# sort tier 3  household related                                                                        
[-1.00687345, -1.00687345,  0.00000000,  0.00000000,  0.87657213, -4.62979337],  # 03 (IFGE(CHILDREN,1)) # derived 1
[ 0.00000000,  0.00000000,  0.00000000,  0.00000000, -0.62647095,  0.00000000],  # 04 (HHSIZE)           # persons 05
[ 0.00000000,  0.00000000,  0.00000000,  0.00000000, -6.33136208,  0.00000000],  # 05 (HSTUD)            # persons 09
[ 0.00000000,  0.00000000,  0.00000000,  0.14226841,  0.66420993,  0.00000000],  # 06 (HFTW)             # persons 10
[ 0.00000000,  0.00000000,  0.00000000,  0.14226841,  0.66420993,  0.00000000],  # 07 (HPTW)             # persons 11
[ 0.00000000,  0.00000000,  0.00000000,  0.55055176,  0.58931046,  0.00000000],  # 08 (HSEN)             # persons 13
[ 0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000, -0.49212690],  # 09 (WORKERS)          # persons 16
[ 0.00000000,  0.00000000, -0.14136458, -0.03547115, -0.49864619, -0.50285399],  # 10 (HHVEH)            # persons 27
[-0.89107568, -0.89107568,  0.00000000,  0.00000000,  0.00000000,  0.00000000],  # 11 (ZEROVEH)          # persons 28
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
                            [1,0,2], # 
                           ],
                "DerivedResults" :  [[0,2,2]], #
                "Persons" : [
                     [ 5, 4,1],  # (HHSIZE)
                     [ 9, 5,3],  # (HSTUD)
                                 #  (HFTW) 
                                 #  (HPTW) 
                     [13, 8,1],  # (HSEN)   
                     [16, 9,1],  # (WORKERS)
                     [27,10,2],  # (HHVEH)  
                                 # (ZEROVEH)
                     ],

                 }

transientCoeffs=[
# Wrk NoStps  # Work Stps    # 1 Uni     # NMTravel    # SAH      # ExternalOnly
# person-related, not part of sort set
[ 0.26927175,  0.26927175,  0.00000000,  0.00000000,  0.00000000,  0.00000000],  # 0 (MALE)                            # derived 2
# submodel result-related                                                                                                                                                                                                                                                                                                                                         
[-4.83267232, -4.83267232, -4.83267232, -2.43250027,  0.00000000,  0.00000000],  # 1 (IFGE(NCH23MAND,1))               # derived 3
[ 0.00000000,  0.00000000,  0.00000000,  0.00000000, -1.58082606,  0.00000000],  # 2 (MALEIFGE(CHILDREN,1))            # derived 4
[ 0.00000000,  0.00000000,  0.00000000,  0.00000000,  1.00508997,  0.00000000],  # 3 (IFGE(NCH2SAH+NCH3SAH,1))         # derived 5
[ 0.00000000,  0.00000000,  0.00000000,  0.00000000,  4.50103382,  0.00000000],  # 4 (IFGE(NNWASAH,1))                 # derived 6
[ 0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  1.62705291],  # 5 (IFGE(NCH2EXT+NCH3EXT+NNWAEXT,1)) # derived 7

]

transientCoeffMap={
"DerivedResults" :  [[2,0,6]] #
} 
                   

