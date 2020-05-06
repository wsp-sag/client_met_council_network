####################################################################
# DailyActivityPatternSubModel_NonWorkingAdult.py
# TBI version
####################################################################

from Globals import *

# the name of the corresponding class on the C# side:
# this allows for multiple scripts targeting the same component
modelComponentName="DAPNonWorkingAdult"  

from DAPMemoryDataReferences import *

# Matrices are different enough to require their own structure:
matrixReferences = [
# for now none
]


# ######################  model structure section  ##########################

# DAP Ids for     1sch,2sch,NMT,SAH,Ext
altIntrinsicValues= [1, 2, 10, 14, 15, 17]

# not used thus far:
# friendly descriptions of the alternatives, maybe for UI display somehow
altNames = ["1 Work Tour No Stops","1 Work Tour 1+ Stops", "1 University Tour", "Non-mandatory Travel", "Stay at Home",  "External Travel Only"] 

# this should evolve into a specification (in general) a tree structure
logitType = "MultinomialLogit"


# non-mandatory travel is the base alternative, thus 0 constant
# Wrk NoStps # Work Stps # 1 Uni     # NMTravel  # SAH       # ExternalOnly
#altSpecificConsts=[-2.24322037, -1.79383572, -5.38637579,  0.00000000,  0.42951885,  0.34303723] # constants
#altSpecificConsts=[-2.62,-1.894,-5.489,0,0.221,-0.019]
#altSpecificConsts=[-2.618,-1.894,-5.51,0,0.245,-0.048]
#altSpecificConsts=[-2.619,-1.895,-5.49,0,0.248,-0.05]
# JPN Calibration begins here
#altSpecificConsts=[-2.556,-1.833,-5.698,0,0.363,-0.094]
#altSpecificConsts=[-2.493,-1.771,-5.906,0,0.478,-0.138]
altSpecificConsts=[-2.617,-1.896,-5.406,0,0.262,-0.06]





durableCoeffs=[
# Wrk NoStps # Work Stps # 1 Uni     # NMTravel  # SAH       # ExternalOnly
#sort tier 1 zone attributes
[ 0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000, -0.09598764],  # 00 (DISTTOEXT)         # zones 1
[ 0.00000000,  0.00000000,  1.40278054,  0.00000000, -0.25958254,  0.00000000],  # 01 (TRANSITACC)        # zones 2
#sort tier 2 (hhinc)                                                                                    
[-0.57153970, -0.57153970,  0.00000000, -0.22616023,  0.00000000,  0.00000000],  # 02 (INCLE50)           # derived 0
[ 0.70464677,  0.70464677,  0.00000000,  0.37642987,  0.00000000,  0.00000000],  # 03 (INC100)            # derived 1
#sort tier 3  household related                                                                                                                                  
[ 0.00000000,  0.00000000,  0.00000000,  0.00000000, -0.82681141, -1.62608713],  # 04 (IFGE(CHILDREN,1))  # derived 2
[-0.47829460, -0.47829460,  0.00000000,  0.00000000,  0.00000000,  0.00000000],  # 05 (HCHILD1)           # persons 06 
[ 0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.44854875,  0.00000000],  # 06 (HSTUD)             # persons 09
[ 0.00000000, -0.13830123,  0.00000000,  0.00000000,  0.00000000,  0.00000000],  # 07 (CHILDREN)          # persons 15
[ 0.00000000,  0.00000000,  0.00000000,  0.57550887,  0.00000000,  0.00000000],  # 08 (IFEQ(CHILDREN,0))  # persons 22
[ 0.20776183,  0.20776183,  0.00000000,  0.00000000,  0.10931832,  0.00000000],  # 09 (HHVEH)             # persons 27

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
                            [1,0,2], #ext_dist, tw_acc
                           ],
                 "DerivedResults" : [
                                     [0,2,3] #(INCLE50)         
                                             #(INC100)          
                                             #(IFGE(CHILDREN,1))                  
                                     ],      
                 "Persons" : [
                                 [6,5,1], #  (HCHILD1)         
                                 [9,6,1], #  (HSTUD)           
                                 [15,7,1],#  (CHILDREN)        
                                 [22,8,1], #  (IFEQ(CHILDREN,0))
                                 [27,9,1] #  (HHVEH)           
                             ],


                 }


transientCoeffs=[
# person-related, not part of sort set
[ 1.00673996,  0.41565701,  0.00000000,  0.00000000,  0.00000000,  0.00000000],  # 00 (MALE)                  # derived 3
[ 0.00000000,  0.23779419,  0.00000000,  0.63985794,  0.00000000,  0.00000000],  # 01 (AGEGR35)               # derived 4
# submodel result-related                                                                                                                                                                                                                                                        
[-0.74301953, -0.74301953,  0.00000000,  0.44702940,  0.00000000,  0.00000000],  # 02 (IFGE(NCH2NM+NCH3NM,1)) # derived 5
[ 0.00000000,  0.00000000,  0.00000000,  0.82320389,  0.00000000,  0.00000000],  # 03 (IFGE(NCH23MAND,1))     # derived 6
[ 0.00000000,  0.00000000,  0.00000000,  0.00000000, -0.11272615,  0.00000000],  # 04 (MALEIFGE(CHILDREN,1))  # derived 7
[ 0.00000000,  0.00000000,  0.00000000,  0.00000000,  1.18857467,  0.00000000],  # 05 (IFGE(NCH2SAH,1))       # derived 8
]


transientCoeffMap={
"DerivedResults" : [[3, 0, 6]]

} 
                   

