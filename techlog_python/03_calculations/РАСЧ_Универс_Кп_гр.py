from math import *
from TechlogMath import *
from operator import *
import sys
if sys.version_info[0]==3:
    from six.moves import range

PI     = 3.14159265358979323846
PIO2   = 1.57079632679489661923
PIO4   = 7.85398163397448309616E-1
SQRT2  = 1.41421356237309504880
SQRTH  = 7.07106781186547524401E-1
E      = exp(1)
LN2    = log(2)
LN10   = log(10)
LOG2E  = 1.4426950408889634073599
LOG10E = 1.0 / LN10
MissingValue = -9999
def iif(condition, trueResult=MissingValue, falseResult=MissingValue):
	if condition:
		return trueResult
	else:
		return falseResult

#Declarations
#The dictionary of parameters v2.0
#name,bname,type,family,measurement,unit,value,mode,description,group,min,max,list,enable,iscombocheckbox,isused
parameterDict = {}
try:
	if Parameter:
		pass
except NameError:
	class Parameter:
		def __init__(self, **d):
			pass
#Type:Variable
#BName:kpo
#Family:Porosity
#Unit:%
#Mode:In
#Description:
KPO = Variable("well", "dataset", "", "Porosity", "%")
parameterDict.update({'KPO' : Parameter(name='KPO',bname='kpo',type='Variable',family='Porosity',measurement='',unit='%',value='Rom-77R..KPO',mode='In',description='',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:%
kpo_gr_unit = "%"
#Measurement:Porosity
kpo_gr_measurement = "Porosity"
#Mode:In
#Description:
#Minimum:
#Maximum:
#List:
kpo_gr = 14
parameterDict.update({'kpo_gr' : Parameter(name='kpo_gr',bname='',type='Number',family='',measurement='Porosity',unit='%',value='14',mode='In',description='',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:lit
#Family:Net Rock Flag
#Unit:unitless
#Mode:Out
#Description:
#Format:auto
LIT = Variable("Rom-77R", "LQC", "lit", "Net Rock Flag", "unitless")
LIT.setGroupName("recalc")
parameterDict.update({'LIT' : Parameter(name='LIT',bname='lit',type='Variable',family='Net Rock Flag',measurement='',unit='unitless',value='Rom-77R.LQC.lit',mode='Out',description='',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})

__version__ = """1.0"""
__pyVersion__ = """3"""
__group__ = """recalc"""
__suffix__ = """"""
__prefix__ = """td_"""
__applyMode__ = """0"""
__awiEngine__ = """v1"""
__layoutTemplateMode__ = """"""
__includeMissingValues__ = """True"""
__keepPreviouslyComputedValues__ = """True"""
__areInputDisplayed__ = """True"""
__useMultiWellLayout__ = """True"""
__idForHelp__ = """"""
__executionGranularity__ = """full"""
#DeclarationsEnd
### Begin Automatic Generation Loop [LOOP_MVTEST:]###
loopSize = KPO.referenceSize()
loopRange = range(loopSize)
for loopIterator in loopRange:
	datasetIterator = loopIterator
	kpo = KPO.value(loopIterator)
	lit = MissingValue
	if MissingValue not in [kpo] :
		### Automatic Generation Loop End ###
		if kpo >= kpo_gr:
			lit = 1
		else:
			lit = 0
		
	### Begin Automatic Generation EndLoop ###
	LIT.setValue(loopIterator, lit)
LIT.save(True)
### Automatic Generation EndLoop End ###
