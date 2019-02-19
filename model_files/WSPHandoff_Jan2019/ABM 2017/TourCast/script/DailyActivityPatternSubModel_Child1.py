####################################################################
# DailyActivityPatternSubModel_Child1.py
# dummy model with one alternative (no pattern)
####################################################################

from Globals import *

# the name of the corresponding class on the C# side:
# this allows for multiple scripts targeting the same component
modelComponentName="DAPChild1"  

from DAPMemoryDataReferences import *

# Matrices are different enough to require their own structure:
matrixReferences = [
# for now none
]


# ######################  model structure section  ##########################

# DAP Ids for     no pattern
altIntrinsicValues= [0]#  

# friendly descriptions of the alternatives
altNames = ["no pattern"] 

# this should evolve into a specification (in general) a tree structure
logitType = "MultinomialLogit"


# Ext travel is base alternative:
#                   # no pattern
altSpecificConsts=[ 1] 

# person sorting will be by zone/income/household/personType
# for now, consider household attributes to be durable
# i.e. refresh durables per household,
# otherwise only have 2 durables, transitAccess and distToExt


durableCoeffs=[
# 1School	    # 2School   # NMTravel   # SAH       # ExternalOnly
# sort tier 1 zone attributes
[ 1.00000000,],  # 00 (DISTTOEXT)   zones 1
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
"Constants" : [[0, 0,1]] #
                 }




# transients here will be person-related attributes
transientCoeffs=[[1]]


transientCoeffMap={
"Constants" : [[0, 0,1]] #
                 }

                   
# no segmentation here
