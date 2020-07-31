:: Set user parameters for Met Council Model
SET MODEL_YEAR=2015

:: FOLDER variables
SET DATA_PATH=..\..\data
SET EXTERNAL_DATA_PATH=%DATA_PATH%\external\met_council
SET INTERIM_DATA_PATH=%DATA_PATH%\interim
SET NETWORK_FOLDER=%INTERIM_DATA_PATH%\networks\fixed_width

SET SCRIPT_PATH=cube_scripts
SET SCENARIO_DIR=%DATA_PATH%\test_new_network_outputs
SET LOOKUP_DIR=lookup_files
SET INPUT_DIR=%EXTERNAL_DATA_PATH%\population_data
SET TOURCAST_DIR=TourCast
SET TRIP_DIR=%EXTERNAL_DATA_PATH%\reference_abm_trip_tables

:: INPUT FILE paths
SET complete_network_script_input_path=%NETWORK_FOLDER%\make_complete_network_from_fixed_width_file.s
SET complete_network_script_output_path=%SCRIPT_PATH%\make_complete_network_from_fixed_width_file.s

:: Set zones
SET zone_attribs=%INPUT_DIR%\Zones_%MODEL_YEAR%.dbf
:: Set link and node paths for complete network
SET LINK_DATA_PATH=%NETWORK_FOLDER%\link.txt
SET NODE_DATA_PATH=%NETWORK_FOLDER%\node.txt
:: Set transit paths
SET xit_lines=%NETWORK_FOLDER%\transit.lin
SET xit_system=%LOOKUP_DIR%\PT_SYSTEM_2010.PTS
SET xit_faremat=%LOOKUP_DIR%\FAREMAT_2010_updated.txt
SET xit_fare=%LOOKUP_DIR%\PT_FARE_2010.FAR
SET xit_pnrnodes=%SCRIPT_PATH%\GENERATE_PNR_ACCESS.s
SET T_PRIORITY_PATH=%LOOKUP_DIR%\T_Priority.dbf
SET T_MANTIME_PATH=%LOOKUP_DIR%\T_MANTIME.dbf
SET T_DISTANCE_PATH=%LOOKUP_DIR%\Distances.dbf
:: Set willingness to pay tolls
SET LU_will2pay=%LOOKUP_DIR%\Will2Pay_oneCurve.txt
:: Set highway network (perhaps scripts should be reworked to avoid this step?)
SET iHwyNet=%SCENARIO_DIR%\highway_2015.net
:: Set highway network parameters
SET LU_AlphaBeta=lookup_files\AlphaBetaLookup.txt
SET LU_capacity=lookup_files\CapacityLookup.txt
SET LU_speed=lookup_files\SpeedLookup85.txt
:: Set truck and special generator files
SET ext_sta=%LOOKUP_DIR%\ext_sta.dbf
SET qrfm=%LOOKUP_DIR%\QRFM.txt
SET qrfm_ff=%LOOKUP_DIR%\QRFM_FF.txt
SET LU_external=%LOOKUP_DIR%\EI_IE_EE_Lookup.txt
SET ee_auto_dist=%LOOKUP_DIR%\eeAutoJointDist.csv
SET LU_spc_tod=%LOOKUP_DIR%\AirportTODParams.txt
SET ee_fratar=%LOOKUP_DIR%\EE_FRATAR.txt
SET ee_trk_dist=%LOOKUP_DIR%\EE_SEED_TRK_4.mat
:: Set household and person files
SET households=%INPUT_DIR%\Households2015.dbf
SET persons=%INPUT_DIR%\Persons2015.dbf

:: CUBE model parameters
:: Initialize the model run to an unconverged state
SET CONV=0
:: Set congergence criteria (percent expressed as integer out of 100)
SET conv_LinkVol=10
SET conv_LinkPerc=1
:: Initialize model to begin on iteration 1
SET ITER=1
SET PREV_ITER=0
:: Set cube cluster threads
SET max_threads=16
:: Set max feedback loops
SET max_feedback=5
:: Set max iterations of highway assignment
SET hwy_assignIters=20
:: Set number of zones (total, internal, external)
SET zones=3061
SET int_zones=3030
SET ext_zones=31
::Set model transit year
SET xit_fac_year=2010
:: Set default bike and walk speeds
SET bikeSpeed1=13
SET bikeSpeed2=13
SET bikeSpeed3=10
SET bikeFact1=0.8
SET walkSpeed=2.5
:: Set HOV occupancy
SET hwy_HOV2OCC=2
SET hwy_HOV3OCC=3.2
:: Set truck factors
SET hwy_TrkFac=2
:: Set highway toll settings
SET hwy_TollSetting=1
::Mode choice coefficients
SET TTIME_AUTO=10.0
SET TTIME_SR=7.5
SET AUTOCOST=0.20
SET C_DA=0.0
SET DA_COST=-0.134
SET C_SR2=-1.35          
SET SR2_COST=-0.134 
SET C_SR3=-2.72
SET SR3_COST=-0.134 
SET HWTCOEFF=-0.0263
:: TRANSIT coefficients
SET TCOEFF_WA=-0.0263
SET FARE_WA=-0.134
SET TCOEFF_DA=-0.0263
SET FARECOST=-0.134 
SET C_TR=-0.677

:: PATH variables
:: !!WARNING!!
:: Do not change unless program installations are non-standard
:: !! WARNING!!

:: The location of the runtpp executable from Citilabs - 64bit first
SET TPP_PATH=C:\Program Files\Citilabs\CubeVoyager;C:\Program Files (x86)\Citilabs\CubeVoyager

:: The location of python
SET PYTHON_PATH=C:\python27\ArcGIS10.6

:: Add these variables to the PATH environment variable, moving the current path to the back
SET OLD_PATH=%PATH%
SET PATH=%TPP_PATH%;%PYTHON_PATH%;%OLD_PATH%

:: Set shortcut keys
SET "beginComment=goto :endComment"
SET "returnToHead=goto :head"
SET "exitRun=goto :endOfFile"
SET "check_cube_errors=IF ERRORLEVEL 2 %exitRun%"
SET "check_python_errors=IF ERRORLEVEL 1 %exitRun%"

