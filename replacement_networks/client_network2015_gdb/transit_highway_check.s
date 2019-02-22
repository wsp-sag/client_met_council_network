; Do not change filenames or add or remove FILEI/FILEO statements using an editor. Use Cube/Application Manager.
RUN PGM=PUBLIC TRANSPORT PRNFILE="Errors2015.PRN" MSG='Export .LIN from a PT 2015 ' ; correct this directory 
FILEI FACTORI[1] = "C:\Users\helseljw\OneDrive - WSP O365\met_council\model_files\WSPHandoff_Jan2019\ABM 2017\Input\transit\PK_WK_2010.FAC" ; find on your system, use same file every time
FILEI SYSTEMI = "C:\Users\helseljw\OneDrive - WSP O365\met_council\model_files\WSPHandoff_Jan2019\ABM 2017\Input\transit\PT_SYSTEM_2010.PTS" ; find on your system, use same file every time 
FILEI NETI = "HighwayNetwork15.net" ; Highway file, year specific 
FILEO LINEO = "2015_ignorethisfile.LIN" ; correct directory to temp folder 
FILEI LINEI[1] = "PT_2015.lin" ; correct directory to PT_year in .lin or .gdb 

PARAMETERS TRANTIME = LW.TRANTIME, SKIPBADLINES = Y

PROCESS PHASE = LINKREAD; 
    LW.TRANTIME = li.T_MANTIME

ENDPROCESS


PHASE=DATAPREP

ENDPHASE

ENDRUN