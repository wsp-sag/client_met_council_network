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

::%beginComment%
:: The network comes as a fixed width file. @Sijia Wang will update the field 
:: widths and column names as necessary and will update that script when 
:: releasing network updates. This step moves that script into the main script 
:: folder so that it is executed in the correct place.
COPY %complete_network_script_input_path% %complete_network_script_output_path%

:: Make Networks
::%beginComment%
runtpp %SCRIPT_PATH%\make_complete_network_from_fixed_width_file.s
::runtpp %SCRIPT_PATH%\set_farezone_values.s
runtpp %SCRIPT_PATH%\make_highway_network_from_file.s
runtpp %SCRIPT_PATH%\make_bike_network_from_file.s
runtpp %SCRIPT_PATH%\make_walk_network_from_file.s
runtpp %SCRIPT_PATH%\FullMakeNetwork15.s 

:: HIGHWAY
::%beginComment%
runtpp %SCRIPT_PATH%\BNNET00B.s
runtpp %SCRIPT_PATH%\HNNET00B.s
::endComment

::endComment
:: This script handles TOD assignment. Batch files require a single character
:: variable.
::%exitRun%
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

runtpp %SCRIPT_PATH%\TSNET00B.s
::endComment

:: Calculate transit speeds for each period
:: Build walk access, transfer access, and drive access connectors for each period
:: Skim walk transit and drive transit
FOR /L %%I IN (1, 1, 1) DO (

	SET TOD=%%I

	IF %%I EQU 1 (
        SET TPER=PK
        )
	IF %%I EQU 2 (
        SET TPER=OP
        )

	runtpp %SCRIPT_PATH%\TSNET00C.s
    runtpp %SCRIPT_PATH%\TSPTR00D.s
    runtpp %SCRIPT_PATH%\TSPTR00F.s
    runtpp %SCRIPT_PATH%\TSPTR00H.s
    runtpp %SCRIPT_PATH%\TSPIL00C.s
    runtpp %SCRIPT_PATH%\TSPTR00A.s
    runtpp %SCRIPT_PATH%\TSPTR00C.s
    runtpp %SCRIPT_PATH%\TSMAT00A.s
    runtpp %SCRIPT_PATH%\TSMAT00C.s
)

::endComment

SET ITER=4
SET PREV_ITER=3

::%beginComment%
:: HIGHWAY
runtpp %SCRIPT_PATH%\HAPIL00D.s
runtpp %SCRIPT_PATH%\HAMAT00E.s
runtpp %SCRIPT_PATH%\HAMAT00G.s
runtpp %SCRIPT_PATH%\HAMAT00I.s
runtpp %SCRIPT_PATH%\HAMAT00K.s
::endComment

::%beginComment%
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
    runtpp %SCRIPT_PATH%\HAHWY00A.s
    runtpp %SCRIPT_PATH%\HAMAT00C.s
)

runtpp %SCRIPT_PATH%\HAPIL00B.s

::endComment
:: TRANSIT skimming
::%beginComment%
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
    :: Build period walk access connectors
::    runtpp %SCRIPT_PATH%\TSPTR00N.s
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
    
)
::endComment
    
%exitRun%

::endComment
:endOfFile