####################################################################
# FullyJointTourSubmodel_Generation.py
# other notes:
#   I am not adhering to the python convention of 70-odd columns per line
####################################################################

from Globals import *

# the name of the corresponding class on the C# side:
# this allows for multiple scripts targeting the same component
modelComponentName="FullyJointTourSubmodelGeneration"  

dataReferences = [
    {"type" : "constants",
     "name" : "Constants",
     "columns" : ["One"],
     "values" : [1]
    },

    # this data will be fed to an instance of HouseholdDataUtility, along with the persons data ref following
    {"type" : "memory",
     "name" : "HouseholdBaseData",
     "dataType" : "int",
     # Column names are uppercase in this file
     "columns" : ["HHID", 
                  "HHINC5S", 
                  "HHZON", 
                  "HCHILD3", 
                  "HSTUD", 
                  "HFTW", 
                  "HPTW", 
                  "HNWA", 
                  "HSEN", 
                  "HH1PERSON", 
                  "ADULT1KIDS", 
                  "hhsize"
                  ]
    },

    # in the generation model the person data is multirow
    {"type" : "memory",
     "dataType" : "int",
     "name" : "PersonBaseData",
     "columns" : [
                  "personId",
                  "HHID", 
                  "HHINC5S", 
                  "HHZON", 
                  "ptypeDAP", 
                  "gender"
                  ]
    },


    {"type" : "memory",
     "dataType" : "int",
     "name" : "HouseholdModeledData",
     "columns" : [
                "hhId",        # 00
                "homeZoneId",   # 01
                "nCars",        # 02
                "nC1_MND",      # 03
                "nC2_MND",      # 04
                "nC3_MND",      # 05
                "nAdS_MND",     # 06
                "nFTW_MND",     # 07
                "nNWA_MND",     # 08
                "nSen_MND",     # 09
                "nPTW_MND",     # 10
                "nHH_MND",      # 11
                "nC1_NMT",      # 12
                "nC2_NMT",      # 13
                "nC3_NMT",      # 14
                "nAdS_NMT",     # 15
                "nFTW_NMT",     # 16
                "nPTW_NMT",     # 17
                "nNWA_NMT",     # 18
                "nSen_NMT",     # 19
                "nHH_NMT",      # 20
                "nCT1_Sch",     # 21
                "nCT2_Sch",     # 22
                "nCT3_Sch",     # 23
                "nCT4_Sch",     # 24
                "nCT5_Sch",     # 25
                "nC_SAH",       # 26
                "nCh_0Tours",   # 27
                "nAdt_0Tours"   # 28    
                ]
},


    # in the generation model the person data is multirow
    {"type" : "memory",
     "dataType" : "double",
     "name" : "PersonModeledData",
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
                  "noCarsInHh",             # 00    
                  "workersGTcars",          # 01    # Workers > Cars
                  "hhSizeEqualsTwo",        # 02    # HH Size = 2
                  "nochildreninHh",         # 03    # 0 Children in HH
                  "oneAdultinHh",           # 04    # 1 Adult in HH
                  "gt2AdultsinHH",          # 05    # 3+ Adults in HH
                  "All_Adults_MND",         # 06    #  1 if All Adults in HH with MND DAP
                  "gt1Child_NoPrevTour", # 07    #  2+ Children with No Previous Tour Selected
                  "gt1Adult_NoPrevTour",   # 08    #  2+ Adults with No Previous Tour Selected
                  "gt1HhMember_NoPrevTour", # 09    #  2+ HH Members with No Previous Tour Selected
				  "xchildrenInHH",			# 10 presence of children in HH
				  "xchildren_MND",				# 11 presence of children with a mandatory DAP
				  "total_DAP",				    # 12 Active patterns in a HH			
				  "noPrevTour"				# 13 1 if any HH member does not have a previous tour scheduled
                 ]                          
    },

    {"type" : "memory",
     "dataType" : "double",
     "name" : "DerivedDoubleValues",
     "columns" : [
                  "maxWinChildren", # 0  Log of (1 + Max Time Window Overlap [no. of 30-min periods] across Children), if < 2 hh members with no previous tours
                  "maxWinAdults",   # 1  #Log of (1 + Max Time Window Overlap [no. of 30-min periods] across Adults)   if < 2 hh members with no previous tours
                  "maxWinHH",       # 2  #Log of (1 + Max Time Window Overlap [no. of 30-min periods] across all HH Members) if < 2 hh members with no previous tours
                  "maxWinHHInc",     # 3  #Log of (1 + Max Time Window Overlap [no. of 30-min periods] across all HH Members), HH Income < $40K, if < 2 hh members with no previous tours
				  "maxWinHHInc4",     # 4  #Log of (1 + Max Time Window Overlap [no. of 30-min periods] across all HH Members), HH Income > $100K, if < 2 hh members with no previous tours
				  "maxWinMixAdltChld" # 5  #Log of (1 + Max Time Window Overlap [no. of 30-min periods] across across a Mixed Travel Group of HH Members)  if < 2 hh members with no previous tours
                 ]                          
    },

    
    {"type" : "memory",
     "name" : "Zones",
     "columns" : ["zoneId", "tw_acc", "rehwyacc10", "tetracc15", "ext_dist"] 
    },

    ]


# Matrices are different enough to require their own structure:
matrixReferences = [
# for now none
]


# ######################  model structure section  ##########################

# DAP Id, 
#altIntrinsicValues= range(14) ##[0-13]
altIntrinsicValues= [ # correspond to TourGenerationEnum values
                    # number of meal, shopping, personal business, social recreation tours for the alternative
                    0,# [0,0,0,0], # 0 Tours 
                    1,# [1,0,0,0], # 1 Meal
                    2,# [0,1,0,0], # 1 Shopping
                    3,# [0,0,1,0], # 1 Personal-Business
                    4,# [0,0,0,1], # 1 Social-Recreation
                    6,# [2,0,0,0], # 2 Meal
                    7,# [1,1,0,0], # 1 Meal + 1 Shopping
                    8,# [1,0,1,0], # 1 Meal + 1 Personal-Business
                    9,# [1,0,0,1], # 1 Meal + 1 Social-Recreation
                    11,# [0,2,0,0], # 2 Shopping
                    12,# [0,1,1,0], # 1 Shopping + 1 Personal-Business
					13,# [0,1,0,1], # 1 Shopping + 1 Social-Recreation
                    15,# [0,0,2,0], # 2 Personal-Business
                    16,# [0,0,1,1], # 1 Personal-Business + 1 Social-Recreation
                    18 # [0,0,0,2]  # 2 Social-Recreation
                     ]

# not used thus far:
# friendly descriptions of the alternatives, maybe for UI display somehow
altNames = ["0 Tours", "1 Meal", "1 Shopping", "1 Personal-Business", "1 Social-Recreation",            # 0-4
            "2 Meal", "1 Meal + 1 Shopping", "1 Meal + 1 Personal-Business",                            # 5-7
            "1 Meal + 1 Social-Recreation", "2 Shopping", "1 Shopping + 1 Personal-Business",           # 8-10
			"1 Shopping + 1 Social-Recreation", "2 Personal-Business",									# 11-12
             "1 Personal-Business + 1 Social-Recreation", "2 Social-Recreation"]  						# 12-14

# this should evolve into a specification (in general) a tree structure
logitType = "MultinomialLogit"

#Sorry about the length
#altSpecificConsts=[ 0.00000000, -9.74051357, -8.41516774, -9.27986902, -8.96458480, -15.84625015, -13.59180281, -14.38239302, -14.07295248, -12.45448428, -13.05704719, -12.87982317, -12.90391116, -14.20423306, -12.95439294] # ASC
#altSpecificConsts=[0, -8.94051357, -7.61516774, -8.47986902, -8.1645848, -15.04625015, -12.79180281, -13.58239302, -13.27295248, -11.65448428, -12.25704719, -12.07982317, -12.10391116, -13.40423306, -12.15439294]
#altSpecificConsts=[ 0, -8.24051357, -6.91516774, -7.77986902, -7.4645848, -14.34625015, -12.09180281, -12.88239302, -12.57295248, -10.95448428, -11.55704719, -11.37982317, -11.40391116, -12.70423306, -11.45439294]
#altSpecificConsts=[0, -7.94051357, -6.61516774, -7.47986902, -7.1645848, -14.04625015, -11.79180281, -12.58239302, -12.27295248, -10.65448428, -11.25704719, -11.07982317, -11.10391116, -12.40423306, -11.15439294]
altSpecificConsts=[0, -7.24051357, -5.91516774, -6.77986902, -6.4645848, -13.34625015, -11.09180281, -11.88239302, -11.57295248, -9.95448428, -10.55704719, -10.37982317, -10.40391116, -11.70423306, -10.45439294]


durableCoeffs=[
## 0 Tours,    1 ML,        1 SH,        1 PB,        1 SR,        2 ML,        1ML+1SH,     1ML+1PB,     1ML+1SR,     2 SH,        1SH+1PB,     1SH+1SR,     2 PB,        1PB+1SR,     2 SR
[ placeholder]*15, # 00 hhinc5s (SEGMENT)
[ 0.00000000, -2.13954591, -2.13954591, -2.13954591, -2.13954591, -2.13954591, -2.13954591, -2.13954591, -2.13954591, -2.13954591, -2.13954591, -2.13954591, -2.13954591, -2.13954591, -2.13954591], # 1 ZEROVEH #   
[ 0.00000000,  0.00000000, -0.11791742, -0.27695142,  0.00000000,  0.00000000, -0.11791742, -0.27695142,  0.00000000, -0.11791742, -0.39486884, -0.11791742, -0.27695142, -0.27695142,  0.00000000], # 2 HHVEH #   
[0, 0.25274415, 0.25274415, 0.25274415, 0.25274415, 0.25274415, 0.25274415, 0.25274415, 0.25274415, 0.25274415, 0.25274415, 0.25274415, 0.25274415, 0.25274415, 0.25274415],# 3 PRES_CHLD # Presence of Children in HH
[ placeholder]*15, # tw available(SEGMENT)
[ 0.00000000,  0.26153871,  0.00000000,  0.00000000,  0.00000000,  0.26153871,  0.26153871,  0.26153871,  0.26153871,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000], # 5 REHWYACC10 # Auto Accessibility to Retail Employment  
[ 0.00000000,  0.12735789,  0.12735789,  0.12735789,  0.12735789,  0.12735789,  0.12735789,  0.12735789,  0.12735789,  0.12735789,  0.12735789,  0.12735789,  0.12735789,  0.12735789,  0.12735789], # 6 RETRACC15 # Transit Accessibility to Retail Employment 
[ 0.00000000, -0.02399971,  0.00000000, -0.01206361,  0.00000000, -0.02399971, -0.02399971, -0.03606332, -0.02399971,  0.00000000, -0.01206361,  0.00000000, -0.01206361, -0.01206361,  0.00000000]  # 7 DISTTOEXT #   
]

durableCoeffMap={"Constants" : [[0,0,1]],             # 00 hhinc5s (SEGMENT)
                 "HouseholdModeledData" : [[2,2,1]],  # 02 nCars
                 "DerivedValues" : [
                                    [0,1,1],  # 01 nocarsinHh
                                    [10,3,1]  # 03 presence of children
                                   ], 
                 "Zones" : [                          
                            [1,4,4] # tw_acc, ret_hwy, ret_xit, ext_dist 
                           ],
                 }

transientCoeffs=[
## 0 Tours,    1 ML,        1 SH,        1 PB,        1 SR,        2 ML,        1ML+1SH,     1ML+1PB,     1ML+1SR,     2 SH,        1SH+1PB,     1SH+1SR,     2 PB,        1PB+1SR,     2 SR
[0, -1.81154416, -1.81154416, -1.81154416, -1.81154416, -2.25690008, -2.25690008, -2.25690008, -2.25690008, -2.25690008, -2.25690008, -2.25690008, -2.25690008, -2.25690008, -2.25690008], # (HFTWMAND+HPTWMAND) # Number of Full-Time/Part-Time Workers in HH with Mandatory DAP  # 0(HFTWMAND+HPTWMAND) # Number of Full-Time Workers in HH with Mandatory DAP 
[0, -1.61154416, -1.61154416, -1.61154416, -1.61154416, -2.05690008, -2.05690008, -2.05690008, -2.05690008, -2.05690008, -2.05690008, -2.05690008, -2.05690008, -2.05690008, -2.05690008], # (HFTWMAND+HPTWMAND) # Number of Full-Time/Part-Time Workers in HH with Mandatory DAP , # 1(HFTWMAND+HPTWMAND) # Number of Part-Time Workers in HH with Mandatory DAP 
[0, -0.08180954, -0.08180954, -0.08180954, -0.08180954, 0.09332842, 0.09332842, 0.09332842, 0.09332842, 0.09332842, 0.09332842, 0.09332842, 0.09332842, 0.09332842, 0.09332842], #  (HFTWNM+HPTWNM) # Number of Full-Time/Part-Time Workers in HH with Non-Mandatory DAP , # 2(HFTWNM+HPTWNM) # Number of Full-Time Workers in HH with Non-Mandatory DAP 
[0, -0.08180954, -0.08180954, -0.08180954, -0.08180954, 0.09332842, 0.09332842, 0.09332842, 0.09332842, 0.09332842, 0.09332842, 0.09332842, 0.09332842, 0.09332842, 0.09332842], #  (HFTWNM+HPTWNM) # Number of Full-Time/Part-Time Workers in HH with Non-Mandatory DAP , # 3(HFTWNM+HPTWNM) # Number of Part-Time Workers in HH with Non-Mandatory DAP 
[ 0.00000000,  0.00000000,  0.00000000,  0.00000000, -0.16086151,  0.00000000,  0.00000000,  0.00000000, -0.16086151,  0.00000000,  0.00000000, -0.16086151,  0.00000000, -0.16086151, -0.16086151], # 4 IFGE(HCHILDMAND,1) # Presence of Children 5-15 years & 16+ years in HH with Mandatory DAP  
[ 0.00000000,  0.18661512,  0.36096999,  0.36096999,  0.54913931,  0.46790686,  0.46790686,  0.46790686,  0.65607618,  0.64226173,  0.64226173,  0.83043105,  0.64226173,  0.83043105,  0.83043105], # 5 (NMAND+MNDA) #  Active Patterns in a HH 
[ 0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.90686234,  0.90686234,  0.90686234,  0.90686234,  0.90686234,  0.90686234,  0.90686234,  0.90686234,  0.90686234,  0.90686234], # 6 NO_PREV # Any HH members with no previous tours scheduled 
[ 0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.00000000,  0.11781168,  0.11781168,  0.11781168,  0.11781168,  0.11781168,  0.11781168,  0.11781168,  0.11781168,  0.11781168,  0.11781168], # 7 LOG(1+CHLDMAXWIN) # Log of (1 + Max Time Window Overlap [no. of 30-min periods] across Children) 
[ 0.00000000,  0.23636285,  0.23636285,  0.49742395,  0.15215574,  0.23636285,  0.23636285,  0.49742395,  0.15215574,  0.23636285,  0.49742395,  0.15215574,  0.49742395,  0.41321684,  0.15215574], # 8 LOG(1+ADLTMAXWIN) # Log of (1 + Max Time Window Overlap [no. of 30-min periods] across Adults) 
[ 0.00000000,  1.39580664,  1.39580664,  1.39580664,  1.39580664,  1.39580664,  1.39580664,  1.39580664,  1.39580664,  1.39580664,  1.39580664,  1.39580664,  1.39580664,  1.39580664,  1.39580664], # 9 LOG(1+WIN_PER) # Log of (1 + Max Time Window Overlap [no. of 30-min periods] across all HH Members) 
[ 0.00000000, -0.02814237, -0.02814237, -0.02814237, -0.02814237, -0.02814237, -0.02814237, -0.02814237, -0.02814237, -0.02814237, -0.02814237, -0.02814237, -0.02814237, -0.02814237, -0.02814237], # 10 LOG(1+WIN_PER)*INC100 # Log of (1 + Max Time Window Overlap [no. of 30-min periods] across all HH Members) with income >$100K 
[ 0.00000000,  0.00000000,  0.00000000,  0.08756940,  0.21303279,  0.00000000,  0.00000000,  0.08756940,  0.21303279,  0.00000000,  0.08756940,  0.21303279,  0.08756940,  0.30060219,  0.21303279], # 11 LOG(1+MIXMAXWIN) # Log of (1 + Max Time Window Overlap [no. of 30-min periods] across a Mixed Travel Group of HH Members) 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],# 12(calibrated) # Number of Seniors in HH with Mandatory DAP 
[0, 1.55, 1.55, 1.95, 1.1, 1.55, 1.55, 1.95, 1.1, 1.55, 1.55, 1.1, 1.95, 1.1, 1.1],# 13(calibrated) # Number of Seniors in HH with Non-Mandatory DAP 
]


# 
transientCoeffMap={
"HouseholdModeledData" : 
        [
            [7,0,1],   ## 00 Number of FTW in HH with MND DAP
			[10,1,1],  ## 01 Number of PTW in HH with MND DAP
            [16,2,2],  ## 02 Number of FTW in HH with NM DAP
					   ## 03 Number of PTW in HH with NM DAP
			[9,12,1], ## 12 Number of Seniors in HH with MND DAP
			[19,13,1], ## 13 Number of Seniors in HH with NM DAP
        ],
"DerivedValues" : 
        [
            [11,4,3]  # 04 presence of children with a mandatory DAP
				      # 05 Active patterns in a HH	
					  # 06 No previous tour
        ],
"DerivedDoubleValues" : 
        [
            [0,7,3],     # 07 Log of (1 + Max Time Window Overlap across Children) [i.e. no. of 30-min periods]
                        # 08 Log of (1 + Max Time Window Overlap across Adults)
                        # 09 Log of (1 + Max Time Window Overlap across all HH Members)
            [4,10,2],   # 10 Log of (1 + Max Time Window Overlap across all HH Members), HH Income > $100K
						# 11 Log of (1 + Max Time Window Overlap across a Mixed Travel Group of HH Members
        ]
} 
                   

segmentDefinitions = [
#  friendly name     , input data ref, offset in input, range of values (order relates to coeff order in segmentCoeffMap)
 {'Name': 'Income 5 segment', 'DataRef': 'HouseholdBaseData','Offset': 1, 'DataRange': [0,1,2,3,4]}
]

segmentCoeffMap = [
{'Segment': 0, 'Vector': 'durable', 'Offset': 0,  # hhinc5 (pure segmentation)
  'Coefficients':
    [    # <25K      25-50k    50-75k    75-100k   >100k  INCLE50 Segmentation
		[ 0.000000, 0.000000, 0.000000, 0.000000, 0.000000], # 0 Tours
		[ 0.138384, 0.138384, 0.000000, 0.000000, 0.000000], # 1 ML
		[ 0.138384, 0.138384, 0.000000, 0.000000, 0.000000], # 1 SH
		[ 0.138384, 0.138384, 0.000000, 0.000000, 0.000000], # 1 PB
		[ 0.138384, 0.138384, 0.000000, 0.000000, 0.000000], # 1 SR
		[ 0.138384, 0.138384, 0.000000, 0.000000, 0.000000], # 2 ML
		[ 0.138384, 0.138384, 0.000000, 0.000000, 0.000000], # 1ML+1SH
		[ 0.138384, 0.138384, 0.000000, 0.000000, 0.000000], #  1ML+1PB
		[ 0.138384, 0.138384, 0.000000, 0.000000, 0.000000], #  1ML+1SR
		[ 0.138384, 0.138384, 0.000000, 0.000000, 0.000000], #  2 SH
		[ 0.138384, 0.138384, 0.000000, 0.000000, 0.000000], # 1SH+1PB
		[ 0.138384, 0.138384, 0.000000, 0.000000, 0.000000], #  1SH+1SR
		[ 0.138384, 0.138384, 0.000000, 0.000000, 0.000000], #  2 PB
		[ 0.138384, 0.138384, 0.000000, 0.000000, 0.000000], # 1PB+1SR
		[ 0.138384, 0.138384, 0.000000, 0.000000, 0.000000], #  2 SR       
    ]
},

{'Segment': 0, 'Vector': 'durable', 'Offset': 4,  #4 TRANSITACC
  'Coefficients':
    [    # <25K      25-50k    50-75k    75-100k   >100k  TRANSITACC*INC100 Segmentation
		[ 0.000000, 0.000000, 0.000000, 0.000000, 0.000000], # 0 Tours
		[ 0.000000, 0.000000, 0.000000, 0.000000, 0.000000], # 1 ML
		[ 0.000000, 0.000000, 0.000000, 0.000000, 0.000000], # 1 SH
		[ 0.000000, 0.000000, 0.000000, 0.000000, 0.000000], # 1 PB
		[ 0.000000, 0.000000, 0.000000, 0.000000, 0.290694], # 1 SR
		[ 0.000000, 0.000000, 0.000000, 0.000000, 0.000000], # 2 ML
		[ 0.000000, 0.000000, 0.000000, 0.000000, 0.000000], # 1ML+1SH
		[ 0.000000, 0.000000, 0.000000, 0.000000, 0.000000], #  1ML+1PB
		[ 0.000000, 0.000000, 0.000000, 0.000000, 0.290694], #  1ML+1SR
		[ 0.000000, 0.000000, 0.000000, 0.000000, 0.000000], #  2 SH
		[ 0.000000, 0.000000, 0.000000, 0.000000, 0.000000], # 1SH+1PB
		[ 0.000000, 0.000000, 0.000000, 0.000000, 0.290694], #  1SH+1SR
		[ 0.000000, 0.000000, 0.000000, 0.000000, 0.000000], #  2 PB
		[ 0.000000, 0.000000, 0.000000, 0.000000, 0.290694], # 1PB+1SR
		[ 0.000000, 0.000000, 0.000000, 0.000000, 0.290694], #  2 SR         
    ]
}


]
