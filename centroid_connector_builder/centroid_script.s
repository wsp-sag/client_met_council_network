; Do not change filenames or add or remove FILEI/FILEO statements using an editor. Use Cube/Application Manager.

; The network is taken from the "Network.net" file in the WSPHandoff_Jan2019 data
; transmission (ftp://ftp.metc.state.mn.us/MTS/NetworkRebuild/WSP_010319/) 
; provided by Rachel Wiken at MetCouncil

/*RUN PGM = NETWORK 

FILEI NETI= "Network.net"

IF (A < 3200 || B < 3200) 
PRINT FILE = "centroid_links.csv" CSV = T LIST = A, B
ENDIF

CENTROID = 0
IF (A < 3200)
CENTROID = 1
ENDIF

EXTERNAL = 0
IF (COUNTY == 10 && A < 3200)
EXTERNAL = 1
ENDIF

PRINT FILE = "input_centroid_node.csv",
  CSV = T,
  LIST = A, CENTROID, EXTERNAL

;PRINTO = 1
ENDRUN
*/

RUN PGM=NETWORK 

NETI = "Network.net"

; Find centroid links
PHASE = LINKMERGE
_MAXZONES = 3200

IF (_taskOne = 0)
  LIST = "    A,", 
         "    B",
  FILE = "centroid_links.csv"
  _taskOne = 1
ENDIF

IF (A < _MAXZONES || B < _MAXZONES)
  LIST = A, ",", B,
  FILE = "centroid_links.csv"
ENDIF

ENDPHASE

; Find centroid nodes
PHASE = NODEMERGE
_MAXZONES = 3200

IF (_taskTwo = 0)
  LIST = "      N,",
         "      X,",
         "      Y,",
  FILE = "input_centroid_node.csv"
  _taskTwo = 1
ENDIF

IF (N  < _MAXZONES)
  LIST = N,",", 
         X,",", 
         Y,         
  FILE = "input_centroid_node.csv"
ENDIF

ENDPHASE

ENDRUN













































