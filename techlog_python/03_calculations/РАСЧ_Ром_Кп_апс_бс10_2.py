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
#Description:Description
ASP = Variable("Rom-77R", "LQC", "td_ASP_TL", "Spontaneous Potential Alpha", "v/v")
parameterDict.update({'ASP' : Parameter(name='ASP',bname='asp',type='Variable',family='Spontaneous Potential Alpha',measurement='',unit='v/v',value='Rom-77R.LQC.td_ASP_TL',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:phit
#Family:Porosity
#Unit:v/v
#Mode:Out
#Description:Description
#Format:auto
PHIT = Variable("Rom-77R", "LQC", "PHIT", "Porosity", "v/v")
PHIT.setGroupName("recalc")
parameterDict.update({'PHIT' : Parameter(name='PHIT',bname='phit',type='Variable',family='Porosity',measurement='',unit='v/v',value='Rom-77R.LQC.PHIT',mode='Out',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})

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
	phit = MissingValue
	if MissingValue not in [asp] :
		### Automatic Generation Loop End ###
		#phit=(9.7405+1105.8346 * asp - 2059.6323 * (asp**2) + 2164.69 * (asp**3) - 803.464 * (asp**4)) ** 0.5
		phit =20.1 * asp ** 0.27
		
	#if (H>K_BS && H <= K_ACH)
	        #{ RV=0.13;APP=0.896; M=1.8653; APN=1.044;   N=1.6504;};
	    #//#KPO=(9.7405+1105.8346* #APS-2059.6323* (#APS^2)+2164.69*(#APS^3)-803.464*(#APS^4)) ^0.5;
	    #//#KPR=10^(0.54323-2.50481*(1.01- #APS) ^0.5 +0.00542*( #KPO^2));
	       #*KVO=10^(-0.3123-7.25317*(((*KPO+ *CGL)/100)^2)+5.73252*(*CGL/100))-0.05; 
	       #*KVO=100* *KVO;
	       #*RGR=(-0.0271**KPO^2 - (0.7826**KPO)+2.5702); 
	                                                        
	#if(H>K_ACH && H <= K_YUS)    /* До кровли АЧ */
	       #{ RV=0.12;APP=2.5275; M=1.4245; APN=0.9892; N=1.5367;};  
	
	#if (H >K_YUS)                /* До кровли ЮС */        
	      #{ RV=0.07;APP=1.4999;  M=1.558;  APN=0.9868;  N=1.6495;}; 
	     
	   #if(*KPO<=2.0) *KPO=2.3; 
	
	   #*RVP= APP*RV*((*KPO/100)^(-M));    
	   #if (*RT/ *RVP>=1.0) *KV=100*(APN**RVP/ *RT)^(1/N);
	
	
	#БС9-10	
	#Кпэф=1.1796*Кпд+3.8627	
	#Кпэф=2.31*Кпск^(-1.35)*Кп^2.93 / Кпэф=1.7391*Кп-20.609	
	#Кпр=10^(0.93*Кп^1.71*Кпск^(-1)-4.3)+0.045 / Кпр=10^(0.0372*Кп^1.71-4.3)+0.045	
	#Кво=1-3.4*Кп^2.4 / [Кп*Кпск^0.68]	
	#РП =3980*Кп**-1.81	
	#РН = 3810*Кв**-1.79	
	#Кв.кр=265*Кп**0.51	
	#Кп =20.1 * Апс**0.27	
	#плотн.=2.7091-0.0189*Кп	
	#Кп=1.27*Апс**0.27*W0.921	
	#Кп=0.08*DT*Апс0.29	
	#3.9	
	#0.27	
	#УЭСгр=9-0.1*Кп	
	#УЭСв=-0.109*ln(Набс)+1.0012	
	
	### Begin Automatic Generation EndLoop ###
	PHIT.setValue(loopIterator, phit)
PHIT.save(True)
### Automatic Generation EndLoop End ###
