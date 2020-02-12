RUN PGM = NETWORK MSG = "Read in Network from FILE"
FILEI NETI = "%SCENARIO_DIR%/complete_network.net"

IF (drive_access = 0 & transit_access = 0) DELETE

FILEO NETO = "%SCENARIO_DIR%/highway.net"

ENDRUN
