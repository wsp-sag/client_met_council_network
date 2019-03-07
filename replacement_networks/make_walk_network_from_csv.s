RUN PGM = NETWORK MSG = "Read in Network from CSV"
FILEI LINKI[1] = "%WALK_LINK_PATH%",
	VAR = ID, A, B, DISTANCE, COUNTY, AREA, CENTROID, isPedLink,  
  REV = 1
  ; I'm manually specifying the column names because I can't get START to work.
  ; 
ZONES = 3061
FILEI NODEI[1] = "%WALK_NODE_PATH%",
  VAR = osmid, id,
  RENAME = id-N
  
FILEO NETO = "%SCENARIO_DIR%/walk.net"
  
ENDRUN
