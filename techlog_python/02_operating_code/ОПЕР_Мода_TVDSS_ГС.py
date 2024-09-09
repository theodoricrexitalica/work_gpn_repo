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
__date__ = """2022-09-19"""
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
import statistics as stat

s = ';'
print('well ; zone ; tvdss_mode ; rtSh_mdn ; rtDp_mdn ; qoil_mer ; wc_mer')

for well in db.selectedWellList():
	dsZone = 'ZONES_gm'
	dsLqc = 'LQC'
	dsMer = 'MER_Sep22'
	dsIndex = 'Index'
	varTvdss = 'TVDSS'
	varDp = 'RT_DP'
	varSh = 'RT_SH'
	varOpd = '13_opd'
	varWct = '15_wct'
	
	varZone = db.variableLoad(well, dsZone, 'ZONES')[0]
	
	ind = db.datasetZoneIndice(well, dsIndex, dsZone, varZone)
	indLqc = db.datasetZoneIndice(well, dsLqc, dsZone, varZone)
	
	wellDepth = db.variableLoad(well, dsIndex, varTvdss)[ind[0]:ind[1]]
	varShList = db.variableLoad(well, dsLqc, varSh)[indLqc[0]:indLqc[1]]
	varDpList = db.variableLoad(well, dsLqc, varDp)[indLqc[0]:indLqc[1]]
	
	varOpdList = stat.mean(db.variableLoad(well, dsMer, varOpd))
	varWctList = stat.mean(db.variableLoad(well, dsMer, varWct))
	
	func1 = lambda x: round(x, 0)
	tvdss = list(map(func1, wellDepth))
	tvdss_mode = stat.mode(tvdss)
	func2 = lambda x: round(x, 1)
	varShList = list(map(func2, varShList))
	varSh_mode = stat.median(varShList)
	varDpList = list(map(func2, varDpList))
	varDp_mode = stat.median(varDpList)

	print(well, s, 
	varZone, s, 
	int(tvdss_mode), s,
	int(varSh_mode),s,
	int(varDp_mode),s,
	int(varOpdList), s,
	int(varWctList))
