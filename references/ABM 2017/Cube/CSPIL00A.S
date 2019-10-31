; Do not change filenames or add or remove FILEI/FILEO statements using an editor. Use Cube/Application Manager.


*COPY "{hwy_AMskims}" "{SCENARIO_DIR}\HWY_SKIM_0_AM.skm"
*COPY "{hwy_MDskims}" "{SCENARIO_DIR}\HWY_SKIM_0_MD.skm"
*COPY "{hwy_PMskims}" "{SCENARIO_DIR}\HWY_SKIM_0_PM.skm"
*COPY "{hwy_NTskims}" "{SCENARIO_DIR}\HWY_SKIM_0_NT.skm"

  IF (ReturnCode == 1) 
    PRINT LIST='Missing Highway Initial Skim file - check scenario key settings in the Scenario Manager'
    ABORT
  ENDIF 
