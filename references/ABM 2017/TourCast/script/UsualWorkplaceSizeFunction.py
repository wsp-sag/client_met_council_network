####################################################################
# UsualWorkplaceSizeFunction.py
# this file is imported by  UsualWorkplaceLocationChoiceModel.py
# For size functions we use 1-D notation for coeff arrays because 
# the coefficients are the same for every alternative(i.e. every location).
# However for the coefficient maps we're holding on to the 2-D notation 
# but only using one row
####################################################################

from Globals import * # for numberOfZones

# all size function coeffs are segmented by ptype
sizeFunction= {

   "lsm" : 1.0,
   "useExpCoeffs" : False,
   "locationStart" : 1,
   "locationEnd" : numberOfZones, 
   # one set of coeffs for all alternatives in this model component;    
   "durableCoeffs" : [placeholder, placeholder], # all segmented by worker type/income segment composite value
   # 0 non-retail employment as NREMP
   # 1 retail Employment as RETEMP


   "transientCoeffs" : [] #only non-zone data is segmentation
}


# coefficient maps will not be part of sizeFunction itself, but handled inside the modelcomponent code
   # same format as for alternative coeff maps:
   # input column start index, durable coeff start index, number of data fields 

sizeFunctionDurableCoeffMap = { "Zones": [[1, 0, 2]] }
sizeFunctionTransientCoeffMap = { }


sizeFunctionSegmentDefinitions = [
#  friendly name     , input data ref, offset in input, range of values (order relates to coeff order in segmentCoeffMap)

# first time I'm doing a composite segmentation:
# code constructs this and sets the workerXIncomeSegmentForSizeFn value in DerivedValues
# takes 10 * ptype (thus 50 = ftw, 60 = ptw, 80 = sen) 
# and adds income segment derived from hhinc5s (where <40 = 1, 40> 100 = 2, >100 = 3)
# thus e.g. 51 means ftw with income < 40k;  63 means ptw with income > 100k
 {'Name': 'worker-Income Segment', 'DataRef': 'DerivedValues','Offset': 0, 'DataRange': [50,51,52,53,54,60,61,62,63,64]}
]

# segmentation in this case only applies to the durable (location) coefficients

sizeFunctionSegmentCoeffMap = [
{'Segment': 0, 'Vector': 'durable', 'Offset': 0,  # NREMP
  'Coefficients':
    [ 
        #keep same format here as for the alternative-related segmentation
        #even though we'll always have only one row of coeffs 
        #ftw                  							ptw               
        #<25k,   	25-50K,    	50-75k     	75k-100K   	>100k		<25k,   	25-50K,    	50-75k     	75k-100K   	>100k     	  income
        [1.0000, 	1.0000, 	1.0000, 	1.0000, 	1.0000, 	1.0000, 	1.0000, 	1.0000, 	1.0000, 	1.0000]
    ]
},
{'Segment': 0, 'Vector': 'durable', 'Offset': 1,  # RETEMP
  'Coefficients':
    [ 
        [3.02072524,0.80314359,0.80314359,0.30985015, 0.30985015, 6.03972681, 2.73945607, 2.44339456, 2.44339456, 2.44339456]
    ]
}
]