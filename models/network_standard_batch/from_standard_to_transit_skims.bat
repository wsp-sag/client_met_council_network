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
:: Step 4:  Transit Skims
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
	
	runtpp %SCRIPT_PATH%\skims_to_omx.s
	if ERRORLEVEL 2 goto done
)
:done