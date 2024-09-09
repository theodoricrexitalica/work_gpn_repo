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
__awiEngine__ = """v1"""
__layoutTemplateMode__ = """"""
__includeMissingValues__ = """True"""
__keepPreviouslyComputedValues__ = """True"""
__areInputDisplayed__ = """True"""
__useMultiWellLayout__ = """True"""
__idForHelp__ = """"""
__executionGranularity__ = """full"""
#DeclarationsEnd
#Переименование датасета в LQC и мнемоник
db.currentChange("import")
ds = "LQC"
for well in db.selectedWellList():
	for ds_init in db.datasetList(well):
		if db.datasetExists(well, ds):
			pass
		else:
			db.datasetRename(well, ds_init, ds)
		for var in db.variableList(well, ds):
			if "GR" in var:
				db.variableFamilyChange(well, ds, var, "Russian Gamma Ray")
				db.variableUnitChange(well, ds, var, "uR/h")
			if "GK" in var:
				db.variableFamilyChange(well, ds, var, "Russian Gamma Ray")
				db.variableUnitChange(well, ds, var, "uR/h")
			if "SP" in var:
				db.variableFamilyChange(well, ds, var, "Spontaneous Potential")
				db.variableUnitChange(well, ds, var, "mV")
			if "KGGK" in var:
				db.variableFamilyChange(well, ds, var, "Porosity")
				db.variableUnitChange(well, ds, var, "%")
			if "CALI" in var:
				db.variableFamilyChange(well, ds, var, "Caliper")
				db.variableUnitChange(well, ds, var, "m")
			if "Resistivity" in db.variableFamily(well, ds,var):
				db.variableUnitChange(well, ds, var, "ohmm")
			if "Gradient" in db.variableFamily(well, ds,var):
				db.variableUnitChange(well, ds, var, "ohmm")
			if "PROX" in var:
				db.variableUnitChange(well, ds, var, "ohmm")
			if "MLM" in var:
				db.variableUnitChange(well, ds, var, "unitless")
			if "IK" in var:
				db.variableUnitChange(well, ds, var, "mS/m")
			if "KPO" in var:
				db.variableUnitChange(well, ds, var, "%")
			if "KW" in var:
				db.variableUnitChange(well, ds, var, "%")
			if "NKT" in var:
				db.variableUnitChange(well, ds, var, "UE")
			if "NKTR" in var:
				db.variableUnitChange(well, ds, var, "%")
			if "PRON" in var:
				db.variableUnitChange(well, ds, var, "mD")
			if "PZ" in var:
				db.variableUnitChange(well, ds, var, "mD")
			if "SXWB" in var:
				db.variableUnitChange(well, ds, var, "%")
			if "VGL" in var:
				db.variableUnitChange(well, ds, var, "%")
			if "SG" in var:
				db.variableUnitChange(well, ds, var, "%")
			if "DENSITY" in var:
				db.variableUnitChange(well, ds, var, "g/cm3")
			if "KGL" in var:
				db.variableUnitChange(well, ds, var, "%")
			if "ALPS" in var:
				db.variableUnitChange(well, ds, var, "v/v")
			if "IKVR1" in var:
				db.variableUnitChange(well, ds, var, "ohmm")
			if "IKVR2" in var:
				db.variableUnitChange(well, ds, var, "ohmm")
			if "IKVR3" in var:
				db.variableUnitChange(well, ds, var, "ohmm")
			if "IKVR4" in var:
				db.variableUnitChange(well, ds, var, "ohmm")
			if "IKVR5" in var:
				db.variableUnitChange(well, ds, var, "ohmm")
			if "TVD" in var:
				db.variableUnitChange(well, ds, var, "m")
			if "BK1" in var:
				db.variableFamilyChange(well, ds, var, "Resistivity - Laterolog Array 0")
				db.variableUnitChange(well, ds, var, "ohmm")
			if "BK2" in var:
				db.variableFamilyChange(well, ds, var, "Resistivity - Laterolog Array 1")
				db.variableUnitChange(well, ds, var, "ohmm")
			if "BK3" in var:
				db.variableFamilyChange(well, ds, var, "Resistivity - Laterolog Array 2")
				db.variableUnitChange(well, ds, var, "ohmm")
			if "BK4" in var:
				db.variableFamilyChange(well, ds, var, "Resistivity - Laterolog Array 3")
				db.variableUnitChange(well, ds, var, "ohmm")
			if "BK5" in var:
				db.variableFamilyChange(well, ds, var, "Resistivity - Laterolog Array 4")
				db.variableUnitChange(well, ds, var, "ohmm")
			if "BK6" in var:
				db.variableFamilyChange(well, ds, var, "Resistivity - Laterolog Array 5")
				db.variableUnitChange(well, ds, var, "ohmm")
			if "PHIT" in var:
				#db.variableFamilyChange(well, ds, var, "Porosity")
				db.variableUnitChange(well, ds, var, "%")
			if "W" in var:
				#db.variableFamilyChange(well, ds, var, "Neutron Porosity")
				db.variableUnitChange(well, ds, var, "%")
			if "SW" in var:
				#db.variableFamilyChange(well, ds, var, "Water Saturation")
				db.variableUnitChange(well, ds, var, "%")
			if "KINT" in var:
				#db.variableFamilyChange(well, ds, var, "Permeability")
				db.variableUnitChange(well, ds, var, "mD")
			if "RHOZ" in var:
				db.variableUnitChange(well, ds, var, "g/cm3")
			if "RHOB" in var:
				db.variableUnitChange(well, ds, var, "g/cm3")
			if "SWI" in var:
				db.variableFamilyChange(well, ds, var, "Irreducible Water Saturation")
				db.variableUnitChange(well, ds, var, "v/v")
			if "PEFZ" in var:
				db.variableUnitChange(well, ds, var, "b/elec")
			if "HMIN" in var:
				db.variableUnitChange(well, ds, var, "ohmm")
			if "HMNO" in var:
				db.variableUnitChange(well, ds, var, "ohmm")
			if "APS" in var:
				db.variableUnitChange(well, ds, var, "v/v")	
			if "DT" in var:
				db.variableUnitChange(well, ds, var, "us/m")
			if "CFTC" in var:
				db.variableUnitChange(well, ds, var, "UE")		
			if "CILD" in var:
				db.variableUnitChange(well, ds, var, "mS/m")
			if "R05" in var:
				db.variableFamilyChange(well, ds, var, "Resistivity 05")
				db.variableUnitChange(well, ds, var, "ohmm")
			if "R07" in var:
				db.variableFamilyChange(well, ds, var, "Resistivity 07")
				db.variableUnitChange(well, ds, var, "ohmm")
			if "R10" in var:
				db.variableFamilyChange(well, ds, var, "Resistivity 10")
				db.variableUnitChange(well, ds, var, "ohmm")
			if "R14" in var:
				db.variableFamilyChange(well, ds, var, "Resistivity 14")
				db.variableUnitChange(well, ds, var, "ohmm")
			if "R20" in var:
				db.variableFamilyChange(well, ds, var, "Resistivity 20")
				db.variableUnitChange(well, ds, var, "ohmm")
			if "RT" in var:
				db.variableFamilyChange(well, ds, var, "Formation Resistivity")
				db.variableUnitChange(well, ds, var, "ohmm")
			if "W" in var:
				db.variableFamilyChange(well, ds, var, "Neutron Porosity")
				db.variableUnitChange(well, ds, var, "%")
			if "KPS" in var:
				db.variableFamilyChange(well, ds, var, "Porosity")
				db.variableUnitChange(well, ds, var, "%")
			if "KGL" in var:
				db.variableFamilyChange(well, ds, var, "Shale Volume")
				db.variableUnitChange(well, ds, var, "%")
			if "DGK" in var:
				db.variableFamilyChange(well, ds, var, "Gamma Ray Normalised")
				db.variableUnitChange(well, ds, var, "v/v")
			if "DNK" in var:
				db.variableFamilyChange(well, ds, var, "Neutron Normalized")
				db.variableUnitChange(well, ds, var, "v/v")
			if "CALI" in var:
				db.variableUnitChange(well, ds, var, "mm")
			if "C1" in var:
				db.variableUnitChange(well, ds, var, "mm")
			if "C2" in var:
				db.variableUnitChange(well, ds, var, "mm")
			if "Phase" in db.variableFamily(well, ds, var):
				db.variableUnitChange(well, ds, var, "deg")
			if "CILD" in db.variableFamily(well, ds, var):
				db.variableUnitChange(well, ds, var, "mS/m")
			if "CFTC" in db.variableFamily(well, ds, var):
				db.variableUnitChange(well, ds, var, "UE")
		
		for var in db.variableList(well, ds):
			if "_" in var:
				db.variableDelete(well, ds, var)							
			
			

__pyVersion__ = """3"""
