::~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
:: run_initial_auto_skim.bat
::
:: MS-DOS batch file to execute the Auto Skim step of teh Met Council travel
:: model.
::
::
::~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@echo off
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
set NETWORK_FOLDER=network_03122019
set SCRIPT_PATH=replacement_scripts
set TRIP_DIR=trip_files
if not exist \outputs mkdir \outputs
set SCENARIO_DIR=outputs
set COMPARISON_DIR=comparisons

set HWY_LINK_PATH=%NETWORK_FOLDER%/drive_and_rail_link.dbf
set HWY_NODE_PATH=%NETWORK_FOLDER%/drive_node_with_rail.dbf
set BIKE_LINK_PATH=%NETWORK_FOLDER%/bike_link.dbf
set BIKE_NODE_PATH=%NETWORK_FOLDER%/bike_node.dbf
set WALK_LINK_PATH=%NETWORK_FOLDER%/walk_link.dbf
set WALK_NODE_PATH=%NETWORK_FOLDER%/walk_node.dbf
set TRANSIT_PATH=%NETWORK_FOLDER%/transit.lin
::set WALK_LINK_PATH=%NETWORK_FOLDER%/test_walk_link.dbf
::set WALK_NODE_PATH=%NETWORK_FOLDER%/test_walk_node.dbf

set max_threads=16
set ITER=1
set PREV_ITER=0

set bikeSpeed1=13
set bikeSpeed2=13
set bikeSpeed3=10
set bikeFact1=0.8
set walkSpeed=2.5

set hwy_assignIters=1
set hwy_HOV2OCC=2
set hwy_HOV3OCC=3.2
set zones=3061
set LU_will2pay=lookup_files/Will2Pay_oneCurve.txt
set hwy_TrkFac=2
set hwy_TollSetting=1

%beginComment%
:: Make Networks
runtpp %SCRIPT_PATH%\make_highway_network_from_file.s
runtpp %SCRIPT_PATH%\make_bike_network_from_file.s
runtpp %SCRIPT_PATH%\make_walk_network_from_file.s
runtpp %SCRIPT_PATH%\FullMakeNetwork15.s


::HIGHWAY
:: Set highway network
set iHwyNet=%SCENARIO_DIR%/highway_2015.net

set LU_AlphaBeta=lookup_files/AlphaBetaLookup.txt
set LU_capacity=lookup_files/SpeedLookup85.txt
set LU_speed=lookup_files/CapacityLookup.txt

runtpp %SCRIPT_PATH%\BNNET00B.s
runtpp %SCRIPT_PATH%\HNNET00B.s

:: This script handles TOD assignment. Batch files require a single character
:: variable.

for /L %%I IN (1, 1, 6) DO (
	set TOD=%%I

	IF %%I EQU 1 (set NETNAME=Overnight 7:00 PM to 5:00 AM)
	IF %%I EQU 2 (set NETNAME=Reverse Lane Change Over 5:00 AM to 6:00 AM  and 1:00 PM to 2:00 PM)
	IF %%I EQU 3 (set NETNAME=AM Peak Period 6:00 AM to 10:00 AM)
	IF %%I EQU 4 (set NETNAME=Mid Day Period 10:00 AM to 1:00 PM)
	IF %%I EQU 5 (set NETNAME=Pre PM Peak Period 2:00 PM to 3:00 PM)
	IF %%I EQU 6 (set NETNAME=PM Peak Period 3:00 PM to 7:00 PM)

	runtpp %SCRIPT_PATH%\HNNET00C.s
)

:: CSPIL00A.s copies skims from a prior iteration. DO NOT USE HERE

runtpp %SCRIPT_PATH%\FFHWY00A.s
runtpp %SCRIPT_PATH%\FFPIL00A.s

::NON-MOTORIZED Networks
runtpp %SCRIPT_PATH%\NMNET00A.s
runtpp %SCRIPT_PATH%\NMHWY00A.s
runtpp %SCRIPT_PATH%\NMHWY00B.s
runtpp %SCRIPT_PATH%\NMMAT00A.s

:: Begin highway assignment scripts (step 7)
runtpp %SCRIPT_PATH%\HAPIL00D.s
runtpp %SCRIPT_PATH%\HAMAT00E.s
runtpp %SCRIPT_PATH%\HAMAT00G.s
runtpp %SCRIPT_PATH%\HAMAT00I.s
runtpp %SCRIPT_PATH%\HAMAT00K.s

for /L %%I IN (1, 1, 4) DO (

	set TOD=%%I

:: Following if statements replace HAPIL00A.s
	IF %%I EQU 1 (
		set PER=AM
		set ASSIGNNAME=AM Peak Period
		set HWY_NET=HWY_NET_3.net
		set NETNAME=AM Peak Period 6:00 AM to 10:00 AM
		set CAPFAC=3.75
		)
	IF %%I EQU 2 (
		set PER=MD
		set ASSIGNNAME=Mid Day Peak Period
		set HWY_NET=HWY_NET_4.net
		set NETNAME=Mid Day Period 10:00 AM to 3:00 PM
		set CAPFAC=4.48
		)
	IF %%I EQU 3 (
		set PER=PM
		set ASSIGNNAME=PM Peak Period
		set HWY_NET=HWY_NET_6.net
		set NETNAME=PM Peak Period 3:00 PM to 7:00 PM
		set CAPFAC=3.9
		)
	IF %%I EQU 4 (
		set PER=NT
		set ASSIGNNAME=Night
		set HWY_NET=HWY_NET_1.net
		set NETNAME=AM Peak Period 7:00 PM to 6:00 AM
		set CAPFAC=4.65
		)


	runtpp %SCRIPT_PATH%\HAMAT00A.s
	runtpp %SCRIPT_PATH%\HAHWY00A.s
	runtpp %SCRIPT_PATH%\HAMAT00C.s
	)

runtpp %SCRIPT_PATH%\HAPIL00B.s

:: HWY Assignment Post-Processor
runtpp %SCRIPT_PATH%\CANET00A.s
runtpp %SCRIPT_PATH%\CANET00B.s
runtpp %SCRIPT_PATH%\CAMAT00As.

:endComment

:: TRANSIT scripts
runtpp %SCRIPT_PATH%\TSNET00A.s
runtpp %SCRIPT_PATH%\TSNET00B.s
runtpp %SCRIPT_PATH%\TSPIL00A.s
runtpp %SCRIPT_PATH%\TSNET00C.s
runtpp %SCRIPT_PATH%\TSPTR00D.s
runtpp %SCRIPT_PATH%\TSPTR00F.s
runtpp %SCRIPT_PATH%\TSPTR00H.s
runtpp %SCRIPT_PATH%\TSPIL00C.s
runtpp %SCRIPT_PATH%\TSPTR00A.s
runtpp %SCRIPT_PATH%\TSPTR00C.s
runtpp %SCRIPT_PATH%\TSMAT00A.s
runtpp %SCRIPT_PATH%\TSMAT00C.s
runtpp %SCRIPT_PATH%\TSPIL00B.s

runtpp %SCRIPT_PATH%\summary_outputs.s
