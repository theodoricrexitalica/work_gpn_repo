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

__author__ = """Taras DOLGUSHIN (Dolgushin.TYu)"""
__date__ = """2021-06-03"""
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
import numpy as np
db.currentChange("import")
#for well in db.wellList():
depth_list = []
for well in db.selectedWellList():
	ds_list= db.datasetList(well)
#Поиск максимальное глубины для создания датасета GDB_LOGS
	for ds in ds_list:
		ind = ds_list.index(ds)
		ref_name = db.referenceName(well,ds)
		depth = db.variableLoad(well, ds, ref_name)[-1]
		depth_list.append(depth)
	dataset_depth = []
	max_depth = int(max(depth_list) + 1.1)
	for i in np.arange(0, max_depth, 0.1):
		dataset_depth.append(i)
#Создание датасета GDB_LOGS
	db.datasetCreate(well, "GDB_LOGS", "MD", "Measured Depth", "m", dataset_depth, "double")
#Копирование переменных из разных датасетов в GDB_LOGS
	for ds in ds_list:
		ind = ds_list.index(ds)
		var_list = db.variableList(well, ds, 0)
		for var in var_list:
			if var != "DEPT":
				db.variableCopy(well, ds,var, "GDB_LOGS", var + "_" + str(ind), "automatic", "import", "import", -1, 0, 0)
		if ds !=  "GDB_LOGS":
			db.datasetDelete(well,ds,1)
