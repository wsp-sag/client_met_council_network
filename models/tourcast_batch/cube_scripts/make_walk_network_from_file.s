RUN PGM = NETWORK MSG = "Read in Network from FILE"
FILEI NETI[1] = "%SCENARIO_DIR%/complete_network.net"

  IF (walk_access = 0) DELETE
  
  B1DIST = 0
  B2DIST = 0
  B3DIST = DISTANCE
  
FILEO NETO = "%SCENARIO_DIR%/walk.net"
  
ENDRUN
