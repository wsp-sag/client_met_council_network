####################################################################
# StopGenerationSubmodelCommon.py
# Common information for all submodels of the Stop Generation model
####################################################################

from Globals import *

# the name of the corresponding class on the C# side:
# this allows for multiple scripts targeting the same component
modelComponentName="StopGenerationSubmodel"

logitType="NestedLogit"

segmentDefinitions = []
segmentCoeffMap = []