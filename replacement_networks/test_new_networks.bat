::~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
:: run_initial_auto_skim.bat
::
:: MS-DOS batch file to execute the Auto Skim step of the Met Council travel
:: model.
::
::
::~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@ECHO off
SetLocal EnableDelayedExpansion
:: ----------------------------------------------------------------------------
::
:: Step 1:  Set the necessary path variables
::
:: ----------------------------------------------------------------------------

:: The location of the runtpp executable from Citilabs - 64bit first
SET TPP_PATH=C:\Program Files\Citilabs\CubeVoyager;C:\Program Files (x86)\Citilabs\CubeVoyager

:: The location of python
SET python_PATH=C:\python27\ArcGIS10.6

:: Add these variables to the PATH environment variable, moving the current path to the back
SET OLD_PATH=%PATH%
SET PATH=%RUNTIME%;%TPP_PATH%;%python_PATH%;%OLD_PATH%

SET NETWORK_FOLDER=network_06242019
SET SCRIPT_PATH=replacement_scripts
SET TRIP_DIR=original_trip_tables
SET SCENARIO_DIR=network_test_outputs
SET COMPARISON_DIR=comparisons
SET LOOKUP_DIR=lookup_files
SET INPUT_DIR=inputs

:: Set zones
SET zone_attribs=%INPUT_DIR%\Zones_2015.dbf
COPY %zone_attribs% %SCENARIO_DIR%\zones.dbf

SET LINK_PATH=%NETWORK_FOLDER%/all_link.dbf
SET NODE_PATH=%NETWORK_FOLDER%/all_node.dbf

:: Set transit
SET xit_lines=%NETWORK_FOLDER%/transit.lin
SET xit_system=%LOOKUP_DIR%/PT_SYSTEM_2010.PTS
SET xit_faremat=%LOOKUP_DIR%/FAREMAT_2010.txt
SET xit_fare=%LOOKUP_DIR%/PT_FARE_2010.FAR
SET xit_pnrnodes=%NETWORK_FOLDER%/GENERATE_PNR_ACCESS.s
SET xit_fac_year=2010

SET max_threads=16


SET hwy_assignIters=500
SET hwy_HOV2OCC=2
SET hwy_HOV3OCC=3.2
SET zones=3061
SET int_zones=3030
SET ext_zones=31
SET LU_will2pay=%LOOKUP_DIR%/Will2Pay_oneCurve.txt
SET hwy_TrkFac=2
SET hwy_TollSetting=1

SET T_PRIORITY_PATH=%LOOKUP_DIR%/T_Priority.dbf
SET T_MANTIME_PATH=%LOOKUP_DIR%/T_MANTIME.dbf
SET T_DISTANCE_PATH=%LOOKUP_DIR%/Distances.dbf

:: Make Networks
::%beginComment%
runtpp %SCRIPT_PATH%\make_complete_network_from_file.s
runtpp %SCRIPT_PATH%\make_highway_network_from_file.s
runtpp %SCRIPT_PATH%\make_bike_network_from_file.s
runtpp %SCRIPT_PATH%\make_walk_network_from_file.s
runtpp %SCRIPT_PATH%\FullMakeNetwork15.s
::endComment

:: HIGHWAY
:: Set highway network
SET iHwyNet=%SCENARIO_DIR%/highway_2015.net

SET LU_AlphaBeta=lookup_files/AlphaBetaLookup.txt
SET LU_capacity=lookup_files/SpeedLookup85.txt
SET LU_speed=lookup_files/CapacityLookup.txt

%beginComment%
runtpp %SCRIPT_PATH%\BNNET00B.s
runtpp %SCRIPT_PATH%\HNNET00B.s
:: This script handles TOD assignment. Batch files require a single character
:: variable.

for /L %%I IN (1, 1, 6) DO (
	SET TOD=%%I

	IF %%I EQU 1 (SET NETNAME=Overnight 7:00 PM to 5:00 AM)
	IF %%I EQU 2 (SET NETNAME=Reverse Lane Change Over 5:00 AM to 6:00 AM  and 1:00 PM to 2:00 PM)
	IF %%I EQU 3 (SET NETNAME=AM Peak Period 6:00 AM to 10:00 AM)
	IF %%I EQU 4 (SET NETNAME=Mid Day Period 10:00 AM to 1:00 PM)
	IF %%I EQU 5 (SET NETNAME=Pre PM Peak Period 2:00 PM to 3:00 PM)
	IF %%I EQU 6 (SET NETNAME=PM Peak Period 3:00 PM to 7:00 PM)

	runtpp %SCRIPT_PATH%\HNNET00C.s
)

runtpp %SCRIPT_PATH%\FFHWY00A.s
runtpp %SCRIPT_PATH%\FFPIL00A.s
::endComment

::%beginComment%
:: HIGHWAY

runtpp %SCRIPT_PATH%\HAPIL00D.s
runtpp %SCRIPT_PATH%\HAMAT00E.s
runtpp %SCRIPT_PATH%\HAMAT00G.s
runtpp %SCRIPT_PATH%\HAMAT00I.s
runtpp %SCRIPT_PATH%\HAMAT00K.s

FOR /L %%I IN (1, 1, 4) DO (

	SET TOD=%%I

	IF %%I EQU 1 (
		SET PER=AM
		SET ASSIGNNAME=AM Peak Period
		SET HWY_NET=HWY_NET_3.net
		SET NETNAME=AM Peak Period 6:00 AM to 10:00 AM
		SET CAPFAC=3.75
		)
	IF %%I EQU 2 (
		SET PER=MD
		SET ASSIGNNAME=Mid Day Peak Period
		SET HWY_NET=HWY_NET_4.net
		SET NETNAME=Mid Day Period 10:00 AM to 3:00 PM
		SET CAPFAC=4.48
		)
	IF %%I EQU 3 (
		SET PER=PM
		SET ASSIGNNAME=PM Peak Period
		SET HWY_NET=HWY_NET_6.net
		SET NETNAME=PM Peak Period 3:00 PM to 7:00 PM
		SET CAPFAC=3.9
		)
	IF %%I EQU 4 (
		SET PER=NT
		SET ASSIGNNAME=Night
		SET HWY_NET=HWY_NET_1.net
		SET NETNAME=AM Peak Period 7:00 PM to 6:00 AM
		SET CAPFAC=4.65
		)


	runtpp %SCRIPT_PATH%\HAMAT00A.s
	runtpp %SCRIPT_PATH%\HAHWY00A.s
	runtpp %SCRIPT_PATH%\HAMAT00C.s
	)

runtpp %SCRIPT_PATH%\HAPIL00B.s

:: HWY Assignment Post-Processor
runtpp %SCRIPT_PATH%\CANET00A.s
runtpp %SCRIPT_PATH%\CANET00B.s
runtpp %SCRIPT_PATH%\CAMAT00A.s
:endComment
