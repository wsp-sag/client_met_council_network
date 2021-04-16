; Do not change filenames or add or remove FILEI/FILEO statements using an editor. Use Cube/Application Manager.
RUN PGM=MATRIX MSG='Expand trip table to full zones'
FILEI MATI[4] = "%SCENARIO_DIR%\XIT_SPC_TRIP_%ITER%_%TPER%.trp"
FILEI MATI[3] = "%SCENARIO_DIR%\XIT_DR_SKIM_%ITER%_%TPER%.SKM"
FILEI MATI[2] = "%SCENARIO_DIR%\XIT_WK_SKIM_%ITER%_%TPER%.SKM"
FILEO MATO[1] = "%SCENARIO_DIR%\XIT_TRIP_%ITER%_%TPER%_CLEAN.trp",
 MO=1-2, NAME=WalkToTransit, DriveToTransit
FILEI MATI[1] = "%SCENARIO_DIR%\XIT_TRIP_%ITER%_%TPER%.trp"

  mw[1] = MI.1.1 + MI.4.1; Walk to Transit
  mw[2] = MI.1.2 + MI.4.2; Drive to Transit
  
  MW[3] = MI.2.1
  MW[4] = MI.3.1
  
  
ENDRUN
