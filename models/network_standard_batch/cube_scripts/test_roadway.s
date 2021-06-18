RUN PGM = HIGHWAY, MSG = 'Assignment Period: %ASSIGNNAME%'

   FILEI NETI = "%SCENARIO_DIR%\%HWY_NET%"
   FILEI MATI[1] = "%SCENARIO_DIR%\HWY_AUTO_TRIP_%ITER%_%PER%.TRP"
   FILEI MATI[2] = "%SCENARIO_DIR%\TRK_TRIP_%ITER%_%PER%.trp"
   FILEI MATI[3] = "%SCENARIO_DIR%\HWY_EXT_TRIP_%ITER%_%PER%.trp"
   FILEI MATI[4] = "%SCENARIO_DIR%\HWY_SPC_AUTO_TRIP_%ITER%_%PER%.trp"

   FILEO NETO = "%SCENARIO_DIR%\HWY_LDNET_%ITER%_%PER%.NET"
   FILEO PRINTO = "%SCENARIO_DIR%\HWY_LDNET_PRN_%ITER%_%PER%.txt"
   FILEO MATO = "%SCENARIO_DIR%\HWY_SKIM_%ITER%_%PER%.tmp", MO = 21-24

   DISTRIBUTEINTRASTEP ProcessID='Intrastep', ProcessList=1-%MAX_THREADS%

   ; Define assignment parameters ----------------------------------------------
   PARAMETERS RAAD = 0.0001 GAP = 0.0001 RELATIVEGAP = 0.00001 AAD = 0.01 MAXITERS = %HWY_ASSIGNITERS% COMBINE = EQUI
   FUNCTION TC[1] = T0 * (1 + ALPHA*(V/C)^(BETA))
   FUNCTION TC[2] = T0 * (1 + ALPHA*(V/C)^(BETA))
   FUNCTION TC[3] = T0 * (1 + ALPHA*(V/C)^(BETA))
   FUNCTION TC[4] = T0 * (1 + ALPHA*(V/C)^(BETA))
   FUNCTION TC[5] = T0 * (1 + ALPHA*(V/C)^(BETA))
   FUNCTION TC[6] = T0 * (1 + ALPHA*(V/C)^(BETA))
   FUNCTION TC[7] = T0 * (1 + ALPHA*(V/C)^(BETA))
   FUNCTION TC[8] = T0 * (1 + ALPHA*(V/C)^(BETA))
   FUNCTION TC[9] = T0 * (1 + ALPHA*(V/C)^(BETA))
   FUNCTION TC[10] = T0 * (1 + ALPHA*(V/C)^(BETA))
   FUNCTION TC[11] = T0 * (1 + ALPHA*(V/C)^(BETA))
   FUNCTION TC[12] = T0 * (1 + ALPHA*(V/C)^(BETA))
   FUNCTION TC[13] = T0 * (1 + ALPHA*(V/C)^(BETA))
   FUNCTION TC[14] = T0 * (1 + ALPHA*(V/C)^(BETA))
   FUNCTION TC[15] = T0 * (1 + ALPHA*(V/C)^(BETA))
   FUNCTION TC[99] = T0 * (1 + ALPHA*(V/C)^(BETA))

   FUNCTION V = VOL[1] + VOL[2] + VOL[3] + VOL[4] + VOL[5] +
                VOL[6] + VOL[7] + VOL[8] + VOL[9] + VOL[10] +
                VOL[11] + VOL[12] + VOL[13] + VOL[14] + VOL[15] +
                VOL[16] + VOL[17] + VOL[18] + VOL[19] +
				VOL[20] * %HWY_TRKFAC%

   ; Define toll price scheme --------------------------------------------------
   LOOKUP NAME = TOLL,
          LOOKUP[1] = 1,
          RESULT = 2,
          INTERPOLATE=Y,
          FAIL = 25,800,
          R = '0.00 25',
              '0.35 50',
              '0.54 150',
              '0.77 250',
              '0.93 350',
              '1.00 600'

   PHASE = LINKREAD

      ; Initialize price array -------------------------------------------------
	    ARRAY _PRICE_ARRAY = %PRICE_ARRAY_SIZE%
	    ARRAY _PRICE_INCREASE = %PRICE_ARRAY_SIZE%

      ; Set input variables ----------------------------------------------------
      T0 = LI.TIME
      IF (LI.CAPACITY == 0)
         T0 = 99999
      ENDIF

      C       = LI.CAPACITY * %CAPFAC%
      ALPHA   = LI.ALPHA
      BETA    = LI.BETA
      DISTANCE = LI.DISTANCE
      LINKCLASS = LI.RCI
	    LW.SEGMENT_ID = LI.SEGMENT_ID

      LW.HOV_TIME_PNLTY = 0
      LW.TOLL_PRICE_SOV = 0
      LW.MNPASS_CODE = LI.MNPASS_CODE
	    LW.MNPASS_PAY = LI.MNPASS_PAY
      IF (LW.MNPASS_PAY > 0)
         LW.TOLL_PRICE_SOV = 25
         LW.HOV_TIME_PNLTY = %HOV_TIME_PENALTY%
      ENDIF

      LW.TOLL_PRICE_HOV2 = LW.TOLL_PRICE_SOV
      LW.TOLL_PRICE_HOV3 = LW.TOLL_PRICE_SOV
      IF (%HWY_TOLLSETTING% == 2)
         LW.TOLL_PRICE_HOV2 = 0
         LW.TOLL_PRICE_HOV3 = 0
      ENDIF
      IF (%HWY_TOLLSETTING% == 3)
         LW.TOLL_PRICE_HOV3 = 0
      ENDIF

      ; Create an HOV lane group and a no truck lane group ---------------------
      IF (LI.HOV_NO_MNPASS > 0) ADDTOGROUP = 1
      IF (LI.MNPASS_CODE > 0 || LI.HOV_NO_MNPASS > 0) ADDTOGROUP = 2

      ; Generalized path cost expressions -------------------------------------
      LW.PATHCOST_SOV_INC_01 = T0 + (0.6 / %VOT_INCOME_01%) * ((DISTANCE * %AUTO_PER_MILE_COST%) + LW.TOLL_PRICE_SOV)
      LW.PATHCOST_SOV_INC_02 = T0 + (0.6 / %VOT_INCOME_02%) * ((DISTANCE * %AUTO_PER_MILE_COST%) + LW.TOLL_PRICE_SOV)
      LW.PATHCOST_SOV_INC_03 = T0 + (0.6 / %VOT_INCOME_03%) * ((DISTANCE * %AUTO_PER_MILE_COST%) + LW.TOLL_PRICE_SOV)
      LW.PATHCOST_SOV_INC_04 = T0 + (0.6 / %VOT_INCOME_04%) * ((DISTANCE * %AUTO_PER_MILE_COST%) + LW.TOLL_PRICE_SOV)
      LW.PATHCOST_SOV_INC_05 = T0 + (0.6 / %VOT_INCOME_05%) * ((DISTANCE * %AUTO_PER_MILE_COST%) + LW.TOLL_PRICE_SOV)

      LW.PATHCOST_HOV2_INC_01 = T0 + (0.6 / %VOT_INCOME_01%) * ((DISTANCE * %AUTO_PER_MILE_COST%) + (LW.TOLL_PRICE_HOV2 / %HWY_HOV2OCC%) + LW.HOV_TIME_PNLTY)
      LW.PATHCOST_HOV2_INC_02 = T0 + (0.6 / %VOT_INCOME_02%) * ((DISTANCE * %AUTO_PER_MILE_COST%) + (LW.TOLL_PRICE_HOV2 / %HWY_HOV2OCC%) + LW.HOV_TIME_PNLTY)
      LW.PATHCOST_HOV2_INC_03 = T0 + (0.6 / %VOT_INCOME_03%) * ((DISTANCE * %AUTO_PER_MILE_COST%) + (LW.TOLL_PRICE_HOV2 / %HWY_HOV2OCC%) + LW.HOV_TIME_PNLTY)
      LW.PATHCOST_HOV2_INC_04 = T0 + (0.6 / %VOT_INCOME_04%) * ((DISTANCE * %AUTO_PER_MILE_COST%) + (LW.TOLL_PRICE_HOV2 / %HWY_HOV2OCC%) + LW.HOV_TIME_PNLTY)
      LW.PATHCOST_HOV2_INC_05 = T0 + (0.6 / %VOT_INCOME_05%) * ((DISTANCE * %AUTO_PER_MILE_COST%) + (LW.TOLL_PRICE_HOV2 / %HWY_HOV2OCC%) + LW.HOV_TIME_PNLTY)

      LW.PATHCOST_HOV3_INC_01 = T0 + (0.6 / %VOT_INCOME_01%) * ((DISTANCE * %AUTO_PER_MILE_COST%) + (LW.TOLL_PRICE_HOV3 / %HWY_HOV3OCC%) + LW.HOV_TIME_PNLTY)
      LW.PATHCOST_HOV3_INC_02 = T0 + (0.6 / %VOT_INCOME_02%) * ((DISTANCE * %AUTO_PER_MILE_COST%) + (LW.TOLL_PRICE_HOV3 / %HWY_HOV3OCC%) + LW.HOV_TIME_PNLTY)
      LW.PATHCOST_HOV3_INC_03 = T0 + (0.6 / %VOT_INCOME_03%) * ((DISTANCE * %AUTO_PER_MILE_COST%) + (LW.TOLL_PRICE_HOV3 / %HWY_HOV3OCC%) + LW.HOV_TIME_PNLTY)
      LW.PATHCOST_HOV3_INC_04 = T0 + (0.6 / %VOT_INCOME_04%) * ((DISTANCE * %AUTO_PER_MILE_COST%) + (LW.TOLL_PRICE_HOV3 / %HWY_HOV3OCC%) + LW.HOV_TIME_PNLTY)
      LW.PATHCOST_HOV3_INC_05 = T0 + (0.6 / %VOT_INCOME_05%) * ((DISTANCE * %AUTO_PER_MILE_COST%) + (LW.TOLL_PRICE_HOV3 / %HWY_HOV3OCC%) + LW.HOV_TIME_PNLTY)

      LW.PATHCOST_TRK = T0 + (0.6 / %VOT_TRK%) * DISTANCE * %TRUCK_PER_MILE_COST%

   ENDPHASE ; LINKREAD

   PHASE = ILOOP

      ; Set demand matrices ----------------------------------------------------

      ; SOV, Income 1
      MW[1] = MI.1.1 + MI.1.16

      ; SOV, Income 2
      MW[2] = MI.1.2 + MI.1.17

      ; SOV, Income 3
      MW[3] = MI.1.3 + MI.1.18

      ; SOV, Income 4
      MW[4] = MI.1.4 + MI.1.19

      ; SOV, Income 5
      MW[5] = MI.1.5 + MI.1.20

      ; HOV2, Income 1
      MW[6] = MI.1.6 + MI.1.21

      ; HOV2, Income 2
      MW[7] = MI.1.7 + MI.1.22

      ; HOV2, Income 3
      MW[8] = MI.1.8 + MI.1.23

      ; HOV2, Income 4
      MW[9] = MI.1.9 + MI.1.24

      ; HOV2, Income 5
      MW[10] = MI.1.10 + MI.1.25

      ; HOV3, Income 1
      MW[11] = MI.1.11 + MI.1.26

      ; HOV3, Income 2
      MW[12] = MI.1.12 + MI.1.27

      ; HOV3, Income 3
      MW[13] = MI.1.13 + MI.1.28

      ; HOV3, Income 4
      MW[14] = MI.1.14 + MI.1.29

      ; HOV3, Income 5
      MW[15] = MI.1.15 + MI.1.30

      ; SOV, externals, special generators
      MW[16] = MI.3.1 + MI.4.1

      ; SOV, no transponders
      MW[17] = MI.1.31 + MI.1.32

      ; HOV2, externals, special generators
      MW[18] = MI.3.2 + MI.4.2

      ; HOV3, externals, special generators
      MW[19] = MI.3.3 + MI.4.3

      ; Trucks
      MW[20] = MI.2.3

      PATHLOAD PATH = LW.PATHCOST_SOV_INC_01,
                      EXCLUDEGRP = 1,
                      VOL[1] = MW[1]

      PATHLOAD PATH = LW.PATHCOST_SOV_INC_02,
                      EXCLUDEGRP = 1,
                      VOL[2] = MW[2]

      PATHLOAD PATH = LW.PATHCOST_SOV_INC_03,
                      EXCLUDEGRP = 1,
                      VOL[3] = MW[3]

      PATHLOAD PATH = LW.PATHCOST_SOV_INC_04,
                      EXCLUDEGRP = 1,
                      VOL[4] = MW[4]

      PATHLOAD PATH = LW.PATHCOST_SOV_INC_05,
                      EXCLUDEGRP = 1,
                      VOL[5] = MW[5]

      PATHLOAD PATH = LW.PATHCOST_HOV2_INC_01,
                      VOL[6] = MW[6]

      PATHLOAD PATH = LW.PATHCOST_HOV2_INC_02,
                      VOL[7] = MW[7]

      PATHLOAD PATH = LW.PATHCOST_HOV2_INC_03,
                      VOL[8] = MW[8]

      PATHLOAD PATH = LW.PATHCOST_HOV2_INC_04,
                      VOL[9] = MW[9]

      PATHLOAD PATH = LW.PATHCOST_HOV2_INC_05,
                      VOL[10] = MW[10]

      PATHLOAD PATH = LW.PATHCOST_HOV3_INC_01,
                      VOL[11] = MW[11]

      PATHLOAD PATH = LW.PATHCOST_HOV3_INC_02,
                      VOL[12] = MW[12]

      PATHLOAD PATH = LW.PATHCOST_HOV3_INC_03,
                      VOL[13] = MW[13]

      PATHLOAD PATH = LW.PATHCOST_HOV3_INC_04,
                      VOL[14] = MW[14]

      PATHLOAD PATH = LW.PATHCOST_HOV3_INC_05,
                      VOL[15] = MW[15]

      PATHLOAD PATH = LW.PATHCOST_SOV_INC_03,
                      VOL[16] = MW[16]

	  PATHLOAD PATH = LW.PATHCOST_SOV_INC_03,
                      EXCLUDEGRP = 2,
                      VOL[17] = MW[17]

	  PATHLOAD PATH = LW.PATHCOST_HOV2_INC_03,
                      VOL[18] = MW[18]

      PATHLOAD PATH = LW.PATHCOST_HOV3_INC_03,
                      VOL[19] = MW[19]

      PATHLOAD PATH = LW.PATHCOST_TRK,
                      EXCLUDEGRP = 2,
                      VOL[20] = MW[20]
					  
	  PATHLOAD PATH = LW.PATHCOST_SOV_INC_03,                 
                      EXCLUDEGRP = 1,
					  MW[21] = PATHTRACE(TIME),
                      MW[22] = PATHTRACE(LW.TOLL_PRICE_SOV),					  
					  MW[23] = PATHTRACE(LI.DISTANCE)
					  
	  PATHLOAD PATH = LW.PATHCOST_SOV_INC_03,                 
                      EXCLUDEGRP = 2,
					  MW[24] = PATHTRACE(TIME)

   ENDPHASE ; ILOOP

   PHASE = ADJUST

     ; Header for CSV ----------------------------------------------------------
     IF (LINKNO == 1 && ITERATION == 1)
       PRINT CSV = T LIST = 'Iteration,ANode,BNode,MNPASS_CODE,MNPASS_PAY,HOV,Volume,VC,TIME,DISTANCE,VHT,VMT,PRICE'  PRINTO = 1
     ENDIF

     ; Reset the price increase indicator --------------------------------------
     IF (LINKNO == 1)
      LOOP K = 1,%PRICE_ARRAY_SIZE%,1
        _PRICE_INCREASE[K] = 0
		  ENDLOOP
    ENDIF

     ; Update toll price -------------------------------------------------------
     IF (LW.MNPASS_CODE > 0 && C > 0)

    	_PRICE = TOLL(1,(V/C))

        IF (_PRICE > _PRICE_ARRAY[LW.MNPASS_CODE])

		       IF (_PRICE_INCREASE[LW.MNPASS_CODE] == 0)

		          _PRICE_INCREASE[LW.MNPASS_CODE] = 1

              _PRICE_ARRAY[LW.MNPASS_CODE] = _PRICE_ARRAY[LW.MNPASS_CODE] + 25
              IF ((_PRICE - _PRICE_INCREASE[LW.MNPASS_CODE]) > 200)
                 _PRICE_ARRAY[LW.MNPASS_CODE] = _PRICE_ARRAY[LW.MNPASS_CODE] + 25
              ENDIF

			        IF (_PRICE_ARRAY[LW.MNPASS_CODE] > %MAX_TOLL_PRICE%)
		            _PRICE_ARRAY[LW.MNPASS_CODE] = %MAX_TOLL_PRICE%
		          ENDIF

		      ENDIF

        ENDIF

     ENDIF

	   IF (LW.MNPASS_PAY > 0)
	      LW.TOLL_PRICE_SOV = _PRICE_ARRAY[LW.MNPASS_PAY]
	   ENDIF

     LW.TOLL_PRICE_HOV2 = LW.TOLL_PRICE_SOV
     LW.TOLL_PRICE_HOV3 = LW.TOLL_PRICE_SOV
     IF (%HWY_TOLLSETTING% == 2)
        LW.TOLL_PRICE_HOV2 = 0
        LW.TOLL_PRICE_HOV3 = 0
     ENDIF
     IF (%HWY_TOLLSETTING% == 3)
        LW.TOLL_PRICE_HOV3 = 0
     ENDIF

     ; Update generalized cost functions ---------------------------------------
     LW.PATHCOST_SOV_INC_01 = TIME + (0.6 / %VOT_INCOME_01%) * (DISTANCE * %AUTO_PER_MILE_COST% + LW.TOLL_PRICE_SOV)
     LW.PATHCOST_SOV_INC_02 = TIME + (0.6 / %VOT_INCOME_02%) * (DISTANCE * %AUTO_PER_MILE_COST% + LW.TOLL_PRICE_SOV)
     LW.PATHCOST_SOV_INC_03 = TIME + (0.6 / %VOT_INCOME_03%) * (DISTANCE * %AUTO_PER_MILE_COST% + LW.TOLL_PRICE_SOV)
     LW.PATHCOST_SOV_INC_04 = TIME + (0.6 / %VOT_INCOME_04%) * (DISTANCE * %AUTO_PER_MILE_COST% + LW.TOLL_PRICE_SOV)
     LW.PATHCOST_SOV_INC_05 = TIME + (0.6 / %VOT_INCOME_05%) * (DISTANCE * %AUTO_PER_MILE_COST% + LW.TOLL_PRICE_SOV)

     LW.PATHCOST_HOV2_INC_01 = TIME + (0.6 / %VOT_INCOME_01%) * (DISTANCE * %AUTO_PER_MILE_COST% + LW.TOLL_PRICE_HOV2 / %HWY_HOV2OCC%) + LW.HOV_TIME_PNLTY
     LW.PATHCOST_HOV2_INC_02 = TIME + (0.6 / %VOT_INCOME_02%) * (DISTANCE * %AUTO_PER_MILE_COST% + LW.TOLL_PRICE_HOV2 / %HWY_HOV2OCC%) + LW.HOV_TIME_PNLTY
     LW.PATHCOST_HOV2_INC_03 = TIME + (0.6 / %VOT_INCOME_03%) * (DISTANCE * %AUTO_PER_MILE_COST% + LW.TOLL_PRICE_HOV2 / %HWY_HOV2OCC%) + LW.HOV_TIME_PNLTY
     LW.PATHCOST_HOV2_INC_04 = TIME + (0.6 / %VOT_INCOME_04%) * (DISTANCE * %AUTO_PER_MILE_COST% + LW.TOLL_PRICE_HOV2 / %HWY_HOV2OCC%) + LW.HOV_TIME_PNLTY
     LW.PATHCOST_HOV2_INC_05 = TIME + (0.6 / %VOT_INCOME_05%) * (DISTANCE * %AUTO_PER_MILE_COST% + LW.TOLL_PRICE_HOV2 / %HWY_HOV2OCC%) + LW.HOV_TIME_PNLTY

     LW.PATHCOST_HOV3_INC_01 = TIME + (0.6 / %VOT_INCOME_01%) * (DISTANCE * %AUTO_PER_MILE_COST% + LW.TOLL_PRICE_HOV3 / %HWY_HOV3OCC%) + LW.HOV_TIME_PNLTY
     LW.PATHCOST_HOV3_INC_02 = TIME + (0.6 / %VOT_INCOME_02%) * (DISTANCE * %AUTO_PER_MILE_COST% + LW.TOLL_PRICE_HOV3 / %HWY_HOV3OCC%) + LW.HOV_TIME_PNLTY
     LW.PATHCOST_HOV3_INC_03 = TIME + (0.6 / %VOT_INCOME_03%) * (DISTANCE * %AUTO_PER_MILE_COST% + LW.TOLL_PRICE_HOV3 / %HWY_HOV3OCC%) + LW.HOV_TIME_PNLTY
     LW.PATHCOST_HOV3_INC_04 = TIME + (0.6 / %VOT_INCOME_04%) * (DISTANCE * %AUTO_PER_MILE_COST% + LW.TOLL_PRICE_HOV3 / %HWY_HOV3OCC%) + LW.HOV_TIME_PNLTY
     LW.PATHCOST_HOV3_INC_05 = TIME + (0.6 / %VOT_INCOME_05%) * (DISTANCE * %AUTO_PER_MILE_COST% + LW.TOLL_PRICE_HOV3 / %HWY_HOV3OCC%) + LW.HOV_TIME_PNLTY

     LW.PATHCOST_TRK = TIME + (0.6 / %VOT_TRK%) * DISTANCE * %TRUCK_PER_MILE_COST%

     ; Debug print -------------------------------------------------------------
     IF (LW.SEGMENT_ID > 0 || LW.MNPASS_PAY > 0)
       PRINT CSV=T LIST = iteration(2.0),
                          A(6.0),
                          B(6.0),
                          LW.MNPASS_CODE(4.0),
						  LW.MNPASS_PAY(4.0),
                          LW.HOV(4.0),
                          V(8.2),
                          V/C(8.42),
                          TIME(5.2),
                          DISTANCE(5.2),
                          V*TIME(15.2),
                          V*DISTANCE(15.2),
                          LW.TOLL_PRICE_SOV(8.2) PRINTO = 1
     ENDIF


   ENDPHASE


ENDRUN

RUN PGM = NETWORK

   FILEI LINKI = "%SCENARIO_DIR%\HWY_LDNET_%ITER%_%PER%.NET"
   FILEO LINKO = "%SCENARIO_DIR%\HWY_LDNET_%ITER%_%PER%.SHP", FORMAT = SHP

ENDRUN