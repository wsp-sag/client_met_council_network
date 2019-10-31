; Do not change filenames or add or remove FILEI/FILEO statements using an editor. Use Cube/Application Manager.
RUN PGM=NETWORK MSG='TEMP: set rail zone node field'
;FILEI LINKI[4] = "%T_PRIORITY_PATH%"
;FILEI LINKI[3] = "%T_MANTIME_PATH%"
;FILEI LINKI[2] = "%T_DISTANCE_PATH%"
FILEO NETO = "%SCENARIO_DIR%\TransitBase.NET"
FILEI NODEI[1] = "%SCENARIO_DIR%\transit_node.dbf"
FILEI LINKI[1] = "%SCENARIO_DIR%\transit_link.dbf"

    ZONES=%zones%

    ; TODO: Move this into the GeoDB
    PHASE = NODEMERGE FILEI = NI.1 
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
