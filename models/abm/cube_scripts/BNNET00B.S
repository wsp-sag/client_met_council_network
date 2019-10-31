; Do not change filenames or add or remove FILEI/FILEO statements using an editor. Use Cube/Application Manager.
RUN PGM=NETWORK MSG='Export Raw Network From GeoDatabase'
FILEO NETO = "%SCENARIO_DIR%/highway_2015.TMP"
FILEI LINKI[1] = "%iHwyNet%"

ENDRUN