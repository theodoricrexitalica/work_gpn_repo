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
#BName:rt
#Family:Formation Resistivity
#Unit:ohmm
#Mode:In
#Description:
RT = Variable("Rom-77R", "LQC", "RT", "Formation Resistivity", "ohmm")
parameterDict.update({'RT' : Parameter(name='RT',bname='rt',type='Variable',family='Formation Resistivity',measurement='',unit='ohmm',value='Rom-77R.LQC.RT',mode='In',description='',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:kpo
#Family:Porosity
#Unit:%
#Mode:In
#Description:
KPO = Variable("well", "dataset", "", "Porosity", "%")
parameterDict.update({'KPO' : Parameter(name='KPO',bname='kpo',type='Variable',family='Porosity',measurement='',unit='%',value='Rom-77R..KPO',mode='In',description='',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:lit
#Family:Net Rock Flag
#Unit:unitless
#Mode:In
#Description:
LIT = Variable("well", "dataset", "", "Net Rock Flag", "unitless")
parameterDict.update({'LIT' : Parameter(name='LIT',bname='lit',type='Variable',family='Net Rock Flag',measurement='',unit='unitless',value='Rom-77R..lit',mode='In',description='',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:unitless
a_unit = "unitless"
#Measurement:Coefficient
a_measurement = "Coefficient"
#Mode:In
#Description:
#Minimum:
#Maximum:
#List:
a = 1
parameterDict.update({'a' : Parameter(name='a',bname='',type='Number',family='',measurement='Coefficient',unit='unitless',value='1',mode='In',description='',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:unitless
m_unit = "unitless"
#Measurement:Coefficient
m_measurement = "Coefficient"
#Mode:In
#Description:
#Minimum:
#Maximum:
#List:
m = 2
parameterDict.update({'m' : Parameter(name='m',bname='',type='Number',family='',measurement='Coefficient',unit='unitless',value='2',mode='In',description='',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:unitless
n_unit = "unitless"
#Measurement:Coefficient
n_measurement = "Coefficient"
#Mode:In
#Description:
#Minimum:
#Maximum:
#List:
n = 2
parameterDict.update({'n' : Parameter(name='n',bname='',type='Number',family='',measurement='Coefficient',unit='unitless',value='2',mode='In',description='',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:ohmm
RV_unit = "ohmm"
#Measurement:Resistivity
RV_measurement = "Resistivity"
#Mode:In
#Description:
#Minimum:
#Maximum:
#List:
RV = 0.1
parameterDict.update({'RV' : Parameter(name='RV',bname='',type='Number',family='',measurement='Resistivity',unit='ohmm',value='0.1',mode='In',description='',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:sg
#Family:Hydrocarbon Saturation
#Unit:%
#Mode:Out
#Description:
#Format:auto
SG = Variable("Rom-77R", "LQC", "SG", "Hydrocarbon Saturation", "%")
SG.setGroupName("recalc")
parameterDict.update({'SG' : Parameter(name='SG',bname='sg',type='Variable',family='Hydrocarbon Saturation',measurement='',unit='%',value='Rom-77R.LQC.SG',mode='Out',description='',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})

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
loopSize = RT.referenceSize()
loopRange = range(loopSize)
for loopIterator in loopRange:
	datasetIterator = loopIterator
	rt = RT.value(loopIterator)
	kpo = KPO.value(loopIterator)
	lit = LIT.value(loopIterator)
	sg = MissingValue
	if MissingValue not in [rt, kpo, lit] :
		### Automatic Generation Loop End ###
		if lit == 1:
			rvp = a * RV * (( kpo / 100) ** (-m))
			if ( rt / rvp >= 1):
				kv = 100 * (rt / rvp) ** (- 1 / n)
				sg = 100 - kv
		else:
			sg = 0
	
	### Begin Automatic Generation EndLoop ###
	SG.setValue(loopIterator, sg)
SG.save(True)
### Automatic Generation EndLoop End ###
