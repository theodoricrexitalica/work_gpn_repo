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
#BName:sp
#Family:Spontaneous Potential
#Unit:mV
#Mode:In
#Description:Description
SP = Variable("165k14", "LQC", "SP", "Spontaneous Potential", "mV")
parameterDict.update({'SP' : Parameter(name='SP',bname='sp',type='Variable',family='Spontaneous Potential',measurement='',unit='mV',value='165k14.LQC.SP',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:asp
#Family:Spontaneous Potential Alpha
#Unit:v/v
#Mode:Out
#Description:Description
#Format:auto
ASP = Variable("165k14", "LQC", "ASP_TL", "Spontaneous Potential Alpha", "v/v")
ASP.setGroupName("recalc")
parameterDict.update({'ASP' : Parameter(name='ASP',bname='asp',type='Variable',family='Spontaneous Potential Alpha',measurement='',unit='v/v',value='165k14.LQC.ASP_TL',mode='Out',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:mV
SP_sand_unit = "mV"
#Measurement:
SP_sand_measurement = ""
#Mode:In
#Description:Description
#Minimum:
#Maximum:
#List:
SP_sand = 70
parameterDict.update({'SP_sand' : Parameter(name='SP_sand',bname='',type='Number',family='',measurement='',unit='mV',value='70',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:mV
SP_shale_unit = "mV"
#Measurement:
SP_shale_measurement = ""
#Mode:In
#Description:Description
#Minimum:
#Maximum:
#List:
SP_shale = 170
parameterDict.update({'SP_shale' : Parameter(name='SP_shale',bname='',type='Number',family='',measurement='',unit='mV',value='170',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})

__author__ = """Alexey LUBINETS (alubinets)"""
__date__ = """2011-01-26"""
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
### Begin Automatic Generation Loop ###
loopSize = SP.referenceSize()
loopRange = range(loopSize)
for loopIterator in loopRange:
	datasetIterator = loopIterator
	sp = SP.value(loopIterator)
	asp = MissingValue
	### Automatic Generation Loop End ###
	if sp == MissingValue or SP_shale == MissingValue or SP_sand==MissingValue or SP_sand == SP_shale:
		asp = MissingValue
	else:
		asp = (SP_shale - sp)/(SP_shale - SP_sand)
		asp = limitValue(asp,0,1)
	### Begin Automatic Generation EndLoop ###
	ASP.setValue(loopIterator, asp)
ASP.save(True)
### Automatic Generation EndLoop End ###
