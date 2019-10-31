####################################################################
# DAPMemoryDataReferences.py
#import this using
# from DAPMemoryDataReferences import *
####################################################################

# All data references for the DAP subcomponents are memory references (except for the constants ref)
# data reference rows are fed to the subcomponents by the main DAP component
# in general each subcomponent uses only a subset of the supplied data rows
dataReferences = [

    {"type" : "constants",
     "name" : "Constants",
     "columns" : ["One"],
     "values" : [1]
    },

    # from PreDAPDataAssembly; sorting is by (zone, hnhinc5s, hhid, pTypeDAP, age, personId)

    {"type" : "memory",
     "name" : "Persons",
     "columns" : [  "personid",     	# 0   x
                    "hhid",     		# 1   x
                    "hhzon",       		# 2   x
                    "pTypeDAP",   		# 3   x
                    "hhinc5s",    		# 4   x
                    "hhsize",   		# 5   x
                    "hchild1",  		# 6   x
                    "hchild2",  		# 7   x
                    "hchild3",  		# 8   x
                    "hstud",    		# 9
                    "hftw", 			# 10
                    "hptw", 			# 11
                    "hnwa", 			# 12  x
                    "hsen", 			# 13
                    "age",  			# 14  # a category in TBI, not actual age
                    "hchildren",    	# 15
                    "hworkers",			# 16
                    "hchildlt16",		# 17
                    "schZoneId"         # 18  # moved from end to keep mapping constant after removal of sqrootage
                    "hh1Person",		# 19
                    "female",			# 20
                    "hpotworkad",		# 21
                    "hnochildre",		# 22
                    "hadults",			# 23
                    "ctype",			# 24
                    "workzoneid",		# 25
                    "noregwkplc",       # 26
                    "nCars",            # 27   x
                    "noCarsInHh",       # 28   x
                    "wkGtCarGt0",       # 29
                    "logsum",           # 30
                    "logRtToWk",        # 31
                    "wlkTraccWk",       # 32
                ]
    },
     

    {"type" : "memory",
     "name" : "Zones",
     "columns" : [
                  "zoneId",             # 0   x
                  "ext_dist",           # 1   x
                  "tw_acc",             # 2   x
                  "mix_dens",           # 3
                  "temp_hwy",           # 4
                 ] 
    },

    # this is added so submodels can get information related to workplace zone; could also just set workzone data here 
    {"type" : "memory",
     "name" : "AllZones",
     "columns" : [
                  "zoneId",             # 0   x
                  "ext_dist",           # 1   
                  "tw_acc",             # 2
                  "mix_dens",           # 3
                  "temp_hwy",           # 4
                 ] 
    },



    
    {"type" : "memory",
     "name" : "Output",     
     "isOutput": "true",
     "columns" : ["personid", "dapId"] # note: this value will be used to update SubmodelResults
    }, 

    # child1 doesn't actually get any input from here; including here as example
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
     #                0            1           2           3          4              5
     "columns" : ["nC1_Sch",   "nC1_NMT",  "nC1_SAH",  "nC1_OOA",  "nC1_Ext",  "nC1_Mandatory",# 0- 5 Child1 (0-5 years)
                  "nC2_Sch",   "nC2_NMT",  "nC2_SAH",  "nC2_OOA",  "nC2_Ext",  "nC2_Mandatory",# 6-11 Child2 (5-15 years)
                  "nC3_Sch",   "nC3_NMT",  "nC3_SAH",  "nC3_OOA",  "nC3_Ext",  "nC3_Mandatory",#12-17  Child3 16+
                  "dNWA_Sch", "nNWA_NMT", "nNWA_SAH", "nNWA_OOA", "nNWA_Ext", "nNWA_Mandatory",#18-23 Non-Working Adult 
                  "dSen_Sch", "nSen_NMT", "nSen_SAH", "nSen_OOA", "nSen_Ext", "nSen_Mandatory",#24-29 Senior
                  "dPTW_Sch", "nPTW_NMT", "nPTW_SAH", "nPTW_OOA", "nPTW_Ext", "nPTW_Mandatory",#30-35 Part-Time Worker
                  "dFTW_Sch", "nFTW_NMT", "nFTW_SAH", "nFTW_OOA", "nFTW_Ext", "nFTW_Mandatory" #36-41 Full-Time Worker
                  #"dAdS_Sch", "nAdS_NMT", "nAdS_SAH", "nAdS_OOA", "nAdS_Ext", "nAds_Mandatory" #7 Adult Student results not needed 
                  # there are 4 extra rows 
                  
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
