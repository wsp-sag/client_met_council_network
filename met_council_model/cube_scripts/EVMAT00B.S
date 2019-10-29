; Do not change filenames or add or remove FILEI/FILEO statements using an editor. Use Cube/Application Manager.
RUN PGM = MATRIX MSG = 'Transit Accessibility'
FILEI ZDATI[1] = "%SCENARIO_DIR%\zones_%PREV_ITER%.dbf"

FILEO PRINTO[1] = "%SCENARIO_DIR%\transit_accessibility.csv"
FILEI MATI[1] = "%SCENARIO_DIR%\XIT_WK_SKIM_%PREV_ITER%_PK.SKM"

; This script creates transit accessibility measures for each TAZ
; Inputs- Transit skim file (PK_XIT_WK.SKM) and Zonal Data File (zones.dbf)
; Output - Transit accessibility measures (transit_accessibility.csv)
; Moby Khan 11/2/16

Zones = %int_zones%

; Six different constants are used to calculate six different transit accessibility measures
MW[100] = MI.1.TRNTIME
C_1 = 1
C_2 = 2
C_5 = 5
C_10 = 10
C_15 = 15
C_20 = 20

; The following loop calculates T_bar
IF (i = 1) ; this if statement makes sure T_bar is calculated only once since it is the same for all i's
  LOOP A = 1, Zones
    LOOP B = 1, Zones
      IF (MATVAL(1, 1, a, b) > 0)
        T_sum = T_sum + MATVAL(1, 1, a, b)
        NumPairs = NumPairs + 1
      ENDIF
    ENDLOOP
  ENDLOOP
  T_bar = T_sum / NumPairs
ENDIF


; Use a constant value of T_bar if desired, otherwise T_bar is calculated in step above
; T_bar = 38.65447734

; Calculate first step of accessibility measure for all ij pair based on the formula emp_j * exp(-C*T_ij/T_bar)
JLOOP
  if(MW[100]>0) ; check that transit skims exist for ij pair, otherwise accessibility is 0
    MW[1] = ZI.1.tot_emp[j] * exp(-1 * C_1 * MW[100] / T_bar) ;accvalT1
    MW[2] = ZI.1.tot_emp[j] * exp(-1 * C_2 * MW[100] / T_bar) ;accvalT2
    MW[3] = ZI.1.tot_emp[j] * exp(-1 * C_5 * MW[100] / T_bar) ;accvalT5
    MW[4] = ZI.1.tot_emp[j] * exp(-1 * C_10 * MW[100] / T_bar) ;accvalT10
    MW[5] = ZI.1.tot_emp[j] * exp(-1 * C_15 * MW[100] / T_bar) ;accvalT15
    MW[6] = ZI.1.tot_emp[j] * exp(-1 * C_20 * MW[100] / T_bar) ;accvalT20
    MW[7] = ZI.1.ret_emp[j] * exp(-1 * C_1 * MW[100] / T_bar) ;accvalR1
    MW[8] = ZI.1.ret_emp[j] * exp(-1 * C_2 * MW[100] / T_bar) ;accvalR2
    MW[9] = ZI.1.ret_emp[j] * exp(-1 * C_5 * MW[100] / T_bar) ;accvalR5
    MW[10] = ZI.1.ret_emp[j] * exp(-1 * C_10 * MW[100] / T_bar) ;accvalR10
    MW[11] = ZI.1.ret_emp[j] * exp(-1 * C_15 * MW[100] / T_bar) ;accvalR15
    MW[12] = ZI.1.ret_emp[j] * exp(-1 * C_20 * MW[100] / T_bar) ;accvalR20
    MW[13] = ZI.1.nret_emp[j] * exp(-1 * C_1 * MW[100] / T_bar) ;accvalN1
    MW[14] = ZI.1.nret_emp[j] * exp(-1 * C_2 * MW[100] / T_bar) ;accvalN2
    MW[15] = ZI.1.nret_emp[j] * exp(-1 * C_5 * MW[100] / T_bar) ;accvalN5
    MW[16] = ZI.1.nret_emp[j] * exp(-1 * C_10 * MW[100] / T_bar) ;accvalN10
    MW[17] = ZI.1.nret_emp[j] * exp(-1 * C_15 * MW[100] / T_bar) ;accvalN15
    MW[18] = ZI.1.nret_emp[j] * exp(-1 * C_20 * MW[100] / T_bar) ;accvalN20
  ENDIF
ENDJLOOP

; Declare arrays (columns) for each of the accessibility measures
ARRAY TETRacc1 = Zones,
      TETRacc2 = Zones,
      TETRacc5 = Zones,
      TETRacc10 = Zones,
      TETRacc15 = Zones,
      TETRacc20 = Zones,
      RETRacc1 = Zones,
      RETRacc2 = Zones,
      RETRacc5 = Zones,
      RETRacc10 = Zones,
      RETRacc15 = Zones,
      RETRacc20 = Zones,
      NETRacc1 = Zones,
      NETRacc2 = Zones,
      NETRacc5 = Zones,
      NETRacc10 = Zones,
      NETRacc15 = Zones,
      NETRacc20 = Zones

; Sum across all rows(js), add 1 and take natural log to obtain accessibility measures

; Total Employment Accessibility
TETRacc1[i] = ln(1 + ROWSUM(1))
TETRacc2[i] = ln(1 + ROWSUM(2))
TETRacc5[i] = ln(1 + ROWSUM(3))
TETRacc10[i] = ln(1 + ROWSUM(4))
TETRacc15[i] = ln(1 + ROWSUM(5))
TETRacc20[i] = ln(1 + ROWSUM(6))

; Retail Employment Accessibility
RETRacc1[i] = ln(1 + ROWSUM(7))
RETRacc2[i] = ln(1 + ROWSUM(8))
RETRacc5[i] = ln(1 + ROWSUM(9))
RETRacc10[i] = ln(1 + ROWSUM(10))
RETRacc15[i] = ln(1 + ROWSUM(11))
RETRacc20[i] = ln(1 + ROWSUM(12))

; Non-retail Employment Accessibility
NETRacc1[i] = ln(1 + ROWSUM(13))
NETRacc2[i] = ln(1 + ROWSUM(14))
NETRacc5[i] = ln(1 + ROWSUM(15))
NETRacc10[i] = ln(1 + ROWSUM(16))
NETRacc15[i] = ln(1 + ROWSUM(17))
NETRacc20[i] = ln(1 + ROWSUM(18))


; Create csv headers
IF (i = 1)
  PRINT CSV = T,
  PRINTO = 1,
  LIST = "Zone", "TETRacc1", "TETRacc2", "TETRacc5", "TETRacc10", "TETRacc15",
  "TETRacc20", "RETRacc1", "RETRacc2", "RETRacc5", "RETRacc10", "RETRacc15",
  "RETRacc20", "NETRacc1", "NETRacc2", "NETRacc5", "NETRacc10", "NETRacc15",
  "NETRacc20"
ENDIF

; Output actual data
PRINT CSV = T,
PRINTO = 1,
LIST = i,
FORM = 10.10,
LIST = TETRacc1[i], TETRacc2[i], TETRacc5[i], TETRacc10[i], TETRacc15[i],
       TETRacc20[i], RETRacc1[i], RETRacc2[i], RETRacc5[i], RETRacc10[i],
       RETRacc15[i], RETRacc20[i], NETRacc1[i], NETRacc2[i], NETRacc5[i],
       NETRacc10[i], NETRacc15[i], NETRacc20[i]

ENDRUN
