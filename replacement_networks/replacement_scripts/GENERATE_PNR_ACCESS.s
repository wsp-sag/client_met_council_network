Generate,
fromnode = 1-3061,
ACCESSLINK=
19759-19759, 0.0, 0.0,

direction = 1,	 ;access direction only
oneway = T,	 ;follow the roadway direction
excludelink = (li.T_MANTIME > 0),   ;no drive access on transit only links
cost = (lw.roadtime),	 ;skim on congested time
;maxcost = 4 * 1, 5 * 10,
;maxntlegs = 4 * 1, 5 * 5,
maxcost = 7 * 10, 30, 30,
maxntlegs = 9 * 20,
ntlegmode = 2
