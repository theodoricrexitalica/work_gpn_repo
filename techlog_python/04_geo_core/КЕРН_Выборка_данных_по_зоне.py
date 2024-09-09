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
__date__ = """2022-03-09"""
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
zones = "ZONES"
target_zone = ['БП16-1-2_TOP_S', 'БП16-2_TOP_S', 'БП16-1-1_TOP_S']																#указать зоны/у для которой ищутся данные
#target_zone = ["Ач1_TOP_S"]																										
target_ds = "RCAL_bp16_all"																												#обязательно указать название датасета для выборки
list_zones_ref = []
for well in db.wellList():
	for ds in db.selectedDatasetList(well):
		zones = db.variableLoad(well, ds, zones)
		ref = db.variableLoad(well, ds, db.referenceName(well, ds))
		for i in range(len(ref)):
			if zones[i] in target_zone:
				list_zones_ref.append(ref[i])																							#формирование набора индексов для нового датасета
				
		db.datasetCreate(well, target_ds, "ID", "Reference", "unitless", list_zones_ref, "float")
		for var in db.variableList(well, ds):
			if var != "ID":
				db.variableCopy(well, ds, var, target_ds, var, "automatic", "project", "project", -1, 0, 1)	#копирование переменных в новый датасет
