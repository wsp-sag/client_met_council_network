
; Write out Walk Distance skims
RUN PGM = MATRIX MSG = 'Export differences in networks to feed Tableau workbook.'
; Fresh skim
FILEI MATI[1] = "%SCENARIO_DIR%/NM_SKIM.skm"
; Comparison skim from prior run
;FILEI MATI[2] = "%COMPARISON_DIR%/new_skims/NM_SKIM_031219.skm"
FILEI MATI[2] = "%COMPARISON_DIR%/original_skims/NM_SKIM.skm"

FILEO MATO[1] = "%COMPARISON_DIR%/walk_comparison.csv", MO = 1-2,
FORMAT = TXT, PATTERN = IJ:MV, DELIMITER = ","
ZONES = %zones%

MW[1] = MI.1.2
MW[2] = MI.2.2
;MW[3] = MI.1.2 - MI.2.2
;MW[4] = MI.1.1
;MW[5] = MI.2.1
;MW[6] = MI.1.1 - MI.2.1


ENDRUN