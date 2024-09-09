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
__date__ = """2021-12-10"""
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
cutoff = "kp_y1"
zone = "ЮВ1-1_TOP_S"
zones_name = "ZONES_vyng"
cutoff_value = 12.8

for well in db.wellList():
	for ds in db.selectedDatasetList(well):
		ref_name = db.referenceName(well, ds)
		db.variableDuplicate(well, ds, ref_name, cutoff)
		db.variableCopy(well, zones_name, "ZONES", ds, "ZONES", "automatic", "project", "project", -1, 0, 1)

		func = lambda x : x*0
		cutoff_empty = map(func, (db.variableLoad(well, ds, cutoff)))
		db.variableSave(well, ds, cutoff, "Average Porosity", "%", list(cutoff_empty), 0, "auto")
		top_zone = []
		bot_zone = []
		
		md = db.variableLoad(well, ds, ref_name)
		zones = db.variableLoad(well, ds, "ZONES")
		cutoff_list = db.variableLoad(well, ds, cutoff)
		for i in range(len(md)):
			if zones[i] == zone and zones[i-1] != zone:
				top_zone.append(i)
			if zones[i] == zone and zones[i+1] != zone:
				bot_zone.append(i)
		
		for i in range(len(md))[top_zone[0]:bot_zone[0]]:
			cutoff_list[i] = cutoff_value
		db.variableSave(well, ds, cutoff, "Average Porosity", "%", cutoff_list, 0, "auto")
			
		
