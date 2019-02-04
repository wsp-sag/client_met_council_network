####################################################################
# DailyActivityPatternSubModel_AdultStudent.py
# TBI version
####################################################################

from Globals import *

# the name of the corresponding class on the C# side:
# this allows for multiple scripts targeting the same component
modelComponentName="DAPAdultStudent"  

from DAPMemoryDataReferences import *

# Matrices are different enough to require their own structure:
matrixReferences = [
# for now none
]


# ######################  model structure section  ##########################

# DAP Id; the order here is arbitrary but this same order needs to be followed 
# by any structures in this file that refer to alternatives, e.g. altSpecificConsts, the rows in the durableCoeffs and transientCoeffs arrays

altIntrinsicValues= [1, 2, 10, 11, 14, 15, 17]


# not used thus far:
# friendly descriptions of the alternatives, maybe for UI display somehow
altNames = ["Wrk NoStps", "Work Stps", "1 Uni", "2 Uni", "NMTravel", "SAH", "ExternalOnly"] 

# this should evolve into a specification (in general) a tree structure
logitType = "MultinomialLogit"

# non-mandatory travel is the base alternative, thus 0 constant
# Wrk NoStps # Work Stps     # 1 Uni       # 2 Uni    # NMTravel   # SAH       # ExternalOnly
#altSpecificConsts=[-2.23436467, -1.92399193,  2.77293101, -0.87099182,  0.00000000, -0.62965251, -2.96441611]
#altSpecificConsts=[-3.469, -2.958,2.137, -1.446, 0, -1.508, -4.588]
#altSpecificConsts=[-3.657,-3.243,1.908,-1.725,0,-2.005,-4.534]
#altSpecificConsts=[-3.777,-3.339,1.796,-1.854,0,-2.152,-4.932]
#altSpecificConsts=[-3.822,-3.387,1.747,-1.887,0,-2.227,-5.054]
# JPN Calibration begins here
#altSpecificConsts=[-3.724,-3.378,1.736,-1.95,0,-2.23,-5.181]
#altSpecificConsts=[-3.626,-3.369,1.725,-2.013,0,-2.233,-5.308]
altSpecificConsts=[-3.753,-3.426,1.71,-1.987,0,-2.251,-5.233]




# person sorting from preprocessor is by zone, hnhinc5s, hhid, pTypeDAP, age, personId
# for each submodel household will be new almost every time, try first in durables though

durableCoeffs=[
# Wrk NoStps # Work Stps     # 1 Uni       # 2 Uni    # NMTravel   # SAH       # ExternalOnly
#sort tier 1 zone attributes
[ 0.00000000,  0.00000000,  0.00000000,  0.00000000, -0.59802400,  0.00000000,  0.00000000],  # 00 TRANSITACC         # zones 2
#sort tier 2 (hhinc)                                                                             
[ 0.00000000,  0.00000000,  0.00000000,  0.00000000, -0.97591249,  0.00000000,  0.00000000],  # 01 INCLE50            # derived 0
#sort tier 3  household related                                                                                                                                        
[ 0.00000000,  0.00000000,  0.00000000,  0.00000000, -0.70544393,  0.00000000,  0.00000000],  # 02 IFGE(CHILDREN,1)   # derived 1
[ 0.00000000,  0.00000000, -1.21529444, -1.21529444,  0.00000000,  0.00000000,  0.00000000],  # 03 HSTUD              # persons 09
[ 0.00000000,  0.00000000,  1.09374101,  1.09374101,  0.00000000,  0.00000000,  0.00000000],  # 04 HSEN               # persons 13
[ 0.00000000,  0.00000000,  0.46741614,  0.46741614,  0.00000000,  0.00000000,  0.00000000],  # 05 WORKERS            # persons 16
[ 0.47552587,  0.47552587,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000],  # 06 HHVEH              # persons 27
[ 0.00000000,  0.00000000,  0.00000000,  0.00000000, -1.28229614,  0.00000000,  0.00000000],  # 07 ZEROVEH            # persons 28

]

durableCoeffMap={"Zones" : [
                            [2,0,1],  # tw_acc 
                           ],
                 "DerivedResults": [
                                    [0,1,2  ],
                                    ],
                 "Persons": [
                                    [9,3,1  ],
                                    [13,4,1  ],
                                    [16,5,1  ],
                                    [27,6,2  ],
                                    ],

                 }


# there is no data that has only non-zone-related components
transientCoeffs=[
# person-related, not part of sort set
[ 0.00000000,  0.00000000,  0.14392756,  0.14392756,  0.00000000,  0.00000000,  0.00000000],  # 00 MALE                                                     # derived 2
[ 0.00000000,  0.00000000,  0.00000000,  0.00000000,  2.57447556,  0.00000000,  0.00000000],  # 01 AGEG24()                                                 # derived 3
# submodel result-related                                                                                                                                                                                                                                                                                                                                         
[ 0.00000000,  0.00000000,  0.00000000,  0.00000000,  3.20397331,  0.00000000,  0.00000000],  # 02 IFGE(NCH2NM+NCH3NM,1)MALE                                # derived 4
[ 0.00000000,  0.00000000,  0.00000000,  0.00000000,  1.67960676,  0.00000000,  0.00000000],  # 03 IFGE(NCH2NM+NCH3NM+NFTWNM+NPTWNM+NNWANM+NSENNM,1)        # derived 5
[ 0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  4.06523243,  0.00000000],  # 04 IFGE(NCH2SAH+NCH3SAH+NPTWSAH+NNWASAH+NSENSAH+NFTWSAH,1)  # derived 6
[ 0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  6.18490269],  # 05 IFGE(NCH2EXT+NCH3EXT+NPTWEXT+NNWAEXT+NSENEXT+NFTWEXT,1)  # derived 7
]



# transientCoeffMap={"table name": [[tableColIndex, matchingCoeffVectorStartIndex, numberOfConsecutiveColumnsToMatch],...]}

transientCoeffMap={
                 "DerivedResults": [
                                    [2,0,6  ],
                                    ],

}


