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
__date__ = """2021-05-30"""
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
#Переименовать переменную tvdss согласно переменной с АО в датасете
#Внимательно контролировтаь альтитуду ротора
import TechlogDialogAdvanced as tda

db.currentChange("import")
tvdss = "Z"
for well in db.selectedWellList():
	for ds in db.datasetList(well):
		db.variableUnitChange(well, ds, "MD", "m")
		db.variableUnitChange(well, ds, "AZIM", "deg")
		db.variableUnitChange(well, ds, "AZIM_GN", "deg")
		db.variableUnitChange(well, ds, "AZIM_TN", "deg")
		db.variableUnitChange(well, ds, "INCL", "deg")
		db.variableUnitChange(well, ds, tvdss, "m")
		db.datasetRename(well,ds,"inclination")
		db.datasetTypeChange(well, ds, "trajectory")
		ds = "inclination"
		md = db.variableLoad(well, ds, db.referenceName(well,ds))
		if db.variableExists(well, ds, tvdss):
			z = db.variableLoad(well, ds, tvdss)
			elev = md[0] + z[0]
			print("well -", well,";",elev)
			db.wellPropertyChange(well, "Elevation", str(elev), "m", "md[0] + z[0]")
		else:
			dlg = tda.dialogAdvanced("DFE")
			dlg.addDoubleInput('dfe', 'DFE', 0, -2147483647, +2147483647, 2, 1, "help")
			dlg.execDialog()
			dfe = round(dlg.getDoubleInput('dfe'),1)
			elev = md[0] + dfe
			print("well -", well,";",elev)
			db.wellPropertyChange(well, "Elevation", str(elev), "m", "input")
	
	
