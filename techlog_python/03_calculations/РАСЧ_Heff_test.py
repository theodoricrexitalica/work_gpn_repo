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
#BName:lit
#Family:Net Rock Flag
#Unit:unitless
#Mode:In
#Description:
Lit_flag = Variable("Sut-7350", "PT_RIGIS_gbd", "lit", "Net Rock Flag", "unitless")
parameterDict.update({'Lit_flag' : Parameter(name='Lit_flag',bname='lit',type='Variable',family='Net Rock Flag',measurement='',unit='unitless',value='Sut-7350.PT_RIGIS_gbd.lit',mode='In',description='',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:h_eff
#Family:Thickness
#Unit:m
#Mode:Out
#Description:
#Format:auto
Heff_gbd = Variable("Sut-7350", "PT_RIGIS_gbd", "Heff_raw", "Thickness", "m")
parameterDict.update({'Heff_gbd' : Parameter(name='Heff_gbd',bname='h_eff',type='Variable',family='Thickness',measurement='',unit='m',value='Sut-7350.PT_RIGIS_gbd.Heff_raw',mode='Out',description='',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})

__author__ = """Taras DOLGUSHIN (Dolgushin.TYu)"""
__date__ = """2021-09-22"""
__version__ = """1.0"""
__pyVersion__ = """3"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""
__applyMode__ = """0"""
__awiEngine__ = """v2"""
__layoutTemplateMode__ = """"""
__includeMissingValues__ = """True"""
__keepPreviouslyComputedValues__ = """True"""
__areInputDisplayed__ = """True"""
__useMultiWellLayout__ = """True"""
__idForHelp__ = """"""
__executionGranularity__ = """full"""
#DeclarationsEnd
cc = 0
### Begin Automatic Generation Loop [LOOP_INV_MVTEST:]###
loopSize = Lit_flag.referenceSize()
loopRange = range(loopSize)
for loopIterator in reversed(loopRange):
	datasetIterator = loopIterator
	lit = Lit_flag.value(loopIterator)
	h_eff = MissingValue
	if MissingValue not in [lit] :
		### Automatic Generation Loop End ###
		if lit == 1:
			cc +=1
		h_eff = cc
	### Begin Automatic Generation EndLoop ###
	Heff_gbd.setValue(loopIterator, h_eff)
Heff_gbd.save(True)
### Automatic Generation EndLoop End ###
