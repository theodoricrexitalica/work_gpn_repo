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

__author__ = """Taras DOLGUSHIN (dolgushin.tyu)"""
__date__ = """2022-03-14"""
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
ds_lqc = 'LQC'
ds_zone = 'ZONES_gm'
zone = 'БС9-2-1+2_TOP_S'
cutoff = 12.8
for well in db.selectedWellList():
	if db.datasetExists(well, ds_zone) and  db.datasetExists(well, ds_lqc) and zone in db.variableLoad(well, ds_zone, 'ZONES'):
		var_name_ref = db.referenceName(well, ds_lqc)
		db.variableDuplicate(well, ds_lqc, var_name_ref, 'KPGR')
		md = db.variableLoad(well, ds_lqc, var_name_ref)
		kpgr_zero = db.variableLoad(well, ds_lqc, 'KPGR')
		for i in range(len(md)):
			kpgr_zero[i] = kpgr_zero[i] * 0
		db.variableSave(well, ds_lqc, 'KPGR', "Porosity", '%', kpgr_zero, 0, 'float')
		indice = db.datasetZoneIndice(well, ds_lqc, ds_zone, zone, 'Zone Name', 0)
		kpgr = db.variableLoad(well, ds_lqc, 'KPGR')
		for i in range(len(md))[indice[0]: indice[1] + 1]:
			kpgr[i] = cutoff
		print(well, 'kpgr is', db.variableSave(well, ds_lqc, 'KPGR', "Porosity", '%', kpgr, 0, 'float'))
	else:
		print(well, "ds_zone is None")
		pass
	
