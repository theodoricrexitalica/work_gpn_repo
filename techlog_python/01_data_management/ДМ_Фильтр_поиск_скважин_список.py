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
__date__ = """2022-03-21"""
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
list_wells = '1536-1556-1557-1576-1577-1596-1615-1616'															#По списку имен скважин в Техлог
list_wells = list_wells.split('-')

list_wells_sort = list_wells.sort
for items in list_wells:
	#print(items.split('-')[1])
	for well in db.wellList():
		if items in well:
			print(well)
print(len(list_wells))


#list_wells = [250, 240, '1538ST2', '1516', 1557, 1558, 1543, '1546_1', 240, 1546]																#По списку имен скважин NGT
#well_ngt_list = []
#well_list = []
#for well in db.wellList():
	#if db.datasetExists(well, 'wellinfo'):
		#try:
			#well_ngt_list.append(db.variableLoad(well, 'wellinfo', 'well_ngt')[0])
			#well_list.append(well)
		#except:
			#pass
#dict_well_ngt = dict(zip(well_ngt_list, well_list))
#for items in list_wells:
	#for well_ngt in well_ngt_list:
		#if str(items) in well_ngt:
			#print(dict_well_ngt[well_ngt])
#print(len(list_wells))
