####################################################################
# FullyJointTourParticipationSubmodelDataReferences.py
# i.e. Common information for PARTICIPATION submodels of the Fully Joint Tour Submodels
####################################################################


# the name of the corresponding class on the C# side:
# this allows for multiple scripts targeting the same component
modelComponentName="FullyJointTourSubmodelParticipation"  


parameters= {
             "PersonType": "Child1",
             "DAPType" : "Mandatory",  # other is "Nonmandatory"
             }

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
                  ]
    },

    {"type" : "memory",
     "dataType" : "int",
     "name" : "PersonBaseData",
     "columns" : [
                  "personId",
                  "HHID", 
                  "ptypeDAP", 
                  "gender"
                  ]
    },


    {"type" : "memory",
     "dataType" : "int",
     "name" : "HouseholdModeledData",
     "columns" : [
                "hhId2",        # 00
                "homeZoneId",   # 01
                "nCars",        # 02
                ]
},


    {"type" : "memory",
     "dataType" : "double",
     "name" : "PersonModeledData",
     "columns" : [
                "personId",    # 0 
                "hhId",        # 1 
                "homeZoneId",  # 2 for grouping
                "DAPId",       # 3 
                "tourCount",   # 4 
                "slotsArriv",  # 5 bit-encoded time slots via PersonTourDaySlots (Least significant bit is 3 am, next 47 bits run 3:30am to 2:30 am)
                "slotsDeprt",  # 6 bit-encoded time slots via PersonTourDaySlots (Least significant bit is 3 am, next 47 bits run 3:30am to 2:30 am)
                "slotsUsed"    # 7 bit-encoded time slots via PersonTourDaySlots (Least significant bit is 3 am, next 47 bits run 3:30am to 2:30 am)
                ]
},


    {"type" : "memory",
     "dataType" : "int",
     "name" : "DerivedValues",
     "columns" : [

                  "noCarsInHh", # 0 derived from hh nCars
                  "twoMand",    # 1 derived from PersonModeledData dapid
                  "workWStops", # 2 derived from PersonModeledData dap
                  "female",     # 3 derived from PersonBaseData gender
                  "wkGTcarGt0", # 4 Workers > Cars, cars > 0
				  "male"		# 5 derived from PersonBaseData gender
                 ]                          
    },

    {"type" : "memory",
     "dataType" : "double",
     "name" : "ModelResults",
     "columns" : [
                  "nOtherChild1Candidates",                      # 0
                  "nChild1_onTour",                              # 1 
                  "xChild1_onTour",                              # 2 
                  "nNWA_onTour",                                 # 3
                  "nSen_onTour",                                 # 4
                  "nChild2_onTour",                              # 5
                  "nChild3_onTour",                              # 6
                  "nPTW_onTour",                                 # 7
                  "nFTW_onTour",                                 # 8
                  "nStud_onTour",                                # 9
                  "xChild1_NoAdultsOnTour",                      # 10
                  "nAdultsLeft_xChild1_NoAdultsOnTour",          # 11
                  "OnlyNonMandOnTour",                           # 12
                  "OnlyMandOnTour",                              # 13
                  "jointTourSizeRatio",                          # 14
                  "logMaxTimeAssumingParticipating",             # 15
                  "logTimeWindowReductionAssumingParticipating", # 16
                  "xChild23_NoAdultsOnTour",                     # 17
                  "nAdultsLeft_xChild23_NoAdultsOnTour",         # 18	
                  "xAdults_NoChildOnTour",        				 # 19					  
                 ]                          
    }
    
]

# Matrices are different enough to require their own structure:
matrixReferences = [ ]
# for now none 

# ######################  model structure section  ##########################

altIntrinsicValues= [0,1] 

# not used thus far:
# friendly descriptions of the alternatives, maybe for UI display somehow
altNames = ["Does not participate", "Participates"]  #

# 'binary'
logitType = "MultinomialLogit"

durableCoeffMap={
       "Constants" : [[0,0,1]],
	   "HouseholdModeledData" : [[2,1,1]]                
}

transientCoeffMap={
    
     "DerivedValues" : [
                        [1,0,1],[5,1,1]
],
     "ModelResults" : [
                       [ 3, 2, 1],
					   [ 5, 3, 4],
					   [12, 7, 8]
                      ],
     
}

segmentDefinitions = [
#  friendly name     , input data ref, offset in input, range of values (order relates to coeff order in segmentCoeffMap)
# compound segmentation for 8 person types x 2 dap patterns, where nonMand pattern = 1, mand pattern = 2
 {'Name': 'Household income ', 'DataRef': 'HouseholdBaseData','Offset': 1, 'DataRange': [0,1,2,3,4]}
]