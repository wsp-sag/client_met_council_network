RUN PGM = NETWORK MSG = "Read in Network from FILE"
FILEI LINKI[1] = "%LINK_PATH%",
	  REV = 1
ZONES = 3061
FILEI NODEI[1] = "%NODE_PATH%"
  
IF (isBikeLink = 0) DELETE

FILEO NETO = "%SCENARIO_DIR%/bike.net"
  
ENDRUN