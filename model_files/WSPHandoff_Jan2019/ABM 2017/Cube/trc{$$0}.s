; Script for program NETWORK in file "C:\Users\helseljw\OneDrive - WSP O365\met_council\model_files\WSPHandoff_Jan2019\ABM 2017\CUBE\BNNET00B.S"
; Do not change filenames or add or remove FILEI/FILEO statements using an editor. Use Cube/Application Manager.
RUN PGM=NETWORK MSG='Export Raw Network From GeoDatabase'
FILEO NETO = "{SCENARIO_DIR}\ALL_NET.tmp"
FILEI LINKI[1] = "{iHwyNet}"


ENDRUN


