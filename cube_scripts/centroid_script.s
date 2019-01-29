; Do not change filenames or add or remove FILEI/FILEO statements using an editor. Use Cube/Application Manager.
RUN PGM = NETWORK 

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
