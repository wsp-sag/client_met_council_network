; Do not change filenames or add or remove FILEI/FILEO statements using an editor. Use Cube/Application Manager.
RUN PGM = NETWORK MSG = 'Calculate Transit Speeds for %TPER%'
FILEO NETO = "%SCENARIO_DIR%\XIT_NET_0_%TPER%.net"
FILEI LOOKUPI[2] = "%LOOKUP_DIR%\%TPER%ExpressDelays.txt"
FILEI LOOKUPI[1] = "%LOOKUP_DIR%\%TPER%LocalDelays.txt"
FILEI LINKI[1] = "%SCENARIO_DIR%\TransitBase.NET"

    ; Set period name
    _per='%TPER%'
    
    ;  transit time = congested time +  distance * link delay
    ;   Delays are calibrated by AREA and facility type and time period.
    LOOKUP NAME = locdelay, LOOKUP[1] = 1, RESULT = 2,
                            LOOKUP[2] = 1, RESULT = 3,
                            LOOKUP[3] = 1, RESULT = 4,
                            LOOKUP[4] = 1, RESULT = 5,
                            LOOKUP[5] = 1, RESULT = 6,
                            LOOKUP[6] = 1, RESULT = 7,
                            LOOKUP[7] = 1, RESULT = 7,
                            LOOKUP[8] = 1, RESULT = 7,
                            LOOKUP[9] = 1, RESULT = 7,
                            LOOKUP[10] = 1, RESULT = 7,
                            FAIL = 0,0,0, INTERPOLATE = N,
                            LOOKUPI = 1, LIST = Y

    LOOKUP NAME = expdelay, LOOKUP[1] = 1, RESULT = 2,
                            LOOKUP[2] = 1, RESULT = 3,
                            LOOKUP[3] = 1, RESULT = 4,
                            LOOKUP[4] = 1, RESULT = 5,
                            LOOKUP[5] = 1, RESULT = 6,
                            LOOKUP[6] = 1, RESULT = 7,
                            LOOKUP[7] = 1, RESULT = 7,
                            LOOKUP[8] = 1, RESULT = 7,
                            LOOKUP[9] = 1, RESULT = 7,
                            LOOKUP[10] = 1, RESULT = 2, ; 1 and 10 are rural area types
                            FAIL = 0,0,0, INTERPOLATE = N,
                            LOOKUPI = 2, LIST = Y


;;--------------------------------------------------------------------------

    ; Set transit speeds - same for PK/OP
    IF (LI.1.SPEED = 0)
      SPEED = 0.1
    ELSE
      SPEED = LI.1.SPEED
    ENDIF
    
;;--------------------------------------------------------------------------

    ; Code free flow speed for all links
    LOCTIME = (DISTANCE * 60 / SPEED)
    EXPTIME = (DISTANCE * 60 / SPEED)
    
;;--------------------------------------------------------------------------    
        
    IF (_per = 'PK')
        _ttime_assert = LI.1.TTIME_ASSERT_AM
    ELSE 
        _ttime_assert = LI.1.TTIME_ASSERT_MD
    ENDIF
    
    ; Override manually coded speed for transit only links
    IF (_ttime_assert > 0)
        LOCTIME = _ttime_assert
        EXPTIME = _ttime_assert
        LRTTIME = _ttime_assert
    ENDIF    

;;--------------------------------------------------------------------------
    
    IF (_per = 'PK')
        _trn_priority = LI.1.TRN_PRIORITY_AM
    ELSE
        _trn_priority = LI.1.TRN_PRIORITY_MD
    ENDIF
        
    ;Calculate Local Bus Transit Travel Time
    IF (LOCTIME = 0)
         _DELAY = locdelay(LI.1.AREA_TYPE, LI.1.RCI)
         IF (_trn_priority = 2)
            IF ((SPEED + 15) < 50)
                _tspeed = MIN(SPEED + 15, 35)
            ELSE
                _tspeed = MAX(SPEED, 35)
            ENDIF
            LOCTIME = (DISTANCE * 60 / _tspeed) + (DISTANCE * _DELAY)
         ELSE
            LOCTIME = (DISTANCE * 60 / SPEED) + (DISTANCE * _DELAY)
         ENDIF
    
        IF (LOCTIME = 0) 
            PRINT LIST = 'LOCAL BUS TIME IS ZERO FOR - ', A(6), B(6)
        ENDIF        
    ENDIF
;;--------------------------------------------------------------------------
    
    ;Calculate Express Bus Transit Travel Time
    IF (EXPTIME = 0)
        _DELAY = expdelay(LI.1.AREA_TYPE, LI.1.RCI)
         IF (_trn_priority = 2)
            IF ((SPEED + 15) < 50)
                _tspeed = MIN(SPEED + 15, 35)
            ELSE
                _tspeed = MAX(SPEED, 35)
            ENDIF
            EXPTIME = (DISTANCE * 60 / _tspeed) + (DISTANCE * _DELAY)
         ELSE
            EXPTIME = (DISTANCE * 60 / SPEED) + (DISTANCE * _DELAY)
         ENDIF
    
        IF (EXPTIME = 0) 
            PRINT LIST = 'EXPRESS BUS TIME IS ZERO FOR - ', A(6), B(6)
        ENDIF
    ENDIF       

ENDRUN
