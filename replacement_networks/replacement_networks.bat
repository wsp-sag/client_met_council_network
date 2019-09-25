::~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
:: run_initial_auto_skim.bat
::
:: MS-DOS batch file to execute the Auto Skim step of the Met Council travel
:: model.
::
::
::~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
%echo off
:: ----------------------------------------------------------------------------
::
:: Step 1:  Set the necessary path variables
::
:: ----------------------------------------------------------------------------
SET "beginComment=goto :endComment"

:: The location of the RUNTPP executable from Citilabs - 64bit first
SET TPP_PATH=C:\Program Files\Citilabs\CubeVoyager;C:\Program Files (x86)\Citilabs\CubeVoyager

:: The location of python
SET PYTHON_PATH=C:\Python27\ArcGIS10.6

:: Add these variables to the PATH environment variable, moving the current path to the back
SET OLD_PATH=%PATH%
SET PATH=%RUNTIME%;%TPP_PATH%;%PYTHON_PATH%;%OLD_PATH%

:: Set CSV input paths
SET NETWORK_FOLDER=network_06242019
SET SCRIPT_PATH=replacement_scripts
SET TRIP_DIR=trip_files
if not exist \outputs mkdir \outputs
SET SCENARIO_DIR=outputs
SET COMPARISON_DIR=comparisons
SET LOOKUP_DIR=lookup_files
SET INPUT_DIR=inputs
SET TOURCAST_DIR=TourCast

SET LINK_PATH=%NETWORK_FOLDER%/all_link.dbf
SET NODE_PATH=%NETWORK_FOLDER%/all_node.dbf

:: Set zones
SET zone_attribs=%INPUT_DIR%/Zones_2015.dbf

:: Set transit
SET xit_lines=%NETWORK_FOLDER%/transit.lin
SET xit_system=%LOOKUP_DIR%/PT_SYSTEM_2010.PTS
SET xit_faremat=%LOOKUP_DIR%/FAREMAT_2010.txt
SET xit_fare=%LOOKUP_DIR%/PT_FARE_2010.FAR
SET xit_pnrnodes=%NETWORK_FOLDER%/GENERATE_PNR_ACCESS.s

SET max_threads=16

SET bikeSpeed1=13
SET bikeSpeed2=13
SET bikeSpeed3=10
SET bikeFact1=0.8
SET walkSpeed=2.5

SET hwy_assignIters=5
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
%beginComment%
runtpp %SCRIPT_PATH%\make_complete_network_from_file.s
runtpp %SCRIPT_PATH%\make_highway_network_from_file.s
runtpp %SCRIPT_PATH%\make_bike_network_from_file.s
runtpp %SCRIPT_PATH%\make_walk_network_from_file.s
runtpp %SCRIPT_PATH%\FullMakeNetwork15.s
:endComment

:: INITIAL NETWORKS AND INITIAL SKIMS
:: NON-MOTORIZED
%beginComment%
runtpp %SCRIPT_PATH%\NMNET00A.s
runtpp %SCRIPT_PATH%\NMHWY00A.s
runtpp %SCRIPT_PATH%\NMHWY00B.s
runtpp %SCRIPT_PATH%\NMMAT00A.s
:endComment

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
:endComment

:: TRANSIT
%beginComment%
runtpp %SCRIPT_PATH%\TSNET00A.s
runtpp %SCRIPT_PATH%\TSNET00B.s

for /L %%I IN (1, 1, 2) DO (

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

:: INITIALIZE TRUCK AND SPECIAL GENERATOR
SET ext_sta=%LOOKUP_DIR%\ext_sta.dbf
SET qrfm=%LOOKUP_DIR%\QRFM.txt
SET qrfm_ff=%LOOKUP_DIR%\QRFM_FF.txt
SET zone_attribs=%INPUT_DIR%\Zones_2015.dbf
SET LU_external=%LOOKUP_DIR%\EI_IE_EE_Lookup.txt
SET ee_auto_dist=%LOOKUP_DIR%\eeAutoJointDist.csv
SET LU_spc_tod=%LOOKUP_DIR%\AirportTODParams.txt
SET ee_fratar=%LOOKUP_DIR%\EE_FRATAR.txt
SET ee_trk_dist=%LOOKUP_DIR%\EE_SEED_TRK_4.mat

%beginComment%
runtpp %SCRIPT_PATH%\TSGEN00A.s
runtpp %SCRIPT_PATH%\TSMAT00H.s
runtpp %SCRIPT_PATH%\TSMAT00I.s
runtpp %SCRIPT_PATH%\TSFRA00A.s

runtpp %SCRIPT_PATH%\TSMAT00K.s
runtpp %SCRIPT_PATH%\TSMAT00L.s
runtpp %SCRIPT_PATH%\TSFRA00B.s
runtpp %SCRIPT_PATH%\TSMAT00M.s
:endComment

:: MODEL LOOP
SET ITER=1
SET PREV_ITER=0

IF ITER EQU 1 (
    *copy %zone_attribs% %SCENARIO_DIR%\zones_0.dbf
    )

:: CREATE EXOGENOUS VARIABLES
%beginComment%
copy %INPUT_DIR%\zones_0.dbf %SCENARIO_DIR%\zones_0.dbf
runtpp %SCRIPT_PATH%\EVMAT00A.s
runtpp %SCRIPT_PATH%\EVMAT00B.s
runtpp %SCRIPT_PATH%\EVMAT00C.s
runtpp %SCRIPT_PATH%\EVMAT00D.s
runtpp %SCRIPT_PATH%\EVMAT00E.s
runtpp %SCRIPT_PATH%\EVMAT00F.s
:endComment

:: Run TourCast
%beginComment%
SET TPER=PK
copy %SCENARIO_DIR%\XIT_WKACC_NTL_0_%TPER%.tmp + %LOOKUP_DIR%\WalkOverrides.txt %SCENARIO_DIR%\XIT_WKACC_NTL_0_%TPER%.ntl
copy %SCENARIO_DIR%\XIT_XFER_NTL_0_%TPER%.tmp + %LOOKUP_DIR%\TransferOverrides.txt %SCENARIO_DIR%\XIT_XFER_NTL_0_%TPER%.ntl
:: The drive access NTL file was created earlier?
::copy %SCENARIO_DIR%\XIT_DRACC_NTL_0_%TPER%.tmp + %LOOKUP_DIR%\DriveOverrides.txt %SCENARIO_DIR%\XIT_DRACC_NTL_0_%TPER%.ntl

SET TPER=OP
copy %SCENARIO_DIR%\XIT_WKACC_NTL_0_%TPER%.tmp + %LOOKUP_DIR%\WalkOverrides.txt %SCENARIO_DIR%\XIT_WKACC_NTL_0_%TPER%.ntl
copy %SCENARIO_DIR%\XIT_XFER_NTL_0_%TPER%.tmp + %LOOKUP_DIR%\TransferOverrides.txt %SCENARIO_DIR%\XIT_XFER_NTL_0_%TPER%.ntl
:: The drive access NTL file was created earlier?
copy %SCENARIO_DIR%\XIT_DRACC_NTL_0_%TPER%.tmp + %LOOKUP_DIR%\DriveOverrides.txt %SCENARIO_DIR%\XIT_DRACC_NTL_0_%TPER%.ntl
:endComment

SET households=%INPUT_DIR%\Households2015.dbf
SET persons=%INPUT_DIR%\Persons2015.dbf

%beginComment%
:: These python scripts replace TCMAT00A.s, TCMAT00B.s.
python %SCRIPT_PATH%\make_tour_cast_input_file.py %TOURCAST_DIR% %SCENARIO_DIR% %ITER% %households% %persons%
python %TOURCAST_DIR%\script\update_tourcast_json_inputs.py %TOURCAST_DIR%\script\

SET TC_vehavail=1
SET TC_schLocation=1
SET TC_workLocation=1
SET TC_pass=1
SET TC_DAP=1
SET TC_mandTourDest=1
SET TC_mandTourTOD=1
SET TC_schEscort=1
SET TC_FJ=1
SET TC_INM=1
SET TC_stopGen=1
SET TC_tourMC=1
SET TC_WB=1
SET TC_stopDestTOD=1
SET TC_tripMC=1

:: This batch file replaces TCPIL00B.S
.\TourCastRun.bat

::Not sure why the following script moves "1" to "ITER". Shouldn't it be iter to iter + 1 or something like that?
:: Also, the naming misses a "_"?
runtpp %SCRIPT_PATH%\TCPIL00D.s

:endComment

:: FREIGHT EXTERNALS AND SPECIAL GENERATOR DISTRIBUTION
:: FREIGHT
:: In %SCRIPT_PATH%\FTPIL00A.s
:: Why the hard code to ITER=2, PREV_ITER=1?
SET ITER=2
SET PREV_ITER=1

%beginComment%
runtpp %SCRIPT_PATH%\FTMAT00A.s
runtpp %SCRIPT_PATH%\FTTRD00A.s
runtpp %SCRIPT_PATH%\FTMAT00B.s
:endComment

:: EXTERNAL AUTOS
SET ITER=1
SET PREV_ITER=0
:: Have questions 1) why is ext_zones in ()? Why is it throwing an  for the array size?
%beginComment%
::runtpp %SCRIPT_PATH%\EEMAT00A.s
::runtpp %SCRIPT_PATH%\EEMAT00B.s

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
)
runtpp %SCRIPT_PATH%\EEMAT00E.s
:endComment

%beginComment%
:: SPECIAL GENERATORS
:: Data from AirportModeChoiceParams.txt
::**********************************************
:: MODE CHOICE MODELS
::**********************************************
SET TTIME_AUTO=10.0
SET TTIME_SR=7.5
SET AUTOCOST=0.20            ; auto operating cost 20 cents per mile
SET C_DA=0.0
SET DA_COST=-0.134
SET C_SR2=-1.35          
SET SR2_COST=-0.134 
SET C_SR3=-2.72
SET SR3_COST=-0.134 
SET HWTCOEFF=-0.0263
::********** TRANSIT
SET TCOEFF_WA=-0.0263
SET FARE_WA=-0.134
SET TCOEFF_DA=-0.0263
SET FARECOST=-0.134 
SET C_TR=-0.677

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
    runtpp %SCRIPT_PATH%\SGMAT00A.s
    runtpp %SCRIPT_PATH%\SGMAT00B.s
)
:endComment

%beginComment%
:: HIGHWAY
SET ITER=2
SET PREV_ITER=1

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

:: TRANSIT
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
    
    runtpp %SCRIPT_PATH%\TSNET00F.s
    runtpp %SCRIPT_PATH%\TSPTR00N.s
    runtpp %SCRIPT_PATH%\TSPTR00S.s
    runtpp %SCRIPT_PATH%\TSPTR00U.s
    runtpp %SCRIPT_PATH%\TSPIL00G.s
    runtpp %SCRIPT_PATH%\TSPTR00J.s
    runtpp %SCRIPT_PATH%\TSPTR00L.s
    runtpp %SCRIPT_PATH%\TSMAT00E.s
    runtpp %SCRIPT_PATH%\TSMAT00G.s
    runtpp %SCRIPT_PATH%\TSPIL00E.s
)
