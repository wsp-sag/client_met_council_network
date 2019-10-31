####################################################################
# FullyJointTourParticipationSubmodel_AdultStudent_Mandatory.py
# i.e. participation submodel for person type of Student with a mandatory DAP pattern
####################################################################

from Globals import *
from FullyJointTourParticipationSubmodelDataReferences import *

parameters= {
             "PersonType": "AdultStudent",
             "DAPType" : "Mandatory",  # other is "Nonmandatory"
             }



# ######################  model structure section  ##########################

altSpecificConsts=[0, # base alternative
                  -7.01174
                   ]  

durableCoeffs=[
  # no       #yes
[ placeholder]*2, # HH Income < $50K  (segmented)
[0.00000,  0.47691] # HHVEH # Number of Cars in HH 
]

transientCoeffs=[
[0.00000,  0.00000], # 2+ Mandatory Tours #   
[0.00000,  0.00000], # MALE #   
[0.00000,  0.00000], # (NJTNWA) # Number of Non-Working Adults assigned to Tour 
[0.00000,  0.00000], # (NJTCH2) # Number of Child 6-15 yrs assigned to Tour 
[0.00000,  0.00000], # (NJTCH3) # Number of Child 16+ yrs assigned to Tour 
[0.00000,  0.00000], # (NJTFTW+NJTPTW) # Number of Part-/Full-Time Workers assigned to Tour 
[0.00000,  0.00000], # (NJTFTW+NJTPTW) # Number of Part-/Full-Time Workers assigned to Tour 
[0.00000,  0.00000], # (1-MND_PAT)*NM_PAT # 1+ Non-Mandatory Patterns on Joint Tour, 0 Mandatory Patterns 
[0.00000,  0.00000], # MND_PAT*(1-NM_PAT) # 0 Non-Mandatory Patterns on Joint Tour, 1+ Mandatory Patterns 
[0.00000,  4.16803], # JTSZRATIO # Joint Tour Size Ratio 
[0.00000,  0.75284], # LOG(1+MXWNREMAIN) # Log (1 + Max Time Window Remaining if Participating) 
[0.00000,  0.00000], # LOG(1+CHNGMAXWIN) # Log (1 + Reduction in Max Time Window Remaining if Participating) 
[0.00000,  0.44152], # NOADT_PAR # Presence of Children 6-15 & 16+ years  assigned to Tour & No Adults assigned to Tour 
[0.00000, -0.75923], # NOADT_PAR*(ADTS_PPL-1) # Number of Remaining Adult Candidates, IF Presence of Children 6-15 & 16+ years  assigned to Tour & No Adults assigned to Tour 
[0.00000, -0.28935]  # ADT_PAR # No Children 6-15 & 16+ years  assigned to Tour & Adults assigned to Tour 
]

segmentDefinitions = [ ##Could remove entirely.  There is not segmentation for these.
#  friendly name     , input data ref, offset in input, range of values (order relates to coeff order in segmentCoeffMap)
# compound segmentation for 8 person types x 2 dap patterns, where nonMand pattern = 1, mand pattern = 2
 {'Name': 'Household income ', 'DataRef': 'HouseholdBaseData','Offset': 1, 'DataRange': [0,1,2,3,4]}
]

segmentCoeffMap = [
{'Segment': 0, 'Vector': 'durable', 'Offset': 0,  #  pure hh income segmentation (no other variable dependency)
  'Coefficients':
    [ 
        [0, 0, 0, 0, 0], # no participation
        [0, 0, 0, 0, 0], # yes participation

    ]
}

]