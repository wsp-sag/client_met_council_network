####################################################################
# StopDestinationSizeFunction.py
# This file is imported by StopDestination.py
# For size functions we use 1-D notation for coeff arrays because 
# the coefficients are the same for every alternative(i.e. every location).
# However for the coefficient maps we're holding on to the 2-D notation 
# but only using one row
####################################################################

from Globals import * # for numberOfZones

sizeFunction= {

   "lsm" : 1.0,
   "locationStart" : 1,
   "locationEnd" : numberOfZones, 
   # one set of coeffs for all alternatives in this model component;
   # all segmented by custom segmentation 
   "durableCoeffs" : [
		placeholder,   # Retail employment segmented by stop purpose
		placeholder,   # non-Retail employment segmented by stop purpose
		placeholder,   # Retail Employment Segmented by work stop/worker type/inc lo-hi
		placeholder,   # non-Retail Employment Segmented by work stop/worker type/inc lo-hi
		0, 			   # population
		0.18926755,    # (enrolled2(1)*(uni+suni-uni*suni)) enrollment within 2 mi, uni tour or uni stop		
    ] ,

   "transientCoeffs" : [] #no individual-dependent data outside of segmentations
}


# coefficient maps will not be part of sizeFunction itself, but handled inside the modelcomponent code
   # same format as for alternative coeff maps:
   # input column start index, durable coeff start index, number of data fields 

sizeFunctionDurableCoeffMap = { "Zones": [
		[4, 0, 2],  # ret_emp, nret_emp
		[4, 2, 4],  # ret_emp, nret_emp, population, enrolled2		
		] }
sizeFunctionTransientCoeffMap = { }


# this is a compound segmentation, where the segment is calculated in the code by the combination of income,stop purpose and person type
sizeFunctionSegmentDefinitions = [
 {'Name': 'StopPurpose', 'DataRef': 'DerivedValues','Offset': 0, # 
  'DataRange': [
                1,  # School = 1,
                2,  # Work  = 2,
                4,  # University = 4,
                8,  # Meal = 8,
                16, # Shop = 16,
                32, # PersonalBusiness = 32,
                64, # SocialRecreation = 64,
                128 # Escort = 128,
                ]},
# compound segment calculation: (6 * is non-work tour) + (3* is hi inc ) + (1 * isFtw) + (2* isPtw) + (3* isNeitherFullNorPartTime) 				
 {'Name': 'Compound: Work stop/worker type/inc lo-hi', 'DataRef': 'DerivedValuesForSizeFn','Offset': 0, 
  'DataRange': [
                 1, # work stop, ftw  , lo inc
                 2, # work stop, ptw  , lo inc
                 3, # work stop, other, lo inc
                 4, # work stop, ftw  , hi inc
                 5, # work stop, ptw  , hi inc
                 6, # work stop, other, hi inc
                 7, # non-work,  ftw  , lo inc
                 8, # non-work,  ptw  , lo inc
                 9, # non-work,  other, lo inc
                10, # non-work,  ftw  , hi inc
                11, # non-work,  ptw  , hi inc
                12, # non-work,  other, hi inc
                ]},
 {'Name': 'Uni tour or stop', 'DataRef': 'DerivedValuesForSizeFn','Offset': 1, # 
  'DataRange': [
				0,  # not a uni tour or stop
                1,  # uni tour or stop
                ]},
				
]



sizeFunctionSegmentCoeffMap = [

    {'Segment': 0, 'Vector': 'durable', 'Offset': 0, 'Coefficients':[		   
		[ 
		  -100.00000, #	# school
		  -100.00000, #	# work
		-11.22384023, # (RetEmp(1)*SUni)
		  3.61160889, # (RetEmp(1)*SEat)
		  3.79679787, # (RetEmp(1)*SShp)
		  2.38424849, # (RetEmp(1)*SMnt)
		  1.44027421, # (RetEmp(1)*SDsc)
		  0.26774768, # (RetEmp(1)*SChf)
		  ]]},  # Retail Employment segmented by stop purpose
    {'Segment': 0, 'Vector': 'durable', 'Offset': 1, 'Coefficients':[		   
		[ 
		   -100.00000, #	# school
		   -100.00000, #	# work
		  -0.44895797, # (NrEmp(1)*SUni)
		  -0.21040163, # (NrEmp(1)*SEat)
		  -1.69754461, # (NrEmp(1)*SShp)
		   0.57013342, # (NrEmp(1)*SMnt)
		  -0.34416818, # (NrEmp(1)*SDsc)
		  -0.28231003, # (NrEmp(1)*SChf)
		  ]]},  # Non-retail Employment segmented by stop purpose
		  
    {'Segment': 1, 'Vector': 'durable', 'Offset': 2, 'Coefficients':[
		   # ftw lo   #ptw lo     #other lo   #ftw hi     #ptw hi     #other hi   
		[ 1.05474287, 0.01231716, -7.38301818, 1.49240313, 0.01231716, -0.69395849,
		  -100.00000, -100.00000, -100.00000, -100.00000, -100.00000, -100.00000]  # these are non-work stop coeffs; -100 to drive the contribution to 0 (coeff is exponentiated prior to combination with variable) 
		]},  # Retail Employment Segmented by work stop/worker type/inc lo-hi
    {'Segment': 1, 'Vector': 'durable', 'Offset': 3, 'Coefficients':[		   
		   # ftw lo   #ptw lo     #other lo   #ftw hi     #ptw hi     #other hi   
		[ 0.60727146, 0.46130879, 0.35497499, 1.37811505, 0.18061868, 0.68498170, # work stop coeffs
		  -100.00000, -100.00000, -100.00000, -100.00000, -100.00000, -100.00000]  # these are non-work stop coeffs; -100 to drive the contribution to 0 (coeff is exponentiated prior to combination with variable)
		  ]},  # Non-retail Employment Segmented by work stop/worker type/inc lo-hi
    {'Segment': 2, 'Vector': 'durable', 'Offset': 5, 'Coefficients':[		   		   
		[-100, 		# not uni tour or stop
		 0.18926755 # uni tour or stop
		]
	]},		  
		  
]
