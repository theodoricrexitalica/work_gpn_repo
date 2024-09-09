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
__date__ = """2021-12-11"""
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
index_problem_list = []
broken_wells_list = []
for well in db.selectedWellList():
	print(well)
	zone = "БС9-2-1+2_TOP_S"
	zone_ds = "ZONES_sug"
	zone_md = db.variableLoad(well, zone_ds, db.referenceName(well, zone_ds))
	zone_list = db.variableLoad(well, zone_ds, "ZONES")
	if db.datasetExists(well, zone_ds) and zone in zone_list:
		top_depth = []
		bot_depth = []
		for i in range(len(zone_md)):
			if zone_list[i] == zone:   #Обязательно разобраться как быть если нет зонейшна за целевым
				try: 
					top_depth.append(zone_md[i])
					bot_depth.append(zone_md[i+1])
				except:
					print("add zone after selected one")
					broken_wells_list.append(well)
		ds = "Index"
		if db.datasetExists(well, ds):
			index_md = db.variableLoad(well, ds, db.referenceName(well, ds))[-1]
			#print(top_depth[0], index_md,  bot_depth[0])
			if bot_depth[0] > index_md > top_depth[0] or index_md  <  top_depth[0]:
				print(well, " - check Index depth", round(index_md,0), "vs", round(top_depth[0],0), "-", round(bot_depth[0],0))
				index_problem_list.append(well + "|")
		else:
			broken_wells_list.append(well)
	else:
		broken_wells_list.append(well)
print("broken_wells_list", broken_wells_list)
print("index_problem_list", index_problem_list)
