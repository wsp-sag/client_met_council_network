RUN PGM = NETWORK ; Calculate RCI values for drive network
NETI = "%SCENARIO_DIR%/highway.net"
NETO = "%SCENARIO_DIR%/highway_2015.net"

;if (area_type = 10) area_type = 1

rci = 0 ; initilize variable
; DISTANCE = SHAPE_length*0.000621371 ; calculates distance in miles from shapelength (meters)

;Assume that the AM lanes set the value for the whole day. Model is not currently set up to have multiple highway networks.
LANES=LANES_AM

;below sets up RCI as a function of assign_group and roadway_class.
if (assign_group = 0) delete
if (assign_group = 1) RCI = 1
if (assign_group = 2) RCI = 2
if (assign_group = 3) RCI = 14
if (assign_group = 4) RCI = 13
if (assign_group = 8) RCI = 1 ; all HOV facilities are access controlled
if (assign_group = 9) rci = 99 ; all centroid have same RCI and roadway_class
if (assign_group = 10) rci = 1 ; hov dummy
if (assign_group = 11) rci = 9
if (assign_group = 13) rci = 14 ; ramps
if (assign_group = 14) rci = 13 ; ramps
if (assign_group = 15) rci = 3 ; expressways
if (assign_group = 100) rci = 100 ; rail
if (assign_group = 101) rci = 101 ; bikes (needs work)

if (assign_group = 5)
  if (roadway_class = 20) RCI = 4
  if (roadway_class = 30) RCI = 6
  if (roadway_class = 40) RCI = 8
  if (roadway_class = 50)  RCI = 11
 elseif (assign_group = 6)
  if (roadway_class = 20) RCI = 5
  if (roadway_class = 30) RCI = 7
  if (roadway_class = 40) RCI = 9
  if (roadway_class = 50) RCI = 11
 elseif (assign_group = 7)
  if (roadway_class = 0,10,20,30,40,60) RCI = 10
  if (roadway_class = 50) RCI = 12
elseif (assign_group = 98) ; bus only
  if (roadway_class = 30) RCI = 6
  if (roadway_class = 40) RCI = 10
  if (roadway_class = 50) RCI = 12
  if (roadway_class = 60) RCI = 13
endif

Linkclass = RCI
LANES = LANES
assign_group = assign_group

;below calculates speed and capacity as a function of RCI and AREA_TYPE
assign_group = assign_group
 LANES = lanes

 if (RCI = 1)
	if (AREA_TYPE = 1,10)	speed = 70,capacity = 1950*LANES
	if (AREA_TYPE = 2) 	speed = 69,capacity = 1950*LANES
	if (AREA_TYPE = 3) 	speed = 67,capacity = 1950*LANES
	if (AREA_TYPE = 4) 	speed = 64,capacity = 1950*LANES
	if (AREA_TYPE = 5) 	speed = 61,capacity = 1950*LANES
	if (AREA_TYPE = 6) 	speed = 66,capacity = 1950*LANES
 elseif (RCI = 2)
 	if (AREA_TYPE = 1,10)	speed = 72,capacity = 1750*LANES
 	if (AREA_TYPE = 2) 	speed = 71,capacity = 1750*LANES
 	if (AREA_TYPE = 3) 	speed = 69,capacity = 1750*LANES
 	if (AREA_TYPE = 4) 	speed = 65,capacity = 1750*LANES
 	if (AREA_TYPE = 5) 	speed = 50,capacity = 1750*LANES
 	if (AREA_TYPE = 6) 	speed = 67,capacity = 1750*LANES
 elseif (RCI = 3)
	if (AREA_TYPE = 1,10)	speed = 64,capacity = 1100*LANES
	if (AREA_TYPE = 2) 	speed = 54,capacity = 1100*LANES
	if (AREA_TYPE = 3) 	speed = 51,capacity = 1100*LANES
	if (AREA_TYPE = 4) 	speed = 44,capacity = 1100*LANES
	if (AREA_TYPE = 5) 	speed = 44,capacity = 1100*LANES
	if (AREA_TYPE = 6) 	speed = 48,capacity = 1100*LANES
 elseif (RCI = 4)
	if (AREA_TYPE = 1,10)	speed = 59,capacity = 1000*LANES
	if (AREA_TYPE = 2) 	speed = 52,capacity = 950*LANES
	if (AREA_TYPE = 3) 	speed = 49,capacity = 850*LANES
	if (AREA_TYPE = 4) 	speed = 43,capacity = 750*LANES
	if (AREA_TYPE = 5) 	speed = 42,capacity = 700*LANES
	if (AREA_TYPE = 6) 	speed = 47,capacity = 700*LANES
 elseif (RCI = 5)
	if (AREA_TYPE = 1,10)	speed = 53,capacity = 900*LANES
	if (AREA_TYPE = 2) 	speed = 51,capacity = 850*LANES
	if (AREA_TYPE = 3) 	speed = 48,capacity = 750*LANES
	if (AREA_TYPE = 4) 	speed = 42,capacity = 650*LANES
	if (AREA_TYPE = 5) 	speed = 41,capacity = 600*LANES
	if (AREA_TYPE = 6) 	speed = 39,capacity = 600*LANES
 elseif (RCI = 6)
	if (AREA_TYPE = 1,10)	speed = 54,capacity = 1000*LANES
	if (AREA_TYPE = 2) 	speed = 46,capacity = 950*LANES
	if (AREA_TYPE = 3) 	speed = 42,capacity = 850*LANES
	if (AREA_TYPE = 4) 	speed = 36,capacity = 750*LANES
	if (AREA_TYPE = 5) 	speed = 31,capacity = 700*LANES
	if (AREA_TYPE = 6) 	speed = 38,capacity = 700*LANES
 elseif (RCI = 7)
	if (AREA_TYPE = 1,10)	speed = 54,capacity = 900*LANES
	if (AREA_TYPE = 2) 	speed = 44,capacity = 850*LANES
	if (AREA_TYPE = 3) 	speed = 38,capacity = 750*LANES
	if (AREA_TYPE = 4) 	speed = 33,capacity = 650*LANES
	if (AREA_TYPE = 5) 	speed = 31,capacity = 600*LANES
	if (AREA_TYPE = 6) 	speed = 37,capacity = 600*LANES
 elseif (RCI = 8)
	if (AREA_TYPE = 1,10)	speed = 47,capacity = 1000*LANES
	if (AREA_TYPE = 2) 	speed = 37,capacity = 950*LANES
	if (AREA_TYPE = 3) 	speed = 37,capacity = 850*LANES
	if (AREA_TYPE = 4) 	speed = 30,capacity = 750*LANES
	if (AREA_TYPE = 5) 	speed = 35,capacity = 700*LANES
	if (AREA_TYPE = 6) 	speed = 34,capacity = 700*LANES
 elseif (RCI = 9)
	if (AREA_TYPE = 1,10)	speed = 50,capacity = 900*LANES
	if (AREA_TYPE = 2) 	speed = 37,capacity = 850*LANES
	if (AREA_TYPE = 3) 	speed = 33,capacity = 750*LANES
	if (AREA_TYPE = 4) 	speed = 31,capacity = 650*LANES
	if (AREA_TYPE = 5) 	speed = 29,capacity = 600*LANES
	if (AREA_TYPE = 6) 	speed = 33,capacity = 600*LANES
 elseif (RCI = 10)
	if (AREA_TYPE = 1,10)	speed = 39,capacity = 600*LANES
	if (AREA_TYPE = 2) 	speed = 35,capacity = 550*LANES
	if (AREA_TYPE = 3) 	speed = 32,capacity = 500*LANES
	if (AREA_TYPE = 4) 	speed = 24,capacity = 450*LANES
	if (AREA_TYPE = 5) 	speed = 24,capacity = 400*LANES
	if (AREA_TYPE = 6) 	speed = 34,capacity = 400*LANES
 elseif (RCI = 11)
	if (AREA_TYPE = 1,10)	speed = 36,capacity = 900*LANES
	if (AREA_TYPE = 2) 	speed = 32,capacity = 850*LANES
	if (AREA_TYPE = 3) 	speed = 31,capacity = 750*LANES
	if (AREA_TYPE = 4) 	speed = 23,capacity = 650*LANES
	if (AREA_TYPE = 5) 	speed = 23,capacity = 600*LANES
	if (AREA_TYPE = 6) 	speed = 35,capacity = 600*LANES
 elseif (RCI = 12)
	if (AREA_TYPE = 1,10)	speed = 29,capacity = 600*LANES
	if (AREA_TYPE = 2) 	speed = 30,capacity = 550*LANES
	if (AREA_TYPE = 3) 	speed = 27,capacity = 500*LANES
	if (AREA_TYPE = 4) 	speed = 23,capacity = 450*LANES
	if (AREA_TYPE = 5) 	speed = 26,capacity = 400*LANES
	if (AREA_TYPE = 6) 	speed = 27,capacity = 400*LANES
 elseif (RCI = 13)
	if (AREA_TYPE = 1,10)	speed = 45,capacity = 1500*LANES
	if (AREA_TYPE = 2) 	speed = 42,capacity = 1400*LANES
	if (AREA_TYPE = 3) 	speed = 40,capacity = 1350*LANES
	if (AREA_TYPE = 4) 	speed = 39,capacity = 1250*LANES
	if (AREA_TYPE = 5) 	speed = 37,capacity = 1200*LANES
	if (AREA_TYPE = 6) 	speed = 37,capacity = 1200*LANES
 elseif (RCI = 14)
	if (AREA_TYPE = 1,10)	speed = 36,capacity = 750*LANES
	if (AREA_TYPE = 2) 	speed = 40,capacity = 725*LANES
	if (AREA_TYPE = 3) 	speed = 39,capacity = 675*LANES
	if (AREA_TYPE = 4) 	speed = 40,capacity = 625*LANES
	if (AREA_TYPE = 5) 	speed = 36,capacity = 600*LANES
	if (AREA_TYPE = 6) 	speed = 39,capacity = 600*LANES
 elseif (RCI = 15)
	if (AREA_TYPE = 1,10)	speed = 26,capacity = 600*LANES
	if (AREA_TYPE = 2) 	speed = 26,capacity = 550*LANES
	if (AREA_TYPE = 3) 	speed = 25,capacity = 500*LANES
	if (AREA_TYPE = 4) 	speed = 20,capacity = 450*LANES
	if (AREA_TYPE = 5) 	speed = 19,capacity = 400*LANES
	if (AREA_TYPE = 6) 	speed = 23,capacity = 400*LANES
 elseif (RCI = 99)
	if (AREA_TYPE = 1,10)	speed = 26,capacity = 99999*LANES
	if (AREA_TYPE = 2) 	speed = 26,capacity = 99999*LANES
	if (AREA_TYPE = 3) 	speed = 25,capacity = 99999*LANES
	if (AREA_TYPE = 4) 	speed = 20,capacity = 99999*LANES
	if (AREA_TYPE = 5) 	speed = 19,capacity = 99999*LANES
	if (AREA_TYPE = 6) 	speed = 23,capacity = 99999*LANES
 endif

 if (speed = 0) speed = 60
 time = 60*(distance/speed)
/*
 ; HOV corridors denoted by SEGMENT_ID
 ;I-394
 if (SEGMENT_ID = 105)			AMCAP = capacity,		PMCAP = capacity+1950,	OFFCAP = capacity+1950
 if (SEGMENT_ID = 104)			AMCAP = capacity+1950,	PMCAP = capacity,		OFFCAP = capacity+1950
 if (SEGMENT_ID = 5||SEGMENT_ID = 6)	AMCAP = capacity,		PMCAP = 0,		OFFCAP = 0
 if (SEGMENT_ID = 3||SEGMENT_ID = 4)	AMCAP = 0,		PMCAP = capacity,		OFFCAP = 0
 if (SEGMENT_ID = 103||SEGMENT_ID = 106)	AMCAP = capacity,		PMCAP = capacity,		OFFCAP = capacity


 ;I-35W
 if (SEGMENT_ID = 1)	AMCAP = capacity,		PMCAP = 0,		OFFCAP = 0
 if (SEGMENT_ID = 2)	AMCAP = 0,		PMCAP = capacity,		OFFCAP = 0
 if (SEGMENT_ID = 7) 	AMCAP = capacity,		PMCAP = capacity,		OFFCAP = 0
 if (SEGMENT_ID = 8) 	AMCAP = capacity,		PMCAP = capacity,		OFFCAP = 0
 if (SEGMENT_ID = 9) 	AMCAP = capacity,		PMCAP = capacity,		OFFCAP = 0
 if (SEGMENT_ID = 10)	AMCAP = capacity,		PMCAP = capacity,		OFFCAP = 0

 if (SEGMENT_ID = 101) 	AMCAP = capacity-1950,	PMCAP = capacity,		OFFCAP = capacity
 if (SEGMENT_ID = 102) 	AMCAP = capacity,		PMCAP = capacity-1950,	OFFCAP = capacity
 if (SEGMENT_ID = 107) 	AMCAP = capacity-1950,	PMCAP = capacity-1950,	OFFCAP = capacity
 if (SEGMENT_ID = 108) 	AMCAP = capacity-1950,	PMCAP = capacity-1950,	OFFCAP = capacity
 if (SEGMENT_ID = 109) 	AMCAP = capacity,		PMCAP = capacity,		OFFCAP = capacity; PDSL
 if (SEGMENT_ID = 110) 	AMCAP = capacity,		PMCAP = capacity,		OFFCAP = capacity; PDSL


;I-35E
 if (SEGMENT_ID = 11) 	AMCAP = capacity,		PMCAP = capacity,		OFFCAP = 0
 if (SEGMENT_ID = 12) 	AMCAP = capacity,		PMCAP = capacity,		OFFCAP = 0
 if (SEGMENT_ID = 111) 	AMCAP = capacity,		PMCAP = capacity,		OFFCAP = capacity
 if (SEGMENT_ID = 112) 	AMCAP = capacity,		PMCAP = capacity,		OFFCAP = capacity



 ;Everything Else
 if (SEGMENT_ID = 0) 	AMCAP = capacity,		PMCAP = capacity,		OFFCAP = capacity


 newvolAM = 0
 congAM = 0
  newvolMD  = 0
 congMD    = 0
 SEGMENT_IDy = SEGMENT_ID

*/
 endrun
