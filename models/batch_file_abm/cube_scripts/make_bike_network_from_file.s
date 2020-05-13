RUN PGM = NETWORK MSG = "Read in Network from FILE"
FILEI NETI[1] = "%SCENARIO_DIR%/complete_network.net"

IF (bike_access = 0) DELETE

FILEO NETO = "%SCENARIO_DIR%/bike.net"
  
ENDRUN
