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
#BName:asp
#Family:Spontaneous Potential Alpha
#Unit:v/v
#Mode:In
#Description:
ASP = Variable("Rom-77R", "LQC", "td_ASP_TL", "Spontaneous Potential Alpha", "v/v")
parameterDict.update({'ASP' : Parameter(name='ASP',bname='asp',type='Variable',family='Spontaneous Potential Alpha',measurement='',unit='v/v',value='Rom-77R.LQC.td_ASP_TL',mode='In',description='',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:vsh
#Family:Shale Volume
#Unit:%
#Mode:Out
#Description:
#Format:auto
VSH = Variable("Rom-77R", "LQC", "VSH", "Shale Volume", "%")
VSH.setGroupName("recalc")
parameterDict.update({'VSH' : Parameter(name='VSH',bname='vsh',type='Variable',family='Shale Volume',measurement='',unit='%',value='Rom-77R.LQC.VSH',mode='Out',description='',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})

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
loopSize = ASP.referenceSize()
loopRange = range(loopSize)
for loopIterator in loopRange:
	datasetIterator = loopIterator
	asp = ASP.value(loopIterator)
	vsh = MissingValue
	if MissingValue not in [asp] :
		### Automatic Generation Loop End ###
		vsh=exp((4.3884136 + 4.1128605*asp)/ (1+3.2637743*asp)) 
		
		
	#if (H>K_BS && H<= K_ACH && #LOB!=6)
	        #{	*CGL=exp((4.3884136+4.1128605**APS)/ (1+3.2637743**APS));
	#//ACGL=-16.692; BCGL=24.66; 
	   #};                                 /* БС До кровли АЧ */
	### Begin Automatic Generation EndLoop ###
	VSH.setValue(loopIterator, vsh)
VSH.save(True)
### Automatic Generation EndLoop End ###
