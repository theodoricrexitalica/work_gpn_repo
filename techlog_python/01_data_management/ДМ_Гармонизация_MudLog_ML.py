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
__date__ = """2022-07-06"""
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
#db.currentChange('import')
for well in db.wellList():
	for ds in db.selectedDatasetList(well):
		for var in db.variableList(well, ds):
			#db.variableRename(well, ds, 'Глуб', 'MD')
			#db.variableUnitChange(well, ds, 'MD', 'm')
			#db.variableFamilyChange(well, ds, 'MD', 'Measured Depth')
			db.variableRename(well, ds, 'С1', 'C1')
			db.variableFamilyChange(well, ds, 'C1', 'Mud Gas C1')
			db.variableRename(well, ds, 'С2', 'C2')
			db.variableFamilyChange(well, ds, 'C2', 'Mud Gas C2')
			db.variableRename(well, ds, 'С3', 'C3')
			db.variableFamilyChange(well, ds, 'C3', 'Mud Gas C3')
			db.variableRename(well, ds, 'C4', 'iC4')
			db.variableFamilyChange(well, ds, 'iC4', 'Mud Gas IC4')
			db.variableRename(well, ds, 'C5', 'iC5')
			db.variableFamilyChange(well, ds, 'iC5', 'Mud Gas IC5')
			db.variableFamilyChange(well, ds, 'Гсум', 'Total Gas')
			db.variableRename(well, ds, 'T', 'HOOKP')
			db.variableFamilyChange(well, ds, 'HOOKP', 'Block Position')
			db.variableUnitChange(well, ds, 'HOOKP', 'm')
			db.variableRename(well, ds, 'Вес', 'WOH')
			db.variableFamilyChange(well, ds, 'WOH', 'Block Position')
			db.variableUnitChange(well, ds, 'WOH', 't')
			db.variableRename(well, ds, 'Нагр', 'WOB')
			db.variableFamilyChange(well, ds, 'WOB', 'Weight On Bit')
			db.variableUnitChange(well, ds, 'WOB', 't')
			db.variableRename(well, ds, 'Д', 'SPP')
			db.variableFamilyChange(well, ds, 'SPP', 'Standpipe Pressure')
			db.variableUnitChange(well, ds, 'SPP', 'atm')
			
