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
__date__ = """2023-02-22"""
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
from itertools import accumulate

for well in db.selectedWellList():
	dsRigisGm = 'RIGIS_gm'
	dsZoneGm = 'ZONES_gm'
	if db.datasetExists(well, dsRigisGm) and db.datasetExists(well, dsZoneGm):
		print(well)
		md = db.variableLoad(well, dsRigisGm, 'DEPT')
		satur = db.variableLoad(well, dsRigisGm, 'satur')
		kng = db.variableLoad(well, dsRigisGm, 'kng')
		kp = db.variableLoad(well, dsRigisGm, 'kp')
		ehc_temp = np.zeros(len(satur))
		for i in range(len(satur)):
			if satur[i] == 8:
				ehc_temp[i] += kp[i]*kng[i]*0.1
		db.variableSave(well, dsRigisGm, 'ehc_temp', '','', ehc_temp, 0, 'auto')
		ehc = list(accumulate(ehc_temp))
		for j in range(len(ehc)):
			ehc[j] = max(ehc) - ehc[j]
		ehc.insert(0,ehc.pop())
		db.variableSave(well, dsRigisGm, 'ehc', '','', ehc, 0, 'auto')
		db.variableFamilyChange(well, dsRigisGm, 'ehc', 'EHC')
		db.variableUnitChange(well, dsRigisGm, 'ehc', 'm')
		db.variableDelete(well, dsRigisGm, 'ehc_temp', 1)
	else:
		print(well, ' - not datasets')
		pass
