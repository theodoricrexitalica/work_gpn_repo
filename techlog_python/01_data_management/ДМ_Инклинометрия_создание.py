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
__date__ = """2021-10-26"""
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
#Скрипт создают копию датасета с ВэллХэдом и добавляет туда зенит и азимут с нулями
list = ["KB", "Pad", "X-Coord", "Y-Coord"]
for well in db.selectedWellList():
	if db.datasetExists(well, "inclination"):
		print(well, "inclination OK")
		pass
	else:
		ds = "WH"
		db.variableCreate(well, ds, "INC", 1)
		db.variableCreate(well, ds, "AZI", 1)
		inc = db.variableLoad(well, ds, "INC")
		azi = db.variableLoad(well, ds, "AZI")
		inc = [i==0 for i in inc]
		azi = [i==0 for i in azi]
		db.variableSave(well, ds, "INC", "Hole Deviation", "deg", inc)
		db.variableSave(well, ds, "AZI", "Hole Azimuth", "deg", inc)
		if not db.datasetExists(well, "inclination"):
			db.datasetDuplicate(well, ds, well, "inclination")
		else:
			print(well, "inclination exist")
		for i in db.variableList(well, "inclination"):
				if i in list:
					db.variableDelete(well, "inclination", i, 0)
		elev = db.variableLoad(well, "WH", "KB")[0]
		db.wellPropertyChange(well, "Elevation", str(elev), "m", "WH.KB") 
		print(well, "inclination DONE")
	
	
