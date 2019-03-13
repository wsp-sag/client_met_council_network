RUN PGM = NETWORK MSG = "Read in Network from CSV"
FILEI LINKI[1] = "%WALK_LINK_PATH%",
  REV = 1
  ; I'm manually specifying the column names because I can't get START to work.
  ; 
ZONES = 3061
FILEI NODEI[1] = "%WALK_NODE_PATH%"
  
  BIKE = 3
  B1DIST = 0
  B2DIST = 0
  B3DIST = DISTANCE
  
FILEO NETO = "%SCENARIO_DIR%/walk.net"
  
ENDRUN
