####################################################################                                                                                                                                                                                           
# SchoolEscortModel.py
# Configuration script for testing School Escorting model
####################################################################                                                                                                                                                                                           

from Globals import *

instantiationType="SchoolEscortComponent"

modelComponentName="SchoolEscorting"

logitType = "NestedLogit"

parameters={
			"OperatingCostCentsPerMile":autoOpCost
            }

dataReferences = [

    {"type" : "dbffile",
     "name" : "Households",
     "filename" : cube___HOUSEHOLDS_FILE___, 
     # Column names are uppercase in this file
     "columns" : ["HHID", "HHINC5S", "HHZON", "HCHILDREN", "HCHILD1", "HCHILD2"],
     "sort": ["HHZON", "HHINC5S", "HHID"],
    },

    {"type" : "dbffile",
     "name" : "InputTours",
     "filename" : cube___DAP_TOUR_TIME_OF_DAY_CHOICE_FIRST_TOURS___,
     "columns" : ["personId", "hhId", "persTourId", "tourPurp", "personType", "age", "male", "destZoneId", "workZoneId", "hhinc5s", 
                  "wkGtCarGt0", "homeZoneId", "noStopTour", "tourCount", "arrival", "departure"],
     "sort" : ["homeZoneId", "hhinc5s", "hhid", "personType", "age", "personId"]
    },
    {"type" : "dbffile",
     "name" : "InputToursSecond",
     "filename" : cube___DAP_TOUR_TIME_OF_DAY_CHOICE_SECOND_TOURS___,
     "columns" : ["personId", "hhId", "persTourId", "tourPurp", "personType", "age", "male", "destZoneId", "workZoneId", "hhinc5s", 
                  "wkGtCarGt0", "homeZoneId", "noStopTour", "tourCount", "arrival", "departure"],
     "sort" : ["homeZoneId", "hhinc5s", "hhid", "personType", "age", "personId"]
    },

    {"type" : "dbffile",
     "name" : "Persons",
     "filename" : cube___DAILY_ACTIVITY_PATTERNS___, # file paths MUST BE RAW strings (open quote preceded by 'r')
     "columns" : ["personId",   # 0
                  "hhId",       # 1
                  "homeZoneId", # 2
                  "personType", # 3
                  "hhinc5s",    # 4 
                  "DAPId",      # 5 
                  "tourCount",  # 6
                  "age",        # 7
                  "female",		# 8
                  "wkGtCarGt0", # 9
                  ],
     "deferredLoad" : True,
      #"sort": ["hhzon", "hhinc5s", "hhid", "ptype2", "age", "personId"],
    },

    {"type" : "memory",
     "name" : "DerivedValuesByPerson",
     "columns" : ["ftw", "ptw", "senior", "MNDdap", "incLT50", ]
    },
    {"type" : "memory",
     "name" : "DerivedValuesByDirection",
     "columns" : ["tracc", "schZnMxDens", "childAge6-12", "childAge13-15"]
    },

    {"type" : "dbffile",
     "name" : "Zones",
     "filename" : cube___ZONES_FILE___, 
     "columns" : ["zoneId", "term_time", "park_cost", "mix_dens"]
    },

   {"type" : "dbffile",
     "isOutput": "true",
     "name" : "OutputTours",     
     "filename" : cube___SCHOOL_ESCORT_TOURS___, # file paths MUST BE RAW strings (preceded by 'r')
     "parameters" : [
                       [ "Person id", "personId"],
                       [ "household id", "hhId"],
                       [ "tour", "persTourId"],
                       [ "tour purpose", "tourPurp"],
                       [ "PersonType", "personType"], 
                       [ "age", "age"], 
                       [ "male", "male"], 
                       [ "DestinationZone", "destZoneId"], 
                       [ "WorkplaceZone", "workZoneId"],
                       [ "hhinc5s", "hhinc5s"], 
                       [ "wkGtCarGt0", "wkGtCarGt0"],
                       [ "homeZone", "homeZoneId"],
                       [ "nonstop tour", "noStopTour"],
                       [ "tourCount", "tourCount"],
                       [ "arrival", "arrival"],
                       [ "departure", "departure"],
                       [ "@escort person id outbound", "esPrsOutId"],
                       [ "@escort tour id outbound", "esTrOutId"],
                       [ "@escort person id inbound", "esPrsInId"],
                       [ "@escort tour id inbound", "esTrInId"],
                       [ "@number escorted outbound", "nEscOut"],  #0 for escortee, 1 for standalone (it seems), 0-N for mandatory
                       [ "@number escorted inbound", "nEscIn"],  #0 for escortee, 1 for standalone (it seems), 0-N for mandatory
                       [ "child 0-4", "child1"], 
                       [ "child 16+", "child3"], 
                       [ "any child", "child"],
                       [ "full time worker", "ftw"],
                       [ "part time worker", "ptw"],
                       [ "adult student", "student"],
                       [ "senior", "senior"]

                       # using '@' in data source name indicates this field is generated by the component, so requires some coordination with C# code
                    ]
    },
    
    {"type" : "dbffile",
     "isOutput": "true",
     "name" : "OutputStops",     
     "filename" : cube___SCHOOL_ESCORT_STOPS___, # file paths MUST BE RAW strings (preceded by 'r')
     "parameters" : [
                       [ "hh zone", "hhzon"],
                       [ "hh inc 5 segments", "hhinc5s"],
                       [ "hhid", "hhid"],
                       [ "Person id", "personId"],
                       [ "person type", "personType"],
                       [ "tour", "tourId"],
                       [ "tour purpose", "tourPurp"],
                       [ "@stop", "stopId" ],
                       [ "half tour", "halfTour"],
                       [ "@stop purpose", "purpose"],
                       [ "@destination zone", "destZone"],
                       [ "@stop time", "time" ]
                    ]
     },
     {"type" : "dbffile",
     "isOutput": "true",
     "name" : "OutputStats",     
     "filename" : cube___SCHOOL_ESCORT_SUMMARY___, # file paths MUST BE RAW strings (preceded by 'r')
     "parameters" : [ 
                     [ "outEscort%", "outMandPct"],
                     [ "inEscort%", "inMandPct" ],
                     [ "outPreSchoolNoEscort%", "outPreSchNo" ],
                     [ "outPreDriveNoEscort%", "outPreDrNo" ],
                     [ "outDriveNoEscort%", "outDriveNo" ],
                     [ "inPreSchoolNoEscort%", "inPreSchNo" ],
                     [ "inPreDriveNoEscort%", "inPreDrNo" ],
                     [ "inDriveNoEscort%", "inDriveNo" ],
                     [ "outPreSchoolCount", "oPreSch"],
                     [ "outPreDriveCount", "oPreDr"],
                     [ "outDriveCount", "oDrive"],
                     [ "inPreSchoolCount", "iPreSch"],
                     [ "inPreDriveCount", "iPreDr"],
                     [ "inDriveCount", "iDrive"],
                    ]
     },

]

from MatrixRef4Hwy4Trans import matrixReferences

########################  model structure section  ##########################

# The model is joint choice model, meaning two choice dimensions, here the outbound escorting choice for a child's school tour 
# and the inbound escorting choice.  Each alternative represents the joint choice of one option from each choice dimension.  
# There are 7 basic alternatives within each choice dimension and 7*7=49 total joint alternatives in the model.
# The seven basic alternatives are:
# 1.	Escorted by first working adult as part of a work tour of that adult
# 2.	Escorted by second working adult as part of a work tour of that adult
# 3.	Escorted by third working adult as part of a work tour of that adult
# 4.	Escorted by first eligible adult as part of a standalone escorting tour for that adult
# 5.	Escorted by second eligible adult as part of a standalone escorting tour for that adult
# 6.	Escorted by third eligible adult as part of a standalone escorting tour for that adult
# 7.	Not escorted

# Effectively 2D matrix represented as vector
#                      Outbound -->                 # Inbound --v
#                         Mand   |    SA     | Not escorted
altIntrinsicValues = [ 0,  1,  2,  3,  4,  5,  6,   # Mandatory 1
                       7,  8,  9, 10, 11, 12, 13,   # Mandatory 2
                      14, 15, 16, 17, 18, 19, 20,   # Mandatory 3
                      21, 22, 23, 24, 25, 26, 27,   # Standalone 1
                      28, 29, 30, 31, 32, 33, 34,   # Standalone 2
                      35, 36, 37, 38, 39, 40, 41,   # Standalone 3
                      42, 43, 44, 45, 46, 47, 48    # Not escorted
                     ]

# altNames: Generate rather than trying to enumerate in config file.

logitType = "NestedLogit"

nestList = [
            ["Root", 0, 1.0, [], [1, 2, 3, 4]],
            ["No Escorting", 1, 0.262, [48], []],
            ["Outbound Only", 2, 0.262, [42, 43, 44, 45, 46, 47], []],
            ["Inbound Only", 3, 0.262, [6, 13, 20, 27, 34, 41], []],
            ["Escorted Both", 4, 0.262, [ 0,  1,  2,  3,  4,  5,
                                          7,  8,  9, 10, 11, 12, 
                                         14, 15, 16, 17, 18, 19,
                                         21, 22, 23, 24, 25, 26,
                                         28, 29, 30, 31, 32, 33, 
                                         35, 36, 37, 38, 39, 40, ], []]
           ]

# There are three escorting types:  mandatory, stand-alone escort, and not escorted. 
# With two choice dimensions, there are a total of nine escorting type combinations.  
# The "not escorted on either half-tour" alternative serves as the base.
#                   # M+M      SA+M    N+M     M+SA    SA+SA   N+SA    M+N     SA+N   N+N
altSpecificConsts = [-20.49, -18, -9.13, -20.23, -16.13, -10.3, -10.83, -8.56, 0] # 

# Coefficients and corresponding mappings are divided first by outbound vs. inbound then by Mnd vs. SA
           
outboundCoeffs=[   # Mnd      SA
				[ 0.28501,  0.28501],	# 0 IFEQ(PSEX_OUT,2)  # Female
				[ 0.00000, -1.93516],	# 1 WRKGTCAR
				[ 1.53637, -0.18629],	# 2 IFEQ(PTYP_OUT,5) # FT worker
				[ 0.61419,  0.01647],	# 3 IFEQ(PTYP_OUT,6) # PT worker
				[-2.04247, -2.04247],	# 4 IFEQ(PTYP_OUT,8)*(ANY) # Senior
				[ 0.00000, -1.90239],	# 5 IFLE(PDAP_OUT,13) #Mandatory DAP
				[-1.15153, -1.15153],	# 6 IFLE(HHINC,2)*ANY
				[ 0.39633,  0.00000],	# 7 HCHILD1
				[ 0.00000,  0.36013],	# 8 HCHILD2
				[ 0.00000,  1.78423],	# 9 TACC_OUT # Transit Access		
				[ 0.42900, -0.05155],	# 10 LOG((DMXDENS)+1)*(+) # Log (1 + School Zone Mixed Use Density)
				[ 3.35288,  2.51173],	# 11 IFEQ(AGE3,2) #Child age 6-12
				[ 1.78202,  1.90650],	# 12 IFEQ(AGE3,3) #Child type 13-15					
               ]

# CoeffMap={"table name": [[tableColIndex, matchingCoeffVectorStartIndex, numberOfConsecutiveColumnsToMatch],...]}
outboundCoeffMap={ "Persons" : [[8, 0, 2]],
                   "DerivedValuesByPerson" : [[0, 2, 5]],
				   "Households" : [[4, 7, 2]],
                   "DerivedValuesByDirection" : [[0, 9, 4]]
                 }

inboundCoeffs=[   # Mnd      SA
				[ 0.52992,  0.52992],	#IFEQ(PSEX_IN,2) # Female
				[ 0.00000, -1.93516],	#WRKGTCAR
				[-0.51423, -0.18798],	#IFEQ(PTYP_IN,5) # FT worker
				[ 0.28594, -0.31178],	#IFEQ(PTYP_IN,6) # PT worker
				[-2.04247, -2.04247],	#IFEQ(PTYP_IN,8)*(ANY) # Senior
				[ 0.00000, -0.87675],	#IFLE(PDAP_IN,13) #Mandatory DAP
				[-1.15153, -1.15153],	#IFLE(HHINC,2)*ANY
				[ 0.39633,  0.00000],	#HCHILD1
				[ 0.00000,  0.36013],	#HCHILD2
				[ 0.00000,  1.13608],	#TACC_IN # Transit Access	
				[ 0.42900, -0.05155],	#LOG((DMXDENS)+1)*(+) # Log (1 + School Zone Mixed Use Density)
				[ 3.16290,  3.16290],	#IFEQ(AGE3,2)*IN #Child age 6-12
				[ 2.27911,  2.27911],	#IFEQ(AGE3,3)*IN #Child type 13-15					
              ]

inboundCoeffMap={ "Persons" : [[8, 0, 2]],
                   "DerivedValuesByPerson" : [[0, 2, 5]],
				   "Households" : [[4, 7, 2]],
                   "DerivedValuesByDirection" : [[0, 9, 4]]
                }

## A separate set of coefficients and mappings are set up for the OutIn combos, where the values must be the same in both directions
				# MndOutIn  not MndOutIn
outInCoeffs= [[ 1.29247,  1.01074],	#SAME_PER # Same person in both directions
			  [ 0.00000,  0.00000],  # Unused - need to have at least one DerivedValuesByPersons ref
			  [ 0.00000,  0.00000]  # Unused - need to have at least one DerivedValuesByDirection ref			  
			  ]

outInCoeffMap={ "Persons" : [[0, 0, 1]], 
				 "DerivedValuesByPerson" : [[0, 1, 1]],
				 "DerivedValuesByDirection" : [[0, 2, 1]] }

# Need both escort tour mode and work tour mode generalized time values

valueOfTime= [# $0-25K, $25-50K, $50-75K, $75-100K, $100K+
              [14.44, 14.44, 14.44, 14.44, 14.44], # Escort Tours
              [6.721, 8.961, 10.754, 11.948, 17.923]  # Work Tours
             ]

outOfVehicleWeight = [2.0, 2.5] # Escort and work respectively
