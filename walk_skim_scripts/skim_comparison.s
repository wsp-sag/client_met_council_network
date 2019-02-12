; Do not change filenames or add or remove FILEI/FILEO statements using an editor. Use Cube/Application Manager.
RUN PGM = MATRIX MSG = "Cross your fingers"
FILEI MATI[1] = "C:\Users\helseljw\OneDrive - WSP O365\met_council\model_files\WSPHandoff_Jan2019\ABM 2017\Base2010\Run2015\HWY_SKIM_0_AM.skm"
<<<<<<< HEAD
<<<<<<< HEAD
FILEI MATI[2] = "C:\Users\helseljw\OneDrive - WSP O365\met_council\model_files\WSPHandoff_Jan2019\ABM 2017\Base2010\Run2015\HWY_SKIM_0_AM.skm" ; XIT_WK_SKIM_3_OP.skm"
=======
FILEI MATI[2] = "C:\Users\helseljw\OneDrive - WSP O365\met_council\model_files\WSPHandoff_Jan2019\ABM 2017\Base2010\Run2015\HWY_SKIM_1_AM.skm" ; XIT_WK_SKIM_3_OP.skm"
>>>>>>> bad417e24e2135ea3f4d387e566eef12b6b9ceae
=======
FILEI MATI[2] = "C:\Users\helseljw\OneDrive - WSP O365\met_council\model_files\WSPHandoff_Jan2019\ABM 2017\Base2010\Run2015\HWY_SKIM_1_AM.skm" ; XIT_WK_SKIM_3_OP.skm"
>>>>>>> bad417e24e2135ea3f4d387e566eef12b6b9ceae
;FILEO MATO[1] = "C:\Users\helseljw\OneDrive - WSP O365\met_council\walk_skim_scripts\skim_comparison.skm", 
;  MO = 1, NAME = skim_diff
FILEO RECO[1] = "C:\Users\helseljw\OneDrive - WSP O365\met_council\walk_skim_scripts\test.dbf",
  FIELDS = origins, num_errors, max_error

  MW[1] = MI.1.daptime - MI.2.daptime

  origins = I
  num_errors = ROWCNT(1)
  max_error = ROWMAX(1)

  WRITE RECO = 1

ENDRUN