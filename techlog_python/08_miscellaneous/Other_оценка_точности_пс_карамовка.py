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
__date__ = """2022-03-31"""
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
s = ';'
cc_well = 0
cc_zone = 0
well_list = []
sp_list_bs8_p5 = []
sp_list_bs8_p95 = []
sp_list_bs11_p5 = []
sp_list_bs11_p95 = []
for well in db.selectedWellList():
	cc_well += 1
	ds_zone = 'ZONES_gm'
	zone_bs8 = 'БС8-1_TOP_S'
	zone_bs11 = 'БС11_TOP_S'
	ds_lqc = 'LQC'
	var_sp = 'SP'
	zone_list = db.variableLoad(well, ds_zone, 'ZONES')
	
	if db.datasetExists(well, ds_zone) and db.variableExists(well, ds_lqc, var_sp):
		cc_zone += 1
		if zone_bs8 in zone_list:
			well_list.append(well)
			ind_bs8 = db.datasetZoneIndice(well, ds_lqc, ds_zone, zone_bs8, 'Zone Name', 0)
			ind_bs8_top = ind_bs8[0]
			ind_bs8_bot = ind_bs8[1]
			var_sp_list_bs8 = db.variableLoad(well, ds_lqc, var_sp)[ind_bs8_top:ind_bs8_bot]
			sp_p5_bs8 = ts.percentile(var_sp_list_bs8, 5, 1)
			sp_p95_bs8 = ts.percentile(var_sp_list_bs8, 95, 1)
			sp_list_bs8_p5.append(sp_p5_bs8)
			sp_list_bs8_p95.append(sp_p95_bs8)
			ind_bs11 = db.datasetZoneIndice(well, ds_lqc, ds_zone, zone_bs11, 'Zone Name', 0)
			ind_bs11_top = ind_bs11[0]
			ind_bs11_bot = ind_bs11[1]
			var_sp_list_bs11 = db.variableLoad(well, ds_lqc, var_sp)[ind_bs11_top:ind_bs11_bot]
			sp_p5_bs11 = ts.percentile(var_sp_list_bs11, 5, 1)
			sp_p95_bs11 = ts.percentile(var_sp_list_bs11, 95, 1)
			sp_list_bs11_p5.append(sp_p5_bs11)
			sp_list_bs11_p95.append(sp_p95_bs11)


print('well', s, 'bs8_p5', s, 'bs8_p95', s, 'bs11_p5', s,  'bs8_p95')
for i in range(len(well_list)):
	print(well_list[i], s, round(sp_list_bs8_p5[i],0), s, round(sp_list_bs8_p95[i],0), s,
										round(sp_list_bs11_p5[i],0), s, round(sp_list_bs11_p95[i],0))
										

print(cc_well)
print(cc_zone)
