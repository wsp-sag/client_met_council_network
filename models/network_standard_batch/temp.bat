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

runtpp %SCRIPT_PATH%\make_assignable.s
if ERRORLEVEL 2 goto done
