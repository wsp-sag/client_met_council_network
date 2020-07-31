####################################################################
# TripModeChoice.py
#   
####################################################################

from Globals import * # for numberOfZones

# the name of the corresponding class on the C# side:
# this allows for multiple scripts targeting the same component
modelComponentName="TripModeChoice"  


parameters= {
             "OperatingCostCentsPerMile": autoOpCost,
             "sharedRide2CostDivisor" : 2.0,
             "sharedRide3CostDivisor" : 3.5,
             "tripTableDataType" : "PA"  # options are "OD" and "PA"; OD is the default
             }


dataReferences = [

    # usual data references follow:

    {"type" : "dbffile",
     "name" : "HouseholdBaseData",  
     "filename" : cube___HOUSEHOLDS_FILE___, # file paths MUST BE RAW strings (open quote preceded by 'r')
     "columns" : ["hhid", 
                  "hhzon",
                  "hhsize", 
                  "hhinc5s", 
				  "hChild1",
				  "hChild2",
				  "hChild3",
                  "hh1Person"
                  ],
        "deferredLoad" : True
     #"sort" :  ["hhzon", "hhinc5s","hhid"] # original household data is sorted this way
    },

    {"type" : "dbffile",
     "dataType" : "int",
     "name" : "HouseholdModeledData",
     "filename" : cube___MODELED_HOUSEHOLDS_FILE___, 
     "columns" : [
                "hhId",         # 00
                "homeZoneId",   # 01
                "nCars",        # 02
                ],
     "deferredLoad" : True 
    },

	#new for tbi:
    {"type" : "dbffile",
     "name" : "HouseholdPassModels",  # this household data is needed only to feed to the logsum; 
     "filename" : cube___PASS_MODEL___, 
     "columns" : ["hhid", "hhzon", "mnPass", "transPass"],
     #"sort" :  ["hhzon", "hhinc5s","hhid"] # implicit sort by hhinc5 though column is not present; original household data is sorted this way
    },

    {"type" : "dbffile",
     "name" : "Persons",
     # Using this to get a list of persons sorted by zone and as a fallback lookup for person type
     "filename" : cube___PERSONS_FILE___, 
     "columns" : ["personId", # 0
                  "hhzon",    # 1
                  "ptypeDAP",   # 2
                  "gender",
                  "age"
                  ],
     "deferredLoad" : True 
    },


    {"type" : "constants",
     "name" : "OutOfVehicleFactorByTourPurpose",
     "columns" : ["school","work","university", "escort","fullyJoint", "workbased", "indNonMnd"],
     "values" : [2.0, 2.5, 2.0, 2.0, 2.0, 2.5, 2.5]
    },

    {"type" : "constants",
     "name" : "GeneralizedTimeCoeffsByTourPurpose",
     "columns" : ["school","work","university", "escort","fullyJoint", "workbased", "indNonMnd"],
     "values" : [-0.0200, -0.0088, -0.0200,     -0.0200,  -0.0428,    -0.0200,      -0.007]
    },

    {"type" : "constantsgrid",
     "name" : "DistanceCoeffsByTourPurpose",
     "columns" : ["school","work","university", "escort","fullyJoint", "workbased", "indNonMnd"],
     "rows" : ["WK", "BK"],
     "values" : [ 
                 [-1.02,  -0.57,  -1.02,  -0.615, -0.397, -1.79,  -0.841], # WK
                 [-0.718, -0.121, -0.718, -0.199, -0.276, -0.121, -0.227]  # BK
                ]
    },    
   
    {"type" : "constantsgrid",
     "name" : "CostCoeffsByIncomeAndTourPurpose",
     "rows" : ["school","work","university", "escort","fullyJoint", "workbased", "indNonMnd"],
     "columns":["hhIncLt20k","hhIncLt40k","hhInc40To70k", "hhInc70To100k", "hhIncGt100k"],
     "values" : [  #<25         <50          <75          <100         100+
                 [ -0.00280000, -0.00280000, -0.00280000, -0.00280000, -0.00280000],    # school
                 [ -0.00078364, -0.00058773, -0.00048977, -0.00044080, -0.00029386],    # work
                 [ -0.00280000, -0.00280000, -0.00280000, -0.00280000, -0.00280000],    # uni
                 [ -0.00088014, -0.00088014, -0.00088014, -0.00088014, -0.00088014],    # escort
                 [ -0.00187748, -0.00187748, -0.00187748, -0.00187748, -0.00187748],    # fully joint
                 [ -0.00098890, -0.00098890, -0.00098890, -0.00098890, -0.00098890],    # work-based
                 [ -0.00160928, -0.00130214, -0.00099380, -0.00088908, -0.00059630]    # Ind non-mand (except escort)
                 ]
    },
   
    # this represents the data from Figure 1 of H-GAC ABM - Trip Mode Choice Model final.docx
    {"type" : "constantsgrid",
     "dataType": "int",
     "name" : "AlternativeEligibilitiesByTourMode",
     "rows" : ["unused","Drive Alone","Shared Ride2","Shared Ride3","Drive Transit","Walk Transit", "Walk","Bike", "School Bus"], # rows are tour mode
     "columns":["Drive Alone","Shared Ride2","Shared Ride3","Drive Transit","Walk Transit", "Walk","Bike", "School Bus"],  #columns are trip mode eligiblity
     "values" : [#DA S2 S3 WT DT WK BK SB  
                 [0, 0, 0, 0, 0, 0, 0, 0], # unused (put here for 1-based indexing by tour mode)
                 [1, 0, 0, 0, 0, 0, 0, 0], # Drive Alone
                 [1, 1, 0, 0, 0, 1, 1, 0], # Shared Ride2
                 [1, 1, 1, 0, 0, 1, 1, 0], # Shared Ride3
                 [1, 1, 1, 1, 0, 1, 1, 1], # Walk Transit
                 [1, 1, 1, 1, 1, 1, 1, 0], # Drive Transit
                 [0, 0, 0, 0, 0, 1, 0, 0], # Walk
                 [0, 0, 0, 0, 0, 0, 1, 0], # Bike
                 [0, 1, 1, 0, 0, 1, 1, 1]  # School Bus
                 ]
    },
   

    {"type" : "dbffile",
     "name" : "Trips",     # from stop time of day
     "filename" : cube___TRIP_TIME_OF_DAY___, # file paths MUST BE RAW strings (preceded by 'r')
     "columns" : [
                    "hhzon",
                    "hhid",
                    "personId",
                    "personType",
                    "escPrsType", # none if not escort tour
                    "tourId",
                    "tourPurp",
                    "tourMode",
                    "stopId" ,
                    "halfTour",
                    "purpose",
                    "origZone",
                    "destZone",
                    "distance",
                    "origTime",
                    "destTime" 
                    ],
     "deferredLoad" : True 
     },


   {"type" : "dbffile",
     "name" : "Tours",     
     "filename" : cube___STOP_GENERATION_TOURS_HOME_BASED___, # file paths MUST BE RAW strings (preceded by 'r')
     "columns" : [
                    "personId",
                    "hhId",
                    "persTourId",
                    "tourPurp", 
                    "arrival",
                    "departure",
                    "homeZoneId",
                    "destZoneId", 
                    "noStopTour",
                    "esPrsOutId",
                    "esTrOutId",
                    "esPrsInId",
                    "esTrInId"
                    ],
     "deferredLoad" : True 
    },



    {"type" : "dbffile",
     "name" : "WorkBasedTours",     
     "filename" : cube___WORK_BASED_TOUR_TIME_OF_DAY_CHOICE___, 
     "columns" : [
                     "personId",
                     "hhId",
                     "persTourId",  
                     "tourPurp",
                     "arrival",
                     "departure",
                     "homeZoneId",
                     "destZoneId",
                     "origZoneId",
                    ]
    },


    #{"type" : "dbffile",
    # "name" : "Stops",     
    # "filename" : @___STOP_TIME_OF_DAY___@, # file paths MUST BE RAW strings (preceded by 'r')
    # "columns" : [
    #                    "hhzon",
    #                    "hhinc5s",
    #                    "hhid",
    #                    "personId",
    #                    "personType",
    #                    "tourId",
    #                    "tourPurpose",
    #                    "stopId" ,
    #                    "halfTour",
    #                    "purpose",
    #                    "destZone",  
    #                    "time"       
    #                ]
    # },

    {"type" : "dbffile",
     "name" : "FullyJointTours",
     "filename" : cube___FULLY_JOINT_TOURS___, # file paths MUST BE RAW strings (open quote preceded by 'r')
     "columns" : [
                    "person1Id", 
                    "tourId",   
                    "tourPurp", 
                    "hhId",
                    "homeZoneId",
                    "nAdults",    
                    "nChildren",
                    "xFtwInTour"
                  ],
        "deferredLoad" : True
          # "sort": ["hhzon", "hhinc5s", "hhid", "ptype2"] this is the sort as originally from PreDAPDataAssembly, and thus from output of DAP

    },


   #{"type" : "dbffile",
   #  "name" : "Tours",     
   #  "filename" : @___STOP_GENERATION_TOURS___@, # file paths MUST BE RAW strings (preceded by 'r')
   #  "columns" : [
   #                     "personId",
   #                     "hhId",
   #                     "persTourId",
   #                     "tourPurp", 
   #                     "arrival",
   #                     "departure",
   #                     "homeZoneId",
   #                     "destZoneId",
   #                    # columns specific to this input below; keep other columns in same order as for ToursWorkBased
   #                     "noStopTour",
   #                     "esPrsOutId",
   #                     "esTrOutId",
   #                     "esPrsInId",
   #                     "esTrInId",
   #                 ],
   #  },

   #{"type" : "dbffile",
   #  "name" : "ToursWorkBased",     
   #  "filename" : @___WORK_BASED_TOURS___@, # file paths MUST BE RAW strings (preceded by 'r')
   #  "columns" : [
   #                    "personId",
   #                    "hhId",
   #                    "persTourId",
   #                    "tourPurp", 
   #                    "arrival",
   #                    "departure",
   #                    "homeZoneId",
   #                    "destZoneId", 
   #                    # columns specific to this input below; keep other columns in same order as for Tours
   #                    "origZoneId",
   #                    "parentMode",
   #                    "parArrive",
   #                    "parDepart",
   #                 ],
   #  },

   #  
    {"type" : "dbffile",
     "name" : "Zones",
     "filename" : cube___ZONES_FILE___, # file paths MUST BE RAW strings (preceded by 'r')
     "columns" : [
                    "zoneId",    # 0
                    "tot_emp",   # 1
                    "term_time", # 2
                    "park_cost", # 3
                    "area",      # 4
                    "tw_acc",    # 5
					"mix_dens"   # 6
                  ]      
    },

    # for values that cannot be computed
    {"type" : "memory",
     "dataType": "int",
     "name": "derivedIntValues",
     "columns": [
        "oneTripHT",         # 00 refresh every half tour
        "isFirstTripOnHt",   # 01 refresh every trip; comes from loop; first trip time-wise on the relevant HT
        "isLastTripOnHt",    # 02 refresh every trip; comes from loop; last trip time-wise on the relevant HT
        "nPersonsOnTrip",    # 03 refresh every trip; part of trans 10 and trans 11
        "mainPType",         # 04 refresh every trip; for trans 12-18; complex determination
        "mainPMale",         # 05 refresh every trip; for trans 19
        "mainPAge",          # 06 refresh every trip; for trans 20 
        "travelSlot",        # 07 refresh every trip; for trans 21, 22: trip travel Slot 0-47 where 0=3AM (origintime for ht2, dest time for ht1)
        "prevTripPurp",      # 08 refresh every trip; for trans 23-27;  0 if no prev trip
        "tourPurp",          # 09 refresh every tour; put here because tours come from different data references
        "prevTripMode",      # 10 refresh every trip
                             
     ]
    },

    # for values that cannot be computed
    {"type" : "memory",
     "dataType": "double",
     "name": "derivedDoubleValues",
     "columns": [
        "empDensTripDest",     # 00 refresh every trip; for trans 0, calc from tot_emp/area for destination zone
		"mixDensTripDest", 	   # 01  
        # these will be mapped directly to transients
        "genAccessibilityDA",  # 02
        "genAccessibilitySR2", # 03
        "genAccessibilitySR3", # 04
        "genAccessibilityTD",  # 05
        "genAccessibilityTW",  # 06
        "genAccessibilityWK",  # 07
        "genAccessibilityBK",  # 08
        "genAccessibilitySB"   # 09      
     ]
    },

    {"type" : "computed",
     "name" :  "computedValues",
     "parameters" : [

            # intermediate values based only on derived values
            ["group3Plus", "derivedIntValues:nPersonsOnTrip > 2"],      # 00
            ["group2Plus", "derivedIntValues:nPersonsOnTrip > 1"],      # 01
            ["isNWA", "derivedIntValues:mainPType == 4"],               # 02
            ["isPTW", "derivedIntValues:mainPType == 6"],               # 03
            ["isFTW", "derivedIntValues:mainPType == 7"],               # 04
            ["isSen", "derivedIntValues:mainPType == 5"],               # 05
            ["isChild2", "derivedIntValues:mainPType == 2"],            # 06
            ["isChild3", "derivedIntValues:mainPType == 3"],            # 07
            ["adultGt35", "derivedIntValues:mainPAge > 6"],             # 08 intermediate

            # for durables:
            ["incLt50k", "HouseholdBaseData:hhinc5s < 2"],              # 09 dur 0
            ["incGt100k", "HouseholdBaseData:hhinc5s == 4"],            # 10 dur 1
            ["noCarsInHh", "HouseholdModeledData:nCars == 0"],          # 11 dur 2

			# for transients:
            ["schoolPurpose", "derivedIntValues:tourPurp == 1"],        # 12 trans 1			
            ["workPurpose", "derivedIntValues:tourPurp == 2"],          # 13 trans 2				
            ["uniPurpose", "derivedIntValues:tourPurp == 4"],           # 14 trans 3				
            ["mealPurpose", "derivedIntValues:tourPurp & 8"],           # 15 trans 4			
            ["shopPurpose", "derivedIntValues:tourPurp & 16"],          # 16 trans 5			
            ["perBusPurpose", "derivedIntValues:tourPurp & 32"],        # 17 trans 6			
            ["socRecPurpose", "derivedIntValues:tourPurp & 64"],        # 18 trans 7			
            ["nonSchEscPurpose", "derivedIntValues:tourPurp == 128"],   # 19 trans 8			
            ["schEscPurpose", "derivedIntValues:tourPurp == 129"],      # 20 trans 9			
            ["workBasedTour", "derivedIntValues:tourPurp & 512"],       # 21 trans 10		
            ["fullyJointTour", "derivedIntValues:tourPurp & 256"],      # 22 trans 11		
            ["fjGroup3Plus", ":fullyJointTour && :group3Plus"],         # 23 trans 12
            ["fjGroup2Plus", ":fullyJointTour && :group2Plus"],         # 24 trans 13

            ["NwaNotFJ", ":isNWA  &! :fullyJointTour"],                 # 25 trans 14
            ["PtwNotFJ", ":isPTW  &! :fullyJointTour"],                 # 26 trans 15
            ["FtwNotFJ", ":isFTW  &! :fullyJointTour"],                 # 27 trans 16			
            ["SenNotFJ", ":isSen  &! :fullyJointTour"],                 # 28 trans 17
            ["C2NotFJ", ":isChild2 &! :fullyJointTour"],                # 29 trans 18
            ["C3NotFJ", ":isChild3 &! :fullyJointTour"],                # 30 trans 19
            ["maleNotFJ", "derivedIntValues:mainPMale &! :fullyJointTour"],         # 31 trans 20
            ["adultGt35NotFJ", ":adultGt35 &! :fullyJointTour"],             # 32 trans 21                       

			["escortTrip", "Trips:purpose & 128"],                      # 33 trans 22
            ["prevTripEscort", "derivedIntValues:prevTripPurp & 128"],  # 34 trans 23
            ["prevTripS3", "derivedIntValues:prevTripMode == 3"],       # 35 intermediate
            ["prevS3Escort", ":prevTripEscort && :prevTripS3"],         # 36 intermediate
            ["travel3AMtoNoon", "derivedIntValues:travelSlot < 18"],    # 37 intermediate			
            ["prevS3EscAM", ":prevS3Escort && :travel3AMtoNoon"],       # 38 trans 24
            ["prevS3EscPostAM", ":prevS3Escort &! :travel3AMtoNoon"],   # 39 trans 25
			
            ["ht1", "Trips:halfTour == 1"],                             # 40 yes, halfTour= 1 means ht1
            ["ht2", "Trips:halfTour == 2"],                             # 41 yes, halfTour= 1 means ht1

            # used in transients to follow
            ["isHt1AndOnlyTrip", ":ht1 && derivedIntValues:oneTripHT"],                       # 42 outbound half tour, 1 trip on ht
            ["isHt2AndOnlyTrip", ":ht2 && derivedIntValues:oneTripHT"],                       # 43 inbound half tour, 1 trip on ht
            ["isHt1AndMultiTrip", ":ht1 AndNot derivedIntValues:oneTripHT"],                  # 44
            ["firstTripMultiHt1",  ":isHt1AndMultiTrip && derivedIntValues:isFirstTripOnHt"], # 45
            ["lastTripMultiHt1",  ":isHt1AndMultiTrip && derivedIntValues:isLastTripOnHt"],   # 46
            ["isHt2AndMultiTrip", ":ht2 AndNot derivedIntValues:oneTripHT"],                  # 47
            ["firstTripMultiHt2",  ":isHt2AndMultiTrip && derivedIntValues:isFirstTripOnHt"], # 48
            ["lastTripMultiHt2",  ":isHt2AndMultiTrip && derivedIntValues:isLastTripOnHt"],   # 49

            ["modeDA", "Trips:tourMode == 1"],                   # 50 mode values are from TourMode enumeration                                                                 
            ["modeSR2", "Trips:tourMode == 2"],                  # 51 trans 27
            ["modeSR3", "Trips:tourMode == 3"],                  # 52 trans 28
            ["modeTW", "Trips:tourMode == 4"],                   # 53 trans 29
            ["modeTD", "Trips:tourMode == 5"],                   # 54 trans 30
            ["modeWK", "Trips:tourMode == 6"],                   # 55 trans 31
            ["modeBK", "Trips:tourMode == 7"],                   # 56 trans 32
            ["modeSB", "Trips:tourMode == 8"],                   # 57 trans 33
            ["DAOnlyTripHt1", ":modeDA && :isHt1AndOnlyTrip"],   # 58 trans 34
            ["SR2OnlyTripHt1", ":modeSR2 && :isHt1AndOnlyTrip"], # 59 trans 35
            ["SR3OnlyTripHt1", ":modeSR3 && :isHt1AndOnlyTrip"], # 60 trans 36
            ["TWOnlyTripHt1", ":modeTW && :isHt1AndOnlyTrip"],   # 61 trans 37
            ["TDOnlyTripHt1", ":modeTD && :isHt1AndOnlyTrip"],   # 62 trans 38
            ["WKOnlyTripHt1", ":modeWK && :isHt1AndOnlyTrip"],   # 63 trans 39
            ["BKOnlyTripHt1", ":modeBK && :isHt1AndOnlyTrip"],   # 64 trans 40
            ["SBOnlyTripHt1", ":modeSB && :isHt1AndOnlyTrip"],   # 65 trans 41
            ["DAOnlyTripHt2", ":modeDA && :isHt2AndOnlyTrip"],   # 66 trans 42
            ["SR2OnlyTripHt2", ":modeSR2 && :isHt2AndOnlyTrip"], # 67 trans 43
            ["SR3OnlyTripHt2", ":modeSR3 && :isHt2AndOnlyTrip"], # 68 trans 44
            ["TWOnlyTripHt2", ":modeTW && :isHt2AndOnlyTrip"],   # 69 trans 45
            ["TDOnlyTripHt2", ":modeTD && :isHt2AndOnlyTrip"],   # 70 trans 46
            ["WKOnlyTripHt2", ":modeWK && :isHt2AndOnlyTrip"],   # 71 trans 47
            ["BKOnlyTripHt2", ":modeBK && :isHt2AndOnlyTrip"],   # 72 trans 48
            ["SBOnlyTripHt2", ":modeSB && :isHt2AndOnlyTrip"],   # 73 trans 49
            
            ["DAFirstOfMultiHt1", ":firstTripMultiHt1 && :modeDA"],  #  74 trans 50
            ["SR2FirstOfMultiHt1", ":firstTripMultiHt1 && :modeSR2"],#  75 trans 51
            ["SR3FirstOfMultiHt1", ":firstTripMultiHt1 && :modeSR3"],#  76 trans 52
            ["TWFirstOfMultiHt1", ":firstTripMultiHt1 && :modeTW"],  #  77 trans 53
            ["TDFirstOfMultiHt1", ":firstTripMultiHt1 && :modeTD"],  #  78 trans 54
            ["WKFirstOfMultiHt1", ":firstTripMultiHt1 && :modeWK"],  #  79 trans 55
            ["BKFirstOfMultiHt1", ":firstTripMultiHt1 && :modeBK"],  #  80 trans 56       
			
            ["DALastOfMultiHt1", ":lastTripMultiHt1 && :modeDA"],    #  81 trans 57
            ["SR2LastOfMultiHt1", ":lastTripMultiHt1 && :modeSR2"],  #  82 trans 58
            ["SR3LastOfMultiHt1", ":lastTripMultiHt1 && :modeSR3"],  #  83 trans 59
            ["TWLastOfMultiHt1", ":lastTripMultiHt1 && :modeTW"],    #  84 trans 60
            ["TDLastOfMultiHt1", ":lastTripMultiHt1 && :modeTD"],    #  85 trans 61
            ["WKLastOfMultiHt1", ":lastTripMultiHt1 && :modeWK"],    #  86 trans 62
            ["BKLastOfMultiHt1", ":lastTripMultiHt1 && :modeBK"],    #  87 trans 63
			
            ["DAFirstOfMultiHt2", ":firstTripMultiHt2 && :modeDA"],  #  88 trans 64
            ["SR2FirstOfMultiHt2", ":firstTripMultiHt2 && :modeSR2"],#  89 trans 65
            ["SR3FirstOfMultiHt2", ":firstTripMultiHt2 && :modeSR3"],#  90 trans 66
            ["TWFirstOfMultiHt2", ":firstTripMultiHt2 && :modeTW"],  #  91 trans 67
            ["TDFirstOfMultiHt2", ":firstTripMultiHt2 && :modeTD"],  #  92 trans 68
            ["WKFirstOfMultiHt2", ":firstTripMultiHt2 && :modeWK"],  #  93 trans 69
            ["BKFirstOfMultiHt2", ":firstTripMultiHt2 && :modeBK"],  #  94 trans 70
			
            ["DALastOfMultiHt2", ":lastTripMultiHt2 && :modeDA"],    #  95 trans 71
            ["SR2LastOfMultiHt2", ":lastTripMultiHt2 && :modeSR2"],  #  96 trans 72
            ["SR3LastOfMultiHt2", ":lastTripMultiHt2 && :modeSR3"],  #  97 trans 73
            ["TWLastOfMultiHt2", ":lastTripMultiHt2 && :modeTW"],    #  98 trans 74
            ["TDLastOfMultiHt2", ":lastTripMultiHt2 && :modeTD"],    #  99 trans 75
            ["WKLastOfMultiHt2", ":lastTripMultiHt2 && :modeWK"],    # 100 trans 76
            ["BKLastOfMultiHt2", ":lastTripMultiHt2 && :modeBK"],    # 101 trans 77

      ]
     },

    {"type" : "dbffile",
     "isOutput": "true",
     "name" : "OutputTrips",     
     "filename" : cube___TRIPS_WITH_MODES___, # file paths MUST BE RAW strings (preceded by 'r')
     "parameters" : [
                       [ "hh zone", "hhzon"],
                       [ "hhid", "hhid"],
                       [ "Person id", "personId"],
                       [ "Person Type", "personType"],
                       [ "person type if escorted", "escPrsType"],
                       [ "tour", "tourId"],
                       [ "tour purpose", "tourPurp"],
                       [ "tour mode", "tourMode"],
                       [ "stop id", "stopId" ],
                       [ "half tour number", "halfTour"],
                       [ "stop purpose", "purpose"],
                       [ "origin zone", "origZone"],
                       [ "destination zone", "destZone"],
                       [ "origin time", "origTime"],
                       [ "distance", "distance"],
                       [ "destination time", "destTime" ],
                       [ "@trip mode", "tripMode"]
                    ]
     },

    # dbf output spec; used in tests for inspecting whether results are reasonable
    {"type" : "delimited",
     "isOutput": "true",
     "name" : "OutputDestinationChoiceStats",     
     "filename" : cube___STOP_DESTINATION_CHOICE_SUMMARY___, # file paths MUST BE RAW strings (preceded by 'r')             
     "parameters" : [
                       [ "StatLine", "AggregateData"],
                    ]
    }

]

# Matrices are different enough to require their own structure:
from MatrixRef4Hwy4Trans import *;


# Names identify trip table segments - segments MUST be mutually exclusive and collectively exhaustive
# At the moment it is assumed that drive modes are always specified explicitly and are not grouped;  this could be changed if desired
# To identify all purpose, income, and/or transponder categories, "All" may be used.  
# Any Trailing 'ALL's do not need to be specified, e.g.:
#   DriveAlone = DriveAlone_All_All_ALL
#   Similarly, DriveAlone_Work == DriveAlone_Work_All_All
#   and DriveAlone_Work_Inc1 == DriveAlone_Work_Inc1_ALL

# use local variable to make sure matrix names are the same for each highwy matrix
highwayMatrixNames = ["DriveAlone_Work_Inc1_XP", "DriveAlone_Work_Inc2_XP", "DriveAlone_Work_Inc3_XP", "DriveAlone_Work_Inc4_XP", "DriveAlone_Work_Inc5_XP", 
	 "SharedRide2_Work_Inc1", "SharedRide2_Work_Inc2", "SharedRide2_Work_Inc3", "SharedRide2_Work_Inc4", "SharedRide2_Work_Inc5",
	 "SharedRide3_Work_Inc1", "SharedRide3_Work_Inc2", "SharedRide3_Work_Inc3", "SharedRide3_Work_Inc4", "SharedRide3_Work_Inc5",
	 "DriveAlone_NonWork_Inc1_XP", "DriveAlone_NonWork_Inc2_XP", "DriveAlone_NonWork_Inc3_XP", "DriveAlone_NonWork_Inc4_XP", "DriveAlone_NonWork_Inc5_XP",
	 "SharedRide2_NonWork_Inc1", "SharedRide2_NonWork_Inc2", "SharedRide2_NonWork_Inc3", "SharedRide2_NonWork_Inc4", "SharedRide2_NonWork_Inc5",
	 "SharedRide3_NonWork_Inc1", "SharedRide3_NonWork_Inc2", "SharedRide3_NonWork_Inc3", "SharedRide3_NonWork_Inc4", "SharedRide3_NonWork_Inc5",
	 "DriveAlone_All_Inc1_NoXP", "DriveAlone_All_Inc2345_NoXP"]

matrixWriterReferences = [
    {"type" : "matrixWriter",
     "name" : "AM1",
     "isHighwayTimeSpanMatrix" : "true",
     "startTime" : "6", #6:00 am
     "endTime" : "6.5",  # 6.5 for an endTime means that this matrix includes up to the instant before 7:00AM (6:59:59.999...)
     "matrixNames" : highwayMatrixNames,
     "zones" : numberOfZones,
     "filename" : AM1___TRIP_TABLE_MATRIX___,
    },
    {"type" : "matrixWriter",
     "name" : "AM2",
     "isHighwayTimeSpanMatrix" : "true",
     "startTime" : "7", #7:00 am
     "endTime" : "7.5",  # 7.5 for an endTime means that this matrix includes up to the instant before 8:00AM (8:59:59.999...)
     "matrixNames" : highwayMatrixNames,
     "zones" : numberOfZones,
     "filename" : AM2___TRIP_TABLE_MATRIX___,
    },
	{"type" : "matrixWriter",
     "name" : "AM3",
     "isHighwayTimeSpanMatrix" : "true",
     "startTime" : "8", #8:00 am
     "endTime" : "8.5",  # 6.5 for an endTime means that this matrix includes up to the instant before 9:00AM (9:59:59.999...)
     "matrixNames" : highwayMatrixNames,
     "zones" : numberOfZones,
     "filename" : AM3___TRIP_TABLE_MATRIX___,
    },
	{"type" : "matrixWriter",
     "name" : "AM4",
     "isHighwayTimeSpanMatrix" : "true",
     "startTime" : "9", #9:00 am
     "endTime" : "9.5",  # 9.5 for an endTime means that this matrix includes up to the instant before 10:00AM (9:59:59.999...)
     "matrixNames" : highwayMatrixNames,
     "zones" : numberOfZones,
     "filename" : AM4___TRIP_TABLE_MATRIX___,
    },	
    {"type" : "matrixWriter",
     "name" : "MD",
     "isHighwayTimeSpanMatrix" : "true",
     "startTime" : "10", #10:00 am
     "endTime" : "14.5", # ends at instant before 15:00
     "matrixNames" : highwayMatrixNames,
     "zones" : numberOfZones,
     "filename" : MD___TRIP_TABLE_MATRIX___,
    },
    {"type" : "matrixWriter",
     "name" : "PM1",
     "isHighwayTimeSpanMatrix" : "true",
     "startTime" : "15", 
     "endTime" : "15.5", # ends at instant before 16:00
     "matrixNames" : highwayMatrixNames,
     "zones" : numberOfZones,
     "filename" : PM1___TRIP_TABLE_MATRIX___,
    },
    {"type" : "matrixWriter",
     "name" : "PM2",
     "isHighwayTimeSpanMatrix" : "true",
     "startTime" : "16", 
     "endTime" : "16.5", # ends at instant before 17:00
     "matrixNames" : highwayMatrixNames,
     "zones" : numberOfZones,
     "filename" : PM2___TRIP_TABLE_MATRIX___,
    },
    {"type" : "matrixWriter",
     "name" : "PM3",
     "isHighwayTimeSpanMatrix" : "true",
     "startTime" : "17", 
     "endTime" : "17.5", # ends at instant before 18:00
     "matrixNames" : highwayMatrixNames,
     "zones" : numberOfZones,
     "filename" : PM3___TRIP_TABLE_MATRIX___,
    },
    {"type" : "matrixWriter",
     "name" : "PM4",
     "isHighwayTimeSpanMatrix" : "true",
     "startTime" : "18", 
     "endTime" : "18.5", # ends at instant before 19:00
     "matrixNames" : highwayMatrixNames,
     "zones" : numberOfZones,
     "filename" : PM4___TRIP_TABLE_MATRIX___,
    },	
    {"type" : "matrixWriter",
     "name" : "EV",
     "isHighwayTimeSpanMatrix" : "true",
     "startTime" : "19", #7:00 pm
     "endTime" : "23.5",  # wrap around midnight is OK; ends at instant before 12:00 AM
     "matrixNames" : highwayMatrixNames,
     "zones" : numberOfZones,
     "filename" : EV___TRIP_TABLE_MATRIX___,
    },
    {"type" : "matrixWriter",
     "name" : "NT",
     "isHighwayTimeSpanMatrix" : "true",
     "startTime" : "0", #12:00 am
     "endTime" : "5.5",  # ends at instant before 6:00 AM
     "matrixNames" : highwayMatrixNames,
     "zones" : numberOfZones,
     "filename" : NT___TRIP_TABLE_MATRIX___,
    },	
    {"type" : "matrixWriter",
     "name" : "PeakTransit",
     "matrixNames" : [ "WalkToTransit", "DriveToTransit" ],
     "zones" : numberOfZones,
     "filename" : PeakTransit___TRIP_TABLE_MATRIX___,
    },
    {"type" : "matrixWriter",
     "name" : "OffPeakTransit",
     "matrixNames" : [ "WalkToTransit", "DriveToTransit" ],
     "zones" : numberOfZones,
     "filename" : OffPeakTransit___TRIP_TABLE_MATRIX___,
    },
     
    ]

# ######################  model structure section  ##########################

# this is meant to represent the alternative output as either:
#    a real world value (e.g. that can be used in downstream utility functions 
#    or an ID of the alternative; 

# Values are those of C# TourMode enum
altIntrinsicValues= [1,2,3,4,5,6,7,8]

# friendly descriptions of the alternatives, for config file readability and maybe for UI display somehow
altNames = ["Drive Alone","Shared Ride2","Shared Ride3","Walk Transit","Drive Transit", "Walk","Bike", "School Bus"]
					# DA,        # S2,        # S3,        # TW,        # TD,         # WK,        # BK        # SB
#altSpecificConsts = [  0.00000000, -1.51655842, -2.15274111, -1.97235335, -1.92685937,  4.31695165,  0.41488296,  0.40510575]
#altSpecificConsts = [  0.00000000, -1.51655842, -2.15274111, -2.08535335, -1.92685937,  4.31695165,  0.41488296,  0.40510575]
#altSpecificConsts = [  0.00000000, -1.51655842, -2.15274111, -2.98535335, -1.92685937,  4.31695165,  0.41488296,  0.40510575]
#altSpecificConsts = [  0.00000000, -1.51655842, -2.15274111, -3.48535335, -1.92685937,  4.31695165,  0.41488296,  0.40510575]
#altSpecificConsts = [  0.00000000, -1.51655842, -2.15274111, -3.48535335, -0.92685937,  4.31695165,  0.41488296,  0.40510575]
#altSpecificConsts = [  0.00000000, -1.51655842, -2.15274111, -3.73535335, -0.42685937,  4.31695165,  0.41488296,  0.40510575]
#altSpecificConsts = [  0.00000000, -1.51655842, -2.15274111, -3.73535335,  0.57314063,  4.31695165,  0.41488296,  0.40510575]
#altSpecificConsts = [  0.00000000, -1.51655842, -2.15274111, -3.73535335,  0.32314063,  4.31695165,  0.41488296,  0.40510575] #5/1/15
#altSpecificConsts = [  0.00000000, -1.51655842, -2.15274111, -1.97235335, -0.92685937,  4.31695165,  0.41488296,  0.40510575] #5/25/15
#altSpecificConsts = [  0.00000000, -1.51655842, -2.15274111, -3.23535335, -1.67685937,  4.31695165,  0.41488296,  0.40510575] #5/25/15 
#altSpecificConsts = [  0.00000000, -1.51655842, -2.15274111, -3.28535335, -1.87685937,  4.31695165,  0.41488296,  0.40510575] #5/26/15 
#altSpecificConsts = [  0.00000000, -1.51655842, -2.15274111, -3.73535335,  0.32314063,  4.31695165,  0.41488296,  0.40510575] #6/1/15
#altSpecificConsts = [  0.00000000, -1.51655842, -2.15274111, -4.53535335,  0.57314063,  4.31695165,  0.41488296,  0.40510575] #6/2/15
#altSpecificConsts = [  0.00000000, -1.51655842, -2.15274111, -4.43535335,  0.97314063,  4.31695165,  0.41488296,  0.40510575] #6/2/15
altSpecificConsts = [  0.00000000, -1.51655842, -2.15274111, -5.76596,  0.681198,  4.31695165,  0.41488296,  0.40510575] #5/18/16
#altSpecificConsts = [  0.00000000, -1.51655842, -2.15274111, -3.76596,  0.681198,  4.31695165,  0.41488296,  0.40510575] #12/22/16

logitType = "MultinomialLogit"

durableCoeffs=[

 # DA,        # S2,        # S3,        # TW,        # TD,         # WK,        # BK        # SB,       
[  0.00000000,  0.00000000,  0.00000000,  1.31975138,  1.55159114,  0.00000000,  0.87989184,  0.00000000], # 0 incle50 # HH Income less than $50K
[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000, -0.25891077], # 1 inc100 # High Income (> $100K)
[  0.00000000,  2.37288163,  2.79381769,  2.55950516,  0.00000000,  3.34964500,  0.00000000,  4.91869815], # 2 zeroveh # No car in household
[  0.06266490,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 3 hhveh # HH Vehicles
[  0.00000000, -0.17482788,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 4 ifeq(hhsize,1) # 1 person household 
]

# Mapping is being done internal to model.
durableCoeffMap={
    "computedValues" : [
                        [ 9, 0, 3], #incLt50k, incGt100k, noCarsInHh
                      ],
    "HouseholdModeledData": [
                        [ 2, 3, 1], # nCars
                      ],
    "HouseholdBaseData": [
                        [ 7, 4, 1], # hh1Person
                      ],                                  
} 


transientCoeffs=[                 
 # DA,        # S2,        # S3,        # TW,        # TD,         # WK,        # BK        # SB,    
[  -0.0000500, -0.00005000, -0.00005000,  0.00013224,  0.00014324,  0.00000000,  0.00000000,  0.00000000], # 0 stpmxdens # Mixed density at destination 
# tour purpose variables
[  0.00000000,  0.67471310,  2.49098811,  0.00000000,  0.00000000,  0.68357554,  0.00000000,  0.00000000], # 1 ifeq(TourPurp,3) # Tour purpose:School
[  0.00000000,  0.08315951,  0.15256858,  0.50000000, -0.37374014,  0.00000000,  0.00000000,  0.00000000], # 2 ifeq(TourPurp,2) # Tour purpose:Work Related
[  0.00000000,  0.57017613,  0.70900732,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 3 ifeq(TourPurp,4) # Tour purpose:University ####
[  0.00000000,  1.20844730,  3.18831402,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 4 ifeq(TourPurp,7) # Tour purpose:Meal
[  0.00000000,  0.82106977,  1.99876469,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 5 ifeq(TourPurp,6) # Tour purpose:Shop 
[  0.00000000,  1.09513030,  1.87947066,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 6 ifeq(TourPurp,5) # Tour purpose:PersBus
[  0.00000000,  1.17132523,  2.33190094,  1.38697642,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 7 ifeq(TourPurp,8) # Tour purpose:SocRec 
[  0.00000000,  0.00000000,  0.75655435,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 8 (ifeq(TourPurp,9)*ifeq(nseep1+nseep2,0)) # Tour type: Non-School Escort
[  0.00000000,  0.13994314,  0.72034643,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 9 (ifeq(TourPurp,9)*ifgt(nseep1+nseep2,0)) # Tour purpose:School Escort
[  0.00000000,  0.86785184,  1.21297637,  0.00000000,  0.00000000,  1.18589202,  0.00000000,  0.00000000], # 10 ifeq(iwbased,1) # Tour type: Work Based
[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000, -1.24924490,  0.00000000,  0.00000000], # 11 ifeq(isFJnt,1) # Tour type: fully joint
[  0.00000000,  0.83545775,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 12 ifge(fjsize,1) # Fully joint group >= 2
[  0.00000000,  0.00000000,  1.58527444,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 13 ifge(fjsize,2) # Fully joint group >= 3
# person type variables
[  0.00000000, -0.20625060, -0.20625060,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 14 ifeq(ptype,7) # Non-worker 
[  0.00000000,  0.00000000,  0.00000000, -0.45031089,  0.00000000, -0.59783273,  0.00000000,  0.00000000], # 15 ifeq(ptype,6) # Part time worker 
[  0.00000000,  0.00000000,  0.00000000, -0.45031089,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 16 ifeq(ptype,5) # Full Time worker
[  0.00000000,  0.12911997,  0.12911997,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 17 ifeq(ptype,8) # Senior
[  0.00000000,  0.00000000, -0.07424855,  0.00000000,  0.00000000,  0.93537080,  1.10477738,  0.34973814], # 18 hchild2 # Child Type 2
[  0.00000000,  0.00000000, -0.07424855,  0.00000000,  0.00000000,  0.93537080,  1.10477738,  0.00000000], # 19 hchild3 # Child Type 3
[  0.00000000,  0.05925361,  0.05925361,  0.00000000,  0.00000000,  0.00000000,  1.21731066,  0.00000000], # 20 male #  
[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000, -1.01535251,  0.00000000], # 21 agegr35 # Adult age > 35
 # escort trip purpose 
[  0.00000000,  3.09252936,  3.09252936,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 22 ifeq(stpurp,9) # Escort Trip purpose
[  2.62820053,  2.85731662,  2.85731662,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 23 (ifeq(prevpurp,9)) # Previous trip purpose: escort
[  0.00000000,  0.56343338,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 24 (ifeq(prevpurp,9)*ifeq(prevmode,3)*ifin(time_per,1,19)) # Previous trip purpose: escort, Previous trip mode S3, 3AM-12PM
[  0.00000000,  0.82262836,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 25 (ifeq(prevpurp,9)*ifeq(prevmode,3)*ifin(time_per,20,48)) # Previous trip purpose: escort, Previous trip mode S3, 12PM-3AM
# previous mode
[  7.93894704,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 26 ifeq(remode,1) # Tour mode: DA
[  6.33673002,  7.93894704,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 27 ifeq(remode,2) # Tour mode: S2
[  5.11444219,  5.35743748,  7.93894704,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 28 ifeq(remode,3) # Tour mode: S3
[  2.42544346,  2.52174350,  3.55524033,  9.93894704,  0.00000000, -0.50000000,  0.00000000,  0.00000000], # 29 ifeq(remode,4) # Tour mode: TW
[  2.81516836,  3.25676485,  4.54792993,  6.18955594,  7.93894704,  0.00000000,  0.00000000,  0.00000000], # 30 ifeq(remode,5) # Tour mode: TD
[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  7.93894704,  0.00000000,  0.00000000], # 31 ifeq(remode,8) # Tour mode: WK
[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  7.93894704,  0.00000000], # 32 ifeq(remode,7) # Tour mode: BK
[  0.00000000,  3.01024266,  6.12760986,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  7.93894704], # 33 ifeq(remode,6) # Tour mode: SB
# Tour Mode: outbound half tour, 1 trip on halftour 
[  0.19598916,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 34 (ifeq(remode,1)*stp_11*iflt(stpno,0)) # Tour mode: DA; outbound half tour, 1 trip on halftour 
[  0.00000000,  0.19598916,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 35 (ifeq(remode,2)*stp_11*iflt(stpno,0)) # Tour mode: S2; outbound half tour, 1 trip on halftour 
[  0.00000000,  0.00000000,  0.19598916,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 36 (ifeq(remode,3)*stp_11*iflt(stpno,0)) # Tour mode: S3; outbound half tour, 1 trip on halftour 
[  0.00000000,  0.00000000,  0.00000000,  0.19598916,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 37 (ifeq(remode,4)*stp_11*iflt(stpno,0)) # Tour mode: TW; outbound half tour, 1 trip on halftour 
[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.19598916,  0.00000000,  0.00000000,  0.00000000], # 38 (ifeq(remode,5)*stp_11*iflt(stpno,0)) # Tour mode: TD; outbound half tour, 1 trip on halftour 
[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.19598916,  0.00000000,  0.00000000], # 39 (ifeq(remode,8)*stp_11*iflt(stpno,0)) # Tour mode: WK; outbound half tour, 1 trip on halftour 
[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.19598916,  0.00000000], # 40 (ifeq(remode,7)*stp_11*iflt(stpno,0)) # Tour mode: BK; outbound half tour, 1 trip on halftour 
[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.19598916], # 41 # Tour mode: SB; outbound half tour, 1 trip on halftour 
# Tour Mode: inbound half tour, 1 trip on halftour 
[  0.23128905,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 42 (ifeq(remode,1)*stp_21*ifgt(stpno,0)) # Tour mode: DA; inbound half tour,  1 trip on halftour 
[  0.00000000,  0.23128905,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 43 (ifeq(remode,2)*stp_21*ifgt(stpno,0)) # Tour mode: S2; inbound half tour,  1 trip on halftour 
[  0.00000000,  0.00000000,  0.23128905,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 44 (ifeq(remode,3)*stp_21*ifgt(stpno,0)) # Tour mode: S3; inbound half tour,  1 trip on halftour 
[  0.00000000,  0.00000000,  0.00000000,  0.23128905,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 45 (ifeq(remode,4)*stp_21*ifgt(stpno,0)) # Tour mode: TW; inbound half tour,  1 trip on halftour 
[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.23128905,  0.00000000,  0.00000000,  0.00000000], # 46 (ifeq(remode,5)*stp_21*ifgt(stpno,0)) # Tour mode: TD; inbound half tour,  1 trip on halftour 
[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.23128905,  0.00000000,  0.00000000], # 47 (ifeq(remode,8)*stp_21*ifgt(stpno,0)) # Tour mode: WK; inbound half tour,  1 trip on halftour 
[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.23128905,  0.00000000], # 48 (ifeq(remode,7)*stp_21*ifgt(stpno,0)) # Tour mode: BK; inbound half tour,  1 trip on halftour 
[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.23128905], # 49 # Tour mode: SB; inbound half tour,  1 trip on halftour 
# Tour Mode: outbound half tour, >1 trip on halftour, first trip of halftour 
[ -0.30747684,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 50 (stp_outg1*ifeq(remode,1)*fr_out) # Tour mode: DA; outbound half tour, >1 trip on halftour, first trip of halftour 
[  0.00000000, -0.30747684,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 51 (stp_outg1*ifeq(remode,2)*fr_out) # Tour mode: S2; outbound half tour, >1 trip on halftour, first trip of halftour 
[  0.00000000,  0.00000000, -0.30747684,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 52 (stp_outg1*ifeq(remode,3)*fr_out) # Tour mode: S3; outbound half tour, >1 trip on halftour, first trip of halftour 
[  0.00000000,  0.00000000,  0.00000000, -0.30747684,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 53 (stp_outg1*ifeq(remode,4)*fr_out) # Tour mode: TW; outbound half tour, >1 trip on halftour, first trip of halftour 
[  0.00000000,  0.00000000,  0.00000000,  0.00000000, -0.30747684,  0.00000000,  0.00000000,  0.00000000], # 54 (stp_outg1*ifeq(remode,5)*fr_out) # Tour mode: TD; outbound half tour, >1 trip on halftour, first trip of halftour 
[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000, -0.30747684,  0.00000000,  0.00000000], # 55 (stp_outg1*ifeq(remode,8)*fr_out) # Tour mode: WK; outbound half tour, >1 trip on halftour, first trip of halftour 
[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000, -0.30747684,  0.00000000], # 56 (stp_outg1*ifeq(remode,7)*fr_out) # Tour mode: BK; outbound half tour, >1 trip on halftour, first trip of halftour 
# Tour Mode: outbound half tour, >1 trip on halftour, last trip of halftour
[ -0.88715218,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 57 (stp_outg1*ifeq(remode,1)*last_out) # Tour mode: DA; outbound half tour, >1 trip on halftour, last trip of halftour 
[  0.00000000, -0.88715218,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 58 (stp_outg1*ifeq(remode,2)*last_out) # Tour mode: S2; outbound half tour, >1 trip on halftour, last trip of halftour 
[  0.00000000,  0.00000000, -0.88715218,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 59 (stp_outg1*ifeq(remode,3)*last_out) # Tour mode: S3; outbound half tour, >1 trip on halftour, last trip of halftour 
[  0.00000000,  0.00000000,  0.00000000, -0.88715218,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 60 (stp_outg1*ifeq(remode,4)*last_out) # Tour mode: TW; outbound half tour, >1 trip on halftour, last trip of halftour 
[  0.00000000,  0.00000000,  0.00000000,  0.00000000, -0.88715218,  0.00000000,  0.00000000,  0.00000000], # 61 (stp_outg1*ifeq(remode,5)*last_out) # Tour mode: TD; outbound half tour, >1 trip on halftour, last trip of halftour 
[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000, -0.88715218,  0.00000000,  0.00000000], # 62 (stp_outg1*ifeq(remode,8)*last_out) # Tour mode: WK; outbound half tour, >1 trip on halftour, last trip of halftour 
[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000, -0.88715218,  0.00000000], # 63 (stp_outg1*ifeq(remode,7)*last_out) # Tour mode: BK; outbound half tour, >1 trip on halftour, last trip of halftour 
# Tour Mode: inbound half tour,  >1 trip on halftour, first trip of halftour
[  0.13493125,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 64 (stp_ing1*ifeq(remode,1)*fr_in) # Tour mode: DA; inbound half tour,  >1 trip on halftour, first trip of halftour
[  0.00000000,  0.13493125,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 65 (stp_ing1*ifeq(remode,2)*fr_in) # Tour mode: S2; inbound half tour,  >1 trip on halftour, first trip of halftour
[  0.00000000,  0.00000000,  0.13493125,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 66 (stp_ing1*ifeq(remode,3)*fr_in) # Tour mode: S3; inbound half tour,  >1 trip on halftour, first trip of halftour
[  0.00000000,  0.00000000,  0.00000000,  0.13493125,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 67 (stp_ing1*ifeq(remode,4)*fr_in) # Tour mode: TW; inbound half tour,  >1 trip on halftour, first trip of halftour
[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.13493125,  0.00000000,  0.00000000,  0.00000000], # 68 (stp_ing1*ifeq(remode,5)*fr_in) # Tour mode: TD; inbound half tour,  >1 trip on halftour, first trip of halftour
[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.13493125,  0.00000000,  0.00000000], # 69 (stp_ing1*ifeq(remode,8)*fr_in) # Tour mode: WK; inbound half tour,  >1 trip on halftour, first trip of halftour
[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.13493125,  0.00000000], # 70 (stp_ing1*ifeq(remode,7)*fr_in) # Tour mode: BK; inbound half tour,  >1 trip on halftour, first trip of halftour
# Tour Mode: inbound half tour,  >1 trip on halftour, last trip of halftour
[ -0.59216242,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 71 (stp_ing1*ifeq(remode,1)*last_in) # Tour mode: DA; inbound half tour,  >1 trip on halftour, last trip of halftour
[  0.00000000, -0.59216242,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 72 (stp_ing1*ifeq(remode,2)*last_in) # Tour mode: S2; inbound half tour,  >1 trip on halftour, last trip of halftour
[  0.00000000,  0.00000000, -0.59216242,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 73 (stp_ing1*ifeq(remode,3)*last_in) # Tour mode: S3; inbound half tour,  >1 trip on halftour, last trip of halftour
[  0.00000000,  0.00000000,  0.00000000, -0.59216242,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 74 (stp_ing1*ifeq(remode,4)*last_in) # Tour mode: TW; inbound half tour,  >1 trip on halftour, last trip of halftour
[  0.00000000,  0.00000000,  0.00000000,  0.00000000, -0.59216242,  0.00000000,  0.00000000,  0.00000000], # 75 (stp_ing1*ifeq(remode,5)*last_in) # Tour mode: TD; inbound half tour,  >1 trip on halftour, last trip of halftour
[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000, -0.59216242,  0.00000000,  0.00000000], # 76 (stp_ing1*ifeq(remode,8)*last_in) # Tour mode: WK; inbound half tour,  >1 trip on halftour, last trip of halftou
[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000, -0.59216242,  0.00000000], # 77 (stp_ing1*ifeq(remode,7)*last_in) # Tour mode: BK; inbound half tour,  >1 trip on halftour, last trip of halftour
# Generalized accessibilities
[  0.78627189,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 78 gen_Acc
[  0.00000000,  0.78627189,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 79 gen_Acc
[  0.00000000,  0.00000000,  0.78627189,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 80 gen_Acc
[  0.00000000,  0.00000000,  0.00000000,  0.78627189,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 81 gen_Acc
[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.78627189,  0.00000000,  0.00000000,  0.00000000], # 82 gen_Acc
[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.78627189,  0.00000000,  0.00000000], # 83 gen_Acc
[  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.78627189,  0.00000000], # 84 gen_Acc
]                 
                 
transientCoeffMap={

    "computedValues" : [
                        [12,  1, 23], #schoolPurpose thru prevTripEscort
                        [38, 24,  2], #prevS3EscAM thru prevS3EscPostAM
                        [50, 26, 52]  #modeDA thru BKLastOfMultiHt2
                      ],
    "derivedDoubleValues" : [
                        [1,   0,  1], #mixDensTripDest
                        [2,  78,  7], #generalized Accessibility for each mode
                      ],

                   
                   }


