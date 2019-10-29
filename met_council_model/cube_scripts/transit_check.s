; Do not change filenames or add or remove FILEI/FILEO statements using an editor. Use Cube/Application Manager.
RUN PGM=PUBLIC TRANSPORT MSG='Export .LIN from a PT 2015 ' ; correct this directory 
FILEI FACTORI[1] = "C:\Users\helseljw\OneDrive - WSP O365\met_council\model_files\WSPHandoff_Jan2019\ABM 2017\Input\transit\PK_WK_2010.FAC" ; find on your system, use same file every time
FILEI SYSTEMI = "C:\Users\helseljw\OneDrive - WSP O365\met_council\model_files\WSPHandoff_Jan2019\ABM 2017\Input\transit\PT_SYSTEM_2010.PTS" ; find on your system, use same file every time 
FILEI NETI = "C:\Users\helseljw\OneDrive - WSP O365\met_council\replacement_networks\osm_roadway_network_builder_022019\testNetwork_2015.net" ; Highway file, year specific 
FILEO LINEO = "C:\Users\helseljw\OneDrive - WSP O365\met_council\replacement_networks\client_network2015_gdb\2015_ignorethisfile.LIN" ; correct directory to temp folder 
FILEI LINEI[1] = "C:\Users\helseljw\OneDrive - WSP O365\met_council\replacement_networks\test_transit.LIN" ; correct directory to PT_year in .lin or .gdb 

PARAMETERS TRANTIME = LW.TRANTIME, SKIPBADLINES = Y

PROCESS PHASE = LINKREAD; 
    LW.TRANTIME = li.T_MANTIME

ENDPROCESS


PHASE=DATAPREP

ENDPHASE

ENDRUN