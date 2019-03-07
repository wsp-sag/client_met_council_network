RUN PGM = NETWORK MSG = "Read in Network from CSV"
FILEI LINKI[1] = "%HWY_LINK_PATH%"",
	VAR = ID,  A, B, DISTANCE, COUNTY, T_PRIORITY, BIKE, AREA, HOV, AADT, AM_CNT, 
	MD_CNT, PM_CNT,   NT_CNT, DY_CNT, ASGNGRP, LANES, CENTROID, RC_NUM, isDriveLink, 
  REV = 1
  ; I'm manually specifying the column names because I can't get START to work.
  ; 
ZONES = 3061
FILEI NODEI[1] = "%HWY_NODE_PATH%",
  VAR = OSMID, ID
FILEO NETO = "%SCENARIO_DIR%/link.net"
  
ENDRUN
