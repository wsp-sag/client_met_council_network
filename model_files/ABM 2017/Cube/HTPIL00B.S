; Do not change filenames or add or remove FILEI/FILEO statements using an editor. Use Cube/Application Manager.

;NEXTITER = ITER + 1
*Cluster Intrastep 1-{max_threads} START EXIT

LOOP TOD=1,11,1
 IF(TOD=1) PER='AM1' ASSIGNNAME='AM1 Peak Period'    HWY_NET ='HWY_NET_3.net'    NETNAME='AM Peak Period 6:00 AM to 7:00 AM'  CAPFAC = 1
 IF(TOD=2) PER='AM2' ASSIGNNAME='AM2 Peak Period'    HWY_NET ='HWY_NET_3.net'    NETNAME='AM Peak Period 7:00 AM to 8:00 AM'  CAPFAC = 1 
 IF(TOD=3) PER='AM3' ASSIGNNAME='AM3 Peak Period'    HWY_NET ='HWY_NET_3.net'    NETNAME='AM Peak Period 8:00 AM to 9:00 AM'  CAPFAC = 1
 IF(TOD=4) PER='AM4' ASSIGNNAME='AM4 Peak Period'    HWY_NET ='HWY_NET_3.net'    NETNAME='AM Peak Period 9:00 AM to 10:00 AM'  CAPFAC = 1 
  
 IF(TOD=5) PER='MD' ASSIGNNAME='Mid Day Period'    HWY_NET ='HWY_NET_4.net'    NETNAME='Mid Day Period 10:00 AM to 3:00 PM'  CAPFAC = 4.48

 IF(TOD=6) PER='PM1' ASSIGNNAME='PM1 Peak Period'    HWY_NET ='HWY_NET_6.net'    NETNAME='PM Peak Period 3:00 PM to 4:00 PM'  CAPFAC = 1
 IF(TOD=7) PER='PM2' ASSIGNNAME='PM2 Peak Period'    HWY_NET ='HWY_NET_6.net'    NETNAME='PM Peak Period 4:00 PM to 5:00 PM'  CAPFAC = 1
 IF(TOD=8) PER='PM3' ASSIGNNAME='PM3 Peak Period'    HWY_NET ='HWY_NET_6.net'    NETNAME='PM Peak Period 5:00 PM to 6:00 PM'  CAPFAC = 1 
 IF(TOD=9) PER='PM4' ASSIGNNAME='PM4 Peak Period'    HWY_NET ='HWY_NET_6.net'    NETNAME='PM Peak Period 6:00 PM to 7:00 PM'  CAPFAC = 1

 IF(TOD=10) PER='EV' ASSIGNNAME='Evening Period'  HWY_NET ='HWY_NET_1.net'    NETNAME='Evening 7:00 PM to 12:00 AM'  CAPFAC = 3.32 
 IF(TOD=11) PER='ON' ASSIGNNAME='Overnight Period'  HWY_NET ='HWY_NET_1.net'    NETNAME='Overnight 12:00 AM to 6:00 AM'  CAPFAC = 2.59
  


