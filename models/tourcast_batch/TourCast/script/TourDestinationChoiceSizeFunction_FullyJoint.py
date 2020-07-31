####################################################################
# TourDestinationChoiceSizeFunction_FullyJoint.py
# size functions are different for the different tour purposes:
# This file is imported into FullyJointTourDestinationChoice.py
####################################################################

from Globals import * # for numberOfZones


sizeFunction= {

   "lsm" : 1.0,
   "locationStart" : 1,
   "locationEnd" : numberOfZones, 
   # one set of coeffs for all alternatives in this model component;
   # All except total employment is segmented (hence 0's)
   "durableCoeffs" : [
					  0,  # Non-retail employment (NOT SEGMENTED, however, zero coeff (which, remember, is exponentiated)
                      placeholder,  # Retail Employment (SEGMENTED tour purpose)
                      placeholder,   # Households  (SEGMENTED tour purpose)
					  4.36900754, # area
    ] ,

   "transientCoeffs" : [] #no individual-dependent data outside of segmentations
}


# coefficient maps will not be part of sizeFunction itself, but handled inside the modelcomponent code
   # same format as for alternative coeff maps:
   # input column start index, durable coeff start index, number of data fields 

sizeFunctionDurableCoeffMap = { "Zones": [[1, 0, 4]] }
# I'll avoid using the transient coeff map so that we can cache the size function values
sizeFunctionTransientCoeffMap = { }


# simple segmentation 
# using tour purpose enum values for meal(8), shopping(16), personal business(32), social rec(64)
# fully joint tours also have the FullyJoint flag set in the TourPurpose so we have to add 256 to each value
sizeFunctionSegmentDefinitions = [
 {'Name': ' Tour Purpose', 'DataRef': 'DerivedValuesForSizeFn','Offset': 0, 
  'DataRange': [256 + 8, 
                256 + 16,
                256 + 32,
                256 + 64,
				]
 }
]

sizeFunctionSegmentCoeffMap = [
    {'Segment': 0, 'Vector': 
	 'durable', 'Offset': 1, 
      #                     meal          shop       per bus       soc rec				
	 'Coefficients':[[  3.21703615,	7.84174139,	  1.83291033,  0.54147129 ]]},  # Retail Employment
    {'Segment': 0, 'Vector': 
	 'durable', 'Offset': 2, 
      #                     meal          shop       per bus       soc rec				
	 'Coefficients':[[-0.34952005,  4.16078657,  -0.97065650,  0.54928880 ]]},  # households 
	 
]
