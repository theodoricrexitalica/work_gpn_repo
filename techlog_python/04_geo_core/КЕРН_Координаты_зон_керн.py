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
__date__ = """2022-06-21"""
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
import numpy as np
target_zone = 'БС10-3'
well_list = []
for well in db.wellList():
	ds_zone = 'ZONES_gm'
	ds_core = 'CORE_RCAL'
	if db.datasetExists(well, ds_core):
		var_core_zone = 'Zone'
		core_zone_list = db.variableLoad(well, ds_core, var_core_zone)
		try:
			for item in core_zone_list:
				if target_zone in item:
					well_list.append(well)
					break
		except:
			pass

for well_core in well_list:
	ds_zone = 'ZONES_gm'
	var_zone = 'ZONES'
	zone_list = db.variableLoad(well_core, ds_zone, var_zone)
	x_coord = db.variableLoad(well_core, ds_zone, 'X')
	y_coord = db.variableLoad(well_core, ds_zone, 'Y')
	for row in zone_list:
		if target_zone in row:
			ind_zone = db.datasetZoneIndice(well_core, 'CORE_RCAL', ds_zone, row)
			phiq = db.variableLoad(well_core, 'CORE_RCAL', 'KPVK')[ind_zone[0]:ind_zone[1]]
			phiq = np.array(phiq)
			
			print(well_core, 
					target_zone,
					x_coord[zone_list.index(row)], 
					y_coord[zone_list.index(row)],
					len(phiq[phiq != -9999]))
			break
