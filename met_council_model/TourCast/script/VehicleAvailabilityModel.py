####################################################################
# VehicleAvailabilityModel.py
# A python script delineating the following:
#   Set of alternatives
#   Utility function coefficients
#   Input data sources 
#   mapping inputs to coefficients

#  Yet to be defined or dealt with:
#   Formulae for combining inputs (need to cover alternative-agnostic and alternative-specific formulae)
#   Logit type and structure (assuming Multinomial for first attempt)
#   Differentiating between input and output data references;
#   specifying the destination of the output data
# other notes:
#   I am not adhering to the python convention of 70-odd columns per line
####################################################################
from Globals import * 
from CubeKeyValues import *

# the name of the corresponding class on the C# side:
# this allows for multiple scripts targeting the same component
modelComponentName="AAOrdered"  

# dataReferences is an array
# each array element is a dictionary (set of key:value pairs); each dictionary has 2 required keys:  name and type
# the value corresponding to the "type" key indicates to C# how to instantiate the data reference
# the set of names is fixed for each C#-side model component
# each type constrains the set of keys to supply in the remainder of that dictionary
# e.g. a type of "db" currently (this spec is in flux) requires the connectionString and queryString
# to demonstrate that this structure can be read I've included an Excel data reference type
# and as an experiment in output, I also have a console data reference type so the component can display alternative choices
# until we have a real output spec
dataReferences = [

    {"type" : "dbffile",
     "name" : "Households",
     "filename" : cube___HOUSEHOLDS_FILE___, 
     # Column names are uppercase in this file
     "columns" : ["HHID", "HHINC5S", "HHZON", "HCHILD3", "HSTUD", 
                  "HPTW", "HNWA", "HSEN", "HH1PERSON", "ADULT1KIDS", 
                  "HFTW", "HHSIZE"],  # last one for stats only
     "sort": ["HHZON", "HHINC5S", "HHID"] #why hhid? because need to output data combined into persons data
    },

    # should be obvious
    {"type" : "constants",
     "name" : "Constants",
     "columns" : ["One"],
     "values" : [1]
    },


     
    {"type" : "dbffile",
     "name" : "Zones",
     "filename" : cube___ZONES_FILE___, 
     "columns" : ["ZONEID",   # 0
                  "HHDENSITY",# 1
                  "TRHWACCRAT"# 2
                  ]
    },


    # dbf output spec
    {"type" : "dbffile",
     "isOutput": "true",
     "name" : "OutputNCarsDbf",     
     "filename" : cube___NUM_CARS_PER_HOUSEHOLD___, 
     # parameters could be generally of form source data reference : field (and column name)
     # some specific knowledge of output fields may lie entirely in the model component
     # original design was a dictionary for parameters:
     #"parameters" : { "Households" : "hhid",
     #                "nCars" : "" , # special case where field is blank, indicates use value of chosen alternative
     #                "OutputNCarsDbf" : "noCarsInHh" # self-referencing this DataReference indicates a value that the component                                                     
     #                },
     # but there's problem keeping this a dictionary because the data reference could repeat
     # also I want to imply a column order in the dbf file (though possibly this is not important)
     # FOR NOW: column names will be used in the output but the data references will be ignored, with the output sources hard-coded in the component
     # could add data type as third value in each row here:
     "parameters" : [ ["Households", "hhid"],
                      ["hhzon", "HHZON"],
                      ["@AlternativeChoice" ,  "nCars" ] , # '@' starting the data source indicates this field is generated by the component, so requires some coordination with C# code
                      ["@noCarsInHousehold", "noCarsInHh"],
                      ["@workersGtCarsGt0", "wkGtCarGt0"] #  more workers than cars and at least one car in hh
                    ]
    },

    # dbf output spec
    {"type" : "dbffile",
     "isOutput": "true",
     "name" : "OutputAAStats",     
     "filename" : cube___VEHICLE_AVAILABILITY_SUMMARY___, 
     # parameters could be generally of form source data reference : field (and column name)
     # some specific knowledge of output fields may lie entirely in the model component
     # original design was a dictionary for parameters:
     #"parameters" : { "Households" : "hhid",
     #                "nCars" : "" , # special case where field is blank, indicates use value of chosen alternative
     #                "OutputNCarsDbf" : "noCarsInHh" # self-referencing this DataReference indicates a value that the component                                                     
     #                },
     # but there's problem keeping this a dictionary because the data reference could repeat
     # also I want to imply a column order in the dbf file (though possibly this is not important)
     # FOR NOW: column names will be used in the output but the data references will be ignored, with the output sources hard-coded in the component
     # could add data type as third value in each row here:
     "parameters" : [ ["HHINC5S", "HHINC5S"],
                      ["hhsize", "hhsize"],
                      ["@noCars" ,  "noCars" ] , 
                      ["@oneCar" ,  "oneCar" ] , 
                      ["@twoCars" ,  "twoCars" ] , 
                      ["@threeCars" ,  "threeCars" ] , 
                      ["@fourCars" ,  "fourCars" ] , 
                      ["@fiveCars" ,  "fiveCars" ] , 
                      ["@sixCars" ,  "sixCars" ] 
                    ]
    },

    
]


# ######################  model structure section  ##########################

# this is meant to represent the alternative output as either:
#    a real world value (e.g. that can be used in downstream utility functions 
#    or an ID of the alternative; in this case the values are number of cars:
altIntrinsicValues= [0, 1, 2, 3, 4, 5, 6]

# friendly descriptions of the alternatives, maybe for UI display somehow
altNames = ["0 Cars", "1 Car", "2 Cars", "3 Cars", "4 Cars", "5 Cars", "6+ Cars"]

# this should evolve into a specification (in general) a tree structure
logitType="OrderedLogit"

# There is only one Utility equation for Ordered Logit, so there would be no alternative-specific consts
# also 1000 is a placeholder to line up the alternatives (for now) with the other alt arrays 
altThetas=[-1.678, 2.982, 6.638, 8.543, 10.056, 12.16]

# NOTE: Alternative-Specific Constants are not used in OrderedLogit
#altSpecificConsts=None

#Coefficients are divided into two types:
#   coefficients whose corresponding values don't change very often ('durable' values)
#   coefficients whose values are assumed to change for every iteration ('transient' or 'mutable' values)
# (Note: I stayed away from using 'volatile' because it is a keyword in C#)
# this division is determined based on how we order the input data
#
# so we have two 2-dimensional arrays, one for durable and one for transient data
# for Ordered Logit we only need one row which will be shared among all alternatives

# proposed sort order is Zone, household income, household number of full time workers (probably somewhat correlated with HHINC5S)


# durables are not segmented so the coefficients are entered here
durableCoeffs=[
  [-0.000202],   # HHDENSITY
  [-0.754]       # TRHWACCRAT
  # note only one utility eq for Ordered Logit 
]

# transients are all household related 
transientCoeffs=[
  [placeholder], # 0 HCHILD3 
  [0.823], # 1 HSTUD
  [placeholder], # 2 HPTW    
  [placeholder], # 3 HNWA
  [1.198], # 4 HSEN
  [-0.971], # 5 HH1PERSON
  [placeholder], # 6 ADULT1KIDS
  [placeholder], # 7 HFTW
  [placeholder]  # 8 INCOME DUMMY
   # zero is segment coeff placeholder;  note only one set of coeffs for Ordered Logit - one utility eq
]


# we need a map from the inputs to the locations in the vectors; instead of name matching do index matching
# It's easier to devise a notation if the order of data columns matches up with a range of the coefficients
# here's what I have come up with:
# durableCoeffMap={"table name": [[tableColIndex, matchingCoeffVectorStartIndex, numberOfConsecutiveColumnsToMatch],...]}
durableCoeffMap={ "Zones": [[1, 0, 2]], "Households": [] }
# i.e. to populate values in the durable value vector:
# starting at offset 1 in the Zone input data for each row (each row is an array, call it z[])
#   copy 3 consecutive values to the durable value vector (call it durable[]) starting at offset 0, i.e:       
#      copy z[1] --> durable[0]
#      copy z[2] --> durable[1]
#   then using household input data row (call it hh)
#      copy hh[4] --> durable[3],
#      copy hh[8] --> durable[4], 

# similarly
transientCoeffMap = {"Households" : 
                     [
                     [3,0,8] # HCHILD3, HSTUD, HPTW, HNWA, HSEN, HH1PERSON, ADULT1KIDS, HFTW
                     ],
                     "Constants" :
                     [[0, 8, 1]	
                     ]
}



# note: this mapping scheme is compatible with handling special-case calculations because we can omit from these maps any coefficients related to these cases,
# and handle those separately, either by custom code in the component, or preferably by specifying the calculation here
# for instance, we could specify formulae for specific durable and transient coefficients, maybe like this:
# durableCoeffFormulae = [5, "ln($0$) + $1$/$2$", {"Households" :[3,8]}, "ZoneAttributes":[2]}]
# translation: calculate the value associated with coefficient 5 using the formula shown, 
# substituting the $N$ placeholders by the values at the specified Households and ZoneAttributes indices


# this would NOT work for alternative-specific formulae, because the value vector for the above calculations is shared across all the alternatives
# but we could do something similar notation-wise
# alternativeSpecificFormulae = [1, "ln($0$) + $1$/$2$ - $0$", {"Households" :[8]}, "ZoneAttributes":[2]}], where $0$ always represents the alternative value
# we'd also need a separate coefficient array for ASVs (probably small), and each alternative would have its own value vector
# based on the formula we could monitor the input values (here Households[8] and ZoneAttributes[2]) and only recalculate the ASV parts when these change.
#  this could save a bunch of calcs if the number of alternatives is large.

# 
# SEGMENTATION maps:
#

# segmentDefinitions is an array, each element of which defines (via a dictionary):
#  Name: a friendly name not used elsewhere except maybe in comments in this file
#  DataRef:  Which input DataReference contains the segmentation info
#  Offset:   which column in the input has this segmentation info
#  DataRange: an array of discrete values representing the segmentation range; 
# there are 2 subtleties here:
#    at the top level, the array index within the segmentDefinitions array is used in the segmentCoeffMap
#    the DataRange array order corresponds to the order of the coefficients in each row of the 'coefficients' value in segmentCoeffMap
segmentDefinitions = [
#  friendly name     , input data ref, offset in input, range of values (order relates to coeff order in segmentCoeffMap)
 {'Name': '5 Income Segments', 'DataRef': 'Households','Offset': 1, 'DataRange': [0,1,2,3,4]}
]

#segmentCoeffMap is another array of dictionaries.  The size of the array = the number of coefficients 
# that are affected by segmentation within the durable and transient vectors of the alternative(s)
# Each dictionary defines:
#  Segment: index into the segmentDefinitions array
#  Vector:  possible values: durable/transient:  which coefficient vector in the alternative(s) this set of coefficients applies to
#  Offset:  offset into the relevant Coefficient vector 
#  Coefficients: an array of arrays; first index is which alternative (only one here)
#           for each alternative, the array represents coefficient value 
#               corresponding by index with each possible value of the segment in the segmentDefinitions.DataRange
#               e.g. if the '5 Income Segments' input value = 2, then the coefficient for hchild3 (the last segmentCoeffMap array 
#               below) is at offset 2 of the Coefficients, or 0.515
#               another example, if the '2 Income Segments' input (at offset 11 of the households data) = 0,
#               for the first 8 array rows below, we'll substitute the 0th cofficient value in the proper coeff vector locations:
#                   durableCoefficientVector[1] = -0.0368;
#                   durableCoefficientVector[3] =  1.46;
#                   transientCoefficientVector[1] =  1.34;
#                   transientCoefficientVector[2] =  1.25;  etc...



segmentCoeffMap = [
# 5 income segments 
# segmentDefinitions offset, which coeffVector, offset in coeffVector, 
# there are no durable variable segments
# ---------------- transients ------------------------
{'Segment': 0, 'Vector': 'transient', 'Offset': 0, #hchild3
  'Coefficients':
    [ 
        [-1.138, -1.138, 1.317, 1.317, 1.317]
    ]
},
{'Segment': 0, 'Vector': 'transient', 'Offset': 2,  # HPTW
  'Coefficients':
    [ 
        [2.532, 1.998, 1.525, 1.525, 1.525]
    ]
}, 
{'Segment': 0, 'Vector': 'transient', 'Offset': 3,  # HNWA
  'Coefficients':
    [ 
        [0.699, 0.699, 1.293, 1.293, 1.293]
    ]
}, 
{'Segment': 0, 'Vector': 'transient', 'Offset': 6,  # singleAdultWChild
  'Coefficients':
    [ 
        [-0.905, -0.905, -1.630, -2.727, -2.727]
    ]
}, 
{'Segment': 0, 'Vector': 'transient', 'Offset': 7,  # hftw
  'Coefficients':
    [ 
        [2.145, 2.145, 1.744, 1.744, 1.744]
    ]
}, 
{'Segment': 0, 'Vector': 'transient', 'Offset': 8, #hhincdummy
  'Coefficients':
    [ 
        [0, 1.059, 2.224, 2.462, 2.648]
    ]
} 
]




