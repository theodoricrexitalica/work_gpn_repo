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
__date__ = """2022-04-06"""
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
	ds_perf = 'PERF'
	ds_lqc = 'LQC'
	var_status = 'Status'
	var_perf = 'PERF'
	if db.datasetExists(well, ds_perf):
		ref_name = db.referenceName(well, ds_perf)
		list_perf = db.variableLoad(well, ds_perf, var_perf)
		ref = db.variableLoad(well, ds_perf, ref_name)
		perf_top = []
		perf_bot = []
		for i in range(len(ref)):
			if list_perf[i] == 1:
				perf_top.append(ref[i])
				perf_bot.append(ref[i+1])
	print(well, ds_perf, perf_top, '-', perf_bot)
	
	if db.datasetExists(well, ds_lqc):
		ref_name = db.referenceName(well, ds_lqc)
		ref = db.variableLoad(well, ds_lqc, ref_name)
		db.variableDuplicate(well, ds_lqc, ref_name, 'PERF')
		perf_lqc = db.variableLoad(well, ds_lqc, 'PERF')
		for i in range(len(perf_lqc)):
			perf_lqc[i] = -9999
		db.variableSave(well, ds_lqc, 'PERF', '', '', perf_lqc, 0, 'auto')
		
		lqc_ind_top = []
		lqc_ind_bot = []
		for i in range(len(ref)):
			for j in range(len(perf_top)):
				if ref[i] == perf_top[j]:
					lqc_ind_top.append(i)
				if ref[i] == perf_bot[j]:
					lqc_ind_bot.append(i)
		#print(lqc_ind_top)
		print(well, ds_lqc, lqc_ind_top, '-', lqc_ind_bot)
		for i in range(len(lqc_ind_top)):
			for j in range(len(perf_lqc))[lqc_ind_top[i]:lqc_ind_bot[i]]:
				perf_lqc[j] = 1
			db.variableSave(well, ds_lqc, 'PERF', 'Perforation', 'unitless', perf_lqc, 0, 'auto')
		
		
		
