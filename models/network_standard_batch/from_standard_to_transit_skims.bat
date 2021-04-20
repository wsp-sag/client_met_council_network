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

goto tnet

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
:: Step 3:  Make Transit Networks
::
:: ----------------------------------------------------------------------------
:tnet
runtpp %SCRIPT_PATH%\TSNET00A.s
if ERRORLEVEL 2 goto done

runtpp %SCRIPT_PATH%\TSNET00B.s
if ERRORLEVEL 2 goto done

runtpp %SCRIPT_PATH%\warmstart_transit_walk_links.s
if ERRORLEVEL 2 goto done

:: ----------------------------------------------------------------------------
::
:: Step 4: Warm Start Transit Skims
::
:: ----------------------------------------------------------------------------

:trnskims
FOR /L %%I IN (1, 2, 1) DO (

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

:: ----------------------------------------------------------------------------
::
:: Step 5: Transit Skims
::
:: ----------------------------------------------------------------------------
SET ITER=4

FOR /L %%I IN (1, 4, 1) DO (

	SET TOD=%%I

	IF %%I EQU 1 (
		SET PER=AM
		runtpp %SCRIPT_PATH%\transit_walk_links.s
		if ERRORLEVEL 2 goto done
		)
	IF %%I EQU 2 (
		SET PER=MD
		runtpp %SCRIPT_PATH%\transit_walk_links.s
		if ERRORLEVEL 2 goto done
		)
	IF %%I EQU 3 (
		SET PER=PM
		runtpp %SCRIPT_PATH%\transit_walk_links.s
		if ERRORLEVEL 2 goto done
		)
	IF %%I EQU 4 (
		SET PER=NT
		runtpp %SCRIPT_PATH%\transit_walk_links.s
		if ERRORLEVEL 2 goto done
		)
	)

:: Loop over peak/off-peak
FOR /L %%I IN (1,2,1) DO (
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
	
	:: Build period transfer access connectors
    runtpp %SCRIPT_PATH%\TSPTR00S.s
	if ERRORLEVEL 2 goto done
	    
    :: Build period drive access connectors
    runtpp %SCRIPT_PATH%\TSPTR00U.s
	if ERRORLEVEL 2 goto done
        
    :: Copy temp files to non-transit leg files
    COPY %SCENARIO_DIR%\XIT_WKACC_NTL_%ITER%_!TPER!.tmp+%LOOKUP_DIR%\WalkOverrides.txt %SCENARIO_DIR%\XIT_WKACC_NTL_%ITER%_!TPER!.ntl
    COPY %SCENARIO_DIR%\XIT_XFER_NTL_%ITER%_!TPER!.tmp + %LOOKUP_DIR%\TransferOverrides.txt %SCENARIO_DIR%\XIT_XFER_NTL_%ITER%_!TPER!.ntl
    COPY %SCENARIO_DIR%\XIT_DRACC_NTL_%ITER%_!TPER!.tmp + %LOOKUP_DIR%\DriveOverrides.txt %SCENARIO_DIR%\XIT_DRACC_NTL_%ITER%_!TPER!.ntl

    :: Walk transit skim step 1
    runtpp %SCRIPT_PATH%\TSPTR00J.s
	if ERRORLEVEL 2 goto done
	
    :: Drive transit skim step 1
    runtpp %SCRIPT_PATH%\TSPTR00L.s
	if ERRORLEVEL 2 goto done
	
    :: Walk transit skim step 2
    runtpp %SCRIPT_PATH%\TSMAT00E.s
	if ERRORLEVEL 2 goto done

    :: Drive transit skim step 2
    runtpp %SCRIPT_PATH%\TSMAT00G.s
	if ERRORLEVEL 2 goto done
	
	runtpp %SCRIPT_PATH%\skims_to_omx.s
	if ERRORLEVEL 2 goto done
    
)


:done