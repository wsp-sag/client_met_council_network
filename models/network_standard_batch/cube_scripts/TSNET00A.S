; Do not change filenames or add or remove FILEI/FILEO statements using an editor. Use Cube/Application Manager.
RUN PGM = NETWORK MSG = 'TEMP: extract link and node dbfs'
FILEO NODEO = "%SCENARIO_DIR%\transit_node.dbf"
FILEO LINKO = "%SCENARIO_DIR%\transit_link.dbf"
FILEI LINKI[1] = "%SCENARIO_DIR%\HWY_ALL_NET.net"


    
ENDRUN
