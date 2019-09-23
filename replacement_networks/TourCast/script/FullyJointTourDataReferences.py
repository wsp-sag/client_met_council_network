####################################################################
# FullyJointTourDataReferences.py
# import this using
# from FullyJointTourDataReferences import *
####################################################################

dataReferences = [
    {"type" : "constants",
     "name" : "Constants",
     "columns" : ["One"],
     "values" : [1]
    },

    # this data will be fed to an instance of HouseholdDataUtility, along with the persons data ref following
    {"type" : "dbffile",
     "name" : "Households",
     "filename" : cube___HOUSEHOLDS_FILE___, 
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
                  ], 
     "deferredLoad" : True 
    },

    {"type" : "dbffile",
     "name" : "Persons",
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
     "name" : "HouseholdsModeledData",
     "filename" : cube___MODELED_HOUSEHOLDS_FILE___, 
     "columns" : [
                ["hhId"],
                ["homeZoneId"],
                ["nCars"],
                ["nC1_NMT"],
                ["nC2_NMT"],
                ["nC3_NMT"],
                [ "nNWA_NMT"],
                [ "nSen_NMT"],
                [ "nPTW_NMT"],
                [ "nFTW_NMT"],
                [ "nAdS_NMT"],
                [ "nHH_NMT"],
                ["nC1_MND"],
                ["nC2_MND"],
                ["nC3_MND"],
                [ "nNWA_MND"],
                [ "nSen_MND"],
                [ "nPTW_MND"],
                [ "nFTW_MND"],
                [ "nAdS_MND"],
                [ "nHH_MND"],
                ["nCT1_Sch"],
                ["nCT2_Sch"],
                ["nCT3_Sch"],
                ["nCT4_Sch"],
                ["nCT5_Sch"],
                ["nC_SAH"],
                ["nCh_0Tours"],
                [ "nAdt_0Tours"]
                ]
},


    {"type" : "dbffile",
     "dataType" : "int",
     "name" : "PersonsModeledData",
     "filename" : cube___DAILY_ACTIVITY_PATTERNS___, # may substitute another downstream item later
     "columns" : [
                ["personId"],
                ["hhId"],
                ["homeZoneId"], # for grouping
                ["DAPId"],
                ["tourCount"]
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

    
    {"type" : "memory",
     "name" : "Zones",
     "columns" : ["zoneId", "tw_acc", "rst_hwy", "ret_hwy","temp_hwy", "hhs_hwy"] 
    },
    
    ]
