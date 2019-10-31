####################################################################
# WorkBasedTourModeChoice.py
# Config for MultiModel component for tour mode choice models
####################################################################

from TourModeChoiceHomeBased import *

subModels={ # the key here is OutingPurpose; if a ';' in the dictionary key, handles both of these separately;
           "WorkBased" : r"TourModeChoiceLogsum_WorkBased.py"
           }

dataReferences[5]["filename"] = cube___WORK_BASED_TOUR_TIME_OF_DAY_CHOICE___ # Tours
dataReferences[5]["columns"] =[

                   "personId",
                   "persTourId",      
                   "hhId",             
                   "homeZoneId", # for chunking
                   "origZoneId", # for chunking
                   "destZoneId",
                   "tourPurp",
                   "arrival", 
                   "departure",
                   #"noStopTour",
                   "parentMode" ]

# .append("parentMode")  # see if this works it does but I want to remove the noStopTour
dataReferences[6]["filename"] = cube___WORK_BASED_STOPS___ # Stops

dataReferences[12]["filename"] = cube___WORK_BASED_TOUR_MODE_CHOICE___ # output
dataReferences[13]["filename"] = cube___WORK_BASED_TOUR_MODE_CHOICE_SUMMARY___ #  output stats

#dataReferences[6]["columns"] =  [
#                  "nAdults",   # for fully joint tours
#                  "nChildren", # for fully joint tours
#                  "xFtwInTour",# for fully joint tours
#                  "nTours",    # for work tour calc
#                  "nWorkTours",# for work tour calc
#                  ]  # derived tour column substitution
#    
#dataReferences[10]["queryString"] = "SELECT taz, [term_time], [park_cost], [mix_dens] from [data$]"
#dataReferences[10]["columns "] = ["taz", "term_time", "park_cost", "mix_dens"]


