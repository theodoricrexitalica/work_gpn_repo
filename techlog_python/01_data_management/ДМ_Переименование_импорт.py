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
import TechlogDialogAdvanced as tda
field_list = [	"VynYa",
					"VynG",
					"Sut",
					"Sug",
					"S_Itu",
					"Spo",
					"Rom",
					"ZapCha",
					"Otd",
					"Nov",
					"Kra",
					"Ety",
					"ZapTark"]
db.currentChange("import")
dlg = tda.dialogAdvanced("Загрузка месторождения")
input_fld = dlg.addListInput("field_list", "Месторождения", field_list, 0, 1, "help")
dlg.execDialog()
output_fld = dlg.getListInput("field_list")

fld = output_fld + "-"
pad = ""
for well in db.selectedWellList():
	name1 = well.split("_")
	if len(name1) == 1:
		db.wellRename(well, fld + well + pad)
	else:
		db.wellRename(well, fld + name1[1] + pad )
