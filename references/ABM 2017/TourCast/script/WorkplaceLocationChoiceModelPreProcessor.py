####################################################################
# WorkplaceLocationChoiceModelPreProcessor.py
# Really should be called UsualWorkplaceExistence.py

# other notes:
#   I am not adhering to the python convention of 70-odd columns per line
####################################################################
from Globals import * 

# the name of the corresponding class on the C# side:
# this allows for multiple scripts targeting the same component
modelComponentName="UsualWorkplaceExistence"  

dataReferences = [
     
    {"type" : "dbffile",
     "name" : "Persons",
     "filename" : cube___PERSONS_ADULTS___, # file paths MUST BE RAW strings (open quote preceded by 'r')
     "columns" :[
                 "PERSONID","HHID", "HHZON", "PTYPE", # 0-3
				 "FEMALE", "AGE", # 4-5
				 "HCHILD2", "HCHILD3", "HPOTWORKAD", "HWORKERS", # 6-9
                 "NOCARSINHH", "HHINC5S", "NCARS", "HH1PERSON", # 10-13
                 # columns needed by UsualWorkplaceTourModeChoiceLogsum:
                 "hhsize", "hadults", "wkGtCarGt0", "hchildren"
                ],
     # sort is now done in the code - can't specify here because of deferred load but this is the order:
     #"sort" : ["hhzon", "hhinc5s", "ptype", "age","female", "hhid"],   # note, sorting by ptype instead of ptype2 because correlates a little better with age
                                                                       # if we could: WHERE ptype in (6,7,8)"  # only ftw, ptw and seniors
                                                                       # sorting by age instead of sqrootage because our sort only supports integers
      "deferredLoad" : True,
     #"maxrecords" : 2000
    },
     

    {"type" : "dbffile",
     "name" : "Zones",
     "filename" : cube___ZONES_FILE___, # file paths MUST BE RAW strings (preceded by 'r')
     "columns" : ["zoneID",  # 0
					"mix_dens",
					"ext_dist"
                  ] 
    },
	
	# CodeBase expects a Derived Result used in HGAC to segment data
	{"type" : "memory",
     "dataType" : "double",
     "name" : "DerivedResults",     
     "columns" : ["Col " + str(x) for x in range(1, 10)] # dummy
    },

	
	{"type" : "computed",
     "name" : "computedValues",
	 # each parameter is of this form:
	 # ["columnNameForResult", "X op Y"]
	 # where X, Y each are one of the following:
	 #       constant e.g. 1.2
	 #       reference to column in another data reference
	 #         of form dataRefName:columnName 
	 #       reference to previous column in this datareference
	 #         using form :columnName
	 # op can be one of the 4 arithmetic operators + - * /
	 # or one of 7 logical operators == < <= > >= AND OR
	 # 
	 
     "parameters" :[
		["Constant", "1 == 1"],
		["incgt100", "Persons:hhinc5s == 4"],
        ["Age65", "Persons:AGE == 10"], 
        ["AgeGt25", "Persons:AGE > 5"]        
		]
    },
	
	

    # dbf output spec
    # because this is feeding directly into the UsualWorkplaceLocation,
    # export enough persons fields to satisfy that component
    {"type" : "dbffile",
     "isOutput": "true",
     "name" : "OutputWorkplaceExistence",     
     "filename" : cube___WORKPLACE_LOCATIONS_PERSONS___, 
     "parameters" : [
                    ["PERSONID","PERSONID"],  #these columns directly copied from Persons input
                    ["HHID","HHID"],
                    ["HHZON","HHZON"],
                    ["PTYPE","PTYPE"],
                    ["HHINC5S","HHINC5S"],
                    # needed for UsualWorkplaceTourModeChoiceLogsum:
                    ["hhsize", "hhsize"],    
                    ["hworkers", "hworkers"],  
                    ["hadults", "hadults"],   
                    ["nCars", "nCars"],     
                    ["noCarsInHh", "noCarsInHh"],
                    ["wkGtCarGt0", "wkGtCarGt0"],
                    ["hh1Person", "hh1Person"], 
                    ["age", "age"],  
                    ["female", "female"],  
					["hchildren", "hchildren"],
                    ["@workZoneId", "workZoneId"],# output from this component
                    ["@noRegWkPlc", "noRegWkPlc"], # output from this component
                    ]
    },

   
    {"type" : "dbffile",
     "isOutput": "true",
     "name" : "OutputPersonStats",     
     "filename" : cube___WORKPLACE_LOCATIONS_PERSONS_SUMMARY___, 
     "parameters" : [
                    ["PTYPE","PTYPE"],
                    ["HHINC5S","HHINC5S"],
                    ["FEMALE","FEMALE"],
                    ["@noRegWkPlc","noRegWkPlc"],
                    ["COUNT","COUNT"]
                    ]
    },

   
]



# Matrices are different enough to require their own structure:
matrixReferences = [
# for now none
]


# ######################  model structure section  ##########################

# regular workplace, no regular workplace 
altIntrinsicValues= [0, 1]#  

# not used thus far:
# friendly descriptions of the alternatives, maybe for UI display somehow
altNames = ["regular workplace", "no regular workplace"] 

# this should evolve into a specification (in general) a tree structure
logitType = "MultinomialLogit"

# constants are segregated so treat them as a segmented variable (i.e. they will appear in the coeffs paired with a dummy variable of 1)
altSpecificConsts= [0.00000000, -3.268]

# ALL COEFFS ARE SEGMENTED by person type so coefficients are all zero here:
# also the regular workplace is the base case, all coeffs are 0
durableCoeffs=[
#  reg,   no reg                                                    map to
 [placeholder]*2, #0 Constants                              DerivedResults 0
 [placeholder]*2, #1 inc5pt
 [placeholder]*2, #2 (Age65*ft)
 [placeholder]*2,  #3 (Age2564*ft) 
 [0.25011664, 0.00000000] #4 FEMALE 
]

# 
transientCoeffs=[
#  reg,   no reg                                                    map to
 [0.00000000, -0.08609447], #0 Number of Children 2 in HH                     Persons 6 hchild2
 [0.00000000, 0.12572319],  #1 Number of Children 3 in HH                     Persons 7 hchild3
 [0.00000000, 0.45339836],  #2 (hsen+hnwa+hstud)
 [0.00000000, -0.13193646], #3 (hftw+hptw)
 [0.00000000, 1.21534262]   #4 0 Cars in HH (Indicator)                       Persons 12 NOCARSINHH
]



# durableCoeffMap={"table name": [[tableColIndex, matchingCoeffVectorStartIndex, numberOfConsecutiveColumnsToMatch],...]}
durableCoeffMap={"computedValues" : [[0,0,4]],
                 "Persons" : [[4,4,1]]                                            
                 }

transientCoeffMap={
"Persons" : [[6,0,5]] # hchildren, senior+nwa+adult student, workers, no cars      
} 
                   
# all data and the constants are segmented by person type; only ftw, ptw, and sen matter (all other coeffs are 0)
segmentDefinitions = [
#  friendly name     , input data ref, offset in input, range of values (order relates to coeff order in segmentCoeffMap)
 {'Name': 'Person Type', 'DataRef': 'Persons','Offset': 3, 'DataRange': [1,2,3,4,5,6,7,8]} # using ptype, not ptype2, i.e. 1=child1, 2=child2, 3=child3, 4=stud, 5=ftw, 6=ptw, 7=nwa, 8=sen
  
]

segmentCoeffMap = [
    {'Segment': 0, 'Vector': 'durable', 'Offset': 0,  # Constants
      'Coefficients':
        [ #(C1, C2, C3, stud, ftw, ptw, nwa, sen   
            [0, 0,   0,   0, 0, 0, 0, 0],  # regular workplace
            [0, 0,   0,   0,  0, 0.602, 0, 0]  # no regular workplace
        ]
    },
    {'Segment': 0, 'Vector': 'durable', 'Offset': 1,  # HH Income > $100K (not treating income as segmented)
      'Coefficients':
        [ #(C1, C2, C3, stud, ftw, ptw, nwa, sen   
            [0, 0,   0,   0, 0, 0, 0, 0],  # regular workplace
            [0, 0,   0,   0, 0, 0.47555576, 0, 0]  # no regular workplace
        ]
    },
    {'Segment': 0, 'Vector': 'durable', 'Offset': 2,  # Age 25 or older
      'Coefficients':
        [ #(C1, C2, C3, stud, ftw, ptw, nwa, sen   
            [0, 0,   0,   0, 0, 0, 0, 0],  # regular workplace
            [0, 0,   0,   0, 0.31103013, 0, 0, 0]  # no regular workplace
        ]
    },
    {'Segment': 0, 'Vector': 'durable', 'Offset': 3,  # Age 65 or older
      'Coefficients':
        [ #(C1, C2, C3, stud, ftw, ptw, nwa, sen   
            [0, 0,   0,   0, 0, 0, 0, 0],  # regular workplace
            [0, 0,   0,   0, 0.59550688, 0, 0, 0]  # no regular workplace
        ]
    }
]