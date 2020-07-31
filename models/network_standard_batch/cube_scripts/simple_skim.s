; Do not change filenames or add or remove FILEI/FILEO statements using an editor. Use Cube/Application Manager.
RUN PGM = HIGHWAY MSG = 'Assignment Period: %ASSIGNNAME%'
FILEI MATI[4] = "%TRIP_DIR%\HWY_SPC_AUTO_TRIP_%ITER%_%PER%.trp"
FILEI MATI[3] = "%TRIP_DIR%\HWY_EXT_TRIP_%ITER%_%PER%.trp"
FILEI MATI[2] = "%TRIP_DIR%\TRK_TRIP_%ITER%_%PER%.trp"

FILEO MATO[1] = "%SCENARIO_DIR%\simple_skim.tmp",
                 MO = 101-102, NAME = litime_skim, time_skim, DEC[1] = 5 * 120

FILEI NETI = "%SCENARIO_DIR%\%HWY_NET%"
FILEI LOOKUPI[1] = "%LU_will2pay%"
FILEI MATI[1] = "%TRIP_DIR%\HWY_AUTO_TRIP_%ITER%_%PER%.TRP"

    PHASE = LINKREAD

        T0      = LI.TIME
        IF (LI.CAPACITY = 0)
            T0  = 99999
        ENDIF
        LW.SEGMENT_ID  = LI.SEGMENT_ID
        C       = LI.CAPACITY * %CAPFAC%
        Alpha   = LI.Alpha
        Beta    = LI.Beta
        LINKCLASS = LI.RCI
        
        

    ENDPHASE

    PHASE=ILOOP

      MW[1] = MI.1.1    MW[2] = MI.1.2    MW[3] = MI.1.3    MW[4] = MI.1.4    MW[5] = MI.1.5 ; SOV Work
      MW[6] = MI.1.6    MW[7] = MI.1.7    MW[8] = MI.1.8    MW[9] = MI.1.9    MW[10]= MI.1.10 ; HOV2 Work
      MW[11]= MI.1.11   MW[12]= MI.1.12   MW[13]= MI.1.13   MW[14]= MI.1.14   MW[15]= MI.1.15 ; HOV3 Work
      MW[16]= MI.1.16   MW[17]= MI.1.17   MW[18]= MI.1.18   MW[19]= MI.1.19   MW[20]= MI.1.20 ; SOV NON Work
      MW[21]= MI.1.21   MW[22]= MI.1.22   MW[23]= MI.1.23   MW[24]= MI.1.24   MW[25]= MI.1.25 ; HOV2 NON Work
      MW[26]= MI.1.26   MW[27]= MI.1.27   MW[28]= MI.1.28   MW[29]= MI.1.29   MW[30]= MI.1.30 ; HOV3 NON Work
      MW[119] = MI.1.31    MW[120] = MI.1.32 + MI.3.1 + MI.3.2 + MI.3.3 + MI.4.1 + MI.4.2 + MI.4.3    ; SOVInc1, SOVInc25 - No Transponder / Externals / Spec Gen in with SOVInc25
      ; TODO: separate the Externals / Spec Gen in with SOVInc25 into their own by mode

    ; *** SKIMS ***
      ; Build SOV Truck Paths
      PATHLOAD PATH = TIME,
               TRACE = (I=1 & J=1000),
               MW[101] = PATHTRACE(LI.TIME), MW[102] = PATHTRACE(TIME)

    ENDPHASE
ENDRUN
