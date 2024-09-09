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
__date__ = """2022-02-03"""
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
import TechlogStat as ts
ds_zone = 'ZONES_ety_gm'
month = 3

for well in db.selectedWellList():
	db.variableCopy(well, "Index", "TVDBML", ds_zone, "TVDBML", "automatic", "project", "project", -1, 0, 1)
	zone_top = db.variableLoad(well, ds_zone, db.referenceName(well, ds_zone))
	zone_top_tvdbml = db.variableLoad(well, ds_zone,"TVDBML")
	tvdbml = db.variableLoad(well, "Index", "TVDBML")
	ref_index = db.variableLoad(well, "Index", db.referenceName(well, "Index"))
	tvdbml_zone = []
	for i in range(len(ref_index)):
		if ref_index[i] > zone_top[0]:
			tvdbml_zone.append(tvdbml[i])
	ref_mer = db.variableLoad(well, "MER", db.referenceName(well, "MER"))
	watercut = db.variableLoad(well, "MER", "watercut")
	watercut_list = []
	#for j in range(len(ref_mer))[3:6]:
	for j in range(len(ref_mer))[0: month]:
		watercut_list.append(watercut[j])

	print(well, round(zone_top_tvdbml[0],0), round(ts.median(tvdbml_zone),1), round(ts.median(watercut_list),2))
