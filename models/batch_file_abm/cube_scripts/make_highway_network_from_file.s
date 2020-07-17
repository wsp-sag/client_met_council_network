RUN PGM = NETWORK MSG = "Read in Network from FILE"
FILEI NETI = "%SCENARIO_DIR%/complete_network.net"

FILEO NETO = "%SCENARIO_DIR%/highway.net"

IF (drive_access = 0 & bus_only = 0 & rail_only = 0) DELETE
IF (drive_access = 0 & bus_only = 1)
    LANES_AM = 1
    LANES_MD = 1
    LANES_PM = 1
    LANES_NT = 1
    ASSIGN_GROUP = 5
ENDIF

IF (rail_only = 1) 
    ASSIGN_GROUP = 100
ENDIF


ENDRUN
