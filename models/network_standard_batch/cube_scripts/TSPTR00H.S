; Do not change filenames or add or remove FILEI/FILEO statements using an editor. Use Cube/Application Manager.
RUN PGM = PUBLIC TRANSPORT MSG='Build %TPER% Drive Access Connectors'
FILEO NTLEGO = "%SCENARIO_DIR%/XIT_DRACC_NTL_0_%TPER%.NTL"
FILEO REPORTO = "%SCENARIO_DIR%/XIT_DRACC_RPT_0_%TPER%.RPT"
FILEO NETO = "%SCENARIO_DIR%/XIT_DRACC_NET_0_%TPER%.NET"
FILEI SYSTEMI = "%xit_system%"
FILEI FACTORI[1] = "%LOOKUP_DIR%/%TPER%_WK_2010.FAC"
FILEI LINEI[1] = "%xit_lines%"
FILEI NETI = "%SCENARIO_DIR%/XIT_NET_0_%TPER%.net"

    REPORT Lines = T
    REREPORT Accesslegs = T, Egresslegs = T, Xferlegs = T, Lines = T, STOPNODES = T
    HDWAYPERIOD = %TOD%

    PHASE = LINKREAD
        _wlkspd = 2.5;mph
        LW.roadtime = (LI.distance / LI.SPEED) * 60
    ENDPHASE

    PHASE = DATAPREP
        Print List = 'Build Peak Drive Access Connectors', printo = 0

        ;set transit travel time
        TRANTIME[5] = LI.loctime       ; local
        TRANTIME[6] = LI.loctime       ; local
        TRANTIME[7] = LI.exptime       ; express
        TRANTIME[8] = LI.lrttime       ; lrt
        TRANTIME[9] = LI.exptime       ; commuter bus

        Read FILE = "%xit_pnrnodes%"
    ENDPHASE

ENDRUN
