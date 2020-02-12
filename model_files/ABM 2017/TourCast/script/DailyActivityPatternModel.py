####################################################################
# DailyActivityPatternModel.py
# A python script with
#   DataReferences, MatrixReferences
#   list of modelComponents that are submodels
#   I am not adhering to the python convention of 70-odd columns per line
####################################################################

from Globals import *

instantiationType="MultiModelComponent"
#characteristics

# the name of the corresponding class on the C# side:
# this allows for multiple scripts targeting the same component
modelComponentName="DailyActivityPattern"  


# for now the model component will use specific knowledge of the submodels and the data
# to determine which submodel to run
subModels= {
            "Child1": r"DailyActivityPatternSubModel_Child1.py",
            "Child2": r"DailyActivityPatternSubModel_Child2.py", 
            "Child3": r"DailyActivityPatternSubModel_Child3.py", 
            "NonWorkingAdult": r"DailyActivityPatternSubModel_NonWorkingAdult.py", 
            "Senior": r"DailyActivityPatternSubModel_Senior.py", 
            "PartTimeWorker": r"DailyActivityPatternSubModel_PartTimeWorker.py", 
            "FullTimeWorker": r"DailyActivityPatternSubModel_FullTimeWorker.py",
            "AdultStudent": r"DailyActivityPatternSubModel_AdultStudent.py", 
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
     "name" : "Persons",
     "filename" : cube___DAILY_ACTIVITY_PATTERN_PRE_PROCESSED_DATA___, # file paths MUST BE RAW strings (open quote preceded by 'r')
     "columns" : ["personid", #0
                  "hhid",       # 1
                  "hhzon",      # 2
                  "pTypeDAP",     # 3
                  "hhinc5s",    # 4 
                  "hhsize",     # 5 
                  "hchild1",    # 6
                  "hchild2",    # 7
                  "hchild3",    # 8
                  "hstud",      # 9
                  "hftw",       # 10
                  "hptw",       # 11
                  "hnwa",       # 12
                  "hsen",       # 13
                  "age",        # 14
                  "hchildren",  # 15
                  "hworkers",   # 16
                  "hchildlt16", # 17
                "schZoneId",	# 18  # this was sqrootage but I moved this from the end to keep the mapping constant
                "hh1Person",	# 19
                "female",		# 20
                "hpotworkad",	# 21
                "hnochildre",	# 22
                "hadults",		# 23
                "ctype",		# 24
                "workzoneid",	# 25
                "noregwkplc",   # 26
                "nCars",        # 27  just added these
                "noCarsInHh",   # 28
                "wkGtCarGt0",   # 29
                "logsum",       # 30  to regular workplace
                "logRtToWk",    # 31
                "wlkTraccWk",   # 32
				"adult1kids"	# 33 to propagate through to TOD
                  ],
     "deferredLoad" : True,
     # sort originates in DAP preprocessor; uses the following sort to support both DAP and SchoolEscorting
     # "sort": ["hhzon", "hhinc5s", "hhid", "pTypeDAP" "age", "personId"]
    },
     
    {"type" : "dbffile",
     "name" : "Zones",
     "filename" : cube___ZONES_FILE___, # file paths MUST BE RAW strings (preceded by 'r')
     "columns" : [
                  "zoneId",    # 0
                  "ext_dist",  # 1
                  "tw_acc",    # 2
                  "mix_dens",  # 3
                  "TEhwyacc10", # 4
                  ] 
    },


    # dbf output spec; used in tests for inspecting whether results are reasonable
    {"type" : "dbffile",
     "isOutput": "true",
     "name" : "OutputDAPPersons",     
     "filename" : cube___DAILY_ACTIVITY_PATTERNS___, # file paths MUST BE RAW strings (preceded by 'r')
     # parameters could be generally of form source data reference : field
     "parameters" : [
                       [ "Persons", "personId"],
                       [ "hhId", "hhId"],
                       [ "homeZone", "homeZoneId"],
                       [ "PersonType", "personType"], 
                       [ "hhinc5s", "hhinc5s"],
                       [ "@alternativeChosen", "DAPId"],
                       [ "@tourCount", "tourCount"],
                       [ "age", "age"],
                       [ "female", "female"], 
                       [ "@zeroCarsInHh", "0CarsInHh"],
                       [ "@wkGtCarGt0", "wkGtCarGt0"],

                       # using '@' in data source name indicates this field is generated by the component, so requires some coordination with C# code
                    ]
    },

    # dbf output spec; beginning of household data to carry 
    {"type" : "dbffile",
     "isOutput": "true",
     "name" : "OutputDAPHouseholds",     
     "filename" : cube___MODELED_HOUSEHOLDS_FILE___, # file paths MUST BE RAW strings (preceded by 'r')
     # parameters could be generally of form source data reference : field
     "parameters" : [
                       [ "hhId",    "hhId"],
                       [ "homeZone", "homeZoneId"],  # for sorting/chunking down the line
                       [ "nCars",    "nCars"],

                       # non-mandatory tour counts by person type and for hh
                       [ "@nC1_NMT", "nC1_NMT"],
                       [ "@nC2_NMT", "nC2_NMT"],
                       [ "@nC3_NMT", "nC3_NMT"],
                       [ "@nNWA_NMT", "nNWA_NMT"],
                       [ "@nSen_NMT", "nSen_NMT"],
                       [ "@nPTW_NMT", "nPTW_NMT"],
                       [ "@nFTW_NMT", "nFTW_NMT"],
                       [ "@nAdS_NMT", "nAdS_NMT"],
                       [ "@nHH_NMT",   "nHH_NMT"],

                       # mandatory tour counts by person type and for hh
                       [ "@nC1_MND", "nC1_MND"],
                       [ "@nC2_MND", "nC2_MND"],
                       [ "@nC3_MND", "nC3_MND"],
                       [ "@nNWA_MND", "nNWA_MND"],
                       [ "@nSen_MND", "nSen_MND"],
                       [ "@nPTW_MND", "nPTW_MND"],
                       [ "@nFTW_MND", "nFTW_MND"],
                       [ "@nAdS_MND", "nAdS_MND"],
                       [ "@nHH_MND",   "nHH_MND"],
                       [ "@hhCtype1tour", "nCT1_Sch"], # number of children of ctype1 in hh with at least one school tour;
                       [ "@hhCtype2tour", "nCT2_Sch"], # number of children of ctype2 in hh with at least one school tour;
                       [ "@hhCtype3tour", "nCT3_Sch"], # number of children of ctype3 in hh with at least one school tour;
                       [ "@hhCtype4tour", "nCT4_Sch"], # number of children of ctype4 in hh with at least one school tour;
                       [ "@hhCtype5tour", "nCT5_Sch"], # number of children of ctype5 in hh with at least one school tour;

                       [ "@n children w SAH", "nC_SAH"],
                       [ "@n children no tours", "nCh_0Tours"],
                       [ "@n adults no tours", "nAdt_0Tours"]
                       # using '@' in data source name indicates this field is generated by the component, so requires some coordination with C# code
                    ]
    },






    # this file holds generated tours for each person, along with some variables that will be needed downstra
    {"type" : "dbffile",
     "isOutput": "true",
     "name" : "OutputDAPFirstTours",     
     "filename" : cube___DAILY_ACTIVITY_PATTERNS_FIRST_TOURS___, # file paths MUST BE RAW strings (preceded by 'r')
     # parameters could be generally of form source data reference : field
     "parameters" : [
                       [ "Person id", "personId"],
                       [ "household id", "hhId"],
                       [ "@tour", "persTourId"],
                       [ "@tour purpose", "tourPurp"],
                       [ "ptype2 (DAP order)", "personType"], # NOTE: THIS IS PTYPE2 output, not ptype
                       [ "hhinc5s", "hhinc5s"], 
                       [ "child 0-4", "cType1"], 
                       [ "child 5-10", "cType2"], 
                       [ "child 11-13", "cType3"], 
                       [ "child 14-15", "cType4"], 
                       [ "child 16+", "cType5"], 
                       [ "age", "age"], 
                       [ "male", "male"], 
                       [ "DestinationZone", "destZoneId"], 
                       [ "WorkplaceZone", "workZoneId"],
                       [ "wkGtCarGt0", "wkGtCarGt0"],
                       [ "homeZone", "homeZoneId"],
                       [ "nonstop tour", "noStopTour"],
                       [ "@alternativeChosen", "dapId"],
                       [ "@tourCount", "tourCount"],
                       [ "@hhChild1tour", "hhC1tour"],
                       [ "@hhChild2tour", "hhC2tour"],
                       [ "@hhChild3tour", "hhC3tour"],
                       [ "@hhChild4tour", "hhC4tour"],
                       [ "@hhChild5tour", "hhC5tour"],
                       [ "@hhChildSAH", "hhChildSAH"],
                       [ "child type", "ctype"], 

                       ["nCars", "nCars"],  # needed by dest choice
                       ["noCarsInHh", "noCarsInHh"],  # needed by dest choice
                       ["@minNTours", "minNTours"],  # needed by dest choice
                       ["@minNStops", "minNStops"],  # needed by dest choice
					   ["one adult 1+ kids", "adult1kids"],  # propagated through for time of day
                       # using '@' in data source name indicates this field is generated by the component, so requires some coordination with C# code
					   ["hChild2", "hChild2"],
					   ["hChild3", "hChild3"]
                    ]
    },

    {"type" : "dbffile",
     "isOutput": "true",
     "name" : "OutputDAPSecondTours",     
     "filename" : cube___DAILY_ACTIVITY_PATTERNS_SECOND_TOURS___, # file paths MUST BE RAW strings (preceded by 'r')
     # parameters could be generally of form source data reference : field
     "parameters" : [
                       [ "Person id", "personId"],
                       [ "household id", "hhId"],
                       [ "@tour", "persTourId"],
                       [ "@tour purpose", "tourPurp"],
                       [ "ptype2 (DAP order)", "personType"], # NOTE: THIS IS PTYPE2 output, not ptype
                       [ "hhinc5s", "hhinc5s"], 
                       [ "child 0-4", "cType1"], 
                       [ "child 5-10", "cType2"], 
                       [ "child 11-13", "cType3"], 
                       [ "child 14-15", "cType4"], 
                       [ "child 16+", "cType5"], 
                       [ "age", "age"], 
                       [ "male", "male"], 
                       [ "DestinationZone", "destZoneId"], 
                       [ "WorkplaceZone", "workZoneId"],
                       [ "wkGtCarGt0", "wkGtCarGt0"],
                       [ "homeZone", "homeZoneId"],
                       [ "nonstop tour", "nostopTour"],
                       [ "@alternativeChosen", "dapId"],
                       [ "@tourCount", "tourCount"],
                       [ "@hhChild1tour", "hhC1tour"],
                       [ "@hhChild2tour", "hhC2tour"],
                       [ "@hhChild3tour", "hhC3tour"],
                       [ "@hhChild4tour", "hhC4tour"],
                       [ "@hhChild5tour", "hhC5tour"],
                       [ "@hhChildSAH", "hhChildSAH"],
                       [ "child type", "ctype"], 
                       # using '@' in data source name indicates this field is generated by the component, so requires some coordination with C# code
                       ["nCars", "nCars"],  # needed by dest choice
                       ["noCarsInHh", "noCarsInHh"],  # needed by dest choice
                       ["@minNTours", "minNTours"],  # needed by dest choice
                       ["@minNStops", "minNStops"],  # needed by dest choice
					   ["one adult 1+ kids", "adult1kids"],
					   ["hChild2", "hChild2"],
					   ["hChild3", "hChild3"]
                    ]
    },



    # statistics for debugging
    {"type" : "dbffile",
     "isOutput": "true",
     "name" : "OutputDAPStats",     
     "filename" : cube___DAILY_ACTIVITY_PATTERNS_SUMMARY___, # file paths MUST BE RAW strings (preceded by 'r')
     "parameters" : [
                       [ "PersonType", "personType"],
                       [ "no DAP"   ,  "noDAP"],
                       [ "OneWorkNS", "OneWorkNS"],
                       [ "OneWork_S", "OneWork_S"],
                       [ "TwoWorkNS", "TwoWorkNS"],
                       [ "TwoWork_S", "TwoWork_S"],
                       [ "TwoWork_SS", "TwoWork_SS"],
                       [ "UniWorkNS", "UniWorkNS"],
                       [ "UniWork_S", "UniWork_S"],
                       [ "SchWorkNS", "SchWorkNS"],
                       [ "SchWork_S", "SchWork_S"],
                       [ "OneUni",    "OneUni"],
                       [ "TwoUni",    "TwoUni"],
                       [ "OneSch",    "OneSch"],
                       [ "TwoSch",    "TwoSch"],
                       [ "NMT",    "NMT"],
                       [ "SAH",    "SAH"],
                       [ "OOA",    "OOA"],
                       [ "Ext",    "Ext"]
                    ]
    },

    # we will use one memory reference that will be passed in as input to each model
    # the columns are cumulative counts for each person type that a particular tour type was selected for him/her
    # i.e. for any one person, a particular column value will remain the same or increment by 1 
    # so e.g. if a FTW was assigned 2 work tours, the nFTW_Wrk column will only increment by 1, as will the nFTW_Mandatory column
    # the multiModel component will fill the bins based on the returned alternative chosen;
    # the last column, nXXX_mandatory, gets incremented if the person has a school, work, or uni tour
    # a leading 'd' means this is a dummy column, just included to square up the number of columns per person type
    {"type" : "memory",
     "dataType" : "int",
     "name" : "SubmodelResults",

     # this column set is out of date with what is being used in the code; extra c4 and c5 'rows' are added
     #                0            1           2           3          4              5
     "columns" : ["nC1_Sch",   "nC1_NMT",  "nC1_SAH",  "nC1_OOA",  "nC1_Ext",  "nC1_Mandatory",#0 persontype = 1 (Child1 0-4 years); equal to ctype 1
                  "nC2_Sch",   "nC2_NMT",  "nC2_SAH",  "nC2_OOA",  "nC2_Ext",  "nC2_Mandatory",#1 persontype = 2 (Child2 5-15 years); equal to ctype range 2-4
                  "nC3_Sch",   "nC3_NMT",  "nC3_SAH",  "nC3_OOA",  "nC3_Ext",  "nC3_Mandatory",#2 persontype = 3 (Child3 16+ years); equal to ctype 5
                  "dNWA_Sch", "nNWA_NMT", "nNWA_SAH", "nNWA_OOA", "nNWA_Ext", "nNWA_Mandatory",#3 Non-Working Adult 
                  "dSen_Sch", "nSen_NMT", "nSen_SAH", "nSen_OOA", "nSen_Ext", "nSen_Mandatory",#4 Senior
                  "dPTW_Sch", "nPTW_NMT", "nPTW_SAH", "nPTW_OOA", "nPTW_Ext", "nPTW_Mandatory",#5 Part-Time Worker
                  "dFTW_Sch", "nFTW_NMT", "nFTW_SAH", "nFTW_OOA", "nFTW_Ext", "nFTW_Mandatory", #6 Full-Time Worker
                  "dAdS_Sch", "nAdS_NMT", "nAdS_SAH", "nAdS_OOA", "nAdS_Ext", "nAds_Mandatory", #7 Adult Student results are now tabulated for household aggregate data
                  "nCT2_Sch",   "nCT2_NMT",  "nCT2_SAH",  "nCT2_OOA",  "nCT2_Ext",  "nCT2_Mandatory",#2 ctype 2  (age 5-10; subset of personType 2 (child2)data)
                  "nCT3_Sch",   "nCT3_NMT",  "nCT3_SAH",  "nCT3_OOA",  "nCT3_Ext",  "nCT3_Mandatory",#2 ctype 3 (age 11-13; subset of personType 2 (child2)data)
                  "nCT4_Sch",   "nCT4_NMT",  "nCT4_SAH",  "nCT4_OOA",  "nCT4_Ext",  "nCT4_Mandatory"#2 ctype 4 (age 14-15; subset of personType 2 (child2)data)
                 ]
    },

    # for each submodel there are different calculated results, mostly from combining various of the SubmodelResults;
    # I could just lay out another large array with named columns, and have each submodel cherrypick and map the results
    # but it will be a little less cumbersome to just use a range of column names
    # just guessing on the number now
    {"type" : "memory",
     "dataType" : "double",
     "name" : "DerivedResults",     
     "columns" : ["Col " + str(x) for x in range(1, 40)]
    }
     
]

# Matrices are different enough to require their own structure:
# I don't see any matrices used directly in the submodels (indirectly through logsums)
matrixReferences = [

]
