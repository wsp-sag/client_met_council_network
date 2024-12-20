; Do not change filenames or add or remove FILEI/FILEO statements using an editor. Use Cube/Application Manager.
RUN PGM = NETWORK MSG = 'TEMP: set rail zone node field'
FILEI LINKI[4] = "C:\Users\helseljw\OneDrive - WSP O365\met_council\model_files\WSPHandoff_Jan2019\ABM 2017\Input\network\T_Priority.dbf"
FILEI LINKI[3] = "C:\Users\helseljw\OneDrive - WSP O365\met_council\model_files\WSPHandoff_Jan2019\ABM 2017\Input\network\T_MANTIME.dbf"
FILEI LINKI[2] = "C:\Users\helseljw\OneDrive - WSP O365\met_council\model_files\WSPHandoff_Jan2019\ABM 2017\Input\network\Distances.dbf"
FILEO NETO = "{SCENARIO_DIR}\TransitBase.NET"
FILEI NODEI[1] = "{SCENARIO_DIR}\node.dbf"
FILEI LINKI[1] = "{SCENARIO_DIR}\link.dbf"

  ZONES = {zones}
  
  ; TODO: Move this into the GeoDB
  PHASE = NODEMERGE FILEI = NI.1 
    IF (N = 17502)
      FAREZONE = 1
    ENDIF
    
    IF (N = 19759)
      FAREZONE = 2
    ENDIF
    
    IF (N = 19761)
      FAREZONE = 3
    ENDIF
    
    IF (N = 19762)
      FAREZONE = 4
    ENDIF
    
    IF (N = 19763)
      FAREZONE = 5
    ENDIF
    
    IF (N = 19764)
      FAREZONE = 6
    ENDIF
    
  ENDPROCESS
    
ENDRUN
