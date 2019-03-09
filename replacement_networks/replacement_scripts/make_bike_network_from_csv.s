RUN PGM = NETWORK MSG = "Read in Network from CSV"
FILEI LINKI[1] = "%BIKE_LINK_PATH%",
	VAR = %BIKE_LINK_VAR%,
  REV = 1
  ; I'm manually specifying the column names because I can't get START to work.
  ; 
ZONES = 3061
FILEI NODEI[1] = "%BIKE_NODE_PATH%",
  VAR = %BIKE_NODE_VAR%
  
FILEO NETO = "%SCENARIO_DIR%/bike.net"
  
ENDRUN
