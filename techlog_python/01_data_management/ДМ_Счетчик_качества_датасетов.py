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
__date__ = """2022-04-12"""
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
well_total = 0
well_data = 0
well_list = []
for well in db.wellList():
	well_total += 1
	#if (db.datasetExists(well, 'inclination')
		#and db.datasetExists(well, 'wellinfo')
		#and db.datasetExists(well, 'WH')):
	if (db.datasetExists(well, 'GDB_LOGS')
		and db.datasetExists(well, 'LQC')):
		
	#if (db.datasetExists(well, 'RIGIS_bdntc')
		#and db.datasetExists(well, 'RIGIS_gm')):
	#if (db.datasetExists(well, 'ZONES_bdntc')
		#and db.datasetExists(well, 'ZONES_gm')):
	#if (db.datasetExists(well, 'MER')):
	#if (db.datasetExists(well, 'PERF')):
		
		well_data += 1
	else:
		well_list.append(well)
		pass
print('well_total', well_total)
print('well_data exist', well_data)
for i in set(well_list):
	print(i)


#well_total = 0
#well_broken_list = []
#standard_set =(['GDB_LOGS', 
							#'inclination', 
							#'Index', 'LQC', 
							#'RIGIS_bdntc', 
							#'RIGIS_gm', 
							#'TL_WellPath', 
							#'wellinfo', 
							#'WH', 
							#'ZONES_bdntc', 
							#'ZONES_gm'])
#for well in db.wellList():
	#well_total += 1
	#for i in standard_set:
		#if i not in db.datasetList(well):
			#well_broken_list.append(well)
#well_broken_well = 0
#well_hrz = 0
#for i in set(well_broken_list):
	#well_broken_well += 1
	#if 'G' in i:
		#well_hrz += 1
#print('well_total', well_total)
#print('well_broken_well', well_broken_well - well_hrz)
#print('well_hrz', well_hrz)
