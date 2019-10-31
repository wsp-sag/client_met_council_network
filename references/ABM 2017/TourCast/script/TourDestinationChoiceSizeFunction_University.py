####################################################################
# TourDestinationChoiceSizeFunction_University.py
# 
# This file is imported into TourDestinationChoiceUniversity.py
####################################################################
from Globals import * # for numberOfZones

# note no segmentation for this size function
sizeFunction= {

   "lsm" : 1.0,
   "locationStart" : 1,
   "locationEnd" : numberOfZones, 
   # one set of coeffs for all alternatives in this model component;    
   "durableCoeffs" : [
         11.38128353, # Enrolled # Enrolled in zone 
         6.44282240, # enrolled2 # enrollment within 2 miles 
         4.06717373, # enrolled5 # enrollment within 5 miles 
         0.00000000, # Enrolled10 # enrollment within 10 miles 
         6.71269079, # NREmp # NonRetail Employment 

    ] ,

   "transientCoeffs" : [] #no individual-dependent data
}


# coefficient maps will not be part of sizeFunction itself, but handled inside the modelcomponent code
   # same format as for alternative coeff maps:
   # input column start index, durable coeff start index, number of data fields 

sizeFunctionDurableCoeffMap = { "Zones": [[1, 0, 5]] }
sizeFunctionTransientCoeffMap = { }

sizeFunctionSegmentDefinitions = []
sizeFunctionSegmentCoeffMap = []
