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
__date__ = """2021-10-25"""
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
	if "G" in well:
		ds = "LQC"
		wrong_gr = "HAGRT"
		if db.variableExists(well, ds, wrong_gr):
			db.variableFamilyChange(well, ds, wrong_gr, "Gamma Ray")
			db.variableUnitChange(well, ds, wrong_gr, "gapi")
		md = db.variableLoad(well, ds, db.referenceName(well, ds))
		list_md = []																										#поиск самой длинной ГК в датасете ГС
		list_var = []
		for var in db.variableList(well, ds):
			if "Gamma" in db.variableFamily(well, ds, var):
				ind = int(db.variableInformation(well, ds,var, "BottomIndex"))
				list_md.append(md[ind])
				list_var.append(var)
				dict_gr = dict(zip(list_md, list_var))
				max_key =max(dict_gr.keys())
				var_gr_max = dict_gr[max_key] 																#поиск названия переменной с максимальной длинной по стволу
				print(well, var_gr_max, max_key, "m", "max_depth is", md[-1])
				for var_delete in list_var:
					if var_delete != var_gr_max:
						db.variableDelete(well, ds, var_delete)
				db.variableFamilyChange(well, ds, var_gr_max, "Gamma Ray")
				db.variableUnitChange(well, ds, var_gr_max, "gapi")
				db.variableRename(well, ds, var_gr_max, 'GR')
		#if  db.variableExists(well, ds, var + '_orig'):													#дублирование самой длинной ГК из списка
			#pass
		#else:
			#db.variableDuplicate(well, ds, var, var + "_orig") 
			#db.variableFamilyChange(well, ds, var, "Gamma Ray")
			#db.variableUnitChange(well, ds, var, "gapi")
		for var in db.variableList(well, ds):																	#поиск и переименование переменных малого и большого зондов УЭС
			if "Shallow Resistivity" in db.variableFamily(well, ds, var):
				db.variableDuplicate(well, ds, var, "RT_SH")
				print(well, var, "is renamed")
				db.variableFamilyChange(well, ds, "RT_SH", 'Shallow Resistivity Hrz')
			if "Deep Resistivity" in db.variableFamily(well, ds, var):
				db.variableDuplicate(well, ds, var, "RT_DP")
				print(well, var, "is renamed")
				db.variableFamilyChange(well, ds, "RT_DP", 'Deep Resistivity Hrz')
