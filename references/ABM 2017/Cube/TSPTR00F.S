; Do not change filenames or add or remove FILEI/FILEO statements using an editor. Use Cube/Application Manager.
RUN PGM = PUBLIC TRANSPORT MSG = 'Build @TPER@ Transfer Access Connectors'
FILEO NTLEGO = "{SCENARIO_DIR}\XIT_XFER_NTL_0_@TPER@.TMP"
FILEO REPORTO = "{SCENARIO_DIR}\XIT_XFER_RPT_0_@TPER@.RPT"
FILEO NETO = "{SCENARIO_DIR}\XIT_XFER_NET_0_@TPER@.NET"
FILEI SYSTEMI = "{XIT_SYSTEM}"
FILEI FACTORI[1] = "{CATALOG_DIR}\INPUT\TRANSIT\@TPER@_WK_2010.FAC"
FILEI LINEI[1] = "{XIT_LINES}"
FILEI NETI = "{SCENARIO_DIR}\XIT_NET_0_@TPER@.net"
    
  SKIPBADLINES = Y
  REPORT Lines = T
  REREPORT Accesslegs = T, Egresslegs = T, Xferlegs = T, Lines = T, STOPNODES = T
  HDWAYPERIOD = @TOD@

  PHASE = LINKREAD
    _wlkspd = 2.5   ;mph
  ENDPHASE

  PHASE=DATAPREP
    PRINT LIST = 'Build Peak Transfer Connectors', PRINTO = 0
    ;set transit travel time
    TRANTIME[5] = li.loctime       ; local
    TRANTIME[6] = li.loctime       ; local
    TRANTIME[7] = li.exptime       ; express
    TRANTIME[8] = li.lrttime       ; lrt
    TRANTIME[9] = li.exptime       ; commuter bus

    ;*************************************
    ;    TRANSFER CONNECTORS
    ;*************************************
    ;generate the transfer legs based on transfer links
    GENERATE,
    FROMNODE = 3100 - 99999,
    TONODE = 3100 - 99999,
    DIRECTION = 3,
    ONEWAY = F,
    EXCLUDELINK = (li.RCI = 1-5, 13, 14),   ;no walking on freeway, tollway, and managed links
    COST = (Li.Distance * 60 / _wlkspd),
    MAXCOST = 4 * 1, 5 * 10,                 ;set maximum walking time to 10 minutes
    MAXNTLEGS = 4 * 1, 5 * 10,
    NTLEGMODE = 4
   
  ENDPHASE

ENDRUN
