####################################################################
# SchoolLocationSizeFunction.py
# This file is imported by SchoolLocationChoiceModel.py
# For size functions we use 1-D notation for coeff arrays because 
# the coefficients are the same for every alternative(i.e. every location).
# However for the coefficient maps we're holding on to the 2-D notation 
# but only using one row
####################################################################

from Globals import * # for numberOfZones

sizeFunction= {

   "lsm" : 1.0,
   "useExpCoeffs" : False,
   "locationStart" : 1,
   "locationEnd" : numberOfZones, 
   # one set of coeffs for all alternatives in this model component;    
   # "durableCoeffs" : [0.574, -6.00, 0, 0, 0, 0 ],   # k12_emp, hh, col_emp (segmented), off_emp (segmented), hh (segmented), k12enrol
   "durableCoeffs" : [1.7757, 0.0025, 0, 0, 0, 1.0 ],   # k12_emp, hh, col_emp (segmented), off_emp (segmented), hh (segmented), k12enrol
   "transientCoeffs" : [] 
}


# coefficient maps will not be part of sizeFunction itself, but handled inside the modelcomponent code
   # same format as for alternative coeff maps:
   # input column start index, durable coeff start index, number of data fields 

sizeFunctionDurableCoeffMap = { "Zones": [
                                          [1, 0, 1], #k12_emp
                                          [4, 1, 1], #hh (unsegmented)
                                          [2, 2, 3], #col_emp, off_emp, hh (all segmented)
                                          [6, 5, 1], #k12_enrol (not segmented but coeff is 0 => 1)
                                          ] }
sizeFunctionTransientCoeffMap = { }



sizeFunctionSegmentDefinitions = [
#  friendly name     , input data ref, offset in input, range of values (order relates to coeff order in segmentCoeffMap)
 {'Name': 'ChildType', 'DataRef': 'Persons','Offset': 3, 'DataRange': [1,2,3,4,5]}
]

# segmentation in this case only applies to the durable (location) coefficients

sizeFunctionSegmentCoeffMap = [
{'Segment': 0, 'Vector': 'durable', 'Offset': 2,  # col_emp (Child Type 5 only)
  'Coefficients':
    [ 
        #keep same format here as for the alternative-related segmentation
        #even though we'll always have only one row of coeffs 
#        [0, 0, 0, 0, -1.099]
        [0, 0, 0, 0, 0.3333]
    ]
},
{'Segment': 0, 'Vector': 'durable', 'Offset': 3,  # off_emp (type 1 only)
  'Coefficients':
    [ 
#        [-0.464, 0, 0, 0, 0]
        [0.6287, 0, 0, 0, 0]
    ]
}, 
{'Segment': 0, 'Vector': 'durable', 'Offset': 4,  # hh (type 1 only)
  'Coefficients':
    [ 
#        [1.144, 0, 0, 0, 0]
        [3.1388, 0, 0, 0, 0]
    ]
}
]