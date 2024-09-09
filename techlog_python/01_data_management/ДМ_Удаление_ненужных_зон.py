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
__date__ = """2021-09-17"""
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
#Удаление зон с индексами _К и _BOT
db.currentChange("import")
for well in db.selectedWellList():
	ds_init = "ZONES_kra"
	ds = db.datasetDuplicate(well, ds_init, well, "ZON")
	ds_source = db.datasetRename(well, ds_init, ds_init + "_orig")
	md = db.variableLoad(well, ds, "MD")
	zones = db.variableLoad(well, ds, "ZONES")
	md_k = []
	md_bot = []
	zones_k = []
	zones_bot = []
	#for i in range(len(zones)):
		#print(zones[i])
		#if not "_K" in zones[i]:
			#md_k.append(md[i])
			#zones_k.append(zones[i])
	#print(md_k)
	#print(zones_k)
	for j in range(len(md)):
		#print(zones[j])
		if "_TOP_S" in zones[j]:
			md_bot.append(md[j])
			zones_bot.append(zones[j])
	#print(md_bot)
	#print(zones_bot)
			
	db.datasetCreate(well, ds_init, "MD", "Measured Depth", "m", md_bot)
	db.variableSave(well, ds_init, "ZONES", None, "unitless", zones_bot)
	db.datasetTypeChange(well, ds_init, "interval")
	db.datasetDelete(well, "ZON")
