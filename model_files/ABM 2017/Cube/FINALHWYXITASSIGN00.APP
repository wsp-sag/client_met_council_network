&PROJFIL
11
0
0
Assign Highway and Transit
HT
00


Mon Feb 04 13:39:11 2019

C:\Users\helseljw\OneDrive - WSP O365\met_council\model_files\WSPHandoff_Jan2019\ABM 2017\CUBE\FINALASSIGN00.APP
C:\Users\helseljw\OneDrive - WSP O365\met_council\model_files\WSPHandoff_Jan2019\ABM 2017\CUBE\FINALHWYXITASSIGN00.APP
VOYAGER


&End_TextAnnotation
English
#PROGRAM0
1
0
1


PILOT

1
1
0
-1.0
Highway Period Loop
999999
536
-394
725
-464
0
0
0
#INFIL0
Script File

0
0
S
C:\Users\helseljw\OneDrive - WSP O365\met_council\model_files\WSPHandoff_Jan2019\ABM 2017\CUBE\HTPIL00B.S
1
PIL
ISCR1 
999999
219
-396
525
-458
-1
-1
0
#INFIL1
Variable File

0
0
VAR
*.VAR
0
VRI
VARI  
999999
219
-430
525
-492
-1
-1
0
#OUTFIL0
Print Data 1

0
0
PRN
*.PRN
0
PIL
PRINTO1
999999
741
-396
1042
-458
0
#OUTFIL1
Print Data 2

0
0
PRN
*.PRN
0
PIL
PRINTO2
999999
736
-164
1042
-226
0
#OUTFIL2
Print Data 3

0
0
PRN
*.PRN
0
PIL
PRINTO3
999999
736
-231
1042
-293
0
#OUTFIL3
Print Data 4

0
0
PRN
*.PRN
0
PIL
PRINTO4
999999
736
-298
1042
-360
0
#OUTFIL4
Print Data 5

0
0
PRN
*.PRN
0
PIL
PRINTO5
999999
736
-365
1042
-427
0
#OUTFIL5
Print Data 6

0
0
PRN
*.PRN
0
PIL
PRINTO6
999999
736
-432
1042
-494
0
#OUTFIL6
Print Data 7

0
0
PRN
*.PRN
0
PIL
PRINTO7
999999
736
-499
1042
-561
0
#OUTFIL7
Print Data 8

0
0
PRN
*.PRN
0
PIL
PRINTO8
999999
736
-566
1042
-628
0
#OUTFIL8
Print Data 9

0
0
PRN
*.PRN
0
PIL
PRINTO9
999999
736
-633
1042
-695
0
#OUTFIL9
Print Data 10

0
0
PRN
*.PRN
0
PIL
PRINTO10
999999
736
-700
1042
-762
0
#PROGRAM1
2
0
2


MATRIX

1
1
0
-1.0
Convert to Vehicle Trip Tables @ASSIGNNAME@
999999
677
-705
866
-775
0
0
0
#INFIL0
Script File

0
0
S
C:\Users\helseljw\OneDrive - WSP O365\met_council\model_files\WSPHandoff_Jan2019\ABM 2017\CUBE\HTMAT00B.S
1
MAT
ISCR1 
999999
360
-575
666
-637
-1
-1
0
#INFIL1
Matrix File 1

0
0
MAT
{SCENARIO_DIR}\HWY_TRIP_@ITER@_@PER@.trp
0
MAT
MATI1 
999999
360
-642
666
-704
-1
-9
0
#INFIL2
Matrix File 2

0
0
MAT
{SCENARIO_DIR}\TRK_TRIP_@ITER@_@PER@.trp
0
MAT
MATI2 
999999
360
-709
666
-771
-1
-1
0
#INFIL3
Matrix File 3

0
0
MAT
{SCENARIO_DIR}\HWY_EXT_TRIP_@ITER@_@PER@.trp
0
MAT
MATI3 
999999
360
-776
666
-838
-1
-1
0
#INFIL4
Matrix File 4

0
0
MAT
{SCENARIO_DIR}\HWY_SPC_TRIP_@ITER@_@PER@.trp
0
MAT
MATI4 
999999
360
-843
666
-905
-1
-1
0
#INFIL5
Matrix File 5

0
0
MAT
*.MAT
0
MAT
MATI5 
999999
360
-745
666
-807
-1
-1
0
#INFIL6
Matrix File 6

0
0
MAT
*.MAT
0
MAT
MATI6 
999999
360
906
666
844
-1
-1
0
#INFIL7
Matrix File 7

0
0
MAT
*.MAT
0
MAT
MATI7 
999999
360
839
666
777
-1
-1
0
#INFIL8
Matrix File 8

0
0
MAT
*.MAT
0
MAT
MATI8 
999999
360
772
666
710
-1
-1
0
#INFIL9
Matrix File 9

0
0
MAT
*.MAT
0
MAT
MATI9 
999999
360
705
666
643
-1
-1
0
#INFIL10
Matrix File 10

0
0
MAT
*.MAT
0
MAT
MATI10
999999
360
638
666
576
-1
-1
0
#INFIL11
Matrix File 11

0
0
MAT
*.MAT
0
MAT
MATI11
999999
360
571
666
509
-1
-1
0
#INFIL12
Matrix File 12

0
0
MAT
*.MAT
0
MAT
MATI12
999999
360
504
666
442
-1
-1
0
#INFIL13
Matrix File 13

0
0
MAT
*.MAT
0
MAT
MATI13
999999
360
437
666
375
-1
-1
0
#INFIL14
Matrix File 14

0
0
MAT
*.MAT
0
MAT
MATI14
999999
360
370
666
308
-1
-1
0
#INFIL15
Matrix File 15

0
0
MAT
*.MAT
0
MAT
MATI15
999999
360
303
666
241
-1
-1
0
#INFIL16
Matrix File 16

0
0
MAT
*.MAT
0
MAT
MATI16
999999
360
236
666
174
-1
-1
0
#INFIL17
Matrix File 17

0
0
MAT
*.MAT
0
MAT
MATI17
999999
360
169
666
107
-1
-1
0
#INFIL18
Matrix File 18

0
0
MAT
*.MAT
0
MAT
MATI18
999999
360
102
666
40
-1
-1
0
#INFIL19
Matrix File 19

0
0
MAT
*.MAT
0
MAT
MATI19
999999
360
35
666
-27
-1
-1
0
#INFIL20
Matrix File 20

0
0
MAT
*.MAT
0
MAT
MATI20
999999
360
-32
666
-94
-1
-1
0
#INFIL21
Record File

0
0
*
*.*
0
REC
RECI  
999999
360
-812
666
-874
-1
-1
0
#INFIL22
Zonal Data 1

0
0
*
*.*
0
ZON
ZDATI1
999999
360
-879
666
-941
-1
-1
0
#INFIL23
Zonal Data 2

0
0
*
*.*
0
ZON
ZDATI2
999999
360
-233
666
-295
-1
-1
0
#INFIL24
Zonal Data 3

0
0
*
*.*
0
ZON
ZDATI3
999999
360
-300
666
-362
-1
-1
0
#INFIL25
Zonal Data 4

0
0
*
*.*
0
ZON
ZDATI4
999999
360
-367
666
-429
-1
-1
0
#INFIL26
Zonal Data 5

0
0
*
*.*
0
ZON
ZDATI5
999999
360
-434
666
-496
-1
-1
0
#INFIL27
Zonal Data 6

0
0
*
*.*
0
ZON
ZDATI6
999999
360
-501
666
-563
-1
-1
0
#INFIL28
Zonal Data 7

0
0
*
*.*
0
ZON
ZDATI7
999999
360
-568
666
-630
-1
-1
0
#INFIL29
Zonal Data 8

0
0
*
*.*
0
ZON
ZDATI8
999999
360
-635
666
-697
-1
-1
0
#INFIL30
Zonal Data 9

0
0
*
*.*
0
ZON
ZDATI9
999999
360
-702
666
-764
-1
-1
0
#INFIL31
Zonal Data 10

0
0
*
*.*
0
ZON
ZDATI10
999999
360
-769
666
-831
-1
-1
0
#INFIL32
Database 1

0
0
*
*.*
0
DBI
DBI1  
999999
360
-946
666
-1008
-1
-1
0
#INFIL33
Database 2

0
0
*
*.*
0
DBI
DBI2  
999999
360
-903
666
-965
-1
-1
0
#INFIL34
Database 3

0
0
*
*.*
0
DBI
DBI3  
999999
360
-970
666
-1032
-1
-1
0
#INFIL35
Database 4

0
0
*
*.*
0
DBI
DBI4  
999999
360
-1037
666
-1099
-1
-1
0
#INFIL36
Database 5

0
0
*
*.*
0
DBI
DBI5  
999999
360
-1104
666
-1166
-1
-1
0
#INFIL37
Database 6

0
0
*
*.*
0
DBI
DBI6  
999999
360
-1171
666
-1233
-1
-1
0
#INFIL38
Database 7

0
0
*
*.*
0
DBI
DBI7  
999999
360
-1238
666
-1300
-1
-1
0
#INFIL39
Database 8

0
0
*
*.*
0
DBI
DBI8  
999999
360
-1305
666
-1367
-1
-1
0
#INFIL40
Database 9

0
0
*
*.*
0
DBI
DBI9  
999999
360
-1372
666
-1434
-1
-1
0
#INFIL41
Database 10

0
0
*
*.*
0
DBI
DBI10 
999999
360
-1439
666
-1501
-1
-1
0
#INFIL42
Lookup File 1

0
0
*
*.*
0
LOK
LOOKUPI1
999999
360
-1013
666
-1075
-1
-1
0
#INFIL43
Lookup File 2

0
0
*
*.*
0
LOK
LOOKUPI2
999999
360
-1573
666
-1635
-1
-1
0
#INFIL44
Lookup File 3

0
0
*
*.*
0
LOK
LOOKUPI3
999999
360
-1640
666
-1702
-1
-1
0
#INFIL45
Lookup File 4

0
0
*
*.*
0
LOK
LOOKUPI4
999999
360
-1707
666
-1769
-1
-1
0
#INFIL46
Lookup File 5

0
0
*
*.*
0
LOK
LOOKUPI5
999999
360
-1774
666
-1836
-1
-1
0
#INFIL47
Lookup File 6

0
0
*
*.*
0
LOK
LOOKUPI6
999999
360
-1841
666
-1903
-1
-1
0
#INFIL48
Lookup File 7

0
0
*
*.*
0
LOK
LOOKUPI7
999999
360
-1908
666
-1970
-1
-1
0
#INFIL49
Lookup File 8

0
0
*
*.*
0
LOK
LOOKUPI8
999999
360
-1975
666
-2037
-1
-1
0
#INFIL50
Lookup File 9

0
0
*
*.*
0
LOK
LOOKUPI9
999999
360
-2042
666
-2104
-1
-1
0
#INFIL51
Lookup File 10

0
0
*
*.*
0
LOK
LOOKUPI10
999999
360
-2109
666
-2171
-1
-1
0
#INFIL52
Lookup File 11

0
0
*
*.*
0
LOK
LOOKUPI11
999999
360
-2176
666
-2238
-1
-1
0
#INFIL53
Lookup File 12

0
0
*
*.*
0
LOK
LOOKUPI12
999999
360
-2243
666
-2305
-1
-1
0
#INFIL54
Lookup File 13

0
0
*
*.*
0
LOK
LOOKUPI13
999999
360
-2310
666
-2372
-1
-1
0
#INFIL55
Lookup File 14

0
0
*
*.*
0
LOK
LOOKUPI14
999999
360
-2377
666
-2439
-1
-1
0
#INFIL56
Lookup File 15

0
0
*
*.*
0
LOK
LOOKUPI15
999999
360
-2444
666
-2506
-1
-1
0
#INFIL57
Lookup File 16

0
0
*
*.*
0
LOK
LOOKUPI16
999999
360
-2511
666
-2573
-1
-1
0
#INFIL58
Lookup File 17

0
0
*
*.*
0
LOK
LOOKUPI17
999999
360
-2578
666
-2640
-1
-1
0
#INFIL59
Lookup File 18

0
0
*
*.*
0
LOK
LOOKUPI18
999999
360
-2645
666
-2707
-1
-1
0
#INFIL60
Lookup File 19

0
0
*
*.*
0
LOK
LOOKUPI19
999999
360
-2712
666
-2774
-1
-1
0
#INFIL61
Lookup File 20

0
0
*
*.*
0
LOK
LOOKUPI20
999999
360
-2779
666
-2841
-1
-1
0
#OUTFIL0
Print File

0
0
PRN
*.PRN
0
MAT
OPRN  
999999
882
-542
1183
-604
0
#OUTFIL1
Matrix File 1

0
0
MAT
{SCENARIO_DIR}\HWY_AUTO_TRIP_@ITER@_@PER@.trp
0
MAT
MATO1 
999999
882
-674
1183
-736
0
#OUTFIL2
Matrix File 2

0
0
MAT
{SCENARIO_DIR}\HWY_SPC_AUTO_TRIP_@ITER@_@PER@.trp
0
MAT
MATO2 
999999
882
-741
1183
-803
0
#OUTFIL3
Matrix File 3

0
0
MAT
*.MAT
0
MAT
MATO3 
999999
882
-743
1183
-805
0
#OUTFIL4
Matrix File 4

0
0
MAT
*.MAT
0
MAT
MATO4 
999999
877
512
1183
450
0
#OUTFIL5
Matrix File 5

0
0
MAT
*.MAT
0
MAT
MATO5 
999999
877
445
1183
383
0
#OUTFIL6
Matrix File 6

0
0
MAT
*.MAT
0
MAT
MATO6 
999999
877
378
1183
316
0
#OUTFIL7
Matrix File 7

0
0
MAT
*.MAT
0
MAT
MATO7 
999999
877
311
1183
249
0
#OUTFIL8
Matrix File 8

0
0
MAT
*.MAT
0
MAT
MATO8 
999999
877
244
1183
182
0
#OUTFIL9
Matrix File 9

0
0
MAT
*.MAT
0
MAT
MATO9 
999999
877
177
1183
115
0
#OUTFIL10
Matrix File 10

0
0
MAT
*.MAT
0
MAT
MATO10
999999
877
110
1183
48
0
#OUTFIL11
Matrix File 11

0
0
MAT
*.MAT
0
MAT
MATO11
999999
877
43
1183
-19
0
#OUTFIL12
Matrix File 12

0
0
MAT
*.MAT
0
MAT
MATO12
999999
877
-24
1183
-86
0
#OUTFIL13
Matrix File 13

0
0
MAT
*.MAT
0
MAT
MATO13
999999
877
-91
1183
-153
0
#OUTFIL14
Matrix File 14

0
0
MAT
*.MAT
0
MAT
MATO14
999999
877
-158
1183
-220
0
#OUTFIL15
Matrix File 15

0
0
MAT
*.MAT
0
MAT
MATO15
999999
877
-225
1183
-287
0
#OUTFIL16
Matrix File 16

0
0
MAT
*.MAT
0
MAT
MATO16
999999
877
-292
1183
-354
0
#OUTFIL17
Matrix File 17

0
0
MAT
*.MAT
0
MAT
MATO17
999999
877
-359
1183
-421
0
#OUTFIL18
Matrix File 18

0
0
MAT
*.MAT
0
MAT
MATO18
999999
877
-426
1183
-488
0
#OUTFIL19
Matrix File 19

0
0
MAT
*.MAT
0
MAT
MATO19
999999
877
-493
1183
-555
0
#OUTFIL20
Matrix File 20

0
0
MAT
*.MAT
0
MAT
MATO20
999999
877
-560
1183
-622
0
#OUTFIL21
Record File 1

0
0
DBF
*.DBF
0
MAT
RECO1 
999999
882
-810
1183
-872
0
#OUTFIL22
Record File 2

0
0
DBF
*.DBF
0
MAT
RECO2 
999999
877
-694
1183
-756
0
#OUTFIL23
Record File 3

0
0
DBF
*.DBF
0
MAT
RECO3 
999999
877
-761
1183
-823
0
#OUTFIL24
Record File 4

0
0
DBF
*.DBF
0
MAT
RECO4 
999999
877
-828
1183
-890
0
#OUTFIL25
Record File 5

0
0
DBF
*.DBF
0
MAT
RECO5 
999999
877
-895
1183
-957
0
#OUTFIL26
Record File 6

0
0
DBF
*.DBF
0
MAT
RECO6 
999999
877
-962
1183
-1024
0
#OUTFIL27
Record File 7

0
0
DBF
*.DBF
0
MAT
RECO7 
999999
877
-1029
1183
-1091
0
#OUTFIL28
Record File 8

0
0
DBF
*.DBF
0
MAT
RECO8 
999999
877
-1096
1183
-1158
0
#OUTFIL29
Record File 9

0
0
DBF
*.DBF
0
MAT
RECO9 
999999
877
-1163
1183
-1225
0
#OUTFIL30
Record File 10

0
0
DBF
*.DBF
0
MAT
RECO10
999999
877
-1230
1183
-1292
0
#OUTFIL31
Record File 11

0
0
DBF
*.DBF
0
MAT
RECO11
999999
877
-1297
1183
-1359
0
#OUTFIL32
Record File 12

0
0
DBF
*.DBF
0
MAT
RECO12
999999
877
-1364
1183
-1426
0
#OUTFIL33
Record File 13

0
0
DBF
*.DBF
0
MAT
RECO13
999999
877
-1431
1183
-1493
0
#OUTFIL34
Record File 14

0
0
DBF
*.DBF
0
MAT
RECO14
999999
877
-1498
1183
-1560
0
#OUTFIL35
Record File 15

0
0
DBF
*.DBF
0
MAT
RECO15
999999
877
-1565
1183
-1627
0
#OUTFIL36
Print Data 1

0
0
PRN
*.PRN
0
MAT
PRINTO1
999999
882
-877
1183
-939
0
#OUTFIL37
Print Data 2

0
0
PRN
*.PRN
0
MAT
PRINTO2
999999
877
-1699
1183
-1761
0
#OUTFIL38
Print Data 3

0
0
PRN
*.PRN
0
MAT
PRINTO3
999999
877
-1766
1183
-1828
0
#OUTFIL39
Print Data 4

0
0
PRN
*.PRN
0
MAT
PRINTO4
999999
877
-1833
1183
-1895
0
#OUTFIL40
Print Data 5

0
0
PRN
*.PRN
0
MAT
PRINTO5
999999
877
-1900
1183
-1962
0
#OUTFIL41
Print Data 6

0
0
PRN
*.PRN
0
MAT
PRINTO6
999999
877
-1967
1183
-2029
0
#OUTFIL42
Print Data 7

0
0
PRN
*.PRN
0
MAT
PRINTO7
999999
877
-2034
1183
-2096
0
#OUTFIL43
Print Data 8

0
0
PRN
*.PRN
0
MAT
PRINTO8
999999
877
-2101
1183
-2163
0
#OUTFIL44
Print Data 9

0
0
PRN
*.PRN
0
MAT
PRINTO9
999999
877
-2168
1183
-2230
0
#OUTFIL45
Print Data 10

0
0
PRN
*.PRN
0
MAT
PRINTO10
999999
877
-2235
1183
-2297
0
#PROGRAM2
4
0
3


HIGHWAY

1
1
0
-1.0
Assignment Period: @ASSIGNNAME@
999999
1806
-733
2016
-803
0
0
0
#INFIL0
Script File

0
0
S
C:\Users\helseljw\OneDrive - WSP O365\met_council\model_files\WSPHandoff_Jan2019\ABM 2017\CUBE\HTHWY00B.S
1
HWY
ISCR1 
999999
1489
-537
1795
-599
-1
-1
0
#INFIL1
Matrix File 1

0
0
MAT
{SCENARIO_DIR}\HWY_AUTO_TRIP_@ITER@_@PER@.trp
0
HWY
MATI1 
999999
1489
-604
1795
-666
1
1
0
#INFIL2
Matrix File 2

0
0
MAT
{SCENARIO_DIR}\TRK_TRIP_@ITER@_@PER@.trp
0
HWY
MATI2 
999999
1489
-671
1795
-733
-1
-1
0
#INFIL3
Matrix File 3

0
0
MAT
{SCENARIO_DIR}\HWY_EXT_TRIP_@ITER@_@PER@.trp
0
HWY
MATI3 
999999
1489
-738
1795
-800
-1
-1
0
#INFIL4
Matrix File 4

0
0
MAT
{SCENARIO_DIR}\HWY_SPC_AUTO_TRIP_@ITER@_@PER@.trp
0
HWY
MATI4 
999999
1489
-805
1795
-867
1
2
0
#INFIL5
Matrix File 5

0
0
MAT
*.MAT
0
HWY
MATI5 
999999
1489
-641
1795
-703
-1
-1
0
#INFIL6
Matrix File 6

0
0
MAT
*.MAT
0
HWY
MATI6 
999999
1489
1307
1795
1245
-1
-1
0
#INFIL7
Matrix File 7

0
0
MAT
*.MAT
0
HWY
MATI7 
999999
1489
1240
1795
1178
-1
-1
0
#INFIL8
Matrix File 8

0
0
MAT
*.MAT
0
HWY
MATI8 
999999
1489
1173
1795
1111
-1
-1
0
#INFIL9
Matrix File 9

0
0
MAT
*.MAT
0
HWY
MATI9 
999999
1489
1106
1795
1044
-1
-1
0
#INFIL10
Matrix File 10

0
0
MAT
*.MAT
0
HWY
MATI10
999999
1489
1039
1795
977
-1
-1
0
#INFIL11
Matrix File 11

0
0
MAT
*.MAT
0
HWY
MATI11
999999
1489
972
1795
910
-1
-1
0
#INFIL12
Matrix File 12

0
0
MAT
*.MAT
0
HWY
MATI12
999999
1489
905
1795
843
-1
-1
0
#INFIL13
Matrix File 13

0
0
MAT
*.MAT
0
HWY
MATI13
999999
1489
838
1795
776
-1
-1
0
#INFIL14
Matrix File 14

0
0
MAT
*.MAT
0
HWY
MATI14
999999
1489
771
1795
709
-1
-1
0
#INFIL15
Matrix File 15

0
0
MAT
*.MAT
0
HWY
MATI15
999999
1489
704
1795
642
-1
-1
0
#INFIL16
Matrix File 16

0
0
MAT
*.MAT
0
HWY
MATI16
999999
1489
637
1795
575
-1
-1
0
#INFIL17
Matrix File 17

0
0
MAT
*.MAT
0
HWY
MATI17
999999
1489
570
1795
508
-1
-1
0
#INFIL18
Matrix File 18

0
0
MAT
*.MAT
0
HWY
MATI18
999999
1489
503
1795
441
-1
-1
0
#INFIL19
Matrix File 19

0
0
MAT
*.MAT
0
HWY
MATI19
999999
1489
436
1795
374
-1
-1
0
#INFIL20
Matrix File 20

0
0
MAT
*.MAT
0
HWY
MATI20
999999
1489
369
1795
307
-1
-1
0
#INFIL21
Network File

0
0
NET
{SCENARIO_DIR}\@HWY_NET@
0
HWY
NETI  
999999
1489
-872
1795
-934
-1
-9
0
#INFIL22
Sub Area Net

0
0
NET
*.NET
0
SBN
SUBAREANETI
999999
1489
-775
1795
-837
-1
-1
0
#INFIL23
Intersctn Data

0
0
IND
*.IND
0
IND
JUNCTIONI
999999
1489
-842
1795
-904
-1
-1
0
#INFIL24
Turn Penalties

0
0
PEN
*.PEN
0
TRN
TURNPENI
999999
1489
-909
1795
-971
-1
-1
0
#INFIL25
Zonal Data 1

0
0
*
*.*
0
ZON
ZDATI1
999999
1489
-976
1795
-1038
-1
-1
0
#INFIL26
Zonal Data 2

0
0
*
*.*
0
ZON
ZDATI2
999999
1489
-33
1795
-95
-1
-1
0
#INFIL27
Zonal Data 3

0
0
*
*.*
0
ZON
ZDATI3
999999
1489
-100
1795
-162
-1
-1
0
#INFIL28
Zonal Data 4

0
0
*
*.*
0
ZON
ZDATI4
999999
1489
-167
1795
-229
-1
-1
0
#INFIL29
Zonal Data 5

0
0
*
*.*
0
ZON
ZDATI5
999999
1489
-234
1795
-296
-1
-1
0
#INFIL30
Zonal Data 6

0
0
*
*.*
0
ZON
ZDATI6
999999
1489
-301
1795
-363
-1
-1
0
#INFIL31
Zonal Data 7

0
0
*
*.*
0
ZON
ZDATI7
999999
1489
-368
1795
-430
-1
-1
0
#INFIL32
Zonal Data 8

0
0
*
*.*
0
ZON
ZDATI8
999999
1489
-435
1795
-497
-1
-1
0
#INFIL33
Zonal Data 9

0
0
*
*.*
0
ZON
ZDATI9
999999
1489
-502
1795
-564
-1
-1
0
#INFIL34
Zonal Data 10

0
0
*
*.*
0
ZON
ZDATI10
999999
1489
-569
1795
-631
-1
-1
0
#INFIL35
Toll Matrix 1

0
0
*
*.*
0
TOL
TOLLMATI1
999999
1489
-1043
1795
-1105
-1
-1
0
#INFIL36
Toll Matrix 2

0
0
*
*.*
0
TOL
TOLLMATI2
999999
1489
-703
1795
-765
-1
-1
0
#INFIL37
Toll Matrix 3

0
0
*
*.*
0
TOL
TOLLMATI3
999999
1489
-770
1795
-832
-1
-1
0
#INFIL38
Toll Matrix 4

0
0
*
*.*
0
TOL
TOLLMATI4
999999
1489
-837
1795
-899
-1
-1
0
#INFIL39
Toll Matrix 5

0
0
*
*.*
0
TOL
TOLLMATI5
999999
1489
-904
1795
-966
-1
-1
0
#INFIL40
Toll Matrix 6

0
0
*
*.*
0
TOL
TOLLMATI6
999999
1489
-971
1795
-1033
-1
-1
0
#INFIL41
Toll Matrix 7

0
0
*
*.*
0
TOL
TOLLMATI7
999999
1489
-1038
1795
-1100
-1
-1
0
#INFIL42
Toll Matrix 8

0
0
*
*.*
0
TOL
TOLLMATI8
999999
1489
-1105
1795
-1167
-1
-1
0
#INFIL43
Toll Matrix 9

0
0
*
*.*
0
TOL
TOLLMATI9
999999
1489
-1172
1795
-1234
-1
-1
0
#INFIL44
Toll Matrix 10

0
0
*
*.*
0
TOL
TOLLMATI10
999999
1489
-1239
1795
-1301
-1
-1
0
#INFIL45
Lookup File 1

0
0
*
{LU_WILL2PAY}
0
LOK
LOOKUPI1
999999
1489
-939
1795
-1001
-1
-9
0
#INFIL46
Lookup File 2

0
0
*
*.*
0
LOK
LOOKUPI2
999999
1489
-1177
1795
-1239
-1
-1
0
#INFIL47
Lookup File 3

0
0
*
*.*
0
LOK
LOOKUPI3
999999
1489
-1440
1795
-1502
-1
-1
0
#INFIL48
Lookup File 4

0
0
*
*.*
0
LOK
LOOKUPI4
999999
1489
-1507
1795
-1569
-1
-1
0
#INFIL49
Lookup File 5

0
0
*
*.*
0
LOK
LOOKUPI5
999999
1489
-1574
1795
-1636
-1
-1
0
#INFIL50
Lookup File 6

0
0
*
*.*
0
LOK
LOOKUPI6
999999
1489
-1641
1795
-1703
-1
-1
0
#INFIL51
Lookup File 7

0
0
*
*.*
0
LOK
LOOKUPI7
999999
1489
-1708
1795
-1770
-1
-1
0
#INFIL52
Lookup File 8

0
0
*
*.*
0
LOK
LOOKUPI8
999999
1489
-1775
1795
-1837
-1
-1
0
#INFIL53
Lookup File 9

0
0
*
*.*
0
LOK
LOOKUPI9
999999
1489
-1842
1795
-1904
-1
-1
0
#INFIL54
Lookup File 10

0
0
*
*.*
0
LOK
LOOKUPI10
999999
1489
-1909
1795
-1971
-1
-1
0
#INFIL55
Lookup File 11

0
0
*
*.*
0
LOK
LOOKUPI11
999999
1489
-1976
1795
-2038
-1
-1
0
#INFIL56
Lookup File 12

0
0
*
*.*
0
LOK
LOOKUPI12
999999
1489
-2043
1795
-2105
-1
-1
0
#INFIL57
Lookup File 13

0
0
*
*.*
0
LOK
LOOKUPI13
999999
1489
-2110
1795
-2172
-1
-1
0
#INFIL58
Lookup File 14

0
0
*
*.*
0
LOK
LOOKUPI14
999999
1489
-2177
1795
-2239
-1
-1
0
#INFIL59
Lookup File 15

0
0
*
*.*
0
LOK
LOOKUPI15
999999
1489
-2244
1795
-2306
-1
-1
0
#INFIL60
Lookup File 16

0
0
*
*.*
0
LOK
LOOKUPI16
999999
1489
-2311
1795
-2373
-1
-1
0
#INFIL61
Lookup File 17

0
0
*
*.*
0
LOK
LOOKUPI17
999999
1489
-2378
1795
-2440
-1
-1
0
#INFIL62
Lookup File 18

0
0
*
*.*
0
LOK
LOOKUPI18
999999
1489
-2445
1795
-2507
-1
-1
0
#INFIL63
Lookup File 19

0
0
*
*.*
0
LOK
LOOKUPI19
999999
1489
-2512
1795
-2574
-1
-1
0
#INFIL64
Lookup File 20

0
0
*
*.*
0
LOK
LOOKUPI20
999999
1489
-2579
1795
-2641
-1
-1
0
#INFIL65
Lookup File 21

0
0
*
*.*
0
LOK
LOOKUPI21
999999
1489
-2646
1795
-2708
-1
-1
0
#INFIL66
Lookup File 22

0
0
*
*.*
0
LOK
LOOKUPI22
999999
1489
-2713
1795
-2775
-1
-1
0
#INFIL67
Lookup File 23

0
0
*
*.*
0
LOK
LOOKUPI23
999999
1489
-2780
1795
-2842
-1
-1
0
#INFIL68
Lookup File 24

0
0
*
*.*
0
LOK
LOOKUPI24
999999
1489
-2847
1795
-2909
-1
-1
0
#INFIL69
Lookup File 25

0
0
*
*.*
0
LOK
LOOKUPI25
999999
1489
-2914
1795
-2976
-1
-1
0
#INFIL70
Lookup File 26

0
0
*
*.*
0
LOK
LOOKUPI26
999999
1489
-2981
1795
-3043
-1
-1
0
#INFIL71
Lookup File 27

0
0
*
*.*
0
LOK
LOOKUPI27
999999
1489
-3048
1795
-3110
-1
-1
0
#INFIL72
Lookup File 28

0
0
*
*.*
0
LOK
LOOKUPI28
999999
1489
-3115
1795
-3177
-1
-1
0
#INFIL73
Lookup File 29

0
0
*
*.*
0
LOK
LOOKUPI29
999999
1489
-3182
1795
-3244
-1
-1
0
#INFIL74
Lookup File 30

0
0
*
*.*
0
LOK
LOOKUPI30
999999
1489
-3249
1795
-3311
-1
-1
0
#OUTFIL0
Print File

0
0
PRN
*.PRN
0
HWY
OPRN  
999999
2032
-339
2333
-401
0
#OUTFIL1
Matrix File 1

0
0
MAT
{SCENARIO_DIR}\HWY_SKIM_@ITER@_@PER@.tmp
0
HWY
MATO1 
999999
2032
-669
2333
-731
0
#OUTFIL2
Matrix File 2

0
0
MAT
*.MAT
0
HWY
MATO2 
999999
2032
-473
2333
-535
0
#OUTFIL3
Matrix File 3

0
0
MAT
*.MAT
0
HWY
MATO3 
999999
2006
1937
2312
1875
0
#OUTFIL4
Matrix File 4

0
0
MAT
*.MAT
0
HWY
MATO4 
999999
2006
1870
2312
1808
0
#OUTFIL5
Matrix File 5

0
0
MAT
*.MAT
0
HWY
MATO5 
999999
2006
1803
2312
1741
0
#OUTFIL6
Matrix File 6

0
0
MAT
*.MAT
0
HWY
MATO6 
999999
2006
1736
2312
1674
0
#OUTFIL7
Matrix File 7

0
0
MAT
*.MAT
0
HWY
MATO7 
999999
2006
1669
2312
1607
0
#OUTFIL8
Matrix File 8

0
0
MAT
*.MAT
0
HWY
MATO8 
999999
2006
1602
2312
1540
0
#OUTFIL9
Matrix File 9

0
0
MAT
*.MAT
0
HWY
MATO9 
999999
2006
1535
2312
1473
0
#OUTFIL10
Matrix File 10

0
0
MAT
*.MAT
0
HWY
MATO10
999999
2006
1468
2312
1406
0
#OUTFIL11
Matrix File 11

0
0
MAT
*.MAT
0
HWY
MATO11
999999
2006
1401
2312
1339
0
#OUTFIL12
Matrix File 12

0
0
MAT
*.MAT
0
HWY
MATO12
999999
2006
1334
2312
1272
0
#OUTFIL13
Matrix File 13

0
0
MAT
*.MAT
0
HWY
MATO13
999999
2006
1267
2312
1205
0
#OUTFIL14
Matrix File 14

0
0
MAT
*.MAT
0
HWY
MATO14
999999
2006
1200
2312
1138
0
#OUTFIL15
Matrix File 15

0
0
MAT
*.MAT
0
HWY
MATO15
999999
2006
1133
2312
1071
0
#OUTFIL16
Matrix File 16

0
0
MAT
*.MAT
0
HWY
MATO16
999999
2006
1066
2312
1004
0
#OUTFIL17
Matrix File 17

0
0
MAT
*.MAT
0
HWY
MATO17
999999
2006
999
2312
937
0
#OUTFIL18
Matrix File 18

0
0
MAT
*.MAT
0
HWY
MATO18
999999
2006
932
2312
870
0
#OUTFIL19
Matrix File 19

0
0
MAT
*.MAT
0
HWY
MATO19
999999
2006
865
2312
803
0
#OUTFIL20
Matrix File 20

0
0
MAT
*.MAT
0
HWY
MATO20
999999
2006
798
2312
736
0
#OUTFIL21
Sub Area Mat.

0
0
MAT
*.MAT
0
HWY
SUBAREAMATO
999999
2032
-540
2333
-602
0
#OUTFIL22
Network File

0
0
NET
{SCENARIO_DIR}\HWY_LDNET_@ITER@_@PER@.NET
0
HWY
NETO  
999999
2032
-736
2333
-798
0
#OUTFIL23
Turn Flows

0
0
INT
*.INT
0
HWY
JUNCTIONO
999999
2032
-674
2333
-736
0
#OUTFIL24
Turn Volumes 1

0
0
TRN
*.TRN
0
HWY
TURNVOLO1
999999
2032
-741
2333
-803
0
#OUTFIL25
Turn Volumes 2

0
0
TRN
*.TRN
0
HWY
TURNVOLO2
999999
2006
463
2312
401
0
#OUTFIL26
Turn Volumes 3

0
0
TRN
*.TRN
0
HWY
TURNVOLO3
999999
2006
396
2312
334
0
#OUTFIL27
Turn Volumes 4

0
0
TRN
*.TRN
0
HWY
TURNVOLO4
999999
2006
329
2312
267
0
#OUTFIL28
Turn Volumes 5

0
0
TRN
*.TRN
0
HWY
TURNVOLO5
999999
2006
262
2312
200
0
#OUTFIL29
Turn Penalties

0
0
DAT
*.DAT
0
HWY
TURNPENO
999999
2032
-808
2333
-870
0
#OUTFIL30
Screenlines 1

0
0
DAT
*.DAT
0
HWY
ESTMDATO1
999999
2032
-875
2333
-937
0
#OUTFIL31
Screenlines 2

0
0
DAT
*.DAT
0
HWY
ESTMDATO2
999999
2006
61
2312
-1
0
#OUTFIL32
Screenlines 3

0
0
DAT
*.DAT
0
HWY
ESTMDATO3
999999
2006
-6
2312
-68
0
#OUTFIL33
Screenlines 4

0
0
DAT
*.DAT
0
HWY
ESTMDATO4
999999
2006
-73
2312
-135
0
#OUTFIL34
Screenlines 5

0
0
DAT
*.DAT
0
HWY
ESTMDATO5
999999
2006
-140
2312
-202
0
#OUTFIL35
Screenlines 6

0
0
DAT
*.DAT
0
HWY
ESTMDATO6
999999
2006
-207
2312
-269
0
#OUTFIL36
Screenlines 7

0
0
DAT
*.DAT
0
HWY
ESTMDATO7
999999
2006
-274
2312
-336
0
#OUTFIL37
Screenlines 8

0
0
DAT
*.DAT
0
HWY
ESTMDATO8
999999
2006
-341
2312
-403
0
#OUTFIL38
Screenlines 9

0
0
DAT
*.DAT
0
HWY
ESTMDATO9
999999
2006
-408
2312
-470
0
#OUTFIL39
Screenlines 10

0
0
DAT
*.DAT
0
HWY
ESTMDATO10
999999
2006
-475
2312
-537
0
#OUTFIL40
Screenlines 11

0
0
DAT
*.DAT
0
HWY
ESTMDATO11
999999
2006
-542
2312
-604
0
#OUTFIL41
Screenlines 12

0
0
DAT
*.DAT
0
HWY
ESTMDATO12
999999
2006
-609
2312
-671
0
#OUTFIL42
Screenlines 13

0
0
DAT
*.DAT
0
HWY
ESTMDATO13
999999
2006
-676
2312
-738
0
#OUTFIL43
Screenlines 14

0
0
DAT
*.DAT
0
HWY
ESTMDATO14
999999
2006
-743
2312
-805
0
#OUTFIL44
Screenlines 15

0
0
DAT
*.DAT
0
HWY
ESTMDATO15
999999
2006
-810
2312
-872
0
#OUTFIL45
Screenlines 16

0
0
DAT
*.DAT
0
HWY
ESTMDATO16
999999
2006
-877
2312
-939
0
#OUTFIL46
Screenlines 17

0
0
DAT
*.DAT
0
HWY
ESTMDATO17
999999
2006
-944
2312
-1006
0
#OUTFIL47
Screenlines 18

0
0
DAT
*.DAT
0
HWY
ESTMDATO18
999999
2006
-1011
2312
-1073
0
#OUTFIL48
Screenlines 19

0
0
DAT
*.DAT
0
HWY
ESTMDATO19
999999
2006
-1078
2312
-1140
0
#OUTFIL49
Screenlines 20

0
0
DAT
*.DAT
0
HWY
ESTMDATO20
999999
2006
-1145
2312
-1207
0
#OUTFIL50
ICP File 1

0
0
ICP
*.ICP
0
HWY
ESTMICPO1
999999
2032
-942
2333
-1004
0
#OUTFIL51
ICP File 2

0
0
ICP
*.ICP
0
HWY
ESTMICPO2
999999
2006
-1279
2312
-1341
0
#OUTFIL52
ICP File 3

0
0
ICP
*.ICP
0
HWY
ESTMICPO3
999999
2006
-1346
2312
-1408
0
#OUTFIL53
ICP File 4

0
0
ICP
*.ICP
0
HWY
ESTMICPO4
999999
2006
-1413
2312
-1475
0
#OUTFIL54
ICP File 5

0
0
ICP
*.ICP
0
HWY
ESTMICPO5
999999
2006
-1480
2312
-1542
0
#OUTFIL55
ICP File 6

0
0
ICP
*.ICP
0
HWY
ESTMICPO6
999999
2006
-1547
2312
-1609
0
#OUTFIL56
ICP File 7

0
0
ICP
*.ICP
0
HWY
ESTMICPO7
999999
2006
-1614
2312
-1676
0
#OUTFIL57
ICP File 8

0
0
ICP
*.ICP
0
HWY
ESTMICPO8
999999
2006
-1681
2312
-1743
0
#OUTFIL58
ICP File 9

0
0
ICP
*.ICP
0
HWY
ESTMICPO9
999999
2006
-1748
2312
-1810
0
#OUTFIL59
ICP File 10

0
0
ICP
*.ICP
0
HWY
ESTMICPO10
999999
2006
-1815
2312
-1877
0
#OUTFIL60
ICP File 11

0
0
ICP
*.ICP
0
HWY
ESTMICPO11
999999
2006
-1882
2312
-1944
0
#OUTFIL61
ICP File 12

0
0
ICP
*.ICP
0
HWY
ESTMICPO12
999999
2006
-1949
2312
-2011
0
#OUTFIL62
ICP File 13

0
0
ICP
*.ICP
0
HWY
ESTMICPO13
999999
2006
-2016
2312
-2078
0
#OUTFIL63
ICP File 14

0
0
ICP
*.ICP
0
HWY
ESTMICPO14
999999
2006
-2083
2312
-2145
0
#OUTFIL64
ICP File 15

0
0
ICP
*.ICP
0
HWY
ESTMICPO15
999999
2006
-2150
2312
-2212
0
#OUTFIL65
ICP File 16

0
0
ICP
*.ICP
0
HWY
ESTMICPO16
999999
2006
-2217
2312
-2279
0
#OUTFIL66
ICP File 17

0
0
ICP
*.ICP
0
HWY
ESTMICPO17
999999
2006
-2284
2312
-2346
0
#OUTFIL67
ICP File 18

0
0
ICP
*.ICP
0
HWY
ESTMICPO18
999999
2006
-2351
2312
-2413
0
#OUTFIL68
ICP File 19

0
0
ICP
*.ICP
0
HWY
ESTMICPO19
999999
2006
-2418
2312
-2480
0
#OUTFIL69
ICP File 20

0
0
ICP
*.ICP
0
HWY
ESTMICPO20
999999
2006
-2485
2312
-2547
0
#OUTFIL70
Path File 1

0
0
PTH
*.PTH
0
HWY
PATHO1
999999
2032
-1009
2333
-1071
0
#OUTFIL71
Path File 2

0
0
PTH
*.PTH
0
HWY
PATHO2
999999
2006
-2619
2312
-2681
0
#OUTFIL72
Path File 3

0
0
PTH
*.PTH
0
HWY
PATHO3
999999
2006
-2686
2312
-2748
0
#OUTFIL73
Path File 4

0
0
PTH
*.PTH
0
HWY
PATHO4
999999
2006
-2753
2312
-2815
0
#OUTFIL74
Path File 5

0
0
PTH
*.PTH
0
HWY
PATHO5
999999
2006
-2820
2312
-2882
0
#OUTFIL75
Path File 6

0
0
PTH
*.PTH
0
HWY
PATHO6
999999
2006
-2887
2312
-2949
0
#OUTFIL76
Path File 7

0
0
PTH
*.PTH
0
HWY
PATHO7
999999
2006
-2954
2312
-3016
0
#OUTFIL77
Path File 8

0
0
PTH
*.PTH
0
HWY
PATHO8
999999
2006
-3021
2312
-3083
0
#OUTFIL78
Print Data 1

0
0
PRN
{SCENARIO_DIR}\HWY_LDNET_PRN_@ITER@_@PER@.txt
0
HWY
PRINTO1
999999
2032
-803
2333
-865
0
#OUTFIL79
Print Data 2

0
0
PRN
*.PRN
0
HWY
PRINTO2
999999
2032
-1143
2333
-1205
0
#OUTFIL80
Print Data 3

0
0
PRN
*.PRN
0
HWY
PRINTO3
999999
2006
-3222
2312
-3284
0
#OUTFIL81
Print Data 4

0
0
PRN
*.PRN
0
HWY
PRINTO4
999999
2006
-3289
2312
-3351
0
#OUTFIL82
Print Data 5

0
0
PRN
*.PRN
0
HWY
PRINTO5
999999
2006
-3356
2312
-3418
0
#OUTFIL83
Print Data 6

0
0
PRN
*.PRN
0
HWY
PRINTO6
999999
2006
-3423
2312
-3485
0
#OUTFIL84
Print Data 7

0
0
PRN
*.PRN
0
HWY
PRINTO7
999999
2006
-3490
2312
-3552
0
#OUTFIL85
Print Data 8

0
0
PRN
*.PRN
0
HWY
PRINTO8
999999
2006
-3557
2312
-3619
0
#OUTFIL86
Print Data 9

0
0
PRN
*.PRN
0
HWY
PRINTO9
999999
2006
-3624
2312
-3686
0
#OUTFIL87
Print Data 10

0
0
PRN
*.PRN
0
HWY
PRINTO10
999999
2006
-3691
2312
-3753
0
#PROGRAM3
5
0
4


PILOT

1
1
0
-1.0
End Highway Period Loop
999999
536
-1100
725
-1170
0
0
0
#INFIL0
Script File

0
0
S
C:\Users\helseljw\OneDrive - WSP O365\met_council\model_files\WSPHandoff_Jan2019\ABM 2017\CUBE\HTPIL00E.S
1
PIL
ISCR1 
999999
219
-1102
525
-1164
-1
-1
0
#INFIL1
Variable File

0
0
VAR
*.VAR
0
VRI
VARI  
999999
219
-1136
525
-1198
-1
-1
0
#OUTFIL0
Print Data 1

0
0
PRN
*.PRN
0
PIL
PRINTO1
999999
741
-1102
1042
-1164
0
#OUTFIL1
Print Data 2

0
0
PRN
*.PRN
0
PIL
PRINTO2
999999
736
-870
1042
-932
0
#OUTFIL2
Print Data 3

0
0
PRN
*.PRN
0
PIL
PRINTO3
999999
736
-937
1042
-999
0
#OUTFIL3
Print Data 4

0
0
PRN
*.PRN
0
PIL
PRINTO4
999999
736
-1004
1042
-1066
0
#OUTFIL4
Print Data 5

0
0
PRN
*.PRN
0
PIL
PRINTO5
999999
736
-1071
1042
-1133
0
#OUTFIL5
Print Data 6

0
0
PRN
*.PRN
0
PIL
PRINTO6
999999
736
-1138
1042
-1200
0
#OUTFIL6
Print Data 7

0
0
PRN
*.PRN
0
PIL
PRINTO7
999999
736
-1205
1042
-1267
0
#OUTFIL7
Print Data 8

0
0
PRN
*.PRN
0
PIL
PRINTO8
999999
736
-1272
1042
-1334
0
#OUTFIL8
Print Data 9

0
0
PRN
*.PRN
0
PIL
PRINTO9
999999
736
-1339
1042
-1401
0
#OUTFIL9
Print Data 10

0
0
PRN
*.PRN
0
PIL
PRINTO10
999999
736
-1406
1042
-1468
0
#PROGRAM4
3
1
6

C:\Users\helseljw\OneDrive - WSP O365\met_council\model_files\WSPHandoff_Jan2019\ABM 2017\CUBE\FINALPOSTPROC00.APP
Post Processing

0
1
0


999999
282
-1664
743
-1784
0
0
0
#PROGRAM5
6
1
5

C:\Users\helseljw\OneDrive - WSP O365\met_council\model_files\WSPHandoff_Jan2019\ABM 2017\CUBE\TRANSITASSIGNMENT00.APP
PublicTransit Assignment

0
1
0


999999
282
-1410
743
-1530
0
0
0
