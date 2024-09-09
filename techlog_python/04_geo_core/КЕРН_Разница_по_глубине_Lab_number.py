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
__date__ = """2022-11-01"""
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
print('lab_num', 'core_d-st', 'core_rcal')
for well in db.selectedWellList():
	ds1 = 'CORE_D-ST'
	ds2 = 'CORE_RCAL'
	labNum1 = db.variableLoad(well, ds1, 'Lab_number')
	md1 = db.variableLoad(well, ds1, db.referenceName(well, ds1))
	dict1 = dict(zip(labNum1, md1))
	#print('dic1', dict1.keys())
	
	labNum2 = db.variableLoad(well, ds2, 'Lab_number')
	md2 = db.variableLoad(well, ds2, db.referenceName(well, ds1))
	dict2 = dict(zip(labNum2, md2))
	#print('dic2', dict2.keys())
	
	newMD = []
	for i in dict1.keys():
		for j in dict2.keys():
			if i == j:
				print(i, dict1[i], dict2[i], dict1[i]- dict2[i])
				newMD.append(dict2[i])
	db.variableSave(well, ds1, 'MDsft', 'Measured Depth', 'm', newMD, 0, 'auto')
