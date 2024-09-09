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

__author__ = """Taras DOLGUSHIN (Dolgushin.TYu)"""
__date__ = """2021-07-01"""
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
#Удаление подчеркивания у переменной
for well in db.wellList():
	for ds in db.datasetList(well):
		for var in db.selectedVariableList(well, ds):
			orig_var = var
			new_var = var.split("_")[0]
			db.variableRename(well, ds, var, new_var)
			if "Porosity" in db.variableFamily(well, ds, new_var):
				db.variableUnitChange(well, ds, new_var, "%")
			if "Resistivity" in db.variableFamily(well, ds, new_var):
				db.variableUnitChange(well, ds, new_var, "ohmm")
			if "Neutron Far" in db.variableFamily(well, ds, new_var):
				db.variableUnitChange(well, ds, new_var, "UE")
			if "Density" in db.variableFamily(well, ds, new_var):
				db.variableUnitChange(well, ds, new_var, "g/cm3")
			if "Spontaneous Potential" in db.variableFamily(well, ds, new_var):
				db.variableUnitChange(well, ds, new_var, "mV")
			if "Spontaneous Potential Alpha" in db.variableFamily(well, ds, new_var):
				db.variableUnitChange(well, ds, new_var, "v/v")
			if "Russian Gamma Ray" in db.variableFamily(well, ds, new_var):
				db.variableUnitChange(well, ds, new_var, "uR/h")
			if "DGK" in new_var:
				db.variableUnitChange(well, ds, new_var, "v/v")
			if "KGL" in new_var:
				db.variableUnitChange(well, ds, new_var, "%")
				db.variableFamilyChange(well, ds, new_var, "Shale Volume")
			if "KINT" in new_var:
				db.variableUnitChange(well, ds, new_var, "mD")
			if "NPHI" in new_var:
				db.variableUnitChange(well, ds, new_var, "%")
			if "KPS" in new_var:
				db.variableUnitChange(well, ds, new_var, "%")
				db.variableFamilyChange(well, ds, new_var, "Porosity")
			if "SXWB" in new_var:
				db.variableUnitChange(well, ds, new_var, "%")
			if "SG" in new_var:
				db.variableUnitChange(well, ds, new_var, "%")
			db.variableCopy(well, ds, new_var, "LQC", new_var, "automatic", "project", "project", -1, 0, 1) 
			db.variableRename(well, ds, new_var, orig_var)
			print(well)
			for var in db.variableList(well, 'LQC'):
				if var ==  'GGK':
					db.variableRename(well, 'LQC', 'GGK', 'RHOB')
				if var == 'GK':
					db.variableRename(well, 'LQC', 'GK', 'GR')
				if var == 'PS':
					db.variableRename(well, 'LQC', 'PS', 'SP')
