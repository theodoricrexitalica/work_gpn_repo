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
__date__ = """2021-06-07"""
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
#Переименование мнемоник в датасете типа Петрел
import TechlogDialogAdvanced as tda
rigis_list = [	"RIGIS_bdntc",
					"RIGIS_gm",
					"Type your own..."]
dlg = tda.dialogAdvanced("Загрузка РИГИС")
input = dlg.addListInput("rigis_list", "Месторождения", rigis_list, 0, 1, "help")
dlg.execDialog()
output = dlg.getListInput("rigis_list")

db.currentChange("import")
pt_ds_name = output
for well in db.selectedWellList():
	for ds in db.datasetList(well):
		db.variableFamilyChange(well,ds,"ALPS", "Spontaneous Potential Alpha")
		db.variableUnitChange(well, ds, "ALPS", "v/v")
		db.variableFamilyChange(well,ds,"aps", "Spontaneous Potential Alpha")
		db.variableUnitChange(well, ds, "aps", "v/v")
		db.variableFamilyChange(well,ds,"BK", "Lateral Log Resistivity")
		db.variableUnitChange(well, ds, "BK", "ohmm")	
		db.variableFamilyChange(well,ds,"GK", "Russian Gamma Ray")
		db.variableUnitChange(well, ds, "GK", "uR/h")	
		db.variableFamilyChange(well,ds,"DT", "Compressional Slowness")
		db.variableUnitChange(well, ds, "DT", "us/m")							
		db.variableFamilyChange(well,ds,"kgl", "Shale Volume Average")
		db.variableUnitChange(well, ds, "kgl", "v/v")		
		db.variableFamilyChange(well,ds,"Kos", "Average Hydrocarbon Saturation")
		db.variableUnitChange(well, ds, "Kos", "%")		
		db.variableFamilyChange(well,ds,"kng", "Average Hydrocarbon Saturation")
		db.variableUnitChange(well, ds, "kng", "v/v")		
		db.variableFamilyChange(well,ds,"Kpo", "Average Porosity")
		db.variableUnitChange(well, ds, "Kpo", "%")		
		db.variableFamilyChange(well,ds,"kp", "Average Porosity")
		db.variableUnitChange(well, ds, "kp", "v/v")		
		db.variableFamilyChange(well,ds,"Kpr", "Average Permeability")
		db.variableUnitChange(well, ds, "Kpr", "mD")	
		db.variableFamilyChange(well,ds,"kpr", "Average Permeability")
		db.variableUnitChange(well, ds, "kpr", "mD")	
		db.variableFamilyChange(well,ds,"kvo", "Irreducible Water Saturation")
		db.variableUnitChange(well, ds, "kvo", "v/v")
		db.variableTypeChange(well, ds, "kvo", "TopBottomCurve")	
		db.variableFamilyChange(well,ds,"KW", "Water Saturation")
		db.variableUnitChange(well, ds, "KW", "%")
		db.variableFamilyChange(well,ds,"Litol", "Net Rock Flag")
		db.variableUnitChange(well, ds, "Litol", "unitless")
		db.variableFamilyChange(well,ds,"lit", "Net Rock Flag")
		db.variableUnitChange(well, ds, "lit", "unitless")
		db.variableFamilyChange(well,ds,"lits", "Net Rock Flag")
		db.variableUnitChange(well, ds, "lits", "unitless")
		db.variableFamilyChange(well,ds,"kol", "Net Rock Flag")
		db.variableUnitChange(well, ds, "kol", "unitless")		
		db.variableFamilyChange(well,ds,"NKTD", "Neutron Porosity Russian")
		db.variableUnitChange(well, ds, "NKTD", "unitless")	
		db.variableFamilyChange(well,ds,"PRON", "Permeability")
		db.variableUnitChange(well, ds, "PRON", "mD")
		db.variableFamilyChange(well,ds,"PZ", "Potential")
		db.variableUnitChange(well, ds, "PZ", "ohmm")	
		db.variableFamilyChange(well,ds,"sand", "Net Reservoir Flag")
		db.variableUnitChange(well, ds, "sand", "unitless")	
		db.variableFamilyChange(well,ds,"rp", "Formation Resistivity Average")
		db.variableUnitChange(well, ds, "rp", "ohmm")	
		db.variableFamilyChange(well,ds,"satur", "Net Pay Flag")
		db.variableUnitChange(well, ds, "satur", "unitless")	
		db.variableFamilyChange(well,ds,"saturgis", "Net Pay Flag")
		db.variableUnitChange(well, ds, "saturgis", "unitless")										
		db.variableDelete(well, ds, "Zoneloglinkedto'CopyofWell_Tops'", 1)
		
		if db.variableExists(well, ds, 'lits'):
			db.variableRename(well, ds, 'lit', 'lit_rxr')
			db.variableRename(well, ds, 'lits', 'lit')
		
		db.datasetRename(well, ds, pt_ds_name )

__pyVersion__ = """3"""
