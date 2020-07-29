; Do not change filenames or add or remove FILEI/FILEO statements using an editor. Use Cube/Application Manager.
RUN PGM = NETWORK MSG = 'TEMP: extract link and node dbfs'
FILEO NODEO = "%SCENARIO_DIR%\transit_node.dbf"
FILEO LINKO = "%SCENARIO_DIR%\transit_link.dbf"
FILEI LINKI[1] = "%SCENARIO_DIR%\HWY_ALL_NET.net"

PHASE=NODEMERGE FILEI=NI.1 
      IF (N=171203)
        FAREZONE=1
      ENDIF
      IF (N=171202)
        FAREZONE=2
      ENDIF
      IF (N=171201)
        FAREZONE=3
      ENDIF
      IF (N=171200)
        FAREZONE=4
      ENDIF
      IF (N=171199)
        FAREZONE=5
      ENDIF
      IF (N=171198)
        FAREZONE=6
      ENDIF
      IF (N=17197)
        FAREZONE=7
      ENDIF
      
    ENDPHASE 
    
ENDRUN
