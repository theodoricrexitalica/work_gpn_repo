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
#BName:phit
#Family:Porosity
#Unit:%
#Mode:In
#Description:
PHIT = Variable("Rom-77R", "LQC", "td_PHIT_v2", "Porosity", "%")
parameterDict.update({'PHIT' : Parameter(name='PHIT',bname='phit',type='Variable',family='Porosity',measurement='',unit='%',value='Rom-77R.LQC.td_PHIT_v2',mode='In',description='',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
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
RV = 0.13
parameterDict.update({'RV' : Parameter(name='RV',bname='',type='Number',family='',measurement='Resistivity',unit='ohmm',value='0.13',mode='In',description='',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
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
#RV=0.13;APP=0.896; M=1.8653; APN=1.044;   N=1.6504

### Begin Automatic Generation Loop [LOOP_MVTEST:]###
loopSize = RT.referenceSize()
loopRange = range(loopSize)
for loopIterator in loopRange:
	datasetIterator = loopIterator
	rt = RT.value(loopIterator)
	phit = PHIT.value(loopIterator)
	sg = MissingValue
	if MissingValue not in [rt, phit] :
		### Automatic Generation Loop End ###
		rvp = 0.955 * RV * (( phit / 100) ** (-1.81))
		if ( rt / rvp >= 1):
			sw = 100 * (rt / rvp) ** (- 1 / 1.79)
			sg = 100 - sw
		
	#F_935PL
	#6.KNG_crv_gis_2015_2.f
	#if (H>=BP && H<BP7){RV=0.12; A=1; B=1; m=1.7404; n=1.7709;}
	#if (H>=BP7 && H<ACH){ A=0.955; B=1.; m=1.81; n=1.79;}
	#if (H>=ACH && H<J1){RV=0.13; A=1.24; B=1.0176; m=1.73; n=1.4502;}
	#if (H>=J1){RV=0.07; A=1.096; B=0.9418; m=1.7366; n=1.8443;}
	
	              ##RVP=A*(pow(KP,-m))*RV;
	              ##KV=100*(#RT/B/(#RVP))^(-1/n);
	
	#//if(#LOB<6.5 || #LOB>12.5) #KV=100;
	#if(#NOB==7.0) #KV=100;
	##KNG=100-#KV;
	#if(#NOB==7) #KNG=0;
	#if(#NOB<0.1) #KNG=0;
	### Begin Automatic Generation EndLoop ###
	SG.setValue(loopIterator, sg)
SG.save(True)
### Automatic Generation EndLoop End ###
