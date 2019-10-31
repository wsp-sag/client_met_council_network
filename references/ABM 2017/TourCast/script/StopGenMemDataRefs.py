####################################################################
# StopGenMemDataRefs.py
# import this using
# from StopGenMemDataRefs import *
####################################################################

# All data references for the Stop Generation subcomponents are memory references 
# data reference rows are fed to the subcomponents by the main component
# in general each subcomponent uses only a subset of the supplied data rows
dataReferences = [
    # Used for segmentation
    {"type" : "constants",
     "name" : "Constants",
     "columns" : ["One"],
     "values" : [1]
    },

    {"type" : "memory",
     "dataType" : "int",
     "name" : "Household",
     "columns" : [  "hhinc5s",      # 0  For possible future segmentation but for now most models use indicators
					"numCarsInHh",	# 1 
					"noCarsInHh",   # 2
                    "hhIncLt50k",   # 3					
                    "hhIncGt100k",  # 4		
				    "hChildren"     # 5
                 ],
    },
    {"type" : "memory",
     "dataType" : "int",
     "name" : "Person",
     "columns" : [
                    "isChild2",         # 0						
                    "isChild3",         # 1
                    "isPartTimeWorker", # 2
                    "isFullTimeWorker", # 3					
                    "male",             # 4
					"ageGt35",			# 5
					"isSenior",         # 6
					"isAdultStudent",   # 7
					"isNonWorkingAdult" # 8
					
                 ],
    },
    {"type" : "memory",
     "dataType" : "int",
     "name" : "Day",
     "columns" : [  
					"numFullyJointNMT",     # 0
					"numIndNonMnd",			# 1	
					"numMandatory",			# 2		
					"numWork",				# 3
					"numSchool",			# 4
					"numUniversity",		# 5
                    "numSocialRecreation",  # 6	
					"numPersonalBusiness",  # 7
                    "schoolEscortHT1",      # 8
                    "schoolEscortHT2",      # 9						
					"2+schoolEscort",		# 10
                    "1+Mandatory",          # 11   
                    "1+Work",               # 12
					"1+FJT"					# 13
                 ],
    },
    {"type" : "memory",
     "dataType" : "double",
     "name" : "Tour",
     "columns" : [  "purpose",                  # 0     For segmentation
                    "duration",                 # 1     In # of half hour periods
                    "ln1+availablePeriodsHt1",  # 2
                    "ln1+availablePeriodsHt2",  # 3
                    "arrivalBefore8:00am",     	# 4					
                    "arrivalBefore9:00am",      # 5					
                    "arrival9:00amTo12pm",      # 6		
                    "arrivalAfter12:00pm",      # 7
                    "arrivalAfter3:00pm",       # 8	
                    "arrivalAfter4:00pm",       # 9
                    "departureBefore9:00am",    # 10	
                    "departureBefore10:00am",   # 11
                    "departure9:00amTo12pm",    # 12					
                    "departureBefore12:00pm",   # 13
                    "departureAfter4:00pm",     # 14
                    "departureAfter6:00pm",     # 15
					"arrivalBefore10:00am",		# 16
					"arrivalAfter7:00pm"		# 17
                 ],
    },
    {"type" : "memory",
     "dataType" : "int",
     "name" : "FullyJointTour",
     "columns" : [  "groupSize",				# 0             
					"groupSizeEq2",             # 1
                    "onlyChildren",             # 2
                    "1+adults",                 # 3
                    "onlyMales",                # 4
                    "1+females",                # 5
                    "1+senior",                 # 6
                    "1+worker",                 # 7
                    "1+mandDap",                # 8
                 ],
     },
    {"type" : "memory",
     "dataType" : "int",
     "name" : "WorkBasedSubtour",
     "columns" : [  "parentDriveAlone",                # 0
                ],
     },
    {"type" : "memory",
     "dataType" : "double",
     "name" : "TourLevelOfService",
     "columns" : [  "roundTripDistance",                # 0
                    "mixedUseDensity",                  # 1
                    "employmentDensity",                # 2
                  ],
     },
    {"type" : "memory",
     "dataType" : "int",
     "name" : "StopsHalfTour1",
     "columns" : [  "totalStops",          # 0
                    "numWork",             # 1
                    "numMeal",             # 2
                    "numPersonalBusiness", # 3
                    "numSocialRecreation", # 4
                    "numEscort",           # 5
                    "1+University",        # 6
                    "1+Meal",              # 7
                    "1+Shop",              # 8
                    "1+PersonalBusiness",  # 8
                    "1+SocialRecreation",  # 9
                    "1+Escort",            # 10
                 ],
     },

]