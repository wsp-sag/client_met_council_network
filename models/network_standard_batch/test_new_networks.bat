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
CALL .\test_new_networks_parameters.bat

goto trnskims

COPY %complete_network_script_input_path% %complete_network_script_output_path%

:: Make Networks
:nets
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

:: Roadway Skims
:road_skims
runtpp %SCRIPT_PATH%\BNNET00B.s
if ERRORLEVEL 2 goto done

runtpp %SCRIPT_PATH%\HNNET00B.s
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

runtpp %SCRIPT_PATH%\FFHWY00A.s
if ERRORLEVEL 2 goto done

runtpp %SCRIPT_PATH%\FFPIL00A.s
if ERRORLEVEL 2 goto done

runtpp %SCRIPT_PATH%\TSNET00A.s
if ERRORLEVEL 2 goto done

runtpp %SCRIPT_PATH%\TSNET00B.s
if ERRORLEVEL 2 goto done

runtpp %SCRIPT_PATH%\warmstart_transit_walk_links.s
if ERRORLEVEL 2 goto done

:: Transit Skims
:trnskims
FOR /L %%I IN (1, 1, 1) DO (

	SET TOD=%%I

	IF %%I EQU 1 (
        SET TPER=PK
        )
	IF %%I EQU 2 (
        SET TPER=OP
        )

	runtpp %SCRIPT_PATH%\TSNET00C.s
	if ERRORLEVEL 2 goto done
	
    runtpp %SCRIPT_PATH%\TSPTR00D.s
	if ERRORLEVEL 2 goto done
	
    runtpp %SCRIPT_PATH%\TSPTR00F.s
	if ERRORLEVEL 2 goto done
	
    runtpp %SCRIPT_PATH%\TSPTR00H.s
	if ERRORLEVEL 2 goto done
	
    runtpp %SCRIPT_PATH%\TSPIL00C.s
	if ERRORLEVEL 2 goto done
	
    runtpp %SCRIPT_PATH%\TSPTR00A.s
	if ERRORLEVEL 2 goto done
	
    runtpp %SCRIPT_PATH%\TSPTR00C.s
	if ERRORLEVEL 2 goto done
	
    runtpp %SCRIPT_PATH%\TSMAT00A.s
	if ERRORLEVEL 2 goto done
	
    runtpp %SCRIPT_PATH%\TSMAT00C.s
	if ERRORLEVEL 2 goto done
)

SET ITER=4
SET PREV_ITER=3

:: HIGHWAY
:highway
runtpp %SCRIPT_PATH%\HAPIL00D.s
if ERRORLEVEL 2 goto done

runtpp %SCRIPT_PATH%\HAMAT00E.s
if ERRORLEVEL 2 goto done

runtpp %SCRIPT_PATH%\HAMAT00G.s
if ERRORLEVEL 2 goto done

runtpp %SCRIPT_PATH%\HAMAT00I.s
if ERRORLEVEL 2 goto done

runtpp %SCRIPT_PATH%\HAMAT00K.s
if ERRORLEVEL 2 goto done

FOR /L %%I IN (1, 4, 1) DO (

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
	
    runtpp %SCRIPT_PATH%\HAHWY00A.s
	if ERRORLEVEL 2 goto done
	
    runtpp %SCRIPT_PATH%\HAMAT00C.s
	if ERRORLEVEL 2 goto done
)

runtpp %SCRIPT_PATH%\HAPIL00B.s
if ERRORLEVEL 2 goto done

:: Rebuild transit network with walk links
runtpp %SCRIPT_PATH%\transit_walk_links.s
if ERRORLEVEL 2 goto done

:: TRANSIT skimming
:: Loop over peak/off-peak
FOR /L %%I IN (1,1,1) DO (
    SET TOD=%%I
    IF %%I EQU 1 (
        SET TPER=PK
        SET ASSIGNNAME=Peak Period
        SET PER=AM
    )
    IF %%I EQU 2 (
        SET TPER=OP
        SET ASSIGNNAME=OffPeak Period
        SET PER=MD
    )
    
    :: Calculate transit speeds for period
    runtpp %SCRIPT_PATH%\TSNET00F.s
	if ERRORLEVEL 2 goto done
	
    :: Build period walk access connectors
    runtpp %SCRIPT_PATH%\TSPTR00N.s
	if ERRORLEVEL 2 goto done
    
)

goto done

::    :: Build period transfer access connectors
::    runtpp %SCRIPT_PATH%\TSPTR00S.s
::    :: Build period drive access connectors
::    runtpp %SCRIPT_PATH%\TSPTR00U.s
::        
::    :: Copy temp files to non-transit leg files
::    COPY %SCENARIO_DIR%\XIT_WKACC_NTL_%ITER%_!TPER!.tmp+%LOOKUP_DIR%\WalkOverrides.txt %SCENARIO_DIR%\XIT_WKACC_NTL_%ITER%_!TPER!.ntl
::    COPY %SCENARIO_DIR%\XIT_XFER_NTL_%ITER%_!TPER!.tmp + %LOOKUP_DIR%\TransferOverrides.txt %SCENARIO_DIR%\XIT_XFER_NTL_%ITER%_!TPER!.ntl
::    COPY %SCENARIO_DIR%\XIT_DRACC_NTL_%ITER%_!TPER!.tmp + %LOOKUP_DIR%\DriveOverrides.txt %SCENARIO_DIR%\XIT_DRACC_NTL_%ITER%_!TPER!.ntl
::
::    :: Walk transit skim step 1
::    runtpp %SCRIPT_PATH%\TSPTR00J.s
::    :: Drive transit skim step 1
::    runtpp %SCRIPT_PATH%\TSPTR00L.s
::    :: Walk transit skim step 2
::    runtpp %SCRIPT_PATH%\TSMAT00E.s
::    :: Drive transit skim step 2
::    runtpp %SCRIPT_PATH%\TSMAT00G.s
::endComment
:done