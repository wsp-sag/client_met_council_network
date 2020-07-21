####################################################################                                                                                                                                                                                           
# TourDestinationChoiceSizeFunction_IndividualNonMandatory.py
# size functions are different for the different tour purposes:
# uses compound segment of tour purpose/income
# This file is imported into IndividualNonMandatoryTourDestinationChoice.py
####################################################################                                                                                                                                                                                           

from Globals import * # for numberOfZones

sizeFunction= {

   "lsm" : 1.0,
   "locationStart" : 1,
   "locationEnd" : numberOfZones, 
   # one set of coeffs for all alternatives in this model component;
   # Entirely segmented (hence 0's)
   "durableCoeffs" : [                      
         0.00000000, # NREmp # Non-Retail Emp 
         placeholder, # Retail Emp Segmented income/purpose
         placeholder, # Households	Segmented purpose
    ] ,

   "transientCoeffs" : [] #no individual-dependent data
}


# coefficient maps will not be part of sizeFunction itself, but handled inside the modelcomponent code
   # same format as for alternative coeff maps:
   # input column start index, durable coeff start index, number of data fields 

sizeFunctionDurableCoeffMap = { "Zones": [
                                          [5, 0, 3],
                                          ] }
sizeFunctionTransientCoeffMap = { }


# data range constructed by adding income segment (0-4) to OutingPurposes values from OutingPurposesEnum (ml = 8,shp = 16, pb = 32, sr = 64)
# variables are defined in Globals.py
sizeFunctionSegmentDefinitions = [
     {'Name': 'Tour purpose by Income', 
      'DataRef': 'DerivedValuesForSizeFn',
      'Offset': 0, 
      'DataRange': [
          purposeMeal + incLt25k,
          purposeMeal + inc25To50k,
          purposeMeal + inc50To75k,
          purposeMeal + inc75To100k,
          purposeMeal + incGt100k,
          purposeShop + incLt25k,
          purposeShop + inc25To50k,
          purposeShop + inc50To75k,
          purposeShop + inc75To100k,
          purposeShop + incGt100k,
          purposePersonalBusiness + incLt25k,
          purposePersonalBusiness + inc25To50k,
          purposePersonalBusiness + inc50To75k,
          purposePersonalBusiness + inc75To100k,
          purposePersonalBusiness + incGt100k,
          purposeSocialRecreation + incLt25k,
          purposeSocialRecreation + inc25To50k,
          purposeSocialRecreation + inc50To75k,
          purposeSocialRecreation + inc75To100k,
          purposeSocialRecreation + incGt100k,]
     }, 
     {'Name': 'Tour purpose', 
      'DataRef': 'DerivedValuesForSizeFn',
      'Offset': 1, 
      'DataRange': [purposeMeal, purposeShop, purposePersonalBusiness, purposeSocialRecreation]
     }, 

]

sizeFunctionSegmentCoeffMap = [
        {'Segment': 0, 'Vector': 'durable', 'Offset': 1, 'Coefficients': [[3.96885706, 3.96885706, 4.05689572, 4.04779077, 4.04779077, 
                                                                           4.89261480, 4.89261480, 4.77888284, 5.08446176, 5.08446176, 
                                                                           1.15947094, 1.15947094, 1.32833364, 1.34572002, 1.34572002, 
                                                                           1.53717591, 1.53717591, 1.73687510, 1.80011833, 1.80011833]]},  # Retail Emp
        {'Segment': 1, 'Vector': 'durable', 'Offset': 2, 'Coefficients': [[2.00801899, 1.71512515, -0.46990446, 1.28825379 ]]},  #households
]