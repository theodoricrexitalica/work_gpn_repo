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
__date__ = """2021-06-17"""
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
#Переименование мнемоник в датасете CORE
#db.currentChange("import")

for well in db.wellList():
	for ds in db.selectedDatasetList(well):
		print(ds)
		for var in db.variableList(well, ds):
			if "Dens_bulk" in var:
				db.variableFamilyChange(well, ds, var, "Core Bulk Density")
				db.variableUnitChange(well, ds, var, "g/cm3")
			if "Dens_min" in var:
				db.variableFamilyChange(well, ds, var, "Core Grain Density")
				db.variableUnitChange(well, ds, var, "g/cm3")
			if "Lab_number" in var:
				db.variableFamilyChange(well, ds, var, "Sample Name")
				db.variableUnitChange(well, ds, var, "unitless")
				db.variableTypeChange(well, ds, var, "RichText")
			if "Lithology" in var:
				db.variableFamilyChange(well, ds, var, "Remarks")
				db.variableUnitChange(well, ds, var, "unitless")
			if "Perm" in var:
				db.variableFamilyChange(well, ds, var, "Core Permeability")
				db.variableUnitChange(well, ds, var, "mD")
			if "Phie" in var:
				db.variableFamilyChange(well, ds, var, "Core Porosity")
				db.variableUnitChange(well, ds, var, "%")
			if "Phit" in var:
				db.variableFamilyChange(well, ds, var, "Core Porosity")
				db.variableUnitChange(well, ds, var, "%")
			if "Phit_h" in var:
				db.variableFamilyChange(well, ds, var, "Core Porosity Helium")
				db.variableUnitChange(well, ds, var, "%")
			if "Phit_k" in var:
				db.variableFamilyChange(well, ds, var, "Core Porosity Kerosene")
				db.variableUnitChange(well, ds, var, "%")
			if "Phit_w" in var:
				db.variableFamilyChange(well, ds, var, "Core Porosity Water")
				db.variableUnitChange(well, ds, var, "%")
			if "Swirr" in var:
				db.variableFamilyChange(well, ds, var, "Core 'Minimal' Saturation")			
				db.variableUnitChange(well, ds, var, "%")
			if "Kphit" in var:
				db.variableFamilyChange(well, ds, var, "Rock Type")			
				db.variableUnitChange(well, ds, var, "v/v")
		
			
