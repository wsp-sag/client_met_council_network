RUN PGM = NETWORK MSG = "Read in network from fixed width file"
FILEI LINKI[1] = %LINK_DATA_PATH%, VAR = A,1-20, B,21-40, assignment_group,41-60
FILEI NODEI[1] = %NODE_DATA_PATH%, VAR = N,1-20, X,21-40, Y, 41-60, drive_node,61-80
FILEO NETO = "%SCENARIO_DIR%/complete_network.net"
    ZONES = %zones%

ENDRUN