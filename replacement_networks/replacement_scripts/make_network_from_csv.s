RUN PGM = NETWORK MSG = "Read in Network from CSV"
FILEI LINKI[1] = "osm_roadway_network_builder_022119/links.csv",
  VAR = ID, A, B, COUNTY, T_PRIORITY, BIKE, AREA, HOV, AADT, AM_CNT, MD_CNT, 
  PM_CNT, NT_CNT, DY_CNT, ASGNGRP10, ASGNGRP15, ASGNGRP40, LANES10, LANES15, 
  LANES40, CENTROID, RC_NUM, DISTANCE, T_MANTIME,
  REV = 1
  ; I'm manually specifying the column names because I can't get START to work.
  ; START = (SUBSTR(RECORD, 1, 2) == 'ID')
ZONES = 3061
FILEI NODEI[1] = "osm_roadway_network_builder_022119/nodes.csv",
  VAR = N, X, Y
FILEO NETO = "osm_roadway_network_builder_022119/link.net"
  
ENDRUN
