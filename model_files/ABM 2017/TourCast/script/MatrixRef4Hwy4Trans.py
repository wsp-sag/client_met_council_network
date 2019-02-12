##################################################
#
#       Matrix References with 4 hwy skims
#               and 4 transit skims
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
     "matrixNames" : ["dapdist", "daptoll", "a2pdist", "a2ptoll", "a3pdist", "a3ptoll", "daptime", "a2ptime", "a3ptime", 
	 "dantime", "a2ntime", "a3ntime","dantoll", "a2ntoll", "a3ntoll"]
    },

    {"type" : "matrix",
     "name" : "Midday",
     "isHighwayTimeSpanMatrix" : "true",
     "startTime" : "10", #10:00 am
     "endTime" : "14.5", # ends at instant before 15:00
     "filename" : cube___MIDDAY_MATRIX___, 
     "matrixNames" : ["dapdist", "daptoll", "a2pdist", "a2ptoll", "a3pdist", "a3ptoll", "daptime", "a2ptime", "a3ptime", 
	 "dantime", "a2ntime", "a3ntime","dantoll", "a2ntoll", "a3ntoll"]
    },

    {"type" : "matrix",
     "name" : "PMPeak",
     "isHighwayTimeSpanMatrix" : "true",
     "startTime" : "15", 
     "endTime" : "18.5", # ends at instant before 19:00
     "filename" : cube___PM_PEAK_MATRIX___, 
     "matrixNames" : ["dapdist", "daptoll", "a2pdist", "a2ptoll", "a3pdist", "a3ptoll", "daptime", "a2ptime", "a3ptime", 
	 "dantime", "a2ntime", "a3ntime","dantoll", "a2ntoll", "a3ntoll"]
    },

    {"type" : "matrix",
     "name" : "Overnight",
     "isHighwayTimeSpanMatrix" : "true",
     "startTime" : "19", #7:00 pm
     "endTime" : "5.5",  # wrap around midnight is OK; ends at instant before 6:00 AM
     "filename" : cube___OVERNIGHT_MATRIX___, 
     "matrixNames" : ["dapdist", "daptoll", "a2pdist", "a2ptoll", "a3pdist", "a3ptoll", "daptime", "a2ptime", "a3ptime", 
	 "dantime", "a2ntime", "a3ntime","dantoll", "a2ntoll", "a3ntoll"]
    },

    {"type" : "matrix",
     "name" : "PeakWalkToTransit",
     "filename" : cube___PEAK_WALK_TO_TRANSIT_MATRIX___, 
     "matrixNames" : ["FARE", "FAREP", "TRNTIME", "WLKACC", "WLKXFER", "WLKEGR", "IWAIT", "XWAIT", "XFERS"]
    },

    {"type" : "matrix",
     "name" : "PeakDriveToTransit",
     "filename" : cube___PEAK_DRIVE_TO_TRANSIT_MATRIX___, 
     "matrixNames" : ["FARE", "FAREP", "DRACC", "TRNTIME", "WLKXFER", "WLKEGR", "IWAIT", "XWAIT", "XFERS"]
    },

    {"type" : "matrix",
     "name" : "OffPeakWalkToTransit",
     "filename" : cube___OFF_PEAK_WALK_TO_TRANSIT_MATRIX___, 
     "matrixNames" : ["FARE", "FAREP", "TRNTIME", "WLKACC", "WLKXFER", "WLKEGR", "IWAIT", "XWAIT", "XFERS"]
    },

    {"type" : "matrix",
     "name" : "OffPeakDriveToTransit",
     "filename" : cube___OFF_PEAK_DRIVE_TO_TRANSIT_MATRIX___, 
     "matrixNames" : ["FARE", "FAREP", "DRACC", "TRNTIME", "WLKXFER", "WLKEGR", "IWAIT", "XWAIT", "XFERS"]
    },

    {"type" : "matrix",
     "name" : "NonMotorized",
     "filename" : cube___NM_MATRIX___, 
     "matrixNames" : ["BIKEDIST", "WALKDIST"]
    }




    # output spec
    # none because this is in logsum mode
]