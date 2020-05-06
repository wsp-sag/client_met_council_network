####################################################################
# FullyJointTourParticipationSubmodel_Child2_NonMandatory.py
# i.e. participation submodel for person type of Child2 with a Non-Mandatory DAP pattern
####################################################################

from Globals import *
from FullyJointTourParticipationSubmodelDataReferences import *

parameters= {
             "PersonType": "Child1",
             "DAPType" : "Nonmandatory",  # other is "Mandatory"
             }


# ######################  model structure section  ##########################

# DAP Id, 
altIntrinsicValues= [0,1] 

# not used thus far:
# friendly descriptions of the alternatives, maybe for UI display somehow
altNames = ["Does not participate", "Particpates"]  #

# 'binary'
logitType = "MultinomialLogit"

#Sorry about the length
altSpecificConsts=[0, # base alternative
                   -1.12637  # because constants are segmented by person type, they will be in the segmentations
                   ]  

durableCoeffs=[
  # no       #yes
[ placeholder]*2, # HH Income < $50K  (segmented)
[0.00000,  0.00000] # HHVEH # Number of Cars in HH 
]

transientCoeffs=[
[0.00000, -0.68689], # 2+ Mandatory Tours #   
[0.00000,  0.00000], # MALE #   
[0.00000,  0.67832], # (NJTNWA) # Number of Non-Working Adults assigned to Tour 
[0.00000,  1.20335], # (NJTCH2) # Number of Child 6-15 yrs assigned to Tour 
[0.00000,  0.00000], # (NJTCH3) # Number of Child 16+ yrs assigned to Tour 
[0.00000,  0.00000], # (NJTFTW+NJTPTW) # Number of Part-/Full-Time Workers assigned to Tour 
[0.00000,  0.00000], # (NJTFTW+NJTPTW) # Number of Part-/Full-Time Workers assigned to Tour 
[0.00000,  0.00000], # (1-MND_PAT)*NM_PAT # 1+ Non-Mandatory Patterns on Joint Tour, 0 Mandatory Patterns 
[0.00000,  0.00000], # MND_PAT*(1-NM_PAT) # 0 Non-Mandatory Patterns on Joint Tour, 1+ Mandatory Patterns 
[0.00000,  4.87472], # JTSZRATIO # Joint Tour Size Ratio 
[0.00000,  0.18667], # LOG(1+MXWNREMAIN) # Log (1 + Max Time Window Remaining if Participating) 
[0.00000,  0.00000], # LOG(1+CHNGMAXWIN) # Log (1 + Reduction in Max Time Window Remaining if Participating) 
[0.00000,  0.00000], # NOADT_PAR # Presence of Children 6-15 & 16+ years  assigned to Tour & No Adults assigned to Tour 
[0.00000,  0.00000], # NOADT_PAR*(ADTS_PPL-1) # Number of Remaining Adult Candidates, IF Presence of Children 6-15 & 16+ years  assigned to Tour & No Adults assigned to Tour 
[0.00000,  0.00000]  # ADT_PAR # No Children 6-15 & 16+ years  assigned to Tour & Adults assigned to Tour 

]
                   
segmentCoeffMap = [
{'Segment': 0, 'Vector': 'durable', 'Offset': 0,  #  pure hh income segmentation (no other variable dependency)
  'Coefficients':
    [ 
		[ 0.000000, 0.000000, 0.000000, 0.000000, 0.000000], # no participation
		[-0.818852,-0.818852, 0.000000, 0.000000, 0.000000]  # yes participation

    ]
}

]