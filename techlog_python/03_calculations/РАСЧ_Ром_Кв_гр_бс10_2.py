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
#Type:Variable
#BName:sw_1
#Family:Cutoff 1 Sw
#Unit:%
#Mode:Out
#Description:
#Format:auto
SW_1 = Variable("Rom-77R", "LQC", "SW_1", "Cutoff 1 Sw", "%")
SW_1.setGroupName("recalc")
parameterDict.update({'SW_1' : Parameter(name='SW_1',bname='sw_1',type='Variable',family='Cutoff 1 Sw',measurement='',unit='%',value='Rom-77R.LQC.SW_1',mode='Out',description='',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:sw_owc
#Family:Cutoff owc Sw
#Unit:%
#Mode:Out
#Description:
#Format:auto
SW_owc = Variable("Rom-77R", "LQC", "SW_owc", "Cutoff owc Sw", "%")
SW_owc.setGroupName("recalc")
parameterDict.update({'SW_owc' : Parameter(name='SW_owc',bname='sw_owc',type='Variable',family='Cutoff owc Sw',measurement='',unit='%',value='Rom-77R.LQC.SW_owc',mode='Out',description='',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:sw_2
#Family:Cutoff 2 Sw
#Unit:%
#Mode:Out
#Description:
#Format:auto
SW_2 = Variable("Rom-77R", "LQC", "SW_2", "Cutoff 2 Sw", "%")
SW_2.setGroupName("recalc")
parameterDict.update({'SW_2' : Parameter(name='SW_2',bname='sw_2',type='Variable',family='Cutoff 2 Sw',measurement='',unit='%',value='Rom-77R.LQC.SW_2',mode='Out',description='',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})

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
	sw_1 = MissingValue
	sw_owc = MissingValue
	sw_2 = MissingValue
	if MissingValue not in [phit] :
		### Automatic Generation Loop End ###
		sw_owc = 265* phit ** (-0.51)
		sw_1 = 0.5 * (905.3 * phit ** (-1.0) + sw_owc)
		sw_2 = 0.5 * (118 * phit ** (-0.19) + sw_owc)
	
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
	SW_1.setValue(loopIterator, sw_1)
	SW_owc.setValue(loopIterator, sw_owc)
	SW_2.setValue(loopIterator, sw_2)
SW_1.save(True)
SW_owc.save(True)
SW_2.save(True)
### Automatic Generation EndLoop End ###
