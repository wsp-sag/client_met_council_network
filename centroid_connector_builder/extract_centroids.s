; Network.net provided by Rachel Wiken at MetCouncil via "WSPHandoff_Jan2019" data
; transmitted here: ftp://ftp.metc.state.mn.us/MTS/NetworkRebuild/WSP_010319/

run pgm = network 

   filei neti = "network.net"
   fileo linko = "centroid_links.csv", format = CS1, include = A, B 
   fileo nodeo = "node_coordinates.csv", format = CS1, include = N, X, Y

   phase = linkmerge 

     if (a > _ZONES && b > _ZONES) delete

   endphase

endrun 















































