####################################################################
# PassSubmodel_MnPass.py
# i.e. household MnPass generation submodel
####################################################################

from Globals import *
from PassSubmodelDataReferences import *

modelComponentName="PassSubmodel_MnPass"  

# 'binary'
logitType = "MultinomialLogit"

# ######################  model structure section  ##########################
# base is no pass
altNames = ["no pass", "Mn pass"]
altIntrinsicValues= [0,1] 

altSpecificConsts=[0, # base alternative
                   #-8.38503029  # because constants are segmented by person type, they will be in the segmentations
				   #-8.772
				   #-8.714
				   #-8.764
				   #-8.713
				   -9.070
				   
				   #-5.94
				   #-5.836
                  ]  


# durables are zone-related here				  
durableCoeffs=[
  # no       #yes
[0.00000000, 0.27692206], # Home TAZ employment highway access index (TEhwyacc10)
[0.00000000, -0.30669352], # Home TAZ employment transit access index (TETRacc15)
[0.00000000, 0.34878925],  # Home TAZ employment MnPass access index (MEhwyacc10)
#[0.00000000, 0.73733584]  # suburb3 (term == 3)
#[0.00000000, 0.167]  # suburb3 (term == 3)
#[0.00000000, 0.091]  # suburb3 (term == 3)
#[0.00000000, 0.159]  # suburb3 (term == 3)
[0.00000000, 0.089]  # suburb3 (term == 3)
]

durableCoeffMap={ 
#[dataRefIndex, durableArrayIndex, number of consecutive values to map]
       "Zones" : [
			[1, 0, 4] # TeHwyAcc10, TeTrAcc15, MeHwyAcc10, suburb3
	   ]
}


transientCoeffs=[
            [placeholder]*2, #  0  hh income segment (mapped to dummy constant)
            [0.00000000, -0.28396352], #  1  nCarsGt1
            [0.00000000, 0.19078540], #  2  nWkplcCBD  (number of persons in hh with workplaces in CBD)
            [0.00000000, -0.12421783], #  3  xWkplcSub  (household has usual workplaces in suburbs)
            [0.00000000, 0.20671718], #  4  hWorkers (number of household workers)
]

transientCoeffMap={
    
     "Constants" : 
	 [ #[dataref, targetindex, n]
		[0,0,1],
	 ],
     "ComputedValues" : 
	 [
		[1,1,1] #hhCarsGt1
     ],
     "DerivedValues" : 
	 [
		[0,2,2] #nWpInCBD, xWpInSub
     ],
     "HouseholdBaseData" : 
	 [
		[9,4,1] #hWorkers
     ],
	 
     
}


#only this submodel uses segmentation 
segmentDefinitions = [
 {'Name': 'Household income', #  friendly name
  'DataRef': 'HouseholdBaseData', # input data reference name
  'Offset': 1,  # zero-based column ordinal within input reference
  'DataRange': [0,1,2,3,4]} # enumerated possible values (order relates to coeff order in segmentCoeffMap)
]

segmentCoeffMap = [
   {'Segment': 0,  # index into segmentDefinitions 
   'Vector': 'transient', # which coefficient array is affected
   'Offset': 0,  #  offset in coefficient array 
     'Coefficients':
       [ 
           [0, 0, 0, 0, 0], # no mnPass
           [0, 0, 0.92166194, 1.78579866, 2.43660267] # yes mnPass
       ]
   }
]