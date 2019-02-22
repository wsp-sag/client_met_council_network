; Do not change filenames or add or remove FILEI/FILEO statements using an editor. Use Cube/Application Manager.
RUN PGM = MATRIX MSG = "Cross your fingers"
/*
File paths to run on John's computer
FILEI MATI[1] = "C:\Users\helseljw\OneDrive - WSP O365\met_council\model_files\WSPHandoff_Jan2019\ABM 2017\Base2010\Run2015\HWY_SKIM_0_AM.skm"
FILEI MATI[2] = "C:\Users\helseljw\OneDrive - WSP O365\met_council\model_files\WSPHandoff_Jan2019\ABM 2017\Base2010\Run2015\HWY_SKIM_1_AM.skm" ; XIT_WK_SKIM_3_OP.skm"

FILEO MATO[1] = "skim_comparison.csv", 
  MO = 1, PATTERN = IJ:MV, DELIMITER = ","
FILEO MATO[2] = "original_skim.csv",
  MO = 1, PATTERN = IJ:MV, DELIMITER = ","
FILEO MATO[3] = "new_skim.csv", 
  MO = 1, PATTERN = IJ:MV, DELIMITER = ","
;FILEO MATO[4] = "original_skim.skm",  MO = 1, NAME = "daptime"
;FILEO MATO[5] = "new_skim.skm",       MO = 1, NAME = "daptime"

  MW[1] = ABS(MI.1.daptime - MI.2.daptime)
  MW[2] = MI.1.daptime
  MW[3] = MI.2.daptime
  MW[4] = MI.1.daptime
  MW[5] = MI.2.daptime
  
 */
 
; File paths to run off github repo.

FILEI MATI[1] = "original_skim.skm"
FILEI MATI[2] = "new_skim.skm"

FILEO MATO[1] = "skim_comparison.csv",
  MO = 1z , PATTERN = IJ:MV, DELIMITER = ","
FILEO MATO[2] = "original_skim.csv",
  MO = 1, PATTERN = IJ:MV, DELIMITER = ","
FILEO MATO[3] = "new_skim.csv", 
  MO = 1, PATTERN = IJ:MV, DELIMITER = ","
  
  MW[1] = ABS(MI.1.daptime - MI.2.daptime)
  MW[2] = MI.1.daptime
  MW[3] = MI.2.daptime
  
ENDRUN