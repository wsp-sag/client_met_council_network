####################################################################                                                                                                                                                                                           
# TourTimeOfDayIndNonMandNonEscort.py
# specifies input files which are outputs of tour destination choice for the tours
# and the TOD output from fully joint for person schedules
# and output files
####################################################################                                                                                                                                                                                           

#Same configuration is used for non-escort and escort individual non-mandatory tours
# inputTourFileName=cube___INDIVIDUAL_NON_MANDATORY_TOUR_DESTINATION_CHOICES___
#inputPersonDaySchedulesFileName=cube___FULLY_JOINT_TOUR_PERSON_SCHEDULES___
#outputTourFileName=cube___INDIVIDUAL_NON_MANDATORY_TOUR_TIME_OF_DAY_CHOICE___
#outputPersonDaySchedulesFileName=cube___INDIVIDUAL_NON_MANDATORY_TOUR_TIME_OF_DAY_PERSON_SCHEDULES___

# except for file names, 
# Same configuration is used for non-escort and escort individual non-mandatory tours
from TourTimeOfDayIndNonMand import *
dataReferences[0]["filename"] = cube___INDIVIDUAL_NON_MANDATORY_TOUR_DESTINATION_CHOICES___
dataReferences[1]["filename"] = cube___FULLY_JOINT_TOUR_PERSON_SCHEDULES___
dataReferences[3]["filename"] = cube___INDIVIDUAL_NON_MANDATORY_TOUR_TIME_OF_DAY_CHOICE___
dataReferences[4]["filename"] = cube___INDIVIDUAL_NON_MANDATORY_TOUR_TIME_OF_DAY_PERSON_SCHEDULES___
