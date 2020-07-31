####################################################################
# TourDestinationChoiceSizeFunction_IndividualNonMandatoryEscort.py
# Size Function handling only INM Escort Tours
# include this file in IndividualNonMandatoryEscortTourDestinationChoice.py
####################################################################

from Globals import * # for numberOfZones, placeholder, purposeXxxx, incXxxx

# note no segmentation for this size function
sizeFunction= {

   "lsm" : 1.0,
   "locationStart" : 1,
   "locationEnd" : numberOfZones, 
   # one set of coeffs for all alternatives in this model component;
   # Entirely segmented (hence 0's)
   "durableCoeffs" : [
         0.00000000, # NREmp # Non-Retail Emp 
         placeholder, # Retail Employment segmented by income
         placeholder, # n households segmented by income         
    ] ,

   "transientCoeffs" : [] #no individual-dependent data
}


# coefficient maps will not be part of sizeFunction itself, but handled inside the modelcomponent code
   # same format as for alternative coeff maps:
   # input column start index, durable coeff start index, number of data fields 

sizeFunctionDurableCoeffMap = { "Zones": [
                                          [13,0,1],
                                          [5,1,1],
                                          [10,2,1],
                                          ] }
sizeFunctionTransientCoeffMap = { }

## 
# data range Is only income segment, as they all share a tour purpose (Escort) and are segmented only by income
sizeFunctionSegmentDefinitions = [{'Name': 'Income 2 segments pivot 50k', 'DataRef': 'DerivedValuesForSizeFn','Offset': 0, 
                                   'DataRange': [0,1]} # 0: < 50k; 1: >=50k
]
sizeFunctionSegmentCoeffMap = [#                                          0-20 20-40 40-70 70-100 >100
        {'Segment': 0, 'Vector': 'durable', 'Offset': 1, 'Coefficients':[[1.12279475, 0.19222927]]},  #retail employment
        {'Segment': 0, 'Vector': 'durable', 'Offset': 2, 'Coefficients':[[0.81754271, 0.31758725]]},  #households
                              ]





