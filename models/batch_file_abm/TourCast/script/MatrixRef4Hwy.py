##################################################
# MatrixRef4Hwy.py
#       Matrix References with 4 Hwy skims
#
##################################################

from MatrixKeyValues import *


matrixReferences = [
    {"type" : "matrix",
     "name" : "AMPeak",
     "isHighwayTimeSpanMatrix" : "true",
     "startTime" : "6", #6:00 am
     "endTime" : "9.5",  # 9.5 for an endTime means that this matrix includes up to the instant before 10:00AM (9:59:59.999...)
     "filename" : cube___AM_PEAK_MATRIX___, 
     "matrixNames" : ["dapdist", "daptoll", "daptime"]
    },

    {"type" : "matrix",
     "name" : "Midday",
     "isHighwayTimeSpanMatrix" : "true",
     "startTime" : "10", #10:00 am
     "endTime" : "14.5", # ends at instant before 15:00
     "filename" : cube___MIDDAY_MATRIX___, 
     "matrixNames" : ["dapdist", "daptoll", "daptime"]
    },

    {"type" : "matrix",
     "name" : "PMPeak",
     "isHighwayTimeSpanMatrix" : "true",
     "startTime" : "15", 
     "endTime" : "18.5", # ends at instant before 19:00
     "filename" : cube___PM_PEAK_MATRIX___, 
     "matrixNames" : ["dapdist", "daptoll", "daptime"]
    },

    {"type" : "matrix",
     "name" : "Overnight",
     "isHighwayTimeSpanMatrix" : "true",
     "startTime" : "19", #7:00 pm
     "endTime" : "5.5",  # wrap around midnight is OK; ends at instant before 6:00 AM
     "filename" : cube___OVERNIGHT_MATRIX___, 
     "matrixNames" : ["dapdist", "daptoll", "daptime"]
    }
]