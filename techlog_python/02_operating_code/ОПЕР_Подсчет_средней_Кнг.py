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
print("well", s, "avg_kng", s, "median_kng", s, "mer_wc ", s, "period")
for well in db.selectedWellList():
	ds = "RIGIS_bdntc"
	ds_mer = "MER"
	if db.variableExists(well, ds, "PERF"):
		md = db.variableLoad(well, ds, db.referenceName(well, ds))
		kng =  db.variableLoad(well, ds,"kng")
		perf = db.variableLoad(well, ds, "PERF")
		wc = db.variableLoad(well, ds_mer, "watercut")[0:period]
		list_kng_perf = []
		for i in range(len(md)):
			if perf[i] == 1 and kng[i] != 0:
				list_kng_perf.append(kng[i])
		
		avg = round(ts.average(list_kng_perf), 2)
		median = round(ts.median(list_kng_perf), 2)
		avg_wc =  round(ts.average(wc), 2)
		#print(well, s, avg, s, median, s, avg_wc, s, period)
		if len(wc) == 6:
			print(well, s, avg, s, median, s, avg_wc)
	else:
		#print(well, "PERF is absent")
		pass
		
