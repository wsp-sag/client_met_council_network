import json
import ModelStructure

class ModelStructureJsonEncoder(json.JSONEncoder):
    """JSON encoder for ModelStructure objects"""
    def default(self, the_class):
        print "In custom encoder"
        if not isinstance (the_class, ModelStructure.ModelStructure):
            print "(0) can only encode ModelStructure type".format(__name__)
            return
        transientCoeffs = [[]]
        # doing these checks because it looks like zip will collapse an empty 2-d array to 1-d.  
        # NOTE, if there is a jagged array, this check will not catch it
        # added zip(*array) to transpose the 2-d array
        if the_class.transientCoeffs and (len(the_class.transientCoeffs[0]) > 0):
            transientCoeffs = zip(*the_class.transientCoeffs)
        durableCoeffs = [[]]
        if the_class.durableCoeffs and len(the_class.durableCoeffs[0]) > 0:
                durableCoeffs = zip(*the_class.durableCoeffs)
        # special case for school escorting, coeff arrays need to be transposed
        outboundCoeffs = [[]]
        inboundCoeffs = [[]]
        outInCoeffs = [[]]
        if the_class.instantiationType == "SchoolEscortComponent":
            if len(the_class.outboundCoeffs) > 1:
                outboundCoeffs = zip(*the_class.outboundCoeffs)
            if len(the_class.inboundCoeffs) > 1:
                inboundCoeffs = zip(*the_class.inboundCoeffs)
            if len(the_class.outInCoeffs) > 1:
                outInCoeffs = zip(*the_class.outInCoeffs)

        return {
                'configFileName': the_class.fileName,
                'instantiationType': the_class.instantiationType,
                'modelComponentName': the_class.modelComponentName,
                'numberOfZones': the_class.numberOfZones,
                'randomSeed': the_class.randomSeed,
                'logitType' : the_class.logitType,
                'nestList': the_class.nestList,
                'altIntrinsicValues': the_class.altIntrinsicValues,
                'altNames': the_class.altNames,
                'altThetas': the_class.altThetas,
                'altSpecificConsts' : the_class.altSpecificConsts,
                'parameters' : the_class.parameters,
                'durableCoeffs' : durableCoeffs,
                'durableCoeffMap' : the_class.durableCoeffMap,
                'transientCoeffs' : transientCoeffs,
                'transientCoeffMap' : the_class.transientCoeffMap,
                'dataReferences' : the_class.dataReferences,
                'matrixReferences' : the_class.matrixReferences,
                'matrixWriterReferences' : the_class.matrixWriterReferences,
                'segmentDefinitions' : the_class.segmentDefinitions,
                'segmentCoeffMap' : the_class.segmentCoeffMap,
                'sizeFunction'   : the_class.sizeFunction,
                'sizeFunctionDurableCoeffMap' : the_class.sizeFunctionDurableCoeffMap,
                'sizeFunctionTransientCoeffMap' : the_class.sizeFunctionTransientCoeffMap,
                'sizeFunctionSegmentDefinitions' : the_class.sizeFunctionSegmentDefinitions,
                'sizeFunctionSegmentCoeffMap' : the_class.sizeFunctionSegmentCoeffMap,
                'subModels' : the_class.subModels,
                # TimeOfDayComponent
                'arrivalConsts' : the_class.arrivalConsts,
                'departureConsts' : the_class.departureConsts,
                'durationConsts' : the_class.durationConsts,
                'arrivalPivot' : the_class.arrivalPivot,
                'durationPivot' : the_class.durationPivot,
                'shiftCoeffs' : the_class.shiftCoeffs,
                'shiftCoeffMap' : the_class.shiftCoeffMap,
                'tourCoeffs' : the_class.tourCoeffs,
                'tourCoeffMap' : the_class.tourCoeffMap,
                'derivedValueCoeffs' : the_class.derivedValueCoeffs,
                'derivedValueCoeffMap' : the_class.derivedValueCoeffMap,
                'congestionShifts' : the_class.congestionShifts,
                'autoTotGenTimeCoeff' : the_class.autoTotGenTimeCoeff,
                # SchoolEscortingComponent
                "outboundCoeffs" : outboundCoeffs,
                "outboundCoeffMap" : the_class.outboundCoeffMap,
                "inboundCoeffs" : inboundCoeffs,
                "inboundCoeffMap" : the_class.inboundCoeffMap,
                "outInCoeffs" : outInCoeffs,
                "outInCoeffMap" : the_class.outInCoeffMap,

                'valueOfTime' : the_class.valueOfTime,
                'outOfVehicleWeight' : the_class.outOfVehicleWeight
                }



