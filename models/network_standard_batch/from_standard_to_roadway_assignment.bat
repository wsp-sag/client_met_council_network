::~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
:: from_standard_to_transit_assignment.bat
::
:: MS-DOS batch file to go from the output from Network Wrangler to transit
:: transit assignment.
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
CALL .\test_new_networks_parameters.bat

COPY %complete_network_script_input_path% %complete_network_script_output_path%

SET ITER=4

:: ----------------------------------------------------------------------------
::
:: Step 2:  Make Roadway Networks
::
:: ----------------------------------------------------------------------------
:rnet
runtpp %SCRIPT_PATH%\make_complete_network_from_fixed_width_file.s
if ERRORLEVEL 2 goto done

runtpp %SCRIPT_PATH%\make_highway_network_from_file.s
if ERRORLEVEL 2 goto done

runtpp %SCRIPT_PATH%\make_bike_network_from_file.s
if ERRORLEVEL 2 goto done

runtpp %SCRIPT_PATH%\make_walk_network_from_file.s
if ERRORLEVEL 2 goto done

runtpp %SCRIPT_PATH%\FullMakeNetwork15.s 
if ERRORLEVEL 2 goto done

:: ----------------------------------------------------------------------------
::
:: Step 3:  Roadway Skimming & Assignment
::
:: ----------------------------------------------------------------------------
:road
runtpp %SCRIPT_PATH%\BNNET00B.s
if ERRORLEVEL 2 goto done

runtpp %SCRIPT_PATH%\HNNET00B.s
if ERRORLEVEL 2 goto done

runtpp %SCRIPT_PATH%\make_assignable.s
if ERRORLEVEL 2 goto done


for /L %%I IN (1, 1, 6) DO (
	SET TOD=%%I

	IF %%I EQU 1 (SET NETNAME=Overnight 7:00 PM to 5:00 AM)
	IF %%I EQU 2 (SET NETNAME=Reverse Lane Change Over 5:00 AM to 6:00 AM  and 1:00 PM to 2:00 PM)
	IF %%I EQU 3 (SET NETNAME=AM Peak Period 6:00 AM to 10:00 AM)
	IF %%I EQU 4 (SET NETNAME=Mid Day Period 10:00 AM to 1:00 PM)
	IF %%I EQU 5 (SET NETNAME=Pre PM Peak Period 2:00 PM to 3:00 PM)
	IF %%I EQU 6 (SET NETNAME=PM Peak Period 3:00 PM to 7:00 PM)

	runtpp %SCRIPT_PATH%\HNNET00C.s
	if ERRORLEVEL 2 goto done
)

runtpp %SCRIPT_PATH%\HAMAT00E.s
if ERRORLEVEL 2 goto done

runtpp %SCRIPT_PATH%\HAMAT00G.s
if ERRORLEVEL 2 goto done

runtpp %SCRIPT_PATH%\HAMAT00I.s
if ERRORLEVEL 2 goto done

runtpp %SCRIPT_PATH%\HAMAT00K.s
if ERRORLEVEL 2 goto done

:temp
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
	if ERRORLEVEL 2 goto done
	
    runtpp %SCRIPT_PATH%\test_roadway.s
	if ERRORLEVEL 2 goto done
	
    runtpp %SCRIPT_PATH%\HAMAT00C.s
	if ERRORLEVEL 2 goto done
)

:done