run pgm=NETWORK ; Calculate RCI values for 2040 network 
 neti=HighwayNetwork.net
 neto=HighwayNetwork15.net  
 
rci=0 ; initilize variable
DISTANCE=SHAPE_length*0.000621371 ; calculates distance in miles from shapelength (meters)

;below sets up RCI as a function of asgngrp and RC_NUM. 
if (asgngrp15=0) delete
if (asgngrp15=1) RCI=1
if (asgngrp15=2) RCI=2
if (asgngrp15=3) RCI=14
if (asgngrp15=4) RCI=13
if (asgngrp15=8) RCI=1 ; all HOV facilities are access controlled 
if (asgngrp15=9) rci=99 ; all centroid have same RCI and RC_NUM
if (asgngrp15=10) rci=1 ; hov dummy
if (asgngrp15=11) rci=9
if (asgngrp15=13) rci=14 ; ramps
if (asgngrp15=14) rci=13 ; ramps
if (asgngrp15=15) rci=3 ; expressways
if (asgngrp15=100) rci=100 ; rail
if (asgngrp15=101) rci=101 ; bikes (needs work)

if (asgngrp15=5)
  if (rc_num=20) RCI=4
  if (rc_num=30) RCI=6
  if (rc_num=40) RCI=8
  if (rc_num=50)  RCI=11 
 elseif (asgngrp15=6)
  if (rc_num=20) RCI=5
  if (rc_num=30) RCI=7
  if (rc_num=40) RCI=9
  if (rc_num=50) RCI=11
 elseif (asgngrp15=7) 
  if (rc_num=0,10,20,30,40,60) RCI=10
  if (rc_num=50) RCI=12
elseif (asgngrp15=98) ; bus only 
  if (rc_num=30) RCI=6
  if (rc_num=40) RCI=10
  if (rc_num=50) RCI=12
  if (rc_num=60) RCI=13 
endif 

Linkclass=RCI
LANES=LANES15
asgngrp=asgngrp15

;below calculates speed and capacity as a function of RCI and AREA
asgngrp=asgngrp15
 LANES=lanes15

 if (RCI=1)
	if (AREA=1,10)	speed=70,capacity=1950*LANES
	if (AREA=2) 	speed=69,capacity=1950*LANES
	if (AREA=3) 	speed=67,capacity=1950*LANES
	if (AREA=4) 	speed=64,capacity=1950*LANES
	if (AREA=5) 	speed=61,capacity=1950*LANES
	if (AREA=6) 	speed=66,capacity=1950*LANES
 elseif (RCI=2)
 	if (AREA=1,10)	speed=72,capacity=1750*LANES
 	if (AREA=2) 	speed=71,capacity=1750*LANES
 	if (AREA=3) 	speed=69,capacity=1750*LANES
 	if (AREA=4) 	speed=65,capacity=1750*LANES
 	if (AREA=5) 	speed=50,capacity=1750*LANES
 	if (AREA=6) 	speed=67,capacity=1750*LANES
 elseif (RCI=3)
	if (AREA=1,10)	speed=64,capacity=1100*LANES
	if (AREA=2) 	speed=54,capacity=1100*LANES
	if (AREA=3) 	speed=51,capacity=1100*LANES
	if (AREA=4) 	speed=44,capacity=1100*LANES
	if (AREA=5) 	speed=44,capacity=1100*LANES
	if (AREA=6) 	speed=48,capacity=1100*LANES
 elseif (RCI=4)
	if (AREA=1,10)	speed=59,capacity=1000*LANES
	if (AREA=2) 	speed=52,capacity=950*LANES
	if (AREA=3) 	speed=49,capacity=850*LANES
	if (AREA=4) 	speed=43,capacity=750*LANES
	if (AREA=5) 	speed=42,capacity=700*LANES
	if (AREA=6) 	speed=47,capacity=700*LANES
 elseif (RCI=5)
	if (AREA=1,10)	speed=53,capacity=900*LANES
	if (AREA=2) 	speed=51,capacity=850*LANES
	if (AREA=3) 	speed=48,capacity=750*LANES
	if (AREA=4) 	speed=42,capacity=650*LANES
	if (AREA=5) 	speed=41,capacity=600*LANES
	if (AREA=6) 	speed=39,capacity=600*LANES
 elseif (RCI=6)
	if (AREA=1,10)	speed=54,capacity=1000*LANES
	if (AREA=2) 	speed=46,capacity=950*LANES
	if (AREA=3) 	speed=42,capacity=850*LANES
	if (AREA=4) 	speed=36,capacity=750*LANES
	if (AREA=5) 	speed=31,capacity=700*LANES
	if (AREA=6) 	speed=38,capacity=700*LANES
 elseif (RCI=7)
	if (AREA=1,10)	speed=54,capacity=900*LANES
	if (AREA=2) 	speed=44,capacity=850*LANES
	if (AREA=3) 	speed=38,capacity=750*LANES
	if (AREA=4) 	speed=33,capacity=650*LANES
	if (AREA=5) 	speed=31,capacity=600*LANES
	if (AREA=6) 	speed=37,capacity=600*LANES
 elseif (RCI=8)
	if (AREA=1,10)	speed=47,capacity=1000*LANES
	if (AREA=2) 	speed=37,capacity=950*LANES
	if (AREA=3) 	speed=37,capacity=850*LANES
	if (AREA=4) 	speed=30,capacity=750*LANES
	if (AREA=5) 	speed=35,capacity=700*LANES
	if (AREA=6) 	speed=34,capacity=700*LANES
 elseif (RCI=9)
	if (AREA=1,10)	speed=50,capacity=900*LANES
	if (AREA=2) 	speed=37,capacity=850*LANES
	if (AREA=3) 	speed=33,capacity=750*LANES
	if (AREA=4) 	speed=31,capacity=650*LANES
	if (AREA=5) 	speed=29,capacity=600*LANES
	if (AREA=6) 	speed=33,capacity=600*LANES
 elseif (RCI=10)
	if (AREA=1,10)	speed=39,capacity=600*LANES
	if (AREA=2) 	speed=35,capacity=550*LANES
	if (AREA=3) 	speed=32,capacity=500*LANES
	if (AREA=4) 	speed=24,capacity=450*LANES
	if (AREA=5) 	speed=24,capacity=400*LANES
	if (AREA=6) 	speed=34,capacity=400*LANES	
 elseif (RCI=11)
	if (AREA=1,10)	speed=36,capacity=900*LANES
	if (AREA=2) 	speed=32,capacity=850*LANES
	if (AREA=3) 	speed=31,capacity=750*LANES
	if (AREA=4) 	speed=23,capacity=650*LANES
	if (AREA=5) 	speed=23,capacity=600*LANES
	if (AREA=6) 	speed=35,capacity=600*LANES
 elseif (RCI=12)
	if (AREA=1,10)	speed=29,capacity=600*LANES
	if (AREA=2) 	speed=30,capacity=550*LANES
	if (AREA=3) 	speed=27,capacity=500*LANES
	if (AREA=4) 	speed=23,capacity=450*LANES
	if (AREA=5) 	speed=26,capacity=400*LANES
	if (AREA=6) 	speed=27,capacity=400*LANES
 elseif (RCI=13)
	if (AREA=1,10)	speed=45,capacity=1500*LANES
	if (AREA=2) 	speed=42,capacity=1400*LANES
	if (AREA=3) 	speed=40,capacity=1350*LANES
	if (AREA=4) 	speed=39,capacity=1250*LANES
	if (AREA=5) 	speed=37,capacity=1200*LANES
	if (AREA=6) 	speed=37,capacity=1200*LANES	
 elseif (RCI=14)
	if (AREA=1,10)	speed=36,capacity=750*LANES
	if (AREA=2) 	speed=40,capacity=725*LANES
	if (AREA=3) 	speed=39,capacity=675*LANES
	if (AREA=4) 	speed=40,capacity=625*LANES
	if (AREA=5) 	speed=36,capacity=600*LANES
	if (AREA=6) 	speed=39,capacity=600*LANES	
 elseif (RCI=15)
	if (AREA=1,10)	speed=26,capacity=600*LANES
	if (AREA=2) 	speed=26,capacity=550*LANES
	if (AREA=3) 	speed=25,capacity=500*LANES
	if (AREA=4) 	speed=20,capacity=450*LANES
	if (AREA=5) 	speed=19,capacity=400*LANES
	if (AREA=6) 	speed=23,capacity=400*LANES		
 elseif (RCI=99)
	if (AREA=1,10)	speed=26,capacity=99999*LANES
	if (AREA=2) 	speed=26,capacity=99999*LANES
	if (AREA=3) 	speed=25,capacity=99999*LANES
	if (AREA=4) 	speed=20,capacity=99999*LANES
	if (AREA=5) 	speed=19,capacity=99999*LANES
	if (AREA=6) 	speed=23,capacity=99999*LANES		
 endif
 
 if (speed=0) speed=60
 time=60*(distance/speed)
 
 ; HOV
 ;I-394
 if (HOV=105)			AMCAP=capacity,		PMCAP=capacity+1950,	OFFCAP=capacity+1950
 if (HOV=104)			AMCAP=capacity+1950,	PMCAP=capacity,		OFFCAP=capacity+1950
 if (HOV=5||HOV=6)	AMCAP=capacity,		PMCAP=0,		OFFCAP=0
 if (HOV=3||HOV=4)	AMCAP=0,		PMCAP=capacity,		OFFCAP=0
 if (HOV=103||HOV=106)	AMCAP=capacity,		PMCAP=capacity,		OFFCAP=capacity
 
 
 ;I-35W
 if (HOV=1)	AMCAP=capacity,		PMCAP=0,		OFFCAP=0
 if (HOV=2)	AMCAP=0,		PMCAP=capacity,		OFFCAP=0
 if (HOV=7) 	AMCAP=capacity,		PMCAP=capacity,		OFFCAP=0
 if (HOV=8) 	AMCAP=capacity,		PMCAP=capacity,		OFFCAP=0
 if (HOV=9) 	AMCAP=capacity,		PMCAP=capacity,		OFFCAP=0
 if (HOV=10)	AMCAP=capacity,		PMCAP=capacity,		OFFCAP=0

 if (HOV=101) 	AMCAP=capacity-1950,	PMCAP=capacity,		OFFCAP=capacity
 if (HOV=102) 	AMCAP=capacity,		PMCAP=capacity-1950,	OFFCAP=capacity
 if (HOV=107) 	AMCAP=capacity-1950,	PMCAP=capacity-1950,	OFFCAP=capacity
 if (HOV=108) 	AMCAP=capacity-1950,	PMCAP=capacity-1950,	OFFCAP=capacity
 if (HOV=109) 	AMCAP=capacity,		PMCAP=capacity,		OFFCAP=capacity; PDSL
 if (HOV=110) 	AMCAP=capacity,		PMCAP=capacity,		OFFCAP=capacity; PDSL


;I-35E
 if (HOV=11) 	AMCAP=capacity,		PMCAP=capacity,		OFFCAP=0
 if (HOV=12) 	AMCAP=capacity,		PMCAP=capacity,		OFFCAP=0
 if (HOV=111) 	AMCAP=capacity,		PMCAP=capacity,		OFFCAP=capacity
 if (HOV=112) 	AMCAP=capacity,		PMCAP=capacity,		OFFCAP=capacity


 ;Everything Else
 if (HOV=0) 	AMCAP=capacity,		PMCAP=capacity,		OFFCAP=capacity
 
 
 newvolAM=0
 congAM=0
  newvolMD =0 
 congMD   =0
 HOVy=HOV
 
 
 endrun
 



