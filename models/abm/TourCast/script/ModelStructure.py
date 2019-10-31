import sys
import os
import json
import ModelStructureJsonEncoder
import Globals

class ModelStructure:
    """load up model structures from a python configuration file"""
    
    fileName=None  #name of configuration module (without .py), also used as output file name
    instantiationType=None  
    modelComponentName=None
    numberOfZones = Globals.numberOfZones
    randomSeed=None
    dataReferences= None
    matrixReferences=None
    matrixWriterReferences=None
    altIntrinsicValues=None
    altNames=None
    logitType=None
    altThetas=None
    altSpecificConsts=None
    parameters=None
    nestList=None
    durableCoeffs=None
    durableCoeffMap=None #dictionary of string, 2D array of int
    transientCoeffs=None
    transientCoeffMap=None #dictionary of string, 2D array of int
    segmentDefinitions=None #array of dictionary of string,object 
    segmentCoeffMap=None #array of dictionary

    sizeFunction=None #dictionary of string, object
    sizeFunctionDurableCoeffMap=None #same format as durableCoeffMap: dictionary of string, 2D array of int
    sizeFunctionTransientCoeffMap=None #same format as transientCoeffMap: dictionary of string, 2D array of int
    sizeFunctionSegmentDefinitions = None # same format as segmentDefinitions
    sizeFunctionSegmentCoeffMap=None # same format as segmentCoeffMap

    subModels=None # multimodelcomponent only 

    # TimeOfDay components
    arrivalConsts=None
    departureConsts=None
    durationConsts=None

    arrivalPivot=None
    durationPivot=None

    shiftCoeffs=None
    shiftCoeffMap=None
    tourCoeffs=None
    tourCoeffMap=None
    derivedValueCoeffs=None
    derivedValueCoeffMap=None

    congestionShifts=None
    autoTotGenTimeCoeff=None

    # School Escorting components
    outboundCoeffs=None
    outboundCoeffMap=None
    inboundCoeffs=None
    inboundCoeffMap=None
    outInCoeffs=None
    outInCoeffMap=None
    
    # Both
    valueOfTime=None
    outOfVehicleWeight=None

    def __init__(self, fileName):
        self.fileName = fileName        
        print "initializing model structure with {0}".format(fileName)

    def load_config(self):
        # fileName is full path so we have to split and tell python where to import from
        head, tail = os.path.split(self.fileName)
        sys.path.append(head)
        module = __import__(tail)
        if hasattr(module, "randomSeed"):
            self.randomSeed = module.randomSeed
        self.instantiationType = "ModelComponent"
        if hasattr(module, "instantiationType"):
            self.instantiationType = module.instantiationType      
        print "instantiationType= {0}".format(self.instantiationType)
        self.modelComponentName = module.modelComponentName

        if hasattr(module, "altThetas"):
            self.altThetas = module.altThetas
        if hasattr(module, "altSpecificConsts"):
            self.altSpecificConsts = module.altSpecificConsts
        if hasattr(module, "parameters"):
            self.parameters = module.parameters
        if hasattr(module, "nestList"):
            self.nestList = module.nestList
        if self.instantiationType == "ModelComponent":
            self.logitType = module.logitType
            self.altIntrinsicValues = module.altIntrinsicValues
            self.altNames = module.altNames
            self.durableCoeffs = module.durableCoeffs
            self.durableCoeffMap = module.durableCoeffMap
            self.transientCoeffs = module.transientCoeffs
            self.transientCoeffMap = module.transientCoeffMap
        if self.instantiationType == "MultiModelComponent":
            self.subModels = module.subModels

        if self.instantiationType == "TimeOfDayComponent":
            self.arrivalConsts = module.arrivalConsts
            self.departureConsts = module.departureConsts
            self.durationConsts = module.durationConsts
            self.shiftCoeffs = module.shiftCoeffs
            self.shiftCoeffMap = module.shiftCoeffMap
            self.tourCoeffs = module.tourCoeffs
            self.tourCoeffMap = module.tourCoeffMap
            if hasattr(module, "derivedValueCoeffs"):
                self.derivedValueCoeffs = module.derivedValueCoeffs
                self.derivedValueCoeffMap = module.derivedValueCoeffMap
            self.congestionShifts = module.congestionShifts
            self.autoTotGenTimeCoeff = module.autoTotGenTimeCoeff
            self.valueOfTime = module.valueOfTime
            self.outOfVehicleWeight = module.outOfVehicleWeight
            self.arrivalPivot = module.arrivalPivot
            self.durationPivot = module.durationPivot

        if self.instantiationType == "SchoolEscortComponent":
            self.logitType = module.logitType
            self.altIntrinsicValues = module.altIntrinsicValues
            self.outboundCoeffs = module.outboundCoeffs
            self.outboundCoeffMap = module.outboundCoeffMap
            self.inboundCoeffs = module.inboundCoeffs
            self.inboundCoeffMap = module.inboundCoeffMap
            self.outInCoeffs = module.outInCoeffs
            self.outInCoeffMap = module.outInCoeffMap
            self.valueOfTime = module.valueOfTime
            self.outOfVehicleWeight = module.outOfVehicleWeight

        self.dataReferences = module.dataReferences
        
        if hasattr(module, "matrixReferences"):
            self.matrixReferences = module.matrixReferences
        if hasattr(module, "matrixWriterReferences"):
            self.matrixWriterReferences = module.matrixWriterReferences
        if hasattr(module, "segmentDefinitions"):
            self.segmentDefinitions = module.segmentDefinitions
            self.segmentCoeffMap = module.segmentCoeffMap
        if hasattr(module, "sizeFunction"):  # this is an import
            self.sizeFunction = module.sizeFunction.sizeFunction
            self.sizeFunctionDurableCoeffMap = module.sizeFunction.sizeFunctionDurableCoeffMap
            self.sizeFunctionTransientCoeffMap = module.sizeFunction.sizeFunctionTransientCoeffMap
            if hasattr(module.sizeFunction,"sizeFunctionSegmentDefinitions"):
                self.sizeFunctionSegmentDefinitions = module.sizeFunction.sizeFunctionSegmentDefinitions
                self.sizeFunctionSegmentCoeffMap = module.sizeFunction.sizeFunctionSegmentCoeffMap
                           
    def dump(self):
        """for debugging print out contents (please modify to include structures as needed)"""
        return "dump disabled for now"
#    (
#            "alternative names and values:\n" +
#            str(zip(self.altNames, self.altIntrinsicValues)) + "\n" + 
#            "durable coefficient vectors:\n" +
#            str(self.durableCoeffs) + "\n" +
#            "transient coefficient vectors:\n" +
#            str(self.transientCoeffs) + "\n" +
#            "data References:\n" +
#           str(self.dataReferences) + "\n" +
#            "Some structures are not shown; add them as needed"
#            )
            

#    def get_altValues(self):
#        """intrinsic values of alternatives"""
#        return self.altValues

    def export_json(self, path):
        """Write model structure in json notation to file readable by C#"""
        dest = path + ".json"
        print "writing {0} contents to {1}".format(self.fileName, dest)
        with open(dest, 'w') as f:
            f.write(json.dumps(self, cls=ModelStructureJsonEncoder.ModelStructureJsonEncoder))
        return dest



