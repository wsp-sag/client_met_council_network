; Network.net provided by Rachel Wiken at MetCouncil via "WSPHandoff_Jan2019" data
; transmitted here: ftp://ftp.metc.state.mn.us/MTS/NetworkRebuild/WSP_010319/


RUN PGM=NETWORK 

   NETI = "Network.net"

   PHASE = LINKMERGE
     
     _MAXZONES = 3200

        IF (_link_header = 0)
           
           LIST = "    A,    B", FILE = "centroid_links.csv"

           _link_header = 1
        
        ENDIF
 
        IF (A < _MAXZONES || B < _MAXZONES)
           
           LIST = A, ",", B, FILE = "centroid_links.csv"
        
        ENDIF

    ENDPHASE

    PHASE = NODEMERGE
       
       _MAXZONES = 3200

       IF (_node_header = 0)

           LIST = "      N,      X,      Y,", FILE = "node_coordinates.csv"

           _node_header = 1

        ENDIF

         LIST = N, ",", X, ",", Y, FILE = "node_coordinates.csv"

    ENDPHASE

ENDRUN













































