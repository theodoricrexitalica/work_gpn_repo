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
__date__ = """2022-03-23"""
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
db.currentChange('project')
well_name = []
ngt_name = []
for well in db.wellList():																							#Чтение имени NGT в датасете скважины и формирование списков
	ds_wi = 'wellinfo'
	var_wi = 'well_ngt'
	if db.datasetExists(well, ds_wi):
		ngt_name_var= db.variableLoad(well, ds_wi, var_wi)
		well_name.append(well)
		ngt_name.append(ngt_name_var[0])
dict_wells = dict(zip(ngt_name, well_name))															#Создание словаря из 2х списков

db.currentChange('import')
for well_imported in db.wellList():
	for well_ngt in dict_wells:																						#Поиск совпадения ключей словаря со названиями скважин в импорте
		if well_ngt == well_imported:
			print(well_ngt, dict_wells[well_ngt])
			db.wellRename(well_ngt, dict_wells[well_ngt])
