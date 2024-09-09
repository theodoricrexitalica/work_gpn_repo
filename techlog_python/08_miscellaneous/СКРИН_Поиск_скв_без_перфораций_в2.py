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
__date__ = """2022-01-10"""
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
s = ";"
cc_wells = 0
cc_perf = 0
ds = "RIGIS_gm"
zone =  "БВ6"											#целевая зона
ds_zone = "ZONES_vyng_gm"
#for well in db.wellList():
for well in db.selectedWellList():
	perf_list = []
	cc_wells += 1
	zones_list = db.variableLoad(well, ds_zone, "ZONES")
	for i in range(len(zones_list)):
		if zone in zones_list[i]:
			ind1 = db.datasetZoneIndice(well, ds, ds_zone, zones_list[i], "Zone Name", 0)[0]
			ind2 = db.datasetZoneIndice(well, ds, ds_zone, zones_list[i], "Zone Name", 0)[1]
			md = db.variableLoad(well, ds, db.referenceName(well, ds))
			kng = db.variableLoad(well, ds, "kng", "auto")
			perf = db.variableLoad(well, ds, "kng", "auto")
			for j in range(len(md))[ind1:ind2]:
				if kng[j] > 0 and perf[j] != MissingValue:
					perf_list.append(0.1)
	#print(perf_list)
	if round(sum(perf_list),1) >= 0.3:								#проверка есть ли хотя 0.3м перфорации в интервале,
		pass																		#если нет, то скважине присваивается код "0"
	else:
		cc_perf += 1
		print(well, s, round(sum(perf_list),1))
print("total_wells", s, "wells_w/o_perf")
print(cc_wells, s, cc_perf)
