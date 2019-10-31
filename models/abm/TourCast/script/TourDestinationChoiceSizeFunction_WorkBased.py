####################################################################
# TourDestinationChoiceSizeFunction_WorkBased.py
# size functions are different for the different tour purposes:
# include this file in TourDestinationChoiceWorkBased.py
####################################################################

from Globals import * # for numberOfZones

sizeFunction= {

   "lsm" : 1.0,
   "locationStart" : 1,
   "locationEnd" : numberOfZones, 
   # one set of coeffs for all alternatives in size function
   "durableCoeffs" : [
		 0.00000000, # NREmp # Non-Retail Emp 
		 4.37992601, # Area # Zone area 		 
		 placeholder, # Retail Employment segmented by tour purpose
		 placeholder, # households segmented by tour purpose
    ] ,

   "transientCoeffs" : [] #no individual-dependent data outside of segmentations
}


# coefficient maps will not be part of sizeFunction itself, but handled inside the modelcomponent code
   # same format as for alternative coeff maps:
   # input column start index, durable coeff start index, number of data fields 

sizeFunctionDurableCoeffMap = { "Zones": [[1, 0, 4]] }
sizeFunctionTransientCoeffMap = { }


sizeFunctionSegmentDefinitions = [
  # straight segmentation by tour purpose
 {'Name': 'Tour Purpose', 'DataRef': 'DerivedValuesForSizeFn','Offset': 0, 
  'DataRange': [ #OKWB
                purposeWork  + purposeWorkBased,    # work  
                purposeMeal  + purposeWorkBased,    # meal  
                purposeShop  + purposeWorkBased,    # shop  
                purposePersonalBusiness  + purposeWorkBased,    # perbus
                purposeSocialRecreation  + purposeWorkBased,    # socrec
                purposeEscort  + purposeWorkBased,    # escort
                ]
  },
]

#OKWB
sizeFunctionSegmentCoeffMap = [                                        
    {'Segment': 0, 'Vector': 'durable', 'Offset': 2 , 'Coefficients':[[
		 0.61294241, # RetEJob # Retail Employment Work 
		 3.96399181, # RetEEat # Retail Employment Meal 
		 4.55785657, # RetEShp # Retail Employment Shop 
		 1.99556261, # RetEMnt # Retail Employment PersBus 
		 1.52132775, # RetEDsc # Retail Employment SocRec 
		 0.00000000, # RetEChf # Retail Employment Escort 
	]]},  # Retail employment
    {'Segment': 0, 'Vector': 'durable', 'Offset': 3 , 'Coefficients':[[
		-1.78796034, # HHtjob # Households	Work 
		 1.62053109, # HHteat # Households	Meal 
		 1.48707497, # HHtshp # Households	Shop 
		 0.10141116, # HHtdsc # Households	SocRec 
		 0.36477646, # HHtmnt # Households	PersBus 
		 0.00000000, # HHtjob # Households	Escort 
	]]},  # households
]











