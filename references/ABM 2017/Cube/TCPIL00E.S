; Do not change filenames or add or remove FILEI/FILEO statements using an editor. Use Cube/Application Manager.


*COPY "{xit_WK_PKskims}" "{SCENARIO_DIR}\XIT_WK_SKIM_0_PK.skm"
*COPY "{xit_WK_OPskim}" "{SCENARIO_DIR}\XIT_WK_SKIM_0_OP.skm"
*COPY "{xit_DR_PKskim}" "{SCENARIO_DIR}\XIT_DR_SKIM_0_PK.skm"
*COPY "{xit_DR_OPskim}" "{SCENARIO_DIR}\XIT_DR_SKIM_0_OP.skm"

IF (ReturnCode = 1) 
  PRINT LIST='Missing Highway Initial Skim file - check scenario key settings in the Scenario Manager'
  ABORT
ENDIF 
