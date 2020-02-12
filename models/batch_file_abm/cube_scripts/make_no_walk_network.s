RUN PGM = NETWORK MSG = "Read in Network from FILE"
FILEI NETI[1] = "SCENARIO_DIR%/complete_network.net"

IF (isDriveLin = 0 & isTranLink = 0 & isBikeLink = 0) DELETE

FILEO NETO = "%SCENARIO_DIR%/no_walk_network.net"

ENDRUN
