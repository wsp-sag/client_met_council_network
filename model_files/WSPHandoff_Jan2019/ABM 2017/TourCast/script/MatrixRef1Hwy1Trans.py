##################################################
# MatrixRef1Hwy1Trans.py
#       Matrix References with 1 hwy skim
#               and 1 transit skim
#
##################################################

from MatrixKeyValues import *

matrixReferences = [
    {"name" : "TransitAccessMatrix",
     "filename" : cube___PEAK_WALK_TO_TRANSIT_MATRIX___, # file paths MUST BE RAW strings (preceded by 'r')
     "matrixNames" : ["WLKXFER"] 
    },

    {"name" : "DistanceMatrixOD",
     "filename" : cube___OD_DISTANCE_MATRIX___, #NOTE: NOT CORRECT DATA: need a matrix with log(1 + round trip distance)
     "matrixNames" : ["dapdist", "lnrtdist"] # using drive alone no tolls; 
    }
]