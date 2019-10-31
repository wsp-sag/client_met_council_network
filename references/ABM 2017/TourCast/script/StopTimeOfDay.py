####################################################################
# StopTimeOfDay.py
# Config for MultiModel component for stop time of day models
####################################################################

from Globals import *

modelComponentName="StopTimeOfDay"
instantiationType="MultiModelComponent"

subModels={
           "HalfTour1" : r"StopTimeOfDaySubmodel_HalfTour1.py",
           "HalfTour2" : r"StopTimeOfDaySubmodel_HalfTour2.py",
           }

dataReferences = [
    {"type" : "dbffile",
     "name" : "Persons",
     # Using this to get a list of persons sorted by zone and as a fallback lookup for person type
     "filename" : cube___PERSONS_FILE___, 
     "columns" : ["personId", # 0
                  "hhzon",    # 1
                  "ptypeDAP",   # 2
                  ],
     "deferredLoad": True
    },
    {"type" : "dbffile",
     "name" : "InputTours",     
     "filename" : cube___STOP_GENERATION_TOURS_HOME_BASED___, 
     "columns" : [
                     "personId",
                     "hhId",
                     "persTourId",  
                     "tourPurp",
                     "arrival",
                     "departure",
                     "homeZoneId",
                     "destZoneId",
                     "esPrsOutId",
                     "esTrOutId",
                     "esPrsInId",
                     "esTrInId",
                    ],
     "deferredLoad": True
    },

    {"type" : "dbffile",
     "name" : "InputTourModes",     
     "filename" : cube___HOME_BASED_TOUR_MODE_CHOICE___, # file paths MUST BE RAW strings (preceded by 'r')
     "columns" : [
                      "personId",   # part 1 of tour pk, for individual tours would be same as person id
                      "persTourId",
                      "homeZoneId", # for chunking
                      "tourMode"    # numerical value of TourMode enum 
                    ],
     "deferredLoad": True
     },

    {"type" : "dbffile",
     "name" : "InputWorkBasedTours",     
     "filename" : cube___WORK_BASED_TOUR_TIME_OF_DAY_CHOICE___, 
     "columns" : [
                     "personId",
                     "hhId",
                     "persTourId",  
                     "tourPurp",
                     "arrival",
                     "departure",
                     "homeZoneId",
                     "destZoneId",
                     "origZoneId",
                     "parArrive",
                     "parDepart",
                    ],
     "deferredLoad": True
    },

    {"type" : "dbffile",
     "name" : "InputWorkTourModes",     
     "filename" : cube___WORK_BASED_TOUR_MODE_CHOICE___, # file paths MUST BE RAW strings (preceded by 'r')
     "columns" : [
                      "personId",   # part 1 of tour pk, for individual tours would be same as person id
                      "persTourId",
                      "homeZoneId", # for chunking
                      "tourMode"    # numerical value of TourMode enum 
                    ],
     "deferredLoad": True
     },

    {"type" : "dbffile",
     "name" : "Stops",     
     "filename" : cube___STOP_DESTINATION_CHOICE___, # file paths MUST BE RAW strings (preceded by 'r')
     "columns" : [
                "hhzon",
                "hhinc5s",
                "hhid",
                "personId",
                "personType",
                "tourId",
                "tourPurpose",
                "stopId" ,
                "halfTour",
                "purpose",
                "destZone",
                "time",
                "distance",
                 ],
     "deferredLoad": True
     },

    {"type" : "dbffile",
     "name" : "SchoolEscortStops",     
     "filename" : cube___SCHOOL_ESCORT_STOPS___, # file paths MUST BE RAW strings (preceded by 'r')
     "columns" : [
                "hhzon",
                "hhinc5s",
                "hhid",
                "personId",
                "personType",
                "tourId",
                "tourPurp",
                "stopId" ,
                "halfTour",
                "purpose",
                "destZone",
                "time" 
                 ],
     "deferredLoad": True
     },

 
     # not used downstream
    {"type" : "dbffile",
     "isOutput": "true",
     "name" : "OutputStops",     
     "filename" : cube___STOPS_WITH_TOUR_OFFSET_TIMES___, # file paths MUST BE RAW strings (preceded by 'r')
     "parameters" : [
                       [ "hh zone", "hhzon"],
                       [ "hh inc 5 segments", "hhinc5s"],
                       [ "hhid", "hhid"],
                       [ "Person id", "personId"],
                       [ "Person Type", "personType"],
                       [ "tour", "tourId"],
                       [ "tour purpose", "tourPurpose"],
                       [ "stop id", "stopId" ],
                       [ "half tour number", "halfTour"],
                       [ "stop purpose", "purpose"],
                       [ "destination zone", "destZone"],
                       [ "@stop time", "time" ], 
                       [ "stop distance", "distance"],
                       [ "relative ToD difference from tour", "trToDDiff"],
                    ]
     },

    {"type" : "dbffile",
     "isOutput": "true",
     "name" : "OutputTrips",     
     "filename" : cube___TRIP_TIME_OF_DAY___, # file paths MUST BE RAW strings (preceded by 'r')
     "parameters" : [
                       [ "hh zone", "hhzon"],
                       [ "hhid", "hhid"],
                       [ "Person id", "personId"],
                       [ "Person Type", "personType"],
                       [ "person type if escorted", "escPrsType"],
                       [ "tour", "tourId"],
                       [ "tour purpose", "tourPurp"],
                       [ "tour mode", "tourMode"],
                       [ "stop id", "stopId" ],
                       [ "half tour number", "halfTour"],
                       [ "stop purpose", "purpose"],
                       [ "origin zone", "origZone"],
                       [ "destination zone", "destZone"],
                       [ "origin time", "origTime"],
                       [ "destination time", "destTime"],
                       [ "distance", "distance"],
                       [ "duration", "duration"],
                    ]
     },


]

from MatrixRef1Dist import matrixReferences
