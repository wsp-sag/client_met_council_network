
; Write out Walk Distance skims
RUN PGM = MATRIX MSG = 'Export differences in networks to feed Tableau workbook.'
; Fresh skim
FILEI MATI[1] = "%SCENARIO_DIR%/NM_SKIM.skm"
; Comparison skim from prior run
FILEI MATI[2] = "%COMPARISON_DIR%/original_skims/NM_SKIM.skm"

; Freeflow Highway
FILEI MATI[3] = "%SCENARIO_DIR%/HWY_SKIM_0_AM.skm"
FILEI MATI[4] = "%COMPARISON_DIR%/original_skims/HWY_SKIM_0_AM.skm"

; Congested Highway
FILEI MATI[5] = "%SCENARIO_DIR%/HWY_SKIM_1_AM.skm"
FILEI MATI[6] = "%COMPARISON_DIR%/original_skims/HWY_SKIM_4_AM.skm"

FILEO MATO[1] = "%COMPARISON_DIR%/skim_comparison.csv", MO = 1-9,
FORMAT = TXT, PATTERN = IJ:MV, DELIMITER = ","
ZONES = %zones%

; Walk networks
MW[1] = MI.1.2
MW[2] = MI.2.2
; Bike Neetworks
MW[4] = MI.1.1
MW[5] = MI.2.1
; AM Freeflow distance
MW[6] = MI.3.5
MW[7] = MI.4.5
; AM Congested distance
MW[8] = MI.5.5
MW[9] = MI.6.5

ENDRUN