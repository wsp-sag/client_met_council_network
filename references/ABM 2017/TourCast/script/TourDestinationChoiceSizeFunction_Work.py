####################################################################
# TourDestinationChoiceSizeFunction_Work.py
# size functions are different for the different tour purposes:
# include this file in TourDestinationChoiceWork.py
####################################################################

from Globals import * # for numberOfZones

# note no segmentation for this size function
sizeFunction= {

   "lsm" : 1.0,
   "locationStart" : 1,
   "locationEnd" : numberOfZones, 
   # one set of coeffs for all alternatives in this model component;
   # Entirely segmented (hence 0's)
   "durableCoeffs" : [
	 0.00000000, # HHTOTAL #  
	 placeholder, # Retail Employment, segmented worker type/income
	 placeholder, # Non-Retail Employment, segmented worker type/income
    ] ,

   "transientCoeffs" : [] #no individual-dependent data
}

# coefficient maps will not be part of sizeFunction itself, but handled inside the modelcomponent code
   # same format as for alternative coeff maps:
   # input column start index, durable coeff start index, number of data fields 

sizeFunctionDurableCoeffMap = { "Zones": [
	[1, 0, 3], # households, ret_emp, nret_emp
] }
sizeFunctionTransientCoeffMap = { }

# both segmentations require some manipulation of the inputs,so come from the DerivedValuesForSizeFn data reference
# 1) worker type/ income:
# 	only interested in 2 income segments, < 75, >=75;  income segment value = 0 for < 75k, 10 for >= 75 k
# 	worker type values: FT=1, PT=2, other=3, so value range is 1,2,3, 11, 12, 13
# 2) worker type segment, FT=1, PT=2, other =3; 
sizeFunctionSegmentDefinitions = [
 {'Name': ' Worker type/Income Segment', 'DataRef': 'DerivedValuesForSizeFn','Offset': 0, 'DataRange': [1,2,3, 11, 12, 13]},
]

sizeFunctionSegmentCoeffMap = [
#																	 FT lo      PT lo         NW low       FT hi	     PT hi        NW hi
{'Segment': 0, 'Vector': 'durable', 'Offset': 1, 'Coefficients':[[ 0.56643946,  0.75237035,  2.00593165, -0.35605436 , 0.75237035,  2.00593165 ]]},      # Retail Employment
{'Segment': 0, 'Vector': 'durable', 'Offset': 2, 'Coefficients':[[ 0.26201870, -0.21567442,  0.50554175,  0.36938506 ,-0.21567442,  0.50554175 ]]},      # non-Retail Employment

]
