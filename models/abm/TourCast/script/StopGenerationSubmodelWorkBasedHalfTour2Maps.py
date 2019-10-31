durableCoeffMap = {
       "Household" : [
                      [3, 0, 1]
                     ],
}

transientCoeffMap = {
        "Constants" : [
                        [0, 0, 1]

                      ],
         "Person" : [
                        [3, 1, 2]
                    ],
         "Day" : [
                        [3, 3, 1]
                    ],					
"TourLevelOfService" : [
						[0, 4, 1],
                ],
         "Tour" : [
						[1, 5, 1],
						[3, 6, 1],
						[10, 7, 1],
						[12, 8, 1],
                   ],                     
}

#segmentDefinitions = [
##  friendly name     , input data ref, offset in input, range of values (order relates to coeff order in segmentCoeffMap)
#{'Name': 'Tour Type', 'DataRef': 'Tour','Offset': 0, 'DataRange': [2,8,16]},
#{'Name': 'Work Tour', 'DataRef': 'Tour','Offset': 0, 'DataRange': [2]},
#]
#