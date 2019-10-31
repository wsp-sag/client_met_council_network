####################################################################
# FullyJointTour.py
# other notes:
#   I am not adhering to the python convention of 70-odd columns per line
####################################################################

from Globals import *

# the name of the corresponding class on the C# side:
# this allows for multiple scripts targeting the same component
modelComponentName="FullyJointTour"  
instantiationType="MultiModelComponent"


# this is a degenerate case of the multimodelcomponent;
# the main component does tour generation, this single submodel does participation:
subModels= {
            "FullyJointTourGeneration": r"FullyJointTourSubmodel_Generation.py",
            "Child1MandParticipation":r"FullyJointTourParticipationSubmodel_Child1_Mandatory.py",
            "Child1NMDParticipation": r"FullyJointTourParticipationSubmodel_Child1_NonMandatory.py",
            "Child2MandParticipation":r"FullyJointTourParticipationSubmodel_Child2_Mandatory.py",
            "Child2NMDParticipation": r"FullyJointTourParticipationSubmodel_Child2_NonMandatory.py",
            "Child3MandParticipation":r"FullyJointTourParticipationSubmodel_Child3_Mandatory.py",
            "Child3NMDParticipation": r"FullyJointTourParticipationSubmodel_Child3_NonMandatory.py",
            "FTWMandParticipation": r"FullyJointTourParticipationSubmodel_FullTimeWorker_Mandatory.py",
            "FTWNMDParticipation":  r"FullyJointTourParticipationSubmodel_FullTimeWorker_NonMandatory.py",
            "PTWMandParticipation": r"FullyJointTourParticipationSubmodel_PartTimeWorker_Mandatory.py",
            "PTWNMDParticipation":  r"FullyJointTourParticipationSubmodel_PartTimeWorker_NonMandatory.py",
            "SENMandParticipation": r"FullyJointTourParticipationSubmodel_Senior_Mandatory.py",
            "SENNMDParticipation":  r"FullyJointTourParticipationSubmodel_Senior_NonMandatory.py",
            "STDMandParticipation": r"FullyJointTourParticipationSubmodel_AdultStudent_Mandatory.py",
            "STDNMDParticipation":  r"FullyJointTourParticipationSubmodel_AdultStudent_NonMandatory.py",
            "NWAMandParticipation": r"FullyJointTourParticipationSubmodel_NonWorkingAdult_Mandatory.py",
            "NWANMDParticipation":  r"FullyJointTourParticipationSubmodel_NonWorkingAdult_NonMandatory.py",
}

parameters= {
             "NumberOfRetriesForParticipationSubmodel": 4,  # number of times to rerun the participation model if not all tours are filled
             "FirstAssignedTourId" : 10
             }


dataReferences = [
    {"type" : "constants",
     "name" : "Constants",
     "columns" : ["One"],
     "values" : [1]
    },

    # this data will be fed to an instance of HouseholdDataUtility, along with the persons data ref following
    {"type" : "dbffile",
     "name" : "HouseholdBaseData",
     "filename" : cube___HOUSEHOLDS_FILE___, 
     # Column names are uppercase in this file
     "columns" : ["HHID", 
                  "HHINC5S", 
                  "HHZON", 
                  "HCHILD1", 
                  "HCHILD3", 
                  "HSTUD", 
                  "HFTW", 
                  "HPTW", 
                  "HNWA", 
                  "HSEN", 
                  "HH1PERSON", 
                  "ADULT1KIDS", 
                  "hhsize",
                  "HWORKERS"
                  ], 
     "deferredLoad" : True 
    },

    {"type" : "dbffile",
     "name" : "PersonBaseData",
     "filename" : cube___PERSONS_FILE___, 
     # Column names are uppercase in this file
     "columns" : [
                  "personId",
                  "HHID", 
                  "HHINC5S", 
                  "HHZON", 
                  "ptypeDAP", 
                  "gender"
                  ],

     "deferredLoad" : True 
    },


    # modeled data for person and household will be fed to a second instance of HouseholdDataUtility    

    {"type" : "dbffile",
     "dataType" : "int",
     "name" : "HouseholdModeledData",
     "filename" : cube___MODELED_HOUSEHOLDS_FILE___, 
     "columns" : [
                "hhId",         # 00
                "homeZoneId",   # 01
                "nCars",        # 02
                "nC1_NMT",      # 03
                "nC2_NMT",      # 04
                "nC3_NMT",      # 05
                "nNWA_NMT",     # 06
                "nSen_NMT",     # 07
                "nPTW_NMT",     # 08
                "nFTW_NMT",     # 09
                "nAdS_NMT",     # 10
                "nHH_NMT",      # 11
                "nC1_MND",      # 12
                "nC2_MND",      # 13
                "nC3_MND",      # 14
                "nNWA_MND",     # 15
                "nSen_MND",     # 16
                "nPTW_MND",     # 17
                "nFTW_MND",     # 18
                "nAdS_MND",     # 19
                "nHH_MND",      # 20
                "nCT1_Sch",     # 21
                "nCT2_Sch",     # 22
                "nCT3_Sch",     # 23
                "nCT4_Sch",     # 24
                "nCT5_Sch",     # 25
                "nC_SAH",       # 26
                "nCh_0Tours",   # 27
                "nAdt_0Tours"   # 28
                ],
     "deferredLoad" : True 
},


    {"type" : "dbffile",
     "dataType" : "int",
     "name" : "PersonModeledData",
     "filename" : cube___FULLY_JOINT_TOUR_PRE_PROCESSED_DATA___, #  
     "columns" : [
                "personId",
                "hhId",
                "homeZoneId", # for grouping
                "DAPId",
                "tourCount",
                "slotsArriv", # bit-encoded time slots via PersonTourDaySlots (Least significant bit is 3 am, next 47 bits run 3:30am to 2:30 am)
                "slotsDeprt",# bit-encoded time slots via PersonTourDaySlots (Least significant bit is 3 am, next 47 bits run 3:30am to 2:30 am)
                "slotsUsed"  # bit-encoded time slots via PersonTourDaySlots (Least significant bit is 3 am, next 47 bits run 3:30am to 2:30 am)

                ]
},


    {"type" : "memory",
     "dataType" : "int",
     "name" : "DerivedValues",
     "columns" : [
                  "workersGTcars",              # 2 Workers > Cars
                  "hhSizeEqualsTwo",            # 4 HH Size = 2
                  "nochildreninHh",             # 5 0 Children in HH
                  "oneAdultinHh",               # 6 1 Adult in HH
                  "gt3AdultsinHH",              # 7 3+ Adults in HH
                  "All_Adults_MND",           # 16 1 if All Adults in HH with MND DAP
                  "gt2Children_NoPrevTour",     # 17 2+ Children with No Previous Tour Selected
                  "gt2Adults_NoPrevTour",       # 18 2+ Adults with No Previous Tour Selected
                  "gt2HhMembers_NoPrevTour"     # 19 2+ HH Members with No Previous Tour Selected
                 ] 
    },

    
    {"type" : "dbffile",
     "name" : "Zones",
     "filename" : cube___ZONES_FILE___, # file paths MUST BE RAW strings (preceded by 'r')
     "columns" : ["zoneId", "tw_acc", "rehwyacc10", "tetracc15", "ext_dist" ] 
    },



    


    # if we had an Id source we could reduce the compound key to simple key
    {"type" : "dbffile",
     "isOutput": "true",
     "name" : "OutputTours",     
     "filename" : cube___FULLY_JOINT_TOURS___, # file paths MUST BE RAW strings (preceded by 'r')
     "parameters" : [
                  ["person1Id",  "person1Id"], # part 1 of pk: using first person in tour
                  ["@tourId",      "tourId"],   # part 2 of pk: tourId starting from 5 for joint tours 
                  ["@tourPurp",   "tourPurp"], 
                  ["hhId",       "hhId"],
                  ["homeZoneId", "homeZoneId"],
                  ["@nAdults",   "nAdults"],    # for tour dest choice logsum (partySize2, noAdults)
                  ["@nChildren",   "nChildren"], # for tour dest choice logsum (partySize2, noChildren)
                  ["@xFtwInTour", "xFtwInTour"],# for tour dest choice logsum (party has at least one ftw)
                  ["TourGenEnum", "TourGenEnum"], # for use in WBST and other downstreams
                  ["household size", "hhSize"],  # for validation stats
                  ["party size", "partySize"],  # for validation
                  ["mand patterns in HH", "nMndHh"],
                  ["mand patterns On Tour", "nMndOnTour"]
                  ] 
    }, 

    # equivalent of link table from personId to tours;
    # if we had an Id source to generate tour ids we could eliminate the now-confusing compound tour id which
    # for fully joint tours consists of the id of one person on the tour plus a persTourId in the range of FirstAssignedTourId to FirstAssignedTourId + 1
    # (where FirstAssignedTourId is an input parameter at the top of this configuration file)
    {"type" : "dbffile",
     "isOutput": "true",
     "name" : "OutputPersonTourLinkTable",     
     "filename" : cube___FULLY_JOINT_TOUR_PERSON_LINK_TABLE___, # file paths MUST BE RAW strings (preceded by 'r')
     "parameters" : [
                  ["persTourId", "persTourId"],  # partial pk to FullyJointTours
                  ["tourId",   "tourId"],        # partial pk to FullyJointTours
                  ["personId",  "personId"],  # person involved in tour
                  ["homeZoneId", "homeZoneId"], # for chunking
                  ["personType", "ptypeDAP"],  # for tod
                  ["female", "female"],  # for tod
                  ["xC123_SAH", "xC123_SAH"] # for tod
                  ] 
    }, 

    {"type" : "dbffile",
     "isOutput": "true",
     "name" : "OutputFJToursByHh",     
     "filename" : cube___FULLY_JOINT_TOUR_SUMMARY___, # file paths MUST BE RAW strings (preceded by 'r')
     "parameters" : [
                  ["hhId",                  "hhId"],         
                  ["hhinc5s",         "hhinc5s"],                   #personbase or hhbase
                  ["number fj in hh",       "nFjToursHh"],      # tour count
                  ["mand patterns in HH",   "nMndHh"],          # person modeled
                  ["nonmand patterns in HH","nNmdHh"],          # person modeled
                  ["inactive patterns in HH","nInactHh"],          # person modeled
                  ["n fj hh tours with mixed mand nonmand","nFjHhMixed"],     # fj
                  ["n fj hh tours with all mand",    "nFjHhMnd"],
                  ["n fj hh tours with all nonmand", "nFjHhNmd"],
                  ["hh is eligible", "isEligible"]    # household not disqualified by hhsize < 2 or < 2 active DAPs
                  ] 
    }, 

	# this output is space and time-consuming so is disabled in the code unless a compile-time define named 'debug_validation' is set
    {"type" : "dbffile",
     "isOutput": "true",
     "name" : "OutputFJGenerationStats",     
     "filename" : cube___FULLY_JOINT_TOUR_GENERATION_SUMMARY___, # file paths MUST BE RAW strings (preceded by 'r')
     "parameters" : [
                  ["hhId",                  "hhId"],         # 0
                  #["mand patterns in HH",   "nMndHh"],       # 1   # person modeled
                  #["nonmand patterns in HH","nNmdHh"],       # 2   # person modeled
                  #["inactive patterns in HH","nInactHh"],    # 3     # person modeled
                  ["choice", "choice"],                      # 4
                    #durables                                # 5
                  ["hhinc5s","hhinc5s"],  # 6
                  ["noCarsinHh","noCarsinHh"],  # 7
                  ["workGtCars","workGtCars"],  # 8
                  ["nCars","nCars"],  # 9
                  ["hhSizeEq2","hhSizeEq2"],  #10
                  ["nochildreninHh","noChildHh"],  #11
                  ["oneAdultinHh","oneAdultHh"],  #12
                  ["gt2AdultsinHH","gt2AdultHh"],  #13
                  ["tw_acc","tw_acc"],  #14
                  ["rst_hwy","rst_hwy"],  #15
                  ["ret_hwy","ret_hwy"],  #16
                  ["temp_hwy","temp_hwy"],  #17
                  ["hhs_hwy","hhs_hwy"],  #18
                  #transients                                #19
                  ["nCh1Mnd", "nCh1Mnd"],                    #20
                  ["nCh2Mnd", "nCh2Mnd"],                    #21
                  ["nCh3Mnd", "nCh3Mnd"],                    #22
                  ["nStdMnd", "nStdMnd"],                    #23
                  ["nFtwMnd", "nFtwMnd"],                    #24
                  ["nNwaMnd", "nNwaMnd"],                    #25
                  ["nSenMnd", "nSenMnd"],                    #26
                  ["nCh1Nmd", "nCh1Nmd"],                    #27
                  ["nCh2Nmd", "nCh2Nmd"],                    #28
                  ["nCh3Nmd", "nCh3Nmd"],                    #29
                  ["nStdNmd", "nStdNmd"],                    #30
                  ["nFtwNmd", "nFtwNmd"],                    #31
                  ["nPtwNmd", "nPtwNmd"],                    #32
                  ["nNwaNmd", "nNwaNmd"],                    #33
                  ["nSenNmd", "nSenNmd"],                    #34
                  ["allAdMnd", "allAdMnd"],                   #35
                  ["Ch2pNoTr", "Ch2pNoTr"],                  #36
                  ["Ad2pNoTr", "Ad2pNoTr"],                  #37
                  ["Hh2pNoTr", "Hh2pNoTr"],                  #38
                  ["lgMxWinCh","lgMxWinCh"],                 #39
                  ["lgMxWinAd","lgMxWinAd"],                 #40
                  ["lgMxWinHh","lgMxWinHh"],                #41
                  ["lgMxWinHhI",  "lgMxWinHhI"],              #42
                  ["EUNoTours"      ,"EUNoTours"     ],            #43 // should be zero
                  ["EU1Meal"      ,"EU1Meal"     ],            #43
                  ["EU1Shop"      ,"EU1Shop"     ],            #44
                  ["EU1PerB"      ,"EU1PerB"     ],            #45
                  ["EU1SRec"      ,"EU1SRec"     ],            #46
                  ["EU2Meal"      ,"EU2Meal"     ],            #47
                  ["EU1Meal1Shop" ,"EU1Meal1Shp"],            #48
                  ["EU1Meal1PB"   ,"EU1Meal1PB"  ],            #49
                  ["EU1Meal1Srec" ,"EU1Meal1SR"],            #50
                  ["EU2Shop"      ,"EU2Shop"     ],            #51
                  ["EU1Shop1PB"   ,"EU1Shop1PB"  ],            #52
                  ["EU2PerB"      ,"EU2PerB"     ],            #53
                  ["EU1PerB1Srec" ,"EU1PerB1SR"],            #54
                  ["EU2SRec"      ,"EU2SRec"     ],             #55
                  ["SumEUtils"      ,"SumEUtils"     ]             #55
                  ]                                            
    },                                                         
                                                               
	# this output is space and time-consuming so is disabled in the code unless a compile-time define named 'debug_validation' is set
    {"type" : "dbffile",                                       
     "isOutput": "true",                                       
     "name" : "OutputFJParticipationStats",                    
     "filename" : cube___FULLY_JOINT_TOUR_PARTICIPATION_SUMMARY___, # file paths MUST BE RAW strings (preceded by 'r')
     "parameters" : [
                  ["hhId",                  "hhId"],  
                  ["trialNumber",    "trialNum"],   
                  ["generated tour Purpose",   "tourPurp"],  
                  ["personId", "personId"],
                  ["mandDAP", "mandDAP"],
                  ["ptype2", "ptypeDAP"],  
                  ["ordinal of potential participant", "ordinal"],
                  ["max window remaining if participating (30 min slots)", "maxWinPtcp"],
                  ["reduction in max window remaining if participating (30 min slots)", "maxWinRed"],
                  ["chosen", "chosen"],

                    ["twoMand", "twoMand"    ],
                    ["gt1WkTrStp","gt1WkTrStp" ],
                    ["female", "female"      ],
                    ["nOthC1Cand", "nOthC1OnCand"],
                    ["nChild1On", "nChild1On"],
                    ["xChild1On", "xChild1On"],
                    ["nNWAOnTr", "nNWAOnTr"  ],
                    ["nSenOnTr", "nSenOnTr"  ],
                    ["nChild2On","nChild2On" ],
                    ["nChild3On","nChild3On" ],
                    ["nPTWOnTr", "nPTWOnTr"  ],
                    ["nFTWOnTr", "nFTWOnTr"  ],
                    ["nStudOnTr", "nStudOnTr"],
                    ["xCh1NoAdTr","xCh1NoAdTr"  ],
                    ["nAdLxC1NoA","nAdLxC1NoA"  ],
                    ["OnlyNmdOn", "OnlyNmdOn"],
                    ["OnlyMandOn","OnlyMandOn"  ],
                    ["jTrSzRatio","jTrSzRatio"  ],
                    ["lgMxTIfPart","lgMxTIfPart"],
                    ["lgRedIfPart", "lgRedIfPart"],
                    # durable value utils
                    ["dv1", "dv1"],
                    ["dv2", "dv2"],
                    ["dv3", "dv3"],
                    ["tv1", "tv1"],
                    ["tv2", "tv2"],
                    ["tv3", "tv3"],
                    ["tv4", "tv4"],
                    ["tv5", "tv5"],
                    ["tv6", "tv6"],
                    ["tv7", "tv7"],
                    ["tv8", "tv8"],
                    ["tv9", "tv9"],
                    ["tv10", "tv10"],
                    ["tv11", "tv11"],
                    ["tv12", "tv12"],
                    ["tv13", "tv13"],
                    ["tv14", "tv14"],
                    ["tv15", "tv15"],
                    ["tv16", "tv16"],
                    ["tv17", "tv17"],
                    ["tv18", "tv18"],
                    ["tv19", "tv19"],
                    ["tv20", "tv20"],
                    ["ASC", "ASC"],
                    ["sumUtils", "sumUtils"],
                    ["person's DAP", "dapId"]
                  ]            
    },                         
    ]                          
