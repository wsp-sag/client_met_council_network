; Do not change filenames or add or remove FILEI/FILEO statements using an editor. Use Cube/Application Manager.
RUN PGM = MATRIX MSG = 'University Enrollment'
FILEI ZDATI[1] = "%SCENARIO_DIR%\zones_%PREV_ITER%.dbf"
FILEI MATI[1] = "%SCENARIO_DIR%\HWY_SKIM_%PREV_ITER%_AM.skm"
FILEO PRINTO[1] = "%SCENARIO_DIR%\universityenrollment.csv"

; This script calculated university enrollment based on 1,2,5 and 10 MIle buffers around TAZs.
; Inputs- Highway skim file (HWY_SKIM_4_AM.skm) and Zonal Data File (zones.dbf)
; Output - University Enrollment for each TAZ by distance buffers (universityenrollment.csv)
; Moby Khan 11/2/16

Zones = %int_zones%

; Buffer is based on drive-alone distance
MW[100]=MI.1.dapdist

; Create arrays for each buffers - 1,2,5 and 10 miles
ARRAY ENROLLED1 = Zones, ENROLLED2 = Zones,
      ENROLLED5 = Zones, ENROLLED10 = Zones

; Loop through all j's and sum enrollment IF destination j is within the buffer
JLOOP
  IF (MW[100] <= 1) ; 1 MIle
    ENROLLED1[i] = ENROLLED1[i] + ZI.1.ENROLLED[j]
  ENDIF
  IF (MW[100] <= 2) ; 2 MIles
    ENROLLED2[i] = ENROLLED2[i] + ZI.1.ENROLLED[j]
  ENDIF
  IF (MW[100] <= 5) ; 5 MIles
    ENROLLED5[i] = ENROLLED5[i] + ZI.1.ENROLLED[j]
  ENDIF
  IF (MW[100] <= 10) ; 10 MIles
    ENROLLED10[i] = ENROLLED10[i] + ZI.1.ENROLLED[j]
  ENDIF
ENDJLOOP


; Create csv headers
IF (i = 1)
PRINT CSV = T,
      PRINTO = 1,
      LIST = "Zone", "ENROLLED1", "ENROLLED2", "ENROLLED5", "ENROLLED10"
ENDIF

; Output actual data
PRINT CSV = T,
      PRINTO = 1,
      LIST = i,
      FORM = 10.0,
      LIST = ENROLLED1[i], ENROLLED2[i], ENROLLED5[i], ENROLLED10[i]


ENDRUN
