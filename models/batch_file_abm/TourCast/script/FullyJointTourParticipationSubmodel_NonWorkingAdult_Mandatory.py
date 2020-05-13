####################################################################
# FullyJointTourParticipationSubmodel_NonWorkingAdult_Mandatory.py
# i.e. participation submodel for person type of Non-Working Adult with a mandatory DAP pattern
####################################################################

from Globals import *
from FullyJointTourParticipationSubmodelDataReferences import *

parameters= {
             "PersonType": "NonWorkingAdult",
             "DAPType" : "Mandatory",  # other is "Nonmandatory"
             }

# ######################  model structure section  ##########################

altSpecificConsts=[0, # base alternative
                   -1.80600  # because constants are segmented by person type, they will be in the segmentations
                   ]  

durableCoeffs=[
  # no       #yes
[ placeholder]*2, # HH Income < $50K  (segmented)
[0.00000, -0.38975]  # HHVEH # Number of Cars in HH 
]

transientCoeffs=[
[0.00000,  0.00000], # 2+ Mandatory Tours #   
[0.00000,  0.61958], # MALE #   
[0.00000,  0.00000], # (NJTNWA) # Number of Non-Working Adults assigned to Tour 
[0.00000,  0.00000], # (NJTCH2) # Number of Child 6-15 yrs assigned to Tour 
[0.00000,  0.00000], # (NJTCH3) # Number of Child 16+ yrs assigned to Tour 
[0.00000,  0.00000], # (NJTFTW+NJTPTW) # Number of Part-/Full-Time Workers assigned to Tour 
[0.00000,  0.00000], # (NJTFTW+NJTPTW) # Number of Part-/Full-Time Workers assigned to Tour 
[0.00000,  0.00000], # (1-MND_PAT)*NM_PAT # 1+ Non-Mandatory Patterns on Joint Tour, 0 Mandatory Patterns 
[0.00000, -0.58377], # MND_PAT*(1-NM_PAT) # 0 Non-Mandatory Patterns on Joint Tour, 1+ Mandatory Patterns 
[0.00000,  5.94954], # JTSZRATIO # Joint Tour Size Ratio 
[0.00000,  0.14964], # LOG(1+MXWNREMAIN) # Log (1 + Max Time Window Remaining if Participating) 
[0.00000,  0.00000], # LOG(1+CHNGMAXWIN) # Log (1 + Reduction in Max Time Window Remaining if Participating) 
[0.00000,  0.44152], # NOADT_PAR # Presence of Children 6-15 & 16+ years  assigned to Tour & No Adults assigned to Tour 
[0.00000, -0.75923], # NOADT_PAR*(ADTS_PPL-1) # Number of Remaining Adult Candidates, IF Presence of Children 6-15 & 16+ years  assigned to Tour & No Adults assigned to Tour 
[0.00000, -0.28935] # ADT_PAR # No Children 6-15 & 16+ years  assigned to Tour & Adults assigned to Tour 
]

segmentCoeffMap = [
{'Segment': 0, 'Vector': 'durable', 'Offset': 0,  #  pure hh income segmentation (no other variable dependency)
  'Coefficients':
    [ 
		[ 0.000000, 0.000000, 0.000000, 0.000000, 0.000000], # no participation
		[ 0.000000, 0.000000, 0.000000, 0.000000, 0.000000]  # yes participation

    ]
}

]