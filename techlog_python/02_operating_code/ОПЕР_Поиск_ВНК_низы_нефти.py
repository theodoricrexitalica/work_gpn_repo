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
__date__ = """2022-01-20"""
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
for well in db.selectedWellList():
	ds = "RIGIS_gm"
	new_sat = "td_satur"
	ds_zone = "ZONES_sug"
	zone_name = "БС9-2-1+2_TOP_S"
	satur_code = 8
	bot_oil_tvdss = []
	#db.variableCopy(well, "Index", "TVDSS", "RIGIS_bdntc", "TVDSS", "automatic", "project", "project", -1, 0, 1)
	#db.variableCopy(well, "Index", "TVDSS", "RIGIS_gm", "TVDSS", "automatic", "project", "project", -1, 0, 1)
	new_sat_list = db.variableLoad(well, ds, new_sat)
	ind1 = db.datasetZoneIndice(well, ds, ds_zone, zone_name, "Zone Name")[0]
	ind2 = db.datasetZoneIndice(well, ds, ds_zone, zone_name, "Zone Name")[1]
	tvdss = db.variableLoad(well, ds, "TVDSS")
	for i in range(len(tvdss))[ind1:ind2+1]:
		if new_sat_list[i] == satur_code and new_sat_list[i+1] != satur_code:
					#print(satur[i])
					bot_oil_tvdss.append(round(tvdss[i],0))
	print(well, bot_oil_tvdss)
