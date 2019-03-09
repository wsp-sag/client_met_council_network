::~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
:: run_initial_auto_skim.bat
::
:: MS-DOS batch file to execute the Auto Skim step of teh Met Council travel 
:: model.  
::
::
::~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:: ----------------------------------------------------------------------------
::
:: Step 1:  Set the necessary path variables
::
:: ----------------------------------------------------------------------------
set "beginComment=goto :endComment"

:: The location of the RUNTPP executable from Citilabs - 64bit first
set TPP_PATH=C:\Program Files\Citilabs\CubeVoyager;C:\Program Files (x86)\Citilabs\CubeVoyager

:: The location of python
set PYTHON_PATH=C:\Python27

:: Add these variables to the PATH environment variable, moving the current path to the back
set OLD_PATH=%PATH%
set PATH=%RUNTIME%;%TPP_PATH%;%PYTHON_PATH%;%OLD_PATH%

:: Set CSV input paths
set CSV_FOLDER=network_03042019
set HWY_LINK_PATH=%CSV_FOLDER%/fixed_drive_network_for_modeling.csv
set HWY_NODE_PATH=%CSV_FOLDER%/fixed_osm_drive_nodes_with_centroid.csv
set BIKE_LINK_PATH=%CSV_FOLDER%/fixed_bike_network_for_modeling.csv
set BIKE_NODE_PATH=%CSV_FOLDER%/fixed_osm_bike_nodes_with_centroid.csv
set WALK_LINK_PATH=%CSV_FOLDER%/fixed_walk_network_for_modeling.csv
set WALK_NODE_PATH=%CSV_FOLDER%/fixed_osm_walk_nodes_with_centroid.csv

set HWY_LINK_VAR=A,B,DISTANCE,COUNTY,T_PRIORITY,BIKE,AREA,HOV,AADT,AM_CNT,MD_CNT,PM_CNT,NT_CNT,DY_CNT,ASGNGRP,LANES,CENTROID,RC_NUM,isDriveLink
set HWY_NODE_VAR=N,X,Y,OSMID
set BIKE_LINK_VAR=A,B,DISTANCE,COUNTY,AREA,CENTROID,isBikeLink
set BIKE_NODE_VAR=N,X,Y,OSMID
set WALK_LINK_VAR=A,B,DISTANCE,COUNTY,AREA,CENTROID,isPedLink
set WALK_NODE_VAR=N,X,Y,OSMID

:: Set path to adjusted scripts that have been updated with new tokens.
set REPLACEMENT_PATH=replacement_scripts

set SCENARIO_DIR=temp

runtpp %REPLACEMENT_PATH%\make_highway_network_from_csv.s

runtpp %REPLACEMENT_PATH%\make_bike_network_from_csv.s

runtpp %REPLACEMENT_PATH%\make_walk_network_from_csv.s

runtpp %REPLACEMENT_PATH%\FullMakeNetwork15.s

::HIGHWAY

:: Set highway network
set iHwyNet=%SCENARIO_DIR%/highway_2015.net

set LU_AlphaBeta=C:/Users/helseljw/OneDrive - WSP O365/met_council/model_files/WSPHandoff_Jan2019/ABM 2017/Input/AlphaBetaLookup.txt
set LU_capacity=C:/Users/helseljw/OneDrive - WSP O365/met_council/model_files/WSPHandoff_Jan2019/ABM 2017/Input/SpeedLookup85.txt
set LU_speed=C:/Users/helseljw/OneDrive - WSP O365/met_council/model_files/WSPHandoff_Jan2019/ABM 2017/Input/CapacityLookup.txt

runtpp %REPLACEMENT_PATH%\BNNET00B.s

runtpp %REPLACEMENT_PATH%\HNNET00B.s

set TOD=1
set NETNAME=Overnight 7:00 PM to 5:00 AM
::runtpp %REPLACEMENT_PATH%\HNPIL00A.s

runtpp %REPLACEMENT_PATH%\HNNET00C.s

::runtpp %REPLACEMENT_PATH%\HNPIL00B.s

::runtpp %REPLACEMENT_PATH%\HNPIL00C.s

:: CSPIL00A.s copies skims from a prior iteration. DO NOT USE HERE
::runtpp %REPLACEMENT_PATH%\CSPIL00A.s

::runtpp %REPLACEMENT_PATH%\FFHWY00A.s

::runtpp %REPLACEMENT_PATH%\FFPIL00A.s

::NON-MOTORIZED
set bikeSpeed1=13
set bikeSpeed2=13
set bikeSpeed3=10
set bikeFact1=0.8
set walkSpeed=2.5

::runtpp %REPLACEMENT_PATH%\NMNET00A.s

::runtpp %REPLACEMENT_PATH%\NMHWY00A.s

::runtpp %REPLACEMENT_PATH%\NMHWY00B.s

::runtpp %REPLACEMENT_PATH%\NMMAT00A.s

::endComment