; Do not change filenames or add or remove FILEI/FILEO statements using an editor. Use Cube/Application Manager.
RUN PGM = MATRIX MSG = "Cross your fingers"
FILEI MATI[1] = "C:\Users\helseljw\OneDrive - WSP O365\met_council\model_files\WSPHandoff_Jan2019\ABM 2017\Base2010\Run2015\HWY_SKIM_0_AM.skm"

FILEI MATI[2] = "C:\Users\helseljw\OneDrive - WSP O365\met_council\model_files\WSPHandoff_Jan2019\ABM 2017\Base2010\Run2015\HWY_SKIM_1_AM.skm" ; XIT_WK_SKIM_3_OP.skm"
FILEO MATO[1] = "C:\Users\helseljw\OneDrive - WSP O365\met_council\walk_skim_scripts\skim_comparison.csv", 
  MO = 1, PATTERN = IJ:MV, DELIMITER = ","
;FILEO RECO[1] = "C:\Users\helseljw\OneDrive - WSP O365\met_council\walk_skim_scripts\skim_comparison.dbf",
;  FIELDS = origins, destinations, error

  MW[1] = ABS(MI.1.daptime - MI.2.daptime)


ENDRUN