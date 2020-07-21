####################################################################
# SchoolLocationChoiceModel.py
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
from Globals import * # for numberOfZones

# Size Function defined in another file to reduce clutter here
import SchoolLocationSizeFunction as sizeFunction

# TODO: Not sure how we'll specify the logsum generator
# Using this placeholder as a reminder:
logsumGeneratorName="SchoolLocationTourModeChoiceLogsum"

# the name of the corresponding class on the C# side:
# this allows for multiple scripts targeting the same component
modelComponentName="SchoolLocation"  

# TODO: I think this will be used by the Model component factory to hand the component the correct logit object
# in AA we hardwired this in the component
logitType="MultinomialLogit"


parameters={
            "MdPmSplitThreshold": 0.54
            }





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
     "name" : "Households",  # this household data is needed only to feed to the logsum; note vars noCarsInHh and nCars, while household, will be supplied by NCarsFromAA
     "filename" : cube___HOUSEHOLDS_FILE___, # file paths MUST BE RAW strings (open quote preceded by 'r')
     "columns" : ["hhid", "hhzon", "hhinc5s", "nKidsGT2", "numWorkers", "hstud"],
     "sort" :  ["hhzon", "hhid"]
    },


    {"type" : "dbffile",
     "name" : "Persons",
     "filename" : cube___PERSONS_CHILDREN___, # file paths MUST BE RAW strings (open quote preceded by 'r')
     "columns" : ["personid", 
                  "hhid", 
                  "hhzon", 
                  "ctype", 
                  "ptype2",# these are used by SchoolLocationTourModeChoiceLogsum
                  "gender",            
                  "age",
                  ], #
      "sort" :  ["hhzon", "hhid", "ctype"],
      #"maxrecords" : 100000 # about 3 minutes
    },
     
    {"type" : "dbffile",
     "name" : "Zones",
     "filename" : cube___ZONES_FILE___, # file paths MUST BE RAW strings (preceded by 'r')
     "columns" : ["zoneId", "k12_emp", "col_emp", "off_emp","households", "tw_acc", "k12_enrol"]
    },

    {"type" : "dbffile",
     "name" : "NCarsFromAA",     
     "filename" : cube___NUM_CARS_PER_HOUSEHOLD___,# file paths MUST BE RAW strings (preceded by 'r')
     # for dbf as input, supply columns instead of parameters
     # one problem with the way we're processing dbf files as input is that we don't have a select statement
     # so could be inputting lots of irrelevant data plus
     "columns" : ["hhid", "nCars", "noCarsInHh"]
    },    
    
    {"type" : "memory",
     "name" : "TotalsChosenPerZone",
     "columns" : ["totalChosen" # total number of children who've chosen this zone so far.
                 ]
    },

    # dbf output spec; used in tests for inspecting whether results are reasonable
    {"type" : "dbffile",
     "isOutput": "true",
     "name" : "OutputSchoolLocation",     
     "filename" : cube___SCHOOL_LOCATIONS___, # file paths MUST BE RAW strings (preceded by 'r')
     # parameters could be generally of form source data reference : field
     "parameters" : [
                       [ "Persons", "personId"],
                       [ "homeZone", "homeZoneId"],
                       [ "@alternativeChosen", "schZoneId"],
#                       [ "ChildType", "ChildType"], 
                       #[ "whichChildInFamily", "childNumber"],
                       #[ "logsum", "logsum"],
                       #[ "distanceOtoD", "distOD"],
                       #[ "noCarDist", "noCarDist"],
                       #[ "intrazone", "intrazone"],
                       #[ "transitAccess11Plus", "trnAcc11Plus"],
                       #[ "zoneEqPrevChildSameType", "zEqPrvEqType"],
                       #[ "zoneEqPrevChildTypeNear", "zEqPrvTypNr"],
                       #[ "zoneEqPrevChild", "zEqPrev"],
                       #[ "zoneEq2ndPrevChildTypeNear", "zEq2PrvNear"],
                       #[ "EmploymentK12", "EmployK12"], 
                       #[ "OfficeEmploymentCType1", "OffEmpCTyp1"], 
                       #[ "EmploymentCollegeCType5", "ColEmpCTyp5"], 
                       #[ "Households", "Households"], 
                       #[ "HouseholdsCType1", "HouseCType1"],
                       #[ "K12Enrollmt", "K12Enrollmt"],
                       #[ "numberCarsInHh", "nCarsHH"]
                       ## using '@' in data source name indicates this field is generated by the component, so requires some coordination with C# code
                    ]
    },        

    # dbf output spec; used in tests for inspecting whether results are reasonable
    {"type" : "delimited",
     "isOutput": "true",
     "name" : "OutputSchoolLocationStats",     
     "filename" : cube___SCHOOL_LOCATIONS_SUMMARY___, # file paths MUST BE RAW strings (preceded by 'r')             
     "parameters" : [
                       [ "StatLine", "AggregateData"],
                    ]
    }
]

# Matrices are different enough to require their own structure:
from MatrixRef1Hwy1Trans import matrixReferences


# ######################  model structure section  ##########################

# this is meant to represent the alternative output as either:
#    a real world value (e.g. that can be used in downstream utility functions 
#    or an ID of the alternative; in this case the values are number of cars:
# Note: not used directly except for end points
altIntrinsicValues= [1, numberOfZones]#

# not used thus far:
# friendly descriptions of the alternatives, maybe for UI display somehow
altNames = [] # the set of zones; component doesn't use this 

# this should evolve into a specification (in general) a tree structure
logitType = "MultinomialLogit"

# NOTE: no Alternative-Specific Constants for this model (size function serves this purpose I guess)
#altSpecificConsts=None

# for this component we'll share one set of coefficients among all alternatives
# because location alternative set is used, zone-specific data must be in durable arrays, which map to location arrays 
durableCoeffs=[
  [1],      # modeLogsum, 
  [0],      # logChDist (child-segmented (5 seg)), 
  [0],      # noCarDist(auto/no auto segment), 
  [-1.110], # intrazone, 
  [0],      # xitChT345 (segmented child type 2 segs) (transit access)
  [3.990],  # sameSibZn,
  [2.518],  # closeSibZn,
  [0.653],  # anySibZn, 
  [0.397]   # closSib2Zn, 
   # sizeFunction is handled separately
]

# HACK: Overloading Transient values to take advantage of the shortcut implementation of exp(U) in 
# LocationAlternativeSet.RecomputeValues
# log(max(0.000000001, (1.2*totEmp - chosen) / 1.2*totEmp))
transientCoeffs=[[1.0]]
transientCoeffMap={}

# note: SizeFunction is handled separately

# mlogsum value comes from code for now, and the matrix value is alternative-specific

# discussion: 
# modeLogsum could be treated as a data reference, for now handle in code instead
# distance is from distance matrix; can note that here, not sure how useful it is; 
#  we can't quite use the map as we'd do normally because we are not just feeding a data row and picking out one or more values
#  we are getting a setof data for all alternatives that we need to set the locationValues at a particular offset in each zone vector
#  in that sense we can use the idea of mapping to that offset
# intrazone comes from interaction with persons field  [offset 2]  and the alternative value; do this in code for now
# xitChT345 comes from transit access matrix but needs massaging for case where origin zone - dest zone; do in code
durableCoeffMap={} 
# standard mapping doesn't work for matrix, need some new scheme; would have to be a diagonal mapping across alternatives
# I had something like this but this is nonsense: durableCoeffMap={"DistanceMatrixOD" : [[0,1,1] , [0, 2, 1]]} 
#sameSibZn, closeSibZn, anySibZn, closSib2Zn are calculated in loop


# these segmentDefinitions are passed in code to the LocationAlternativeSet for handling
segmentDefinitions = [
#  friendly name     , input data ref, offset in input, range of values (order relates to coeff order in segmentCoeffMap)
 {'Name': 'No Car In HH', 'DataRef': 'NCarsFromAA','Offset': 2, 'DataRange': [0,1]},
 {'Name': 'Child Type', 'DataRef': 'Persons','Offset': 3, 'DataRange': [1,2,3,4,5]}
# {'Name': 'Child 11 or older', 'DataRef': 'Persons','Offset': 4, 'DataRange': [0,1]} dont need this
]

segmentCoeffMap = [
{'Segment': 0, 'Vector': 'durable', 'Offset': 2,  # noCarInHh
  'Coefficients':
    [ 
        # shared coeffs across all alternatives
        [0, -0.222]
    ]
},
{'Segment': 1, 'Vector': 'durable', 'Offset': 1,  # chLogDist
  'Coefficients':
    [ 
        [-2.512, -3.118, -2.590, -2.523, -2.337]
    ]
}, 
{'Segment': 1, 'Vector': 'durable', 'Offset': 4,  # xitChT345 GV: eliminate age11plus and use segmentation of ctype instead (ctype 3,4, or 5)
  'Coefficients':
    [ 
        [0, 0, 0.349, 0.349, 0.349]
    ]
}

]