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
__date__ = """2022-02-15"""
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
s = ";"
period = 6
#print("well", s, "heff", s, "avg_oil ", s, "avg_water", s, "period")
for well in db.selectedWellList():
	ds = "RIGIS_bdntc"
	ds_mer = "MER"
	if db.variableExists(well, ds, "PERF"):
		md = db.variableLoad(well, ds, db.referenceName(well, ds))
		heff =  db.variableLoad(well, ds,"lit")
		perf = db.variableLoad(well, ds, "PERF")
		v_oil = db.variableLoad(well, ds_mer, "v_oil")[0:period]
		v_water = db.variableLoad(well, ds_mer, "v_water")[0:period]
		list_heff_perf = []
		for i in range(len(md)):
			if perf[i] == 1 and heff[i] == 1:
				list_heff_perf.append(heff[i])
		sum = round((ts.sum(list_heff_perf))*0.1, 2)
		avg_oil =  round(ts.average(v_oil), 2)
		avg_water =  round(ts.average(v_water), 2)
		#print(well, s, avg, s, median, s, avg_wc, s, period)
		print(well, s, sum, s, avg_oil, s, avg_water, s, period)
	else:
		md = db.variableLoad(well, ds, db.referenceName(well, ds))
		heff =  db.variableLoad(well, ds,"lit")
		v_oil = db.variableLoad(well, ds_mer, "v_oil")[0:period]
		v_water = db.variableLoad(well, ds_mer, "v_water")[0:period]
		zone_top = db.datasetZoneIndice(well, ds, "ZONES_kar_bdntc", "ACH_1_TOP_S")[0]
		zone_bot = db.datasetZoneIndice(well, ds, "ZONES_kar_bdntc", "ACH_3_TOP_S")[1]
		list_heff_perf = []
		for i in range(len(md))[zone_top:zone_bot]:
			list_heff_perf.append(heff[i])
		sum = round((ts.sum(list_heff_perf))*0.1, 2)
		avg_oil =  round(ts.average(v_oil), 2)
		avg_water =  round(ts.average(v_water), 2)
		print(well, s, sum, s, avg_oil, s, avg_water, s, period, "fracked")
		print(md[zone_top], md[zone_bot])
