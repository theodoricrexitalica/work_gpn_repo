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
#BName:rt_sh
#Family:Shallow Resistivity Hrz
#Unit:ohmm
#Mode:In
#Description:
RT_SH = Variable("Ety-3752G", "LQC", "RT_SH", "Shallow Resistivity Hrz", "ohmm")
parameterDict.update({'RT_SH' : Parameter(name='RT_SH',bname='rt_sh',type='Variable',family='Shallow Resistivity Hrz',measurement='',unit='ohmm',value='Ety-3752G.LQC.RT_SH',mode='In',description='',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:gr
#Family:Gamma Ray
#Unit:gAPI
#Mode:In
#Description:
GR = Variable("Ety-3752G", "LQC", "GR", "Gamma Ray", "gAPI")
parameterDict.update({'GR' : Parameter(name='GR',bname='gr',type='Variable',family='Gamma Ray',measurement='',unit='gAPI',value='Ety-3752G.LQC.GR',mode='In',description='',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:ohm.m
RT_cutoff_unit = "ohm.m"
#Measurement:Resistivity
RT_cutoff_measurement = "Resistivity"
#Mode:In
#Description:Description
#Minimum:
#Maximum:
#List:
RT_cutoff = 15
parameterDict.update({'RT_cutoff' : Parameter(name='RT_cutoff',bname='',type='Number',family='',measurement='Resistivity',unit='ohm.m',value='15',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:gAPI
GR_cutoff_max_unit = "gAPI"
#Measurement:Gamma_Ray
GR_cutoff_max_measurement = "Gamma_Ray"
#Mode:In
#Description:Description
#Minimum:
#Maximum:
#List:
GR_cutoff_max = 90
parameterDict.update({'GR_cutoff_max' : Parameter(name='GR_cutoff_max',bname='',type='Number',family='',measurement='Gamma_Ray',unit='gAPI',value='90',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:lit_hrz
#Family:Net Rock Flag
#Unit:unitless
#Mode:Out
#Description:
#Format:auto
LIT_HRZ = Variable("Ety-3752G", "LQC", "lit_hrz", "Net Rock Flag", "unitless")
parameterDict.update({'LIT_HRZ' : Parameter(name='LIT_HRZ',bname='lit_hrz',type='Variable',family='Net Rock Flag',measurement='',unit='unitless',value='Ety-3752G.LQC.lit_hrz',mode='Out',description='',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})

__author__ = """Taras DOLGUSHIN (dolgushin.tyu)"""
__date__ = """2022-09-28"""
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
### Begin Automatic Generation Loop [LOOP_MVTEST:]###
loopSize = RT_SH.referenceSize()
loopRange = range(loopSize)
for loopIterator in loopRange:
	datasetIterator = loopIterator
	rt_sh = RT_SH.value(loopIterator)
	gr = GR.value(loopIterator)
	lit_hrz = MissingValue
	if MissingValue not in [rt_sh, gr] :
		### Automatic Generation Loop End ###
		lit_hrz = 0
		if gr <= GR_cutoff_max and rt_sh <= RT_cutoff:
			lit_hrz = 1
	### Begin Automatic Generation EndLoop ###
	LIT_HRZ.setValue(loopIterator, lit_hrz)
LIT_HRZ.save(True)
### Automatic Generation EndLoop End ###
