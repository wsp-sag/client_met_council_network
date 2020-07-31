; Do not change filenames or add or remove FILEI/FILEO statements using an editor. Use Cube/Application Manager.
RUN PGM=NETWORK MSG='TEMP: set rail zone node field'
;FILEI LINKI[4] = "%T_PRIORITY_PATH%"
;FILEI LINKI[3] = "%T_MANTIME_PATH%"
;FILEI LINKI[2] = "%T_DISTANCE_PATH%"
FILEO NETO = "%SCENARIO_DIR%\TransitBase.NET"
FILEI NETI[1] = "%SCENARIO_DIR%\HWY_ALL_NET.net"

    ZONES=%zones%

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
