durableCoeffMap = {
       "Household" : [
                      [2, 0, 1],
                      [4, 1, 2],
                     ],
}

transientCoeffMap = {
        "Constants" : [
                        [0,0,1]
                      ],
         "Person" : [
                     [1,1,2],
                     [4,3,4],					 
                    ],
         "Day" : [
                  [0,7,1],
                  [2,8,1],				  
				  [6,9,2],				  
                  [10,11,1],
                 ],
         "TourLevelOfService" : [
                                 [0,12,2],
                                ],
         "Tour" : [
				   [1,14,1],
				   [3,15,1],				   
                   [10,16,1],
				   [12,17,1],
				   [14,18,1],
				   [15,20,1]
                  ],            
         "StopsHalfTour1" : [
				   [0,19,1]
                  ],   				  
}
