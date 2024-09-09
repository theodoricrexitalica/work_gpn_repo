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
#BName:phit
#Family:Porosity
#Unit:%
#Mode:In
#Description:
PHIT = Variable("Rom-77R", "LQC", "td_PHIT_v2", "Porosity", "%")
parameterDict.update({'PHIT' : Parameter(name='PHIT',bname='phit',type='Variable',family='Porosity',measurement='',unit='%',value='Rom-77R.LQC.td_PHIT_v2',mode='In',description='',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable Optional
#BName:vsh
#Family:Shale Volume
#Unit:%
#Mode:In
#Description:
VSH = Variable("Rom-77R", "LQC", "td_VSH", "Shale Volume", "%")
parameterDict.update({'VSH' : Parameter(name='VSH',bname='vsh',type='Variable Optional',family='Shale Volume',measurement='',unit='%',value='Rom-77R.LQC.td_VSH',mode='In',description='',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:swir
#Family:Irreducible Water Saturation
#Unit:%
#Mode:Out
#Description:
#Format:auto
SWIR = Variable("Rom-77R", "LQC", "SWIR", "Irreducible Water Saturation", "%")
SWIR.setGroupName("recalc")
parameterDict.update({'SWIR' : Parameter(name='SWIR',bname='swir',type='Variable',family='Irreducible Water Saturation',measurement='',unit='%',value='Rom-77R.LQC.SWIR',mode='Out',description='',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})

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
loopSize = PHIT.referenceSize()
loopRange = range(loopSize)
for loopIterator in loopRange:
	datasetIterator = loopIterator
	phit = PHIT.value(loopIterator)
	vsh = VSH.value(loopIterator)
	swir = MissingValue
	if MissingValue not in [phit, vsh] :
		### Automatic Generation Loop End ###
		swir=0.028 * phit ** 3 - 1.36 * phit ** 2 + 15.2 * phit + 45
		
		
	#F_935PL
	#7.KVO_KV1_KV2_2015.f
	#if (H>=BP7 && H<ACH)
	#{
	#*KVO=0.028* *KPO^3-1.36* *KPO^2+15.2* *KPO+45;
	#*KVK=265* *KPO^(-0.51);
	#*KV1=0.5*(905.3* *KPO^(-1.0)+ *KVK); //  Н--Н+В
	#*KV2=0.5*(118* *KPO^(-0.19)+ *KVK);  //  В--В+Н 
	#}
	### Begin Automatic Generation EndLoop ###
	SWIR.setValue(loopIterator, swir)
SWIR.save(True)
### Automatic Generation EndLoop End ###
