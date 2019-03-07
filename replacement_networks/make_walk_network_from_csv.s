RUN PGM = NETWORK MSG = "Read in Network from CSV"
FILEI LINKI[1] = "%WALK_LINK_PATH%"",
  VAR = ID, A, B, DISTANCE, COUNTY, AREA, CENTROID, geometry, isPedLink,
  REV = 1
  ; I'm manually specifying the column names because I can't get START to work.
  ; START = (SUBSTR(RECORD, 1, 2) == 'ID')
ZONES = 3061
FILEI NODEI[1] = "%WALK_NODE_PATH%",
  VAR = OSMID, ID, GEOMETRY
FILEO NETO = "%SCENARIO_DIR%/walk.net"
  
ENDRUN
