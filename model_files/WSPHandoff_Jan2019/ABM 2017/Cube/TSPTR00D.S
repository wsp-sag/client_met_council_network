; Do not change filenames or add or remove FILEI/FILEO statements using an editor. Use Cube/Application Manager.
RUN PGM = PUBLIC TRANSPORT MSG='Build @TPER@ Walk Access Connectors'

  FILEO NTLEGO = "{SCENARIO_DIR}\XIT_WKACC_NTL_0_@TPER@.tmp"

  FILEO REPORTO = "{SCENARIO_DIR}\XIT_WKACC_RPT_0_@TPER@.rpt"

  FILEO NETO = "{SCENARIO_DIR}\XIT_WKACC_NET_0_@TPER@.NET"

  FILEI SYSTEMI = "{xit_system}"

  FILEI FACTORI[1] = "{CATALOG_DIR}\input\transit\@TPER@_WK_2010.FAC"

  FILEI LINEI[1] = "{xit_lines}"

  FILEI NETI = "{SCENARIO_DIR}\XIT_NET_0_@TPER@.net"

  REPORT Lines = T
  REREPORT Accesslegs = T, Egresslegs = T, Xferlegs = T, Lines = T, STOPNODES = T
  HDWAYPERIOD = @TOD@

  PHASE = LINKREAD
      _wlkspd = 2.5   ;mph
  ENDPHASE

  PHASE = DATAPREP
      PRINT LIST = 'Build Peak Walk Access Connectors', PRINTO = 0

      ;set transit travel time
      TRANTIME[5] = li.loctime       ; local
      TRANTIME[6] = li.loctime       ; local
      TRANTIME[7] = li.exptime       ; express
      TRANTIME[8] = li.lrttime       ; lrt
      TRANTIME[9] = li.exptime       ; commuter bus

      GENERATE,
      FROMNODE = 1-3061,
      TONODE = 3100-99999,
      DIRECTION = 3,
      ONEWAY = F,
      COST = li.Distance,
      EXTRACTCOST = (Li.Distance*60/_wlkspd),
      EXCLUDELINK = (li.RCI=1-5,13,14),   ;no walking on freeway, tollway,ramps and managed links
      MAXCOST = 4 * 0, 5 * 2,                 ;set maximum walking distance to 2 Miles
      MAXNTLEGS = 4 * 1, 5 * 99,
      NTLEGMODE = 1
  ENDPHASE

ENDRUN
