
*Cluster donkey 1-4 START Exit

token_dir = 'C:\projects\met_council\model_files\outputs2015\outputs'

token_internal_zones = 3100

; dump time-period-specific databases
loop period = 1, 4
  
   ; a two letter token is used for each time period
   if (period = 1)   
      token_period = 'AM'   
  
   elseif (period = 2)   
      token_period = 'MD'    
  
   elseif (period = 3)   
      token_period = 'PM'    
  
   elseif (period = 4)   
      token_period = 'NT'
      
   endif
   
   ; do each time of day as a separate process
   DistributeMultistep processid = 'donkey', processNum = period
     
   ; total travel time by mode
   run pgm = matrix
      
      ; highway skim
      filei mati[1] = @token_dir@\HWY_SKIM_0_@token_period@.skm
    
      
      ; print header for time by mode for each of the three files 
      if (i==1) 
      
         list = "orig,dest,daptime,dapdist", file = @token_dir@\highway_skims_@token_period@.csv
      
      endif
      
      if (i<=@token_internal_zones@)
      
         jloop
         
            if (j<=@token_internal_zones@)
      
               daptime = mi.1.daptime
               dapdist = mi.1.dapdist
               
               ; write the output ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
               list = i(8.0),",",j(8.0),",",daptime(10.2),",",dapdist(10.2), 
                      file = @token_dir@\highway_skims_@token_period@.csv
               
            endif ; internal j zones only
         
         endjloop
      
      endif ; internal i zones only
      
   endrun
   
   EndDistributeMultistep

endloop ; token_period

Wait4Files files = donkey1.script.end, donkey2.script.end, donkey3.script.end, donkey4.script.end,
         printfiles = merge, deldistribfiles = t, CheckReturnCode = t
		 
*Cluster donkey 1-4 Close Exit



