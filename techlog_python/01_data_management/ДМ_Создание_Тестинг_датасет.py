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
list = [10, 20, 30, 40, 50]
zone_name =  "Testing"
zone_var = "Result"
db.currentChange("project")
for well in db.selectedWellList():
	#for ds in db.datasetList(well):
		#db.datasetRename(well, ds, "inclination")
	db.datasetCreate(well, zone_name, "MD", "Measured Depth", "m", list)
	db.datasetTypeChange(well, zone_name, "interval")
	db.variableCreate(well, zone_name, zone_var, 1)
	db.variableFamilyChange(well, zone_name, zone_var, "Open Hole Testing Interval")
	db.variableTypeChange(well,zone_name, zone_var, "RichText")
	db.variableUnitChange(well, zone_name, zone_var, "unitless")
	
	db.variableCreate(well, zone_name, "Qoil", 1)
	db.variableFamilyChange(well, zone_name, "Qoil", "Cumulative Oil Rate")
	db.variableTypeChange(well,zone_name, "Qoil", "TopBottomCurve")
	db.variableUnitChange(well, zone_name, "Qoil", "m3/d")
	
	db.variableCreate(well, zone_name, "Qwat", 1)
	db.variableFamilyChange(well, zone_name, "Qwat", "Cumulative Water Rate")
	db.variableTypeChange(well,zone_name, "Qwat", "TopBottomCurve")
	db.variableUnitChange(well, zone_name, "Qwat", "m3/d")
	
	
