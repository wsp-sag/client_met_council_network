####################################################################
# DailyActivityPatternSubModel_Child3.py
# other notes:
# TBI: finished
####################################################################

from Globals import *

# the name of the corresponding class on the C# side:
# this allows for multiple scripts targeting the same component
modelComponentName="DAPChild3"  

from DAPMemoryDataReferences import *

# Matrices are different enough to require their own structure:
matrixReferences = [
# for now none
]


# ######################  model structure section  ##########################

# DAP Id; the order here is arbitrary but this same order needs to be followed 
# by any structures in this file that refer to alternatives, e.g. altSpecificConsts, the rows in the durableCoeffs and transientCoeffs arrays

altIntrinsicValues= [1, 2, 8, 9, 12, 13, 14, 15, 17]

# not used thus far:
# friendly descriptions of the alternatives, maybe for UI display somehow
altNames = ["1 Work Tour - No Stops", "1 Work Tour - With Stops", "1 Work Tour - No Stops & 1 School Tour",
            "1 Work Tour - With Stops and 1 School Tour", "1 School Tour", "2 School Tours", 
            "Non-mandatory Travel", "Stay at Home", "External Travel Only"] 

# this should evolve into a specification (in general) a tree structure
logitType = "MultinomialLogit"


# non-mandatory travel is the base alternative, thus 0 constant
						# 1Wk-S,    1Wk+S,    1Wk-S1SCH,   1Wk+S1SCH,    1SCH,        2SCH,          NMT,         SAH,        Ext,
#altSpecificConsts=[-0.43419156, -0.91126797, -1.22921940, -3.41598384,  0.48258752, -5.31168778,  0.00000000, -0.93851539,  0.29228685]
#altSpecificConsts=[-0.406,-0.864,-1.138,-3.336,0.436,-4.902,0,-0.694,0.618]
#altSpecificConsts=[-0.399,-0.848,-1.156,-3.380,0.399,-4.910,0,-0.512,0.632]
#altSpecificConsts=[-0.402,-0.847,-1.172,-3.419,0.384,-4.926,0,-0.476,0.642]
#altSpecificConsts=[-0.403,-0.849,-1.179,-3.401,0.379,-4.938,0,-0.472,0.643]
# JPN calibration begins here
#altSpecificConsts=[-0.383,-0.887,-1.193,-3.436,0.375,-4.925,0,-0.478,0.603]
altSpecificConsts=[-0.363,-0.925,-1.207,-3.471,0.371,-4.912,0,-0.484,0.563]


# alts 1,2,3 are corrected here as per Jason email 5/23/13;

# person sorting from preprocessor is by zone, hnhinc5s, hhid, pTypeDAP, age, personId
# for each submodel household will be new almost every time, try first in durables though
# however, it's worth an experiment to try household information in transient and durable

durableCoeffs=[

# Wrk NoStps  #Work Stps   #Wrk/Sch0Stps #Wrk/SchStps # 1School	   # 2School   # NMTravel    # SAH      # ExternalOnly
#tier 1, zone-related, first sort order
[ 0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000, -0.08348653],  # (DISTTOEXT)
[ 0.00000000,  0.00000000,  0.27608133,  0.27608133,  0.27608133,  0.27608133,  0.00000000,  0.00000000,  0.00000000],  # (TRANSITACC)
#tier 2 hh income, second sort order
[ 0.00000000,  0.00000000, -0.43816761, -0.43816761, -0.43816761, -0.43816761,  0.00000000,  0.00000000,  0.00000000],  # (INCLE50)
[ 0.00000000,  0.00000000,  0.41259793,  0.41259793,  0.41259793,  0.41259793,  0.00000000,  0.00000000,  0.00000000],  # (INC100)
#tier 3 hh related, third sort order (but less relevant because submodels will probably run only 1-2x per household)
# do speed experiments to see whether it's faster to have these in transients 
[-0.30904528, -0.30904528, -0.30904528, -0.30904528,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000],  # (HHSIZE) 4    
[-1.74383855, -1.74383855, -1.74383855, -1.74383855,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000],  # (HSEN)   13
[ 0.00000000,  0.00000000,  0.26062023,  0.26062023,  0.26062023,  0.77345008,  0.00000000,  0.00000000,  0.00000000],  # (CHILDREN) 15
[ 0.29882351,  0.29882351,  0.29882351,  0.29882351,  0.00000000,  0.74304695,  0.00000000,  0.00000000,  0.00000000],  # (HHVEH)   27
[ 0.00000000,  0.00000000,  2.91230705,  2.91230705,  2.91230705,  2.91230705,  0.00000000,  2.20966281,  0.00000000],  # (ZEROVEH)  28
]

# durableCoeffMap={"table name": [[tableColIndex, matchingCoeffVectorStartIndex, numberOfConsecutiveColumnsToMatch],...]}
durableCoeffMap={
     "Zones" : [
                [1,0,2], # dist to ext,TRANSITACC							
               ],
     "DerivedResults" : [
                     [0, 2,2] #incLt50, inc > 100,
                   ],
     "Persons" : [
              [5, 4,1], #
              [13, 5,1], #
              [15, 6,1], #
              [27, 7,2], #
            ],                 
}



transientCoeffs=[
#   1Wk,         1Wk+S,     1Wk+SCH,      1Wk+SCH+S,    1SCH,        2SCH,        NMT,        SAH,       Ext
# Wrk NoStps  #Work Stps   #Wrk/Sch0Stps #Wrk/SchStps # 1School	   # 2School   # NMTravel    # SAH      # ExternalOnly
#tier 4 not included in sort criteria
[ 0.00000000,  0.00000000, -2.20997009, -2.20997009, -2.20997009, -2.20997009,  0.00000000,  2.00000000,  0.00000000],  # (IFGE(NCH2SAH,1))
[ 0.00000000,  0.00000000, -2.40266390, -2.40266390, -2.40266390, -2.40266390,  0.75645987,  0.00000000,  0.00000000],  # (IFGE(NCH2NM,1))
[ 0.00000000,  0.00000000,  1.42756589,  1.42756589,  1.42756589,  1.42756589,  0.00000000,  0.00000000,  0.00000000],  # (IFGE(NCH2SCH,1))
[ 0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  2.00000000],  # (IFGE(NCH2EXT,1))
[ 0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000, -1.81030841],  # (MALE)
]

transientCoeffMap={
"DerivedResults" : [
                    [2,0,5], #
                   ]
}
# no segments