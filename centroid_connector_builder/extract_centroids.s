; Network.net provided by Rachel Wiken at MetCouncil via "WSPHandoff_Jan2019" data
; transmitted here: ftp://ftp.metc.state.mn.us/MTS/NetworkRebuild/WSP_010319/

RUN PGM = NETWORK

   FILEI NETI = "network.net"
   FILEO LINKO = "centroid_links.csv", FORMAT = CS1, INCLUDE = A, B 
   FILEO NODEO = "node_coordinates.csv", FORMAT = CS1, INCLUDE = N, X, Y

   PHASE = LINKMERGE 

     IF(A > _ZONES && B > _ZONES) 
      
      DELETE

     ENDIF

   ENDPHASE

ENDRUN















































