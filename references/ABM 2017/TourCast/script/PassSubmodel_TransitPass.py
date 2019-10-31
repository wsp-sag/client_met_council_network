####################################################################
# PassSubmodel_TransitPass.py
# i.e. household MnPass generation submodel
####################################################################

from Globals import *
from PassSubmodelDataReferences import *

modelComponentName="PassSubmodel"  

# 'binary'
logitType = "MultinomialLogit"

# ######################  model structure section  ##########################
# base is no pass
altNames = ["no pass", "Transit pass"]
altIntrinsicValues= [0,1] 

altSpecificConsts=[0, # no pass
                   #-8.32742559  # transit pass
				   #-8.478
				   #-8.488
				   #-8.945
				   -9.400
				   
				   #-8.520
				   #-9.314
				   #-10.225
				   #-10.968
				   #-11.426
				   #-11.8
				   #-11.819
                  ]  


# durables are zone-related here				  
durableCoeffs=[
  # no       #yes
[0.00000000, 0.45720423], # Home TAZ employment highway access index (TEhwyacc10)
[0.00000000, 0.09656469], # Home TAZ employment transit access index (TETRacc15)
#[0.00000000, 0.37731153]  # suburb2 (term == 2)
#[0.00000000, 0.2]  # suburb2 (term == 2)
#[0.00000000, 0.254]  # suburb2 (term == 2)
[0.00000000, 0.300]  # suburb2 (term == 2)
]

durableCoeffMap={ 
#[dataRefIndex, durableArrayIndex, number of consecutive values to map]
       "Zones" : [
			[1, 0, 2], # TeHwyAcc10, TeTrAcc15
			[5, 2, 1] # suburb2
	   ]
}


transientCoeffs=[
            [0.00000000, -0.12157926], #  0  hhChild23  (computedValues)
            [0.00000000, -0.59935331], #  1  nCarsGt1    (computedValues)
            [0.00000000, 0.22017580], #  2  inc75To100 (computedValues)
            [0.00000000, 1.71903285], #  3  noCarsInHh  (computedValues)
            [0.00000000, 1.89105356], #  4  nWkplcCBD  (number of persons in hh with workplaces in CBD) (derivedValues)
            [0.00000000, 0.14146806], #  5  hChild1  householdBase
            [0.00000000, 1.53555199], #  6  hStud (adult students)
            [0.00000000, 0.66941267], #  7  hFtw (full time workers)
            [0.00000000, 0.91100894], #  8  hPtw (full time workers)
]

transientCoeffMap={
     "ComputedValues" : 
	 [
		#[srcIndex, destIndex, count]
		[0,0,4] #hhChild23, nCarsGt1, inc75To100, noCarsInHh
     ],
     "DerivedValues" : 
	 [
		[0,4,1] #nWpInCBD
     ],
     "HouseholdBaseData" : 
	 [
		[3,5,1], #hchild1
		[6,6,3], #hchild1
     ],
	 
     
}


#no segmentation for transit pass submodel
segmentDefinitions = []
segmentCoeffMap = []
