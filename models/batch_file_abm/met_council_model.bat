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
SET "beginComment=goto :endComment"
SET "returnToHead=goto :head"
SET "exitRun=goto :endOfFile"

:: Parameters are found in set_parameters.bat
:: Future work could move this to a folder and name parameter files after model run
CALL .\set_parameters.bat

:: ----------------------------------------------------------------------------
::
:: Step 2:  Networks and initial skims 
::
:: ----------------------------------------------------------------------------
:: Generate zonal data for model run
COPY "%zone_attribs%" "%SCENARIO_DIR%\zones.dbf"

:: Make Networks
:: Filter the all_link and all_node shape files to create separate 
:: highway, bike, and walk networks.
%beginComment%
runtpp %SCRIPT_PATH%\make_complete_network_from_file.s
IF ERRORLEVEL 2 %exitRun%
runtpp %SCRIPT_PATH%\make_highway_network_from_file.s
IF ERRORLEVEL 2 %exitRun%
runtpp %SCRIPT_PATH%\make_bike_network_from_file.s
IF ERRORLEVEL 2 %exitRun%
runtpp %SCRIPT_PATH%\make_walk_network_from_file.s
IF ERRORLEVEL 2 %exitRun%
:: FullMakeNetwork15.s uses hard codes that should be adjusted to match model years.
runtpp %SCRIPT_PATH%\FullMakeNetwork15.s
IF ERRORLEVEL 2 %exitRun%
:endComment

:: INITIAL NETWORKS AND INITIAL SKIMS
:: NON-MOTORIZED
:: Skim bike and walk networks
%beginComment%
runtpp %SCRIPT_PATH%\NMNET00A.s
IF ERRORLEVEL 2 %exitRun%
runtpp %SCRIPT_PATH%\NMHWY00A.s
IF ERRORLEVEL 2 %exitRun%
runtpp %SCRIPT_PATH%\NMHWY00B.s
IF ERRORLEVEL 2 %exitRun%
runtpp %SCRIPT_PATH%\NMMAT00A.s
IF ERRORLEVEL 2 %exitRun%
:endComment

:: HIGHWAY
:: No current option to copy skims as a warm start, could be added.
%beginComment%
:: Export highway network from temp file (candidate for streamlining)
runtpp %SCRIPT_PATH%\BNNET00B.s
IF ERRORLEVEL 2 %exitRun%
:: Set drive link speeds capacities, alpha/beta parameters
runtpp %SCRIPT_PATH%\HNNET00B.s
IF ERRORLEVEL 2 %exitRun%
:: Set managed lanes (comments cannot go inside for loops)
FOR /L %%I IN (1, 1, 6) DO (
	SET TOD=%%I

	IF %%I EQU 1 (SET NETNAME=Overnight 7:00 PM to 5:00 AM)
	IF %%I EQU 2 (SET NETNAME=Reverse Lane Change Over 5:00 AM to 6:00 AM  and 1:00 PM to 2:00 PM)
	IF %%I EQU 3 (SET NETNAME=AM Peak Period 6:00 AM to 10:00 AM)
	IF %%I EQU 4 (SET NETNAME=Mid Day Period 10:00 AM to 1:00 PM)
	IF %%I EQU 5 (SET NETNAME=Pre PM Peak Period 2:00 PM to 3:00 PM)
	IF %%I EQU 6 (SET NETNAME=PM Peak Period 3:00 PM to 7:00 PM)

	runtpp %SCRIPT_PATH%\HNNET00C.s
    :: Need to test how exitRun works inside loop
    IF ERRORLEVEL 2 %exitRun%
)

::: Skim free flow network
runtpp %SCRIPT_PATH%\FFHWY00A.s
IF ERRORLEVEL 2 %exitRun%
:: Copy skims to all time periods
runtpp %SCRIPT_PATH%\FFPIL00A.s
IF ERRORLEVEL 2 %exitRun%
::endComment

:: TRANSIT
:: No current option to copy skims as a warm start, could be added.
::%beginComment%
:: extract link and node dbfs, set rail zone nodes
runtpp %SCRIPT_PATH%\TSNET00A.s
IF ERRORLEVEL 2 %exitRun%
runtpp %SCRIPT_PATH%\TSNET00B.s
IF ERRORLEVEL 2 %exitRun%

:: Calculate transit speeds for each period
:: Build walk access, transfer access, and drive access connectors for each period
:: Skim walk transit and drive transit
FOR /L %%I IN (1, 1, 2) DO (

	SET TOD=%%I

	IF %%I EQU 1 (
        SET TPER=PK
        )
	IF %%I EQU 2 (
        SET TPER=OP
        )

	runtpp %SCRIPT_PATH%\TSNET00C.s
    IF ERRORLEVEL 2 %exitRun%
    runtpp %SCRIPT_PATH%\TSPTR00D.s
    IF ERRORLEVEL 2 %exitRun%
	runtpp %SCRIPT_PATH%\TSPTR00F.s
    IF ERRORLEVEL 2 %exitRun%
	runtpp %SCRIPT_PATH%\TSPTR00H.s
    IF ERRORLEVEL 2 %exitRun%
	runtpp %SCRIPT_PATH%\TSPIL00C.s
    IF ERRORLEVEL 2 %exitRun%
	runtpp %SCRIPT_PATH%\TSPTR00A.s
    IF ERRORLEVEL 2 %exitRun%
	runtpp %SCRIPT_PATH%\TSPTR00C.s
    IF ERRORLEVEL 2 %exitRun%
	runtpp %SCRIPT_PATH%\TSMAT00A.s
    IF ERRORLEVEL 2 %exitRun%
	runtpp %SCRIPT_PATH%\TSMAT00C.s
    IF ERRORLEVEL 2 %exitRun%
)
::endComment

:: ----------------------------------------------------------------------------
::
:: Step 3:  Trucks and Special Generators 
::
:: ----------------------------------------------------------------------------

:: INITIALIZE TRUCK AND SPECIAL GENERATOR
::%beginComment%
:: Quick response freight manual routine
runtpp %SCRIPT_PATH%\TSGEN00A.s
IF ERRORLEVEL 2 %exitRun%
:: External auto allocation and mode choice
runtpp %SCRIPT_PATH%\TSMAT00H.s
IF ERRORLEVEL 2 %exitRun%
:: Build distribution matrix for auto EE IPF
runtpp %SCRIPT_PATH%\TSMAT00I.s
IF ERRORLEVEL 2 %exitRun%
:: Fratar station targets using distribution from survey
runtpp %SCRIPT_PATH%\TSFRA00A.s
IF ERRORLEVEL 2 %exitRun%
:: Generate airport trips
runtpp %SCRIPT_PATH%\TSMAT00K.s
IF ERRORLEVEL 2 %exitRun%
:: Create special generator matrix
runtpp %SCRIPT_PATH%\TSMAT00L.s
IF ERRORLEVEL 2 %exitRun%
:: Fratar EE trucks from FAF
runtpp %SCRIPT_PATH%\TSFRA00B.s
IF ERRORLEVEL 2 %exitRun%
:: Split freight into truck types
runtpp %SCRIPT_PATH%\TSMAT00M.s
IF ERRORLEVEL 2 %exitRun%
::endComment

:: ----------------------------------------------------------------------------
::
:: Step 3:  Start the Model Feedback Loop
::
:: ----------------------------------------------------------------------------

:: MODEL LOOP
:: Iteration loop returns to HERE
:head
:: ----------------------------------------------------------------------------
::
:: Step 3a:  Create Exogenous Variables 
::
:: ----------------------------------------------------------------------------

:: CREATE EXOGENOUS VARIABLES
::%beginComment%
COPY %SCENARIO_DIR%\zones.dbf %SCENARIO_DIR%\zones_%PREV_ITER%.dbf
IF ERRORLEVEL 2 %exitRun%
:: Highway Accessibility
runtpp %SCRIPT_PATH%\EVMAT00A.s
IF ERRORLEVEL 2 %exitRun%
:: Transit Accessibility
runtpp %SCRIPT_PATH%\EVMAT00B.s
IF ERRORLEVEL 2 %exitRun%
:: Distance to external stations
runtpp %SCRIPT_PATH%\EVMAT00C.s
IF ERRORLEVEL 2 %exitRun%
:: School TAZs
runtpp %SCRIPT_PATH%\EVMAT00D.s
IF ERRORLEVEL 2 %exitRun%
:: University enrollment
runtpp %SCRIPT_PATH%\EVMAT00E.s
IF ERRORLEVEL 2 %exitRun%
:: Update zonal database
runtpp %SCRIPT_PATH%\EVMAT00F.s
IF ERRORLEVEL 2 %exitRun%
::endComment

:: ----------------------------------------------------------------------------
::
:: Step 3b: Run TourCast 
::
:: ----------------------------------------------------------------------------
::%beginComment%
python %TOURCAST_DIR%\make_tour_cast_input_file.py %TOURCAST_DIR% %SCENARIO_DIR% %ITER% %households% %persons%
IF ERRORLEVEL 1 %exitRun%
python %TOURCAST_DIR%\script\update_tourcast_json_inputs.py %TOURCAST_DIR%\script\
IF ERRORLEVEL 1 %exitRun%
::endComment

::%beginComment%
:: Run TourCast
CALL .\TourCastRun.bat
::endComment

:: ----------------------------------------------------------------------------
::
:: Step 3c: Freight Externals and Special Generator Distribution
::
:: ----------------------------------------------------------------------------
::%beginComment%
:: FREIGHT
:: Create weighted skim times
runtpp %SCRIPT_PATH%\FTMAT00A.s
IF ERRORLEVEL 2 %exitRun%
:: Truck gravity model
runtpp %SCRIPT_PATH%\FTTRD00A.s
IF ERRORLEVEL 2 %exitRun%
:: Time period splits
runtpp %SCRIPT_PATH%\FTMAT00B.s
IF ERRORLEVEL 2 %exitRun%
::endComment

:: EXTERNAL AUTOS
::%beginComment%
:: Auto EI/IE destination choice
runtpp %SCRIPT_PATH%\EEMAT00A.s
IF ERRORLEVEL 2 %exitRun%
:: Combine EI/IE trips with tranpose and EE
runtpp %SCRIPT_PATH%\EEMAT00B.s
IF ERRORLEVEL 2 %exitRun%

:: Loop through time periods, sum trips from each time period
for /L %%I IN (1, 1, 11) DO (
    SET TOD=%%I
    
    IF %%I EQU 1 (SET PER=AM1)
    IF %%I EQU 2 (SET PER=AM2)
    IF %%I EQU 3 (SET PER=AM3)
    IF %%I EQU 4 (SET PER=AM4)  
    IF %%I EQU 5 (SET PER=MD)
    IF %%I EQU 6 (SET PER=PM1)
    IF %%I EQU 7 (SET PER=PM2)
    IF %%I EQU 8 (SET PER=PM3)
    IF %%I EQU 9 (SET PER=PM4)
    IF %%I EQU 10 (SET PER=EV)
    IF %%I EQU 11 (SET PER=ON)
    
    runtpp %SCRIPT_PATH%\EEMAT00D.s
    IF ERRORLEVEL 2 %exitRun%
)
:: Split trips by TOD
runtpp %SCRIPT_PATH%\EEMAT00E.s
IF ERRORLEVEL 2 %exitRun%
::endComment

::%beginComment%
:: SPECIAL GENERATORS
:: Data from AirportModECHOiceParams.txt
for /L %%I IN (1, 1, 11) DO (
    SET TOD=%%I
    
    IF %%I EQU 1 (
        SET PER=AM1
        SET HPER=AM
        SET TPER=PK
    )
    IF %%I EQU 2 (
        SET PER=AM2
        SET HPER=AM
        SET TPER=PK
    ) 
    IF %%I EQU 3 (
        SET PER=AM3
        SET HPER=AM
        SET TPER=PK
    ) 
    IF %%I EQU 4 (
        SET PER=AM4
        SET HPER=AM
        SET TPER=PK
    )   
    IF %%I EQU 5 (
        SET PER=MD 
        SET HPER=MD
        SET TPER=OP
    )
    IF %%I EQU 6 (
        SET PER=PM1
        SET HPER=PM
        SET TPER=PK
    )  
    IF %%I EQU 7 (
        SET PER=PM2
        SET HPER=PM
        SET TPER=PK
    ) 
    IF %%I EQU 8 (
        SET PER=PM3
        SET HPER=PM
        SET TPER=PK
    ) 
    IF %%I EQU 9 (
        SET PER=PM4
        SET HPER=PM
        SET TPER=PK
    )
    IF %%I EQU 10 (
        SET PER=EV
        SET HPER=NT
        SET TPER=OP
    ) 
    IF %%I EQU 11 (
        SET PER=ON
        SET HPER=NT
        SET TPER=OP
    )
    
    :: Airport mode choice
    :: Seeing errors from SGMAT00A.s - should we add a zero out option to prevent divide by 0 errors?
    runtpp %SCRIPT_PATH%\SGMAT00A.s
    IF ERRORLEVEL 2 %exitRun%
    :: Return trips from airport
    runtpp %SCRIPT_PATH%\SGMAT00B.s
    IF ERRORLEVEL 2 %exitRun%
)
::endComment

::%beginComment%
:: ----------------------------------------------------------------------------
::
:: Step 3d: Assignment and Skimming
::
:: ----------------------------------------------------------------------------
:: HIGHWAY skims
:: Start cube cluster
runtpp %SCRIPT_PATH%\HAPIL00D.s
IF ERRORLEVEL 2 %exitRun%
:: Aggregate trip tables for interim assignment
runtpp %SCRIPT_PATH%\HAMAT00E.s
IF ERRORLEVEL 2 %exitRun%
:: Aggregtate truck trip tables for interim assignment
runtpp %SCRIPT_PATH%\HAMAT00G.s
IF ERRORLEVEL 2 %exitRun%
:: Aggregtate IE/EI trip tables for interim assignment
runtpp %SCRIPT_PATH%\HAMAT00I.s
IF ERRORLEVEL 2 %exitRun%
:: Aggregate SPC trip tables for interim assignment
runtpp %SCRIPT_PATH%\HAMAT00K.s
IF ERRORLEVEL 2 %exitRun%

:: Loop over time of day
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

    :: Record stats and convert to vehicle trip tables
	runtpp %SCRIPT_PATH%\HAMAT00A.s
    IF ERRORLEVEL 2 %exitRun%
    :: Highway assignment
	runtpp %SCRIPT_PATH%\HAHWY00A.s
    IF ERRORLEVEL 2 %exitRun%
    :: Create highway skims
	runtpp %SCRIPT_PATH%\HAMAT00C.s
    IF ERRORLEVEL 2 %exitRun%
	)

:: End cube cluster
runtpp %SCRIPT_PATH%\HAPIL00B.s
IF ERRORLEVEL 2 %exitRun%

:: HWY Assignment Post-Processor
:: Combine convergence assignment networks
runtpp %SCRIPT_PATH%\CANET00A.s
IF ERRORLEVEL 2 %exitRun%
:: export link dbf
runtpp %SCRIPT_PATH%\CANET00B.s
IF ERRORLEVEL 2 %exitRun%
:: Export files to csv
runtpp %SCRIPT_PATH%\CAMAT00A.s
IF ERRORLEVEL 2 %exitRun%
::endComment

:: TRANSIT skimming
::%beginComment%
:: Loop over peak/off-peak
FOR /L %%I IN (1,1,2) DO (
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
    IF ERRORLEVEL 2 %exitRun%
    :: Build period walk access connectors
    runtpp %SCRIPT_PATH%\TSPTR00N.s
    IF ERRORLEVEL 2 %exitRun%
    :: Build period transfer access connectors
    runtpp %SCRIPT_PATH%\TSPTR00S.s
    IF ERRORLEVEL 2 %exitRun%
    :: Build period drive access connectors
    runtpp %SCRIPT_PATH%\TSPTR00U.s
    IF ERRORLEVEL 2 %exitRun%
    
    :: Copy temp files to non-transit leg files
    COPY %SCENARIO_DIR%\XIT_WKACC_NTL_%ITER%_!TPER!.tmp+%LOOKUP_DIR%\WalkOverrides.txt %SCENARIO_DIR%\XIT_WKACC_NTL_%ITER%_!TPER!.ntl
    COPY %SCENARIO_DIR%\XIT_XFER_NTL_%ITER%_!TPER!.tmp + %LOOKUP_DIR%\TransferOverrides.txt %SCENARIO_DIR%\XIT_XFER_NTL_%ITER%_!TPER!.ntl
    COPY %SCENARIO_DIR%\XIT_DRACC_NTL_%ITER%_!TPER!.tmp + %LOOKUP_DIR%\DriveOverrides.txt %SCENARIO_DIR%\XIT_DRACC_NTL_%ITER%_!TPER!.ntl
    
    :: Walk transit skim step 1
    runtpp %SCRIPT_PATH%\TSPTR00J.s
    IF ERRORLEVEL 2 %exitRun%
    :: Drive transit skim step 1
    runtpp %SCRIPT_PATH%\TSPTR00L.s
    IF ERRORLEVEL 2 %exitRun%
    :: Walk transit skim step 2
    runtpp %SCRIPT_PATH%\TSMAT00E.s
    IF ERRORLEVEL 2 %exitRun%
    :: Drive transit skim step 2
    runtpp %SCRIPT_PATH%\TSMAT00G.s
    IF ERRORLEVEL 2 %exitRun%
)
::endComment

:: ----------------------------------------------------------------------------
::
:: Step 3e: Check Convergence and Final Assignment
::
:: ----------------------------------------------------------------------------
:: CHECK CONVERGENCE
::%beginComment%
:: Skip convergence tests on first iteration, "unbuil network"
IF %ITER% EQU 1 (
    FOR /L %%I IN (1,1,4) DO (
        IF %%I EQU 1 (SET PER=NT)
        IF %%I EQU 2 (SET PER=AM)
        IF %%I EQU 3 (SET PER=MD)
        IF %%I EQU 4 (SET PER=PM)
        
        runtpp %SCRIPT_PATH%\IINET00C.s
        IF ERRORLEVEL 2 %exitRun%
    )
)
::endComment

::%beginComment%
:: After first iteration, check convergence criteria
IF %ITER% GEQ 2 (
    
    @ECHO. >> %SCENARIO_DIR%\converge.txt
    @ECHO. >> %SCENARIO_DIR%\converge.txt
    @ECHO Checking convergence for iteration %ITER% >> %SCENARIO_DIR%\converge.txt
    @ECHO %date% %time% >> %SCENARIO_DIR%\converge.txt
    SET error_flag=0
    
    FOR /L %%I IN (1,1,4) DO (
        
        IF %%I EQU 1 (SET PER=NT)
        IF %%I EQU 2 (SET PER=AM)
        IF %%I EQU 3 (SET PER=MD)
        IF %%I EQU 4 (SET PER=PM)
        
        runtpp %SCRIPT_PATH%\CCNET00D.s
        IF ERRORLEVEL 2 %exitRun%
        runtpp %SCRIPT_PATH%\CCMAT00A.s
        IF ERRORLEVEL 2 %exitRun%
        
        @ECHO. >> %SCENARIO_DIR%\converge.txt
        @type %SCENARIO_DIR%\converge_%ITER%_!PER!.txt >> %SCENARIO_DIR%\converge.txt
        @ECHO. >> %SCENARIO_DIR%\converge_%ITER%_!PER!.txt
        
        FOR /f "tokens=*" %%a IN (TPPL.VAR) DO (
            SET %%a
        )
    )
      
    IF !OP._ERRLINKS! GTR %conv_LinkPerc% (
        SET error_flag=1
        )
    IF !MD._ERRLINKS! GTR %conv_LinkPerc% (
        SET error_flag=1
        )
    IF !AM._ERRLINKS! GTR %conv_LinkPerc% (
        SET error_flag=1
        )
    IF !PM._ERRLINKS! GTR %conv_LinkPerc% (
        SET error_flag=1
        )
    
    ECHO.
    ECHO Iteration %ITER%: error flag !error_flag!
    ECHO.
    
    IF !error_flag! EQU 1 (
        @ECHO Iteration %ITER% Not Converged >> %SCENARIO_DIR%\converge.txt
    )
    IF !error_flag! EQU 0 (
        @ECHO Iteration %ITER% Converged! >> %SCENARIO_DIR%\converge.txt        
        SET CONV=1
    )
    IF %ITER% EQU %max_feedback% (
        @ECHO. >> %SCENARIO_DIR%\converge.txt
        ECHO Maximum Iterations %max_feedback% Hit >> %SCENARIO_DIR%\converge.txt
        @ECHO. >> %SCENARIO_DIR%\converge.txt
        
        SET CONV=1
    )
)
::endComment

IF %CONV% EQU 0 (SET FinalAssign=1)
IF %CONV% EQU 1 (SET FinalAssign=2)

::%beginComment%
:: If the model is converged, run assignment one last time
IF %FinalAssign% EQU 2 (
    :: FINAL HIGHWAY 
    FOR /L %%I IN (1,1,11) DO (
        IF %%I EQU 1 (
            SET PER=AM1
            SET ASSIGNNAME=AM1 Peak Period
            SET HWY_NET=HWY_NET_3.net
            SET NETNAME=AM Peak Period 6:00 AM to 7:00 AM
            SET CAPFAC=1
        )
        IF %%I EQU 2 (
            SET PER=AM2
            SET ASSIGNNAME=AM2 Peak Period
            SET HWY_NET=HWY_NET_3.net
            SET NETNAME=AM Peak Period 7:00 AM to 8:00 AM
            SET CAPFAC=1
        )
        IF %%I EQU 3 (
            SET PER=AM3
            SET ASSIGNNAME=AM3 Peak Period
            SET HWY_NET=HWY_NET_3.net
            SET NETNAME=AM Peak Period 8:00 AM to 9:00 AM
            SET CAPFAC=1
        )
        IF %%I EQU 4 (
            SET PER=AM4
            SET ASSIGNNAME=AM4 Peak Period
            SET HWY_NET = HWY_NET_3.net
            SET NETNAME=AM Peak Period 9:00 AM to 10:00 AM
            SET CAPFAC=1
        )
        IF %%I EQU 5 (
            SET PER=MD
            SET ASSIGNNAME=Mid Day Period
            SET HWY_NET=HWY_NET_4.net
            SET NETNAME=Mid Day Period 10:00 AM to 3:00 PM
            SET CAPFAC=4.48
        )
        IF %%I EQU 6 (
            SET PER=PM1
            SET ASSIGNNAME=PM1 Peak Period
            SET HWY_NET = HWY_NET_6.net
            SET NETNAME=PM Peak Period 3:00 AM to 4:00 PM
            SET CAPFAC=1
        )
        IF %%I EQU 7 (
            SET PER=PM2
            SET ASSIGNNAME=PM2 Peak Period
            SET HWY_NET=HWY_NET_6.net
            SET NETNAME=PM Peak Period 4:00 AM to 5:00 PM
            SET CAPFAC=1
        )
        IF %%I EQU 8 (
            SET PER=PM3
            SET ASSIGNNAME=PM3 Peak Period
            SET HWY_NET=HWY_NET_6.net
            SET NETNAME=PM Peak Period 5:00 AM to 6:00 PM
            SET CAPFAC=1
        )
        IF %%I EQU 9 (
            SET PER=PM4
            SET ASSIGNNAME=PM4 Peak Period
            SET HWY_NET=HWY_NET_6.net
            SET NETNAME=PM Peak Period 6:00 AM to 7:00 PM
            SET CAPFAC=1
        )
        IF %%I EQU 10 (
            SET PER=EV
            SET ASSIGNNAME=Evening Period
            SET HWY_NET=HWY_NET_1.net
            SET NETNAME=Evening 7:00 PM to 12:00 AM
            SET CAPFAC=3.32
        )
        IF %%I EQU 6 (
            SET PER=ON
            SET ASSIGNNAME=Overnight Period
            SET HWY_NET=HWY_NET_1.net
            SET NETNAME=Overnight 12:00 AM to 6:00 AM
            SET CAPFAC=2.59
        )
        
        runtpp %SCRIPT_PATH%\HTMAT00B.s
        IF ERRORLEVEL 2 %exitRun%
        runtpp %SCRIPT_PATH%\HTHWY00B.s
        IF ERRORLEVEL 2 %exitRun%
    )
    
    :: FINAL TRANSIT
    runtpp %SCRIPT_PATH%\PAMAT00C.s
    IF ERRORLEVEL 2 %exitRun%
    
    FOR /L %%I IN (1,1,2) DO (
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
        
        runtpp %SCRIPT_PATH%\PAMAT00A.s
        IF ERRORLEVEL 2 %exitRun%
        runtpp %SCRIPT_PATH%\PAPTR00B.s
        IF ERRORLEVEL 2 %exitRun%
        runtpp %SCRIPT_PATH%\PAPTR00D.s
        IF ERRORLEVEL 2 %exitRun%

        FOR /L %%K IN (1,1,2) DO (
            IF %%K EQU 1 (SET ACC=WK)
            IF %%K EQU 2 (SET ACC=DR)
        
            runtpp %SCRIPT_PATH%\PAMAT00B.s
            IF ERRORLEVEL 2 %exitRun%
        )
    )
    
    :: FINAL POSTPROCESSING
    FOR /L %%I IN (1,1,2) DO (
        IF %%I EQU 1 (SET PER=AM)
        IF %%I EQU 2 (SET PER=PM)
        
        :: Combine time period networks
        runtpp %SCRIPT_PATH%\PPNET00A.s
        IF ERRORLEVEL 2 %exitRun%
        runtpp %SCRIPT_PATH%\PPNET00B.s
        IF ERRORLEVEL 2 %exitRun%
        :: Export to csv
        runtpp %SCRIPT_PATH%\PPMAT00A.s
        IF ERRORLEVEL 2 %exitRun%
    )
)
::endComment

SET /a ITER=ITER+1
SET /a PREV_ITER=PREV_ITER+1

:: Return to beginning of model loop if model is no converged
IF %ITER% LEQ %max_feedback% (IF %CONV% EQU 0 (%returnToHead%))
:endComment

COPY *.prn %DATA_PATH%\abm_logs\*.prn

:: Delete all the temporary TP+ printouts and cluster files
DEL *.prn

:endOfFile
IF ERRORLEVEL EQU 0 (
    ECHO RUN SUCCEEDED
)
IF ERRORLEVEL EQU 1 (
    ECHO RUN FAILED IN TOURCAST
)
IF ERRORLEVEL EQU 2 (
    ECHO RUN FAILED IN CUBE SCRIPTS
)