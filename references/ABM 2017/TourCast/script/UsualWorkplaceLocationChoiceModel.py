####################################################################
# UsualWorkplaceLocationChoiceModel.py
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
import UsualWorkplaceSizeFunction as sizeFunction

# TODO: Not sure how we'll specify the logsum generator
# Using this placeholder as a reminder:
logsumGeneratorName="UsualWorkplaceLocationTourModeChoiceLogsum"

# the name of the corresponding class on the C# side:
# this allows for multiple scripts targeting the same component
modelComponentName="UsualWorkplaceLocation"  

# TODO: I think this will be used by the Model component factory to hand the component the correct logit object
# in AA we hardwired this in the component
logitType="MultinomialLogit"

parameters={
            "ZeroTolerance": 0.000000001, # value to use instead of zero so that log doesn't blow up
            "TotEmpUpperBoundScale": 1.2, # scale the total employment by this factor when implementing the constraint
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

	
    {"type" : "constantsgrid",
     "dataType":"double",
     "name" : "TimeOfDayArriveReturnDistribution",
     "columns" : ["returnAM", "returnMD", "returnPM", "returnNT"],
     "rows" : ["arriveAM", "arriveMD", "arrivePM", "arriveNT"],
     "values" : [
                 [0.005967928, 0.222668224, 0.373816283, 0.014838114], # arriveAM
                 [0.000000000, 0.088023847, 0.130401534, 0.049080217], # arriveMD
                 [0.000000000, 0.000000000, 0.006364711, 0.033860118], # arrivePM
                 [0.012784761, 0.032946217, 0.011992501, 0.017255545]  # arriveNT
                ]
    },
	

    {"type" : "dbffile",
     "name" : "Households",  # this household data is needed only to feed to the logsum; note vars noCarsInHh and nCars, while household, will be supplied by NCarsFromAA
     "filename" : cube___HOUSEHOLDS_FILE___, # file paths MUST BE RAW strings (open quote preceded by 'r')
     "columns" : ["hhid", "hhzon", "hhinc5s", "nKidsGT2", "hworkers", "hstud"],
     "sort" :  ["hhzon", "hhid"]
    },


    {"type" : "dbffile",
     "name" : "Persons",
     "filename" : cube___WORKPLACE_LOCATIONS_PERSONS___, # file paths MUST BE RAW strings (open quote preceded by 'r')
     "columns" : ["personid", 
                  "hhid",      
                  "hhzon", 
                  "ptype",    # for location set segmentation (segmentation in coeff array, not segmentDefinitions)
                  "hhinc5s",  # for location set segmentation (normal)
                  "noRegWkPlc",
                  #some values are needed by the TourModeChoicelogsum; not known yet                                    
                  "hhsize",     # 6 for deriving '2 person hh', 'hh size 3+'
                  "hworkers",   # 7 used alone and for deriving workers > cars
                  "hadults",    # 8 for deriving Adults > Cars, Workers <= Cars, Cars > 0              
                  "nCars",      # 9 for nCars and deriving workers > cars
                  "noCarsInHh", # 10
                  "wkGtCarGt0", # 11
                  "hh1Person",  # 12 could derive from hhsize if we wanted less data input
                  "age",        #  13 for deriving 'age < 30'
                  "female",      # 14 for deriving male for logsum
				  "hchildren"
                  ], 
      "deferredLoad" : True,
      #"sort" : ["hhzon", "hhinc5s", "ptype", "age","female", "hhid"] # this is sort as output by UsualWorkplaceExistence
      #"maxrecords" : 5000 # about 3 minutes
      # need only homezone f
    },
     
    {"type" : "dbffile",
     "name" : "Zones",
     "filename" : cube___ZONES_FILE___, # file paths MUST BE RAW strings (preceded by 'r')
     "columns" : ["ZONEID",    # 0
                  "NRET_EMP",	# 1
				  "RET_EMP", # 2
				  "AREA", # 3
				  "CBD", # 4
				  "TW_ACC", # 5				  
				  "TERM_TIME", #6
				  "TOT_EMP", # 7 
				  "MIX_DENS", #8
                  ]
    },

    {"type" : "memory",
     "name" : "DerivedValues",
     "columns" : ["workerXIncomeSegment", #use this for size fn and location
                                            # only care about 2 ptypes(workers) and 3 income segments: 
                                             #ptypes  5=ftw, 6=ptw
                                             # income segments: <25k, 25 - 50k, 50 - 75k, >75k,
                                             #so take 10X ptype + income 1 or 2 or 3 or 4
                  ]         #
    },	

    # dbf output spec; used in tests for inspecting whether results are reasonable
    {"type" : "dbffile",
     "isOutput": "true",
     "name" : "OutputWorkplaceLocation",     
     "filename" : cube___WORKPLACE_LOCATIONS___, # file paths MUST BE RAW strings (preceded by 'r')
     # parameters could be generally of form source data reference : field
     "parameters" : [
                       [ "Persons", "personId"],
                       [ "hhId", "hhId"],
                       [ "hhzon", "hhzon"],
                       [ "no regular workplace", "noRegWkPlc"],
                       [ "@alternativeChosen", "workzoneId"],
                       [ "@logsum", "logsum"],  # logsum from homezone to chosen zone
                       [ "@logRtToWk", "logRtToWk"],  # logsum from homezone to chosen zone
                       [ "@wlkTraccWk", "wlkTraccWk"], # logsum from homezone to chosen zone
					   ["@workplace in CBD", "wkPlcInCBD"], 
					   ["@workplace in Suburb", "wkPlcInSub"]					   
                       # using '@' in data source name indicates this field is generated by the component, so requires some coordination with C# code
                    ]
    },        

    {"type" : "delimited",
     "isOutput": "true",
     "name" : "OutputWorkplaceLocationStats",     
     "filename" : cube___WORKPLACE_LOCATIONS_SUMMARY___, # file paths MUST BE RAW strings (preceded by 'r')
     # parameters could be generally of form source data reference : field
     "parameters" : [
                       [ "StatLine", "AggregateData"]
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

# for location set component we'll share one set of coefficients among all alternatives
# because location alternative set is used, zone-specific data must be in durable arrays, which map to location arrays 
durableCoeffs=[
  [placeholder],      #0 modeLogsum,  All data is segmented by a composite of ptype and hhinc
  [placeholder],      #1 intrazone,   
  [placeholder],      #2 log(1 +RT Dist), 
  [placeholder],      #3 RT Dist,   
  [placeholder],      #4 mixed density, 
  [0.13177565],#5 term time = 5,
  [placeholder]      #6 Transit Walk Access and non-zero autos > workers
  
  
   # sizeFunction is handled separately
]
durableCoeffMap={} 
# standard mapping doesn't work for matrix, need some new scheme; would have to be a diagonal mapping across alternatives

# HACK: Overloading Transient values to take advantage of the shortcut implementation of exp(U) in 
# LocationAlternativeSet.RecomputeValues
# log(max(0.000000001, (1.2*totEmp - chosen) / 1.2*totEmp))
transientCoeffs=[[1.0]] 
transientCoeffMap={}

# note: SizeFunction is handled separately

# mlogsum value comes from code for now, and the matrix value is alternative-specific


# these segmentDefinitions are passed in code to the LocationAlternativeSet for handling
segmentDefinitions = [
#  friendly name     , input data ref, offset in input, range of values (order relates to coeff order in segmentCoeffMap)
 {'Name': 'worker-Income Segment', 'DataRef': 'DerivedValues','Offset': 0, 'DataRange': [50,51,52,53,54,60,61,62,63,64]}
]

segmentCoeffMap = [
{'Segment': 0, 'Vector': 'durable', 'Offset': 0,  # modeLogsum
  'Coefficients':
    [ 
        # shared coeffs across all alternatives
        #ftw                  							ptw               
        #<25k,   	25-50K,    	50-75k     	75k-100K   	>100k		<25k,   	25-50K,    	50-75k     	75k-100K   	>100k     	  income
        [0.64811204, 0.64811204, 0.64811204, 0.64811204, 0.64811204, 0.25630895, 0.25630895, 0.25630895, 0.25630895, 0.25630895]
    ]
},
{'Segment': 0, 'Vector': 'durable', 'Offset': 1,  # intrazone
  'Coefficients':
    [ 
		#[1.86349822,1.86349822,1.86349822,1.86349822,1.86349822,0.89598937,0.89598937,0.89598937,0.89598937,0.89598937]
		#[1.916,1.916,1.916,1.916,1.916,1.276,1.276,1.276,1.276,1.276]
		#[1.916,1.916,1.916,1.916,1.916,1.423,1.423,1.423,1.423,1.423]
		[1.9,1.9,1.9,1.9,1.9,1.479,1.479,1.479,1.479,1.479]
		
        #[1.71,1.71,1.71,1.71,1.71,0.585,0.585,0.585,0.585,0.585]
		#[1.539,1.539,1.539,1.539,1.539,0.1,0.1,0.1,0.1,0.1]
		#[1.3851,1.3851,1.3851,1.3851,1.3851,0,0,0,0,0]
		#[1.3851,1.3851,1.3851,1.3851,1.3851,-0.1,-0.1,-0.1,-0.1,-0.1]
		#[1.3851,1.3851,1.3851,1.3851,1.3851,-0.2,-0.2,-0.2,-0.2,-0.2]
		#[7.45399288,7.45399288,7.45399288,7.45399288,7.45399288,3.58395748,3.58395748,3.58395748,3.58395748,3.58395748]
	]
}, 
{'Segment': 0, 'Vector': 'durable', 'Offset': 2,  # log(1 +RT Dist)
  'Coefficients':
    [ 
        [-0.882139251,-0.660107364,-0.5810330925,-0.5810330925,-0.5810330925,-1.4096925455,-1.4096925455,-1.4096925455,-1.4096925455,-1.4096925455]
		#[-0.92624621355,-0.6931127322,-0.610084747125,-0.610084747125,-0.610084747125,-1.480177172775,-1.480177172775,-1.480177172775,-1.480177172775,-1.480177172775]
		#[-0.972559,-0.727768,-0.640589,-0.640589,-0.640589,-1.554186,-1.554186,-1.554186,-1.554186,-1.554186]
    ]
},
{'Segment': 0, 'Vector': 'durable', 'Offset': 3,  # Dist
  'Coefficients':
    [ 
        [-0.03503922,-0.03503922,-0.03503922,-0.03503922,-0.03503922,-0.03014343,-0.03014343,-0.03014343,-0.03014343,-0.03014343]
		#[-0.036,-0.036,-0.036,-0.036,-0.036,-0.031,-0.031,-0.031,-0.031,-0.031]
		#[-0.0396,-0.0396,-0.0396,-0.0396,-0.0396,-0.0341,-0.0341,-0.0341,-0.0341,-0.0341]
    ]
},
{'Segment': 0, 'Vector': 'durable', 'Offset': 4,  # mixed density
  'Coefficients':
    [ 
        [-0.00014204, -0.00014204, -0.00014204, -0.00014204, -0.00014204, -0.00060535, -0.00060535, -0.00060535, -0.00060535, -0.00060535]
    ]
},
{'Segment': 0, 'Vector': 'durable', 'Offset': 6,  #  Transit Walk Access and non-zero autos > workers
  'Coefficients':
    [ 
        [-0.37929287, -0.37929287, -0.37929287, -0.37929287, -0.37929287, -0.44439402, -0.44439402, -0.44439402, -0.44439402, -0.44439402]
    ]
}
]