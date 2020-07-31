; Do not change filenames or add or remove FILEI/FILEO statements using an editor. Use Cube/Application Manager.
RUN PGM=NETWORK MSG='TEMP: set rail zone node field'
;FILEI LINKI[4] = "%T_PRIORITY_PATH%"
;FILEI LINKI[3] = "%T_MANTIME_PATH%"
;FILEI LINKI[2] = "%T_DISTANCE_PATH%"
FILEO NETO = "%SCENARIO_DIR%\TransitBase.NET"
FILEI NETI[1] = "%SCENARIO_DIR%\HWY_ALL_NET.net"

    ZONES=%zones%

    ; TODO: Move this into the GeoDB
    PHASE = NODEMERGE 
    IF (N = 170600)
        FAREZONE = 1
      ENDIF
      IF (N = 170601)
        FAREZONE = 2
      ENDIF
      IF (N = 45138)
        FAREZONE = 3
      ENDIF
      IF (N = 170608)
        FAREZONE = 4
      ENDIF
      IF (N = 170607)
        FAREZONE = 5
      ENDIF
      IF (N = 170632)
        FAREZONE = 6
      ENDIF
      
    ENDPROCESS

ENDRUN
