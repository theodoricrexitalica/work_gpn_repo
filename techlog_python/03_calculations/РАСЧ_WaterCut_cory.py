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
#BName:perm
#Family:Permeability
#Unit:mD
#Mode:In
#Description:Description
Perm = Variable("Priob-88001", "ELAN", "PERM_TiCo_res_pet_leu", "Permeability", "mD")
parameterDict.update({'Perm' : Parameter(name='Perm',bname='perm',type='Variable',family='Permeability',measurement='',unit='mD',value='Priob-88001.ELAN.PERM_TiCo_res_pet_leu',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:soirr
#Family:Irreducible Oil Saturation
#Unit:v/v
#Mode:In
#Description:Description
Soirr = Variable("Priob-88001", "ELAN", "SOI", "Irreducible Oil Saturation", "v/v")
parameterDict.update({'Soirr' : Parameter(name='Soirr',bname='soirr',type='Variable',family='Irreducible Oil Saturation',measurement='',unit='v/v',value='Priob-88001.ELAN.SOI',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:swirr
#Family:Irreducible Water Saturation
#Unit:v/v
#Mode:In
#Description:Description
Swirr = Variable("Priob-88001", "ELAN", "SWI", "Irreducible Water Saturation", "v/v")
parameterDict.update({'Swirr' : Parameter(name='Swirr',bname='swirr',type='Variable',family='Irreducible Water Saturation',measurement='',unit='v/v',value='Priob-88001.ELAN.SWI',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:sw
#Family:Water Saturation
#Unit:v/v
#Mode:In
#Description:Description
Sw = Variable("Priob-88001", "ELAN", "KV", "Water Saturation", "v/v")
parameterDict.update({'Sw' : Parameter(name='Sw',bname='sw',type='Variable',family='Water Saturation',measurement='',unit='v/v',value='Priob-88001.ELAN.KV',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:cP
visc_o_unit = "cP"
#Measurement:Viscosity
visc_o_measurement = "Viscosity"
#Mode:In
#Description:Description
#Minimum:
#Maximum:
#List:
visc_o = 2.2
parameterDict.update({'visc_o' : Parameter(name='visc_o',bname='',type='Number',family='',measurement='Viscosity',unit='cP',value='2.2',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:cP
visc_w_unit = "cP"
#Measurement:Viscosity
visc_w_measurement = "Viscosity"
#Mode:In
#Description:Description
#Minimum:
#Maximum:
#List:
visc_w = 0.4
parameterDict.update({'visc_w' : Parameter(name='visc_w',bname='',type='Number',family='',measurement='Viscosity',unit='cP',value='0.4',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:unitless
sw_corr_unit = "unitless"
#Measurement:Coefficient
sw_corr_measurement = "Coefficient"
#Mode:In
#Description:Description
#Minimum:
#Maximum:
#List:
sw_corr = 0
parameterDict.update({'sw_corr' : Parameter(name='sw_corr',bname='',type='Number',family='',measurement='Coefficient',unit='unitless',value='0',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:unitless
swirr_corr_unit = "unitless"
#Measurement:Coefficient
swirr_corr_measurement = "Coefficient"
#Mode:In
#Description:Description
#Minimum:
#Maximum:
#List:
swirr_corr = 0
parameterDict.update({'swirr_corr' : Parameter(name='swirr_corr',bname='',type='Number',family='',measurement='Coefficient',unit='unitless',value='0',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:unitless
bo_unit = "unitless"
#Measurement:Coefficient
bo_measurement = "Coefficient"
#Mode:In
#Description:Description
#Minimum:
#Maximum:
#List:
bo = 1.1
parameterDict.update({'bo' : Parameter(name='bo',bname='',type='Number',family='',measurement='Coefficient',unit='unitless',value='1.1',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:unitless
krwe_unit = "unitless"
#Measurement:Coefficient
krwe_measurement = "Coefficient"
#Mode:In
#Description:Description
#Minimum:
#Maximum:
#List:
krwe = 1
parameterDict.update({'krwe' : Parameter(name='krwe',bname='',type='Number',family='',measurement='Coefficient',unit='unitless',value='1',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:unitless
nw_unit = "unitless"
#Measurement:Coefficient
nw_measurement = "Coefficient"
#Mode:In
#Description:Description
#Minimum:
#Maximum:
#List:
nw = 2.2
parameterDict.update({'nw' : Parameter(name='nw',bname='',type='Number',family='',measurement='Coefficient',unit='unitless',value='2.2',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:unitless
kroe_unit = "unitless"
#Measurement:Coefficient
kroe_measurement = "Coefficient"
#Mode:In
#Description:Description
#Minimum:
#Maximum:
#List:
kroe = 0.915
parameterDict.update({'kroe' : Parameter(name='kroe',bname='',type='Number',family='',measurement='Coefficient',unit='unitless',value='0.915',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:unitless
no_unit = "unitless"
#Measurement:Coefficient
no_measurement = "Coefficient"
#Mode:In
#Description:Description
#Minimum:
#Maximum:
#List:
no = 1.95
parameterDict.update({'no' : Parameter(name='no',bname='',type='Number',family='',measurement='Coefficient',unit='unitless',value='1.95',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:krw
#Family:Relative Water Permeability
#Unit:v/v
#Mode:Out
#Description:Description
#Format:auto
KRW = Variable("Priob-88001", "ELAN", "krw", "Relative Water Permeability", "v/v")
KRW.setGroupName("test")
parameterDict.update({'KRW' : Parameter(name='KRW',bname='krw',type='Variable',family='Relative Water Permeability',measurement='',unit='v/v',value='Priob-88001.ELAN.krw',mode='Out',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:kro
#Family:Relative Oil Permeability
#Unit:v/v
#Mode:Out
#Description:Description
#Format:auto
KRO = Variable("Priob-88001", "ELAN", "kro", "Relative Oil Permeability", "v/v")
KRO.setGroupName("test")
parameterDict.update({'KRO' : Parameter(name='KRO',bname='kro',type='Variable',family='Relative Oil Permeability',measurement='',unit='v/v',value='Priob-88001.ELAN.kro',mode='Out',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:wor
#Family:Ratio
#Unit:unitless
#Mode:Out
#Description:Description
#Format:auto
WOR = Variable("Priob-88001", "ELAN", "wor", "Ratio", "unitless")
WOR.setGroupName("test")
parameterDict.update({'WOR' : Parameter(name='WOR',bname='wor',type='Variable',family='Ratio',measurement='',unit='unitless',value='Priob-88001.ELAN.wor',mode='Out',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:wco
#Family:Water Cut
#Unit:unitless
#Mode:Out
#Description:Description
#Format:auto
WCO = Variable("Priob-88001", "ELAN", "WCO", "Water Cut", "unitless")
WCO.setGroupName("test")
parameterDict.update({'WCO' : Parameter(name='WCO',bname='wco',type='Variable',family='Water Cut',measurement='Coefficient',unit='unitless',value='Priob-88001.ELAN.WCO',mode='Out',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})

__author__ = """Taras DOLGUSHIN (SE64403)"""
__date__ = """2020-11-30"""
__version__ = """1.0"""
__pyVersion__ = """3"""
__group__ = """test"""
__suffix__ = """_test"""
__prefix__ = """"""
__applyMode__ = """1"""
__awiEngine__ = """v2"""
__layoutTemplateMode__ = """"""
__includeMissingValues__ = """True"""
__keepPreviouslyComputedValues__ = """True"""
__areInputDisplayed__ = """True"""
__useMultiWellLayout__ = """True"""
__idForHelp__ = """"""
__executionGranularity__ = """full"""
#DeclarationsEnd
### Begin Automatic Generation Loop ###
loopSize = Perm.referenceSize()
loopRange = range(loopSize)
for loopIterator in loopRange:
	datasetIterator = loopIterator
	perm = Perm.value(loopIterator)
	soirr = Soirr.value(loopIterator)
	swirr = Swirr.value(loopIterator)
	sw = Sw.value(loopIterator)
	krw = MissingValue
	kro = MissingValue
	wor = MissingValue
	wco = MissingValue
	### Automatic Generation Loop End ###
	#print(round(sw,2), loopIterator)
	if  sw < 1:
		sw = sw - sw_corr
		swirr = swirr - swirr_corr
		swirr = round(limitValue(swirr, 0, 1),4)
		sw = round(limitValue(sw, 0, 1),4)
		soirr = round(limitValue(soirr, 0, 1),4)
		krw = abs(krwe*((sw-swirr)/(1-swirr-soirr))**nw)
		krw =  limitValue(krw, 0.0001, 1)
		kro = abs(kroe*((1-sw-soirr)/(1-swirr-soirr))**no)
		kro = limitValue(kro, 0.0001, 1)
		kw = krw*perm
		ko = kro*perm
		wco = (kw/visc_w)*(1/((ko/visc_o)+(kw/visc_w)))
		if kro == 0.000001 or kro == MissingValue:
			wco = 1
		
	### Begin Automatic Generation EndLoop ###
	KRW.setValue(loopIterator, krw)
	KRO.setValue(loopIterator, kro)
	WOR.setValue(loopIterator, wor)
	WCO.setValue(loopIterator, wco)
KRW.save(True)
KRO.save(True)
WOR.save(True)
WCO.save(True)
### Automatic Generation EndLoop End ###
