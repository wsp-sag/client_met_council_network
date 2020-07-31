@echo on 
@cd ..\TourCast\bin 
@echo TourCast Aborted > ..\..\Cube\TC_error.txt 
ModelEngine.exe VehicleAvailabilityModel.py 
@IF ERRORLEVEL 2 GOTO TCERROR 
ModelEngine.exe VehicleAvailabilityModelPostProcessor.py  
@IF ERRORLEVEL 2 GOTO TCERROR 
ModelEngine.exe SchoolLocationConstrChoice.py  
@IF ERRORLEVEL 2 GOTO TCERROR 
ModelEngine.exe WorkplaceLocationChoiceModelPreProcessor.py  
@IF ERRORLEVEL 2 GOTO TCERROR 
ModelEngine.exe UsualWorkplaceLocationChoiceModel.py UsualWorkplaceLocationTourModeChoiceLogsumModel.py  
@IF ERRORLEVEL 2 GOTO TCERROR 
ModelEngine.exe PassModels.py  
@IF ERRORLEVEL 2 GOTO TCERROR 
ModelEngine.exe DailyActivityPatternModelPreProcessor.py  
@IF ERRORLEVEL 2 GOTO TCERROR 
ModelEngine.exe DailyActivityPatternModel.py  
@IF ERRORLEVEL 2 GOTO TCERROR 
ModelEngine.exe TourDestinationChoiceUniversity.py  TourModeChoiceLogsum_SchoolLocation.py  
@IF ERRORLEVEL 2 GOTO TCERROR 
ModelEngine.exe TourDestinationChoiceWork.py TourModeChoiceLogsum_Work.py  
@IF ERRORLEVEL 2 GOTO TCERROR 
ModelEngine.exe MandatoryTourTimeOfDayChoiceModelPreProcessor.py  
@IF ERRORLEVEL 2 GOTO TCERROR 
ModelEngine.exe TourTimeOfDayDAPFirstTours.py  
@IF ERRORLEVEL 2 GOTO TCERROR 
ModelEngine.exe TourTimeOfDayDAPSecondTours.py  
@IF ERRORLEVEL 2 GOTO TCERROR 
ModelEngine.exe SchoolEscortModel.py  
@IF ERRORLEVEL 2 GOTO TCERROR 
ModelEngine.exe FullyJointTourPreProcessor.py  
@IF ERRORLEVEL 2 GOTO TCERROR 
ModelEngine.exe FullyJointTour.py  
@IF ERRORLEVEL 2 GOTO TCERROR 
ModelEngine.exe FullyJointTourDestinationChoice.py TourModeChoiceLogsum_FullyJoint.py  
@IF ERRORLEVEL 2 GOTO TCERROR 
ModelEngine.exe FullyJointTourTimeOfDay.py  
@IF ERRORLEVEL 2 GOTO TCERROR 
ModelEngine.exe IndividualNonMandatoryPreProcessor.py  
@IF ERRORLEVEL 2 GOTO TCERROR 
ModelEngine.exe IndividualNonMandatory.py  
@IF ERRORLEVEL 2 GOTO TCERROR 
ModelEngine.exe IndividualNonMandatoryEscortTourDestinationChoice.py TourModeChoiceLogsum_IndividualNonMandatory_Escort.py  
@IF ERRORLEVEL 2 GOTO TCERROR 
ModelEngine.exe IndividualNonMandatoryTourDestinationChoice.py TourModeChoiceLogsum_IndividualNonMandatory.py  
@IF ERRORLEVEL 2 GOTO TCERROR 
ModelEngine.exe TourTimeOfDayIndNonMandNonEscort.py  
@IF ERRORLEVEL 2 GOTO TCERROR 
ModelEngine.exe TourTimeOfDayIndNonMandEscort.py  
@IF ERRORLEVEL 2 GOTO TCERROR 
ModelEngine.exe StopGeneration.py  
@IF ERRORLEVEL 2 GOTO TCERROR 
ModelEngine.exe TourModeChoiceHomeBased.py  
@IF ERRORLEVEL 2 GOTO TCERROR 
ModelEngine.exe WorkBasedSubTourPreProcessor.py  
@IF ERRORLEVEL 2 GOTO TCERROR 
ModelEngine.exe WorkBasedSubTour.py  
@IF ERRORLEVEL 2 GOTO TCERROR 
ModelEngine.exe WorkBasedTourDestinationChoice.py TourModeChoiceLogsum_WorkBased.py  
@IF ERRORLEVEL 2 GOTO TCERROR 
ModelEngine.exe WorkBasedTourTimeOfDay.py  
@IF ERRORLEVEL 2 GOTO TCERROR 
ModelEngine.exe WorkBasedStopGeneration.py  
@IF ERRORLEVEL 2 GOTO TCERROR 
ModelEngine.exe WorkBasedTourModeChoice.py  
@IF ERRORLEVEL 2 GOTO TCERROR 
ModelEngine.exe StopDestination.py  
@IF ERRORLEVEL 2 GOTO TCERROR 
ModelEngine.exe StopTimeOfDay.py  
@IF ERRORLEVEL 2 GOTO TCERROR 
ModelEngine.exe TripModeChoice.py  
@IF ERRORLEVEL 2 GOTO TCERROR 
@del ..\..\Cube\TC_error.txt 
exit 
:TCERROR 
@echo TourCast Error > ..\..\Cube\TC_error.txt 
@pause 
exit 
