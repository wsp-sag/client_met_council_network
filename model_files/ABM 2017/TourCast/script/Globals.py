numberOfZones = 3030    #from inspection of zonal data file http://www.h-gac.com/community/socioeconomic/forecasts/archive/documents/traffic_analysis_zones.xls
numberOfTimeSlotsInDay = 48 # 
from CubeKeyValues import *
randomSeed = 1234
# put this in durableCoeffs or transientCoeffs where values are segmented
# this can flush out situations where segmentation is not implemented properly
# by producing an exponentiated utility of infinity
placeholder = float('NaN')

#from OutingPurposeEnum in C# code:
purposeSchool = 1
purposeWork  = 2
purposeUniversity = 4,
purposeMeal = 8
purposeShop = 16
purposePersonalBusiness = 32
purposeSocialRecreation = 64
purposeEscort = 128
purposeSchoolEscort  = purposeEscort + purposeSchool
purposeFullyJointNMT = 256 
purposeWorkBased = 512
purposeIndNonMnd = 1024
purposeTourReturn = 2048


#tbi values
incLt25k = 0
inc25To50k = 1
inc50To75k = 2
inc75To100k = 3
incGt100k = 4

autoOpCost = 15 # cents per mile


# tour (and trip) modes
modeDA = 1
modeSR2 = 2
modeSR3 = 3
modeTW = 4
modeTD = 5
modeWK = 6
modeBK = 7
modeSB = 8

# mode synonyms
driveAlone = 1
sharedRide2 = 2
sharedRide3 = 3
walkToTransit = 4
driveToTransit = 5
walk = 6
bike = 7
schoolBus = 8
