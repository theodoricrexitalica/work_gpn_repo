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
__date__ = """2022-04-19"""
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
	ds_gbd = 'GDB_LOGS'
	#ds_lqc = 'LQC'
	var_list = []
	md_bot = []
	#if db.datasetExists(well, ds_gbd) and db.datasetExists(well, ds_lqc):
	if db.datasetExists(well, ds_gbd):
		for var in db.variableList(well, ds_gbd)[:]:
			var_data = db.variableLoad(well, ds_gbd, var)
			md = db.variableLoad(well, ds_gbd, db.referenceName(well, ds_gbd))
			for i in range(len(md)):
				try:
					if var_data[i] != MissingValue and var_data[i+1] == MissingValue:
						var_list.append(var)
						md_bot.append(md[i])
				except:
					pass
	dict_data = dict(zip(md_bot, var_list))
	keys_list = list(dict_data.keys())

	print(well, 													#Вывод скважины, мнемоники, ее макс глубины и глубины индекса датасета
	ds_gbd,
	dict_data[max(keys_list)], 
	int(max(keys_list)),
	int(md[-1]),
	int(md[-1]) - int(max(keys_list)))
#print(dict_data)
				
