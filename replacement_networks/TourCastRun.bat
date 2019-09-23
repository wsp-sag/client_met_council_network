@echo on 
@cd TourCast\bin  

@IF %TC_vehavail%==1 (
    echo Vehicle Availability Sequence
    ModelEngine.exe VehicleAvailabilityModel.py 
    ModelEngine.exe VehicleAvailabilityModelPostProcessor.py  
)


@IF %TC_schLocation%==1 (
    echo School Location
    ModelEngine.exe SchoolLocationConstrChoice.py
)


@IF %TC_workLocation%==1 (
    echo Usual Work Location
    ModelEngine.exe WorkplaceLocationChoiceModelPreProcessor.py
    ModelEngine.exe UsualWorkplaceLocationChoiceModel.py UsualWorkplaceLocationTourModeChoiceLogsumModel.py
)

@IF %TC_pass%==1 (
    echo Pass Models
    ModelEngine.exe PassModels.py
)

@IF %TC_DAP%==1 (
    echo DAP
    ModelEngine.exe DailyActivityPatternModelPreProcessor.py
    ModelEngine.exe DailyActivityPatternModel.py
)

@IF %TC_mandTourDest%==1 (
    echo Mandatory Tour Destination Choice - Work and University
    ModelEngine.exe TourDestinationChoiceUniversity.py  TourModeChoiceLogsum_SchoolLocation.py
    ModelEngine.exe TourDestinationChoiceWork.py TourModeChoiceLogsum_Work.py
)

@IF %TC_mandTourTOD%==1 (
    echo Mandatory Tour TOD
    ModelEngine.exe MandatoryTourTimeOfDayChoiceModelPreProcessor.py
    ModelEngine.exe TourTimeOfDayDAPFirstTours.py
    ModelEngine.exe TourTimeOfDayDAPSecondTours.py
)

@IF %TC_schEscort%==1 (
    echo School Escorting
    ModelEngine.exe SchoolEscortModel.py
)

@IF %TC_FJ%==1 (
    echo Fully Joint Tours
    ModelEngine.exe FullyJointTourPreProcessor.py
    ModelEngine.exe FullyJointTour.py
    ModelEngine.exe FullyJointTourDestinationChoice.py TourModeChoiceLogsum_FullyJoint.py
    ModelEngine.exe FullyJointTourTimeOfDay.py
)

@IF %TC_INM%==1 (
    echo INM Tours
    ModelEngine.exe IndividualNonMandatoryPreProcessor.py
    ModelEngine.exe IndividualNonMandatory.py
    ModelEngine.exe IndividualNonMandatoryEscortTourDestinationChoice.py TourModeChoiceLogsum_IndividualNonMandatory_Escort.py
    ModelEngine.exe IndividualNonMandatoryTourDestinationChoice.py TourModeChoiceLogsum_IndividualNonMandatory.py
    ModelEngine.exe TourTimeOfDayIndNonMandNonEscort.py
    ModelEngine.exe TourTimeOfDayIndNonMandEscort.py
)

@IF %TC_stopGen%==1 (
    echo Stop Generation
    ModelEngine.exe StopGeneration.py
)

@IF %TC_tourMC%==1 (
    echo Home-Based Tour Mode Choice
    ModelEngine.exe TourModeChoiceHomeBased.py
)

@IF %TC_WB%==1 (
    echo Work-Based Tours
    ModelEngine.exe WorkBasedSubTourPreProcessor.py
    ModelEngine.exe WorkBasedSubTour.py
    ModelEngine.exe WorkBasedTourDestinationChoice.py TourModeChoiceLogsum_WorkBased.py
    ModelEngine.exe WorkBasedTourTimeOfDay.py
    ModelEngine.exe WorkBasedStopGeneration.py
    ModelEngine.exe WorkBasedTourModeChoice.py
)

@IF %TC_stopDestTOD%==1 (
    echo Stop-Level Models
    ModelEngine.exe StopDestination.py
    ModelEngine.exe StopTimeOfDay.py
)

@IF %TC_tripMC%==1 (
    echo Trip Mode Choice
    ModelEngine.exe TripModeChoice.py
)

