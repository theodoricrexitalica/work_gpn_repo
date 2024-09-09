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
__date__ = """2022-12-12"""
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
well_cc = 0
gr_cc = 0
for well in db.wellList()[:]:
	well_cc += 1
	dsLqc = 'LQC'
	dsGr = 'GR_ds'
	dsZone = 'ZONES_gm'
	dsInd = 'Index'
	#md = db.variableLoad(well, dsGr, db.referenceName(well, dsGr))
	#zones = db.variableLoad(well, dsGr, 'ZONES')
	#md_zones_list = []
	#for i in range(len(md)):
		#if zones[i] == 'БС9-2-1+2_TOP_S':
			#md_zones_list.append(1)
	#print(well, round(sum(md_zones_list)*0.1,0))
	
	
	
	#db.datasetDuplicate(well, dsLqc, well, 'GR_ds')
	#for var in db.variableList(well, dsGr, 1):
		#if var == 'GR':
			#gr_cc += 1
	#print(well, db.variableList(well, dsGr))
	#if 'GR' in db.variableList(well, dsGr):
		#pass
	#else:
		#print(well)
#print(well_cc, gr_cc)
	#for var in db.variableList(well, dsGr, 1):
		#if var != db.referenceName(well, dsGr) and var != 'GR':
			##print(well, dsGr, var)
			#db.variableDelete(well, dsGr, var)
	#db.variableCopy(well, dsInd, 'TVDSS', dsGr, 'TVDSS', 'automatic', 'project', 'project', -1, 0, 1)
	db.variableCopy(well, dsZone, 'ZONES', dsGr, 'ZONES', 'automatic', 'project', 'project', -1, 0, 1)
	db.variableCopy(well, dsZone, 'X', dsGr, 'X', 'automatic', 'project', 'project', -1, 0, 1)
	db.variableCopy(well, dsZone, 'Y', dsGr, 'Y', 'automatic', 'project', 'project', -1, 0, 1)
