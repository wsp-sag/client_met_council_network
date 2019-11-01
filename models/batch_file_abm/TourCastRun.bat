@echo on 
@cd TourCast\bin  

@IF %TC_vehavail% EQU 1 (
    echo Vehicle Availability Sequence
    ModelEngine.exe VehicleAvailabilityModel.py 
    ModelEngine.exe VehicleAvailabilityModelPostProcessor.py  
)
IF ERRORLEVEL 1 %exitRun%

@IF %TC_schLocation% EQU 1 (
    echo School Location
    ModelEngine.exe SchoolLocationConstrChoice.py
)
IF ERRORLEVEL 1 %exitRun%

@IF %TC_workLocation% EQU 1 (
    echo Usual Work Location
    ModelEngine.exe WorkplaceLocationChoiceModelPreProcessor.py
    ModelEngine.exe UsualWorkplaceLocationChoiceModel.py UsualWorkplaceLocationTourModeChoiceLogsumModel.py
)
IF ERRORLEVEL 1 %exitRun%

@IF %TC_pass% EQU 1 (
    echo Pass Models
    ModelEngine.exe PassModels.py
)
IF ERRORLEVEL 1 %exitRun%

@IF %TC_DAP% EQU 1 (
    echo DAP
    ModelEngine.exe DailyActivityPatternModelPreProcessor.py
    ModelEngine.exe DailyActivityPatternModel.py
)
IF ERRORLEVEL 1 %exitRun%

@IF %TC_mandTourDest% EQU 1 (
    echo Mandatory Tour Destination Choice - Work and University
    ModelEngine.exe TourDestinationChoiceUniversity.py  TourModeChoiceLogsum_SchoolLocation.py
    ModelEngine.exe TourDestinationChoiceWork.py TourModeChoiceLogsum_Work.py
)
IF ERRORLEVEL 1 %exitRun%

@IF %TC_mandTourTOD% EQU 1 (
    echo Mandatory Tour TOD
    ModelEngine.exe MandatoryTourTimeOfDayChoiceModelPreProcessor.py
    ModelEngine.exe TourTimeOfDayDAPFirstTours.py
    ModelEngine.exe TourTimeOfDayDAPSecondTours.py
)
IF ERRORLEVEL 1 %exitRun%

@IF %TC_schEscort% EQU 1 (
    echo School Escorting
    ModelEngine.exe SchoolEscortModel.py
)
IF ERRORLEVEL 1 %exitRun%

@IF %TC_FJ% EQU 1 (
    echo Fully Joint Tours
    ModelEngine.exe FullyJointTourPreProcessor.py
    ModelEngine.exe FullyJointTour.py
    ModelEngine.exe FullyJointTourDestinationChoice.py TourModeChoiceLogsum_FullyJoint.py
    ModelEngine.exe FullyJointTourTimeOfDay.py
)
IF ERRORLEVEL 1 %exitRun%

@IF %TC_INM% EQU 1 (
    echo INM Tours
    ModelEngine.exe IndividualNonMandatoryPreProcessor.py
    ModelEngine.exe IndividualNonMandatory.py
    ModelEngine.exe IndividualNonMandatoryEscortTourDestinationChoice.py TourModeChoiceLogsum_IndividualNonMandatory_Escort.py
    ModelEngine.exe IndividualNonMandatoryTourDestinationChoice.py TourModeChoiceLogsum_IndividualNonMandatory.py
    ModelEngine.exe TourTimeOfDayIndNonMandNonEscort.py
    ModelEngine.exe TourTimeOfDayIndNonMandEscort.py
)
IF ERRORLEVEL 1 %exitRun%

@IF %TC_stopGen% EQU 1 (
    echo Stop Generation
    ModelEngine.exe StopGeneration.py
)
IF ERRORLEVEL 1 %exitRun%

@IF %TC_tourMC% EQU 1 (
    echo Home-Based Tour Mode Choice
    ModelEngine.exe TourModeChoiceHomeBased.py
)
IF ERRORLEVEL 1 %exitRun%

@IF %TC_WB% EQU 1 (
    echo Work-Based Tours
    ModelEngine.exe WorkBasedSubTourPreProcessor.py
    ModelEngine.exe WorkBasedSubTour.py
    ModelEngine.exe WorkBasedTourDestinationChoice.py TourModeChoiceLogsum_WorkBased.py
    ModelEngine.exe WorkBasedTourTimeOfDay.py
    ModelEngine.exe WorkBasedStopGeneration.py
    ModelEngine.exe WorkBasedTourModeChoice.py
)
IF ERRORLEVEL 1 %exitRun%

@IF %TC_stopDestTOD% EQU 1 (
    echo Stop-Level Models
    ModelEngine.exe StopDestination.py
    ModelEngine.exe StopTimeOfDay.py
)
IF ERRORLEVEL 1 %exitRun%

@IF %TC_tripMC% EQU 1 (
    echo Trip Mode Choice
    ModelEngine.exe TripModeChoice.py
)
IF ERRORLEVEL 1 %exitRun%

@CD ../..
