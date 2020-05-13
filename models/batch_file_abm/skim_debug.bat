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

:: The network comes as a fixed width file. @Sijia Wang will update the field 
:: widths and column names as necessary and will update that script when 
:: releasing network updates. This step moves that script into the main script 
:: folder so that it is executed in the correct place.

SET ITER=4
SET PER=AM
SET ASSIGNNAME=AM Peak Period
SET HWY_NET=HWY_NET_3.net
SET NETNAME=AM Peak Period 6:00 AM to 10:00 AM
SET CAPFAC=3.75

runtpp %SCRIPT_PATH%\simple_skim.s
 
%exitRun%
::endComment
:endOfFile