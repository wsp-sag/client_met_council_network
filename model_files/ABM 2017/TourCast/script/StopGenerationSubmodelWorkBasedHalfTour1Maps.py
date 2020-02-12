durableCoeffMap = {
       "Household" : [
                      [3, 0, 2]
                     ],
}

transientCoeffMap = {
        "Constants" : [
                        [0, 0, 1]

                      ],
         "Person" : [
                        [3, 1, 2]
                    ],
"TourLevelOfService" : [
						[0, 3, 1],
                ],
         "Tour" : [
						[1, 4, 2],
						[5, 6, 3]
                   ],                     
}
#segmentDefinitions = [
#  friendly name     , input data ref, offset in input, range of values (order relates to coeff order in segmentCoeffMap)
#{'Name': 'Tour Type', 'DataRef': 'Tour','Offset': 0, 'DataRange': [2,8]},
#]
